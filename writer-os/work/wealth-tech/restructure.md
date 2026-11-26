# Restructure note — Wealth Tech

Functional tree: `docs/Offerings/wealth-tech/`. This file stays unstaged.

## 1. Decision summary

- **Decision being made:** Publish a new Offerings section for equity, mutual funds, and bonds from the Wealth Tech HTML guides, in the page list the user supplied.
- **Decider:** Technical writer for the files. The user (Publisher) decides whether to merge.
- **Reversibility:** Two-way medium. These are new pages. No existing page was deleted, hidden, or rewritten. `docs/Offerings/_order.yaml` gained one entry, `wealth-tech`, after `festive-checkout-experience`.
- **Cost if wrong:** An integrator uses the wrong hash or the wrong product field and the payment is rejected, or funds are expected in the wrong account.

The user confirmed the contract in this conversation: write the new pages from the HTML guides, and do not edit existing docs. `docs/Offerings/mutual-funds-payments/` and `reference/Wealth Tech/` were not modified.

## 2. Cognitive pre-work

- **Reader base rate:** A merchant developer at a SEBI-registered stock broker, mutual fund broker, direct AMC, or OBPP who already posts PayU `_payment` and needs the Wealth Tech fields.
- **Falsifiers:** Hash strings and `products` samples in the HTML guides; `reference/Wealth Tech/collect-payment-for-wealthtech-payu-hosted.md` still shows `more_info.wtParams` and `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)`.
- **Pre-mortem:** An integrator shipped the standard payment hash and `more_info.wtParams` because an older reference page is still public, while these new pages require `products` and the longer hash. The build pages and the API page state that difference.
- **Inversion:** One blended page that uses `api_version=21` for equity would fail stock-broker requests. The tree keeps equity, mutual funds, and bonds in separate folders, with `api_version` 6 only on equity.

## 3. Quantitative method

- Pages named in the confirmed tree: 25 markdown pages. Pages created: 25. Order files created: 4 (`wealth-tech`, `equity`, `mutual-funds`, `bonds`).
- `_order.yaml` entries added outside the new tree: 1 (`wealth-tech` on `docs/Offerings/_order.yaml`).
- Parameters on each build page: 12 equity fields, 13 mutual fund fields, 13 bond fields, matching the HTML tables.
- Product-object fields: 12 mutual fund fields, 7 required bond fields plus the five unused AMC fields, matching the HTML tables.
- Error messages copied from the mutual fund and bond HTML tables: 8 mutual fund rows, 6 bond rows. Equity TPV and hash codes are unpublished in the HTML (`[TBC]` removed, no code invented).
- `payment-error-codes.json`: not applicable because the HTML gives condition text, not entries from that file, and those codes were not added.
- Recipe files: not applicable because the outline put the cURL samples on the build and recurring pages and did not name `recipes/`.
- Internal links: build, product, recurring, response, test, and go-live links point at files created in this tree. External links used: `doc:generate-test-merchant-key-and-salt`, `doc:generate-merchant-key-and-salt-on-payu-dashboard`, `doc:hashing-request-and-response`, `doc:webhooks`, `doc:tpv-recurring-payments-integration-pay-hosted-checkout`, `ref:verify_payment_api`. `<KeySaltReference />` is the test-key block.

## 4. Red-team pass

- **Wrong integrator:** A broker who copies the direct AMC sample will send scheme fields and more than one object. Broker and AMC samples are in separate tabs. Bonds are a separate folder and settle to NCL.
- **Stale contract:** `reference/Wealth Tech/` still documents `more_info.wtParams` on `_payment` and the standard hash. These new pages follow the HTML (`products` on `_payment`, `wtParams` only inside `si_transaction` `var1`). The user chose the HTML and said not to edit the reference pages. That disagreement remains for the Publisher.
- **Secret leakage:** Samples use `YOUR_KEY` and `YOUR_SHA512_HASH`. Account numbers, UCC-style ids, and the recurring `card_token` are the example values from the HTML guides, labelled as samples.
- **Support load:** Test pages do not invent sandbox VPAs or bank accounts, because the HTML guides do not list them. Settlement timing is not stated, because the HTML guides do not give a clock. `bse2`, `nse_mf`, and `cams` are called out as not available yet.

## 5. Tripwires and rollback

- A request hash on a build page that does not match the HTML string for that product.
- A mutual fund or bond sample that omits `products`, or an equity sample that sends `products`.
- An `_order.yaml` entry with no file. `wealth-tech` maps to `docs/Offerings/wealth-tech/index.md`.
- A page under `docs/Offerings/mutual-funds-payments/` or `reference/Wealth Tech/` changed in this branch. None should be.

**Rollback owner:** the user. Close the pull request. The agent does not push `v1`. Restore the previous markdown by reverting the feature branch.

## 6. Frameworks applied

- WR-1. Each page has one job: choose a product, build the request, describe `products`, debit a mandate, verify the response, test, or go live.
- WR-3. Test keys link `KeySaltReference` and the dashboard key pages. The Wealth Tech hash is not the string in `custom_blocks/HashingSample.md`. The pages say so and link `doc:hashing-request-and-response` as the standard hash, not as the Wealth Tech hash. Counter-metric: a merchant whose `_payment` hash matches HashingSample and omits `beneficiarydetail` or `products` is rejected.
- WR-5. New URLs only. Existing mutual fund docs were left in place, including their current `hidden` flags. No `deprecated: true` was set.
- Decision requested of the Publisher: merge the pull request, or name the page whose hash or `products` sample does not match the HTML guide.
- `Writer-OS-Metrics: skill_id=writer-restructure, date=2026-11-25`

Rubric on this note: D1–D8 present. Raw 8. Rubric 5.0. The pages still need the Publisher's merge decision. No JIRA key was supplied. Branch: `v1_restructure-wealth-tech`.
