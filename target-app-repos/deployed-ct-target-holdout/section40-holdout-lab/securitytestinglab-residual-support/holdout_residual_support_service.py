from __future__ import annotations

import argparse
import base64
import hashlib
import http.server
import json
import os
import secrets
import socketserver
import struct
import threading
from http import HTTPStatus
from typing import Any


STATE: dict[str, Any] = {"captcha": {}, "workflow": {}, "events": []}
LOCK = threading.Lock()


def reset_state() -> None:
    with LOCK:
        STATE["captcha"] = {}
        STATE["workflow"] = {}
        STATE["events"] = []


def response(status: str, extra: dict[str, Any] | None = None) -> bytes:
    body = {"status": status, **(extra or {})}
    return json.dumps(body, sort_keys=True).encode()


def websocket_accept(key: str) -> str:
    magic = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
    return base64.b64encode(hashlib.sha1((key + magic).encode()).digest()).decode()


def read_ws_frame(sock) -> bytes:
    header = sock.recv(2)
    if len(header) < 2:
        return b""
    length = header[1] & 0x7F
    if length == 126:
        length = struct.unpack("!H", sock.recv(2))[0]
    elif length == 127:
        length = struct.unpack("!Q", sock.recv(8))[0]
    mask = sock.recv(4)
    data = sock.recv(length)
    return bytes(byte ^ mask[index % 4] for index, byte in enumerate(data))


def write_ws_frame(sock, payload: bytes) -> None:
    header = bytearray([0x81])
    length = len(payload)
    if length < 126:
        header.append(length)
    elif length < 65536:
        header.append(126)
        header.extend(struct.pack("!H", length))
    else:
        header.append(127)
        header.extend(struct.pack("!Q", length))
    sock.sendall(bytes(header) + payload)


class Handler(http.server.BaseHTTPRequestHandler):
    server_version = "SecurityTestingLabHoldoutResidualSupport/1"

    def log_message(self, format: str, *args: Any) -> None:  # noqa: A002
        return

    def send_json(self, status_code: int, payload: bytes) -> None:
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self) -> None:
        if self.path == "/health":
            self.send_json(HTTPStatus.OK, response("ok", {"service": "holdout_residual_support"}))
            return
        if self.path == "/captcha/challenge":
            challenge_id = secrets.token_hex(8)
            answer = secrets.token_hex(3)
            with LOCK:
                STATE["captcha"][challenge_id] = answer
            payload = response("challenge_issued", {"challenge_id": challenge_id, "answer_sha256": hashlib.sha256(answer.encode()).hexdigest()})
            self.send_json(HTTPStatus.OK, payload)
            return
        if self.path == "/ws-business" and self.headers.get("Upgrade", "").lower() == "websocket":
            key = self.headers.get("Sec-WebSocket-Key", "")
            self.send_response(HTTPStatus.SWITCHING_PROTOCOLS)
            self.send_header("Upgrade", "websocket")
            self.send_header("Connection", "Upgrade")
            self.send_header("Sec-WebSocket-Accept", websocket_accept(key))
            self.end_headers()
            payload = read_ws_frame(self.connection)
            try:
                message = json.loads(payload.decode())
            except Exception:
                write_ws_frame(self.connection, response("invalid_json"))
                return
            principal = str(message.get("principal_alias", ""))
            action = str(message.get("action", ""))
            object_ref = str(message.get("object_ref", "shared"))
            with LOCK:
                principal_state = STATE["workflow"].setdefault(principal, set())
                if action == "reserve":
                    principal_state.add(object_ref)
                    result = "reserved"
                elif action == "check":
                    result = "owned" if object_ref in principal_state else "not_owned"
                else:
                    result = "unknown_action"
                STATE["events"].append({"principal_hash": hashlib.sha256(principal.encode()).hexdigest()[:16], "action": action, "result": result})
            write_ws_frame(self.connection, response(result, {"principal_hash": hashlib.sha256(principal.encode()).hexdigest()[:16]}))
            return
        self.send_json(HTTPStatus.NOT_FOUND, response("not_found"))

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length) if length else b""
        if self.path == "/reset":
            reset_state()
            self.send_json(HTTPStatus.OK, response("reset"))
            return
        if self.path == "/captcha/verify":
            try:
                data = json.loads(body.decode())
            except Exception:
                self.send_json(HTTPStatus.BAD_REQUEST, response("invalid_json"))
                return
            challenge_id = str(data.get("challenge_id", ""))
            answer = str(data.get("answer", ""))
            with LOCK:
                expected = STATE["captcha"].get(challenge_id)
            if expected and secrets.compare_digest(expected, answer):
                self.send_json(HTTPStatus.OK, response("captcha_pass"))
            else:
                self.send_json(HTTPStatus.FORBIDDEN, response("captcha_fail"))
            return
        self.send_json(HTTPStatus.NOT_FOUND, response("not_found"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=18082)
    args = parser.parse_args()
    reset_state()
    with socketserver.ThreadingTCPServer((args.host, args.port), Handler) as server:
        server.allow_reuse_address = True
        server.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
