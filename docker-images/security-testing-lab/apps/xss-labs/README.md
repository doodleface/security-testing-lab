# XSS-Labs

Runtime URL: http://10.190.190.91:18154/
Runtime host: ct-target-dvwa
Source reference: target-app-repos/deployed-ct-target-dvwa/securitytestinglab-targets/dvwa-additional/xss-labs
Docker asset: docker-images/security-testing-lab/bundles/additional-dvwa-original-targets.yml
Compose reference: bundles/additional-dvwa-original-targets.yml
Compose service: xss-labs
Default port: 18154
Internal port: 80
Credential ref: none
Status: containerized

Notes: Built from copied deployed source overlay.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh xss-labs
```
