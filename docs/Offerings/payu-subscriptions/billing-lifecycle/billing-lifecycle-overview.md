---
title: Billing Lifecycle Overview
excerpt: >-
  End-to-end subscription lifecycle from mandate registration through recurring
  charges, modifications, and cancellation.
deprecated: false
hidden: false
metadata:
  title: PayU Subscription Billing Lifecycle
  description: >-
    Understand the PayU subscription billing lifecycle including mandate
    registration, pre-debit, recurring debits, and mandate management.
  robots: index
next:
  description: Learn how individual charges move through the system.
  pages:
    - slug: charge-lifecycle
      type: basic
      title: Charge Lifecycle
---
## Purpose

Explain how a PayU Subscription moves from initial customer consent through recurring billing and eventual cancellation or completion.

## When to use this

Use this page when you need to:

* Design your billing orchestration logic
* Explain subscription flows to product or support teams
* Determine where webhooks and status APIs fit in your integration

## Prerequisites

* [Quick Start Guide](doc:quick-start-guide) — key concepts
* Payment mode selected

## Workflow

```
Registration → Active mandate → Pre-debit (Cards/UPI) → Recurring debit → Modify / Pause / Cancel / Complete
```

## Subscription lifecycle stages

| Stage | What happens | Your action |
| ----- | ------------ | ----------- |
| **1. Registration** | Customer consents via consent transaction | Call `_payment` with `si_details` |
| **2. Active** | Mandate is live; debits allowed | Store `authpayuid`; schedule billing |
| **3. Pre-debit** (Cards/UPI) | Customer notified before charge | Call Pre-Debit Notification API ≥24h prior |
| **4. Recurring debit** | Funds collected per mandate | Call Recurring Payment Transaction API |
| **5. Management** | Pause, modify, or cancel | Use mandate management APIs per payment mode |
| **6. Terminal** | Revoked, completed, or expired | No further debits; archive mandate reference |

For state definitions, see [Mandate States and Transitions](doc:mandate-states-and-transitions).

## Lifecycle by integration path

| Path | Who orchestrates billing |
| ---- | ------------------------ |
| **API** | Your backend schedules pre-debit and recurring calls |
| **Zion** | Zion generates invoices and executes charges automatically |
| **Dashboard** | You upload CSV files or use payment links for registration and debits |

## Implementation

### API-managed lifecycle

1. **Register** — Consent transaction creates mandate
2. **Schedule** — Your scheduler triggers pre-debit then debit per billing cycle
3. **Reconcile** — Webhooks + Verify Payment API confirm outcomes
4. **Manage** — Modify amount/dates or cancel via mandate APIs

Detailed charge mechanics: [Pre-Debit and Recurring Debit Flow](doc:pre-debit-and-recurring-debit-flow).

### Zion-managed lifecycle

1. **Define subscription** — [Define Subscription API](ref:create-a-subscription)
2. **Consent** — Customer completes payment instrument registration
3. **Automate** — Zion creates invoices per plan schedule, handles pre-debit and retries
4. **Notify** — [Zion webhooks](doc:zion-subscription-webhooks) report invoice and subscription events

## Verification

* Mandate status APIs return **Active** after successful registration
* Each billing cycle produces a traceable transaction ID
* Failed debits surface in [Troubleshooting](doc:troubleshooting-guide) and [Retry Logic](doc:retry-logic-overview)

## Troubleshooting

| Scenario | See |
| -------- | --- |
| Mandate stuck in Pending | [Mandate Registration Failures](doc:mandate-registration-failures) |
| Debit failed mid-cycle | [Recurring Debit Failures](doc:recurring-debit-failures) |
| Customer wants to cancel | [Mandate Management](doc:mandate-management) |

## Related Pages

* [Charge Lifecycle](doc:charge-lifecycle)
* [Mandate States and Transitions](doc:mandate-states-and-transitions)
* [First Successful Subscription](doc:first-successful-subscription)
* [Webhooks and Events](doc:webhooks-and-events)

## Next Step

[Charge Lifecycle](doc:charge-lifecycle) — how a single billing cycle executes.
