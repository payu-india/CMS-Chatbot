# Writer OS

Operating system for writing and revising docs.payu.in. These files are for Cursor agents. They are not documentation pages.

ReadMe publishes only the folders named in `_readme.yaml`: `docs/`, `recipes/`, and `reference/`. Writer OS stays outside those folders and is not listed in any `_order.yaml`, so it does not appear in the docs navigation and it does not become a page on docs.payu.in. Do not move this folder under `docs/`, `recipes/`, or `reference/`.

## Install

Open this repository in Cursor. These files load with the project:

- `.cursor/rules/writer-os-principles.mdc`
- `.cursor/rules/writer-os-stage-gate.mdc`
- `.cursor/rules/writer-os-execution-rigor.mdc`
- `.cursor/skills/writer-os/` and the `writer-*` skills next to it

## Prompt library

Agent prompts you can reuse live in `writer-os/prompts/`. Copy `_TEMPLATE.md` to a new file to add one. Start an agent with `Run prompt doc-update` or `Run prompt restructure`, and fill the `{{placeholders}}`.

## How to ask

Describe the documentation job in plain language. The agent names the skill in the first line. You can override with `Using writer-page-draft:` (or any other `writer-*` skill).

Nothing moves to the next stage until you confirm the specific risky claim. A full chain still pauses at each handoff:

```text
Run source brief through page draft for this guide, and pause at each handoff.
```

Internal notes go in `writer-os/work/<slug>/`. Those notes are not published. Published pages are written only under `docs/`, `recipes/`, or `custom_blocks/` after you confirm that stage.

## Roles

Content lead · Technical writer · Editor · Publisher

## Motions

1. **Guide** — source brief → scope canvas → page draft → editorial review → accuracy review → IA publish → release note only if behavior or deprecation changed.
2. **API reference** — same chain, with API reference and a recipe between scope and editorial review.
3. **Deprecation or what's-new only** — source brief → release note → editorial review → accuracy review.
4. **Existing doc update** — a dev-docs JIRA ticket names the file and the change. The agent creates `v1_<ISSUE-KEY>-<short-slug>` from `v1`, edits only that change, and opens a pull request. You merge. Docs go live after that merge.
5. **Restructure** — you supply an information architecture or a reference doc. The agent creates `v1_restructure-<slug>` from `v1` (or `v1_<ISSUE-KEY>-<slug>` when you pass a key), creates the files that outline names, updates `_order.yaml` for those files, and opens a pull request. You review and merge.

## Branch name

ReadMe syncs branches named `v1_{branch}`. `{branch}` is the short slug. The stable line stays `v1`. The agent does not use `update/…`.

Skill details: `.cursor/skills/writer-os/collaboration-map.md`.

## Editing rules that still win

Repository editing rules still apply inside every skill: do not edit `RECYCLE BIN/`, do not change frontmatter unless the task asks, keep code samples in `recipes/`, use parameter tables, and link error codes from `payment-error-codes.json`.
