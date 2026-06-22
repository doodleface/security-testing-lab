#!/usr/bin/env python3
from __future__ import annotations
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
APP_ID = 'cors-jwt-header-misconfig-lab'
APP_NAME = 'CORS JWT Header Misconfiguration Lab'
COVERAGE = 'Deterministic CORS, JWT, CSP, HSTS, security-header, and auth-boundary misconfiguration variants.'
ENDPOINTS = [('/', 'CORS JWT header lab'), ('/cors/open', 'CORS open shape'), ('/jwt/none', 'JWT none-alg shape'), ('/headers/missing', 'Missing headers'), ('/auth/boundary', 'Auth boundary shape')]
ENDPOINT_MAP = dict(ENDPOINTS)
class Handler(BaseHTTPRequestHandler):
    server_version = "SecurityTestingLabLab/1.0"
    def log_message(self, fmt, *args):
        return
    def _send(self, status, content_type, body, headers=None):
        data = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("X-SecurityTestingLab-Lab", APP_ID)
        if headers:
            for key, value in headers.items():
                self.send_header(key, value)
        self.end_headers()
        self.wfile.write(data)
    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/healthz":
            self._send(200, "application/json", json.dumps({"status":"ok","app_id":APP_ID}))
            return
        if path in {"/openapi.json", "/.well-known/openid-configuration", "/jwks", "/schema"}:
            self._send(200, "application/json", json.dumps({"app_id":APP_ID,"name":APP_NAME,"coverage":COVERAGE,"paths":[p for p,_ in ENDPOINTS]}, sort_keys=True))
            return
        if path == "/graphql":
            self._send(200, "application/json", json.dumps({"data":{"__typename":"SecurityTestingLabGraphQLLab"},"extensions":{"lab":APP_ID}}))
            return
        if path == "/cors/open":
            self._send(200, "application/json", json.dumps({"cors":"open-shape","raw_sensitive_material_retained":False}), {"Access-Control-Allow-Origin":"*","Access-Control-Allow-Credentials":"true"})
            return
        if path == "/headers/missing":
            self._send(200, "text/html", "<html><title>Missing security header shape</title><body>header fixture</body></html>")
            return
        prefixes = tuple(p.rstrip('/') + '/' for p,_ in ENDPOINTS if p != '/')
        if path in ENDPOINT_MAP or (prefixes and path.startswith(prefixes)):
            self._send(200, "text/html", f"<html><title>{APP_NAME}</title><body><h1>{APP_NAME}</h1><p>{COVERAGE}</p><p>Endpoint: {path}</p></body></html>")
            return
        self._send(404, "application/json", json.dumps({"error":"not_found","app_id":APP_ID}))
def main():
    port = int(os.environ.get("PORT", "8080"))
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
if __name__ == "__main__":
    main()
