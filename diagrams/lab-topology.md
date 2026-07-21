# Planned Lab Topology

```text
Existing home network
        |
        | isolated lab path
        |
Cisco lab router or gateway
        |
        | lab VLANs
        |
Cisco Catalyst switch
        |
        | access port first
        | optional later 802.1Q trunk
        |
future dedicated x86 Proxmox host
        |
        +-- Linux VM
        |
        +-- LXC container
        |
        +-- backup target
        |
        +-- read-only inventory API
                    |
                    v
        sanitized sample export
                    |
                    v
        network-operations-data-lab
```

## Current implementation status

Only the Cisco-side physical lab exists. The Proxmox host and all objects beneath it are planned future components.
