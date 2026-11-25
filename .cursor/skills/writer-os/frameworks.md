# Writer OS — Domain frameworks

Cite these by id (WR-1 … WR-6) in the frameworks footer. They specialize the PM OS org frameworks for docs.payu.in. They do not replace repository editing rules.

## WR-1 Reader task first

Every page answers one job the integrator is in the middle of. The first screen states that job, the product area, and test versus live when both exist. A page that explains a product without a task is unfinished.

## WR-2 Spec is source of truth

`reference/` OpenAPI or JSON specs, `payment-error-codes.json`, and `custom_blocks/` outrank memory and older prose. If two sources disagree, quote both paths and stop for a human. Do not average them into a third behavior.

## WR-3 Reuse before rewrite

Search `custom_blocks/` and neighboring pages before writing a new explanation of hashing, errors, authentication, or test keys. Link to the block. A second copy will drift.

Hash samples already live in `custom_blocks/HashingSample.md`.

- Payment API hash: `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)`
- General APIs hash: `sha512(key|command|var1|salt)`

Use these strings only when the page is about that hash. Do not invent a third formula.

## WR-4 Example is the contract

Every field in a recipe appears in the parameter table with the same name and required flag. Every required field appears in at least one recipe. Recipes live under `recipes/` (Java, PHP, Python, cURL). The guide page links to them instead of becoming the only copy of the sample.

## WR-5 Public contract is a door

Changing a documented endpoint, parameter, hash string, or error behavior is two-way medium or one-way. Set `deprecated: true` only when the task asks for a deprecation, and point to the replacement. Do not edit `RECYCLE BIN/`. Do not remove a live contract page as the way to deprecate it.

## WR-6 Counter-metric

Name how the doc fails in the wild: wrong hash, test key used in live, missing error branch, or a duplicate page that diverges. A change whose only success line is "clearer docs," with no failure signal, is incomplete.

## Segment header

Every artefact names one primary reader segment. Merchant-hosted checkout, PayU-hosted checkout, payouts, BBPS, partners, and WhatsApp payment links do not share one integration story. If the scope canvas lists two segments, say what is shared and what is not.
