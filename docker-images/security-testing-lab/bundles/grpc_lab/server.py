from __future__ import annotations

import signal
import threading
import time
from concurrent import futures
from pathlib import Path

import grpc

import protocol_lab_pb2
import protocol_lab_pb2_grpc


ACCOUNT_DATA = {
    ("tenant-alpha", "alice"): {
        "email": "alice@alpha.lab",
        "role": "user",
        "secret_note": "alpha api signing key rotated late",
    },
    ("tenant-beta", "bob"): {
        "email": "bob@beta.lab",
        "role": "admin",
        "secret_note": "beta payroll export path is /exports/beta.csv",
    },
}
TENANT_EVENTS = {
    "tenant-alpha": [
        ("alpha-1", "alpha grpc admin stream opened"),
        ("alpha-2", "alpha backup object copied"),
    ],
    "tenant-beta": [
        ("beta-1", "beta quarterly report approved"),
        ("beta-2", "beta temporary credentials issued"),
    ],
}


class ProtocolLab(protocol_lab_pb2_grpc.ProtocolLabServicer):
    def GetAccount(self, request, context):  # type: ignore[no-untyped-def]
        # Intentionally vulnerable: caller metadata is ignored, so any tenant/user can be requested.
        record = ACCOUNT_DATA.get((request.tenant, request.username))
        if record is None:
          context.abort(grpc.StatusCode.NOT_FOUND, "unknown tenant or user")
        return protocol_lab_pb2.AccountReply(
            tenant=request.tenant,
            username=request.username,
            email=record["email"],
            role=record["role"],
            secret_note=record["secret_note"],
        )

    def StreamTenantEvents(self, request, context):  # type: ignore[no-untyped-def]
        # Intentionally vulnerable: any caller can stream any tenant's events.
        for event_id, message in TENANT_EVENTS.get(request.tenant, []):
            yield protocol_lab_pb2.Event(tenant=request.tenant, id=event_id, message=message)
            time.sleep(0.3)

    def ResetPassword(self, request, context):  # type: ignore[no-untyped-def]
        metadata = dict(context.invocation_metadata())
        role = metadata.get("x-role", "")
        # Intentionally vulnerable: any non-empty x-role is treated as privileged.
        if not role:
            context.abort(grpc.StatusCode.PERMISSION_DENIED, "x-role metadata required")
        return protocol_lab_pb2.ActionReply(
            ok=True,
            detail=(
                f"password for {request.username}@{request.tenant} reset to {request.new_password}; "
                f"accepted x-role={role} without checking privileges"
            ),
        )


def build_server(*, secure: bool) -> grpc.Server:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    protocol_lab_pb2_grpc.add_ProtocolLabServicer_to_server(ProtocolLab(), server)
    if secure:
        cert_dir = Path("/certs")
        private_key = (cert_dir / "server.key").read_bytes()
        certificate_chain = (cert_dir / "server.crt").read_bytes()
        creds = grpc.ssl_server_credentials(((private_key, certificate_chain),))
        server.add_secure_port("[::]:50052", creds)
    else:
        server.add_insecure_port("[::]:50051")
    return server


def main() -> None:
    insecure_server = build_server(secure=False)
    secure_server = build_server(secure=True)
    insecure_server.start()
    secure_server.start()

    stop_event = threading.Event()

    def handle_signal(signum, _frame) -> None:  # type: ignore[no-untyped-def]
        stop_event.set()

    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGINT, handle_signal)
    stop_event.wait()
    insecure_server.stop(0)
    secure_server.stop(0)


if __name__ == "__main__":
    main()
