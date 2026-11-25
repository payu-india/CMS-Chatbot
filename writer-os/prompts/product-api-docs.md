---
id: product-api-docs
skill: writer-api-reference
title: Document a product's APIs for review
---

# When to use

A product's source is newer than the docs. The user wants the existing pages aligned, the missing APIs added as normal markdown, and a PM review brief. Do not run this until `{{product}}` and `{{source}}` are filled.

# Fill in

- `{{product}}` — product area, such as partner payments
- `{{source}}` — repo path or the source the user names as the contract
- `{{branch}}` — short slug. The git branch is `v1_{{branch}}`

# Prompt

```text
Using writer-api-reference:

Document {{product}} from {{source}}. Branch from current origin/v1 as v1_{{branch}} and put only this change on it, so ReadMe shows current v1 plus these pages.

Match the existing pages in that section. Write markdown pages, not OpenAPI files, unless I ask for an OpenAPI page. When a parameter table changes, update the request and response samples in the same edit. Samples include every required and optional field. A new table row uses that table's columns and the same markup for type and required.

Put each new API in the existing section it belongs to. Create a new category only when it does not fit, with an index.md and an _order.yaml entry. The index overviews only the pages in that category, in the shape of reference/Self-Serve Products/payment-links/index.md: what those pages do, shared authentication, a card for each page, and a how-it-works sequence built from those pages.

A page this run creates is hidden: true and the title ends with [New]. Do not hide or retitle a page that already existed.

Commit and push v1_{{branch}}. Do not merge. Do not push v1.

When I ask for the PM review, write a decision brief and do not commit it. Changes are bullet points. Lead with the live-page corrections, then the new sections in one table, the confirmations, and the URLs. Say an agent made the edits, that this exercise will run on other products, and that issues should be reported back so the prompt can be adapted.
```
