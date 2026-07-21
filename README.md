# Proxmox Virtualization Lab

Planned virtualization learning lab documenting architecture decisions, hardware selection, network integration, storage, backup, access control, validation and future API-based inventory.

## Current status

**Planning and pre-hardware preparation.**

A dedicated x86 host has not yet been acquired, and this repository does not claim an installed or verified Proxmox environment.

The current repository foundation contains:

- a clearly bounded project scope
- hardware selection criteria
- a staged architecture and implementation roadmap
- planned Cisco network integration
- storage and backup design questions
- access-control and API principles
- a validation checklist
- synthetic public-safe inventory examples
- a small Python validator that can be used without Proxmox hardware

## Purpose

The project is intended to build practical understanding of virtualization infrastructure while supporting a Data/BI-oriented portfolio.

The future lab should connect three separate layers:

```text
cisco-switching-lab
        |
        | physical ports, VLANs and trunks
        v
proxmox-virtualization-lab
        |
        | nodes, guests, storage, networks and backups
        v
network-operations-data-lab
        |
        | Python, SQLite, SQL, data quality and Power BI
        v
operational reporting
```

## Repository boundaries

### This repository covers

- dedicated host selection and baseline
- Proxmox installation and validation
- virtual machines and LXC containers
- Linux bridges and future VLAN-aware networking
- storage layout
- snapshots, backups and restore tests
- users, roles and API tokens
- sanitized inventory export
- implementation logs and lessons learned

### This repository does not cover

- Cisco IOS configuration, which belongs in `cisco-switching-lab`
- analytical data modelling and Power BI, which belong in `network-operations-data-lab`
- production infrastructure claims
- enterprise-scale clustering without suitable hardware
- publishing real credentials, addresses, fingerprints or private topology

## Planned repository structure

```text
proxmox-virtualization-lab/
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── docs/
│   ├── 00-project-scope.md
│   ├── 01-hardware-selection.md
│   ├── 02-architecture-roadmap.md
│   ├── 03-network-design.md
│   ├── 04-storage-and-backup-design.md
│   ├── 05-access-control-and-api.md
│   ├── 06-validation-checklist.md
│   ├── 07-implementation-log.md
│   └── 99-lessons-learned.md
├── diagrams/
│   └── lab-topology.md
├── examples/
│   └── inventory-sample.json
└── scripts/
    ├── README.md
    └── validate_sample_inventory.py
```

## Pre-hardware work that is valid now

The following work can be completed before buying a host:

1. define hardware requirements and exclusions
2. design the initial access-port network baseline
3. plan later VLAN and trunk stages
4. define storage, backup and restore acceptance criteria
5. define least-privilege access and API principles
6. test synthetic inventory schemas locally
7. prepare a public-safe implementation log

## First implementation milestone

The first real milestone should remain deliberately small:

- one dedicated x86 host
- one Ethernet connection
- one lab VLAN
- one Linux VM
- one LXC container
- one backup target
- one successful restore test
- one least-privilege API token
- one sanitized inventory export

Cluster, Ceph, high availability and complex software-defined networking are not required for the first portfolio milestone.

## Public-safety policy

Never commit:

- passwords or password hashes
- API tokens or ticket cookies
- private keys
- real management IP addresses
- complete private topology
- cluster fingerprints
- real node, guest or storage names
- raw private API responses
- backup credentials
- ISO images, VM disks, containers or backup archives

Use synthetic examples and placeholders in the public repository.

## Related repositories

- `DataTideHH/cisco-switching-lab`
- `DataTideHH/network-operations-data-lab`

## Portfolio standard

This is a learning and documentation project, not a production infrastructure template. Claims should be limited to steps that have been completed and validated.
