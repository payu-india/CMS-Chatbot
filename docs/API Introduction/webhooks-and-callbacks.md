---
title: Webhooks and Callbacks
excerpt: >-
  Understand PayU surl/furl callbacks and webhooks — how to verify payloads,
  handle duplicates, and keep payment status in sync.
deprecated: false
hidden: false
metadata:
  title: PayU Webhooks and Callbacks
  description: >-
    Learn how PayU callbacks (surl/furl) and webhooks work, how to verify
    signatures or reverse hashes, and how to process payment events reliably.
  keywords:
    - PayU webhooks
    - PayU surl furl
    - PayU payment callback
    - PayU webhook verification
    - PayU webhook events
  robots: index
next:
  description: ''
---
PayU notifies your systems in two complementary ways:

1. **Redirect callbacks** — browser returns to your `surl` (success) or `furl` (failure) after checkout.
2. **Webhooks** — server-to-server event notifications for payment, refund, subscription, and other product events.

Use both. Redirects improve UX; webhooks and Verify Payment keep your source of truth accurate.

## Redirect callbacks (`surl` / `furl`)

| Parameter | Purpose |
| :-------- | :------ |
| `surl` | Customer redirect URL after successful payment completion path |
| `furl` | Customer redirect URL after failed payment completion path |

### Callback handling rules

* Accept the posted response on your server.
* Verify **reverse hash** before trusting status.
* Persist the raw callback payload.
* Confirm final status with [Verify Payment](ref:verify_payment_api) when needed.
* Never mark an order paid from client-side JavaScript alone.

Guides:

* [Handling Web Checkout](doc:handling-web-checkout)
* [Handling Mobile SDK Checkout](doc:handling-mobile-sdk-checkout)
* [Generate Hash](doc:hashing-request-and-response) (reverse hashing)

## Webhooks

Webhooks deliver asynchronous events even when the customer does not return to your app.

### Configure webhooks

Use the PayU Dashboard to register endpoints and choose events:

* [Manage Webhooks using Dashboard](doc:manage-webhooks-using-dashboard)

### Product webhook docs

| Product area | Doc |
| :----------- | :-- |
| Refunds | [Webhooks for Refunds](doc:webhooks-for-refunds) |
| Subscriptions / Zion | [Webhooks for Subscription](doc:webhooks-for-subscription) |
| Chargeback | Chargeback webhook docs under [Chargeback](doc:chargeback) |
| Payouts | Payout event docs under Payouts reference/custom blocks |

## Reliable processing pattern

```
Receive event
→ Verify signature / reverse hash
→ Check idempotency key / event id / txn id
→ Update internal state transition safely
→ Return HTTP 2xx quickly
→ Perform heavy work asynchronously if needed
→ Reconcile with Verify/transaction APIs for critical orders
```

### Idempotency

PayU event delivery should be treated as **at-least-once**. Your handler must tolerate duplicates:

* Store processed event IDs or unique payment/refund request IDs.
* Ignore repeated notifications that would re-apply the same state transition.
* Allow valid forward transitions (for example, `pending → success`, `success → refunded`).

### Security

* Use HTTPS endpoints only.
* Validate reverse hash or webhook signature as documented for that product.
* Restrict processing to expected event types.
* Keep raw payloads for audit/troubleshooting.

## When callbacks and webhooks disagree

| Situation | What to do |
| :-------- | :--------- |
| Callback success, webhook pending/delayed | Keep order in confirming state; wait for webhook or verify via API |
| No callback, webhook success | Trust verified server notification + optional Verify Payment |
| Conflicting statuses | Call Verify Payment / transaction details and use server API as source of truth |

## What to read next

* [Common API Workflows](doc:common-api-workflows)
* [API Best Practices](doc:api-best-practices)
* [Error Handling for APIs](doc:error-handling-for-apis)
* [Verify Payment API](ref:verify_payment_api)

## Related APIs

* [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
* [Verify Payment API](ref:verify_payment_api)
* [Check Transaction APIs](ref:check-transaction-apis)
