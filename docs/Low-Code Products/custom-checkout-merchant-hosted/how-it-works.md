---
title: How Merchant Hosted Checkout Works
excerpt: How a Merchant Hosted payment moves from your form to PayU and back
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: How Merchant Hosted Checkout Works | PayU Developer Docs
  description: >-
    Merchant Hosted Checkout flow: browser form POST to PayU _payment, bank authentication, surl or furl redirect, SHA-512 hash, and server-side verify. Read on.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# How Merchant Hosted Checkout Works

You collect payment details on your site and post them to PayU. PayU processes the payment with the bank, then redirects the customer to your site with the result.

## Architecture Overview

The source describes three movements:

1. A form post from the customer's browser sends the payment data to PayU.
2. The payment passes through PayU's secured environment, then to the card ACS or the bank's net banking page when that method needs it.
3. After the bank finishes, PayU redirects the customer to your website.

<Image src="https://files.readme.io/4aeeafdbefc392fa362522d8209dc7268178e104e699b067895a3408ff412c42-merchant_hosted_flow.png" alt="Merchant Hosted Checkout flow from the merchant site through PayU to the bank and back" align="center" />

<Image src="https://files.readme.io/f3853b72839386d63dda5c0929a3d8f82812c794036a97a5e50f3940a6bea27c-merchant_hosted_customer_journey.png" alt="Merchant Hosted Checkout customer journey" align="center" width="250px" />

<Image src="https://files.readme.io/1764f1a919d1e2a65ea7af0227bbb1b649c85cfde4cdbc4b435be8e6fb722fd3-merchant_hosted_acs_page.png" alt="Bank ACS page shown during a Merchant Hosted card payment" align="center" width="300px" border={true} />

## Endpoints

| Purpose | Test | Production |
| --- | --- | --- |
| Collect payment (`_payment`) | `POST https://test.payu.in/_payment` | `POST https://secure.payu.in/_payment` |
| Postservice commands (BIN, as written on the cards page) | `POST https://test.payu.in/merchant/postservice?form=2` | `POST https://info.payu.in/merchant/postservice?form=2` |

<!-- VALIDATION NEEDED: Postservice host and path disagree across the Merchant Hosted source.
- Cards BIN: test `https://test.payu.in/merchant/postservice?form=2`, production `https://info.payu.in/merchant/postservice?form=2`.
- UPI Validate VPA sample: `https://test.payu.in/merchant/postservice?form=2` (no `.php`).
- The APIs page: `POST https://info.payu.in/merchant/postservice.php?form=2` for command APIs, with no separate test URL.
- The shared Verify Payment block uses `postservice.php?form=2` on test.payu.in and info.payu.in.
Confirm which host and whether the path includes `.php`. -->

The go-live checklist in the source also writes the production base as `https://secure.payu.in/` without `_payment`. The method pages include `/_payment`.

## Key Parameters

`pg` and `bankcode` select the payment method on `_payment`. Other fields depend on the method. Use the method page for the set you post.

| Parameter | Role |
| --- | --- |
| `key` | Merchant key from PayU |
| `txnid` | Unique transaction id you generate. The saved-card parameters say PayU will not accept a duplicate txnid |
| `amount` | Payment amount |
| `productinfo` | Short description of the product |
| `firstname`, `email`, `phone` | Customer details. Phone is described as required for fraud checks |
| `pg` | Payment category, for example `CC`, `NB`, `CASH`, `UPI`, `PAYPAL`, `MC` |
| `bankcode` | Method or bank code. The source says values are case-sensitive |
| `surl` | URL PayU redirects to after a successful payment, on the cards, PayPal, and Pluxee pages |
| `furl` | URL PayU redirects to after a failed payment, on those same pages |
| `hash` | SHA-512 of the request fields and the salt |

<!-- VALIDATION NEEDED: The net-banking parameter table and the wallets parameter table describe `furl` as the success URL and `surl` as the failure URL. Their HTML samples, and the cards, PayPal, and Pluxee tables, do the opposite. The UPI Collect table describes them correctly and then swaps the example URLs. -->

## Hash Generation

### Request Hash

The formula on the cards, net banking, wallets, UPI Collect, PayPal, and Pluxee pages is:

```text
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||Salt)
```

Empty `udf` values stay in the string as empty segments. Do not drop the pipes. Generate this on the server. The salt is the secret PayU shared with you.

<HashingSample />

<!-- VALIDATION NEEDED: A second Python sample on the current overview builds `key|txnid|amount|productinfo|firstname|email` followed by ten pipes and then the salt. That is one pipe short of the formula above when every udf is empty (eleven pipes between email and the salt). The APIs page says card and other modes can require an extended or different sequence, and it does not show that sequence. Use the formula in the method-page tables unless PayU confirms another one. -->

### Response Hash Verification

PayU returns a `hash` on the callback. Recreate it and compare. The UPI Collect page and the shared reverse-hash block write:

```text
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

<ReverseHashing />

<!-- DOCUMENTATION GAP: The Merchant Hosted source states the reverse-hash formula and does not include a Node.js, PHP, or Python implementation. Do not invent one. The request-hash samples in Hashing Sample are not the reverse hash. -->

### Postservice Hash

Command APIs on the postservice URL use the formula on the current APIs page:

```text
sha512(key|command|var1|SALT)
```

The shared Verify Payment block writes the same sequence as `sha512(key|command|var1|salt)`.

## Payment Flow — Step by Step

<Accordion title="1. Collect the payment details on your page" icon="fa-circle-1">
  The customer chooses a method and enters the fields that method needs. Card number and CVV are entered on your page for cards and Pluxee. UPI Collect needs a VPA. Net banking needs the bank code.
</Accordion>

<Accordion title="2. Hash the request on your server" icon="fa-circle-2">
  Your server builds the request hash and returns it to the page that will submit the form. The browser posts the hash. It does not calculate it.
</Accordion>

<Accordion title="3. Browser form POST to _payment" icon="fa-circle-3">
  The page posts `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `pg`, `bankcode`, `surl`, `furl`, `hash`, and the method fields to the test or production `_payment` URL.
</Accordion>

<Accordion title="4. PayU and the bank authenticate" icon="fa-circle-4">
  The customer passes through PayU. For cards, the source journey continues to the bank ACS, where the customer enters the OTP.
</Accordion>

<Accordion title="5. PayU redirects to surl or furl" icon="fa-circle-5">
  PayU posts the result to your success or failure URL. Read `status`, `unmappedstatus`, `mihpayid`, `txnid`, `error`, and `error_Message`.
</Accordion>

<Accordion title="6. Check the reverse hash" icon="fa-circle-6">
  Compare your hash with the `hash` in the callback before you accept the result.
</Accordion>

<Accordion title="7. Verify on the server" icon="fa-circle-7">
  Call Verify Payment. The source says to do this when the callback fails, and the method pages say to verify the payment and monitor with webhooks.
</Accordion>

## PCI-DSS Scope

If you store, process, or transmit cardholder data, the source says you must comply with PCI-DSS. It names the Self-Assessment Questionnaire A-EP and the Attestation of Compliance. It also says that Merchant Hosted Checkout collects card details on your website, so you must be PCI-DSS compliant.

Do not store the CVV. Do not store the full card number on your servers. For Pluxee, the source says you are not allowed to store the complete card number, expiry, or CVV even when the customer agrees to save the card. Use `save_sodexo_card` and the `sourceId` PayU returns instead.

If you only use UPI and wallets, the source does not repeat the SAQ A-EP instruction. It says to keep the website secure.

International card transactions need to be enabled by writing to the PayU Integration Team at integration@pay.in. That address is the one printed on the cards page.

## When to Use Merchant Hosted Checkout vs Alternatives

<!-- DOCUMENTATION GAP: The Merchant Hosted source folder has no product-comparison table. The only distinction it draws is that this product is not the prebuilt PayU payment page and not a generic "host the fields yourself" pattern. Do not add Checkout Plus, Payment Links, or SDK recommendations from other guides. -->

## Key Concepts

| Term | What the source uses it for |
| --- | --- |
| `key` | Your merchant identifier from PayU |
| `salt` | Secret known to you and PayU, appended when the hash is calculated |
| `txnid` | Your reference for the order. It must be unique |
| `pg` | Payment category posted on `_payment` |
| `bankcode` | The specific option inside that category. Case-sensitive |
| `surl` / `furl` | Your success URL and failure URL. See the validation note above |
| `hash` | SHA-512 signature on the request and on the response |
| `mihpayid` | PayU's id for the payment, returned on the callback |
| `status` | Callback result such as `success` or `failure` in the samples |
| `unmappedstatus` | Finer status in the samples, such as `captured` or `failed` |
| `error` | `E000` with "No Error" on the success samples. `E1903` with "Authorization failed at Bank" on the cards failure sample |
