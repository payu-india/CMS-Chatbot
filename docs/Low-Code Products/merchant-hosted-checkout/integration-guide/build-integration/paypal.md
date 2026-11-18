---
title: PayPal
excerpt: >-
  Post a PayPal payment with pg=PAYPAL and bankcode=PAYPAL. Activate PayPal on
  the PayU Dashboard first.
deprecated: false
hidden: true
metadata:
  title: PayPal — Merchant Hosted Checkout
  description: >-
    Merchant Hosted PayPal: pg=PAYPAL, bankcode=PAYPAL, INR settlement, and
    refunds from the PayPal balance.
  keywords:
    - payu merchant hosted paypal
    - payu pg PAYPAL
  robots: index
next:
  description: Explore related information and resources.
---
Activate PayPal from the PayU Dashboard before you post `pg=PAYPAL` and `bankcode=PAYPAL`. Settlements are in INR. Refunds need a PayPal balance.

<!-- VALIDATION NEEDED: The customer journey describes a PayU-hosted wallet list. The overview table says the PayPal bankcode is N/A. -->

***

## Prerequisites

Read [Build the Integration](./index). Enable PayPal on the Dashboard.

***

## Overview of Steps

1. Prepare `pg=PAYPAL` and `bankcode=PAYPAL`.
2. Generate the hash on the server.
3. Post the form.
4. Verify the reverse hash.
5. Call `verify_payment`.

***

## Build Integration Steps

### Step 1: Prepare Payment Request Parameters

<Tabs>
  <Tab title="Mandatory Parameters and Description">
    | Parameter | Description | Example |
    | --- | --- | --- |
    | `pg` | PayPal | PAYPAL |
    | `bankcode` | PayPal | PAYPAL |
    | `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, `furl`, `hash` | Shared fields. `surl` is success and `furl` is failure on this page | |
  </Tab>
  <Tab title="Optional Parameters and Description">
    `address1`, `address2`, `city`, `state`, `country`, `zipcode`, `udf1`–`udf5`.
  </Tab>
</Tabs>

<!-- DOCUMENTATION GAP: No HTML form sample is in the PayPal page. -->

***

### Step 2: Generate Secure Hash

```text
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

***

### Step 3: Post the Payment Form

| Environment | URL |
| --- | --- |
| Test | `https://test.payu.in/_payment` |
| Production | `https://secure.payu.in/_payment` |

<Accordion title="POST the HTML Form" icon="fa-paper-plane">
  Post the shared fields with `pg=PAYPAL` and `bankcode=PAYPAL`.
</Accordion>

<Accordion title="Success and Error Response" icon="fa-circle-check">
  Sample: `mode=PAYPAL`, `bankcode=PAYPAL`, `status=success`, `error=E000`, `field4=0.12`, `field5=USD`.
</Accordion>

***

### Step 4: Verify Response via Reverse Hashing

<ReverseHashing />

***

### Step 5: Verify the Payment

<Verify_Payment_Tabs />

Refund from the Dashboard or with `cancel_refund_transaction`. The PayPal account needs sufficient funds.

***

## Security

<!-- DOCUMENTATION GAP: No PayPal test buyer is published in this folder. -->

***

## Next Steps

<Cards columns="2">
  <Card title="Test Integration" href="../test-integration" icon="fa-flask">
    Confirm PayPal is enabled before you test.
  </Card>
  <Card title="APIs" href="../../merchant-hosted-checkout-apis" icon="fa-rectangle-api">
    The PayPal Try-it link points at the wallets API reference.
  </Card>
</Cards>
