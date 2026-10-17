---
title: Common API Workflows
excerpt: >-
  Workflow-centric guide to the most common PayU API journeys — create payment,
  verify status, handle callbacks, refund, and reconcile transactions.
deprecated: false
hidden: false
metadata:
  title: Common PayU API Workflows
  description: >-
    Learn common PayU API workflows for creating payments, checking status,
    handling callbacks and webhooks, issuing refunds, and reconciling
    transactions.
  keywords:
    - PayU API workflows
    - PayU payment workflow
    - PayU verify payment workflow
    - PayU refund workflow
    - PayU webhook workflow
  robots: index
next:
  description: ''
---
PayU integrations are easiest when you build around **workflows**, not isolated endpoints. This page maps the most common developer journeys to the APIs and docs you need.

## Workflow 1 — Make your first payment

```
Create payment (_payment / Payment Link)
→ Customer completes payment
→ Receive surl/furl callback
→ Verify Payment
→ Fulfill order
```

| Step | Action | Docs / APIs |
| :--- | :----- | :---------- |
| 1 | Create payment request with unique `txnid` | [Collect Payment](ref:_payment_payu_hosted_checkout), [Payment Links](ref:create-payment-links) |
| 2 | Customer pays using Test instruments in Test env | [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) |
| 3 | Handle return URLs | [Handling Web Checkout](doc:handling-web-checkout) |
| 4 | Confirm status server-to-server | [Verify Payment](ref:verify_payment_api) |

## Workflow 2 — Authenticate requests

```
Load key + salt (or OAuth credentials)
→ Build hash or fetch token
→ Attach auth to request
→ Call PayU
```

| API family | Auth step |
| :--------- | :-------- |
| Collect Payment / General | Generate SHA-512 hash | 
| Payouts / Partner | Generate OAuth access token |

See [API Authentication and Security](doc:api-authentication-and-security).

## Workflow 3 — Check payment status

```
Receive uncertain status (timeout, pending, callback mismatch)
→ Call Verify Payment / get transaction details
→ Update order from server response
```

Use cases:

* Customer closed the browser before redirect
* Callback delayed or duplicated
* You need a reconciliation job

APIs:

* [Verify Payment](ref:verify_payment_api)
* [Check Transaction APIs](ref:check-transaction-apis)

## Workflow 4 — Handle callbacks and webhooks

```
PayU sends surl/furl or webhook
→ Verify signature / reverse hash
→ Idempotently update payment state
→ Acknowledge receipt
→ Optionally re-verify via API
```

See [Webhooks and Callbacks](doc:webhooks-and-callbacks).

Product webhook examples:

* [Webhooks for Refunds](doc:webhooks-for-refunds)
* [Webhooks for Subscriptions](doc:webhooks-for-subscription)
* Dashboard configuration under [Manage Webhooks](doc:manage-webhooks-using-dashboard)

## Workflow 5 — Refund a payment

```
Identify successful payment (mihpayid / txnid)
→ Call Refund API
→ Store refund request id
→ Track refund state via API or webhook
```

Start with:

* [Introduction to Refunds](doc:introduction-refunds)
* [APIs used in Refunds integration](doc:apis-used-in-refunds-integration)

## Workflow 6 — Reconcile transactions

```
Fetch transactions for a time range / settlement
→ Match against orders in your system
→ Flag missing callbacks or state mismatches
→ Repair state using Verify / transaction detail APIs
```

Helpful APIs and products:

* Transaction detail / check transaction General APIs
* [Settlement APIs](https://docs.payu.in/reference/settlement_transaction_details_api)
* Dashboard reports under [PayU Dashboard](doc:payu-dashboard)

## Workflow 7 — Recurring / subscription collection

```
Create consent transaction
→ Customer approves mandate
→ Store subscription/mandate identifiers
→ Execute recurring debit
→ Handle failures, retries, and webhooks
```

Start with [Recurring payments integration](doc:introduction-recurring-payments-integration) and Subscription / Zion API Reference collections.

## Workflow 8 — Marketplace split settlement

```
Onboard child merchants
→ Collect payment with split instructions (or split after)
→ Track child shares
→ Handle refunds against split payments
```

Start with [Split Settlements](doc:split-settlments) and [Split During Transaction](ref:split-during-transaction-using-_payment).

## Workflow 9 — Payouts disbursement

```
Generate OAuth token
→ Create / verify beneficiary
→ Initiate payout
→ Track status via API + webhooks
```

Start with [Introduction to Payouts](doc:introduction-to-payouts) and [Payouts token API](ref:generate-token-using-merchants-credentials-api).

## Recommended sequence for new merchants

1. [Making Your First API Request](doc:making-your-first-api-request)
2. Workflow 1 (Create + verify payment)
3. Workflow 4 (Callbacks/webhooks)
4. Workflow 5 (Refunds)
5. Add product-specific workflows (subscriptions, split, payouts) as needed

## What to read next

* [Error Handling for APIs](doc:error-handling-for-apis)
* [API Best Practices](doc:api-best-practices)
* [API Troubleshooting](doc:api-troubleshooting)
* [API Reference](ref:introduction-api-reference)

## Related APIs

* [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
* [Verify Payment API](ref:verify_payment_api)
* [Create Payment Link API](ref:create-payment-links)
* [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api)
