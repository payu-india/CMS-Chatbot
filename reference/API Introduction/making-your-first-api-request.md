---
title: API Versioning
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU uses a **capability-driven versioning model**. Unlike a single global `/v1` surface for every product, versioning appears as:

- an `api_version` request parameter on many Collect Payment flows
- path-based versions for selected APIs (for example, `/v2/payments`)
- feature-specific request fields that change hash formulas

## Versioning mechanisms

| Mechanism                        | Where you see it                                      | What it controls                                        |
| :------------------------------- | :---------------------------------------------------- | :------------------------------------------------------ |
| `api_version`**&#x20;parameter** | `_payment` and related checkout/subscription requests | Enables fields and behaviors for a given capability set |
| **URL path version**             | e.g. `https://api.payu.in/v2/payments`                | Selects a distinct API contract                         |
| **Feature payload fields**       | `si_details`, `splitRequest`, offers fields, etc.     | Adds required hash segments and validation rules        |

## Using `api_version` with Collect Payment

Some integrations require a specific `api_version` value. Examples commonly seen in docs include values such as `7` or `19`, depending on the feature.

Rules of thumb:

1. Set `api_version` exactly as required by the Integration Guide / API Reference for that feature.
2. Regenerate `hash` after including version-dependent fields.
3. Do not assume a newer number is always better — use the version documented for your flow.

### Example: hash changes with version 19

For `_payment` with **api_version=19**, hash input expands to include additional fields such as `udf6…udf10`, `user_token`, offer fields, cart details, extra charges, and phone.

See [API Authentication and Security](doc:api-authentication-and-security) and [Generate Hash](doc:hashing-request-and-response).

## Path-based versions

Selected products expose versioned hosts/paths:

| Environment | v2 Payments base URL                  |
| :---------- | :------------------------------------ |
| Test        | `https://apitest.payu.in/v2/payments` |
| Production  | `https://api.payu.in/v2/payments`     |

When an API is on a versioned path, treat it as a separate contract: different auth, headers, or response shapes may apply.

## How to choose the correct version

| Question                                         | Action                                                      |
| :----------------------------------------------- | :---------------------------------------------------------- |
| Does my Integration Guide specify `api_version`? | Use that exact value                                        |
| Does the API Reference path include `/v2/`?      | Use the v2 base URL and schema                              |
| Am I enabling SI, split, offers, or TPV fields?  | Confirm whether hash formula changes                        |
| Am I copying an old sample?                      | Diff required fields against the current API Reference page |

## Compatibility guidance

- Pin the version your integration was certified with.
- When upgrading versions, retest hash generation, callbacks, and Verify Payment handling in Test.
- Keep version values in server-side configuration — not hard-coded in multiple places inconsistently.

## What to read next

- [API Architecture](doc:api-architecture)
- [API Authentication and Security](doc:api-authentication-and-security)
- [Request and Response Format](doc:rest-api-format)
- [Testing PayU APIs](doc:testing-payu-apis)

## Related APIs

- [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
- [Collect Payment API — S2S](ref:_payment_server_to_server)
- [Payment Consent Transaction](ref:payment-consent-transaction-payu-hosted)
