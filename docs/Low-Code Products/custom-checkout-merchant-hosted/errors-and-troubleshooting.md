---
title: Errors and Troubleshooting
excerpt: Look up the error values this folder documents and the checks for hash, parameters, and callbacks
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Merchant Hosted Checkout Errors and Troubleshooting | PayU Developer Docs
  description: >-
    Troubleshoot PayU Merchant Hosted Checkout. Covers E000, E1903, incorrect hash, missing parameters, callbacks, and UPI Collect limits from the source guides.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Errors & Troubleshooting

Use this page for the error values and failure notes that appear in the Merchant Hosted guides. Codes that are not in those guides are not listed here.

## Quick Reference

| Error or symptom | Where it appears | What the source says |
| --- | --- | --- |
| E000, error_Message `No Error` | Success callbacks for cards, UPI, net banking, wallets, PayPal, and Pluxee | The sample status is `success`. |
| E1903, error_Message `Authorization failed at Bank` | Cards failure sample | `status=failure`, `unmappedstatus=failed`, `field7=AUTHNEGATIVE`, `field9=Authorization failed at Bank`. |
| Incorrect hash | Overview troubleshooting | Check the parameter order in the hash string. |
| Invalid API credentials | Overview troubleshooting | Use the key and salt for the environment you are calling, test or production. |
| Payment method not enabled | Overview troubleshooting | Enable the method on the PayU merchant account. |
| Webhook processing errors | Overview troubleshooting | Check webhook logs. |

## Hash Errors

<Accordion title="Incorrect hash" icon="fa-shield-halved">
  The overview says to check the hash generation logic and the parameter order.

  Request string used on the method pages:

  ```
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||Salt)
  ```

  Response string:

  ```
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  <!-- VALIDATION NEEDED: The overview Authentication section also shows a Python sample with a different pipe count. That sample is not the formula on the method pages. See How It Works. -->

  <!-- DOCUMENTATION GAP: No error code for a hash mismatch is named in this folder. -->
</Accordion>

## Parameter Errors

<Accordion title="Missing mandatory parameters" icon="fa-table">
  Each method page lists its own mandatory fields. Cards require the card fields. UPI Collect requires `vpa`. Pluxee requires the Pluxee card fields unless you pay with `source_id`.

  <!-- DOCUMENTATION GAP: This folder does not name the error code returned when a mandatory parameter is missing. -->
</Accordion>

<Accordion title="Duplicate txnid" icon="fa-copy">
  The saved-card parameters say PayU will not accept a duplicate transaction ID. Generate a new `txnid` for each attempt.

  <!-- DOCUMENTATION GAP: No error code or response body for a duplicate txnid is in this folder. -->
</Accordion>

<Accordion title="Wrong pg or bankcode" icon="fa-credit-card">
  `pg` and `bankcode` are case-sensitive. The overview says to enable the method on the merchant account.

  <!-- VALIDATION NEEDED: Conflicting pg and bankcode values are listed on the overview and on the method pages. Cards samples use CC, MAST, AMEX, VISA, and MASTERCARD. Net banking text says NB and samples post TESTPG / TESTPGNB. Wallet samples post cash / paytm while the table says CASH / PAYTM. -->

  <!-- DOCUMENTATION GAP: No error string for a wrong pg or bankcode is in this folder. -->
</Accordion>

## Callback Issues

<Accordion title="surl not received" icon="fa-link">
  The production checklist says to confirm the transaction on the server if the callback fails, and to use webhooks. See [Verify Payment API](ref:verify_payment_api) and [Webhooks](doc:webhooks).

  <!-- DOCUMENTATION GAP: Causes for a missing surl are not listed in this folder. -->
</Accordion>

<Accordion title="Pending status at surl" icon="fa-clock">
  <!-- DOCUMENTATION GAP: The overview says to test pending transactions. It does not define the pending status value or what to show the customer. -->
</Accordion>

## Payment Failures

<Accordion title="E1903 — authorization failed at bank" icon="fa-xmark">
  The cards failure sample returns:

  | Field | Value |
  | --- | --- |
  | status | failure |
  | unmappedstatus | failed |
  | field7 | AUTHNEGATIVE |
  | field9 | Authorization failed at Bank |
  | error | E1903 |
  | error_Message | Authorization failed at Bank |

  <!-- DOCUMENTATION GAP: The sample does not add customer-facing copy beyond error_Message. -->
</Accordion>

<Accordion title="Callback and verify status mismatch" icon="fa-triangle-exclamation">
  The production checklist says to confirm the transaction on the server when the callback fails, using `verify_payment`.

  <!-- DOCUMENTATION GAP: This folder does not describe a case where the callback status and the verify status disagree, or which one to treat as final beyond that checklist line. -->
</Accordion>

## UPI Collect Rejected

<Accordion title="MCC and channel limits" icon="fa-mobile-screen">
  UPI Collect is allowed only for MCC 6012 and 6211. Web integrations use a UPI Intent deeplink rendered as a QR. Android uses Smart Intent. Seamless form POST does not support Intent on Android and desktop web.

  <!-- DOCUMENTATION GAP: No error code for a Collect request outside those rules is in this folder. -->
</Accordion>

## Card Authentication Fields

<Accordion title="field7 on card callbacks" icon="fa-credit-card">
  The cards success sample sets `field7` to `AUTHPOSITIVE` and `field9` to `Transaction is Successful`. The failure sample sets `field7` to `AUTHNEGATIVE` and `field9` to `Authorization failed at Bank`. `field8` is empty in both samples.
</Accordion>
