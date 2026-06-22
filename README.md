# Security Testing Lab Setup

This repository contains lab deployment assets for intentionally vulnerable web application targets used in authorized security testing and training environments.

## Contents

- `lab-setup/LabSetup.sh`: interactive deployment helper for Linux Docker targets and Windows/IIS targets.
- `lab-setup/lab-apps.tsv`: application inventory used by the setup script.
- `lab-setup/windows-iis-apps.tsv`: Windows/IIS application inventory used by the setup script.
- `docker-images/security-testing-lab/`: Docker Compose bundles and build contexts.
- `target-app-repos/`: source caches and copied target application sources used by the lab manifests.

## Usage

Run from the repository root:

```bash
bash lab-setup/LabSetup.sh --linux
```

For Windows/IIS targets:

```bash
bash lab-setup/LabSetup.sh --windows-iis
```

The script prompts for destination servers and can use SSH keys or password-based SSH when `sshpass` is available. Do not store plaintext credentials in this repository.

## Safety

These applications are intentionally vulnerable. Deploy them only on authorized lab networks. Review exposed ports, firewall rules, and credentials before starting any target.

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
