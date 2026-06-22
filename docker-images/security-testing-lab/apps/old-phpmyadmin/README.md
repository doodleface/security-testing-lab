# old phpMyAdmin

Runtime URL: http://10.190.190.96:18162/
Runtime host: ct-target-legacy-web-zoo
Source reference: target-app-repos/phpmyadmin
Docker asset: docker-images/security-testing-lab/bundles/additional-cms-heavy-targets.yml
Compose reference: bundles/additional-cms-heavy-targets.yml
Compose service: old-phpmyadmin
Default port: 18162
Internal port: 80
Credential ref: none
Status: containerized

Notes: Uses phpmyadmin/phpmyadmin 4.8 with MySQL 5.7.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh old-phpmyadmin
```
