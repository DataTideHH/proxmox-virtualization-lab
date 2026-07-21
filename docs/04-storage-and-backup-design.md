# Storage and Backup Design

## Key distinction

A snapshot is not automatically a backup. The lab must test restoration from a separately stored backup.

## Initial storage goals

- simple local SSD layout
- enough free capacity for test guests
- no production data
- clear distinction between host storage, guest disks, ISO images and backups
- documented capacity thresholds

## Initial backup goals

- one separate backup target
- scheduled test backup
- documented retention
- at least one successful restore test
- restore validation recorded in the implementation log

## Questions to decide after hardware selection

- single SSD or separate system and guest SSDs
- local directory or LVM-thin layout
- external disk, NAS or other backup target
- encryption requirements
- backup frequency
- retention periods
- acceptable recovery time for a learning guest

## Validation checklist

- storage is visible and healthy
- guest disk location is documented
- backup target is not confused with the guest datastore
- backup completes without errors
- restored guest starts in an isolated test
- timestamps and retention are understandable
- no backup archives are committed to GitHub
