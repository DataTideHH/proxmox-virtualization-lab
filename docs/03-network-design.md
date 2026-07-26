# Network Design

## Design principle

Start with the simplest recoverable design and add segmentation only after the single-node baseline is stable.

Every bridge, VLAN or management-address change requires a documented rollback and a local or independent console path before implementation.

## Stage 1: access-port baseline

```text
home or lab gateway
        |
Cisco lab switch
        |
single access port in VLAN 20
        |
future Proxmox host
        |
default Linux bridge
        |
initial VM and LXC
```

This is the first implementation target. It does not require a Cisco router, an 802.1Q trunk or a VLAN-aware bridge.

Acceptance criteria:

- expected link speed and duplex
- stable management reachability
- no unexpected switch interface errors
- local or independent console recovery available
- no public port forwarding
- bridge and addressing baseline recorded privately

## Stage 2: management separation

- dedicated management VLAN 99
- explicitly allowed management clients
- documented gateway and DNS behavior
- NTP consistency between switch and host
- guest networks unable to reach management by default
- management reachability validated before removing the earlier access-port baseline

## Stage 3: optional VLAN trunk

- dedicated 802.1Q trunk
- allow only VLANs `20,30,99,998`
- VLAN 99 carries tagged Proxmox management traffic
- VLAN 998 is the matching unused native VLAN and carries no host, guest or management address
- VLAN 999 remains a Cisco-side parking VLAN for unused access ports and is not allowed on the Proxmox trunk
- configure a VLAN-aware Linux bridge only after access-port recovery is documented
- validate each tagged VLAN separately
- retain console access until the trunk and management path are proven stable

## Planned VLAN roles

| VLAN | Role | Proxmox use | Status |
|---:|---|---|---|
| 20 | LAB | initial access-port baseline and general lab guests | planned |
| 30 | SERVERS_GUESTS | later server and guest services | planned |
| 99 | MGMT | tagged host management after separation is validated | planned |
| 998 | NATIVE_UNUSED | no SVI, host address or guest assignment | planned trunk control |
| 999 | BLACKHOLE | none; Cisco-side parking VLAN for unused access ports | Cisco-side roadmap |

## Recovery order for network changes

1. record the current switch port and Proxmox bridge state
2. confirm physical or out-of-band console access
3. prepare the Cisco rollback commands in `cisco-switching-lab`
4. change one layer at a time
5. verify link, management reachability, gateway, DNS and NTP
6. verify guest VLAN behavior separately
7. roll back immediately if the management path becomes ambiguous

## Repository boundary

Cisco switch configuration belongs in `cisco-switching-lab`. This document covers the Proxmox-side design, dependency order, acceptance criteria and recovery requirements.
