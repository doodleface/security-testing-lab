# SecurityTestingLab Vulnerable Lab 01

Host: ct-vulnlab-01 (10.190.190.99)

This directory contains Docker Compose deployment files for intentionally vulnerable or candidate-generating validation fixtures. Services are lab-only and must not be exposed outside the SecurityTestingLab validation network.

## Services

- XVWA: http://10.190.190.99:18101/
- WackoPicko: http://10.190.190.99:18102/
- Hackazon: http://10.190.190.99:18103/
- Headers/static leak fixture: http://10.190.190.99:18110/
- JWT/auth fixture: http://10.190.190.99:18111/
- Cache deception fixture via Varnish: http://10.190.190.99:18112/
- WAF bypass-shape fixture: http://10.190.190.99:18114/
- SOAP/WSDL fixture: http://10.190.190.99:18115/
- Internal OOB callback fixture: http://10.190.190.99:18116/
- AI safety prompt fixture: http://10.190.190.99:18117/

## Operations

Start or refresh with:

```sh
cd /opt/securitytestinglab-vulnlab
sudo docker-compose up -d --build
```

Stop with:

```sh
cd /opt/securitytestinglab-vulnlab
sudo docker-compose down
```
