---
title: Errors and Troubleshooting
excerpt: Statuses, handler outcomes, and the errors Checkout Plus actually names
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Checkout Plus Errors and Troubleshooting | PayU Developer Docs
  description: >-
    Checkout Plus handler statuses, response status and unmappedstatus values,
    duplicate transaction IDs, and the errors these product pages do not document.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

## Quick Reference

| What you see | Where it is documented | What the source says to do |
| --- | --- | --- |
| `txnStatus` `FAILED` | `responseHandler` sample | Log a retry message |
| `txnStatus` `CANCEL` | `responseHandler` sample | Log a retry message |
| `catchException` runs | Handlers sample | Log a retry message. No exception list is published. |
| `status` `success` | Response table | Map the order from this status. The table calls `success` a successful transaction. |
| `status` `failure` | Response table | Treat as a failed transaction |
| `status` `pending` | Response table | Treat as a failed transaction. See the validation note below. |
| Duplicate `txnid` | `txnid` description | PayU does not accept a duplicate transaction ID. No error code is given. |
| `error` `E000` and `error_Message` `No Error` | Success response sample | This pair appears on the published success sample only |

<!-- VALIDATION NEEDED: Treating pending as failed is the response-table rule. Confirm it before using it as production logic. Standard PayU guidance elsewhere is to verify pending rather than treat it as final. -->

<!-- DOCUMENTATION GAP: E501, an empty hash, and a bank-declined code are not named in the Checkout Plus pages. They are not listed in this table. -->

## Response Statuses

<Accordion title="txnStatus, status, and unmappedstatus" icon="fa-flag">

The handler sample reads `BOLT.response.txnStatus` and checks `SUCCESS`, `FAILED`, and `CANCEL`.

The response table tells you to map the order from `status`. Documented values are `success`, `failure`, and `pending`.

`unmappedstatus` is PayU's internal status. Documented values are `dropped`, `bounced`, `captured`, `auth`, `failed`, `usercancelled`, and `pending`. Descriptions are deferred to [Payment State Explanations](ref:payment-state-explanations).

<!-- VALIDATION NEEDED: The success sample body contains status: success and unmappedstatus: captured. It does not contain txnStatus. -->

</Accordion>

<Accordion title="mode values" icon="fa-credit-card">

The response table says `mode` is the category the customer used: `CC`, `DC`, `NB`, `CASH`, `EMI`, `CLEMI`, `BNPL`.

<!-- VALIDATION NEEDED: The overview lists Credit Card, Debit Card, Net Banking, UPI, Wallet, EMI, and BNPL. UPI and Wallet are not in the mode list. CASH and CLEMI are not in the overview list. -->

</Accordion>

## Hash Errors

<Accordion title="Hash problems" icon="fa-shield-halved">

`hash` is mandatory on the request, and a `hash` field comes back on the response. The pages link to the merchant-hosted hash guide.

<!-- DOCUMENTATION GAP: No mismatch code, empty-hash case, or fix steps are documented for Checkout Plus. Do not add E501 unless a Checkout Plus source names it. -->

</Accordion>

## Parameter Errors

<Accordion title="Missing mandatory parameters" icon="fa-table">

The integration page marks these as mandatory: `key`, `hash`, `txnid`, `amount`, `firstname`, `email`, `phone`, `productinfo`, `surl`, `furl`.

<!-- DOCUMENTATION GAP: The error returned for each missing field is not documented. -->

</Accordion>

<Accordion title="Duplicate txnid" icon="fa-copy">

A transaction ID can be used once. PayU does not accept a duplicate.

<!-- DOCUMENTATION GAP: The response body for a duplicate txnid is not documented. -->

</Accordion>

## Callback and Handler Issues

<Accordion title="responseHandler and surl or furl" icon="fa-link">

`responseHandler` is how the sample reads the result on the page. `surl` and `furl` are mandatory, and the customer journey says the result page depends on them.

<!-- DOCUMENTATION GAP: Causes for a missing surl callback are not documented. Whether the browser is redirected, the handler is called, or both happen, is not documented. -->

</Accordion>

<Accordion title="Pending status" icon="fa-clock">

Quote the response table when you handle `status`: if status is `failure` or `pending`, treat it as a failed transaction.

<Callout icon="⚠️" theme="warn">

Do not fulfil an order from the browser handler alone. The Checkout Plus API page names [Verify Payment](https://docs.payu.in/reference/verify_payment_api) (`verify_payment`) for reconciliation.

</Callout>

<!-- VALIDATION NEEDED: Pending-as-failed is unresolved. See the note in Quick Reference. -->

</Accordion>

## Payment Failures

<Accordion title="FAILED and CANCEL" icon="fa-xmark">

For both `txnStatus` values, the sample logs `Payment failed. Please try again.` The overview also says the customer can retry inside the modal without starting checkout again.

</Accordion>

<Accordion title="catchException" icon="fa-triangle-exclamation">

The function captures the transaction message for an exception. The sample logs a retry message. No cause list is published.

</Accordion>

<!-- DOCUMENTATION GAP: No case of responseHandler and Verify Payment disagreeing is documented. No bank-declined error code is named on these pages. -->
