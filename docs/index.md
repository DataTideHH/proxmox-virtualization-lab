---
layout: default
title: Proxmox Virtualization Lab
description: Public-safe virtualization learning lab for architecture, networking, recovery, access control and future operational data integration.
---

# Proxmox Virtualization Lab

**A public-safe learning and portfolio project documenting the planned path from dedicated x86 hardware to a small, recoverable Proxmox environment and later operational data integration.**

[View repository](https://github.com/DataTideHH/proxmox-virtualization-lab) · [View CI](https://github.com/DataTideHH/proxmox-virtualization-lab/actions/workflows/ci.yml) · [Read the full README](https://github.com/DataTideHH/proxmox-virtualization-lab/blob/main/README.md) · [DataTideHH portfolio](https://datatidehh.de/)

---

## Current status

**Planning and pre-hardware preparation.**

A dedicated x86 host has not yet been acquired. This project does not claim an installed or verified Proxmox environment.

The current repository provides a tested foundation for:

- hardware selection including a recoverable console path
- staged architecture decisions
- conservative Cisco network integration
- storage, guest-backup, restore and host-recovery planning
- least-privilege user, ACL and API-token design
- public-safe validation criteria
- synthetic node and guest inventory schema `0.1`
- a standard-library Python validator and unit tests
- GitHub Actions validation
- official Proxmox references

---

## Project purpose

The future lab should build practical virtualization knowledge while remaining connected to a Data/BI-oriented portfolio.

The intended cross-layer structure is:

```text
Cisco physical network
        |
        v
Proxmox virtualization platform
        |
        v
sanitized operational metadata
        |
        v
Python + SQLite + SQL data-quality workflow
        |
        v
Power BI operational reporting
```

Each layer remains documented in its own repository so that networking, virtualization administration and analytical data work stay clearly separated.

---

## Repository role

| Area | What this repository documents |
|---|---|
| Hardware | Dedicated-host requirements, exclusions and independent recovery access |
| Installation | Planned Proxmox installation, integrity checks and validation sequence |
| Networking | Linux bridges, an access-port-first baseline and later VLAN-aware options |
| Guests | Small VM and LXC lifecycle exercises after hardware exists |
| Storage | Storage layout, capacity decisions and separation of concerns |
| Recovery | Guest backups, restore testing and separate host reconstruction planning |
| Security | Users, roles, ACL paths, privilege-separated API tokens and private/public separation |
| Operations data | Sanitized inventory exports for the separate Data/BI workflow |

---

## Network stages

The first hardware baseline remains simple:

```text
home or lab gateway
        |
Cisco switch
        |
access port in VLAN 20
        |
Proxmox host and default Linux bridge
```

Only after the baseline is stable should the lab introduce tagged management on VLAN 99 and a restricted trunk. VLAN 998 remains native and unused, while VLAN 999 remains a Cisco-side parking VLAN and is not part of the Proxmox trunk.

Every bridge, VLAN or management-address change requires a documented rollback and a physical or independently validated console path.

---

## Synthetic inventory scope

Schema `0.1` covers nodes and guests only. It validates:

- exact schema version and public-safe sample type
- UTC timestamp format
- unique node and guest keys
- allowed status and guest-type values
- positive integer resource values
- guest-to-node relationships
- ownership, purpose and backup-policy fields

Storage inventory, virtual-network assignments and backup-run records remain planned until live API fields and data-quality rules have been reviewed.

The repository runs syntax checks, unit tests and the committed sample validator in the `Python 3.12` GitHub Actions job.

---

## First implementation milestone

The first verified hardware stage should remain deliberately small:

- one dedicated x86 host
- one recoverable console path
- one Ethernet connection
- one controlled access-port lab VLAN
- one Linux virtual machine
- one LXC container
- one separate backup target
- one successful VM and LXC restore test
- one documented host reconstruction sequence
- one least-privilege API token with privilege separation and expiration
- one sanitized node and guest inventory export

Cluster, Ceph, high availability and complex software-defined networking are not required for the first portfolio milestone.

---

## Documentation

| Document | Purpose |
|---|---|
| [Project scope](00-project-scope.md) | Boundaries, schema scope, learning goals and portfolio role |
| [Hardware selection](01-hardware-selection.md) | Host requirements, useful features, exclusions and recovery access |
| [Architecture roadmap](02-architecture-roadmap.md) | Staged path from planning to validated operation |
| [Network design](03-network-design.md) | Access-port-first integration, VLAN roles and rollback order |
| [Storage and backup design](04-storage-and-backup-design.md) | Storage, guest restore and separate host-recovery criteria |
| [Access control and API](05-access-control-and-api.md) | Users, roles, ACL paths, tokens and least-privilege principles |
| [Validation checklist](06-validation-checklist.md) | Planned acceptance checks for each implementation stage |
| [Implementation log](07-implementation-log.md) | Public-safe record for verified repository and future hardware work |
| [Official references](08-official-references.md) | Proxmox documentation, API, networking, backup and installer sources |
| [Lessons learned](99-lessons-learned.md) | Findings and revisions as the lab develops |
| [Lab topology](https://github.com/DataTideHH/proxmox-virtualization-lab/blob/main/diagrams/lab-topology.md) | Separate baseline, segmented and backup paths |

---

## Public-safe starter artifacts

The repository includes a synthetic inventory example, validator and tests that can be used before any Proxmox hardware exists:

- [Synthetic inventory sample](https://github.com/DataTideHH/proxmox-virtualization-lab/blob/main/examples/inventory-sample.json)
- [Inventory validation script](https://github.com/DataTideHH/proxmox-virtualization-lab/blob/main/scripts/validate_sample_inventory.py)
- [Validator documentation](https://github.com/DataTideHH/proxmox-virtualization-lab/blob/main/scripts/README.md)
- [Unit tests](https://github.com/DataTideHH/proxmox-virtualization-lab/blob/main/tests/test_validate_sample_inventory.py)

Real node names, guest identifiers, addresses, tokens, fingerprints, storage names and private topology must remain outside the public repository.

---

## What this demonstrates

- structured infrastructure planning before implementation
- explicit separation between roadmap and verified results
- virtualization, networking, storage and recovery fundamentals
- least-privilege access and API thinking
- validation and rollback criteria rather than configuration alone
- public/private data separation
- tested synthetic data contracts before live collection
- preparation for operational inventory and data-quality workflows
- clear repository boundaries across Cisco, Proxmox and Data/BI work

---

## Related DataTideHH project pages

- [Cisco Switching Lab](https://datatidehh.github.io/cisco-switching-lab/) — physical switching, management, segmentation and troubleshooting
- [Network Operations Data Lab](https://datatidehh.github.io/network-operations-data-lab/) — sanitized infrastructure data, Python, SQL, data quality and BI-oriented reporting
- [Open Learning Resources](https://github.com/DataTideHH/open-learning-resources) — curated official documentation and standards references

---

## Next steps

1. evaluate suitable dedicated x86 hardware
2. document the selected hardware and console baseline
3. record the chosen installer and official integrity verification
4. install Proxmox and validate local console recovery
5. begin with one access-port network connection
6. create one Linux VM and one LXC container
7. configure one separate backup target and complete controlled restore tests
8. document the host reconstruction sequence
9. create a privilege-separated, expiring inventory API token
10. export only sanitized node and guest metadata to the Data/BI workflow

Only completed and validated work should move from roadmap status into the verified project baseline.
