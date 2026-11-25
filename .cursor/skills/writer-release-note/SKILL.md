---
name: writer-release-note
description: >-
  Writes an integrator-facing release or deprecation note for docs.payu.in,
  with the reasoning in an annexure. Use when documenting what changed, a
  deprecated page, or a replacement path for an existing API or guide. Use
  writer-release-note. Not a marketing announcement.
---

# Release note

## Purpose

Tell an integrator what changed, what they must do, and what remains supported. Deprecation points at a replacement. It does not delete the old page and does not edit `RECYCLE BIN/`.

## Decision summary

- **Decision being made:** What changed for implementers, and whether the old path is deprecated.
- **Decider:** Publisher. Content lead confirms before the note is treated as final.
- **Reversibility:** two-way medium for a what's-new paragraph; one-way once `deprecated: true` is set on a live page.
- **Cost if wrong:** merchants migrate to the wrong API, or stay on one you meant to retire.

## Inputs required

- Confirmed source brief, or a cold start that lists old path, new path, and the behavior delta with a spec citation.
- For a deprecation, the user must explicitly ask to change frontmatter `deprecated`. Otherwise describe the deprecation in the note and leave frontmatter alone.
- Accuracy pass **pass** when this note follows a page change. For Motion C (note only), the source brief's citations must be opened in this turn.

## Agentic workflow

1. Context check. No old/new behavior delta: stop. Do not write "various improvements."
2. Annexure first: `writer-os/work/<slug>/08-release-ANNEXURE.md` with all six rigor sections.
3. Functional note: either a short section the canvas named, or `writer-os/work/<slug>/08-release-note.md` if no page was in scope. The functional note contains: what changed, who must act, the date if the user supplied one, and the replacement link. If the date was not supplied, omit it. Do not invent an effective date.
4. Set `deprecated: true` only when the user asked. Keep every other frontmatter field. Add one pointer to the replacement at the top of the old page.
5. Do not move the old page into `RECYCLE BIN/`. Do not edit files already in `RECYCLE BIN/`.
6. Cross-link note and annexure. Score. Ask the content lead to confirm the behavior delta. Stop. Do not commit.

## Quantitative method

Count of behavior changes stated, count that cite a path, count of invented dates (must be zero).

## Red-team pass

- **Wrong integrator:** a note that tells a hosted-checkout merchant to change a merchant-hosted field, or the reverse.
- **Stale contract:** the note describes a field the current spec does not have.
- **Secret leakage:** not applicable if the note has no samples. Say why.
- **Support load:** "please migrate" with no replacement link.

## Tripwires and rollback

A deprecation flag set without an explicit user request. A date the user did not provide. A replacement link that does not resolve in the repo. No statement of what still works.

**Rollback owner:** Publisher. Restore frontmatter and remove the note section.

## Output

- Functional note with no rigor headings.
- `08-release-ANNEXURE.md` with `Writer-OS-Metrics: skill_id=writer-release-note, date=YYYY-MM-DD`.
- The note's last line: `Decision record: writer-os/work/<slug>/08-release-ANNEXURE.md`.

## Anti-patterns

- Marketing language ("excited to announce").
- Deprecating by deletion.
- A changelog that bundles unrelated products because they were in the same branch.

## Handoff

**Editor** — decision: run `writer-editorial-review` if this note has not been reviewed. If it has, **Content lead** — decision: confirm the delta is the one they want merchants to read.

## Frameworks applied

WR-5, WR-6, WR-2
