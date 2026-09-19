---
title: Troubleshooting Guide
excerpt: >-
  Diagnose and fix subscription integration failures across mandate registration,
  pre-debit, and recurring debit phases.
deprecated: false
hidden: false
metadata:
  title: PayU Subscriptions Troubleshooting
  description: >-
    Troubleshooting guide for PayU subscription and recurring payment errors
    including mandate, pre-debit, and SI transaction failures.
  robots: index
---
## Purpose

Help developers self-resolve subscription failures **without contacting PayU Support** by phase, symptom, and error code.

## When to use this

Use this guide when:

* A consent, pre-debit, or recurring debit fails
* Mandate status is unexpected (Pending, Failed, Revoked)
* You need error code meanings and recovery steps

## Prerequisites

* Error code or symptom from API response or webhook
* `authpayuid`, `requestId`, and transaction timestamps

## Workflow

```
Identify phase → Match error code → Apply fix → Verify via status API or webhook
```

## Troubleshooting by phase

| Phase | Page |
| ----- | ---- |
| Mandate registration | [Mandate Registration Failures](doc:mandate-registration-failures) |
| Pre-debit notification | [Pre-Debit Failures](doc:pre-debit-failures) |
| Recurring debit | [Recurring Debit Failures](doc:recurring-debit-failures) |
| All error codes | [Error Code Reference](doc:error-code-reference) |

## Quick reference — top errors

| Code | Meaning | Fix |
| ---- | ------- | --- |
| `E4530` / `E4531` | Invalid mandate start/end date | Validate `si_details` dates |
| `E4112` | Debit amount does not match mandate | Align amount with billing rule |
| `E4105` | Invalid recurring sequence | Avoid concurrent debits same cycle |
| `E4271` | Customer declined mandate | New mandate required |
| `E4278` | Bank rejected mandate setup | Try another account/instrument |
| `E4682` | Debit already in progress | Poll status; do not retry immediately |
| `E4683` | Debit already completed | Reconcile; treat as duplicate |

Full searchable table: [Error Code Reference](doc:error-code-reference) (migrated from `recurring-and-si-errors.md`).

## Common mistakes

* Retrying recurring debit while `E4682` in progress → duplicate charge risk
* Skipping 24-hour pre-debit window for Cards/UPI
* Not polling mandate status when registration returns pending

## Verification

After applying a fix:

1. Confirm mandate status via appropriate status API
2. Verify transaction via [Verify Payment API](ref:verify-payment-api)
3. Check webhook for final state

## Related Pages

* [Retry Logic](doc:retry-logic-overview)
* [Billing Lifecycle](doc:billing-lifecycle-overview)
* [FAQs](doc:faqs)

## Next Step

Identify your failure phase and open the matching sub-page, or search [Error Code Reference](doc:error-code-reference).
