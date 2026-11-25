---
name: writer-scope-canvas
description: >-
  Locks audience, in-scope pages, non-goals, and success criteria for a
  docs.payu.in change. Use when deciding what a documentation effort will and
  will not cover, before drafting a guide, API reference, or recipe. Use
  writer-scope-canvas.
---

# Scope canvas

## Purpose

Turn a confirmed source brief into a scope the writer is allowed to edit: audience, files in, files out, success, and non-goals.

## Decision summary

- **Decision being made:** What this documentation change includes and what it refuses.
- **Decider:** Content lead.
- **Reversibility:** two-way medium once a draft exists; two-way low before any page is written.
- **Cost if wrong:** the wrong pages get edited, or a public contract change is smuggled in as a copy edit.

## Inputs required

- Confirmed `01-source-brief.md`, or a cold-start message that lists segment, job, non-goals, and source paths.
- Whether the output is a guide page, an API reference, a recipe, a deprecation, or a combination.

## Agentic workflow

1. Context check. If the source brief is unconfirmed and the user did not start cold, stop.
2. State one reader segment and one job. If the brief implies two products, split them into shared versus not shared. Do not write a universal page.
3. List repo paths that may be created or edited. List paths that must not be touched, including `RECYCLE BIN/`.
4. Classify reversibility for the public contract, not for the markdown file.
5. Write `writer-os/work/<slug>/02-scope-canvas.md` with the six rigor sections inline.
6. Score the rubric. Ask the content lead to confirm the non-goals. Name the inclusion most likely to be scope creep. Stop.

## Quantitative method

Counts: pages in scope, pages explicitly out, source files the draft must open, open questions. If there are zero source files and the change is not a net-new explainer the user has accepted as UNVERIFIED, stop.

## Red-team pass

- **Wrong integrator:** scope that mixes two checkout models or two product areas without saying so.
- **Stale contract:** scope that updates a guide but leaves a contradicting page in place. Name that page as in-scope or as a known conflict.
- **Secret leakage:** not applicable — no samples in this artefact. Say why.
- **Support load:** a non-goal that drops test-versus-live, hashing, or errors when the job needs them.

## Tripwires and rollback

- A later skill edits a path not listed as in scope.
- A non-goal shows up as a section in the draft.
- **Rollback owner:** Content lead. Replace `02-scope-canvas.md` before the draft is confirmed.

## Output

`writer-os/work/<slug>/02-scope-canvas.md`

```markdown
# Scope canvas — [job]

Segment: [reader]
Job: [one sentence]

## Decision summary
## Cognitive pre-work
## In scope
| Path | Action (create / edit / link only) | Why |
## Out of scope
## Success
The reader can [task] without guessing [specific fact].
## Non-goals
## Open questions
## Quantitative method
## Red-team pass
## Tripwires and rollback
## Frameworks applied
Writer-OS-Metrics: skill_id=writer-scope-canvas, date=YYYY-MM-DD

## Handoff
Technical writer — decision: draft only the in-scope paths, using writer-page-draft and/or writer-api-reference.
```

## Anti-patterns

- Non-goals left blank.
- "Update the docs" as the job.
- Adding `_order.yaml` or a release note to scope by default. Those belong to Publisher skills after the draft is confirmed, unless the user put them in scope here.

## Handoff

**Technical writer** — decision: which of `writer-page-draft`, `writer-api-reference`, and `writer-recipe` to run, and only those. Next skill is one of those three, after confirmation.

## Frameworks applied

WR-1, WR-5, WR-6
