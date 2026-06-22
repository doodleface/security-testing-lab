# DVWP phpMyAdmin

Runtime URL: http://10.190.190.96:18141/
Runtime host: ct-target-legacy-web-zoo
Source reference: target-app-repos/dvwp
Docker asset: docker-images/security-testing-lab/bundles/ct-target-legacy-web-zoo/additional-enterprise-cms-targets.yml
Compose reference: bundles/ct-target-legacy-web-zoo/additional-enterprise-cms-targets.yml
Compose service: dvwp-phpmyadmin
Default port: 18141
Internal port: 80
Credential ref: none
Status: containerized

Notes: Auxiliary phpMyAdmin service for DVWP.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh dvwp-phpmyadmin
```
