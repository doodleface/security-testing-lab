# DVWA

Runtime URL: http://10.190.190.91:8080/
Runtime host: ct-target-dvwa
Source reference: target-app-repos/dvwa
Docker asset: docker-images/security-testing-lab/bundles/runtime-targets/dvwa.yml
Compose reference: bundles/runtime-targets/dvwa.yml
Compose service: dvwa
Default port: 8080
Internal port: 80
Credential ref: secret/runtime-targets/dvwa/admin
Status: containerized

Notes: Uses upstream vulnerables/web-dvwa image and local source mirror where available.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh dvwa
```
