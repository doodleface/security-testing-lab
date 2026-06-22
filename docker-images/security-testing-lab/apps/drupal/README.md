# Drupal

Runtime URL: http://10.190.190.95:18164/
Runtime host: ct-target-holdout
Source reference: target-app-repos/drupal
Docker asset: docker-images/security-testing-lab/bundles/additional-heavy-apps.yml
Compose reference: bundles/additional-heavy-apps.yml
Compose service: drupal-vuln
Default port: 18164
Internal port: 80
Credential ref: none
Status: containerized

Notes: Requires generated target-local database credentials.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh drupal
```
