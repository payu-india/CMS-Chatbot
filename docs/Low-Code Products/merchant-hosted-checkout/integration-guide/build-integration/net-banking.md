---
title: Net Banking
excerpt: >-
  Post a net banking payment. The parameter table says pg=NB. Test samples use
  pg=TESTPG and bankcode=TESTPGNB.
deprecated: false
hidden: true
metadata:
  title: Net Banking — Merchant Hosted Checkout
  description: >-
    Merchant Hosted net banking: pg, bankcode, test login payu/payu, and the
    getNetBankingStatus health check.
  keywords:
    - payu merchant hosted net banking
    - payu TESTPG TESTPGNB
  robots: index
next:
  description: Explore related information and resources.
---
<!-- VALIDATION NEEDED: The parameter text says pg=NB. Samples use pg=TESTPG and bankcode=TESTPGNB. The steps card says pg=NEFT. Account number and IFSC are not on this page. -->

***

## Prerequisites

Read [Build the Integration](./index). Bank codes are listed in [Net Banking Codes](https://docs.payu.in/docs/net-banking-codes).

***

## Overview of Steps

1. Prepare parameters with `pg` and `bankcode`.
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
    | `pg` | Parameter text says NB | TESTPG |
    | `bankcode` | Bank code. Test sample | TESTPGNB |
    | `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, `furl`, `hash` | Shared fields | |
  </Tab>
  <Tab title="Optional Parameters and Description">
    `address1`, `address2`, `city`, `state`, `country`, `zipcode` (limit 20), `udf1`–`udf5`.
  </Tab>
</Tabs>

<!-- VALIDATION NEEDED: This page's table describes furl as success and surl as failure. -->

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
  The test form posts `pg=TESTPG` and `bankcode=TESTPGNB`. The same form is on the [Quick Start](../../quick-start).
</Accordion>

<Accordion title="Success and Error Response" icon="fa-circle-check">
  Sample: `mode=NB`, `status=success`, `bankcode=TESTPGNB`, `error=E000`, `error_Message=No Error`.
</Accordion>

***

### Step 4: Verify Response via Reverse Hashing

<ReverseHashing />

***

### Step 5: Verify the Payment

<Verify_Payment_Tabs />

You can check whether net banking is up with `getNetBankingStatus`. The request body is not in this folder.

***

## Security

Generate the hash on the server. Do not treat the redirect as the only confirmation.

***

## Next Steps

<Cards columns="2">
  <Card title="Test Integration" href="../test-integration" icon="fa-flask">
    Username `payu`, password `payu`, OTP `123456`.
  </Card>
  <Card title="Net Banking Codes" href="https://docs.payu.in/docs/net-banking-codes" icon="fa-list">
    Production bank codes.
  </Card>
</Cards>
