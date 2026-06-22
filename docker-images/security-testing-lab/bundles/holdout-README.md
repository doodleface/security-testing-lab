# Section 40 Holdout Lab

Host: `ct-target-holdout` (`10.190.190.95`)

This VM is an intentionally vulnerable development/QA target for SecurityTestingLab Section 40 holdout evaluation. Do not use these apps outside the authorized lab network.

## Services

| Service | URL | Purpose |
| --- | --- | --- |
| crAPI | `http://10.190.190.95:8888/` | REST/API authorization, object ownership, JWT/session, and business-logic workflow proof |
| crAPI MailHog | `http://10.190.190.95:8025/` | crAPI mailbox/callback inspection for authorized lab workflows |
| DVGA holdout | `http://10.190.190.95:5013/` | Authenticated GraphQL holdout UI |
| DVGA GraphQL | `http://10.190.190.95:5013/graphql` | GraphQL endpoint for schema, auth-boundary, and operation proof |
| WebGoat | `http://10.190.190.95:8081/WebGoat/` | Authenticated workflow, file handling, and business-logic training flows |
| WebWolf | `http://10.190.190.95:9090/WebWolf/` | WebGoat companion mailbox/callback service |
| DVWS | `http://10.190.190.95:8082/` | Damn Vulnerable WebSockets UI |
| DVWS auxiliary port | `http://10.190.190.95:8084/` | DVWS exposed auxiliary/WebSocket service port |
| bWAPP | `http://10.190.190.95:8083/login.php` | Broad web vulnerability/file-handling holdout target |

## Local Stack

The compose files live in `/home/dev/section40-holdout-lab`:

- `crapi-compose.yml`: official OWASP crAPI compose file fetched from upstream.
- `section40-holdout-apps.yml`: DVGA, WebGoat/WebWolf, DVWS, and bWAPP compose file.
- `section40-holdout.env`: non-secret listener/version values.

Start or refresh the stack from this directory with:

```bash
docker-compose --env-file section40-holdout.env -f crapi-compose.yml -f section40-holdout-apps.yml up -d
```

Check status with:

```bash
docker-compose --env-file section40-holdout.env -f crapi-compose.yml -f section40-holdout-apps.yml ps
```

## Credential Handling

Do not commit plaintext app credentials. Use the secret refs recorded in `docs/runtime_target_inventory.md` on the SecurityTestingLab host.
