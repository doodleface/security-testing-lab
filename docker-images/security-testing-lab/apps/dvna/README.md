# DVNA

Runtime URL: http://10.190.190.97:9090/
Runtime host: ct-target-node-zoo
Source reference: target-app-repos/dvna
Docker asset: docker-images/security-testing-lab/bundles/ct-target-node-zoo/docker-compose.yml
Compose reference: bundles/ct-target-node-zoo/docker-compose.yml
Compose service: dvna
Default port: 9090
Internal port: 9090
Credential ref: secret/runtime-targets/dvna/reviewer
Status: containerized

Notes: Uses appsecco/dvna sqlite image.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh dvna
```
