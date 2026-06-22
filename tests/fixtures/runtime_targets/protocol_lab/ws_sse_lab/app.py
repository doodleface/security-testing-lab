from __future__ import annotations

import asyncio
import json
import time
from collections import defaultdict
from typing import Any

from fastapi import FastAPI, HTTPException, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse, StreamingResponse


app = FastAPI(title="SecurityTestingLab WS/SSE Lab")

TENANT_EVENTS: dict[str, list[dict[str, Any]]] = {
    "tenant-alpha": [
        {"id": "alpha-1", "event": "seed", "message": "alpha payroll export ready"},
        {"id": "alpha-2", "event": "seed", "message": "alpha session token refresh skipped"},
    ],
    "tenant-beta": [
        {"id": "beta-1", "event": "seed", "message": "beta audit export uploaded"},
        {"id": "beta-2", "event": "seed", "message": "beta websocket admin console opened"},
    ],
}
TENANT_QUEUES: dict[str, set[asyncio.Queue[dict[str, Any]]]] = defaultdict(set)
TOKEN_SCOPE = {
    "guest-alpha": {"tenant-alpha"},
    "guest-beta": {"tenant-beta"},
    "auditor": {"tenant-alpha", "tenant-beta"},
}


def advisory_scope(token: str | None) -> list[str]:
    if not token:
        return []
    return sorted(TOKEN_SCOPE.get(token, []))


def insecure_protocol_gate(token: str | None) -> bool:
    # Intentionally weak: any non-empty token grants access to any tenant stream.
    return bool(token)


@app.get("/")
async def index() -> JSONResponse:
    return JSONResponse(
        {
            "service": "ws-sse-lab",
            "vulnerabilities": [
                "cross-tenant websocket subscription",
                "cross-tenant server-sent events subscription",
                "unauthenticated event publication",
            ],
            "example_ws": "/ws/tenant-alpha?token=guest-beta",
            "example_sse": "/events/tenant-beta?token=guest-alpha",
        }
    )


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/tenants/{tenant}/events")
async def list_events(tenant: str) -> dict[str, Any]:
    if tenant not in TENANT_EVENTS:
        raise HTTPException(status_code=404, detail="unknown tenant")
    return {"tenant": tenant, "events": TENANT_EVENTS[tenant]}


@app.post("/publish/{tenant}")
async def publish_event(tenant: str, request: Request) -> dict[str, Any]:
    if tenant not in TENANT_EVENTS:
        raise HTTPException(status_code=404, detail="unknown tenant")
    body = await request.json()
    event = {
        "id": f"{tenant}-{int(time.time() * 1000)}",
        "event": body.get("event", "message"),
        "message": body.get("message", "empty"),
    }
    TENANT_EVENTS[tenant].append(event)
    for queue in list(TENANT_QUEUES[tenant]):
        await queue.put(event)
    return {
        "tenant": tenant,
        "stored": event,
        "warning": "publication endpoint intentionally has no authorization checks",
    }


@app.get("/events/{tenant}")
async def sse_events(tenant: str, token: str | None = None) -> StreamingResponse:
    if tenant not in TENANT_EVENTS:
        raise HTTPException(status_code=404, detail="unknown tenant")
    if not insecure_protocol_gate(token):
        raise HTTPException(status_code=401, detail="token required")

    queue: asyncio.Queue[dict[str, Any]] = asyncio.Queue()
    TENANT_QUEUES[tenant].add(queue)
    snapshot = list(TENANT_EVENTS[tenant])
    claimed_scope = advisory_scope(token)

    async def event_stream() -> Any:
        try:
            for event in snapshot:
                yield (
                    f"id: {event['id']}\n"
                    f"event: {event['event']}\n"
                    f"data: {json.dumps({'tenant': tenant, 'event': event, 'claimed_scope': claimed_scope})}\n\n"
                )
            while True:
                event = await queue.get()
                yield (
                    f"id: {event['id']}\n"
                    f"event: {event['event']}\n"
                    f"data: {json.dumps({'tenant': tenant, 'event': event, 'claimed_scope': claimed_scope})}\n\n"
                )
        finally:
            TENANT_QUEUES[tenant].discard(queue)

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@app.websocket("/ws/{tenant}")
async def websocket_events(websocket: WebSocket, tenant: str) -> None:
    token = websocket.query_params.get("token")
    if tenant not in TENANT_EVENTS:
        await websocket.close(code=4404)
        return
    if not insecure_protocol_gate(token):
        await websocket.close(code=4401)
        return

    await websocket.accept()
    await websocket.send_json(
        {
            "warning": "tenant authorization is intentionally broken",
            "tenant": tenant,
            "claimed_scope": advisory_scope(token),
            "history": TENANT_EVENTS[tenant],
        }
    )
    try:
        while True:
            message = await websocket.receive_text()
            event = {
                "id": f"{tenant}-{int(time.time() * 1000)}",
                "event": "ws-message",
                "message": message,
            }
            TENANT_EVENTS[tenant].append(event)
            for queue in list(TENANT_QUEUES[tenant]):
                await queue.put(event)
            await websocket.send_json({"tenant": tenant, "echo": message, "stored": event})
    except WebSocketDisconnect:
        return
