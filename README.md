# Proxmox Virtualization Lab

[![CI](https://github.com/DataTideHH/proxmox-virtualization-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/DataTideHH/proxmox-virtualization-lab/actions/workflows/ci.yml)

Planned virtualization learning lab documenting architecture decisions, hardware selection, network integration, storage, backup, recovery, access control, validation and future API-based inventory.

Project page: https://datatidehh.github.io/proxmox-virtualization-lab/

## Current status

**Planning and pre-hardware preparation.**

A dedicated x86 host has not yet been acquired, and this repository does not claim an installed or verified Proxmox environment.

The current repository foundation contains:

- a clearly bounded project scope
- hardware selection criteria including a recoverable console path
- a staged architecture and implementation roadmap
- Cisco-aligned access-port and VLAN planning
- separate guest-backup, restore and host-recovery criteria
- least-privilege access and API principles
- a validation checklist
- a synthetic public-safe node and guest inventory example
- a standard-library Python validator and unit tests
- GitHub Actions validation on pull requests and pushes to `main`
- official Proxmox reference links

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
- local or independent console recovery
- virtual machines and LXC containers
- Linux bridges and future VLAN-aware networking
- storage layout
- snapshots, guest backups, restore tests and host reconstruction planning
- users, roles, ACLs and API tokens
- sanitized inventory export
- implementation logs and lessons learned

### This repository does not cover

- Cisco IOS configuration, which belongs in `cisco-switching-lab`
- analytical data modelling and Power BI, which belong in `network-operations-data-lab`
- production infrastructure claims
- enterprise-scale clustering without suitable hardware
- publishing real credentials, addresses, fingerprints or private topology
- presenting synthetic inventory as a live Proxmox export

## Repository structure

```text
proxmox-virtualization-lab/
├── .github/
│   └── workflows/ci.yml
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
│   ├── 08-official-references.md
│   └── 99-lessons-learned.md
├── diagrams/
│   └── lab-topology.md
├── examples/
│   └── inventory-sample.json
├── scripts/
│   ├── README.md
│   └── validate_sample_inventory.py
└── tests/
    └── test_validate_sample_inventory.py
```

## Pre-hardware work that is valid now

The following work can be completed before buying a host:

1. define hardware requirements and exclusions
2. require a physical or independent console recovery path
3. design the initial access-port network baseline
4. plan later VLAN and trunk stages
5. define storage, guest backup, restore and host reconstruction criteria
6. define least-privilege user, role, ACL and API-token principles
7. test synthetic inventory schemas locally and in CI
8. prepare a public-safe implementation log
9. maintain official references without fixing the project to one product release

## Synthetic inventory scope

Schema `0.1` covers **nodes and guests only**. The committed example and validator check:

- exact schema metadata and UTC timestamp format
- node and guest keys
- allowed status and type values
- positive integer resource fields
- guest-to-node relationships
- ownership, purpose and backup-policy classifications

Storage entities, virtual-network assignments and backup-run records remain planned until the corresponding live API fields and data-quality rules have been reviewed on a real lab system.

Run the current validation from the repository root:

```text
python scripts/validate_sample_inventory.py
python -m unittest discover -s tests -p "test_*.py" -v
```

On Windows, `py -3.12` can replace `python`.

## First implementation milestone

The first real milestone should remain deliberately small:

- one dedicated x86 host
- one recoverable console path
- one Ethernet connection
- one access-port lab VLAN
- one Linux VM
- one LXC container
- one backup target separate from the active guest datastore
- one successful VM and LXC restore test
- one documented host reconstruction sequence
- one least-privilege API token with privilege separation and expiration
- one sanitized node and guest inventory export

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
- ACL exports containing private identities
- backup credentials
- ISO images, VM disks, containers or backup archives

Use synthetic examples and placeholders in the public repository.

## Related repositories

- [DataTideHH/cisco-switching-lab](https://github.com/DataTideHH/cisco-switching-lab)
- [DataTideHH/network-operations-data-lab](https://github.com/DataTideHH/network-operations-data-lab)
- [DataTideHH/open-learning-resources](https://github.com/DataTideHH/open-learning-resources)

## Portfolio standard

This is a learning and documentation project, not a production infrastructure template. Claims should be limited to steps that have been completed and validated. For the current pre-hardware phase, the verified artifacts are the design decisions, public-safety boundaries, synthetic schema, validator, unit tests and CI workflow.
