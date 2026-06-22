#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
import json, time

APP_ID = 'gitea-devops-lab'
APP_NAME = 'Gitea DevOps Lab'
COVERAGE = 'Git web UI, webhooks, repo permissions, release artifacts, and issue workflow coverage'
ROUTES = {'/': 'overview landing page', '/login': 'role boundary form shape', '/admin': 'admin workflow route', '/api/v1/status': 'JSON API metadata endpoint', '/upload': 'upload workflow route', '/search': 'search/query route', '/health': 'health metadata endpoint', '/org/repo': 'repository UI', '/org/repo/settings/hooks': 'webhook settings', '/api/v1/repos/org/repo/releases': 'release API'}

class Handler(BaseHTTPRequestHandler):
    server_version = "SecurityTestingLabTarget/1.0"
    def log_message(self, fmt, *args):
        return
    def _send(self, status, content_type, body):
        data = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-SecurityTestingLab-App", APP_ID)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)
    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/health":
            self._send(200, "application/json", json.dumps({"app_id": APP_ID, "status": "ok", "timestamp": int(time.time())}, sort_keys=True))
            return
        desc = ROUTES.get(path, "generic application route")
        if path.startswith("/api/") or path.startswith("/ocs/") or path.endswith("/Check") or path.endswith("/GetItem") or path.endswith("/services"):
            self._send(200, "application/json", json.dumps({"app_id": APP_ID, "route": path, "coverage": desc}, sort_keys=True))
            return
        links = "".join(f'<li><a href="{route}">{label}</a></li>' for route, label in sorted(ROUTES.items()))
        html = f"""<!doctype html><html><head><meta charset='utf-8'><title>{APP_NAME}</title></head><body><main><h1>{APP_NAME}</h1><p>{COVERAGE}</p><p>Route: <code>{path}</code></p><p>Coverage point: {desc}</p><ul>{links}</ul><form method='post' action='/workflow'><input name='item' value='demo'><button>submit workflow</button></form></main></body></html>"""
        self._send(200, "text/html", html)
    def do_POST(self):
        self._send(200, "application/json", json.dumps({"app_id": APP_ID, "route": urlparse(self.path).path, "accepted": True}, sort_keys=True))

if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
