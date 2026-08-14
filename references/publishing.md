# Self-Contained Skill Publishing

Use the bundled publisher only after the user explicitly requests GitHub publication.

## Capability Contract

`scripts/publish_skill.py` provides:

1. `SKILL.md` and `manifest.json` identity/version checks;
2. MIT `LICENSE` creation when missing;
3. README generation or quality validation;
4. an optional minimal Kang author section without invented biography or media assets;
5. GitHub owner and repository detection;
6. repository creation with a baseline default branch when needed;
7. feature-branch commit and push while blocking direct default-branch publication;
8. pull-request creation, review/check inspection, and optional merge;
9. immutable version guards for existing Releases;
10. GitHub Release and discovery verification;
11. optional isolated install verification and optional local synchronization, both controlled by explicit flags and user intent.

## Commands

Read-only audit:

```bash
python3 scripts/publish_skill.py /path/to/skill --dry-run
```

Prepare local public files without GitHub writes:

```bash
python3 scripts/publish_skill.py /path/to/skill --prepare-only
```

Publish without downloading or installing the Skill locally:

```bash
python3 scripts/publish_skill.py /path/to/skill --no-sync-local --skip-install-check
```

Stop after a passing PR:

```bash
python3 scripts/publish_skill.py /path/to/skill --no-merge --no-sync-local --skip-install-check
```

Useful target controls:

- `--github-user OWNER`
- `--repo-name REPO`
- `--branch codex/...`
- `--private`
- `--skip-author-section`
- `--no-sync-local`
- `--skip-install-check`

## Safety Decisions

- Full publication is an external mutation and requires explicit authorization.
- `--dry-run` is read-only and does not create or modify local files.
- New repositories receive an initial baseline before the Skill enters through a feature branch and PR.
- Existing repositories never receive a direct push to `main`, `master`, or another default branch.
- Staged content passes secret scanning and `git diff --cached --check` before commit.
- Failed or pending checks, conflicts, or requested changes block merging.
- Existing Releases are immutable; changed content requires a new semantic version.
- Discovery can be verified with `npx skills add --list` without installing the Skill.
- Local synchronization is skipped when `--no-sync-local` is supplied.
- Isolated install verification is skipped when `--skip-install-check` is supplied.

## Evidence Boundary

The publisher can prove package gates, Git/PR/Release state, discovery, and any installation check actually run. It cannot prove domain output quality, user satisfaction, adoption, or business outcomes. Keep those as separate runtime, provider, or human evidence and mark absent proof as `missing evidence`.
