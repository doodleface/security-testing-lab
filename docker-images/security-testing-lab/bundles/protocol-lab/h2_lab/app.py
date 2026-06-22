from __future__ import annotations

from fastapi import FastAPI, Request


app = FastAPI(title="SecurityTestingLab H2 Lab")

INTERNAL_REPORT = {
    "service": "h2-lab",
    "secrets": [
        "internal billing export path: /srv/reports/billing.csv",
        "upstream admin callback token: h2-admin-callback-token",
    ],
}


def effective_path(request: Request) -> str:
    # Intentionally vulnerable: trust client-supplied proxy rewrite headers.
    return (
        request.headers.get("x-original-url")
        or request.headers.get("x-rewrite-url")
        or request.headers.get("x-forwarded-uri")
        or request.url.path
    )


@app.get("/")
async def index() -> dict[str, object]:
    return {
        "service": "h2-lab",
        "notes": [
            "serve this endpoint over TLS so clients can negotiate HTTP/2",
            "proxy rewrite headers are intentionally trusted",
        ],
        "interesting_paths": ["/headers", "/proxy-bypass", "/internal/report", "/delay/5"],
    }


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/headers")
async def headers(request: Request) -> dict[str, object]:
    return {
        "http_version": request.scope.get("http_version", "unknown"),
        "effective_path": effective_path(request),
        "headers": dict(request.headers),
    }


@app.get("/delay/{seconds}")
async def delay(seconds: int, request: Request) -> dict[str, object]:
    capped = max(0, min(seconds, 15))
    return {
        "delay_seconds": capped,
        "http_version": request.scope.get("http_version", "unknown"),
        "message": "use this endpoint to exercise timeout, replay, and long-lived request handling",
    }


@app.get("/internal/report")
async def internal_report() -> dict[str, object]:
    return INTERNAL_REPORT


@app.get("/proxy-bypass")
async def proxy_bypass(request: Request) -> dict[str, object]:
    path = effective_path(request)
    if path == "/internal/report":
        return {
            "warning": "proxy rewrite headers are trusted without validation",
            "effective_path": path,
            "report": INTERNAL_REPORT,
        }
    return {
        "effective_path": path,
        "warning": "set x-original-url, x-rewrite-url, or x-forwarded-uri to /internal/report to demonstrate the flaw",
    }
