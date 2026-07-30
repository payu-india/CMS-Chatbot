---
title: API Architecture
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU APIs are organized by **developer workflow and product capability**, not as a single monolithic REST surface. Understanding this architecture helps you pick the correct base URL, authentication model, request shape, and reference collection.

## Architectural overview

PayU’s API surface has four common patterns:

| Pattern                        | Description                                                | Examples                                                  |
| :----------------------------- | :--------------------------------------------------------- | :-------------------------------------------------------- |
| **Payment initiation APIs**    | Create a payment or consent transaction                    | `_payment` (hosted, merchant-hosted, S2S), Payment Links  |
| **Command-based General APIs** | Server-to-server operations using `command` + `var1…var15` | Verify Payment, Refund, BIN Info, and transaction details |
| **OAuth resource APIs**        | Bearer/OAuth token against product hosts                   | Payouts and Partner onboarding                            |
| **Product-specific REST APIs** | Dedicated hosts and schemas per product                    | BBPS, Chargeback, Zion, Cross-border, and V2 payments     |

## Collect Payment APIs (`_payment`)

Collect Payment APIs initiate customer payments.

| Integration style        | Who hosts checkout UI  | Reference entry                                           |
| :----------------------- | :--------------------- | :-------------------------------------------------------- |
| PayU Hosted Checkout     | PayU                   | [PayU Hosted Checkout](ref:_payment_payu_hosted_checkout) |
| Merchant Hosted Checkout | Merchant               | [Merchant Hosted Checkout](ref:_payment_merchant_hosted)  |
| Server-to-Server         | Merchant orchestration | [S2S Collect Payment](ref:_payment_server_to_server)      |

**Typical characteristics**

- Base URL pattern: `https://test.payu.in/_payment` (Test) / `https://secure.payu.in/_payment` (Production)
- Auth: merchant `key` + SHA-512 `hash`
- Request body: form-urlencoded payment parameters (`txnid`, `amount`, `productinfo`, `surl`, `furl`, and more)
- Outcome: redirect, callback, and/or S2S response depending on flow

## General APIs

General APIs are server-to-server calls used **after** or **around** a payment — verification, refunds, BIN checks, EMI eligibility, health checks, and similar operations.

**Typical characteristics**

- Base URL: `https://test.payu.in/merchant/postservice.php?form=2` (Test) / `https://info.payu.in/merchant/postservice.php?form=2` (Production)
- Auth: `key` + `hash` where hash is usually `sha512(key|command|var1|salt)`
- Request shape: `key`, `command`, `hash`, `var1`…`var15`
- Response shape: commonly includes `status`, `msg`, and command-specific fields such as `transaction_details`

See [REST API Format](doc:rest-api-format) for the shared contract.

## OAuth and partner products

Some PayU products authenticate with OAuth rather than payment-hash logic:

| Product                 | Why OAuth                                                          | Entry points                                                                                                 |
| :---------------------- | :----------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| **Payouts**             | Disbursement APIs need scoped access tokens                        | [Payouts token API](ref:generate-token-using-merchants-credentials-api)                                      |
| **Partner integration** | Multi-merchant platforms need client credentials / auth code flows | [Partner Get Token](ref:get_token_api), [Partner API introduction](ref:partner-integration-api-introduction) |
| **Merchant onboarding** | KYC and account creation workflows                                 | [Partner Integration — Merchant Onboarding](ref:step-00-authentication)                                      |

## Product API collections in Reference

The [API Reference](ref:introduction-api-reference) groups endpoints by product collection:

- Collect Payment
- General
- Payment Links
- Subscriptions / Recurring
- Zion
- Settlements
- Affordability / Offers
- Tokenization / Save Cards
- Split Settlements
- Payouts
- Partner Integration
- Cross-border Payments
- Pre-Authorize Payment
- Merchant Wallet
- BBPS
- Chargeback
- In-person payments
- Apple Pay, Sodexo, Rewards, Wealth Tech, and related collections

Use [Which API should I use?](doc:which-api-should-i-use) if you need a workflow-based chooser instead of a catalog view.

## Environments and hosts

PayU uses **different hosts per API family**. There is no single global gateway URL for every product.

| Family           | Test host (examples)                           | Production host (examples)                     |
| :--------------- | :--------------------------------------------- | :--------------------------------------------- |
| Collect Payment  | `test.payu.in/_payment`                        | `secure.payu.in/_payment`                      |
| General APIs     | `test.payu.in/merchant/postservice.php?form=2` | `info.payu.in/merchant/postservice.php?form=2` |
| v2 Payments      | `apitest.payu.in/v2/payments`                  | `api.payu.in/v2/payments`                      |
| Accounts / OAuth | `uat-accounts.payu.in`                         | `accounts.payu.in`                             |
| BBPS             | `bbps-sb.payu.in`                              | Provided by PayU for production access         |

Full map: [API Environments and Base URLs](doc:api-environments-and-base-urls).

## Versioning model

PayU versioning is **capability-driven**:

- Many Collect Payment enhancements are selected with an `api_version` request parameter.
- Some products expose path versions such as `/v2/payments`.
- Hash formulas can change when optional fields or versions are introduced.

Details: [API Versioning](doc:api-versioning).
