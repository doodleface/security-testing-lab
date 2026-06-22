# crAPI

Runtime URL: http://10.190.190.95:8888/
Runtime host: ct-target-holdout
Source reference: target-app-repos/deployed-ct-target-holdout/section40-holdout-lab
Docker asset: docker-images/security-testing-lab/bundles/ct-target-holdout/crapi-compose.yml
Compose reference: bundles/ct-target-holdout/crapi-compose.yml
Compose service: crapi-web
Default port: 8888
Internal port: 80
Credential ref: secret/runtime-targets/crapi/operator
Status: containerized

Notes: crAPI is multi-service and Compose starts required dependencies.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh crapi
```
