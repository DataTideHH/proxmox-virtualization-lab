# Implementation Log

## Current entries

### 2026-07-26 — Pre-hardware design and validation hardened

Status: completed repository work; no Proxmox hardware claim

Purpose:

- align the Proxmox-side VLAN design with the Cisco lab
- separate guest restore from host reconstruction
- formalize the public synthetic inventory boundary
- make the validator repeatable through unit tests and CI

Actions:

- required a physical or independent console recovery path
- documented access-port-first networking and later VLAN roles 20, 30, 99, 998 and 999
- separated the backup target from the active guest datastore in the topology
- refined privilege-separated API-token, ACL and expiration principles
- limited schema `0.1` to nodes and guests
- hardened timestamp, status, relationship and numeric validation
- added standard-library unit tests and GitHub Actions
- added official Proxmox reference links

Validation:

- committed synthetic sample must pass the validator
- unit tests exercise valid and invalid schema behavior
- GitHub Actions runs syntax checks, tests and sample validation
- documentation continues to state that no live Proxmox host exists

Result:

- pre-hardware planning is internally consistent and executable where hardware is not required
- storage, network-assignment and backup-run entities remain deferred
- the next substantive milestone requires dedicated x86 hardware

Rollback or recovery:

- repository changes are isolated in a pull request and remain reversible through Git history

Public-safe evidence:

- source, tests, CI workflow and documentation only

Open questions:

- final host model and storage layout
- final separate backup target
- exact API paths and ACL roles after live field review

### 2026-07-21 — Repository foundation prepared

Status: planning only

Completed:

- project scope defined
- hardware criteria drafted
- architecture phases defined
- network design prepared
- storage and backup questions documented
- access-control and API principles documented
- validation checklist created
- synthetic inventory sample and validator prepared

Not completed:

- hardware purchase
- Proxmox installation
- VM or LXC creation
- backup or restore test
- live API collection

## Entry template

### YYYY-MM-DD — Change title

Status:

Purpose:

Actions:

Validation:

Result:

Rollback or recovery:

Public-safe evidence:

Open questions:
