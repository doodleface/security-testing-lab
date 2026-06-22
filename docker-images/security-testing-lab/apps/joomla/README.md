# Joomla

Runtime URL: http://10.190.190.96:18163/
Runtime host: ct-target-legacy-web-zoo
Source reference: target-app-repos/joomla-cms
Docker asset: docker-images/security-testing-lab/bundles/ct-target-legacy-web-zoo/additional-cms-heavy-targets.yml
Compose reference: bundles/ct-target-legacy-web-zoo/additional-cms-heavy-targets.yml
Compose service: joomla-vuln
Default port: 18163
Internal port: 80
Credential ref: none
Status: containerized

Notes: Requires generated target-local database password.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh joomla
```
