#!/usr/bin/env python3
"""Capability parity contract for Kang Meta Skill."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CapabilityParityTest(unittest.TestCase):
    def test_required_general_capabilities_have_dispositions(self) -> None:
        payload = json.loads((ROOT / "references" / "capability-parity.json").read_text(encoding="utf-8"))
        expected = {
            "routing_authority",
            "prior_art_discovery",
            "generalization_gate",
            "operating_modes",
            "skill_ir",
            "trigger_eval",
            "output_eval",
            "resource_boundaries",
            "creation_handoff",
            "skill_readme",
            "permission_gates",
            "release_gates",
            "github_publication",
            "release_discovery",
            "isolated_install_verification",
            "failure_degradation",
        }
        entries = {item["id"]: item for item in payload["capabilities"]}
        self.assertEqual(set(entries), expected)
        for item in entries.values():
            self.assertIn(item["disposition"], {"preserve", "identity_adapt", "remove_identity_only"})
            self.assertTrue(item["kang_location"])
            self.assertTrue(item["verification"])

    def test_no_general_capability_is_removed(self) -> None:
        payload = json.loads((ROOT / "references" / "capability-parity.json").read_text(encoding="utf-8"))
        self.assertNotIn("remove", {item["disposition"] for item in payload["capabilities"]})

    def test_root_exposes_complete_general_workflow(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for heading in (
            "## Router Rules",
            "## Modes",
            "## Built-In Prior-Art Discovery",
            "## Generalization Gate",
            "## Kang Skill OS",
            "## Compact Workflow",
            "## Gate Ladder",
            "## Output Contract",
            "## Publish Flow",
            "## Kang Defaults",
            "## Reference Map",
        ):
            self.assertIn(heading, text)


if __name__ == "__main__":
    unittest.main()
