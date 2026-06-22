# source-matched BenchmarkJava

Runtime URL: https://10.190.190.96:18443/benchmark/
Runtime host: ct-target-legacy-web-zoo
Source reference: target-app-repos/deployed-ct-target-legacy-web-zoo/securitytestinglab-targets/legacy-web-zoo/benchmarkjava-source-matched
Docker asset: docker-images/security-testing-lab/bundles/legacy-web-zoo.yml
Compose reference: bundles/legacy-web-zoo.yml
Compose service: benchmarkjava
Default port: 18443
Internal port: 8443
Credential ref: none
Status: containerized

Notes: Current source-matched sidecar is deployment-local. Reuses Benchmark image unless the source-matched context is refreshed.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh benchmarkjava-source-matched
```
