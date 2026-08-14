#!/usr/bin/env python3
"""Identity and archival-mode contract for Kang Meta Skill."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class IdentityContractTest(unittest.TestCase):
    def test_manifest_uses_kang_defaults(self) -> None:
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))

        self.assertEqual(manifest["name"], "kang-meta-skill")
        self.assertEqual(manifest["owner"], "Kang")
        self.assertEqual(manifest["version"], "1.0.0")
        self.assertEqual(manifest["kang_defaults"]["skill_name_prefix"], "kang-")
        self.assertEqual(manifest["kang_defaults"]["github_owner"], "KanG-ciyuan")

    def test_entrypoint_and_interface_use_kang_invocation(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        interface = (ROOT / "agents" / "interface.yaml").read_text(encoding="utf-8")

        self.assertIn("name: kang-meta-skill", skill)
        self.assertIn("$kang-meta-skill", interface)
        self.assertIn("Kang Meta Skill", interface)

    def test_package_has_no_profile_asset_bundle(self) -> None:
        self.assertFalse((ROOT / "assets").exists())

    def test_archive_mode_does_not_claim_automatic_upstream_sync(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("does not update automatically", readme)
        self.assertIn("not installed locally", readme)

    def test_public_readme_explains_value_usage_outputs_and_evidence(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        required_sections = (
            "## 为什么需要它",
            "## 它会做什么",
            "## 它会交付什么",
            "## 你可以直接这样说",
            "## 验证记录",
            "## Troubleshooting",
        )
        for section in required_sections:
            with self.subTest(section=section):
                self.assertIn(section, readme)

        self.assertIn("npx skills add KanG-ciyuan/kang-meta-skill", readme)
        self.assertIn("35 / 35", readme)
        self.assertIn("23 / 23", readme)


if __name__ == "__main__":
    unittest.main()
