---
title: Recurring and SI Errors
excerpt: >-
  Troubleshoot PayU Standing Instruction, UPI Autopay, mandate, and recurring
  debit errors.
deprecated: false
hidden: true
metadata:
  robots: index
---
Recurring and Standing Instruction (SI) errors happen during mandate registration, mandate modification, pre-debit processing, or recurring debit execution.

## Common Recurring and SI Errors

These are some of the common recurring and SI errors.

<Accordion title="My Accordion Title" icon="fa-info-circle">
  Lorem ipsum dolor sit amet, **consectetur adipiscing elit.** Ut enim
  ad minim veniam, quis nostrud exercitation ullamco. Excepteur sint
  occaecat cupidatat non proident!
</Accordion>

| Error code / type | Error message as returned by PayU                                   | Description                                 | Possible cause                                                      | Recommended fix                                                                      |
| ----------------- | ------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `E4530`           | `Mandate request failed as start date is less than current date`    | SI/mandate start date is invalid.           | `startDate` is in the past or timezone conversion changed date.     | Send a valid future/current mandate start date as per API requirements.              |
| `E4531`           | `Mandate request failed as end date is less than start date`        | SI/mandate end date is invalid.             | End date is before start date.                                      | Validate mandate date range before creating mandate.                                 |
| `E4112`           | `Transaction failed as mandate and transaction amount is different` | Debit amount does not match mandate rules.  | Debit exceeds fixed mandate amount or does not follow billing rule. | Align debit amount with mandate amount and billing rule.                             |
| `E4105`           | `Transaction failed due to recurring sequence mismatch`             | Recurring sequence is invalid.              | Wrong sequence number or parallel debit issue.                      | Use the correct recurring sequence and avoid concurrent debits for the same mandate. |
| `E4271`           | `Mandate request declined by the customer`                          | Customer declined the mandate.              | Customer rejected UPI Autopay/SI approval.                          | Ask customer to create a new mandate.                                                |
| `E4272`           | `Transaction declined due to timeout at Issuer/Acquirer end`        | Mandate authentication timed out.           | Issuer/acquirer did not respond.                                    | Keep status pending until verified; retry mandate setup if final status is failed.   |
| `E4278`           | `Transaction failed as mandate setup failed from customer's bank`   | Mandate setup failed at customer bank.      | Bank rejected mandate or account does not support it.               | Ask customer to use another account/payment method.                                  |
| `E4682`           | `Recurrence Payment is in progress`                                 | Recurring debit is already being processed. | Duplicate or parallel recurring request.                            | Do not retry immediately. Wait for final status or webhook.                          |
| `E4683`           | `Recurrence Payment is already completed`                           | Recurring debit was already completed.      | Duplicate debit request for the same cycle.                         | Treat as duplicate and reconcile existing debit.                                     |

## When it occurs

Recurring/SI failures commonly appear when:

* A customer rejects the mandate in the bank or UPI app.
* Mandate dates are invalid.
* Debit amount does not match the mandate rule.
* Multiple recurring debits are sent for the same cycle.
* Issuer, PSP, or customer bank times out during mandate authentication.

## Debugging guide

1. Identify whether the failure happened during mandate setup, mandate modification, or debit execution.
2. Check `authpayuid` or `authPayuId`, `requestId`, `debitDate`, `amount`, billing rule, and billing cycle.
3. Confirm mandate start and end dates in the expected timezone.
4. Confirm the debit amount follows the approved mandate rule.
5. Do not send parallel debits for the same mandate cycle.
6. Treat `in progress` responses as pending until the final webhook/status is available.
7. For customer-declined mandates, ask the customer to create a new mandate.

> **Common Mistake**
>
> Reusing the same recurring request while the first debit is still in progress can create duplicate or sequence-mismatch errors.
