---
title: Errors and Troubleshooting
excerpt: Practical error handling and debugging guide for PayU payment integrations.
deprecated: false
hidden: false
metadata:
  title: Errors and Troubleshooting
  description: Practical error handling and debugging guide for PayU Hosted Checkout, Merchant Hosted Checkout, S2S, webhooks, and recurring payment integrations.
  robots: index
next:
  description: ''
---

Use this section to identify, debug, and fix PayU integration errors across Hosted Checkout, Merchant Hosted Checkout, Server-to-Server (S2S), webhooks, and recurring payment flows.

## What are errors in PayU?

Errors in PayU are response indicators returned during payment initiation, authentication, authorization, bank processing, webhook delivery, refund, or recurring-payment processing.

They can be returned in:

* Browser redirect responses to `surl` or `furl`.
* Server-to-server webhooks.
* API responses.
* Transaction status or verification APIs.
* Dashboard transaction details.

## Why errors occur

PayU errors usually fall into these causes:

* **Merchant configuration issues**: invalid merchant key, disabled payment mode, missing S2S access, wrong environment, webhook URL not configured.
* **Request validation issues**: missing mandatory parameters, invalid amount, duplicate `txnid`, invalid `bankcode`, invalid VPA, invalid card details.
* **Hash or security issues**: incorrect hash sequence, wrong salt, response hash mismatch, sending salt in the request, altered response parameters.
* **Customer or issuer declines**: insufficient funds, incorrect OTP/CVV, card blocked, VPA inactive, transaction not permitted by bank.
* **Network or timeout issues**: bank unavailable, PSP timeout, no callback from bank, PayU-to-merchant webhook delivery failure.
* **Recurring or SI issues**: mandate declined, invalid billing dates, amount mismatch, sequence mismatch, mandate timeout.

> **Pro Tip**
>
> Do not rely only on browser redirects to decide order status. Always verify the final status using the payment response hash, webhooks, and Transaction Detail APIs.

## Browse by error category

Use the category below first, then open the relevant detailed guide or product-specific reference.

### Authentication and authorization errors

| Sub-page | Use it for |
| --- | --- |
| [Payment failed or declined](doc:payment-failed-declined) | Customer, issuer, OTP, CVV, 3DS, authorization, and payment-method declines. |
| [Issuer decline errors](doc:payment-errors-issuer-declines) | Issuer/card-network decline codes and customer-bank rejection reasons. |
| [Transaction stage errors](doc:payment-errors-transaction-stages) | Field7/Field8 authentication, authorization, and bank/wallet stage failures. |
| [Collect Payments payment errors](doc:payment-errors-collect-payments) | Collect Payments errors including `AUC*`, `AUTH*`, `3DS_*`, UPI, card, wallet, and bank failures. |

### Hash and security errors

| Sub-page | Use it for |
| --- | --- |
| [Invalid hash errors](doc:invalid-hash) | `E700`, `SECURE_HASH_FAILURE`, request hash mismatch, and response hash validation issues. |

### Validation errors

| Sub-page | Use it for |
| --- | --- |
| [Error codes and messages](doc:error-codes-and-messages) | General validation, API, request, product, QR, payout, KYC, and product-specific errors that are not covered by a specialized deep dive. |
| [Ecommerce plugin payment errors](doc:payment-errors-ecommerce-plugins) | WooCommerce, Wix, Shopmatic, OpenCart, Magento, BigCommerce, and PrestaShop configuration issues. |
| [Alt ID errors](doc:payment-errors-alt-id) | Card number, CVV, expiry, card eligibility, and token/Alt ID provisioning issues. |
| [UPI QR API payment errors](doc:payment-errors-qr-apis) | QR request validation, merchant VPA setup, amount, and transaction ID issues. |

### Payment failures

| Sub-page | Rows categorized | Source docs |
| --- | ---: | --- |
| [Collect Payments payment errors](doc:payment-errors-collect-payments) | 1,673 | Collect Payment Error Codes |
| [Issuer decline errors](doc:payment-errors-issuer-declines) | 55 | Issuer Decline Error Codes |
| [Transaction stage errors](doc:payment-errors-transaction-stages) | 4 | Transaction Stages Field7/Field8 |
| [S2S Link and Pay errors](doc:payment-errors-s2s-link-and-pay) | 0 | S2S Link and Pay Error Codes; overlapping rows are listed under BNPL |
| [Refund payment errors](doc:payment-errors-refunds) | 81 | Refund Initiation Error Codes, Refund Status Error Codes |
| [Payouts and Smart Send errors](doc:payment-errors-payouts) | 17 | Payouts Error Codes, Smart Send Error Codes |
| [BNPL payment errors](doc:payment-errors-bnpl) | 4 | BNPL Error Codes |
| [CheckoutPro SDK payment errors](doc:payment-errors-checkoutpro-sdk) | 2 | CheckoutPro SDK Troubleshooting |
| [KYC and partner payment errors](doc:payment-errors-kyc) | 6 | KYC Errors and Solutions |

### Pending, timeout, and uncertain-status errors

| Sub-page | Use it for |
| --- | --- |
| [Pending transactions](doc:pending-transactions) | `E227`, dropped transactions, delayed bank callbacks, UPI pending states, late responses, and reconciliation. |

### Network and API errors

| Sub-page | Use it for |
| --- | --- |
| [Error codes and messages](doc:error-codes-and-messages) | API validation, routing, merchant configuration, payout, refund, QR, SDK, KYC, and product errors. |
| [S2S Link and Pay errors](doc:payment-errors-s2s-link-and-pay) | S2S Link and Pay enablement and eligibility issues; overlapping BNPL rows are linked from this page. |
| [Payouts and Smart Send errors](doc:payment-errors-payouts) | Payout request, beneficiary, transfer, and Smart Send errors. |
| [Refund payment errors](doc:payment-errors-refunds) | Refund initiation/status errors and refund eligibility issues. |

### Webhook errors

| Sub-page | Use it for |
| --- | --- |
| [Webhook failures](doc:webhook-failures) | Webhook delivery failures, HTTP errors, endpoint content types, firewall/WAF issues, and idempotency. |

### Recurring and SI errors

| Sub-page | Use it for |
| --- | --- |
| [Recurring and SI errors](doc:recurring-si-errors) | Standing Instruction, UPI Autopay, mandate registration, mandate modification, recurring debit, and invoice/subscription lifecycle issues. |

### Cross-category operational guides

| Sub-page | Use it for |
| --- | --- |
| [Debugging playbook](doc:debugging-playbook) | Step-by-step troubleshooting across frontend, backend, PayU, bank, webhook, and reconciliation layers. |
| [Integration best practices](doc:integration-best-practices) | Prevention guidance across hash, validation, retries, idempotency, webhook, and recurring flows. |
| [Sample error responses](doc:sample-error-responses) | Realistic success, failed, invalid hash, and authentication-failure payloads. |
| [Escalation checklist](doc:escalation-checklist) | Details to collect before contacting PayU Support or Integration Team. |
| [Error categories](doc:error-categories) | The taxonomy that this section uses for categorization. |

## Start here

1. Check [Error categories](doc:error-categories) to identify the error class.
2. Use [Error codes and messages](doc:error-codes-and-messages) for code-specific guidance.
3. If the issue is common, use the relevant deep dive:
   * [Invalid hash errors](doc:invalid-hash)
   * [Payment failed or declined](doc:payment-failed-declined)
   * [Pending transactions](doc:pending-transactions)
   * [Webhook failures](doc:webhook-failures)
4. Use the [Debugging playbook](doc:debugging-playbook) to isolate frontend, backend, PayU, bank, or merchant-infrastructure issues.

## Reference docs

* [Error Codes](ref:error-codes)
* [Transaction Stages - Error References on Field7 & Field8](ref:transaction-stages-error-references-field7-field8)
* [Generate Hash for PayU Hosted Checkout](doc:generate-hash-payu-hosted)
* [Generate Hash for Merchant Hosted Checkout](doc:generate-hash-merchant-hosted)
* [Webhooks for Payments](doc:webhooks)
* [Transaction Detail APIs](ref:transaction-detail-apis)

<!-- PAYU_REPO_ERROR_COVERAGE_BEGIN -->

## Repo error coverage

The troubleshooting sub-pages now include categorized tables for every unique error row extracted from explicit error-code and troubleshooting pages in this repository. Total rows categorized: **3480**.

| Target page | Rows categorized |
| --- | ---: |
| `error-codes-and-messages` | 82 |
| `invalid-hash` | 361 |
| `payment-failed-declined + product sub-pages` | 1866 |
| `pending-transactions` | 214 |
| `recurring-si-errors` | 604 |
| `webhook-failures` | 353 |

<!-- PAYU_REPO_ERROR_COVERAGE_END -->
