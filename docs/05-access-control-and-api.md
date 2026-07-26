# Access Control and API

## Principles

- no public exposure of the management interface
- named user identities instead of shared administration where practical
- least privilege
- separate interactive and API identities
- privilege separation for the inventory token
- ACL roles and paths limited to reviewed read-only calls
- an explicit token expiration date
- local recovery path retained
- secrets stored outside Git

## Planned API identity

The first API identity should use the normal Proxmox user-and-token form:

```text
portfolio-reader@pve!inventory
```

This is a placeholder, not a real identity or token.

The token must use privilege separation. Its effective permissions are constrained by both the owning user's permissions and the token-specific ACL assignments. The design should grant only the read-only roles and paths needed for the reviewed inventory calls rather than describing access as an endpoint-only restriction.

A predefined read-only role such as `PVEAuditor` may be appropriate for some paths, but the final ACL design must be checked against the exact data collection calls. Do not grant broad administrative roles merely to simplify a first script.

## Planned lifecycle

1. create a named non-administrative user for inventory work
2. create a separate API token with privilege separation enabled
3. assign only reviewed read-only ACL roles and paths
4. configure an expiration date
5. inspect effective permissions
6. verify required reads
7. verify representative write operations are rejected
8. test token revocation
9. rotate or replace the token before expiry when the lab remains active

## Schema 0.1 data boundary

The current synthetic schema and validator cover only:

- node status and capacity
- VM and LXC inventory
- selected resource allocations
- ownership, purpose and backup-policy classification

The following entities remain planned until live API fields and data-quality rules have been reviewed:

- storage inventory and utilization
- virtual network assignment
- backup-run status and timestamps

## Public data boundary

Do not publish:

- real names and IDs
- IP and MAC addresses
- ticket cookies
- API token secrets
- cluster fingerprints
- raw private API responses
- backup credentials
- complete ACL exports
- private topology or certificate details

## Environment handling

Local secrets may be stored in an ignored `.env` file based on `.env.example`.

The public repository should contain only placeholders, synthetic responses and reviewed sanitized exports. TLS verification should remain enabled. A private certificate or fingerprint workflow may be documented later, but disabling verification must not become the default workaround.

## Future validation

- privilege separation is enabled
- token has an explicit expiration date
- effective permissions match the reviewed ACL design
- required inventory reads succeed
- write operations are rejected
- token revocation is tested
- access is limited to required paths
- TLS verification behavior is documented
- failed authentication is handled safely
- logs do not print token secrets
- exports are sanitized before entering the public repository
