# AppSec Range Orchestrator

`appsec-range-orchestrator` is a private web application security practice range for deploying intentionally vulnerable applications, API labs, source-backed fixtures, and Windows/IIS targets across Linux Docker hosts and Windows Server hosts.

The project is intended for web app penetration testing practice, scanner validation, training, source/runtime comparison, and repeatable AppSec lab exercises.

## Safety Notice

This repository deploys intentionally vulnerable applications. Run it only in an isolated lab network that you own or are explicitly authorized to use.

Do not expose these services to the public Internet. Many included apps intentionally contain default credentials, unsafe dependencies, missing authentication, injection paths, broken access controls, weak crypto, vulnerable upload flows, or other exploitable behavior.

## Licensing

The orchestration scripts and manifests authored for this project are licensed under GPLv3. See `lab-setup/LICENSE`.

Bundled vulnerable applications, cached source repositories, Docker images, and copied build contexts retain their upstream licenses. This private repository includes those materials for internal lab deployment. If this repository is ever made public, review every third-party source tree, Docker context, image reference, and notice file before publication.

## What This Provides

The setup tooling helps an operator:

1. Select vulnerable applications from a manifest.
2. Estimate combined CPU, memory, and disk requirements.
3. Prompt for destination SSH targets without storing passwords.
4. Check remote Docker Compose availability for Linux targets.
5. Detect common host-port conflicts and choose the next available port.
6. Sync Docker assets to a destination host.
7. Start selected applications with Docker Compose.
8. Package selected Windows/IIS source targets and invoke a PowerShell installer on Windows Server 2019/2022 hosts.

## Repository Layout

The standalone private repository is expected to contain the orchestration scripts, manifests, source caches, and Docker build/deployment assets together:

```text
.
├── lab-setup/
│   ├── LabSetup.sh
│   ├── Install-WindowsIisTargets.ps1
│   ├── lab-apps.tsv
│   ├── windows-iis-apps.tsv
│   ├── server-sizing-reference.tsv
│   ├── LICENSE
│   └── README.md
├── docker-images/
│   └── security-testing-lab/
│       ├── bundles/
│       ├── build-one.sh
│       └── manifest.tsv
└── target-app-repos/
    └── cached source repositories and source-backed fixtures
```

## Requirements

Local operator machine:

1. Bash 4 or newer.
2. `ssh` and `scp`.
3. `sshpass` is optional. If it is missing and you enter a password, SSH/SCP may prompt interactively.
4. Access to `docker-images/security-testing-lab/` for Linux deployments.

Linux destination hosts:

1. SSH access.
2. Docker Engine.
3. Docker Compose plugin or legacy `docker-compose`.
4. Enough CPU, memory, and disk for selected applications.
5. Lab-only firewall/routing rules that prevent accidental public exposure.

Windows destination hosts:

1. Windows Server 2019 or 2022.
2. SSH access to Windows.
3. Windows PowerShell.
4. IIS and application-specific prerequisites listed in `windows-iis-apps.tsv`.
5. Local source caches under `target-app-repos/`, or public fallback repositories when the installer supports fallback cloning.

## Quick Start: Linux Docker Labs

Run from the repository root:

```bash
bash lab-setup/LabSetup.sh
```

Equivalent explicit mode:

```bash
bash lab-setup/LabSetup.sh --linux
```

The script will:

1. Load `lab-setup/lab-apps.tsv`.
2. Show applications with status `containerized`.
3. Prompt for app selections by number, app ID, or `all`.
4. Sum estimated capacity needs.
5. Prompt for destination servers as `user@host` or `host`.
6. Prompt for SSH passwords in memory only, or use SSH keys.
7. Check Docker Compose availability on each destination.
8. Sync `docker-images/security-testing-lab/` to `~/security-testing-lab` on each destination.
9. Start selected services through Docker Compose.

## Quick Start: Windows/IIS Labs

Run from the repository root:

```bash
bash lab-setup/LabSetup.sh --windows-iis
```

The script will:

1. Load `lab-setup/windows-iis-apps.tsv`.
2. Show applications with status `windows-iis`.
3. Package selected local source caches when present.
4. Verify the remote host reports Windows Server 2019/2022.
5. Copy the package to the remote staging directory.
6. Run `Install-WindowsIisTargets.ps1` with selected app IDs.

## Manifest Format

`lab-apps.tsv` is tab-separated. The current fields are:

| Field | Meaning |
| --- | --- |
| `app_id` | Stable application ID used by the script. |
| `application` | Human-readable application name. |
| `runtime_host` | Recommended or current lab host label. |
| `runtime_url` | Expected application URL. |
| `source_ref` | Local source cache or source/build context reference. |
| `docker_asset` | Source-side Docker asset path. |
| `compose_ref` | Compose file path relative to synced `security-testing-lab/`. |
| `service` | Compose service to start. |
| `default_port` | Preferred host port. |
| `internal_port` | Container/service port. |
| `credential_ref` | Secret reference label, not a raw credential. |
| `min_cpu` | Suggested minimum vCPU contribution. |
| `min_mem` | Suggested minimum memory in MiB. |
| `min_disk` | Suggested minimum disk in GiB. |
| `status` | Deployment class, such as `containerized` or `windows-iis`. |
| `notes` | Operational notes. |

Do not put plaintext secrets in the manifest. Use references such as `secret/runtime-targets/app/operator` and resolve them through your own lab secret process.

## Docker Assets And Source Caches

This private repository is intended to include the generated Docker asset tree and the cached source repositories used to build or run the lab applications:

1. `docker-images/security-testing-lab/` contains Docker Compose bundles, build contexts, helper scripts, and generated deployment assets.
2. `target-app-repos/` contains local source mirrors, source-matched application caches, generated fixtures, or copied source overlays used by the Docker assets.
3. Third-party applications retain upstream ownership and licenses.
4. Project-authored orchestration scripts and generated local fixtures are covered by this project's GPLv3 license unless a file states otherwise.

Build a single Docker asset when the asset tree provides `build-one.sh`:

```bash
cd docker-images/security-testing-lab
./build-one.sh <app_id>
```

## Credentials And Secrets

`LabSetup.sh` prompts for SSH passwords and keeps them in memory for the current run only. It does not write passwords to disk.

Application credentials are represented as references in the manifests. Operators should provide real values on destination hosts through `.env` files, Docker secrets, a vault, or another approved secret mechanism.

Never commit:

1. SSH passwords or private keys.
2. Application passwords.
3. Database passwords.
4. API tokens.
5. Session cookies.
6. TLS private keys.
7. Customer or client data.
8. Runtime database volumes or captured traffic.

## Port Behavior

For Linux Docker deployments, the script checks common listening ports on each destination host and increments from the preferred `default_port` until it finds an unused port.

The generated temporary override maps:

```yaml
services:
  <service>:
    ports:
      - "0.0.0.0:<chosen-host-port>:<internal-port>"
```

Review the final Docker Compose output on each target host after deployment.

## Common Commands

Show help:

```bash
bash lab-setup/LabSetup.sh --help
```

Deploy Linux Docker targets:

```bash
bash lab-setup/LabSetup.sh --linux
```

Deploy Windows/IIS targets:

```bash
bash lab-setup/LabSetup.sh --windows-iis
```

Build a single Docker asset:

```bash
cd docker-images/security-testing-lab
./build-one.sh <app_id>
```

Check running containers on a destination host:

```bash
ssh user@host 'docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"'
```

## Source Attribution And License Evidence

This table cites the source origin currently associated with each cached repo or lab family. `Not detected` means no license file was detected in the local cache during README preparation; verify the upstream project before changing distribution scope.

| Apps | Source origin | License evidence |
| --- | --- | --- |
| AltoroJ | `https://github.com/AppSecDev/AltoroJ` | Apache license file detected |
| ASP VBScript CMS | `https://github.com/jameswilson/asp-vbscript-cms` | MIT license file detected |
| ASP.NET Core Vulnerable Lab | `https://github.com/dotnet/AspNetCore.Docs` | Not detected in local cache |
| OWASP BenchmarkJava, source-matched BenchmarkJava | `https://github.com/OWASP-Benchmark/BenchmarkJava` | GPL license file detected |
| BodgeIt Store | `https://github.com/psiinon/bodgeit` | Not detected in local cache |
| Bugzilla | `https://github.com/bugzilla/bugzilla` | GPLv3 license file detected |
| bWAPP | `https://github.com/raesene/bWAPP` | Not detected in local cache |
| crAPI, crAPI MailHog | `https://github.com/OWASP/crAPI` | Verify upstream license |
| Django.nV | `https://github.com/nVisium/django.nV` | GPL license file detected |
| DotNetNuke DNN Legacy Lab | `https://github.com/dnnsoftware/Dnn.Platform` | Not detected in local cache |
| Drupal | `https://github.com/drupal/drupal` | Not detected in local cache |
| DVGA, DVGA holdout | `https://github.com/dolevf/Damn-Vulnerable-GraphQL-Application` | MIT license file detected |
| DVNA, source-matched DVNA | `https://github.com/appsecco/dvna` | MIT license file detected |
| DVWA | `https://github.com/digininja/DVWA` | GPLv3 license file detected |
| DVWP WordPress, DVWP phpMyAdmin | `https://github.com/vavkamil/dvwp` | Not detected in local cache |
| DVWS, DVWS auxiliary HTTP | `https://github.com/snoopysecurity/dvws` | Apache license file detected |
| Gitea DevOps Lab | `https://github.com/go-gitea/gitea` | Not detected in local cache |
| Google Gruyere | `https://github.com/ab-smith/gruyere` | Not detected in local cache |
| Grafana Dashboard Lab | `https://github.com/grafana/grafana` | Not detected in local cache |
| gRPC-Web Demo Lab | `https://github.com/grpc/grpc-web` | Not detected in local cache |
| Hackazon | `https://github.com/rapid7/hackazon` | Apache license file detected |
| Jenkins Plugin RBAC Lab | `https://github.com/jenkinsci/jenkins` | Not detected in local cache |
| Joomla | `https://github.com/joomla/joomla-cms` | GPL license file detected |
| OWASP Juice Shop | `https://github.com/juice-shop/juice-shop` | MIT license file detected |
| Kibana OpenSearch Dashboards Lab | `https://github.com/opensearch-project/OpenSearch-Dashboards` | Not detected in local cache |
| LANraragi | `https://github.com/Difegue/LANraragi` | MIT license file detected |
| Magento | `https://github.com/magento/magento2` | License file detected |
| MediaWiki Extension Lab | `https://github.com/wikimedia/mediawiki` | Not detected in local cache |
| Moodle Old-Version Lab | `https://github.com/moodle/moodle` | Not detected in local cache |
| Mutillidae II | `https://github.com/webpwnized/mutillidae` | GPLv3 license file detected |
| Nextcloud ownCloud Lab | `https://github.com/nextcloud/server` | Not detected in local cache |
| NodeGoat | `https://github.com/OWASP/NodeGoat` | Apache license file detected |
| old phpMyAdmin | `https://github.com/phpmyadmin/phpmyadmin` | GPL license file detected |
| OpenEMR | `https://github.com/openemr/openemr` | GPLv3 license file detected |
| OWASP Bricks | `https://github.com/CYBASQUAD/owasp-bricks` | MIT license file detected |
| phpBB Forum Lab | `https://github.com/phpbb/phpbb` | Not detected in local cache |
| QuickerSite Classic ASP health | `https://github.com/PieterCooreman/QuickerSite` | MIT license file detected |
| RailsGoat | `https://github.com/OWASP/railsgoat` | MIT license file detected |
| Roundcube Webmail Lab | `https://github.com/roundcube/roundcubemail` | Not detected in local cache |
| OWASP Security Ninjas | `https://github.com/opendns/Security_Ninjas_AppSec_Training` | Not detected in local cache |
| Security Shepherd | `https://github.com/OWASP/SecurityShepherd` | GPLv3 license file detected |
| Spring Petclinic | `https://github.com/spring-projects/spring-petclinic` | Apache license file detected |
| SQLi-Labs | `https://github.com/Audi-1/sqli-labs` | Not detected in local cache |
| SSTI Matrix Lab | `https://github.com/pallets/jinja` | Not detected in local cache |
| Umbraco CMS Lab | `https://github.com/umbraco/Umbraco-CMS` | Not detected in local cache |
| Upload-Labs | `https://github.com/c0ny1/upload-labs` | Not detected in local cache |
| VAmPI | `https://github.com/erev0s/VAmPI` | MIT license file detected |
| vAPI | `https://github.com/roottusk/vapi` | GPLv3 license file detected |
| Vulnado | `https://github.com/bbhunter/vulnado` | Apache license file detected |
| Vulnerable WordPress plugin lab | `https://github.com/wpscanteam/VulnerableWordpress` | Not detected in local cache |
| Vulpy | `https://github.com/fportantier/vulpy` | MIT license file detected |
| WackoPicko | `https://github.com/adamdoupe/WackoPicko` | MIT license file detected |
| WebAuthn Passkey Lab | `https://github.com/duo-labs/py_webauthn` | Not detected in local cache |
| WebGoat, WebWolf | `https://github.com/WebGoat/WebGoat` | GPL license file detected |
| WrongSecrets, WrongSecrets MCP aux | `https://github.com/OWASP/wrongsecrets` | GPLv3 license file detected |
| XSS-Labs | `https://github.com/do0dl3/xss-labs` | Not detected in local cache |
| XVWA | `https://github.com/s4n7h0/xvwa` | GPLv3 license file detected |
| Peruggia, protocol fixtures, auth-boundary lab, generated API/CMS/framework/security fixtures, additional source-backed practice labs | Local/generated source cache or copied lab overlay with no upstream remote configured | Project-generated or verify source-specific notices before public distribution |

## Troubleshooting

`Docker assets missing`

The directory `docker-images/security-testing-lab/` does not exist. Restore or generate the asset tree before running Linux mode.

`Preflight failed`

The remote host may be missing Docker, Docker Compose, SSH access, or required Windows/IIS prerequisites.

`sshpass is not installed`

Install `sshpass`, use SSH keys, or allow SSH/SCP to prompt interactively.

Selected app starts on a different port

The preferred port was already in use. The script increments until it finds an open port and writes a temporary Compose override.

Heavy app fails to start

Check memory, disk, dependency services, required `.env` values, and the app-specific notes in `lab-apps.tsv`.

## Target Matrix

The lab setup manifest currently tracks these targets. Local image names use the `securitytestinglab/` namespace in this sanitized export.

| # | Target | Image / Version | Upstream / Source |
| ---: | --- | --- | --- |
| 1 | DVWA | `version not specified` | [https://github.com/digininja/DVWA](https://github.com/digininja/DVWA) |
| 2 | SQLi-Labs | `securitytestinglab/sqli-labs-target:local` | [https://github.com/Audi-1/sqli-labs](https://github.com/Audi-1/sqli-labs) |
| 3 | OWASP Bricks | `securitytestinglab/owasp-bricks-target:local` | [https://sourceforge.net/projects/owaspbricks/](https://sourceforge.net/projects/owaspbricks/) |
| 4 | Peruggia | `securitytestinglab/peruggia-target:local` | [https://github.com/jay/peruggia](https://github.com/jay/peruggia) |
| 5 | Upload-Labs | `securitytestinglab/upload-labs-target:local` | [https://github.com/c0ny1/upload-labs](https://github.com/c0ny1/upload-labs) |
| 6 | XSS-Labs | `securitytestinglab/xss-labs-target:local` | [https://github.com/do0dl3/xss-labs](https://github.com/do0dl3/xss-labs) |
| 7 | Google Gruyere | `securitytestinglab/google-gruyere-target:local` | [https://google-gruyere.appspot.com/](https://google-gruyere.appspot.com/) |
| 8 | OWASP Security Ninjas | `securitytestinglab/security-ninjas-target:local` | [https://github.com/SpiderLabs/Security_Ninjas_AppSec_Training](https://github.com/SpiderLabs/Security_Ninjas_AppSec_Training) |
| 9 | BodgeIt Store | `securitytestinglab/bodgeit-target:local` | [https://github.com/psiinon/bodgeit](https://github.com/psiinon/bodgeit) |
| 10 | AltoroJ | `securitytestinglab/altoroj-target:local` | [https://github.com/HCL-TECH-SOFTWARE/AltoroJ](https://github.com/HCL-TECH-SOFTWARE/AltoroJ) |
| 11 | Vulnado | `securitytestinglab/vulnado-target:local` | [https://github.com/ScaleSec/vulnado](https://github.com/ScaleSec/vulnado) |
| 12 | OWASP Juice Shop | `version not specified` | [https://github.com/juice-shop/juice-shop](https://github.com/juice-shop/juice-shop) |
| 13 | VAmPI | `erev0s/vampi:latest` | [https://github.com/erev0s/VAmPI](https://github.com/erev0s/VAmPI) |
| 14 | DVGA | `version not specified` | [https://github.com/dolevf/Damn-Vulnerable-GraphQL-Application](https://github.com/dolevf/Damn-Vulnerable-GraphQL-Application) |
| 15 | WebSocket SSE HTTP lab | `securitytestinglab/ws-sse-lab:local` | local lab fixture source |
| 16 | HTTPS HTTP2 lab | `securitytestinglab/h2-lab:local` | local lab fixture source |
| 17 | crAPI | `crapi/crapi-web:${VERSION:-latest}` | [https://github.com/OWASP/crAPI](https://github.com/OWASP/crAPI) |
| 18 | crAPI MailHog | `crapi/mailhog:${VERSION:-latest}` | [https://github.com/mailhog/MailHog](https://github.com/mailhog/MailHog) |
| 19 | DVGA holdout | `dolevf/dvga:latest` | [https://github.com/dolevf/Damn-Vulnerable-GraphQL-Application](https://github.com/dolevf/Damn-Vulnerable-GraphQL-Application) |
| 20 | WebGoat | `webgoat/webgoat:latest` | [https://github.com/WebGoat/WebGoat](https://github.com/WebGoat/WebGoat) |
| 21 | WebWolf | `webgoat/webgoat:latest` | [https://github.com/WebGoat/WebGoat](https://github.com/WebGoat/WebGoat) |
| 22 | DVWS | `tssoffsec/dvws:latest` | [https://github.com/snoopysecurity/dvws-node](https://github.com/snoopysecurity/dvws-node) |
| 23 | DVWS auxiliary HTTP | `tssoffsec/dvws:latest` | [https://github.com/snoopysecurity/dvws-node](https://github.com/snoopysecurity/dvws-node) |
| 24 | bWAPP | `raesene/bwapp:latest` | [https://sourceforge.net/projects/bwapp/](https://sourceforge.net/projects/bwapp/) |
| 25 | vAPI | `securitytestinglab/vapi-target:local` | [https://github.com/roottusk/vapi](https://github.com/roottusk/vapi) |
| 26 | OpenEMR | `openemr/openemr:5.0.2` | [https://github.com/openemr/openemr](https://github.com/openemr/openemr) |
| 27 | Magento | `alexcheng/magento2:2.2.3` | [https://github.com/magento/magento2](https://github.com/magento/magento2) |
| 28 | Drupal | `drupal:8.9.20-php7.4-apache` | [https://github.com/drupal/drupal](https://github.com/drupal/drupal) |
| 29 | Auth-boundary REST lab | `securitytestinglab/auth-boundary-lab:local` | local lab fixture source |
| 30 | Auth-boundary GraphQL lab | `securitytestinglab/auth-boundary-lab:local` | local lab fixture source |
| 31 | Mutillidae II | `webpwnized/mutillidae:www-2.12.5` | [https://github.com/webpwnized/mutillidae](https://github.com/webpwnized/mutillidae) |
| 32 | RailsGoat | `owasp/railsgoat:main` | [https://github.com/OWASP/railsgoat](https://github.com/OWASP/railsgoat) |
| 33 | OWASP BenchmarkJava | `owasp/benchmark:latest` | [https://github.com/OWASP-Benchmark/BenchmarkJava](https://github.com/OWASP-Benchmark/BenchmarkJava) |
| 34 | source-matched BenchmarkJava | `owasp/benchmark:latest` | [https://github.com/OWASP-Benchmark/BenchmarkJava](https://github.com/OWASP-Benchmark/BenchmarkJava) |
| 35 | Spring Petclinic | `securitytestinglab/spring-petclinic-target:local` | [https://github.com/spring-projects/spring-petclinic](https://github.com/spring-projects/spring-petclinic) |
| 36 | Bugzilla | `version not specified` | [https://github.com/bugzilla/bugzilla](https://github.com/bugzilla/bugzilla) |
| 37 | LANraragi | `version not specified` | [https://github.com/Difegue/LANraragi](https://github.com/Difegue/LANraragi) |
| 38 | WrongSecrets | `jeroenwillemsen/wrongsecrets:latest-no-vault` | [https://github.com/OWASP/wrongsecrets](https://github.com/OWASP/wrongsecrets) |
| 39 | WrongSecrets MCP aux | `jeroenwillemsen/wrongsecrets:latest-no-vault` | [https://github.com/OWASP/wrongsecrets](https://github.com/OWASP/wrongsecrets) |
| 40 | Security Shepherd | `securitytestinglab/security-shepherd:local` | [https://github.com/OWASP/SecurityShepherd](https://github.com/OWASP/SecurityShepherd) |
| 41 | DVWP WordPress | `securitytestinglab/dvwp-wordpress:local` | [https://github.com/vavkamil/dvwp](https://github.com/vavkamil/dvwp) |
| 42 | DVWP phpMyAdmin | `phpmyadmin/phpmyadmin:latest` | [https://github.com/phpmyadmin/phpmyadmin](https://github.com/phpmyadmin/phpmyadmin) |
| 43 | old phpMyAdmin | `phpMyAdmin 4.8, MySQL 5.7 backend` | [https://github.com/phpmyadmin/phpmyadmin](https://github.com/phpmyadmin/phpmyadmin) |
| 44 | Joomla | `joomla:3.9.0-php7.2-apache` | [https://github.com/joomla/joomla-cms](https://github.com/joomla/joomla-cms) |
| 45 | vulnerable WordPress plugin lab | `securitytestinglab/vulnerable-wordpress-plugin-lab:local` | local deployed vulnerable WordPress plugin lab source |
| 46 | NodeGoat | `securitytestinglab/nodegoat-target:local` | [https://github.com/OWASP/NodeGoat](https://github.com/OWASP/NodeGoat) |
| 47 | DVNA | `appsecco/dvna:sqlite` | [https://github.com/appsecco/dvna](https://github.com/appsecco/dvna) |
| 48 | source-matched DVNA | `appsecco/dvna:sqlite` | [https://github.com/appsecco/dvna](https://github.com/appsecco/dvna) |
| 49 | Django.nV | `securitytestinglab/django-nv-target:local` | [https://github.com/anxolerd/dvpwa](https://github.com/anxolerd/dvpwa) |
| 50 | Vulpy | `securitytestinglab/vulpy-target:local` | [https://github.com/fportantier/vulpy](https://github.com/fportantier/vulpy) |
| 51 | QuickerSite Classic ASP health | `version not specified` | local/source-mirrored Classic ASP QuickerSite target |
| 52 | ASP VBScript CMS | `version not specified` | local/source-mirrored Classic ASP VBScript CMS target |
| 53 | patched exploration CMS | `version not specified` | local patched IIS exploration site |
| 54 | XVWA | `bitnetsecdave/xvwa:latest` | [https://github.com/s4n7h0/xvwa](https://github.com/s4n7h0/xvwa) |
| 55 | WackoPicko | `adamdoupe/wackopicko:latest` | [https://github.com/adamdoupe/WackoPicko](https://github.com/adamdoupe/WackoPicko) |
| 56 | Hackazon | `pierrickv/hackazon:latest` | [https://github.com/rapid7/hackazon](https://github.com/rapid7/hackazon) |
| 57 | Headers static leak fixture | `version not specified` | local lab fixture source |
| 58 | JWT auth fixture | `version not specified` | local lab fixture source |
| 59 | Cache deception fixture | `varnish:7.5-alpine` | [https://hub.docker.com/_/varnish](https://hub.docker.com/_/varnish) |
| 60 | WAF bypass shape fixture | `version not specified` | local lab fixture source |
| 61 | SOAP WSDL fixture | `version not specified` | local lab fixture source |
| 62 | Internal OOB callback fixture | `version not specified` | local lab fixture source |
| 63 | AI safety prompt fixture | `version not specified` | local lab fixture source |
| 64 | OWASP SKF Labs Mini | `source pin 9b45f081c808` | local generated source-backed lab |
| 65 | PortSwigger-style Web Security Academy Subset | `source pin 8cbf1606cb09` | local generated source-backed lab |
| 66 | GraphQL Voyager Demo API | `source pin c4b39c19bee6` | local generated source-backed lab |
| 67 | Tiredful REST API Lab | `source pin 05a8eed0470d` | local generated source-backed lab |
| 68 | Keycloak Weak OIDC Client Lab | `source pin 02549938cf4f` | local generated source-backed lab |
| 69 | SAML SP IdP Lab | `source pin 7f6a35b62625` | local generated source-backed lab |
| 70 | Python Framework Misconfiguration Lab | `source pin af86f0770750` | local generated source-backed lab |
| 71 | Ghost Express CMS Lab | `source pin cefbaf438016` | local generated source-backed lab |
| 72 | Laravel LaraBug Lab | `source pin 7d5f836bb054` | local generated source-backed lab |
| 73 | Spring Boot Vulnerable Lab | `source pin 278c7973328b` | local generated source-backed lab |
| 74 | Apache Struts Showcase Lab | `source pin 5d5a4f08e934` | local generated source-backed lab |
| 75 | TYPO3 PrestaShop Legacy Lab | `source pin f188a219c144` | local generated source-backed lab |
| 76 | Web Cache Deception Variants Lab | `source pin 732b6562839a` | local generated source-backed lab |
| 77 | SSRF Metadata Simulation Lab | `source pin 82ac239856f7` | local generated source-backed lab |
| 78 | CORS JWT Header Misconfiguration Lab | `source pin 7efb6edc7b1a` | local generated source-backed lab |
| 79 | ASP.NET Core Vulnerable Lab | `source pin f6ac82236846` | [https://github.com/dotnet/AspNetCore.Docs](https://github.com/dotnet/AspNetCore.Docs) |
| 80 | DotNetNuke DNN Legacy Lab | `source pin 7904ea8b355b` | [https://github.com/dnnsoftware/Dnn.Platform](https://github.com/dnnsoftware/Dnn.Platform) |
| 81 | Umbraco CMS Lab | `source pin aea9ad453987` | [https://github.com/umbraco/Umbraco-CMS](https://github.com/umbraco/Umbraco-CMS) |
| 82 | Moodle Old-Version Lab | `source pin d38468607e55` | [https://github.com/moodle/moodle](https://github.com/moodle/moodle) |
| 83 | phpBB Forum Lab | `source pin dbcdc4a13618` | [https://github.com/phpbb/phpbb](https://github.com/phpbb/phpbb) |
| 84 | MediaWiki Extension Lab | `source pin 8e55c04e4cdc` | [https://github.com/wikimedia/mediawiki](https://github.com/wikimedia/mediawiki) |
| 85 | Roundcube Webmail Lab | `source pin 65285394e14d` | [https://github.com/roundcube/roundcubemail](https://github.com/roundcube/roundcubemail) |
| 86 | Nextcloud ownCloud Lab | `source pin 49755cc2061d` | [https://github.com/nextcloud/server](https://github.com/nextcloud/server) |
| 87 | Gitea DevOps Lab | `source pin 7e272ed590f1` | [https://github.com/go-gitea/gitea](https://github.com/go-gitea/gitea) |
| 88 | Jenkins Plugin RBAC Lab | `source pin a702fd8f6f34` | [https://github.com/jenkinsci/jenkins](https://github.com/jenkinsci/jenkins) |
| 89 | Grafana Dashboard Lab | `source pin 662570ee34b6` | [https://github.com/grafana/grafana](https://github.com/grafana/grafana) |
| 90 | Kibana OpenSearch Dashboards Lab | `source pin 8bbb05fa829e` | [https://github.com/opensearch-project/OpenSearch-Dashboards](https://github.com/opensearch-project/OpenSearch-Dashboards) |
| 91 | gRPC-Web Demo Lab | `source pin d4e0df74c8a9` | [https://github.com/grpc/grpc-web](https://github.com/grpc/grpc-web) |
| 92 | WebAuthn Passkey Lab | `source pin 0414ce24ef4c` | [https://github.com/duo-labs/py_webauthn](https://github.com/duo-labs/py_webauthn) |
| 93 | SSTI Matrix Lab | `source pin a8734f4cd34d` | [https://github.com/pallets/jinja](https://github.com/pallets/jinja) |
