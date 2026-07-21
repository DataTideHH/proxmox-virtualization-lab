# Network Design

## Design principle

Start with the simplest recoverable design and add segmentation only after the single-node baseline is stable.

## Stage 1: access-port baseline

```text
home or lab gateway
        |
Cisco lab switch
        |
single access port
        |
future Proxmox host
        |
default Linux bridge
        |
initial VM and LXC
```

Acceptance criteria:

- expected link speed and duplex
- stable management reachability
- no unexpected switch interface errors
- local console recovery available
- no public port forwarding

## Stage 2: management separation

- dedicated management VLAN
- explicitly allowed management clients
- documented gateway and DNS behavior
- NTP consistency between switch and host
- guest networks unable to reach management by default

## Stage 3: optional VLAN trunk

- dedicated 802.1Q trunk
- allow only required VLANs
- document native and tagged VLAN behavior
- configure VLAN-aware bridges only after access-port recovery is documented
- validate each VLAN separately

## Planned VLAN roles

| VLAN | Role | Status |
|---:|---|---|
| 20 | general lab | planned |
| 30 | server and guest services | planned |
| 99 | management | planned |
| 999 | unused-port blackhole | Cisco-side roadmap |

## Repository boundary

Cisco switch configuration belongs in `cisco-switching-lab`. This document covers the Proxmox-side design and acceptance criteria.
