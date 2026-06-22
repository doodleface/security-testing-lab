# Auth-boundary REST lab

Runtime URL: http://10.190.190.95:18080/api/items
Runtime host: ct-target-holdout
Source reference: generated compatible fixture because target-local source was unavailable noninteractively
Docker asset: docker-images/security-testing-lab/bundles/auth-boundary-lab/docker-compose.yml
Compose reference: bundles/auth-boundary-lab/docker-compose.yml
Compose service: auth-boundary-lab
Default port: 18080
Internal port: 8080
Credential ref: secret/runtime-targets/auth-boundary-lab/principal-alpha-token
Status: containerized

Notes: Generated compatible support-service context. Source parity with target-local service is not claimed.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh auth-boundary-rest
```
