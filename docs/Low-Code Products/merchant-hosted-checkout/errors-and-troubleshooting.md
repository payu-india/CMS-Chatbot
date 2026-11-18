---
title: Errors and Troubleshooting
excerpt: Error values and callback symptoms documented for Merchant Hosted Checkout
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Merchant Hosted Checkout Errors | PayU Developer Docs
  description: >-
    Merchant Hosted Checkout errors from the source: E000, E1903 authorization failed at bank, incorrect hash, wrong key or salt, and a method that is not enabled.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Errors & Troubleshooting

Only codes and symptoms that appear in the Merchant Hosted source are listed here.

## Quick Reference

| Error or symptom | Meaning in the source | What the source says to do |
| --- | --- | --- |
| E000 | `error_Message` is No Error on the success samples | Treat this with `status=success` only after you verify the response hash and call Verify Payment |
| E1903 | Authorization failed at Bank, on the cards failure sample | The sample shows a failed card payment. See the payment-failures section |
| Incorrect hash | Troubleshooting list: hash parameters are in the wrong order | Check the field order in [How It Works](./how-it-works) |
| Invalid API credentials | Wrong key or salt for test or production | Use the key and salt for the environment you are calling |
| Payment method not enabled | The method is not enabled on the merchant account | Enable it on the PayU account before you retry |
| Webhook issues | Webhook processing errors | Check webhook logs. Event names are not listed in this folder |

<!-- DOCUMENTATION GAP: E501, E002, and an empty-hash error are not in the Merchant Hosted source. They are not added here. -->

## Hash Errors

<Accordion title="Incorrect hash" icon="fa-shield-halved">
  The legacy overview says to check that the hash parameters are in the correct order.

  The method pages use:

  ```
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
  ```

  <!-- VALIDATION NEEDED: A second sample on the legacy overview omits the UDF fields. The APIs page says some modes can use a different sequence and does not print it. -->
</Accordion>

<Accordion title="Hash is empty" icon="fa-shield-halved">
  <!-- DOCUMENTATION GAP: No empty-hash error code or cause is documented in this folder. -->
</Accordion>

## Parameter Errors

<Accordion title="Missing mandatory parameters" icon="fa-table">
  <!-- DOCUMENTATION GAP: The method pages list mandatory fields. They do not say which error each missing field returns. -->
</Accordion>

<Accordion title="Duplicate txnid" icon="fa-copy">
  The saved-card parameter text says PayU will not accept a duplicate transaction id.

  <!-- DOCUMENTATION GAP: No error code or response body for a duplicate txnid is in this folder. -->
</Accordion>

<Accordion title="Wrong pg or bankcode" icon="fa-credit-card">
  The legacy overview says bank codes are case-sensitive. Known conflicts in the source, which are not resolved on this page:

  - Net banking: `NB` in the parameter text, `TESTPG` in samples, `NEFT` on the steps card.
  - PayPal: `bankcode=PAYPAL` on the PayPal page, and N/A on the overview table.
  - Wallets: the parameter table uses `CASH` and `PAYTM`. The Paytm cURL uses `cash` and `paytm`.
  - Cards: samples use `CC`, `MAST`, `AMEX`, `VISA`, and `MASTERCARD`.
</Accordion>

## Callback Issues

<Accordion title="surl not received" icon="fa-link">
  The production checklist says to confirm the transaction on the server if the callback fails, and to use webhooks to hear callbacks. Call `verify_payment`.

  <!-- DOCUMENTATION GAP: The source does not list causes such as timeouts, blocked URLs, or browser closes. -->
</Accordion>

<Accordion title="Pending status at surl" icon="fa-clock">
  <!-- DOCUMENTATION GAP: The test steps say to simulate pending transactions. They do not define the pending status value or say whether you may fulfil the order. -->
</Accordion>

## Payment Failures

<Accordion title="E1903 — authorization failed at bank" icon="fa-xmark">
  The cards failure sample contains:

  - `status=failure`
  - `unmappedstatus=failed`
  - `error=E1903`
  - `error_Message=Authorization failed at Bank`
  - `field7=AUTHNEGATIVE`
  - `field9=Authorization failed at Bank`
  - `bankcode=AMEX`

  The success sample uses `field7=AUTHPOSITIVE` and `field9=Transaction is Successful`.
</Accordion>

<Accordion title="Callback and verify status mismatch" icon="fa-triangle-exclamation">
  The production checklist says to confirm the status on the server if the callback fails. It points to Verify Payment and webhooks.

  <!-- DOCUMENTATION GAP: The source does not say which source wins when the callback status and verify_payment status differ, beyond telling you to confirm on the server. -->
</Accordion>

## Card Response Fields

These fields are in the cards callback samples:

| Field | Value in the source |
| --- | --- |
| field7 | `AUTHPOSITIVE` on the success sample. `AUTHNEGATIVE` on the failure sample |
| field9 | `Transaction is Successful` or `Authorization failed at Bank` |
| cardhash | The failure sample says this field is no longer supported in postback params |
| authRefNo | Present on a guest-checkout response sample. The source says it holds the AMEX AEVV or the RuPay auth reference, and that you ask PayU to enable it |
