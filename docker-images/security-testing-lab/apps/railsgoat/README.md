# RailsGoat

Runtime URL: http://10.190.190.96:3001/
Runtime host: ct-target-legacy-web-zoo
Source reference: target-app-repos/railsgoat
Docker asset: docker-images/security-testing-lab/bundles/legacy-web-zoo.yml
Compose reference: bundles/legacy-web-zoo.yml
Compose service: railsgoat
Default port: 3001
Internal port: 3000
Credential ref: secret/runtime-targets/railsgoat/reviewer
Status: containerized

Notes: Uses owasp/railsgoat image in current lab compose.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh railsgoat
```
