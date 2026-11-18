---
title: Errors and Troubleshooting
excerpt: >-
  Incorrect hash, a callback that does not arrive, reverse hash mismatch, and
  the bank decline named in the Merchant Hosted source.
deprecated: false
hidden: false
next:
  pages: []
metadata:
  title: Merchant Hosted Checkout Errors and Troubleshooting
  description: >-
    Fix PayU Merchant Hosted Checkout issues: incorrect hash, wrong key or salt,
    a missing callback, reverse hash mismatch, and E1903.
  keywords:
    - payu merchant hosted errors
    - payu incorrect hash
    - payu E1903 authorization failed
  robots: index
---

Diagnose issues using the symptoms the Merchant Hosted pages name.

***

<Accordion title="Invalid Hash" icon="fa-key">
  The legacy overview calls this an incorrect hash and says to check the parameter order.

  **What the source tells you to check:**

  - Field order is `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT`
  - The key and salt match test or production

  <!-- VALIDATION NEEDED: A second sample on the legacy overview omits the UDF fields. -->

  **Recommended Fix:**

  - Rebuild the string in the method-page order.
  - Generate the hash on the server.
</Accordion>

<Accordion title="Payment Request Not Accepted" icon="fa-display">
  The legacy overview's matching symptoms are invalid credentials and a payment method that is not enabled.

  **What the source tells you to check:**

  - The key and salt belong to the environment you are calling.
  - The method is enabled on the PayU merchant account.
  - The form posts to `https://test.payu.in/_payment` or `https://secure.payu.in/_payment`.

  <!-- DOCUMENTATION GAP: Merchant Hosted Checkout does not load a PayU page for the customer to choose a method. A blank PayU page is not described here. -->
</Accordion>

<Accordion title="Callback Not Triggered (surl / furl)" icon="fa-link-slash">
  The production checklist says to confirm the transaction on the server if the callback fails, and to use webhooks.

  **Recommended Fix:**

  - Call `verify_payment` with the `txnid`.
  - Use webhooks when the browser redirect does not arrive.

  <!-- DOCUMENTATION GAP: Causes such as localhost or HTTP are not listed in this folder. -->
</Accordion>

<Accordion title="Reverse Hash Mismatch" icon="fa-shield-halved">
  Recreate the response hash and compare it with the hash PayU sent.

  ```text
  SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key
  ```
</Accordion>

<Accordion title="Duplicate Order Processing" icon="fa-clone">
  The saved-card text says PayU will not accept a duplicate transaction id. Use a new `txnid` for another attempt.

  <!-- DOCUMENTATION GAP: No error code for a duplicate txnid is in this folder. -->
</Accordion>

<Accordion title="Amount Mismatch" icon="fa-receipt">
  <!-- DOCUMENTATION GAP: An amount-mismatch error is not described. Success and failure samples do include amount. -->
</Accordion>

<Accordion title="Bank declined the card (E1903)" icon="fa-xmark">
  The cards failure sample contains `error=E1903`, `error_Message=Authorization failed at Bank`, `status=failure`, and `field7=AUTHNEGATIVE`.

  Success samples use `error=E000` and `error_Message=No Error`.
</Accordion>

***

## Still Having Issues?

The legacy overview says to check webhook logs when webhook processing fails. See [Webhooks](https://docs.payu.in/docs/webhooks) and [PayU Support](https://help.payu.in).
