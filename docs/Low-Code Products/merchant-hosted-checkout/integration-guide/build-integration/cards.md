---
title: Cards
excerpt: >-
  Post a card payment with pg=CC. Includes BIN lookup, saved cards, Alt ID, and
  3DS 2.0.
deprecated: false
hidden: false
next:
  pages: []
metadata:
  title: Cards — Merchant Hosted Checkout
  description: >-
    Merchant Hosted card payments: pg=CC, BIN lookup, saved-card token, guest
    Alt ID, and 3DS 2.0 browser data.
  keywords:
    - payu merchant hosted cards
    - payu pg CC bankcode
    - payu 3ds merchant hosted
  robots: index
---
<Callout icon="⚠️" theme="warn">
  Collecting card data on your site requires PCI-DSS SAQ A-EP. International cards must be enabled by writing to integration@pay.in. Networks named in the source: Visa, Mastercard, American Express, Diners, and RuPay.
</Callout>

`pg=CC`. `bankcode` is network-specific.

<!-- VALIDATION NEEDED: Samples use bankcode CC, MAST, AMEX, VISA, and MASTERCARD. -->

***

## Prerequisites

Read [Build the Integration](./index) for the shared hash, reverse hash, and Verify Payment steps.

***

## Overview of Steps

1. Validate the BIN, then prepare card parameters.
2. Generate the SHA-512 hash on the server.
3. Post the form to `_payment`.
4. Verify the reverse hash.
5. Call `verify_payment`.

***

## Build Integration Steps

### Step 1: Prepare Payment Request Parameters

Call `getBinInfo` first. Test URL: `POST https://test.payu.in/merchant/postservice?form=2`. The prose says `var1=1`, `var2=512345`, `var5=1`. The cURL sends `var1=2`.

<!-- VALIDATION NEEDED: var1 is 1 in the prose and 2 in the sample. -->

<Tabs>
  <Tab title="Mandatory Parameters and Description">
    | Parameter | Description | Example |
    | --- | --- | --- |
    | `pg` | Cards | CC |
    | `bankcode` | Issuing network. See Cards Bank Codes | AMEX |
    | `ccnum` | 13–19 digits. 15 for AMEX. Validate with LUHN | 5123456789012346 |
    | `ccname` | Name on card | Ashish Kumar |
    | `ccvv` | 3 digits, or 4 for AMEX | 123 |
    | `ccexpmon` | Expiry month, MM | 10 |
    | `ccexpyr` | Expiry year, four digits in the table | 2026 |
    | `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, `furl`, `hash` | Shared fields. See [Build the Integration](./index) | |
  </Tab>
  <Tab title="Optional Parameters and Description">
    `lastname`, `address1`, `address2`, `city`, `state`, `country`, `zipcode` (limit 20, mandatory for cardless EMI), `udf1`–`udf5`.

    Saved card: `store_card_token`, `storecard_token_type=1`, `additional_info` with `last4Digits`, `TAVV`, `trid`, and `tokenRefNo`.

    Guest Alt ID: `alt_id` and `additional_info` with `tavv`, `last4Digits`, `par`, and `tokenReferenceId`. Plain guest PAN was not allowed after 31 Oct 2023.

    3DS 2.0: `threeDS2RequestData` with `browserInfo`. The sample also sends `txn_s2s_flow=4`.
  </Tab>
</Tabs>

***

### Step 2: Generate Secure Hash

Same formula as [Build the Integration](./index#step-2-generate-secure-hash):

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
  The HTML sample posts `pg=CC` and `bankcode=MAST`. The cURL sample posts `bankcode=CC`. Copy the full form from the legacy cards page until you pick one `bankcode`.
</Accordion>

<Accordion title="Success and Error Response" icon="fa-circle-check">
  Success: `mode=CC`, `status=success`, `error=E000`, `field7=AUTHPOSITIVE`.

  Failure: `status=failure`, `error=E1903`, `error_Message=Authorization failed at Bank`, `field7=AUTHNEGATIVE`. The sample says `cardhash` is no longer returned.
</Accordion>

***

### Step 4: Verify Response via Reverse Hashing

<ReverseHashing />

`authRefNo` on a guest response holds the AMEX AEVV or the RuPay reference. The source says to ask PayU to enable it.

***

### Step 5: Verify the Payment

<Verify_Payment_Tabs />

***

## Security

Do not store the CVV or the full card number. Card collection on your site is in PCI-DSS scope (SAQ A-EP).

***

## Next Steps

<Cards columns="2">
  <Card title="Test Integration" href="../test-integration" icon="fa-flask">
    EMI test cards are listed there. Plain card test numbers are not in this folder.
  </Card>
  <Card title="Cards bank codes" href="https://docs.payu.in/docs/cards-bank-codes" icon="fa-list">
    Values for `bankcode`.
  </Card>
</Cards>
