# Validation Checklist

## Pre-installation

- [ ] dedicated hardware selected
- [ ] virtualization support confirmed
- [ ] firmware settings documented
- [ ] wired network available
- [ ] local physical or independently validated out-of-band console available
- [ ] first access-port design reviewed
- [ ] storage and backup design reviewed
- [ ] separate backup target selected
- [ ] installer filename and official integrity value recorded

## Host baseline

- [ ] installation completes successfully
- [ ] local console recovery works
- [ ] management access works
- [ ] hostname and addressing are documented privately
- [ ] installed package and version baseline is recorded privately
- [ ] package repository channel is documented
- [ ] initial update process completes and is documented
- [ ] time synchronization works
- [ ] storage is healthy
- [ ] no public management exposure exists

## Guest baseline

- [ ] one Linux VM created
- [ ] one LXC container created
- [ ] start, stop and restart tested
- [ ] console access tested
- [ ] guest purpose documented
- [ ] resource allocations documented
- [ ] LXC bind or device mounts, if any, are reviewed for backup exclusions

## Network

- [ ] switch port role documented
- [ ] speed and duplex verified
- [ ] error counters checked
- [ ] gateway, DNS and NTP validated
- [ ] management access restricted
- [ ] VLAN 99 reserved for tagged management in the later trunk stage
- [ ] VLAN 998 remains native and unused without host or guest assignment
- [ ] VLAN 999 remains Cisco-side only and is excluded from the Proxmox trunk
- [ ] trunk rollback documented before activation
- [ ] console access retained until the changed network path is verified

## Backup and guest recovery

- [ ] backup target is separate from the active guest datastore
- [ ] VM backup succeeds
- [ ] LXC backup succeeds
- [ ] restore succeeds
- [ ] restored guest is validated in isolation
- [ ] retention is documented
- [ ] expected services or data are checked after restore

## Host recovery

- [ ] minimum host reconstruction information is documented privately
- [ ] network and storage reconstruction order is documented
- [ ] separate backup target can be reattached
- [ ] guest recovery dependencies after host reinstallation are understood
- [ ] public documentation contains no raw configuration archive or secret

## Access control and API

- [ ] named administrative identity exists
- [ ] API identity is separate
- [ ] inventory token uses privilege separation
- [ ] token has an explicit expiration date
- [ ] assigned roles and paths are read-only and limited to reviewed calls
- [ ] effective permissions are inspected
- [ ] non-inventory operations remain unavailable to the token
- [ ] token disablement is tested
- [ ] TLS verification remains enabled
- [ ] secrets remain outside Git
- [ ] sanitized sample export reviewed

## Synthetic inventory and CI

- [ ] schema `0.1` remains limited to nodes and guests
- [ ] committed sample passes the validator
- [ ] unit tests pass locally
- [ ] GitHub Actions `Python 3.12` check passes
- [ ] storage, network and backup entities remain marked as planned

## Portfolio publication

- [ ] every implementation claim is verified
- [ ] current state and roadmap are separated
- [ ] screenshots contain no private details
- [ ] real identifiers are replaced
- [ ] limitations and failure points are documented
- [ ] official reference links were checked at the time of implementation
