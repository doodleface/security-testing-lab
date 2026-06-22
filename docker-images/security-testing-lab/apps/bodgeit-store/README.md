# BodgeIt Store

Runtime URL: http://10.190.190.91:18157/bodgeit/
Runtime host: ct-target-dvwa
Source reference: target-app-repos/deployed-ct-target-dvwa/securitytestinglab-targets/dvwa-additional/bodgeit
Docker asset: docker-images/security-testing-lab/bundles/ct-target-dvwa-additional/additional-dvwa-original-targets.yml
Compose reference: bundles/ct-target-dvwa-additional/additional-dvwa-original-targets.yml
Compose service: bodgeit-store
Default port: 18157
Internal port: 8080
Credential ref: none
Status: containerized

Notes: Built from copied deployed source overlay.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh bodgeit-store
```
