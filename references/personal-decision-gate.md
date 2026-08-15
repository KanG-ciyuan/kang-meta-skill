# Personal Decision Gate

Use this gate before creating a new Skill, splitting an existing Skill, or turning a repeated workflow into a package. Do not run the full inventory for ordinary use of an existing capability.

## Inventory Order

Inspect in this order and stop when verified coverage is sufficient:

1. built-in Meta Skill capabilities and referenced playbooks;
2. installed Skills and their trigger boundaries;
3. existing Kang repositories and recorded capabilities;
4. public capability research only when a genuine gap remains.

Preserve factual capability-research evidence when required, but do not inherit another person's profile, brand, or ownership defaults.

## Decisions

### Direct Reuse

Choose Direct Reuse when an existing capability covers the requested job, output, permission boundary, and lifecycle. Continue with that capability and explain the choice in one short sentence. Do not emit a full inventory report for ordinary execution.

### Extend Existing

Choose Extend Existing when the core job and trigger surface are shared but a mechanism is missing. Show the proposed extension and wait for approval before editing the owning Skill.

### Create New

Choose Create New only when at least one material independence reason exists:

- a distinct recurring user job or trigger;
- an independent output contract;
- an independent permission or safety boundary;
- a distinct tool dependency;
- a separate maintenance lifecycle;
- meaningful context-cost reduction that cannot be achieved with a reference or adapter.

The user may still choose Create New after reviewing the card. This gate blocks unproven duplication, not deliberate user choice.

## Partial Overlap

Partial overlap must pause before implementation. Do not interpret an initial request to create a Skill as approval to ignore an existing owner.

## Decision Card

For Extend Existing or Create New, show a concise Decision Card:

```text
Requested outcome:
Capabilities found:
Overlap:
Missing capability:
Recommended decision:
Routing and maintenance consequences:
Evidence gaps:
User choices:
```

The user may accept, revise, defer, or override the recommendation. Preserve that choice for the current task.

## README Boundary

- Agent Skill repository README work uses the built-in README playbook as part of the Meta Skill lifecycle.
- ordinary repository README work does not trigger this Meta Skill.
- one-off README work does not become a Skill automatically.
- when a general repository README Skill already exists, inventory it before proposing another package.

## Kang Ownership Boundary

Every created Kang package uses Kang authorship and ownership defaults. Do not inherit another person's profile, biography, social accounts, avatar, QR code, personal assets, or automatic brand injection. Preserve functionally required public references, dependencies, licenses, and research evidence, and comply with their terms.

## Missing Evidence

Incomplete inventory means uniqueness is `missing evidence`. Discussion may continue, but new-Skill implementation must pause until the user sees the gap and chooses how to proceed.

## Quick Reference

| Situation | Decision |
|---|---|
| Existing capability fully covers the job | Direct Reuse |
| Same job and trigger, missing mechanism | Extend Existing and pause |
| Materially independent recurring job | Create New and pause |
| One-off task | Do not create a Skill |
| Inventory unavailable | Missing evidence and pause |
