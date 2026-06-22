# VAmPI

Runtime URL: http://10.190.190.92:5000/
Runtime host: ct-target-appsuite
Source reference: target-app-repos/vampi
Docker asset: docker-images/security-testing-lab/bundles/runtime-targets/appsuite.yml
Compose reference: bundles/runtime-targets/appsuite.yml
Compose service: vampi
Default port: 5000
Internal port: 5000
Credential ref: secret/runtime-targets/vampi/api
Status: containerized

Notes: Run /createdb after first start when using a fresh data store.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh vampi
```
