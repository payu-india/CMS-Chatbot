---
title: Mandate States and Transitions
excerpt: >-
  Reference for subscription and mandate states including Active, Pending,
  Paused, Revoked, and how to interpret status API responses.
deprecated: false
hidden: false
metadata:
  title: PayU Mandate States
  description: >-
    Mandate and subscription state definitions for PayU recurring payments
    including Active, Revoked, Pending, Paused, and Failed states.
  robots: index
---
## Purpose

Define mandate and subscription states so you can build correct status handling, customer communications, and retry logic.

## When to use this

Use this page when:

* Polling mandate status APIs after registration or modification
* Handling webhooks that report state changes
* Deciding whether to attempt a recurring debit

## Prerequisites

* Completed [First Successful Subscription](doc:first-successful-subscription) or equivalent registration

## Workflow

```
Pending → Active → (Paused) → Revoked / Completed
         ↘ Failed (registration or debit)
```

## Mandate states

| State | Meaning | Can debit? |
| ----- | ------- | ---------- |
| **Active** | Mandate is live and operational | Yes |
| **Pending** | Awaiting confirmation, setup, or transaction processing | No — poll until terminal state |
| **Success** | Registration or transaction completed successfully | Yes (if mandate active) |
| **Failed** | Registration or transaction failed | No — new mandate required |
| **Paused** | (UPI) Temporarily suspended; no debits until resumed | No |
| **Modification Pending** | Change request in progress at issuer | No — wait for completion |
| **Revoked** | Mandate cancelled; no further debits | No |

<Callout icon="📘" theme="info">
  UPI mandates support **pause** and **resume**. Cards and Net Banking use modify/cancel APIs instead of pause.
</Callout>

## State check APIs

| Payment Mode | API |
| ------------ | --- |
| Cards | [Check Mandate Status for Cards](ref:check-mandate-status-api) |
| Net Banking | [Check Net Banking Mandate Status](ref:net_banking_mandate_status_api) |
| UPI | [Get UPI Mandate Status](ref:get-mandate-status-api-for-upi-only) |
| Zion subscriptions | [Get Subscription Details](ref:get-subscription-details-api) + webhooks |

## Implementation

After every consent transaction:

1. If response is pending, poll status API or wait for webhook
2. Only schedule pre-debit/debit when state = **Active**
3. On **Revoked** or **Failed**, stop billing and prompt customer to re-register

## Verification

* Status API response matches your internal subscription record
* No debit attempted while state = Pending or Paused

## Troubleshooting

| State stuck | Action |
| ----------- | ------ |
| Pending > 30 min | Check webhook; poll status; see [Mandate Registration Failures](doc:mandate-registration-failures) |
| Modification Pending | Wait for issuer; do not send parallel modify requests |
| Paused (UPI) | [Resume](doc:mandate-management) before next debit |

## Related Pages

* [Billing Lifecycle Overview](doc:billing-lifecycle-overview)
* [Mandate Management](doc:mandate-management)
* [Webhooks and Events](doc:webhooks-and-events)

## Next Step

[Pre-Debit and Recurring Debit Flow](doc:pre-debit-and-recurring-debit-flow)
