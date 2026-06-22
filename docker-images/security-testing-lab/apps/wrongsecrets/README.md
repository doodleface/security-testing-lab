# WrongSecrets

Runtime URL: http://10.190.190.96:18120/
Runtime host: ct-target-legacy-web-zoo
Source reference: target-app-repos/wrongsecrets
Docker asset: docker-images/security-testing-lab/bundles/additional-enterprise-cms-targets.yml
Compose reference: bundles/additional-enterprise-cms-targets.yml
Compose service: wrongsecrets
Default port: 18120
Internal port: 8080
Credential ref: none
Status: containerized

Notes: Uses jeroenwillemsen/wrongsecrets image.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh wrongsecrets
```
