---
name: writer-api-reference
description: >-
  Writes a docs.payu.in API reference page from an OpenAPI or JSON spec in
  reference/, with parameters, errors, and hash notes sourced from files.
  Decisioning goes in an annexure. Use when documenting an endpoint, request
  or response fields, or an API contract. Use writer-api-reference.
---

# API reference

## Purpose

Produce a reference page whose tables match a spec file you opened. Reasoning stays in the annexure.

## Decision summary

- **Decision being made:** Which operations and fields this page documents, and which it leaves to another page.
- **Decider:** Technical writer.
- **Reversibility:** two-way medium for a new reference page; one-way if it changes a field merchants already send.
- **Cost if wrong:** failed API calls or a wrong hash.

## Inputs required

- Confirmed scope canvas, or a cold start naming the spec path, segment, and non-goals.
- The spec file path under `reference/`. You must open it.
- `payment-error-codes.json` if the page documents errors.
- `custom_blocks/HashingSample.md` if the operation uses a PayU hash.

## Agentic workflow

1. Context check. No spec path: stop and ask. Do not choose a similarly named spec on your own.
2. Read the operation. Extract method, path, required and optional parameters, and documented errors. If the spec and an existing `docs/` page disagree, list the conflict in the annexure and do not pick a winner.
3. Write `writer-os/work/<slug>/03-api-ANNEXURE.md` first (six rigor sections, coverage counts).
4. Write or edit only the in-scope page. Preserve frontmatter unless asked. Use tables:

| Name | In | Type | Required | Description | Source |
|------|----|------|----------|-------------|--------|

The Source column may live in the annexure instead of the published table if it clutters the page. The annexure must still map every row to a spec location.

5. Errors: a table of code, message, and when it happens, limited to codes you found in the spec or in `payment-error-codes.json`. Link the JSON file. Do not paste the whole file.
6. Hash: name payment versus general, link `custom_blocks/HashingSample.md`, and show the field order only from that block or from the spec. Missing salt-separator fields is a defect, not a style choice.
7. Cross-link the page and the annexure. Do not put rigor sections in `docs/`. Do not commit.
8. Score the pair. Ask the user to confirm the required-field list. Stop.

## Quantitative method

Required. `documented fields / fields on the operation`, `documented errors / errors named in the spec`, and how many rows are UNVERIFIED (target zero for required fields).

## Red-team pass

All four lenses. Stale contract is mandatory: name the spec path and the page path.

## Tripwires and rollback

A required spec field missing from the table. A table field absent from the spec. A hash string that does not match `custom_blocks/HashingSample.md`. An error code with no JSON or spec source.

**Rollback owner:** technical writer. Restore the previous page.

## Output

- In-scope API page, tables, no decisioning headings.
- Closing line: `Decision record: writer-os/work/<slug>/03-api-ANNEXURE.md`.
- Annexure with `Writer-OS-Metrics: skill_id=writer-api-reference, date=YYYY-MM-DD`.

## Anti-patterns

- Documenting from memory of PayU APIs.
- Merging two operations onto one page when the canvas named one.
- Example JSON that includes fields the table does not list.

## Handoff

**Technical writer** — decision: whether `writer-recipe` must run (yes if the page shows or promises a request sample).

**Editor** — decision: after the recipe, if any, accept the field list as the contract. Next skill: `writer-recipe` or `writer-editorial-review`.

## Frameworks applied

WR-2, WR-3, WR-4, WR-5
