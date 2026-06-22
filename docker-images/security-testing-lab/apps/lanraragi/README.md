# LANraragi

Runtime URL: http://10.190.190.96:18096/
Runtime host: ct-target-legacy-web-zoo
Source reference: target-app-repos/perl-lanraragi
Docker asset: docker-images/security-testing-lab/bundles/ct-target-legacy-web-zoo
Compose reference: bundles/ct-target-legacy-web-zoo/source-review/perl-lanraragi/docker-compose.securitytestinglab.yml
Compose service: lanraragi
Default port: 18096
Internal port: 3000
Credential ref: secret/runtime-targets/lanraragi/reviewer
Status: containerized

Notes: Source-matched deployment path is copied when present. If compose is absent, rebuild from source cache before deploy.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh lanraragi
```
