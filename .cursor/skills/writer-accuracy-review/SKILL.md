---
name: writer-accuracy-review
description: >-
  Checks a docs.payu.in draft claim by claim against reference specs,
  payment-error-codes.json, and custom blocks. Use when verifying API fields,
  hash formulas, error codes, or whether a page invents behavior. Use
  writer-accuracy-review.
---

# Accuracy review

## Purpose

Decide whether every contractual claim in the draft is backed by a file you opened in this turn.

## Decision summary

- **Decision being made:** Which claims are supported, which are UNVERIFIED, and whether the page can go to publish.
- **Decider:** Editor.
- **Reversibility:** two-way medium. Publishing an unsupported field is the expensive direction.
- **Cost if wrong:** merchants implement a contract PayU does not serve.

## Inputs required

- Editorial verdict **accept**, confirmed, or a user waiver that says accuracy may run in parallel. Record the waiver.
- The functional page and its annexure.
- The spec, error-code, and custom-block paths named in the source brief. Open them again. Do not trust the annexure's citations without reading.

## Agentic workflow

1. Context check. Missing spec path for an API page: stop. Do not review "from knowledge."
2. Split the page into claims (a field, a step that changes a request, a hash, an error, a URL). Ignore pure navigation prose.
3. For each claim, record **Supported** plus path, or **UNVERIFIED**. A conflict between two opened files is **Conflict**, not a coin flip.
4. Required fields and hash strings must be Supported. One UNVERIFIED required field fails the stage.
5. Write `writer-os/work/<slug>/06-accuracy-review.md` with the six rigor sections and the claim table.
6. Verdict: **pass** or **fail**. Ask the user to confirm the claim you almost marked Supported. Stop. Do not edit the page unless they ask.

## Quantitative method

Required. `supported / total claims`, `unverified required fields` (must be 0 to pass), `conflicts`.

## Red-team pass

All four lenses are in play. Secret leakage fails the stage on any non-placeholder credential. Stale contract must name the file that would drift.

## Tripwires and rollback

An UNVERIFIED required field. A hash that does not match `custom_blocks/HashingSample.md`. An error code absent from both the spec and `payment-error-codes.json`. A recipe field that failed parity.

**Rollback owner:** Editor. Page stays as drafted until the technical writer applies a fix the user confirms.

## Output

`writer-os/work/<slug>/06-accuracy-review.md` including:

```markdown
## Claims
| # | Claim (short) | Verdict | Path |
```

`Writer-OS-Metrics: skill_id=writer-accuracy-review, date=YYYY-MM-DD`

## Anti-patterns

- Marking Supported because the sentence "sounds like PayU."
- Editing `reference/` specs to match the page. The spec wins until a human says otherwise.
- Passing with conflicts hidden in prose.

## Handoff

**Fail:** Technical writer — decision: remove or source each failed claim, then return here.

**Pass:** Publisher — decision: whether navigation must change (`writer-ia-publish`) and whether a release note is required. Next skill after confirmation: `writer-ia-publish`.

## Frameworks applied

WR-2, WR-4, WR-5
