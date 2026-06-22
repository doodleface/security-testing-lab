# DVWS

Runtime URL: http://10.190.190.95:8082/
Runtime host: ct-target-holdout
Source reference: target-app-repos/dvws
Docker asset: docker-images/security-testing-lab/bundles/ct-target-holdout/section40-holdout-apps.yml
Compose reference: bundles/ct-target-holdout/section40-holdout-apps.yml
Compose service: dvws
Default port: 8082
Internal port: 80
Credential ref: secret/runtime-targets/dvws/reviewer
Status: containerized

Notes: Same service also exposes auxiliary WebSocket HTTP port 8084.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh dvws
```
