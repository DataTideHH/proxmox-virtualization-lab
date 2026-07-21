# Project Scope

## Goal

Build a small, reproducible and public-safe Proxmox virtualization learning lab after suitable dedicated x86 hardware becomes available.

## Current phase

The project is currently in the planning and pre-hardware phase.

Valid current outputs include architecture decisions, selection criteria, security boundaries, synthetic examples and validation logic. Installation results must not be documented as completed until they have been tested on real hardware.

## In scope

- hardware selection
- installation baseline
- host update and validation workflow
- Linux bridges and staged VLAN integration
- VM and LXC lifecycle
- storage planning
- backup and restore testing
- roles, users and API tokens
- sanitized API inventory
- troubleshooting and lessons learned

## Out of scope

- production hosting
- public exposure of the management interface
- enterprise-scale cluster claims
- Ceph or high availability without suitable multi-node hardware
- publishing secrets or private infrastructure details
- replacing the Cisco or Data/BI repositories

## Portfolio role

This is a supporting infrastructure project for a Data/BI and process-analysis profile. Its value comes from controlled implementation, operational validation, API awareness, data lineage and clear documentation.
