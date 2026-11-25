---
name: writer-source-brief
description: >-
  Builds a source brief that lists what is already true about a docs.payu.in
  change and which repo files prove it. Use when starting a documentation
  project, gathering evidence before writing a guide or API page, or when the
  user asks what sources exist for a topic. Use writer-source-brief.
---

# Source brief

## Purpose

Lock the evidence before any page is written. Record which files in this repo support the change, which contradict it, and what is still unknown.

## Decision summary

- **Decision being made:** Which sources the later page is allowed to cite.
- **Decider:** Technical writer. Content lead confirms the brief is complete enough to scope.
- **Reversibility:** two-way low.
- **Cost if wrong:** a page that documents behavior the spec does not contain.

## Inputs required

- The reader segment (merchant developer, partner platform, or internal operator).
- The product area (for example checkout, payouts, BBPS, partners, WhatsApp).
- The job the page should help the reader finish, even if rough.
- Any existing page path or spec path the user already trusts. Optional. Do not invent one.

## Agentic workflow

Follow `writer-os-stage-gate.mdc`.

1. Context check. If segment, product area, or job is missing, ask. Do not infer a product area from a vague noun.
2. Search `docs/`, `reference/`, `custom_blocks/`, `recipes/`, and `payment-error-codes.json` for the job. Read the files you will cite. Searching filenames is not reading.
3. Classify each hit: **cite**, **conflict**, or **out of scope**.
4. Write `writer-os/work/<slug>/01-source-brief.md` using the template below. Put all six rigor sections in that file.
5. Score with `.cursor/skills/writer-os/quality-rubric.md`. If the rubric is under 3.5, revise before asking for confirmation.
6. Ask the user to confirm the source list. Name the claim most likely to be the wrong file. Stop. Do not start the scope canvas.

## Quantitative method

Counts: files read, files marked cite, files marked conflict, topics with no file (unknowns). "Not applicable" is not allowed for this skill.

## Red-team pass

- **Wrong integrator:** a source from a different product area (hosted checkout cited for merchant-hosted, or the reverse).
- **Stale contract:** an older page that disagrees with `reference/` or `payment-error-codes.json`.
- **Secret leakage:** not applicable — this artefact cites paths, not credentials. Say that reason.
- **Support load:** an unknown that, if filled in later by guesswork, would make a merchant call support.

## Tripwires and rollback

- A later page cites a path that is not on this brief.
- Two cited files describe different request fields for the same API.
- **Rollback owner:** the technical writer. Delete or replace `01-source-brief.md` before the scope canvas is confirmed.

## Output

`writer-os/work/<slug>/01-source-brief.md`

```markdown
# Source brief — [job]

Segment: [reader]
Product area: [area]
Job: [one sentence]

## Decision summary
## Cognitive pre-work
## Sources
| Path | Status (cite / conflict / out of scope) | What it supports | Lines or section read |
## Unknowns
## Quantitative method
## Red-team pass
## Tripwires and rollback
## Frameworks applied
Writer-OS-Metrics: skill_id=writer-source-brief, date=YYYY-MM-DD

## Handoff
Content lead — decision: confirm this source list is sufficient to lock scope, or name the missing file.
```

## Anti-patterns

- Inventing an endpoint, parameter, or error code because the search was empty. Record it as an unknown and stop.
- Citing `RECYCLE BIN/` as a source of truth.
- Treating a page title match as evidence without opening the file.

## Handoff

**Content lead** — decision: confirm the source list, or name the file still missing. Next skill after confirmation: `writer-scope-canvas`.

## Frameworks applied

WR-2, WR-6
