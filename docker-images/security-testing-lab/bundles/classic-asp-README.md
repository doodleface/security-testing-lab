# ct-target-classic-asp Windows Container Bundle

This bundle contains fixed source contexts for the two ASP VBScript CMS targets:

- `asp-vbscript-cms` -> `securitytestinglab/asp-vbscript-cms:local`, published on `18098:80`
- `asp-vbscript-cms-patched` -> `securitytestinglab/asp-vbscript-cms-patched:local`, published on `18100:80`

Both images are Windows IIS Classic ASP images and require a Windows container builder/runtime.

Build from a Windows Docker host:

```powershell
cd docker-images\security-testing-lab
docker compose -f bundles\ct-target-classic-asp\docker-compose.yml build asp-vbscript-cms
docker compose -f bundles\ct-target-classic-asp\docker-compose.yml build asp-vbscript-cms-patched
```

Run from a Windows Docker host:

```powershell
docker compose -f bundles\ct-target-classic-asp\docker-compose.yml up -d
```

The authoritative Linux Docker daemon reports `OSType=linux` and cannot build these images because the Windows Dockerfile must run `powershell`/`dism` inside a Windows container layer to enable Classic ASP and configure IIS.
