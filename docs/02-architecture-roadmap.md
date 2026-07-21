# Architecture Roadmap

## Phase 0: pre-hardware preparation

- define scope and boundaries
- define hardware acceptance criteria
- prepare network and storage designs
- define validation steps
- test synthetic inventory schemas
- keep all implementation claims marked as planned

## Phase 1: single-node baseline

- install one Proxmox node
- configure updates and time synchronization
- validate storage and networking
- create one Linux VM
- create one LXC container
- document start, stop, restart and console access
- record a verified baseline

## Phase 2: backup and recovery

- configure a backup target
- run VM and LXC backups
- restore into a controlled test
- document retention assumptions
- distinguish snapshots from backups

## Phase 3: network segmentation

- begin with one access VLAN
- introduce a management VLAN only after the baseline works
- add an 802.1Q trunk only with Cisco rollback and console recovery prepared
- map guest networks explicitly

## Phase 4: access control and API

- create named administrative identities
- separate interactive administration from API access
- create a least-privilege inventory token
- export only required metadata
- retain raw private responses outside GitHub

## Phase 5: Data/BI integration

- sanitize source identifiers
- export reviewed sample inventory
- pass data to `network-operations-data-lab`
- validate completeness, relationships and freshness
- build a small Power BI reporting concept

## Deferred topics

- multi-node cluster
- high availability
- Ceph
- live migration
- advanced SDN
- production workloads

These topics should be added only when the hardware and learning purpose justify them.
