# Scripts

## Current script

`validate_sample_inventory.py` validates the synthetic public-safe example under `examples/inventory-sample.json`.

It does not connect to a Proxmox host.

Run from the repository root:

```bash
python3 scripts/validate_sample_inventory.py
```

The script checks:

- required top-level fields
- unique node and guest keys
- allowed guest types
- guest-to-node relationships
- non-negative resource allocations
- required ownership, purpose and backup-policy fields

A future live collector should be added only after dedicated hardware exists and the required API permissions have been reviewed.
