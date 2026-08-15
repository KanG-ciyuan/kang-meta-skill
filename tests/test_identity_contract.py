#!/usr/bin/env python3
"""Identity, lifecycle, and public-package contract for Kang Meta Skill."""

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
        self.assertEqual(manifest["version"], "2.0.0")
        self.assertEqual(manifest["status"], "active")
        self.assertEqual(manifest["maintenance"]["mode"], "manual-reviewed")
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

    def test_public_text_contains_only_kang_identity(self) -> None:
        forbidden_fragments = (
            "qiao" + "mu",
            "joesee" + "sun",
            "vista" + "8",
            "yaojin" + "gang",
        )
        scanned_suffixes = {".md", ".json", ".yaml", ".yml", ".py"}
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts or path.suffix not in scanned_suffixes:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore").lower()
            for token in forbidden_fragments:
                self.assertNotIn(token, text, f"prohibited identity in {path.relative_to(ROOT)}")

    def test_public_package_has_no_external_provenance_contract(self) -> None:
        forbidden_contracts = (
            "upstream_" + "inspiration",
            "declared upstream" + " credit",
            "upstream" + "_sync",
            "upstream" + "_drift",
            "upstream" + " credit",
        )
        scanned_suffixes = {".md", ".json", ".yaml", ".yml", ".py"}
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts or path.suffix not in scanned_suffixes:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore").lower()
            for token in forbidden_contracts:
                self.assertNotIn(token, text, f"external provenance contract in {path.relative_to(ROOT)}")

    def test_readme_positions_v2_as_active_kang_skill(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("`v2.0.0`", readme)
        self.assertIn("复用优先", readme)
        self.assertNotIn("独立备份", readme)
        self.assertNotIn("not installed locally", readme)
        self.assertNotIn("archived-backup", readme)

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
        self.assertIn("47 / 47", readme)
        self.assertIn("23 / 23", readme)


if __name__ == "__main__":
    unittest.main()
