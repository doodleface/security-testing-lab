# DVGA

Runtime URL: http://10.190.190.93:5013/
Runtime host: ct-target-graphql
Source reference: target-app-repos/dvga
Docker asset: docker-images/security-testing-lab/bundles/runtime-targets/graphql.yml
Compose reference: bundles/runtime-targets/graphql.yml
Compose service: dvga
Default port: 5013
Internal port: 5013
Credential ref: secret/runtime-targets/dvga/reviewer
Status: containerized

Notes: Uses upstream dolevf/dvga image and local source mirror where available.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh dvga
```
