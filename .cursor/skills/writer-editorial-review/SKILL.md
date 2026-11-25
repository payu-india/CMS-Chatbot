---
name: writer-editorial-review
description: >-
  Reviews a docs.payu.in page for reader task, structure, voice, and leaks of
  internal decisioning. Use when editing a draft for clarity, heading structure,
  or whether an integrator can finish the job. Use writer-editorial-review.
  Accuracy against the spec is writer-accuracy-review.
---

# Editorial review

## Purpose

Decide whether the named reader can finish the job from this page alone, and whether the published file still reads as a page.

## Decision summary

- **Decision being made:** Accept the draft for accuracy review, or return it with specific rewrites.
- **Decider:** Editor.
- **Reversibility:** two-way low. Review comments do not change the public contract by themselves.
- **Cost if wrong:** a clear page that is still wrong (that is the next skill), or a rewrite that drops a required step.

## Inputs required

- Confirmed page, API page, or release note, plus its annexure.
- Confirmed scope canvas (segment, job, non-goals).

## Agentic workflow

1. Context check. Unconfirmed draft: stop.
2. Read the functional file as a reader. Do not re-check the spec in this skill. That is `writer-accuracy-review`.
3. Check the opening states the task, the segment's product area, and test versus live when both exist.
4. Check heading order, parameter tables where fields exist, and that non-goals did not become sections.
5. Check the functional file has no Decision summary, Cognitive pre-work, Red-team, or Tripwires headings. Those belong in the annexure.
6. Check frontmatter was not changed unless the scope asked for it.
7. Write `writer-os/work/<slug>/05-editorial-review.md` with the six rigor sections inline. Each finding is a file path and a quoted heading or sentence, plus the rewrite.
8. Verdict: **accept** or **return**. Ask the writer to confirm the finding you are least sure is a real defect. Stop.

## Quantitative method

Count of blocking findings, count of suggestions, and whether the first screen contains the task (yes/no). Not applicable is not allowed.

## Red-team pass

- **Wrong integrator:** steps that assume a dashboard click for an API-only reader, or the reverse.
- **Stale contract:** not applicable in this skill — accuracy review owns spec drift. Say why.
- **Secret leakage:** placeholder scan. Any live-looking key fails the review.
- **Support load:** a step that says "configure as needed" or "handle errors" with no next link.

## Tripwires and rollback

Blocking finding left unresolved and the next skill still starts. Decisioning headings copied into `docs/`.

**Rollback owner:** Editor. The page is unchanged by this skill unless the user asks to apply a rewrite. Default is a review file only.

## Output

`writer-os/work/<slug>/05-editorial-review.md`

```markdown
# Editorial review — [job]

## Decision summary
Verdict: accept | return
## Cognitive pre-work
## Findings
| # | Path | Quoted text | Blocking? | Rewrite |
## Quantitative method
## Red-team pass
## Tripwires and rollback
## Frameworks applied
Writer-OS-Metrics: skill_id=writer-editorial-review, date=YYYY-MM-DD
## Handoff
```

## Anti-patterns

- A review that says "looks good" with an empty findings table and no verdict line.
- Rewriting the page in the same turn as the review. Apply rewrites only if the user confirms them.
- Failing a page for tone that is already task-first and plain.

## Handoff

If the verdict is **return**: **Technical writer** — decision: apply the blocking rewrites and bring the page back.

If the verdict is **accept**: **Editor** — decision: run `writer-accuracy-review` on the same files. Next skill only after the user confirms the verdict.

## Frameworks applied

WR-1, WR-6
