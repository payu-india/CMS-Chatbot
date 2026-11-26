---
name: writer-recipe
description: >-
  Writes PayU docs code samples in recipes/ for Java, PHP, Python, and cURL so
  every field matches the confirmed API page or parameter table. Use when
  adding or fixing request examples, sample code, or integration recipes. Use
  writer-recipe.
---

# Recipe

## Purpose

Add samples under `recipes/` that a merchant can transpose without inventing a field. The guide page links to them. It does not become the only copy.

## Decision summary

- **Decision being made:** That the sample sends every field on the confirmed table, required and optional.
- **Decider:** Technical writer.
- **Reversibility:** two-way medium. A sample merchants paste is a contract.
- **Cost if wrong:** a copied sample that fails or moves money with the wrong payload.

## Inputs required

- Confirmed API page or a confirmed parameter table in the scope canvas.
- The spec path already read for that page.
- Target recipe paths. If the canvas did not name them, propose paths under `recipes/` and ask before writing.

## Agentic workflow

1. Context check. No confirmed field list: stop. Do not draft a sample from a feature name.
2. Annexure first: `writer-os/work/<slug>/04-recipe-ANNEXURE.md`.
3. Write one sample per language the canvas names. Default set, when the canvas says "the usual samples," is Java, PHP, Python, and cURL. Skip a language only if the canvas says so.
4. Use placeholders `YOUR_KEY`, `YOUR_SALT`, `YOUR_TXNID`. No live credentials, card numbers, or VPAs that look real.
5. Every sample sends every field from the request or response table, required and optional, using the row examples. If the table format marks type or required in bold or backticks, do not restyle those rows while touching the sample.
6. Hash samples call the same field order as `custom_blocks/HashingSample.md` (payment or general). Do not re-derive the string.
7. Link the samples from the in-scope page with a relative link. Do not paste the full sample into `docs/` as a second source.
8. Cross-link annexure and recipe files. Score. Commit and push the `v1_{branch}` branch. Ask the user to confirm the field set in the sample. Stop. Do not merge.

## Quantitative method

For each language: required fields present, extra fields not in the table (must be zero), hash present or not applicable.

## Red-team pass

- **Wrong integrator:** test URL in a sample the page says is live, or the reverse.
- **Stale contract:** a renamed field that still matches an old page.
- **Secret leakage:** anything that is not a placeholder.
- **Support load:** a missing `txnid`, amount format, or hash that would fail the first call.

## Tripwires and rollback

Field in sample absent from the table. Required or optional table field missing from the sample. Hash order differs from the custom block. A second full copy of the sample left in `docs/`.

**Rollback owner:** technical writer. Delete the new recipe files or restore the old ones.

## Output

Recipe files under `recipes/`, the page link, and `04-recipe-ANNEXURE.md` with `Writer-OS-Metrics: skill_id=writer-recipe, date=YYYY-MM-DD`.

Each recipe file ends with `Decision record: writer-os/work/<slug>/04-recipe-ANNEXURE.md` only if that file format is markdown. For source files, put the cross-reference in the annexure and in the page near the link, not inside the code.

## Anti-patterns

- A cURL sample that "simplifies" by dropping a required or optional field.
- Pseudocode instead of the four languages when the canvas asked for samples.
- Real-looking card PANs even as examples.

## Handoff

**Editor** — decision: can a merchant paste the sample after substituting placeholders and match the parameter table exactly. Next skill: `writer-editorial-review`.

## Frameworks applied

WR-4, WR-3, WR-6
