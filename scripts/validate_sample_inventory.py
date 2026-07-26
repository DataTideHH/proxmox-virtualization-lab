#!/usr/bin/env python3
"""Validate the repository's synthetic Proxmox inventory example.

This script does not connect to a live Proxmox host.
"""

from __future__ import annotations

from datetime import datetime, timedelta
import json
from pathlib import Path
import sys
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_PATH = REPO_ROOT / "examples" / "inventory-sample.json"
EXPECTED_SCHEMA_VERSION = "0.1"
EXPECTED_SAMPLE_TYPE = "synthetic-public-safe"
ALLOWED_NODE_STATUS = {"online", "offline", "unknown"}
ALLOWED_GUEST_TYPES = {"qemu", "lxc"}
ALLOWED_GUEST_STATUS = {"running", "stopped", "template", "unknown"}


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError:
        raise ValueError(f"Sample file not found: {path}") from None
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError("Top-level JSON value must be an object.")
    return data


def require_mapping_list(data: dict[str, Any], key: str) -> list[dict[str, Any]]:
    value = data.get(key)
    if not isinstance(value, list):
        raise ValueError(f"'{key}' must be a list.")

    mappings: list[dict[str, Any]] = []
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            raise ValueError(f"'{key}[{index}]' must be an object.")
        mappings.append(item)
    return mappings


def is_positive_int(value: Any) -> bool:
    return type(value) is int and value > 0


def is_utc_z_timestamp(value: Any) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False

    try:
        parsed = datetime.fromisoformat(f"{value[:-1]}+00:00")
    except ValueError:
        return False

    return parsed.utcoffset() == timedelta(0)


def validate_inventory(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    if data.get("schema_version") != EXPECTED_SCHEMA_VERSION:
        errors.append(
            f"schema_version must be {EXPECTED_SCHEMA_VERSION!r}"
        )

    if data.get("sample_type") != EXPECTED_SAMPLE_TYPE:
        errors.append(f"sample_type must be {EXPECTED_SAMPLE_TYPE!r}")

    if not is_utc_z_timestamp(data.get("collected_at_utc")):
        errors.append("collected_at_utc must be an ISO 8601 UTC timestamp ending in 'Z'")

    try:
        nodes = require_mapping_list(data, "nodes")
    except ValueError as exc:
        errors.append(str(exc))
        nodes = []

    try:
        guests = require_mapping_list(data, "guests")
    except ValueError as exc:
        errors.append(str(exc))
        guests = []

    node_keys: set[str] = set()
    for index, node in enumerate(nodes):
        node_key = node.get("node_key")
        if not isinstance(node_key, str) or not node_key.strip():
            errors.append(f"nodes[{index}] has no valid node_key")
            continue
        if node_key in node_keys:
            errors.append(f"Duplicate node_key: {node_key}")
        node_keys.add(node_key)

        node_status = node.get("node_status")
        if node_status not in ALLOWED_NODE_STATUS:
            errors.append(
                f"Node {node_key}: node_status must be one of "
                f"{sorted(ALLOWED_NODE_STATUS)}"
            )

        for numeric_field in ("cpu_threads", "memory_total_mb", "storage_total_gb"):
            value = node.get(numeric_field)
            if not is_positive_int(value):
                errors.append(
                    f"Node {node_key}: {numeric_field} must be a positive integer"
                )

    guest_keys: set[str] = set()
    for index, guest in enumerate(guests):
        guest_key = guest.get("guest_key")
        if not isinstance(guest_key, str) or not guest_key.strip():
            errors.append(f"guests[{index}] has no valid guest_key")
            continue
        if guest_key in guest_keys:
            errors.append(f"Duplicate guest_key: {guest_key}")
        guest_keys.add(guest_key)

        node_key = guest.get("node_key")
        if node_key not in node_keys:
            errors.append(f"Guest {guest_key}: unknown node_key {node_key!r}")

        guest_type = guest.get("guest_type")
        if guest_type not in ALLOWED_GUEST_TYPES:
            errors.append(
                f"Guest {guest_key}: guest_type must be one of "
                f"{sorted(ALLOWED_GUEST_TYPES)}"
            )

        guest_status = guest.get("guest_status")
        if guest_status not in ALLOWED_GUEST_STATUS:
            errors.append(
                f"Guest {guest_key}: guest_status must be one of "
                f"{sorted(ALLOWED_GUEST_STATUS)}"
            )

        for numeric_field in ("cpu_allocated", "memory_allocated_mb"):
            value = guest.get(numeric_field)
            if not is_positive_int(value):
                errors.append(
                    f"Guest {guest_key}: {numeric_field} must be a positive integer"
                )

        for required_field in (
            "purpose_category",
            "owner_role",
            "backup_policy_key",
        ):
            value = guest.get(required_field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"Guest {guest_key}: missing or invalid {required_field}")

    return errors


def main() -> int:
    try:
        data = load_json(SAMPLE_PATH)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    errors = validate_inventory(data)
    if errors:
        print("Inventory validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Inventory validation passed.")
    print(f"Schema: {data['schema_version']}")
    print(f"Nodes: {len(data['nodes'])}")
    print(f"Guests: {len(data['guests'])}")
    print(f"Sample: {SAMPLE_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
