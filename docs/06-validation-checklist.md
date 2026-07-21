# Validation Checklist

## Pre-installation

- [ ] dedicated hardware selected
- [ ] virtualization support confirmed
- [ ] firmware settings documented
- [ ] wired network available
- [ ] recovery console available
- [ ] storage and backup design reviewed

## Host baseline

- [ ] installation completes successfully
- [ ] management access works
- [ ] hostname and addressing are documented privately
- [ ] time synchronization works
- [ ] update process is documented
- [ ] storage is healthy
- [ ] no public management exposure exists

## Guest baseline

- [ ] one Linux VM created
- [ ] one LXC container created
- [ ] start, stop and restart tested
- [ ] console access tested
- [ ] guest purpose documented
- [ ] resource allocations documented

## Network

- [ ] switch port role documented
- [ ] speed and duplex verified
- [ ] error counters checked
- [ ] gateway, DNS and NTP validated
- [ ] management access restricted
- [ ] optional trunk rollback documented before activation

## Backup and recovery

- [ ] backup target configured
- [ ] VM backup succeeds
- [ ] LXC backup succeeds
- [ ] restore succeeds
- [ ] restored guest is validated in isolation
- [ ] retention is documented

## Access control and API

- [ ] named administrative identity exists
- [ ] API identity is separate
- [ ] inventory token is read-only
- [ ] secrets remain outside Git
- [ ] sanitized sample export reviewed

## Portfolio publication

- [ ] every claim is verified
- [ ] current state and roadmap are separated
- [ ] screenshots contain no private details
- [ ] real identifiers are replaced
- [ ] limitations and failure points are documented
