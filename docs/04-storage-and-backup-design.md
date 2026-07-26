# Storage and Backup Design

## Key distinctions

A snapshot is not automatically a backup. The lab must test restoration from a separately stored backup.

Guest backups also do not replace a host recovery plan. Recovering a VM or LXC archive and rebuilding a failed Proxmox host are separate procedures with different evidence and dependencies.

## Initial storage goals

- simple local SSD layout
- enough free capacity for test guests
- no production data
- clear distinction between host storage, guest disks, ISO images and backups
- documented capacity thresholds
- no assumption that local guest storage is also a backup target

## Initial backup goals

- one backup target separate from the guest datastore
- scheduled test backups for one VM and one LXC container
- documented retention
- at least one successful controlled restore test
- restore validation recorded in the implementation log
- review of any LXC bind or device mount because its contents may require a separate backup method

The first target may be an external disk, NAS-backed storage or another suitable destination. Proxmox Backup Server is optional and should be introduced only when its operational value justifies the additional system.

## Host recovery plan

Before treating the lab as recoverable, document privately:

- installer filename and official integrity verification
- installed release and `pveversion -v` output
- package repository channel and package state after updates
- firmware and virtualization settings
- network interface names and bridge design
- storage layout and content types
- the minimum reviewed host and cluster configuration needed for reconstruction
- how the separate backup target becomes available after reinstallation
- the order for restoring the VM and LXC container

Do not publish real hostnames, addresses, certificates, fingerprints, credentials or raw configuration archives.

## Questions to decide after hardware selection

- single SSD or separate system and guest SSDs
- local directory or LVM-thin layout
- external disk, NAS or other backup target
- encryption requirements
- backup frequency
- retention periods
- acceptable recovery time for a learning guest
- which host configuration information is required for reconstruction
- whether any guest uses bind, device or external mount points that need separate protection

## Guest backup and restore validation

- storage is visible and healthy
- guest disk location is documented
- backup target is distinct from the active guest datastore
- backup completes without errors
- restored guest starts in an isolated test
- expected services and data are checked after restore
- timestamps and retention are understandable
- LXC mount-point exclusions are reviewed
- no backup archives are committed to GitHub

## Host recovery validation

- physical or out-of-band console path is available
- installation media and integrity evidence are recorded
- host reconstruction steps are documented without secrets
- network and storage dependencies are ordered explicitly
- the separate backup target can be reattached
- one reviewed guest restore can be completed after the reconstructed baseline exists
