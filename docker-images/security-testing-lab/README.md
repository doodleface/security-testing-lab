# SecurityTestingLab Lab Docker Assets

This ignored directory contains generated Docker deployment assets for the current SecurityTestingLab runtime target inventory.

Use `../lab-setup/LabSetup.sh` for interactive deployment, or use `build-one.sh <app_id>` from this directory to build or pull one application context.

The source of truth manifest is `lab-setup/lab-apps.tsv`. Windows-only Classic ASP targets are intentionally excluded from Docker image creation.
