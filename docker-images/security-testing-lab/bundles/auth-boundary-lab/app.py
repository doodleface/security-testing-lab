from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def _send(self, status, body, content_type="application/json"):
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path.startswith("/api/items"):
            token = self.headers.get("Authorization", "")
            principal = "beta" if "beta" in token.lower() else "alpha"
            self._send(200, {"items": [{"id": "item-alpha", "owner": principal}], "principal": principal})
            return
        self._send(200, {"service": "securitytestinglab-auth-boundary-lab", "routes": ["/api/items", "/graphql"]})

    def do_POST(self):
        if self.path.startswith("/graphql"):
            self._send(200, {"data": {"viewer": {"id": "principal-alpha"}, "items": [{"id": "item-alpha"}]}})
            return
        self._send(404, {"error": "not found"})

HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
