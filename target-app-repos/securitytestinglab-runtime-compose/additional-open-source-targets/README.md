# Additional Open Source Target Deployment Bundle

Prepared source-cache and compose bundle for adding these authorized lab targets without committing plaintext target credentials.

Source copies are retained under `/home/dev/securitytestinglab/target-app-repos/`:

- `wrongsecrets` from OWASP WrongSecrets
- `vapi` from roottusk/vapi
- `django-nv` from nVisium/django.nV
- `vulpy` from fportantier/vulpy
- `security-shepherd` from OWASP/SecurityShepherd
- `dvwp` from vavkamil/dvwp

Prepared target compose overlays:

- `deployed-ct-target-legacy-web-zoo/securitytestinglab-targets/legacy-web-zoo/additional-enterprise-cms-targets.yml`
- `deployed-ct-target-holdout/section40-holdout-lab/additional-api-targets.yml`
- `deployed-ct-target-node-zoo/securitytestinglab-targets/node-zoo/additional-python-targets.yml`

Target-local `.env` files must provide only deployment-local secret values. Do not commit those values.
