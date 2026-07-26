# Project Scope

## Goal

Build a small, reproducible and public-safe Proxmox virtualization learning lab after suitable dedicated x86 hardware becomes available.

## Current phase

The project is currently in the planning and pre-hardware phase.

Valid current outputs include architecture decisions, selection criteria, security boundaries, synthetic examples, validation logic, unit tests and CI. Installation results must not be documented as completed until they have been tested on real hardware.

## In scope

- hardware selection
- installation baseline
- host update and validation workflow
- local or independent console recovery
- Linux bridges and staged VLAN integration
- VM and LXC lifecycle
- storage planning
- guest backup and restore testing
- host reconstruction planning
- roles, users and API tokens
- sanitized API inventory
- troubleshooting and lessons learned

## Current synthetic schema boundary

Schema `0.1` covers node and guest inventory only. It verifies identifiers, status values, resource allocations, ownership classification and guest-to-node relationships using synthetic public-safe data.

Storage, virtual-network assignment and backup-run entities remain planned until the corresponding live Proxmox API fields and data-quality rules have been reviewed.

## Out of scope

- production hosting
- public exposure of the management interface
- enterprise-scale cluster claims
- Ceph or high availability without suitable multi-node hardware
- publishing secrets or private infrastructure details
- pretending that synthetic data came from a live Proxmox system
- replacing the Cisco or Data/BI repositories

## Portfolio role

This is a supporting infrastructure project for a Data/BI and process-analysis profile. Its value comes from controlled implementation, operational validation, API awareness, data lineage, recovery thinking and clear documentation.
