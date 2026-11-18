---
title: Build the Integration
excerpt: >-
  Request parameters, hash, HTML form post, reverse hash, and server-side
  verification for Merchant Hosted Checkout.
deprecated: false
hidden: false
next:
  pages: []
metadata:
  title: Build Merchant Hosted Checkout
  description: >-
    Build PayU Merchant Hosted Checkout: parameters, SHA-512 hash, form POST to
    _payment, reverse hash, and Verify Payment. Method pages add pg and bankcode.
  keywords:
    - payu merchant hosted build integration
    - payu _payment form post parameters
    - payu sha512 hash merchant hosted
  robots: index
---
<Banner
  isInline={true}
  message="Integration effort: Developer required"
  color="#FFC107"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

<Callout icon="📘" theme="info">
  ### **Choose a method**

  Every payment adds `pg`, `bankcode`, and sometimes extra fields. Read the shared steps, then open the method page:

  [Cards](./cards) · [Net Banking](./net-banking) · [Wallets](./wallets) · [UPI Collect](./upi-collect) · [PayPal](./paypal) · [Pluxee](./pluxee)
</Callout>

***

## Prerequisites

Go through [What All I Need to Get Started](../../index#what-all-i-need-to-get-started) before you proceed.

***

## Overview of Steps

1. [Prepare payment request parameters](#step-1-prepare-payment-request-parameters), including `pg` and `bankcode` from the method page.
2. [Generate a secure hash](#step-2-generate-secure-hash) on your server.
3. [Post the HTML form](#step-3-post-the-payment-form) to `_payment`.
4. [Verify the response with the reverse hash](#step-4-verify-response-via-reverse-hashing).
5. [Verify the payment](#step-5-verify-the-payment) with `verify_payment`.

***

## Build Integration Steps

Follow these steps for every method. The method page lists the extra fields.

### Step 1: Prepare Payment Request Parameters

These fields appear on every method page. The method page adds `pg`, `bankcode`, and fields such as `ccnum` or `vpa`.

<Tabs>
  <Tab title="Mandatory Parameters and Description">
    | Parameter | Description |
    | --- | --- |
    | `key` | Merchant key provided by PayU. |
    | `txnid` | Unique transaction id you generate. The saved-card text says PayU will not accept a duplicate. |
    | `amount` | Payment amount. |
    | `productinfo` | Product description. |
    | `firstname` | Customer first name. |
    | `email` | Customer email. The source says this helps fraud detection and chargebacks. |
    | `phone` | Customer phone. The source says this helps fraud detection and chargebacks. |
    | `pg` | Payment category. See the method page. |
    | `bankcode` | Network, bank, or wallet code. The overview says bank codes are case-sensitive. |
    | `surl` | Success URL on the cards, UPI Collect, PayPal, and Pluxee pages. |
    | `furl` | Failure URL on those pages. |
    | `hash` | SHA-512 hash from Step 2. |
  </Tab>
  <Tab title="Optional Parameters and Description">
    | Parameter | Description |
    | --- | --- |
    | `address1` | Billing line 1. Source says this helps fraud detection and chargebacks. |
    | `address2` | Billing line 2. |
    | `city` | Billing city. |
    | `state` | Billing state. |
    | `country` | Billing country. |
    | `zipcode` | Billing zip. Several tables set a 20-character limit and say it is mandatory for cardless EMI. |
    | `udf1` – `udf5` | User-defined fields. Empty values still occupy a place in the hash. |
  </Tab>
</Tabs>

<!-- VALIDATION NEEDED: The net banking and wallets tables describe furl as the success URL and surl as the failure URL. -->

***

### Step 2: Generate Secure Hash

<Accordion title="Steps to Generate Hash" icon="fa-key">
  The method pages print this order. Generate it on the server.

  ```text Logic
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
  ```

  <!-- VALIDATION NEEDED: The legacy overview also shows a hash with no UDF fields. The APIs page says some modes can use a different sequence and does not print it. -->

  <HashingSample />
</Accordion>

***

### Step 3: Post the Payment Form

<Accordion title="POST the HTML Form" icon="fa-paper-plane">
  Your server puts the hash in a hidden field. The browser posts the form.

  | Environment | URL |
  | --- | --- |
  | Test | `https://test.payu.in/_payment` |
  | Production | `https://secure.payu.in/_payment` |

  Use `method="post"`. Add the method fields from the method page. A net banking test form is on the [Quick Start](../../quick-start).
</Accordion>

<Accordion title="Success and Error Response" icon="fa-circle-check">
  Success samples include `status=success`, `error=E000`, and `error_Message=No Error`.

  The cards failure sample includes `status=failure`, `unmappedstatus=failed`, `error=E1903`, and `error_Message=Authorization failed at Bank`.
</Accordion>

***

### Step 4: Verify Response via Reverse Hashing

<Callout icon="✅" theme="okay">
  Compare your hash with the `hash` PayU posted before you fulfil the order.
</Callout>

<Accordion title="Reverse Hashing Logic" icon="fa-arrow-rotate-left">
  The UPI Collect page prints this order:

  ```text
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  <ReverseHashing />
</Accordion>

<Callout icon="⚠️" theme="warn">
  A redirect to `surl` is not proof of payment. Verify the hash, then call Verify Payment.
</Callout>

***

### Step 5: Verify the Payment

<Accordion title="Verify Payment" icon="fa-check-double">
  <Verify_Payment_Tabs />
</Accordion>

***

## Security

| Requirement | Where it applies | Why the source says so |
| --- | --- | --- |
| Generate the hash on the server | Step 2 | The salt is a secret known to you and PayU |
| Do not store CVV or the full card number | Your checkout | Integration best practices and the Pluxee page |
| Use HTTPS | Browser and callbacks | Security list |
| Validate the reverse hash on every callback | Step 4 | Hash verification section of the legacy overview |
| Confirm with Verify Payment | Step 5 | Production checklist, if the callback fails |

<Callout icon="⚠️" theme="warn">
  ### **Non-negotiable Rules**

  - Never put the salt in the browser.
  - Never store the CVV.
  - Never fulfil an order from the browser redirect alone.
</Callout>

### PCI-DSS

If you store, process, or transmit cardholder data, the source says you must complete SAQ A-EP. Collecting cards on your site is in that scope.

***

## Next Steps

<Cards columns="2">
  <Card title="Test Integration" href="../test-integration" icon="fa-flask">
    Test values and scenarios before you go live.
  </Card>
  <Card title="Go-Live Checklist" href="../go-live-checklist" icon="fa-list-check">
    Switch the key, salt, and endpoint.
  </Card>
</Cards>
