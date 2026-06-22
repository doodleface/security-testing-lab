# OWASP BenchmarkJava

Runtime URL: https://10.190.190.96:8443/benchmark/
Runtime host: ct-target-legacy-web-zoo
Source reference: target-app-repos/benchmarkjava
Docker asset: docker-images/security-testing-lab/bundles/ct-target-legacy-web-zoo/docker-compose.yml
Compose reference: bundles/ct-target-legacy-web-zoo/docker-compose.yml
Compose service: benchmarkjava
Default port: 8443
Internal port: 8443
Credential ref: none
Status: containerized

Notes: Uses owasp/benchmark image.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh benchmarkjava
```
