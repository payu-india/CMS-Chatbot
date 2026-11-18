---
title: Quick Start
excerpt: >-
  Make your first Merchant Hosted Checkout test payment. Get your test
  credentials, generate a hash, and post a net banking payment.
deprecated: false
hidden: false
next:
  pages: []
metadata:
  title: Merchant Hosted Checkout Quick Start
  description: >-
    Make your first PayU Merchant Hosted test payment: test key and salt,
    SHA-512 hash, HTML form post with pg=TESTPG, and verify the result.
  keywords:
    - payu merchant hosted checkout quick start
    - payu custom checkout first test payment
    - payu test net banking payu payu 123456
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

## When to Use Merchant Hosted Checkout

Use Merchant Hosted Checkout if you want to:<br />

- Collect payment details on your own page
- Choose the payment method with `pg` and `bankcode`
- Keep the checkout UI in your site

<Callout icon="📘" theme="info">
  ### **Other Integration Options**

  If you want PayU to host the payment page, use [PayU Hosted Checkout](https://docs.payu.in/docs/payu-hosted-checkout-1). If you need no technical setup, use [Payment Links](https://docs.payu.in/docs/payment-links-dashboard).
</Callout>

***

## What Do I Need Before I Start (Prerequisites)

- A PayU merchant account, and the test key and salt.
- HTTPS success (`surl`) and failure (`furl`) URLs.
- Ability to generate SHA-512 on the server.
- A unique `txnid` for this attempt.

<Callout icon="📘" theme="info">
  ### **Test vs Production Credentials**

  Use the test key and test salt for this payment. The legacy test page says you must only use the test key and salt for a test transaction. Production key and salt come from the Dashboard in Live Mode, under **Payment Gateway → Web Integration → Key Salt Details**.
</Callout>

<KeySaltReference />

***

## Overview of Steps

This quick start posts one net banking test payment:<br />

1. Prepare payment request parameters, including `pg` and `bankcode`
2. Generate a SHA-512 hash on your server
3. POST an HTML form to PayU's test endpoint
4. Handle the response at your `surl` / `furl`
5. Verify the payment on your server

<Callout icon="📘" theme="info">
  ### **Integration Guide**

  Once this test payment works, go to [Build the Integration](./integration-guide/build-integration) for each payment method.
</Callout>

***

## Make Your First Test Payment

| **Environment** | **URL** |
| :------------------------- | :------------------------------------------------------------------ |
| **Test Environment** | [https://test.payu.in/\_payment](https://test.payu.in/_payment) |
| **Production Environment** | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

<Accordion title="Step 1: Prepare Request Parameters" icon="fa-table">
  This quick start uses the net banking test values from the source: `pg=TESTPG` and `bankcode=TESTPGNB`.

  <Tabs>
    <Tab title="Mandatory Parameters">
      ```text Parameters
      key=YOUR_KEY
      txnid=t6svtqtjRdl34W
      amount=10.00
      productinfo=iPhone
      firstname=Ashish
      email=test@gmail.com
      phone=9876543210
      pg=TESTPG
      bankcode=TESTPGNB
      surl=https://yourwebsite.com/success
      furl=https://yourwebsite.com/failure
      hash=GENERATED_ON_YOUR_SERVER
      ```
    </Tab>
    <Tab title="Parameter Description">
      | **Parameters** | **Description** |
      | :------------- | :-------------- |
      | `key` | Merchant key from PayU. |
      | `txnid` | Unique transaction id you generate. |
      | `amount` | Payment amount. The net banking sample uses `10.00`. |
      | `productinfo` | Product description. Sample: `iPhone`. |
      | `firstname` | Customer first name. |
      | `email` | Customer email. |
      | `phone` | Customer phone. |
      | `pg` | `TESTPG` in the net banking test sample. The parameter text also says `NB`. |
      | `bankcode` | `TESTPGNB` in the test sample. |
      | `surl` | Success URL on the cards, UPI, PayPal, and Pluxee pages. |
      | `furl` | Failure URL on those same pages. |
      | `hash` | SHA-512 hash generated on your server. |
    </Tab>
  </Tabs>

  <Callout icon="📘" theme="info">
    ### **Tips:**

    - `txnid` must be unique. The saved-card text says PayU will not accept a duplicate transaction id.
    - Net banking test login: username `payu`, password `payu`, OTP `123456`.
  </Callout>
</Accordion>

<Accordion title="Step 2: Generate SHA-512 Hash (Critical)" icon="fa-key">
  The method pages use this formula. Generate it on the server.

  <Tabs>
    <Tab title="Hash Formula">
      ```text Formula
      sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
      ```
    </Tab>
    <Tab title="Example with values">
      ```text Example Hash String
      sha512(YOUR_KEY|t6svtqtjRdl34W|10.00|iPhone|Ashish|test@gmail.com|||||||||||YOUR_SALT)
      ```
    </Tab>
  </Tabs>

  <!-- VALIDATION NEEDED: A second sample on the legacy overview omits the UDF fields. This quick start follows the formula on the method pages. -->

  <Callout icon="⚠️" theme="warn">
    ### **Critical Rules of Hash Generation**

    - [x] Generate the hash on the server. The salt is not a browser value.
    - [x] Keep the empty UDF positions in the string.
    - [x] Use SHA-512.
  </Callout>

  <Accordion title="Step 2.1 Generate Hash using Other Language Bindings" icon="fa-code">
    <HashingSample />
  </Accordion>
</Accordion>

<Accordion title="Step 3: Create the payment HTML form" icon="fa-paper-plane">
  The form below is the net banking test form from the source. Replace the key and the hash.

  <Tabs>
    <Tab title="Sample Request">
      ```html
      <form action="https://test.payu.in/_payment" method="post">
        <input type="hidden" name="key" value="JP***g" />
        <input type="hidden" name="txnid" value="t6svtqtjRdl34W" />
        <input type="hidden" name="productinfo" value="iPhone" />
        <input type="hidden" name="amount" value="10" />
        <input type="hidden" name="email" value="test@gmail.com" />
        <input type="hidden" name="firstname" value="Ashish" />
        <input type="hidden" name="pg" value="TESTPG" />
        <input type="hidden" name="bankcode" value="TESTPGNB" />
        <input type="hidden" name="surl" value="your own success url" />
        <input type="hidden" name="furl" value="your own failure url" />
        <input type="hidden" name="phone" value="9988776655" />
        <input type="hidden" name="hash" value="GENERATED_HASH" />
        <input type="submit" value="submit" />
      </form>
      ```
    </Tab>
    <Tab title="Sample Response">
      ```text Success Response
      mode=NB
      status=success
      unmappedstatus=captured
      bankcode=TESTPGNB
      error=E000
      error_Message=No Error
      ```
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Step 4: Complete a Test Payment" icon="fa-credit-card">
  Submit the form. On the bank test page, sign in with username `payu`, password `payu`, and OTP `123456`. PayU then redirects to your `surl` or `furl`.
</Accordion>

<Accordion title="Step 5: Verify the response" icon="fa-shield-halved">
  Rebuild the reverse hash and compare it with the `hash` in the response:

  ```text
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  Then call Verify Payment. Do not fulfil the order from the redirect alone.

  <Verify_Payment_Tabs />
</Accordion>

***

## Common First-Time Errors

<Accordion title="Errors and Troubleshooting" icon="fa-triangle-exclamation">
  The legacy overview lists these symptoms:

  - Incorrect hash: the parameters are in the wrong order.
  - Invalid API credentials: the key or salt does not match test or production.
  - Payment method not enabled on the merchant account.

  See [Errors and Troubleshooting](./errors-and-troubleshooting).
</Accordion>

***

## Next Steps

<Cards>
  <Card title="Build the Integration" href="./integration-guide/build-integration">
    Parameters and samples for each payment method.
  </Card>
  <Card title="Test Your Integration" href="./integration-guide/test-integration">
    Test values for net banking, UPI, EMI, and wallets.
  </Card>
</Cards>
