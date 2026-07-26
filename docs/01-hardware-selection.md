# Hardware Selection

## Current status

No dedicated x86 host has been selected.

## Minimum practical target

- x86-64 CPU with hardware virtualization support
- 16 GB RAM minimum
- 32 GB RAM preferred
- reliable Ethernet interface
- SSD storage
- local physical console access or an independently validated out-of-band console
- firmware settings that permit virtualization
- hardware that can remain separate from the main iMac and school devices

A recoverable console path is required for the first host. Network, bridge, VLAN or management-address changes must not depend on the same interface being changed as the only recovery method.

## Preferred target

- business mini PC or small-form-factor desktop
- replaceable SSD
- upgradeable RAM
- quiet idle operation
- reasonable power consumption
- documented firmware updates
- at least one stable 1 GbE interface
- optional second Ethernet interface, but not required initially
- optional IPMI, iKVM or equivalent out-of-band management

## Exclusions

- the private main iMac
- school-owned ThinkPad or BBQ desktop
- systems without reliable wired networking
- devices without a practical local or independent recovery console
- devices requiring unsupported workarounds for basic operation
- hardware bought only to imitate enterprise scale

## Evaluation checklist

| Criterion | Required | Notes |
|---|---:|---|
| x86-64 architecture | yes | dedicated Proxmox target |
| hardware virtualization | yes | verify in firmware |
| 16 GB RAM | yes | usable minimum |
| 32 GB RAM | preferred | more comfortable for multiple guests |
| SSD | yes | host and guest storage |
| wired Ethernet | yes | stable lab networking |
| local or independent console | yes | recovery during network and upgrade failures |
| RAM upgradeable | preferred | extends useful life |
| second NIC | optional | later routing or separation experiments |
| out-of-band management | optional | useful but not required when physical console access is reliable |
| low idle power | preferred | suitable for a home lab |

## Purchase principle

Buy only after the first lab use cases are defined. A modest, stable and well-documented host is more valuable than an oversized system with no clear workload.
