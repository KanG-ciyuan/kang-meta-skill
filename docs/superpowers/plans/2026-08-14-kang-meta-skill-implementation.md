# Kang Meta Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build, verify, and publish a standalone `kang-meta-skill` backup repository without installing it into the active local Skill directories.

**Architecture:** Adapt the neutral research, validation, evaluation, and governed publishing mechanisms from the authorized local source into a Kang-owned package. Replace identity-dependent contracts through tests first, omit original profile assets and historical evidence, and publish from a feature branch through PR and Release while explicitly disabling local synchronization.

**Tech Stack:** Markdown, JSON, YAML, Python standard library, `unittest`, Git, GitHub CLI, `npx skills` discovery verification.

---

### Task 1: Establish Repository Baseline

**Files:**
- Existing: `docs/superpowers/specs/2026-08-14-kang-meta-skill-design.md`
- Existing: `docs/superpowers/plans/2026-08-14-kang-meta-skill-implementation.md`
- Create: `.gitignore`

- [ ] **Step 1: Confirm the target is not already an installed Skill**

Run read-only checks for `~/.codex/skills/kang-meta-skill` and `~/.agents/skills/kang-meta-skill`.

- [ ] **Step 2: Initialize the repository on `main`**

Run `git init -b main`, add only the specification, plan, and `.gitignore`, then commit `docs: define Kang Meta Skill`.

- [ ] **Step 3: Create the implementation branch**

Run `git switch -c codex/create-kang-meta-skill` and verify the current branch is not `main` or `master`.

### Task 2: Create Identity And Safety Tests First

**Files:**
- Create: `tests/test_identity_contract.py`
- Create: `tests/test_validate_skill.py`
- Create: `tests/test_publish_skill.py`
- Create: `tests/test_release_check.py`
- Create: `tests/test_research_prior_art.py`
- Create: `tests/test_skillsmp_search.py`
- Create: `tests/test_creation_handoff.py`
- Create: `tests/test_builtin_discovery.py`

- [ ] **Step 1: Write failing Kang identity tests**

Require package name `kang-meta-skill`, owner `Kang`, prefix `kang-`, GitHub owner `KanG-ciyuan`, Kang interface prompts, and absence of the source author's personal branding and profile assets.

- [ ] **Step 2: Write failing retained-behavior tests**

Adapt the source package's tests for recursive entrypoint detection, version consistency, catalog normalization, resilient prior-art research, dry-run immutability, default-branch blocking, PR gate behavior, MIT preparation, and no local sync by default.

- [ ] **Step 3: Verify RED**

Run `python3 -m unittest discover -s tests -v`. Expected result: failures or import errors because the Kang scripts and package files do not exist yet.

- [ ] **Step 4: Commit tests**

Commit only the failing tests as `test: define Kang meta skill contract`.

### Task 3: Adapt Core Package And References

**Files:**
- Create: `SKILL.md`
- Create: `README.md`
- Create: `LICENSE`
- Create: `manifest.json`
- Create: `agents/interface.yaml`
- Create: `evals/trigger_cases.json`
- Create: `references/*.md`

- [ ] **Step 1: Create the concise entrypoint and interface**

Use `kang-meta-skill` and `$kang-meta-skill`; preserve create, improve, audit, evaluate, package, install-check, and publish triggers; state that this archived Kang copy does not auto-sync with its source.

- [ ] **Step 2: Create Kang metadata and trigger cases**

Set version `1.0.0`, owner `Kang`, prefix `kang-`, GitHub `https://github.com/KanG-ciyuan/`, and realistic Chinese/English positive, negative, and near-neighbor cases.

- [ ] **Step 3: Adapt neutral references**

Retain reusable methods while replacing source-specific identity and publisher language. Keep necessary third-party repositories only as factual prior-art references. Remove profile/QR workflows and historical evidence claims.

- [ ] **Step 4: Write public README and MIT license**

Explain capabilities, use cases, limitations, install instructions for future use, non-install status, validation commands, security boundary, update model, and attribution-free Kang ownership under the user's stated authorization.

### Task 4: Adapt Scripts Until Tests Pass

**Files:**
- Create: `scripts/validate_skill.py`
- Create: `scripts/trigger_eval.py`
- Create: `scripts/export_skill_ir.py`
- Create: `scripts/search_skillsmp.py`
- Create: `scripts/research_prior_art.py`
- Create: `scripts/release_check.py`
- Create: `scripts/publish_skill.py`

- [ ] **Step 1: Adapt validation and trigger evaluation**

Replace package-specific identifiers and require Kang concepts only for `kang-meta-skill`. Add forbidden-identity scanning without treating necessary neutral source labels inside private design docs as public package failures.

- [ ] **Step 2: Adapt research and IR export**

Preserve catalog fallback and deduplication, rename schema/default fields to neutral or Kang terms, and avoid generating inherited evidence.

- [ ] **Step 3: Adapt release and publisher behavior**

Default to `Kang` and `KanG-ciyuan`; generate a minimal Kang author section with no invented biography or assets; keep direct default-branch pushes blocked; make `--no-sync-local` the enforced publication choice for this release.

- [ ] **Step 4: Verify GREEN**

Run `python3 -m unittest discover -s tests -v` until all tests pass with no warnings or errors.

- [ ] **Step 5: Commit implementation**

Commit package, references, scripts, and tests as `feat: create Kang Meta Skill`.

### Task 5: Generate Honest Evidence And Run Release Gates

**Files:**
- Create: `reports/trigger-eval.json`
- Create: `reports/skill-ir.json`
- Create: `reports/verification-2026-08-14.md`

- [ ] **Step 1: Generate trigger and IR reports**

Run `python3 scripts/trigger_eval.py . --cases evals/trigger_cases.json --output reports/trigger-eval.json` and `python3 scripts/export_skill_ir.py . --output reports/skill-ir.json` using each script's actual supported arguments.

- [ ] **Step 2: Run package and release validation**

Run `python3 scripts/validate_skill.py .`, the complete unit suite, and `python3 scripts/release_check.py . --phase local --run-tests`.

- [ ] **Step 3: Run identity and secret scans**

Scan public runtime and repository files for forbidden personal branding, credential-shaped content, `.env` files, private absolute paths, and unexpected binary assets. Do not print any secret value.

- [ ] **Step 4: Record evidence honestly**

Write only commands, pass/fail totals, known warnings, and the explicit statement that domain output quality and future upstream synchronization are not yet validated.

- [ ] **Step 5: Commit evidence**

Commit generated reports as `test: record Kang meta skill verification`.

### Task 6: Publish Without Local Installation

**Files:**
- Modify only if required by final checks: package files and reports

- [ ] **Step 1: Verify GitHub prerequisites and scope**

Run `gh --version`, `gh auth status`, `git status -sb`, `git diff main...HEAD --stat`, and confirm the authenticated GitHub owner is `KanG-ciyuan` without displaying credentials.

- [ ] **Step 2: Create the public repository baseline**

Create `KanG-ciyuan/kang-meta-skill` as public if it does not exist, establish `main` only with the baseline documentation, and set `origin`.

- [ ] **Step 3: Push the feature branch and open a PR**

Push `codex/create-kang-meta-skill`, open a PR describing the backup purpose, identity adaptation, verification, and explicit non-install boundary, then inspect checks and mergeability.

- [ ] **Step 4: Merge and create `v1.0.0` Release**

Merge only after gates pass, create the immutable GitHub Release, and verify the default branch contains `manifest.json` version `1.0.0`.

- [ ] **Step 5: Verify discovery without installation**

Use list/discovery commands only. Do not run an install command and do not sync to `~/.codex/skills` or `~/.agents/skills`.

- [ ] **Step 6: Reconfirm non-install status**

Verify both local Skill installation paths remain absent, then report repository, PR, release, commit, test results, and the manual future-update boundary.
