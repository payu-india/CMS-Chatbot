---
title: Errors and Troubleshooting
excerpt: The error codes and failure cases the Merchant Hosted source actually names
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Errors and Troubleshooting — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Merchant Hosted Checkout errors from the source. E000 means no error. E1903
    is authorization failed at the bank. Hash and callback checks are included.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Errors and Troubleshooting

Only codes and causes that appear in the Merchant Hosted source are listed here.

## Quick Reference

| Code or symptom | Meaning in the source | What the source says to do |
| --- | --- | --- |
| `E000` | `error_Message` is "No Error" on the success samples | The samples pair this with `status=success` |
| `E1903` | "Authorization failed at Bank" on the cards failure sample | `status=failure`, `unmappedstatus=failed`, `field7=AUTHNEGATIVE`, `field9=Authorization failed at Bank` |
| Incorrect hash | The overview troubleshooting list | Recheck hash generation and parameter order |
| Invalid API credentials | The overview troubleshooting list | Use the key and salt for the environment you are calling |
| Payment method not enabled | The overview troubleshooting list | Enable the method on the PayU merchant account |
| Webhook issues | The overview troubleshooting list | Check webhook logs |

## Hash Errors

<Accordion title="Incorrect hash" icon="fa-shield-halved">
  The overview says to recheck the hash logic and the parameter order. The order on the method pages is:

  ```text
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||Salt)
  ```

  <!-- VALIDATION NEEDED: The overview also has a Python sample with fewer pipes between email and the salt. A mismatch can come from using that shorter string. -->
</Accordion>

<!-- DOCUMENTATION GAP: "Hash is empty" is not described in this folder. E501 is not in this folder and is not listed. -->

## Parameter Errors

<Accordion title="Missing mandatory parameters" icon="fa-table">
  Each method page lists its mandatory fields. The source does not say which error code a missing field returns.

  <!-- DOCUMENTATION GAP: No per-field error codes for missing parameters. -->
</Accordion>

<Accordion title="Duplicate txnid" icon="fa-copy">
  The saved-card parameters say PayU will not accept a duplicate transaction id.

  <!-- DOCUMENTATION GAP: No error code or response sample for a duplicate txnid. -->
</Accordion>

<Accordion title="Wrong pg or bankcode" icon="fa-credit-card">
  The overview says a payment method that is not enabled will fail, and that `bankcode` is case-sensitive. Several pages disagree on the value itself. See the validation notes on Cards, UPI, PayPal, Net Banking, and EFTNET.

  <!-- DOCUMENTATION GAP: No error code for a wrong bankcode. -->
</Accordion>

## Callback Issues

<Accordion title="Callback not received" icon="fa-link">
  The source says to confirm the status on the server if the callback fails, and to use webhooks.

  <!-- DOCUMENTATION GAP: No list of reasons a surl post would be missing. -->
</Accordion>

<Accordion title="Pending status" icon="fa-clock">
  <!-- DOCUMENTATION GAP: The overview says to test pending transactions. It does not define pending, and it does not include a pending callback. Do not add a "pending is not success" rule that is not in the source. -->
</Accordion>

## Payment Failures

<Accordion title="E1903 — authorization failed at the bank" icon="fa-xmark">
  The cards failure sample:

  - `status=failure`
  - `unmappedstatus=failed`
  - `error=E1903`
  - `error_Message=Authorization failed at Bank`
  - `field7=AUTHNEGATIVE`
  - `field9=Authorization failed at Bank`

  The success sample uses `field7=AUTHPOSITIVE` and `field9=Transaction is Successful`.

  <!-- DOCUMENTATION GAP: The source does not say what message to show the customer for E1903. -->
</Accordion>

<Accordion title="Callback and Verify Payment disagree" icon="fa-triangle-exclamation">
  The source says that if the callback fails, confirm with Verify Payment. It does not show a case where the callback and Verify Payment return different statuses.

  <!-- DOCUMENTATION GAP: No mismatch example. -->
</Accordion>

## Card Response Fields

<Accordion title="field7, cardhash, and authRefNo" icon="fa-credit-card">
  - `field7` is `AUTHPOSITIVE` on the cards success sample and `AUTHNEGATIVE` on the failure sample.
  - The failure sample says `cardhash` is no longer supported in postback params.
  - `authRefNo` is documented for guest checkout. For AMEX it holds the AEVV. For Rupay it holds `rupayAuthRefId`. The source says you must ask PayU to enable `authRefNo` on the response.
</Accordion>
