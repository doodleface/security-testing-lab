# OWASP Juice Shop

Runtime URL: http://10.190.190.92:3000/
Runtime host: ct-target-appsuite
Source reference: target-app-repos/juice-shop
Docker asset: docker-images/security-testing-lab/bundles/runtime-targets/appsuite.yml
Compose reference: bundles/runtime-targets/appsuite.yml
Compose service: juice-shop
Default port: 3000
Internal port: 3000
Credential ref: secret/runtime-targets/juice-shop/operator
Status: containerized

Notes: Uses upstream bkimminich/juice-shop image and local source mirror where available.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh juice-shop
```
