# Mutillidae II

Runtime URL: http://10.190.190.96:8085/
Runtime host: ct-target-legacy-web-zoo
Source reference: target-app-repos/mutillidae
Docker asset: docker-images/security-testing-lab/bundles/legacy-web-zoo.yml
Compose reference: bundles/legacy-web-zoo.yml
Compose service: mutillidae
Default port: 8085
Internal port: 80
Credential ref: secret/runtime-targets/mutillidae/reviewer
Status: containerized

Notes: Uses webpwnized Mutillidae images with database service.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh mutillidae-ii
```
