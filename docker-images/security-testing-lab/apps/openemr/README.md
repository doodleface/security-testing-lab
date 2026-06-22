# OpenEMR

Runtime URL: http://10.190.190.95:18160/
Runtime host: ct-target-holdout
Source reference: target-app-repos/openemr
Docker asset: docker-images/security-testing-lab/bundles/additional-heavy-apps.yml
Compose reference: bundles/additional-heavy-apps.yml
Compose service: openemr-vuln
Default port: 18160
Internal port: 80
Credential ref: none
Status: containerized

Notes: Heavy app. Review upstream setup prompts after first boot.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh openemr
```
