---
name: writer-page-draft
description: >-
  Drafts or revises a docs.payu.in guide page from a confirmed scope canvas,
  with decisioning kept in a companion annexure. Use when writing or
  substantially updating a documentation page, integration guide, or how-to.
  Use writer-page-draft. Not for OpenAPI field tables (use writer-api-reference)
  or a one-line wording fix.
---

# Page draft

## Purpose

Write the reader-facing guide, and keep the reasoning in an annexure so the published page stays a page.

## Decision summary

- **Decision being made:** What the page asserts, and what it refuses to assert.
- **Decider:** Technical writer. Editor accepts it only after editorial and accuracy review.
- **Reversibility:** from the scope canvas. Do not downgrade a contract change to a copy edit.
- **Cost if wrong:** an integrator follows the wrong steps.

## Inputs required

- Confirmed scope canvas, or a cold start that states segment, job, non-goals, in-scope paths, and sources.
- The source files named on the brief, opened in this turn.
- Search of `custom_blocks/` before any new inline explanation of hashing, errors, auth, or test keys.

## Agentic workflow

1. Context check. Missing canvas or unconfirmed sources: stop.
2. Fill the annexure first at `writer-os/work/<slug>/03-page-ANNEXURE.md`. All six rigor sections live there.
3. Draft or edit only in-scope page files. Preserve YAML frontmatter unless the task says to change it. Match this shape when creating a page:

```yaml
---
title:
excerpt:
deprecated: false
hidden: false
metadata:
  robots: index
---
```

4. Page body, in order: the reader task, prerequisites, steps, a parameter table when the page has fields, errors linked from `payment-error-codes.json` when the page has errors, and a link to an existing custom block instead of a pasted duplicate.
5. Hash content: link `custom_blocks/HashingSample.md`. Quote the payment or general formula only when this page is about that hash. Do not invent a formula.
6. Mark any sentence you could not tie to an opened file as **UNVERIFIED** in the annexure, not as confident prose. Prefer omitting it.
7. The page and the annexure must name each other.
8. Do not edit `_order.yaml`, `RECYCLE BIN/`, or files outside scope. Do not commit.
9. Score the pair. Ask the user to confirm the sentence most likely to be wrong. Stop.

## Quantitative method

Parameters in the table versus parameters you actually found in source. Error codes mentioned versus keys you opened in `payment-error-codes.json`. Custom blocks reused versus new explanations. If the page has no parameters, say so.

## Red-team pass

Run all four lenses in the annexure. A guide page always has a wrong-integrator risk.

## Tripwires and rollback

Spec contradiction, duplicated custom block, broken relative link, UNVERIFIED sentence left in the page body.

**Rollback owner:** technical writer. Restore the previous page markdown. Remove the new file if this stage created it and the user rejects it.

## Output

- Functional page at the in-scope path. No rigor headings in the body.
- `writer-os/work/<slug>/03-page-ANNEXURE.md` with the six sections, the rubric score, and `Writer-OS-Metrics: skill_id=writer-page-draft, date=YYYY-MM-DD`.

End the page with a single line: `Decision record: writer-os/work/<slug>/03-page-ANNEXURE.md`. That line is the cross-reference, not a rigor section.

## Anti-patterns

- Writing the page before the annexure.
- Changing `title`, `excerpt`, `deprecated`, `hidden`, or `metadata` when the task did not ask.
- A step list with no reader task in the opening.
- Code samples as the only copy of the example when the scope includes `writer-recipe`. Link the recipe path instead, or leave a placeholder the recipe skill will fill, and say which.

## Handoff

**Editor** — decision: does a reader in the named segment finish the job without a second page, and is any sentence still UNVERIFIED. Next skill after confirmation: `writer-editorial-review`.

## Frameworks applied

WR-1, WR-3, WR-4
