# Vulpy

Runtime URL: http://10.190.190.97:18124/
Runtime host: ct-target-node-zoo
Source reference: target-app-repos/deployed-ct-target-node-zoo/securitytestinglab-targets/node-zoo/vulpy
Docker asset: docker-images/security-testing-lab/bundles/ct-target-node-zoo/additional-python-targets.yml
Compose reference: bundles/ct-target-node-zoo/additional-python-targets.yml
Compose service: vulpy
Default port: 18124
Internal port: 5000
Credential ref: none
Status: containerized

Notes: Built from copied deployed source overlay.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh vulpy
```
