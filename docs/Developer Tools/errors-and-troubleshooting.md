---
title: Errors and Troubleshooting
excerpt: >-
  Practical error handling and debugging guide for PayU Hosted Checkout,
  Merchant Hosted Checkout, S2S, webhooks, and recurring payment integrations.
deprecated: false
hidden: true
metadata:
  robots: index
---
This page lets you identify, debug, and fix PayU integration errors across Hosted Checkout, Merchant Hosted Checkout, Server-to-Server (S2S), webhooks, and recurring payment flows.

## What are Errors in PayU?

Errors in PayU are responses returned during payment initiation, authentication, authorization, bank processing, webhook delivery, refund, or recurring-payment processing.

They can be returned in:

* Browser redirect responses to `surl` or `furl`
* Server-to-server webhooks
* API responses
* Hash generation
* Transaction status or verification APIs
* Dashboard transaction details

## Why Errors Occur

PayU errors usually fall into these causes:

<Accordion title="Error Causes" icon="fa-exclamation-triangle">
  Lorem ipsum dolor sit amet, **consectetur adipiscing elit.** Ut enim
  ad minim veniam, quis nostrud exercitation ullamco. Excepteur sint
  occaecat cupidatat non proident!
</Accordion>

* **Merchant configuration issues**: invalid merchant key, disabled payment mode, missing S2S access, wrong environment, webhook URL not configured.
* **Request validation issues**: missing mandatory parameters, invalid amount, duplicate `txnid`, invalid `bankcode`, invalid VPA, invalid card details.
* **Hash or security issues**: incorrect hash sequence, wrong salt, response hash mismatch, sending salt in the request, altered response parameters.
* **Customer or issuer declines**: insufficient funds, incorrect OTP/CVV, card blocked, VPA inactive, transaction not permitted by bank.
* **Network or timeout issues**: bank unavailable, PSP timeout, no callback from bank, PayU-to-merchant webhook delivery failure.
* **Recurring or SI issues**: mandate declined, invalid billing dates, amount mismatch, sequence mismatch, mandate timeout.

## Pages in this section

| Page                                                         | Use it for                                                                         |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| [Error categories](doc:error-categories)                     | Understand the main classes of PayU errors and ownership.                          |
| [Error codes and messages](doc:error-codes-and-messages)     | Look up common PayU error codes, messages, causes, and fixes.                      |
| [Invalid hash errors](doc:invalid-hash-errors)               | Debug `E700`, `SECURE_HASH_FAILURE`, hash mismatch, and response hash issues.      |
| [Payment failed or declined](doc:payment-failed-or-declined) | Debug bank, issuer, UPI, wallet, OTP, CVV, and customer-driven failures.           |
| [Pending transactions](doc:pending-transactions)             | Handle `E227`, delayed bank callbacks, UPI pending states, and reconciliation.     |
| [Webhook failures](doc:webhook-failures)                     | Debug webhook delivery failures, HTTP errors, content types, and idempotency.      |
| [Debugging playbook](doc:debugging-playbook)                 | Follow a step-by-step troubleshooting flow.                                        |
| [Integration best practices](doc:integration-best-practices) | Prevent errors with hash, validation, idempotency, retries, and status handling.   |
| [Sample error responses](doc:sample-error-responses)         | See realistic success, failure, invalid hash, and authentication-failure payloads. |
| [Escalation checklist](doc:escalation-checklist)             | Collect the right details before contacting PayU Support.                          |

## Start here

1. Check [Error categories](doc:error-categories) to identify the error class.
2. Use [Error codes and messages](doc:error-codes-and-messages) for code-specific guidance.
3. If the issue is common, use the relevant deep dive:
   * [Invalid hash errors](doc:invalid-hash-errors)
   * [Payment failed or declined](doc:payment-failed-or-declined)
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
