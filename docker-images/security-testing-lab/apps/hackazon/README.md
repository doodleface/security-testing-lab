# Hackazon

Runtime URL: http://10.190.190.99:18103/
Runtime host: ct-vulnlab-01
Source reference: target-app-repos/hackazon
Docker asset: docker-images/security-testing-lab/bundles/vulnlab-01.yml
Compose reference: bundles/vulnlab-01.yml
Compose service: hackazon
Default port: 18103
Internal port: 80
Credential ref: none
Status: containerized

Notes: Uses compatible pierrickv/hackazon image.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh hackazon
```
