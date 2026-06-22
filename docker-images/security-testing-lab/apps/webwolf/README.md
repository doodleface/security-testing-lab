# WebWolf

Runtime URL: http://10.190.190.95:9090/WebWolf/
Runtime host: ct-target-holdout
Source reference: target-app-repos/webgoat
Docker asset: docker-images/security-testing-lab/bundles/ct-target-holdout/section40-holdout-apps.yml
Compose reference: bundles/ct-target-holdout/section40-holdout-apps.yml
Compose service: webgoat-webwolf
Default port: 9090
Internal port: 9090
Credential ref: secret/runtime-targets/webwolf/reviewer
Status: containerized

Notes: Auxiliary service exposed by WebGoat container.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh webwolf
```
