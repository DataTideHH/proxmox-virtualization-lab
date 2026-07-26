# Lessons Learned

## Pre-hardware lessons

- architecture can be prepared without pretending that implementation exists
- clear repository boundaries prevent duplicated or inflated portfolio claims
- access-port-first networking reduces recovery risk
- network changes need a console path independent from the interface being changed
- management VLAN, unused native VLAN and unused-port parking VLAN are different roles
- a backup target should be represented separately from the active guest datastore
- guest restore and host reconstruction require separate plans
- LXC bind and device mounts need explicit backup review
- API access should begin with reviewed data needs, privilege separation, limited ACL paths and expiration
- synthetic examples are useful for testing schemas before live data exists
- a small schema with tests is stronger than speculative entities based on unreviewed API fields
- CI can verify public-safe code and data contracts without implying that hardware has been installed

## Future entries

Add only findings that were observed during real installation, validation, failure analysis or recovery.
