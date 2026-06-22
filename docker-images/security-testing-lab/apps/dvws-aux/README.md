# DVWS auxiliary HTTP

Runtime URL: http://10.190.190.95:8084/
Runtime host: ct-target-holdout
Source reference: target-app-repos/dvws
Docker asset: docker-images/security-testing-lab/bundles/section40-holdout-apps.yml
Compose reference: bundles/section40-holdout-apps.yml
Compose service: dvws
Default port: 8084
Internal port: 8080
Credential ref: secret/runtime-targets/dvws/reviewer
Status: containerized

Notes: Auxiliary WebSocket service port for DVWS.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh dvws-aux
```
