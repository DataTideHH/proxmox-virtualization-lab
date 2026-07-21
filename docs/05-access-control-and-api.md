# Access Control and API

## Principles

- no public exposure of the management interface
- named user identities instead of shared administration where practical
- least privilege
- separate interactive and API identities
- local recovery path retained
- secrets stored outside Git

## Planned API identity

The first API token should be read-only and limited to the inventory endpoints required for the portfolio workflow.

Example placeholder:

```text
portfolio-reader@example!inventory
```

This is not a real token identifier.

## Data collection boundary

Collect only metadata needed for the documented model:

- node status and capacity
- VM and LXC inventory
- selected resource allocations
- storage status and utilization
- virtual network assignment
- backup status and timestamps

Do not publish:

- real names and IDs
- IP and MAC addresses
- ticket cookies
- API token secrets
- cluster fingerprints
- raw private API responses
- backup credentials

## Environment handling

Local secrets may be stored in an ignored `.env` file based on `.env.example`.

The public repository should contain only placeholders and synthetic responses.

## Future validation

- token cannot perform write actions
- token access is limited to required paths
- TLS verification behavior is documented
- failed authentication is handled safely
- logs do not print token secrets
- exports are sanitized before entering the public repository
