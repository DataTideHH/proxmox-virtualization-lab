---
layout: default
title: Proxmox Virtualization Lab
description: Public-safe virtualization learning lab for architecture, networking, storage, backup, access control and future operational data integration.
---

# Proxmox Virtualization Lab

**A public-safe learning and portfolio project documenting the planned path from dedicated x86 hardware to a small, validated Proxmox environment and later operational data integration.**

[View repository](https://github.com/DataTideHH/proxmox-virtualization-lab) · [Read the full README](https://github.com/DataTideHH/proxmox-virtualization-lab/blob/main/README.md) · [DataTideHH portfolio](https://datatidehh.de/)

---

## Current status

**Planning and pre-hardware preparation.**

A dedicated x86 host has not yet been acquired. This project does not claim an installed or verified Proxmox environment.

The current repository already provides a structured foundation for:

- hardware selection and exclusions
- staged architecture decisions
- conservative Cisco network integration
- storage, backup and restore planning
- least-privilege access and API design
- public-safe validation criteria
- synthetic inventory examples
- a small Python inventory validator

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
sanitized node, guest, storage, network and backup metadata
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
| Hardware | Dedicated-host requirements, exclusions and future baseline |
| Installation | Planned Proxmox installation and validation sequence |
| Networking | Linux bridges, an access-port-first baseline and later VLAN-aware options |
| Guests | Small VM and LXC lifecycle exercises after hardware exists |
| Storage | Storage layout, capacity decisions and separation of concerns |
| Backup | Backup policy, restore testing and evidence of recoverability |
| Security | Users, roles, least-privilege API tokens and private/public separation |
| Operations data | Sanitized inventory exports for the separate Data/BI workflow |

---

## First implementation milestone

The first verified hardware stage should remain deliberately small:

- one dedicated x86 host
- one Ethernet connection
- one controlled lab VLAN
- one Linux virtual machine
- one LXC container
- one backup target
- one successful restore test
- one least-privilege API token
- one sanitized inventory export

Cluster, Ceph, high availability and complex software-defined networking are not required for the first portfolio milestone.

---

## Documentation

| Document | Purpose |
|---|---|
| [Project scope](00-project-scope.md) | Boundaries, learning goals and portfolio role |
| [Hardware selection](01-hardware-selection.md) | Host requirements, useful features and exclusions |
| [Architecture roadmap](02-architecture-roadmap.md) | Staged path from planning to validated operation |
| [Network design](03-network-design.md) | Access-port-first integration and later segmentation options |
| [Storage and backup design](04-storage-and-backup-design.md) | Storage questions, backup policy and restore criteria |
| [Access control and API](05-access-control-and-api.md) | Users, roles, tokens and least-privilege principles |
| [Validation checklist](06-validation-checklist.md) | Planned acceptance checks for each implementation stage |
| [Implementation log](07-implementation-log.md) | Public-safe record for future verified work |
| [Lessons learned](99-lessons-learned.md) | Findings and revisions as the lab develops |
| [Lab topology](../diagrams/lab-topology.md) | Sanitized current and planned cross-layer architecture |

---

## Public-safe starter artifacts

The repository includes a synthetic inventory example and a small Python validator that can be used before any Proxmox hardware exists:

- [Synthetic inventory sample](https://github.com/DataTideHH/proxmox-virtualization-lab/blob/main/examples/inventory-sample.json)
- [Inventory validation script](https://github.com/DataTideHH/proxmox-virtualization-lab/blob/main/scripts/validate_sample_inventory.py)
- [Script documentation](https://github.com/DataTideHH/proxmox-virtualization-lab/blob/main/scripts/README.md)

Real node names, guest identifiers, addresses, tokens, fingerprints, storage names and private topology must remain outside the public repository.

---

## What this demonstrates

- structured infrastructure planning before implementation
- explicit separation between roadmap and verified results
- virtualization, networking, storage and backup fundamentals
- least-privilege access and API thinking
- validation and recovery criteria rather than configuration alone
- public/private data separation
- preparation for operational inventory and data-quality workflows
- clear repository boundaries across Cisco, Proxmox and Data/BI work

---

## Related DataTideHH project pages

- [Cisco Switching Lab](https://datatidehh.github.io/cisco-switching-lab/) — physical switching, management, segmentation and troubleshooting
- [Network Operations Data Lab](https://datatidehh.github.io/network-operations-data-lab/) — sanitized infrastructure data, Python, SQL, data quality and BI-oriented reporting

---

## Next steps

1. evaluate suitable dedicated x86 hardware
2. document the selected hardware baseline
3. install Proxmox and validate local console recovery
4. begin with one access-port network connection
5. create one Linux VM and one LXC container
6. configure one backup target and complete a restore test
7. create a least-privilege inventory API token
8. export only sanitized operational metadata to the Data/BI workflow

Only completed and validated work should move from roadmap status into the verified project baseline.
