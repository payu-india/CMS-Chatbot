---
title: Pluxee
excerpt: >-
  Post a Pluxee payment with pg=MC and bankcode=SODEXO. Check the balance
  before you charge a saved card.
deprecated: false
hidden: true
metadata:
  title: Pluxee — Merchant Hosted Checkout
  description: >-
    Merchant Hosted Pluxee: pg=MC, bankcode=SODEXO, check_balance, and
    save_sodexo_card.
  keywords:
    - payu merchant hosted pluxee
    - payu sodexo SODEXO bankcode
  robots: index
next:
  description: Explore related information and resources.
---
`pg=MC` and `bankcode=SODEXO`. Do not store the full PAN, expiry, or CVV, even with consent.

***

## Prerequisites

Read [Build the Integration](./index).

***

## Overview of Steps

1. Prepare Pluxee fields. Call `check_balance` when you charge a saved card.
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
    | `pg` | Meal card | MC |
    | `bankcode` | Pluxee | SODEXO |
    | `ccnum`, `ccname`, `ccvv`, `ccexpmon`, `ccexpyr` | Card fields for a new card | |
    | `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, `furl`, `hash` | Shared fields | |
  </Tab>
  <Tab title="Optional Parameters and Description">
    `save_sodexo_card` is 0 or 1. A repeat payment uses `source_id`. `is_check_balance` is sent only with `source_id`.

    `udf1`–`udf5` on this page include the cross-border notes written there: PAN, date of birth, legal name, and invoice.

    <!-- DOCUMENTATION GAP: The check_balance request body is not in this folder. -->
  </Tab>
</Tabs>

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
  Post `pg=MC` and `bankcode=SODEXO` with the card fields or `source_id`.
</Accordion>

<Accordion title="Success and Error Response" icon="fa-circle-check">
  A success response returns `sourceId` in `field3`. The masked sample PAN `637513XXXXXX9318` is not a published test card.
</Accordion>

***

### Step 4: Verify Response via Reverse Hashing

<ReverseHashing />

***

### Step 5: Verify the Payment

<Verify_Payment_Tabs />

***

## Security

Do not store the full PAN, expiry, or CVV. The source says this even if the customer consents.

***

## Next Steps

<Cards columns="2">
  <Card title="Test Integration" href="../test-integration" icon="fa-flask">
    No Pluxee test card is published in this folder.
  </Card>
  <Card title="Fetch Balance" href="https://docs.payu.in/reference/fetch-balance-api-sodexo" icon="fa-wallet">
    `check_balance` reference.
  </Card>
</Cards>
