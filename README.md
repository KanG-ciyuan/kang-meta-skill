# Kang Meta Skill

> A personal, governed backup for researching, creating, improving, evaluating, preserving, and publishing reusable agent Skills.

[![License](https://img.shields.io/badge/license-MIT-2f855a.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-2563eb.svg)](manifest.json)

## Why This Repository Exists

`kang-meta-skill` preserves a reviewed Skill-authoring workflow under Kang's ownership so it remains available if the currently used source changes or disappears. It is an independent backup, not an automatic mirror.

This repository does not update automatically. New upstream capabilities must be compared, adapted, tested, and released manually. The repository version is not installed locally; Kang can continue using the actively maintained source Skill for day-to-day research and creation.

## What It Does

- decides whether a repeated workflow should become a Skill;
- researches relevant Skills and source repositories with graceful fallback;
- creates, improves, migrates, or audits Skill packages;
- evaluates trigger boundaries, output evidence, package structure, and trust;
- exports a compact Skill IR;
- validates release readiness and public claims;
- publishes through a feature branch, pull request, immutable Release, and discovery checks;
- keeps installation and local synchronization optional.

## 你可以直接这样说

- “把这套重复流程整理成我的 Kang Skill。”
- “先研究类似 Skill，再取长补短创建一个新的能力包。”
- “只审计这个 Skill，先不要修改文件。”
- “发布到 GitHub，但不要安装或同步到本机。”

## Future Installation

The current release is intentionally not installed locally. If it is needed later, review the repository first and then use:

```bash
npx skills add KanG-ciyuan/kang-meta-skill --skill kang-meta-skill
```

Verify the package after installation:

```bash
test -f ~/.agents/skills/kang-meta-skill/SKILL.md
python3 ~/.agents/skills/kang-meta-skill/scripts/validate_skill.py ~/.agents/skills/kang-meta-skill
```

## Local Validation

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_skill.py .
python3 scripts/trigger_eval.py . --cases evals/trigger_cases.json
python3 scripts/release_check.py . --phase local --run-tests
```

## Safety Boundary

- Never expose or commit API keys, tokens, cookies, `.env` files, authentication files, private correspondence, or private paths.
- Audit-only requests must not edit files.
- Publishing requires explicit authorization and cannot push directly to the default branch.
- A released version is immutable; changes require a version bump.
- Local installation and synchronization require a separate explicit request.
- External Skill code is inspected before use and is never executed merely for research.

## Update Model

This is a manually maintained fallback. Before updating it:

1. compare the current source behavior and this repository;
2. identify useful changes without importing personal branding or historical claims;
3. add failing tests for the intended behavior;
4. adapt the smallest necessary change;
5. rerun validation and release through a pull request.

## Prerequisites

- [ ] Python 3 for validation and evaluation scripts
- [ ] Node.js and `npx` for catalog discovery
- [ ] Git and GitHub CLI for publication
- [ ] Explicit user authorization before any GitHub write or local installation

## Troubleshooting

| Problem | Likely cause | Resolution |
|---|---|---|
| `No valid skills found` | Invalid YAML frontmatter or wrong repository path | Run `scripts/validate_skill.py` and inspect the root `SKILL.md` |
| Trigger cases fail | Description and examples are misaligned | Update the trigger description or cases, then rerun `trigger_eval.py` |
| Release gate blocks | Missing evidence, dirty branch, reused version, or secret risk | Read the named gate and fix the underlying evidence |
| Features differ from the active source | This backup does not auto-sync | Perform a reviewed manual comparison and publish a new version |

## License

MIT License. Copyright (c) 2026 Kang.

<!-- kang-author:start -->
## About Kang

Maintained by Kang. GitHub: https://github.com/KanG-ciyuan/
<!-- kang-author:end -->
