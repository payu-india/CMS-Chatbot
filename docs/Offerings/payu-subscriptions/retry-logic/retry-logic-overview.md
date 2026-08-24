---
title: Retry Logic Overview
excerpt: >-
  When and how to retry failed pre-debit notifications, recurring debits, and
  mandate registration across API and Zion integrations.
deprecated: false
hidden: false
metadata:
  title: PayU Subscription Retry Logic
  description: >-
    Payment retry rules for PayU subscriptions including pre-debit retries,
    recurring debit retries, and Zion automatic retry behavior.
  robots: index
---
## Purpose

Clarify **when retries are appropriate**, **when they are dangerous**, and how Zion handles retries automatically — reducing duplicate charges and support escalations.

## When to use this

Use this page when:

* A pre-debit or recurring debit returns `status=0` or an error code
* You are designing scheduler/retry logic in your billing system
* You need to distinguish merchant retry vs Zion automatic retry

## Prerequisites

* [Billing Lifecycle Overview](doc:billing-lifecycle-overview)
* [First Successful Subscription](doc:first-successful-subscription)

## Workflow

```
Failure → Classify (transient vs terminal) → Retry or stop → Verify final status
```

## Retry rules by phase

| Phase | Retry? | Guidance |
| ----- | ------ | -------- |
| **Consent / registration** | Yes, with new attempt | Customer may need different payment method if bank rejected (`E4278`) |
| **Pre-debit (Cards/UPI)** | Yes if `status=0` | Wait briefly; retry pre-debit API. Do not proceed to debit until `status=1` |
| **Recurring debit** | **Conditional** | Never retry on `E4682` (in progress) or `E4683` (already completed). See [Cards and UPI Retry Behavior](doc:cards-and-upi-retry-behavior) |
| **Zion invoices** | Automatic | Zion retries failed invoice payments for up to 3 days — see [Zion Automatic Retries](doc:zion-automatic-retries) |

## Implementation

### Safe retry pattern (API integrations)

1. Capture `requestId`, `authpayuid`, and error code
2. Consult [Error Code Reference](doc:error-code-reference)
3. If transient (e.g., pre-debit `status=0`): retry with exponential backoff
4. If in-progress (`E4682`): poll status/webhook — **do not** send duplicate debit
5. If terminal (revoked mandate, amount mismatch): stop and alert customer

### What not to do

* Send parallel recurring debits for the same billing cycle
* Retry debit immediately after `E4682`
* Assume failure without checking webhook final status

## Verification

* Each retry uses a new request only when prior attempt confirmed failed
* Reconciliation log shows single successful debit per billing period

## Troubleshooting

See phase-specific pages:

* [Cards and UPI Retry Behavior](doc:cards-and-upi-retry-behavior)
* [Net Banking Retry Behavior](doc:net-banking-retry-behavior)
* [Zion Automatic Retries](doc:zion-automatic-retries)

## Related Pages

* [Troubleshooting Guide](doc:troubleshooting-guide)
* [Pre-Debit and Recurring Debit Flow](doc:pre-debit-and-recurring-debit-flow)
* [Recurring Debit Failures](doc:recurring-debit-failures)

## Next Step

[Cards and UPI Retry Behavior](doc:cards-and-upi-retry-behavior)
