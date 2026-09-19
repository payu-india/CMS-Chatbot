---
title: Plans and Mandates
excerpt: Understand Zion plans, API-only mandates, plan lifecycle, and mandate management tasks.
deprecated: false
hidden: false
metadata:
  robots: index
---
## Purpose

Explain **plans** (Zion billing schedules) vs **mandates** (bank payment consent) and how to create, modify, pause, and cancel them.

## When to use this

* Choosing Zion plans vs API-only `si_details`
* Implementing cancel, modify, or pause flows
* Associating multiple billing schedules with one customer

## Content mapping (implementation)

| Page | Source |
| ---- | ------ |
| What Is a Plan? | `using-zion-subscription-automation-platform/understanding-plan.md` |
| Plans vs Without Plans | **New** — synthesize Zion index + API integration index |
| Plan Lifecycle | `understanding-plan.md` + deprecated `_TEST` plan APIs (mark deprecated) |
| Mandate Management | `manage-recurring-payment-for-cards/*`, `manage-recurring-payments-for-net-banking/*`, `api-commands-to-manage-upi-recurring-transaction/*` |

<Callout icon="⚠️" theme="warn">
  **Gap:** Standalone Plan CRUD APIs exist only in deprecated/`_TEST` reference. Confirm with product whether plans are defined only via [Define Subscription API](ref:create-a-subscription).
</Callout>

## Related Pages

* [Zion Subscription Automation](doc:zion-subscription-automation)
* [Mandate States and Transitions](doc:mandate-states-and-transitions)
* [Subscription APIs](doc:subscription-apis)

## Next Step

[What Is a Plan?](doc:what-is-a-plan)
