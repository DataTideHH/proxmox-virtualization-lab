# Official References

Reviewed: 2026-07-26

Use the documentation matching the release actually installed on the future lab host. These links are reference starting points, not a fixed product-version requirement for the repository.

## Proxmox VE documentation

- [Proxmox VE documentation index](https://pve.proxmox.com/pve-docs/)
  - administration guide, command references and generated product documentation
- [Proxmox VE Administration Guide](https://pve.proxmox.com/pve-docs/pve-admin-guide.html)
  - installation, package repositories, networking, storage, backup, permissions and operations
- [Proxmox VE API Viewer](https://pve.proxmox.com/pve-docs/api-viewer/)
  - authoritative path and parameter reference for reviewed future inventory calls
- [Proxmox VE Network Configuration](https://pve.proxmox.com/wiki/Network_Configuration)
  - Linux bridges, VLAN-aware designs and other supported host-network patterns
- [Proxmox VE User Management CLI Reference](https://pve.proxmox.com/pve-docs/pveum.1.html)
  - users, groups, roles, ACLs and API-token properties
- [Proxmox VE Backup and Restore](https://pve.proxmox.com/pve-docs/chapter-vzdump.html)
  - guest backup modes, scheduling, retention and restore concepts
- [Proxmox Container Toolkit](https://pve.proxmox.com/pve-docs/chapter-pct.html)
  - LXC lifecycle, mount points and backup/restore behavior

## Installer and integrity information

- [Official Proxmox VE ISO downloads](https://www.proxmox.com/en/downloads/proxmox-virtual-environment/iso)
- [Proxmox ISO directory and signature guidance](https://enterprise.proxmox.com/iso/)

At review time, the current published Proxmox VE ISO was `9.2-1`. This is a time-stamped reference only. Before installation, record the actual filename, release, official SHA-256 value, installation date and signature or checksum verification used for the selected image.

After installation, record privately:

```text
installer filename
release and installation date
official integrity value
pveversion -v output
configured package repository channel
package state after the initial update
```

Do not publish real host identifiers, subscription details, repository credentials or private configuration output.

## Project application rules

- verify documentation against the installed release
- prefer the official guide and API Viewer over copied command snippets
- retain physical or independent console access during network and major update changes
- treat guest backup, guest restore and host reconstruction as separate validation concerns
- review LXC bind and device mount behavior before claiming complete backups
- configure API access through reviewed roles and ACL paths rather than broad administrator rights
- keep TLS verification enabled and secrets outside Git
- add storage, network and backup-run entities to the public schema only after live fields are reviewed

## Related curated learning repository

- [DataTideHH/open-learning-resources](https://github.com/DataTideHH/open-learning-resources)
  - curated official documentation and standards references used across the portfolio
- [GitHub Actions Documentation](https://github.com/DataTideHH/open-learning-resources/tree/main/resources/git/github-actions-documentation)
  - workflow and CI reference for the public-safe Python validation job
- [Cisco Catalyst 3560-CX IOS 15.2E Reference](https://github.com/DataTideHH/open-learning-resources/tree/main/resources/networking/cisco-catalyst-3560cx-ios-15-2e-reference)
  - switch-side reference for the separate Cisco lab
