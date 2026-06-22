# WackoPicko

Runtime URL: http://10.190.190.99:18102/
Runtime host: ct-vulnlab-01
Source reference: target-app-repos/wackopicko
Docker asset: docker-images/security-testing-lab/bundles/vulnlab-01.yml
Compose reference: bundles/vulnlab-01.yml
Compose service: wackopicko
Default port: 18102
Internal port: 80
Credential ref: none
Status: containerized

Notes: Uses adamdoupe/wackopicko image.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh wackopicko
```
