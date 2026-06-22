# ASP VBScript CMS

Runtime URL: http://10.190.190.98:18098/
Runtime host: ct-target-classic-asp
Source reference: target-app-repos/classic-asp-vbscript-cms
Docker asset: docker-images/security-testing-lab/bundles/classic-asp.yml
Compose reference: bundles/classic-asp.yml
Compose service: asp-vbscript-cms
Default port: 18098
Internal port: 80
Credential ref: secret/runtime-targets/classic-asp/administrator-password
Status: containerized

Notes: Fixed Classic ASP/IIS Windows container bundle. Requires a Windows container builder/runtime; live lab remains IIS-hosted on ct-target-classic-asp.

Build or pull from the lab asset root:

```bash
cd docker-images/security-testing-lab
./build-one.sh asp-vbscript-cms
```
