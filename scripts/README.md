# Scripts

## Current validator

`validate_sample_inventory.py` validates the synthetic public-safe example under `examples/inventory-sample.json`.

It does not connect to a Proxmox host, authenticate to an API or claim that a live environment exists.

Run from the repository root:

```bash
python scripts/validate_sample_inventory.py
```

On Windows with the Python launcher:

```powershell
py -3.12 scripts/validate_sample_inventory.py
```

The validator checks:

- exact schema version and public-safe sample type
- ISO 8601 UTC collection timestamp ending in `Z`
- node and guest collections containing objects
- unique node and guest keys
- allowed node status, guest types and guest status values
- positive integer resource values without accepting booleans
- guest-to-node relationships
- required ownership, purpose and backup-policy text fields

## Unit tests

Run the standard-library test suite from the repository root:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

On Windows:

```powershell
py -3.12 -m unittest discover -s tests -p "test_*.py" -v
```

GitHub Actions runs syntax checks, the unit tests and validation of the committed sample on pull requests and pushes to `main`.

## Deliberate boundary

Schema `0.1` covers node and guest inventory only. Storage entities, virtual-network assignments and backup-run records remain planned until the corresponding live API fields and data-quality rules have been reviewed on a real lab system.

A future live collector should be added only after dedicated hardware exists, required API calls have been reviewed and least-privilege permissions have been validated.
