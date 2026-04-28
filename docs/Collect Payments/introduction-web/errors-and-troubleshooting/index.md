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

## Troubleshooting guides

Use this page as the main hub. Detailed guides are linked below as sub-pages.

| Sub-page | Use it for |
| --- | --- |
| [Error categories](doc:error-categories) | Understand the main classes of PayU errors and ownership. |
| [Error codes and messages](doc:error-codes-and-messages) | Look up common PayU error codes, messages, causes, and fixes. |
| [Invalid hash errors](doc:invalid-hash) | Debug `E700`, `SECURE_HASH_FAILURE`, hash mismatch, and response hash issues. |
| [Payment failed or declined](doc:payment-failed-declined) | Debug bank, issuer, UPI, wallet, OTP, CVV, and customer-driven failures. |
| [Pending transactions](doc:pending-transactions) | Handle `E227`, delayed bank callbacks, UPI pending states, and reconciliation. |
| [Webhook failures](doc:webhook-failures) | Debug webhook delivery failures, HTTP errors, content types, and idempotency. |
| [Recurring and SI errors](doc:recurring-si-errors) | Debug Standing Instruction, UPI Autopay, mandate, and recurring debit failures. |
| [Debugging playbook](doc:debugging-playbook) | Follow a step-by-step troubleshooting flow. |
| [Integration best practices](doc:integration-best-practices) | Prevent errors with hash, validation, idempotency, retries, and status handling. |
| [Sample error responses](doc:sample-error-responses) | See realistic success, failure, invalid hash, and authentication-failure payloads. |
| [Escalation checklist](doc:escalation-checklist) | Collect the right details before contacting PayU Support. |

## Payment failure errors by product

| Product sub-page | Rows categorized | Source docs |
| --- | ---: | --- |
| [Collect Payments payment errors](doc:payment-errors-collect-payments) | 2,389 | Collect Payment Error Codes |
| [Issuer decline errors](doc:payment-errors-issuer-declines) | 55 | Issuer Decline Error Codes |
| [Transaction stage errors](doc:payment-errors-transaction-stages) | 4 | Transaction Stages Field7/Field8 |
| [S2S Link and Pay errors](doc:payment-errors-s2s-link-and-pay) | 4 | S2S Link and Pay Error Codes |
| [Refund payment errors](doc:payment-errors-refunds) | 85 | Refund Initiation Error Codes, Refund Status Error Codes |
| [Payouts and Smart Send errors](doc:payment-errors-payouts) | 17 | Payouts Error Codes, Smart Send Error Codes |
| [Alt ID errors](doc:payment-errors-alt-id) | 9 | Alt ID Error Page |
| [BNPL payment errors](doc:payment-errors-bnpl) | 4 | BNPL Error Codes |
| [UPI QR API payment errors](doc:payment-errors-qr-apis) | 3 | QR API Error Codes |
| [CheckoutPro SDK payment errors](doc:payment-errors-checkoutpro-sdk) | 2 | CheckoutPro SDK Troubleshooting |
| [KYC and partner payment errors](doc:payment-errors-kyc) | 6 | KYC Errors and Solutions |

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

The troubleshooting sub-pages now include categorized tables for every unique error row extracted from explicit error-code and troubleshooting pages in this repository. Total rows categorized: **4192**.

| Target page | Rows categorized |
| --- | ---: |
| `error-codes-and-messages` | 82 |
| `invalid-hash` | 361 |
| `payment-failed-declined + product sub-pages` | 2578 |
| `pending-transactions` | 214 |
| `recurring-si-errors` | 604 |
| `webhook-failures` | 353 |

<!-- PAYU_REPO_ERROR_COVERAGE_END -->
