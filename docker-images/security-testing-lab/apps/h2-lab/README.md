# HTTPS HTTP2 lab

Runtime URL: https://10.190.190.94:9443/
Runtime host: ct-target-protocol-lab
Source reference: tests/fixtures/runtime_targets/protocol_lab/h2_lab
Docker asset: docker-images/security-testing-lab/bundles/protocol-lab/docker-compose.yml
Compose reference: bundles/protocol-lab/docker-compose.yml
Compose service: h2-lab
Default port: 9443
Internal port: 9443
Credential ref: none
Status: containerized

Notes: Requires local cert mount when using TLS like the current lab.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh h2-lab
```
