# vulnerable WordPress plugin lab

Runtime URL: http://10.190.190.96:18165/
Runtime host: ct-target-legacy-web-zoo
Source reference: target-app-repos/vulnerable-wordpress
Docker asset: docker-images/security-testing-lab/bundles/additional-cms-heavy-targets.yml
Compose reference: bundles/additional-cms-heavy-targets.yml
Compose service: vulnerable-wordpress
Default port: 18165
Internal port: 80
Credential ref: none
Status: containerized

Notes: Built from copied deployed source overlay.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh vulnerable-wordpress
```
