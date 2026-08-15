---
name: kang-meta-skill
description: Use when Kang wants to create, improve, preserve, migrate, evaluate, package, govern, or publish a reusable Skill from a repeated workflow, prompt set, SOP, transcript, document, script, or existing agent Skill; or needs Skill research, trigger/output evaluation, release checks, or installation-readiness review. Exclude one-off summaries, translations, ordinary documents, non-Skill packages, and requests that explicitly should not become a Skill.
metadata:
  author: Kang
  version: "2.0.0"
---

# Kang Meta Skill

Build reusable Kang Skill packages, not long prompts.

## Router Rules

- Route by frontmatter `description` first.
- Once selected, `kang-meta-skill` is the single Skill-authoring authority. Do not invoke another creator unless the user explicitly requests comparison or this Skill is unavailable.
- Built-in public capability research belongs to this Skill. Do not install or delegate to a separate discovery Skill.
- Built-in GitHub publishing belongs to this Skill. Do not require a separate publisher after this package is selected.
- Before proposing a new Skill or substantial split, pass the [Reuse-First Gate](references/personal-decision-gate.md).
- Keep root `SKILL.md` focused on routing and mandatory workflow. Put judgment in `references/`, deterministic behavior in `scripts/`, regression cases in `evals/`, and evidence in `reports/`.
- A package has one discoverable root `SKILL.md`; embedded examples use `SKILL.example.md` or `SKILL.fixture.md`.
- Do not turn one-off summaries, translations, explanations, ordinary documents, or brainstorming into Skills.
- Match the requested action: create or improve requests may edit; audit, evaluate, diagnose, and compare-only requests remain read-only.
- Public Kang packages must not inherit another person's authorship, profile, social accounts, avatar, QR code, personal assets, brand injection, or ownership defaults. Preserve factual research, license, dependency, and candidate evidence when it is functionally required.

## Modes

- `Scaffold`: personal exploration with the minimum useful package.
- `Production`: reusable package with README, interface, trigger evaluation, output contract, and installation evidence.
- `Library`: shared infrastructure with Skill IR, portability, trust, and review cadence.
- `Governed`: public or high-trust package with permission, rollback, secret, release, and claim gates.

Choose proportionally with [Operating Modes](references/operating-modes.md), [Gate Selection](references/gate-selection.md), and [QA Ladder](references/qa-ladder.md).

## Built-In Prior-Art Discovery

Before a new Skill or substantial redesign:

1. Pass the Reuse-First Gate before searching outside the current capability inventory.
2. Derive 2-4 intent-shaped queries covering outcome, domain action, quality mechanism, and an adjacent synonym when useful.
3. Prefer the unified runner:

```bash
python3 scripts/research_prior_art.py "<query 1>" "<query 2>" --strict --summary --output reports/prior-art-candidates.json
```

Its catalog calls remain:

```bash
npx --yes skills find "<query>"
python3 scripts/search_skillsmp.py "<query>" --limit 20 --sort stars
```

The adapters query the skills.sh catalog and SkillsMP separately; never combine their metrics.

4. Keep adoption, repository metrics, ratings, maintenance, license, trust, and relevance separate.
5. Inspect source behavior, maintenance, license, permissions, and security without executing untrusted code.
6. Synthesize `keep / adapt / reject / invent`; learn mechanisms semantically and do not copy personal branding or unlicensed material.
7. Preserve dated candidates, links, metrics, licenses, lessons, rejections, and missing evidence when they are part of the research record. Do not present a candidate's creator as the owner or endorser of the Kang package.

If a catalog fails, continue with available sources, record `missing evidence`, and lower the claim. Full method: [Prior-Art Research](references/prior-art-research.md).

## Generalization Gate

Before promoting one failure into a core rule:

1. restate it as domain-neutral behavior;
2. classify it as core mechanism, optional adapter, or eval-only fixture;
3. promote only safety, factual, permission, or repeated cross-domain behavior;
4. keep one-off details in fixtures or specialist references;
5. rerun the original and unrelated boundary cases.

Prefer intent fidelity, decision rules, and general mechanisms over an expanding topic encyclopedia.

## Kang Skill OS

1. `Intent`: recurring job, users, inputs, output, exclusions, standards, and permissions.
2. `Inventory`: built-in capabilities, installed Skills, Kang repositories, then public research when still necessary.
3. `Decision`: Direct Reuse, Extend Existing, or Create New.
4. `Skill IR`: platform-neutral meaning and evidence boundary.
5. `Package`: lean root instructions, interface, README, and earned resources.
6. `Eval`: trigger boundaries first; output, runtime, and human evaluation when risk justifies it.
7. `Review`: package, context, trust, install, ownership, README, and public claims.
8. `Operate`: explicit feedback, failures, drift, and next-iteration proposals without raw private content.

## Compact Workflow

1. Decide whether the request deserves a reusable Skill; otherwise answer directly and create no package.
2. Capture job, output, users, inputs, exclusions, permissions, standards, assets, platforms, and publication intent.
3. Pass the Reuse-First Gate and stop for user choice on partial overlap.
4. Research public capabilities only when inventory still has a genuine gap; keep source notes temporary.
5. Pass the Generalization Gate for sample-driven core changes.
6. Choose the lightest valid mode.
7. Write the trigger description early and run trigger cases before expanding structure.
8. Create only earned resources; do not duplicate README and `SKILL.md` prose.
9. Export Skill IR for Production+, public, or cross-platform packages.
10. Add output evaluations when correctness, safety, persuasion, or repeatability cannot be shown by trigger tests alone.
11. Keep mutations within the requested action boundary and preserve rollback for risky changes.
12. Validate package, tests, trigger behavior, context budget, ownership, secret boundaries, and evidence claims.
13. Produce a creation handoff naming reference Skills studied, candidate-specific lessons, deliberate rejections, original contributions, and missing evidence, without inheriting personal branding or authorship.
14. Publish only after explicit authorization through feature branch, validation, Pull Request, Release, discovery, and isolated-install gates.

Core commands:

```bash
python3 scripts/validate_skill.py .
python3 scripts/export_skill_ir.py . --output reports/skill-ir.json
python3 scripts/trigger_eval.py . --cases evals/trigger_cases.json --output reports/trigger-eval.json
python3 scripts/release_check.py . --phase local --run-tests
python3 scripts/publish_skill.py /path/to/skill --dry-run
```

## Gate Ladder

- `Scaffold`: valid frontmatter, useful README hook, natural triggers, and explicit exclusions.
- `Production`: Scaffold plus interface, trigger evaluation, output contract, troubleshooting, root isolation, and install verification.
- `Library`: Production plus Skill IR, portability, trust, review cadence, and evidence artifacts.
- `Governed`: Library plus permission and rollback boundaries, secret and ownership scans, output or human evidence, and public-claim guards.

Unavailable telemetry, provider runs, approval, install proof, or human review remain `missing evidence`; planned work is not proof. See [Review And Release Gates](references/review-release-gates.md) and [Resource Boundary Spec](references/resource-boundaries.md).

## Output Contract

For package-producing requests, provide only what the selected mode earns:

1. a working Skill directory with one trigger-aware root `SKILL.md`;
2. aligned `agents/interface.yaml`;
3. a reader-facing README for shared or public Skills;
4. trigger cases and generated trigger report for Production+;
5. Skill IR, prior-art research report, and creation handoff for Production+;
6. references, scripts, output evals, and reports only when they improve judgment or evidence;
7. publication artifacts only when publication was requested.

The handoff must name reference Skills studied, give candidate-specific lessons, explain deliberate rejections and original contributions, and label highlights as `design advantage`, `validated advantage`, or `hypothesis`. Preserve factual references without inheriting another person's authorship or private profile information. Never claim global superiority without fair evidence. Use [Creation Handoff](references/creation-handoff.md).

## Publish Flow

1. Treat README as a product page: value, install, natural examples, prerequisites, outputs, configuration, risks, and troubleshooting.
2. Audit read-only when useful: `python3 scripts/publish_skill.py /path/to/skill --dry-run`.
3. Publish only after explicit authorization.
4. The publisher prepares Kang-owned LICENSE, README, and author content; resolves repository identity; blocks secrets, external provenance, and reused versions; and publishes only through a feature branch and Pull Request.
5. Merge is blocked by conflicts, failed or pending checks, or requested changes. Successful publication creates `vX.Y.Z`, verifies discovery, and performs an isolated install check.
6. Do not report publication complete until the remote default version, Release, discovery, and isolated installation are verified.

Detailed decisions: [Publishing](references/publishing.md). README method: [GitHub README Playbook](references/github-readme-playbook.md). Operation method: [SkillOps Loop](references/skillops-loop.md).

## Kang Defaults

- Prefer practical, concise, Chinese-first output.
- Default to `kang-` names with no more than three preferred hyphen parts.
- Use `Copyright (c) Kang` and GitHub `https://github.com/KanG-ciyuan/` unless Kang selects another owner.
- Keep one creator authority and one root Skill entrypoint.
- Preserve platform-neutral source with minimal adapters.
- Public packages use Kang authorship, ownership, and branding while preserving functionally required licenses, dependencies, and research evidence.
- Public research may identify factual candidates and repositories, but must not inject another person's profile or imply endorsement.

## Reference Map

- Design: [Skill Engineering Method](references/skill-engineering-method.md), [Skill Archetypes](references/skill-archetypes.md), [Intent Dialogue](references/intent-dialogue.md), [Non-Skill Decision Tree](references/non-skill-decision-tree.md)
- Personal decisions: [Reuse-First Gate](references/personal-decision-gate.md), [Capability Parity](references/capability-parity.json)
- Evidence: [Eval Playbook](references/eval-playbook.md), [Output Eval](references/output-eval-method.md), [Skill IR](references/skill-ir-method.md), [Governance](references/governance.md)
- Release: [Publishing](references/publishing.md), [Review And Release Gates](references/review-release-gates.md), [GitHub README](references/github-readme-playbook.md), [SkillOps](references/skillops-loop.md)
