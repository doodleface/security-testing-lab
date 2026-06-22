# Internal OOB callback fixture

Runtime URL: http://10.190.190.99:18116/
Runtime host: ct-vulnlab-01
Source reference: target-app-repos/securitytestinglab-vulnlab-fixtures
Docker asset: docker-images/security-testing-lab/bundles/ct-vulnlab-01/docker-compose.yml
Compose reference: bundles/ct-vulnlab-01/docker-compose.yml
Compose service: oob-callback-fixture
Default port: 18116
Internal port: 8080
Credential ref: none
Status: containerized

Notes: Built from SecurityTestingLab vulnlab fixture source.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh oob-callback-fixture
```
