---
name: kang-meta-skill
description: Use when Kang wants to create, improve, preserve, migrate, evaluate, package, govern, or publish a reusable Skill from a repeated workflow, prompt set, SOP, transcript, document, script, or existing agent Skill; or needs Skill research, trigger/output evaluation, release checks, or installation-readiness review. Exclude one-off summaries, translations, ordinary documents, non-Skill packages, and requests that explicitly should not become a Skill.
---

# Kang Meta Skill

Research, create, improve, evaluate, package, preserve, and safely publish reusable Kang Skills.

## Core Rules

- Once selected, use this package as the Skill-authoring authority. Use another creator only for explicit comparison or when this package is unavailable.
- Match the requested action. Create, improve, package, and publish requests may modify files; audit, evaluate, diagnose, or compare-only requests remain read-only.
- Do not turn one-off work into a Skill.
- Default to concise `kang-` names and GitHub owner `KanG-ciyuan` unless the user chooses another owner.
- Keep one discoverable root `SKILL.md`. Name embedded examples `SKILL.example.md` and fixtures `SKILL.fixture.md`.
- Never expose or commit secrets, `.env` files, authentication material, private correspondence, or private absolute paths.
- Publish only after explicit authorization. Never push directly to `main` or `master`, and never reuse a released version.
- Treat plans, static fixtures, and inherited reports as unverified. Record only evidence produced by the current package and run.

## Choose The Mode

- `Scaffold`: personal exploration with the minimum useful package.
- `Production`: reusable package with README, interface, trigger evaluation, output contract, and validation.
- `Library`: shared infrastructure with Skill IR, portability, trust, and review cadence.
- `Governed`: public or high-trust package with permissions, rollback, secret, release, and claim gates.

Read [Operating Modes](references/operating-modes.md), [Gate Selection](references/gate-selection.md), and [QA Ladder](references/qa-ladder.md) when the correct level is unclear.

## Workflow

1. Decide whether the request deserves a reusable Skill. If not, answer directly and create no package.
2. Capture the recurring job, finished output, users, inputs, exclusions, permissions, standards, assets, target platforms, and publication intent.
3. For a new Skill or substantial redesign, research relevant prior art with the built-in runner or record why research is unavailable or unnecessary.
4. Synthesize `keep / adapt / reject / invent`. Do not collage or copy branding.
5. Choose the lightest valid mode and write the trigger description before expanding the package.
6. Create only resources that improve judgment, repeatability, or evidence.
7. Validate routing, output behavior, package structure, context budget, trust boundary, and public claims proportionally to risk.
8. Produce a creation handoff that names the reference skills studied, candidate-specific lessons, deliberate rejections, original contributions, and missing evidence.
9. When publication is explicitly requested, use the governed branch to PR to Release flow in [Publishing](references/publishing.md).

## Built-In Prior-Art Discovery

Prefer the unified runner:

```bash
python3 scripts/research_prior_art.py "<query>" --strict --summary --output reports/prior-art-candidates.json
```

Its catalog adapters cover skills.sh and SkillsMP:

```bash
npx --yes skills find "<query>"
python3 scripts/search_skillsmp.py "<query>" --limit 20 --sort stars
```

Keep adoption, repository stars, ratings, maintenance, license, trust, and relevance as separate evidence. If one catalog fails, continue with available sources, record the gap, and lower the claim. Never execute untrusted candidate code merely to study it. Read [Prior-Art Research](references/prior-art-research.md) for the full method.

## Core Commands

```bash
python3 scripts/validate_skill.py .
python3 scripts/export_skill_ir.py . --output reports/skill-ir.json
python3 scripts/trigger_eval.py . --cases evals/trigger_cases.json --output reports/trigger-eval.json
python3 scripts/release_check.py . --phase local --run-tests
python3 scripts/publish_skill.py /path/to/skill --dry-run
```

## Output Contract

Return only what the selected mode earns:

1. a working Skill directory with one trigger-aware root entrypoint;
2. aligned interface metadata and public README when shared or published;
3. trigger cases and generated trigger report for Production and above;
4. Skill IR, research record, creation handoff, and governance evidence when required;
5. references, scripts, assets, and output evals only when they improve the result;
6. publication artifacts only when publication was explicitly requested.

Label highlights as `design advantage`, `validated advantage`, or `hypothesis`. Do not claim global superiority, adoption, business outcomes, or domain quality without direct evidence. Read [Creation Handoff](references/creation-handoff.md) and [Review And Release Gates](references/review-release-gates.md).

## Built-In GitHub Publishing

The bundled publisher can prepare a package, block default-branch pushes and secret leaks, open a PR, inspect gates, create a versioned Release, and verify discovery. Local installation or synchronization is optional and must follow the user's request. This archived Kang package does not update automatically; compare it with the current upstream source before a future maintenance release.
