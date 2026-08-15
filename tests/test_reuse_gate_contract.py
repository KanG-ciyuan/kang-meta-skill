#!/usr/bin/env python3
from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReuseGateContractTest(unittest.TestCase):
    def test_personal_decision_reference_exists(self) -> None:
        self.assertTrue((ROOT / "references" / "personal-decision-gate.md").is_file())

    def test_root_requires_inventory_before_new_skill(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for phrase in (
            "Reuse-First Gate",
            "Direct Reuse",
            "Extend Existing",
            "Create New",
            "missing evidence",
        ):
            self.assertIn(phrase, text)

    def test_fixture_covers_regression_families(self) -> None:
        payload = json.loads((ROOT / "evals" / "reuse_gate_cases.json").read_text(encoding="utf-8"))
        ids = {case["id"] for case in payload["cases"]}
        self.assertEqual(
            ids,
            {
                "reuse_builtin_skill_readme",
                "one_off_frontend_readme",
                "partial_overlap_requires_confirmation",
                "distinct_skill_allowed",
                "incomplete_inventory_blocks_creation",
                "ordinary_invocation_stays_concise",
            },
        )

    def test_decision_card_and_readme_boundary_are_explicit(self) -> None:
        text = (ROOT / "references" / "personal-decision-gate.md").read_text(encoding="utf-8")
        for phrase in (
            "built-in Meta Skill capabilities",
            "installed Skills",
            "existing Kang repositories",
            "public capability research",
            "Decision Card",
            "Agent Skill repository README",
            "ordinary repository README",
        ):
            self.assertIn(phrase, text)

    def test_partial_overlap_requires_user_choice(self) -> None:
        text = (ROOT / "references" / "personal-decision-gate.md").read_text(encoding="utf-8")
        self.assertIn("Partial overlap must pause", text)
        self.assertIn("The user may still choose Create New", text)

    def test_public_package_ownership_is_part_of_creation_decision(self) -> None:
        text = (ROOT / "references" / "personal-decision-gate.md").read_text(encoding="utf-8")
        self.assertIn("Kang authorship", text)
        self.assertIn("Preserve functionally required public references", text)
        self.assertIn("QR code", text)


if __name__ == "__main__":
    unittest.main()
