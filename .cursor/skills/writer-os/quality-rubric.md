# Writer OS — Quality rubric

Score each substantive artefact before declaring the stage ready for confirmation. Target ≥3.5 to hand off. Target ≥4.5 to keep as a worked example under `writer-os/work/<slug>/`.

## Dimensions

Score each 0 or 1.

| # | Dimension | 1 if… |
|---|-----------|--------|
| D1 | Decision summary | Decision, decider, reversibility, and cost-if-wrong are all present |
| D2 | Cognitive pre-work | Reader base rate, falsifiers, pre-mortem, and inversion |
| D3 | Quantitative method | Coverage counts, or "not applicable because…" with a reason |
| D4 | Red-team pass | Every applicable lens has a concrete risk. A lens marked not applicable says why. A bare "not applicable" fails D4. Marking "wrong integrator" not applicable on a page merchants follow fails D4 outright |
| D5 | Tripwires and rollback | At least two measurable tripwires, a named owner, and a revert path |
| D6 | Handoff | Next role and one explicit decision |
| D7 | Frameworks footer | At least one WR-# and a counter-metric |
| D8 | Grounding | Repo paths or UNVERIFIED. No live secrets or production PII |

**Raw** = sum(D1…D8), 0–8.

**Rubric** = round(raw × 5 / 8, 1).

| Rubric | Meaning |
|--------|---------|
| 0–1.9 | Rewrite against execution rigor |
| 2.0–3.4 | Draft only. Do not hand off |
| 3.5–4.4 | Acceptable to confirm |
| 4.5–5.0 | Exemplar |

## Split artefacts

For page, API reference, recipe, and release note, read D1–D5 and D7 from the annexure and D6 and D8 from the functional file. A missing companion file fails the pair. Decisioning inside a `docs/` page fails D8 and the split rule.

## What the score does not do

The score does not replace the user's confirmation. A 5.0 draft is still unconfirmed until they answer the stage-gate question.
