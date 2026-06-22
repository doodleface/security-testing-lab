# bWAPP

Runtime URL: http://10.190.190.95:8083/
Runtime host: ct-target-holdout
Source reference: target-app-repos/bwapp
Docker asset: docker-images/security-testing-lab/bundles/section40-holdout-apps.yml
Compose reference: bundles/section40-holdout-apps.yml
Compose service: bwapp
Default port: 8083
Internal port: 80
Credential ref: secret/runtime-targets/bwapp/reviewer
Status: containerized

Notes: Uses current lab image raesene/bwapp.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh bwapp
```
