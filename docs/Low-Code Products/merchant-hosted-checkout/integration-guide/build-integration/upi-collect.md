---
title: UPI Collect
excerpt: >-
  Post a UPI Collect payment with pg=UPI, bankcode=UPI, and the customer's VPA.
deprecated: false
hidden: true
metadata:
  title: UPI Collect — Merchant Hosted Checkout
  description: >-
    Merchant Hosted UPI Collect: pg=UPI, bankcode=UPI, vpa, validateVPA, and
    the MCC 6012 and 6211 limit.
  keywords:
    - payu merchant hosted upi collect
    - payu validateVPA
  robots: index
next:
  description: Explore related information and resources.
---
<Callout icon="⚠️" theme="warn">
  UPI Collect is allowed only for MCC 6012 and 6211. Web and Android must use UPI Intent S2S. Seamless form POST does not support Intent. iOS may keep a deeplink and UPI Collect.
</Callout>

***

## Prerequisites

Read [Build the Integration](./index).

***

## Overview of Steps

1. Validate the VPA, then prepare `pg`, `bankcode`, and `vpa`.
2. Generate the hash on the server.
3. Post the form.
4. Verify the reverse hash.
5. Call `verify_payment`.

***

## Build Integration Steps

### Step 1: Prepare Payment Request Parameters

`validateVPA` posts to `https://test.payu.in/merchant/postservice?form=2` with `command=validateVPA` and `var1` set to the VPA. Success: `status=SUCCESS`, `isVPAValid=1`. Invalid: `isVPAValid=0`, `payerAccountName=NA`.

<Tabs>
  <Tab title="Mandatory Parameters and Description">
    | Parameter | Description | Example |
    | --- | --- | --- |
    | `pg` | UPI | UPI |
    | `bankcode` | UPI Collect | UPI |
    | `vpa` | Customer VPA | 9999999999@upi |
    | `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, `furl`, `hash` | Shared fields | |
  </Tab>
  <Tab title="Optional Parameters and Description">
    `address1`, `address2`, `city`, `state`, `country`, `zipcode` (limit 20), `udf1`–`udf5`.
  </Tab>
</Tabs>

<!-- VALIDATION NEEDED: The UPI Collect example URLs are swapped even though the field descriptions are correct. -->

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
  Post `pg=UPI`, `bankcode=UPI`, and `vpa`. The customer approves the collect request in their UPI app.
</Accordion>

<Accordion title="Success and Error Response" icon="fa-circle-check">
  Sample: `mode=UPI`, `PG_TYPE=UPI-PG`, `bankcode=UPI`, `status=success`, `error=E000`.
</Accordion>

***

### Step 4: Verify Response via Reverse Hashing

The UPI Collect page prints this order:

```text
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

<ReverseHashing />

***

### Step 5: Verify the Payment

<Verify_Payment_Tabs />

***

## Security

Test VPAs are `anything@payu` and `9999999999@payu.in`. UPI in-app and UPI Intent are not available in test mode.

***

## Next Steps

<Cards columns="2">
  <Card title="Test Integration" href="../test-integration" icon="fa-flask">
    Test VPAs and the UPI Integration Lab.
  </Card>
  <Card title="UPI handles" href="https://docs.payu.in/docs/upi-handles" icon="fa-list">
    Handles referenced from the legacy page.
  </Card>
</Cards>
