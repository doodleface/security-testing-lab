# Vulnado

Runtime URL: http://10.190.190.91:18159/cowsay
Runtime host: ct-target-dvwa
Source reference: target-app-repos/deployed-ct-target-dvwa/securitytestinglab-targets/dvwa-additional/vulnado
Docker asset: docker-images/security-testing-lab/bundles/ct-target-dvwa-additional/additional-dvwa-original-targets.yml
Compose reference: bundles/ct-target-dvwa-additional/additional-dvwa-original-targets.yml
Compose service: vulnado
Default port: 18159
Internal port: 8080
Credential ref: none
Status: containerized

Notes: Requires local VULNADO_POSTGRES_PASSWORD in deployment environment.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh vulnado
```
