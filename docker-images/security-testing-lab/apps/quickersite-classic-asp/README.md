# QuickerSite Classic ASP health

Runtime URL: http://10.190.190.98:18097/ct-health.asp
Runtime host: ct-target-classic-asp
Source reference: target-app-repos/classic-asp-quickersite
Docker asset: none
Compose reference: none
Compose service: none
Default port: 18097
Internal port: 80
Credential ref: secret/runtime-targets/classic-asp/administrator-password
Status: skipped_windows

Notes: Windows Server IIS Classic ASP target. Not containerized per goal constraint.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh quickersite-classic-asp
```
