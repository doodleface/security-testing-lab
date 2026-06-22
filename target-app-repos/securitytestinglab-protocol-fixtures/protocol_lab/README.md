# Protocol Vulnerability Lab

This fixture set provides small intentionally vulnerable protocol services for the optional 4th runtime-target VM.

It is designed to give SecurityTestingLab deterministic protocol targets for:

1. WebSocket cross-tenant subscription testing
2. SSE unauthorized subscription testing
3. gRPC cross-tenant data exposure and weak method authorization
4. HTTP/2-over-TLS validation plus proxy/header-trust abuse scenarios

These services are intentionally simple. They are not a full production-realistic exploit lab for HTTP/2 desync or advanced protocol smuggling, but they are good development targets for the protocol workers.
