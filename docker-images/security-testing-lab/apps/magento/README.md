# Magento

Runtime URL: http://10.190.190.95:18161/
Runtime host: ct-target-holdout
Source reference: target-app-repos/magento2
Docker asset: docker-images/security-testing-lab/bundles/additional-heavy-apps.yml
Compose reference: bundles/additional-heavy-apps.yml
Compose service: magento-old
Default port: 18161
Internal port: 80
Credential ref: none
Status: containerized

Notes: Heavy app. Requires substantial disk and memory.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh magento
```
