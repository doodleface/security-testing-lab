# WebGoat

Runtime URL: http://10.190.190.95:8081/WebGoat/
Runtime host: ct-target-holdout
Source reference: target-app-repos/webgoat
Docker asset: docker-images/security-testing-lab/bundles/section40-holdout-apps.yml
Compose reference: bundles/section40-holdout-apps.yml
Compose service: webgoat-webwolf
Default port: 8081
Internal port: 8080
Credential ref: secret/runtime-targets/webgoat/reviewer
Status: containerized

Notes: Same service also exposes WebWolf on 9090.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh webgoat
```
