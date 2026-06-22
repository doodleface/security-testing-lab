# crAPI MailHog

Runtime URL: http://10.190.190.95:8025/
Runtime host: ct-target-holdout
Source reference: target-app-repos/deployed-ct-target-holdout/section40-holdout-lab
Docker asset: docker-images/security-testing-lab/bundles/crapi-compose.yml
Compose reference: bundles/crapi-compose.yml
Compose service: mailhog
Default port: 8025
Internal port: 8025
Credential ref: none
Status: containerized

Notes: Auxiliary mailbox for crAPI workflows.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh crapi-mailhog
```
