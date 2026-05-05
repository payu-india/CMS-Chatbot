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

<Accordion title="Errors and Fixes" icon="fa-wrench">
 <SearchableTable
  headers={['Error code / type', 'What it means', 'Recommended fix']}
  rows={[
    ['`E4530`', 'SI/mandate start date is invalid.', 'Send a valid future/current mandate start date as per API requirements.'],
    ['`E4531`', 'SI/mandate end date is invalid.', 'Validate mandate date range before creating mandate.'],
    ['`E4112`', 'Debit amount does not match mandate rules.', 'Align debit amount with mandate amount and billing rule.'],
    ['`E4105`', 'Recurring sequence is invalid.', 'Use the correct recurring sequence and avoid concurrent debits for the same mandate.'],
    ['`E4271`', 'Customer declined the mandate.', 'Ask customer to create a new mandate.'],
    ['`E4272`', 'Mandate authentication timed out.', 'Keep status pending until verified; retry mandate setup if final status is failed.'],
    ['`E4278`', 'Mandate setup failed at customer bank.', 'Ask customer to use another account/payment method.'],
    ['`E4682`', 'Recurring debit is already being processed.', 'Do not retry immediately. Wait for final status or webhook.'],
    ['`E4683`', 'Recurring debit was already completed.', 'Treat as duplicate and reconcile existing debit.'],
  ]}
  placeholder="Search errors..."
/>
</Accordion>

## When these Errors Occur

<Accordion title="Error Causes" icon="fa-info-circle">

Recurring/SI failures commonly appear when:

* A customer rejects the mandate in the bank or UPI app.
* Mandate dates are invalid.
* Debit amount does not match the mandate rule.
* Multiple recurring debits are sent for the same cycle.
* Issuer, PSP, or customer bank times out during mandate authentication.

</Accordion>

## Troubleshooting

Now that we know the error causes, let's see how how to troubleshoot.

<Accordion title="Troubleshooting Steps" icon="fa-info-circle">
  1. Identify whether the failure happened during mandate setup, mandate modification, or debit execution.
  2. Check `authpayuid` or `authPayuId`, `requestId`, `debitDate`, `amount`, billing rule, and billing cycle.
  3. Confirm mandate start and end dates in the expected timezone.
  4. Confirm the debit amount follows the approved mandate rule.
  5. Do not send parallel debits for the same mandate cycle.
  6. Treat `in progress` responses as pending until the final webhook/status is available.
  7. For customer-declined mandates, ask the customer to create a new mandate.
</Accordion>

<Callout icon="📘" theme="info">
  **Common Mistake:**

  Reusing the same recurring request while the first debit is still in progress can create duplicate or sequence-mismatch errors.
</Callout>
