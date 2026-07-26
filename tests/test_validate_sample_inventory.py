from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest

from scripts.validate_sample_inventory import load_json, validate_inventory


REPO_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_PATH = REPO_ROOT / "examples" / "inventory-sample.json"


class InventoryValidatorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.valid_sample = load_json(SAMPLE_PATH)

    def sample(self) -> dict:
        return deepcopy(self.valid_sample)

    def test_repository_sample_is_valid(self) -> None:
        self.assertEqual([], validate_inventory(self.sample()))

    def test_schema_version_is_exact(self) -> None:
        data = self.sample()
        data["schema_version"] = "1.0"
        self.assertIn("schema_version must be '0.1'", validate_inventory(data))

    def test_sample_type_is_exact(self) -> None:
        data = self.sample()
        data["sample_type"] = "live-export"
        self.assertIn(
            "sample_type must be 'synthetic-public-safe'",
            validate_inventory(data),
        )

    def test_timestamp_must_be_utc_and_end_in_z(self) -> None:
        data = self.sample()
        data["collected_at_utc"] = "2026-07-21T20:00:00+02:00"
        self.assertIn(
            "collected_at_utc must be an ISO 8601 UTC timestamp ending in 'Z'",
            validate_inventory(data),
        )

    def test_node_status_is_constrained(self) -> None:
        data = self.sample()
        data["nodes"][0]["node_status"] = "degraded"
        errors = validate_inventory(data)
        self.assertTrue(any("node_status must be one of" in error for error in errors))

    def test_numeric_fields_require_positive_ints_and_reject_bool(self) -> None:
        data = self.sample()
        data["nodes"][0]["cpu_threads"] = True
        data["guests"][0]["memory_allocated_mb"] = 0
        errors = validate_inventory(data)
        self.assertIn(
            "Node pve-node-01: cpu_threads must be a positive integer",
            errors,
        )
        self.assertIn(
            "Guest vm-data-01: memory_allocated_mb must be a positive integer",
            errors,
        )

    def test_duplicate_keys_are_rejected(self) -> None:
        data = self.sample()
        data["nodes"].append(deepcopy(data["nodes"][0]))
        data["guests"].append(deepcopy(data["guests"][0]))
        errors = validate_inventory(data)
        self.assertIn("Duplicate node_key: pve-node-01", errors)
        self.assertIn("Duplicate guest_key: vm-data-01", errors)

    def test_guest_must_reference_an_existing_node(self) -> None:
        data = self.sample()
        data["guests"][0]["node_key"] = "missing-node"
        self.assertIn(
            "Guest vm-data-01: unknown node_key 'missing-node'",
            validate_inventory(data),
        )

    def test_required_guest_text_fields_must_be_non_empty_strings(self) -> None:
        data = self.sample()
        data["guests"][0]["owner_role"] = 123
        self.assertIn(
            "Guest vm-data-01: missing or invalid owner_role",
            validate_inventory(data),
        )

    def test_mapping_collections_reject_non_object_entries(self) -> None:
        data = self.sample()
        data["nodes"] = ["not-an-object"]
        self.assertIn("'nodes[0]' must be an object.", validate_inventory(data))

    def test_load_json_rejects_invalid_json_and_non_object_top_level(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            invalid_path = Path(directory) / "invalid.json"
            invalid_path.write_text("{invalid", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Invalid JSON"):
                load_json(invalid_path)

            list_path = Path(directory) / "list.json"
            list_path.write_text(json.dumps([]), encoding="utf-8")
            with self.assertRaisesRegex(
                ValueError,
                "Top-level JSON value must be an object",
            ):
                load_json(list_path)


if __name__ == "__main__":
    unittest.main()
