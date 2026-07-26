# Planned Lab Topology

## Stage 1: first verified baseline

```text
Existing home or lab gateway
        |
Cisco Catalyst switch
        |
        | access port in VLAN 20
        |
future dedicated x86 Proxmox host
        |
        +-- Linux VM
        |
        +-- LXC container

Separate backup target
        ^
        |
        +-- tested VM and LXC backups from the Proxmox host
```

The first stage requires one recoverable access-port connection. It does not depend on a Cisco router, an 802.1Q trunk or a dedicated management VLAN.

## Later segmented stage

```text
Existing home network
        |
optional isolated lab gateway or router
        |
Cisco Catalyst switch
        |
        | 802.1Q trunk
        | tagged: VLAN 20, 30 and 99
        | native but unused: VLAN 998
        |
Proxmox VLAN-aware bridge
        |
        +-- tagged management on VLAN 99
        +-- lab guests on VLAN 20
        +-- server and service guests on VLAN 30

Separate backup target
        ^
        |
        +-- scheduled backups and controlled restore tests

Read-only inventory API
        |
        v
sanitized node and guest sample export
        |
        v
network-operations-data-lab
```

VLAN 999 remains a Cisco-side parking VLAN for unused access ports and is not part of the Proxmox trunk.

## Current implementation status

Only the Cisco-side physical switch lab exists. The Proxmox host, guests, backup target, API identity and segmented network shown here are planned future components.
