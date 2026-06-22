# DVGA holdout

Runtime URL: http://10.190.190.95:5013/
Runtime host: ct-target-holdout
Source reference: target-app-repos/dvga
Docker asset: docker-images/security-testing-lab/bundles/ct-target-holdout/section40-holdout-apps.yml
Compose reference: bundles/ct-target-holdout/section40-holdout-apps.yml
Compose service: dvga-holdout
Default port: 5013
Internal port: 5013
Credential ref: secret/runtime-targets/dvga-holdout/reviewer
Status: containerized

Notes: Uses upstream DVGA image.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh dvga-holdout
```
