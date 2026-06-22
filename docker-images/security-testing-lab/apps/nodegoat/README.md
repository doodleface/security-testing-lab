# NodeGoat

Runtime URL: http://10.190.190.97:4000/
Runtime host: ct-target-node-zoo
Source reference: target-app-repos/deployed-ct-target-node-zoo/securitytestinglab-targets/node-zoo/nodegoat
Docker asset: docker-images/security-testing-lab/bundles/ct-target-node-zoo/docker-compose.yml
Compose reference: bundles/ct-target-node-zoo/docker-compose.yml
Compose service: nodegoat
Default port: 4000
Internal port: 4000
Credential ref: secret/runtime-targets/nodegoat/reviewer
Status: containerized

Notes: Built from copied deployed source overlay with MongoDB dependency.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh nodegoat
```
