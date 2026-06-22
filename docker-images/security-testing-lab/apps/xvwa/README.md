# XVWA

Runtime URL: http://10.190.190.99:18101/
Runtime host: ct-vulnlab-01
Source reference: target-app-repos/xvwa
Docker asset: docker-images/security-testing-lab/bundles/vulnlab-01.yml
Compose reference: bundles/vulnlab-01.yml
Compose service: xvwa
Default port: 18101
Internal port: 80
Credential ref: none
Status: containerized

Notes: Uses compatible bitnetsecdave/xvwa image because legacy manifest v1 images are unsupported.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh xvwa
```
