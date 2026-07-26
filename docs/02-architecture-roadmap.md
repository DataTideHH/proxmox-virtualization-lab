# Architecture Roadmap

## Phase 0: pre-hardware preparation

- define scope and boundaries
- define hardware acceptance criteria including a recoverable console path
- prepare access-port-first network and storage designs
- define backup, guest restore and host reconstruction criteria
- define least-privilege API principles
- test synthetic node and guest inventory schema `0.1`
- run unit tests and CI without claiming a live Proxmox environment
- keep all implementation claims marked as planned

## Phase 1: single-node baseline

- verify installer filename and official integrity information
- install one Proxmox node
- record the installed release, package repository channel and package baseline privately
- configure updates and time synchronization
- validate local console recovery, storage and networking
- create one Linux VM
- create one LXC container
- document start, stop, restart and console access
- record a verified baseline

## Phase 2: backup and recovery

- configure a backup target separate from the active guest datastore
- run VM and LXC backups
- restore into a controlled isolated test
- document retention assumptions
- distinguish snapshots from backups
- review LXC bind and device mount exclusions
- document the minimum host reconstruction sequence separately from guest restore

## Phase 3: network segmentation

- begin with one access VLAN
- introduce management VLAN 99 only after the baseline works
- add an 802.1Q trunk only with Cisco rollback and console recovery prepared
- keep VLAN 998 native and unused
- keep VLAN 999 on the Cisco side for unused access ports
- map guest networks explicitly
- validate management and guest VLANs separately

## Phase 4: access control and API

- create named administrative identities
- separate interactive administration from API access
- create a least-privilege inventory token with privilege separation
- assign only reviewed read-only roles and paths
- configure an expiration date
- inspect effective permissions and token disablement behavior
- export only required metadata
- retain raw private responses outside GitHub

## Phase 5: Data/BI integration

- sanitize source identifiers
- export reviewed node and guest inventory
- pass data to `network-operations-data-lab`
- validate completeness, relationships and freshness
- add storage, virtual-network or backup-run entities only after live fields are reviewed
- build a small Power BI reporting concept

## Deferred topics

- multi-node cluster
- high availability
- Ceph
- live migration
- advanced SDN
- production workloads
- infrastructure automation without a validated target platform

These topics should be added only when the hardware, operational evidence and learning purpose justify them.
