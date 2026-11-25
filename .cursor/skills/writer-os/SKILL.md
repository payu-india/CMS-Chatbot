---
name: writer-os
description: >-
  Operating system for PayU developer documentation on docs.payu.in. Routes a
  documentation request to the right Writer OS skill, enforces stage order, and
  names the next role. Use when the user asks for Writer OS, a doc project, a
  new or revised guide, API reference, recipe, information architecture change,
  deprecation, or release note. Also use when the user brings a dev-docs JIRA
  ticket for an existing-page update, or an information architecture or
  reference doc for a restructure that should end in a pull request. Do not
  use for a single named-file typo or wording fix with no branch or PR.
---

# Writer OS

PayU developer-docs operating system for this repository (docs.payu.in). Adapted from the PM OS kit pattern: shared principles, a fixed artefact shape, stage gates, and role skills. Domain rules for this repo stay in force (frontmatter, `RECYCLE BIN/`, `custom_blocks/`, `recipes/`, `_order.yaml`, error codes, hash samples).

Writer OS files are not docs pages. Do not add them to `_order.yaml` or `_readme.yaml`. ReadMe publishes only `docs/`, `recipes/`, and `reference/`.

## When to start

Read this skill when a documentation project starts, or when the user says "Writer OS."

1. Read [collaboration-map.md](collaboration-map.md) and pick one motion.
2. First line, before any draft: `Reading this as writer-<skill> — say if that's wrong.`
3. Open that skill and run its context check. Do not draft the page in this turn unless the picked skill is the one whose inputs are already confirmed.
4. Write internal artefacts under `writer-os/work/<slug>/`. `<slug>` is kebab-case from the page or API name.
5. Do not commit or push unless the user asks in this conversation. Exception: `writer-doc-update` and `writer-restructure` commit, push a `v1_{branch}` branch, and open a pull request into `v1`. They do not merge.

A named file and a typo, link, or wording fix, with no request for a branch or a pull request, is not a Writer OS stage. Say `Treating this as a scoped edit, not a Writer OS stage.` and edit only that file.

A JIRA key or a pasted change request is Motion D (`writer-doc-update`). An IA or a reference doc plus a restructure ask is Motion E (`writer-restructure`). Ticket shape: [ticket-format.md](ticket-format.md).

## Prompt library

Saved agent prompts live in `writer-os/prompts/`. One file per prompt. `_TEMPLATE.md` is the blank copy, not a prompt to run.

When the user says `Run prompt <id>` or names a file in that folder, open `writer-os/prompts/<id>.md` and follow its `prompt` block and `skill`. Do not paraphrase the prompt. If a `{{placeholder}}` is still empty, ask for that value and stop. Ignore `_TEMPLATE.md`.

## Roles

| Role | Decides |
|------|---------|
| Content lead | Audience, pages in scope, non-goals |
| Technical writer | Page, API reference, and recipe accuracy against sources |
| Editor | Whether a reader can finish the task, and whether every claim is sourced |
| Publisher | Navigation, `_order.yaml`, deprecation, release note, and merging a doc-update or restructure pull request |

## Skills

| Skill | Stage |
|-------|--------|
| `writer-source-brief` | What is true, and which files prove it |
| `writer-scope-canvas` | Audience, files in and out, success, non-goals |
| `writer-page-draft` | Guide page plus annexure |
| `writer-api-reference` | API page from an OpenAPI file plus annexure |
| `writer-recipe` | Java, PHP, Python, cURL samples plus annexure |
| `writer-editorial-review` | Task fit, structure, voice, leaks of internal decisioning |
| `writer-accuracy-review` | Claim-by-claim check against spec and error codes |
| `writer-ia-publish` | Order, links, custom-block reuse |
| `writer-release-note` | Integrator-facing change or deprecation note |
| `writer-doc-update` | JIRA ticket to a pull request for an existing page |
| `writer-restructure` | IA or reference doc to new files and a pull request |

## Also read

- [frameworks.md](frameworks.md) — WR-1 through WR-6
- [quality-rubric.md](quality-rubric.md) — score before calling a stage done
- `.cursor/rules/writer-os-principles.mdc`
- `.cursor/rules/writer-os-stage-gate.mdc`
- `.cursor/rules/writer-os-execution-rigor.mdc`

## Smoke test

Use once on a fictional slug. Do not write under `docs/` until the user confirms the page-draft stage.

```text
Using writer-source-brief: fictional page "Retry a failed UPI collect".
Segment: merchant developer.
Evidence: say which files you would need in reference/ and payment-error-codes.json.
If those files are not named, stop and ask. Do not invent endpoints.
```

Expected next skill after confirmation: `writer-scope-canvas`.
