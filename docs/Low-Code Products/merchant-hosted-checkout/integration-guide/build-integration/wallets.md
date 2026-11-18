---
title: Wallets
excerpt: >-
  Post a wallet payment with pg=CASH. Advantage Club uses pg=RD and
  bankcode=ADVCLUB.
deprecated: false
hidden: true
metadata:
  title: Wallets — Merchant Hosted Checkout
  description: >-
    Merchant Hosted wallets: pg=CASH and a wallet bankcode. Advantage Club uses
    pg=RD and bankcode=ADVCLUB.
  keywords:
    - payu merchant hosted wallets
    - payu pg CASH PAYTM
    - payu advantage club ADVCLUB
  robots: index
next:
  description: Explore related information and resources.
---
`pg=CASH` and the wallet `bankcode` from [Wallet Codes](https://docs.payu.in/docs/wallet-codes). The Paytm sample uses `PAYTM`. Advantage Club uses `pg=RD` and `bankcode=ADVCLUB`.

***

## Prerequisites

Read [Build the Integration](./index).

***

## Overview of Steps

1. Prepare `pg` and `bankcode`.
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
    | `pg` | CASH. Advantage Club is RD | CASH |
    | `bankcode` | Wallet code | PAYTM |
    | `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, `furl`, `hash` | Shared fields | |
  </Tab>
  <Tab title="Optional Parameters and Description">
    <!-- DOCUMENTATION GAP: The wallets page has no separate optional-parameter table. -->
  </Tab>
</Tabs>

<!-- VALIDATION NEEDED: The wallets table swaps surl and furl. The Paytm cURL uses lowercase cash and paytm. The overview says bank codes are case-sensitive. -->

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
  The HTML sample posts `pg=CASH` and `bankcode=PAYTM`. Advantage Club has no test environment. Its sample still shows `pg=RD` and `bankcode=ADVCLUB`.
</Accordion>

<Accordion title="Success and Error Response" icon="fa-circle-check">
  Sample: `mode=CASH`, `PG_TYPE=CASH-PG`, `error=E000`, `error_Message=No Error`.
</Accordion>

***

### Step 4: Verify Response via Reverse Hashing

<ReverseHashing />

***

### Step 5: Verify the Payment

<Verify_Payment_Tabs />

***

## Security

If you use only wallets and UPI, the source still says the website must be secure.

***

## Next Steps

<Cards columns="2">
  <Card title="Test Integration" href="../test-integration" icon="fa-flask">
    Paytm `7777777777` / OTP `888888`.
  </Card>
  <Card title="Wallet Codes" href="https://docs.payu.in/docs/wallet-codes" icon="fa-list">
    Values for `bankcode`.
  </Card>
</Cards>
