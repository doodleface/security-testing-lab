# vAPI

Runtime URL: http://10.190.190.95:18122/
Runtime host: ct-target-holdout
Source reference: target-app-repos/deployed-ct-target-holdout/section40-holdout-lab/vapi
Docker asset: docker-images/security-testing-lab/bundles/additional-api-targets.yml
Compose reference: bundles/additional-api-targets.yml
Compose service: vapi
Default port: 18122
Internal port: 80
Credential ref: none
Status: containerized

Notes: Requires generated target-local database credentials.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh vapi
```
