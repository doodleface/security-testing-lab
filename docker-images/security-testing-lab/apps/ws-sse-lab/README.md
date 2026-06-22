# WebSocket SSE HTTP lab

Runtime URL: http://10.190.190.94:8082/
Runtime host: ct-target-protocol-lab
Source reference: tests/fixtures/runtime_targets/protocol_lab/ws_sse_lab
Docker asset: docker-images/security-testing-lab/bundles/protocol-lab.yml
Compose reference: bundles/protocol-lab.yml
Compose service: ws-sse-lab
Default port: 8082
Internal port: 8082
Credential ref: secret/runtime-targets/protocol-lab/ws-tenant-alpha
Status: containerized

Notes: Built from repository protocol fixture source.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh ws-sse-lab
```
