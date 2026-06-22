# DVWP WordPress

Runtime URL: http://10.190.190.96:18140/
Runtime host: ct-target-legacy-web-zoo
Source reference: target-app-repos/dvwp
Docker asset: docker-images/security-testing-lab/bundles/additional-enterprise-cms-targets.yml
Compose reference: bundles/additional-enterprise-cms-targets.yml
Compose service: dvwp-wordpress
Default port: 18140
Internal port: 80
Credential ref: none
Status: containerized

Notes: Requires generated target-local database password.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh dvwp-wordpress
```
