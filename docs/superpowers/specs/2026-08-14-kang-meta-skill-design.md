# Kang Meta Skill Design

## 1. Goal

Create `kang-meta-skill`, a personal meta Skill for Kang that can research prior art, decide whether material should become a Skill, create or improve a Skill, evaluate it, package it, check installation, and publish it through a governed GitHub release flow.

The result must preserve the useful engineering capabilities of the current local `qiaomu-meta-skill` while presenting only Kang's identity, defaults, evidence, and release history. This is a functional adaptation, not a superficial rename.

## 2. Identity And Defaults

- Skill name: `kang-meta-skill`
- Display name: `Kang Meta Skill`
- Public author and maintainer: `Kang`
- Default generated Skill prefix: `kang-`
- Default GitHub owner: `KanG-ciyuan`
- Intended repository: `KanG-ciyuan/kang-meta-skill`
- Initial release version: `1.0.0`
- Primary invocation: `$kang-meta-skill`
- Primary language: concise Chinese-first instructions, with English where package formats or ecosystem discovery require it

No public file may contain another individual's profile, avatar, QR code, social account, personal website, repository default, author biography, or personal release history. Third-party project names and repository links may appear only when they are necessary, factual prior-art references rather than personal branding.

The user states that the source copyright holder authorized removal of attribution. Keep that authorization private; do not publish private messages or supporting personal correspondence.

## 3. Supported Jobs

The Skill supports these operating modes:

1. Decide whether a workflow, prompt, transcript, SOP, document, script, or repeated task should become a Skill.
2. Research relevant existing Skills and source repositories before authoring when external research adds value.
3. Create a new Kang Skill from confirmed requirements and reusable material.
4. Improve, migrate, audit, or repair an existing Skill without changing unrelated behavior.
5. Evaluate routing, trigger boundaries, output quality, package structure, safety, and installability.
6. Export a compact Skill IR for comparison and governance.
7. Prepare README, manifest, license, release evidence, and installation instructions.
8. Publish only after explicit user authorization, through feature branch, pull request, versioned release, discovery verification, and isolated clean installation.

The Skill must respect audit-only requests: report findings without editing files. It must not convert one-off summaries, translations, ordinary documents, or explicitly non-reusable tasks into Skills.

## 4. Retained Functional Capabilities

Adapt and retain the source package's useful mechanisms:

- dual-catalog prior-art research with GitHub source verification and graceful degradation when a catalog is unavailable;
- keep/adapt/reject/invent synthesis before authoring;
- proportional validation gates rather than forcing the same process on every Skill;
- trigger evaluation with positive, negative, and adversarial cases;
- output-evaluation guidance and honest evidence boundaries;
- Skill IR export;
- package validation, release readiness checks, and version checks;
- governed publication that forbids direct pushes to the default branch;
- pull-request, release, discovery, and clean-install verification;
- security checks that prevent credentials, `.env` files, private paths, or personal data from entering public packages.

Do not inherit the source package's historical validation totals, reports, catalog claims, endorsements, or release evidence. Generate Kang-specific reports only from tests actually run against `kang-meta-skill`.

## 5. Package Structure

```text
kang-meta-skill/
├── SKILL.md
├── README.md
├── LICENSE
├── manifest.json
├── agents/
│   └── interface.yaml
├── references/
├── scripts/
├── tests/
├── evals/
├── reports/
└── docs/superpowers/
    ├── specs/
    └── plans/
```

`SKILL.md` remains the concise entry point. Detailed methods belong in directly linked reference files. Scripts contain repeatable deterministic operations. Tests and evals prove behavior. Reports contain only current Kang evidence. Project documentation is retained for repository governance but is not installed as runtime guidance unless required.

## 6. Required Adaptations

### Entrypoint And Interface

- Rewrite frontmatter and body for `kang-meta-skill` triggers and Kang defaults.
- Replace all `$qiaomu-meta-skill` invocations with `$kang-meta-skill`.
- Update interface metadata, starter prompts, routing examples, and release criteria.
- Keep the meta Skill as the single authoring authority once selected, while allowing explicit comparison with other creator Skills.

### Manifest And License

- Set package identity, owner, repository, prefix, and version to the confirmed Kang values.
- Use an MIT license identifying Kang, based on the user's stated authorization.
- Remove original personal-profile injection and original social defaults.

### Publishing

- Change publisher defaults to `Kang` and `KanG-ciyuan`.
- Replace profile injection with a minimal optional Kang author section that contains no invented biography, social account, avatar, or QR code.
- Keep publication opt-in and preserve the feature branch to PR to Release to discovery to clean-install sequence.
- Rename source-specific flags, constants, temporary prefixes, module identifiers, and messages where they form part of the public or maintained contract.

### Validation And Evaluation

- Change validators and trigger concepts from Qiaomu identity to Kang identity.
- Rebuild trigger cases with `$kang-meta-skill`, `Kang`, `kang-`, and realistic Chinese/English requests.
- Add negative cases for ordinary documentation, unrelated GitHub publishing, and requests that explicitly reject Skill creation.
- Preserve tests for source research, package validation, release readiness, publishing safety, discovery, and handoff generation.
- Add a repository-wide identity scan that fails if forbidden original personal branding or profile assets are present.

### Reports And Assets

- Do not copy `assets/qiaomu-profile/`.
- Do not copy source iteration reports, personal catalog reports, generated Skill IR, or source trigger report as Kang evidence.
- Create only fresh baseline and verification reports generated during this implementation.

## 7. Security And Trust Boundary

- Never display or commit complete API keys, tokens, cookies, credentials, `.env` files, authentication files, or private correspondence.
- When checking credentials, report only variable names, locations, and risks.
- Do not move, replace, delete, or revoke credentials without explicit user permission.
- Review the source, permissions, install behavior, and network behavior of any new third-party plugin or script before installation and obtain user confirmation.
- External research may read public sources; publication and other external writes require explicit authorization.
- Reject direct default-branch pushes even if requested under time pressure; prepare a reviewable branch and pull request instead.

## 8. Verification Strategy

Use test-first adaptation for maintained behavior:

1. Establish baseline scenarios that expose failures without the Kang Skill, including wrong prefix, inherited identity, unsafe direct publication, and false evidence reuse.
2. Write or adapt tests so they fail against the not-yet-created Kang package for the intended reason.
3. Implement the minimum changes needed to pass each behavior.
4. Run unit tests, trigger evaluation, package validation, release dry-run, identity scan, and secret scan.
5. Forward-test realistic create, improve, audit-only, and publish-dry-run requests with minimal leaked context.
6. Record only the evidence produced by those runs.

Publication is outside the implementation completion boundary. Local creation and validation happen first. Installation into `~/.codex/skills` and GitHub publication require separate user approval after review.

## 9. Acceptance Criteria

- `$kang-meta-skill` clearly triggers on creating, improving, evaluating, packaging, preserving, or publishing reusable Skills.
- Generated Skill names default to `kang-` and repository defaults point to `KanG-ciyuan`.
- No original personal profile, social account, personal website, QR code, avatar, repository default, or historical claims remain.
- Necessary third-party prior-art citations are factual, limited, and not presented as authorship or endorsement.
- All retained scripts work with Kang naming and pass their adapted tests.
- Direct default-branch publication remains blocked.
- Audit-only mode produces no file changes.
- Reports distinguish verified evidence, historical context, and items still requiring verification.
- Local validation and forward tests pass before installation or publication is proposed.

## 10. Out Of Scope

- Publishing the repository during initial implementation.
- Installing the Skill into the active Codex Skill directory without approval.
- Creating Kang avatars, QR codes, social profiles, or an invented biography.
- Claiming source-project test counts or release history as Kang's achievements.
- Rewriting every retained method when a neutral, working implementation can be safely adapted and tested.
