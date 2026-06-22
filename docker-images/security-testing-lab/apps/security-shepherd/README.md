# Security Shepherd

Runtime URL: https://10.190.190.96:18131/login.jsp
Runtime host: ct-target-legacy-web-zoo
Source reference: target-app-repos/security-shepherd
Docker asset: docker-images/security-testing-lab/bundles/additional-enterprise-cms-targets.yml
Compose reference: bundles/additional-enterprise-cms-targets.yml
Compose service: security-shepherd
Default port: 18131
Internal port: 8443
Credential ref: none
Status: containerized

Notes: Requires generated DB and keystore passwords in deployment environment.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh security-shepherd
```
