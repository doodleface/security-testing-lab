# Cache deception fixture

Runtime URL: http://10.190.190.99:18112/
Runtime host: ct-vulnlab-01
Source reference: target-app-repos/securitytestinglab-vulnlab-fixtures
Docker asset: docker-images/security-testing-lab/bundles/ct-vulnlab-01/docker-compose.yml
Compose reference: bundles/ct-vulnlab-01/docker-compose.yml
Compose service: cache-varnish
Default port: 18112
Internal port: 80
Credential ref: none
Status: containerized

Notes: Uses Varnish front end and fixture origin service.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh cache-deception-fixture
```
