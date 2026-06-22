# Bugzilla

Runtime URL: http://10.190.190.96:18095/
Runtime host: ct-target-legacy-web-zoo
Source reference: target-app-repos/perl-bugzilla
Docker asset: docker-images/security-testing-lab/bundles/ct-target-legacy-web-zoo
Compose reference: bundles/ct-target-legacy-web-zoo/source-review/perl-bugzilla/docker-compose.securitytestinglab.full.yml
Compose service: bugzilla
Default port: 18095
Internal port: 80
Credential ref: secret/runtime-targets/bugzilla/reviewer
Status: containerized

Notes: Source-matched deployment path is copied when present. If compose is absent, rebuild from source cache before deploy.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh bugzilla
```
