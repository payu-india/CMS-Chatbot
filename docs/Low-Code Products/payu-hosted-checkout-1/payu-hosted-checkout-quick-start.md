---
title: Quick Start
excerpt: >-
  Make your first PayU Hosted Checkout test payment in minutes. Get your test
  credentials, generate a hash, and run your first transaction.
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: PayU Hosted Checkout Quick Start
  description: >-
    Make your first PayU Hosted Checkout test payment: get test credentials,
    generate SHA-512 hash, create an HTML form, and verify the result.
  keywords:
    - payu hosted checkout quick start
    - payu hosted checkout first test payment
    - payu test credentials india
    - payu sha512 hash generation example
    - payu html form post payment tutorial
    - payu test.payu.in _payment endpoint
    - payu checkout integration getting started
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payu-hosted-checkout-1
      title: PayU Hosted Checkout
      type: basic
    - slug: payu-hosted-checkout-workflow
      title: How PayU Hosted Checkout Works
      type: basic
---
## When to Use PayU Hosted Checkout

Use <Anchor target="_blank" href="https://docs.payu.in/docs/payu-hosted-checkout-1">PayU Hosted Checkout</Anchor> if you want to:

- Accept payments on your website without building a custom payment page
- Go live quickly with minimal development effort
- Let PayU handle payment security, authentication, and PCI compliance

<Callout icon="fad fa-comment-captions" theme="info">
  ### **Other Integration Options**

  If you need complete control over the checkout UI, consider [Merchant Hosted Checkout](../../custom-checkout-merchant-hosted) instead. If you need no technical setup at all, consider [Payment Links](../../introduction-no-code-payments-integration/payment-links-dashboard).
</Callout>

***

## What Do I Need Before I Start (Prerequisites)

- Create a <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signup">PayU account</Anchor>.
- Get your merchant key and salt for test and production environment.
- Make sure https success (surl) and failure (furl) URLs are reachable from the public internet.
- Ability to generate SHA-512 on the server (not recommended in browser).
- Make sure you have the transaction ID created.

<Callout icon="📘" theme="info">
  ### **Test vs Production Credentials**

  Use test credentials (key and salt marked as **Test**) for all sandbox testing. Production credentials are separate and obtained from your PayU Dashboard once your account is live.
</Callout>

***

## Overview of Steps

A complete PayU Hosted Checkout integration has five stages. This quick start walks through all five at a simplified level so you can make your first test payment now:

1. Prepare payment request parameters
2. Generate a SHA-512 hash on your server
3. POST an HTML form to PayU's endpoint
4. Handle the response at your `surl` / `furl`
5. Verify the payment on your server

<Callout icon="fad fa-grip-dots-vertical" theme="success">
  ### **Integration Guide**

  Once your test payment works end-to-end here, go to the full [Build Integration](./integrate/build-integration) guide to build production-ready code. It covers all parameters, hash edge cases, multi-language code samples, and response handling in detail.
</Callout>

***

## Make Your First Test Payment

| **Environment**            | **URL**                                                             |
| :------------------------- | :------------------------------------------------------------------ |
| **Test Environment**       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
| **Production Environment** | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

<Accordion title="Step 1: Prepare Request Parameters" icon="fad fa-table">
  These are the minimum parameters you need. All should be present. Missing any of these will cause the request to fail.

  <Tabs>
    <Tab title="Mandatory Parameters">
      ```text Parameters
      key=YOUR_KEY
      txnid=txn_123456
      amount=10.00
      productinfo=TestProduct
      firstname=Test
      email=test@example.com
      phone=9999999999
      surl=https://yourwebsite.com/success
      furl=https://yourwebsite.com/failure
      salt={{salt_value}}
      ```
    </Tab>

    <Tab title="Parameter Description">
      | **Parameters** | **Description**                                                                                                                                                                                                      |
      | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | `key`          | `string` Merchant key from PayU Dashboard. For example `JPG****.k`                                                                                                                                                   |
      | `txnid`        | `string` Unique transaction ID you generate. For example, `txn_123456`.                                                                                                                                              |
      | `amount`       | `string` The transaction amount in INR. The value should be in the two decimal places format and should be: <ul><li>Numeric</li> <li>Up to 2 decimal places</li> <li>No commas</li></ul>. For example, `10.00`       |
      | `productinfo`  | `string` A brief description of the product. For example, `iPhone`                                                                                                                                                   |
      | `firstname`    | `string` The first name of the customer. For example, `Aarav`                                                                                                                                                        |
      | `email`        | `string` The email address of the customer. For example, `aarav@testmail.com`                                                                                                                                        |
      | `phone`        | `string` The email address of the customer. For example, `aarav@testmail.com`                                                                                                                                        |
      | `surl`         | `string` The success URL to which PayU redirects the user after a successful transaction. <a href="https://test-payment-middleware.payu.in/simulatorResponse" title="Example surl">Success URL Example</a>           |
      | `furl`         | `string` The failure URL to which PayU redirects the user after a failure transaction. For example, <a href="https://test-payment-middleware.payu.in/simulatorResponse" title="Example surl">Success URL Example</a> |
      | `salt`         | `string` The salt provided by PayU during onboarding.                                                                                                                                                                |
    </Tab>
  </Tabs>

  <Callout icon="📘" theme="info">
    ### **Tips:**

    - `txnid` must be unique for every payment attempt.
    - No trailing spaces in any parameter. They will break the hash.
    - `amount` must be consistently formatted: `10.00` not `10` or `₹10`.
  </Callout>
</Accordion>

<Accordion title="Step 2: Generate SHA-512 Hash (Critical)" icon="fad fa-key">
  The hash protects your payment request from tampering. PayU will reject any request with an invalid hash.

  Create a hash value by by concatenating the following parameters in a specific order.

  - `key`
  - `txnid`
  - `amount`
  - `productinfo`
  - `firstname`
  - `email`
  - `salt`

  <Tabs>
    <Tab title="Hash Formula">
      ```text Formula
      sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
      ```
    </Tab>

    <Tab title="Example with values">
      ```text Example Hash String
      sha512(YOUR_KEY|txn_123456|10.00|iPhone|Aarav|aarav@example.com|||||||||||YOUR_SALT)
      ```
    </Tab>

    <Tab title="New Tab">

    </Tab>
  </Tabs>

  <Callout icon="⚠️" theme="warn">
    ### **Critical Rules of Hash Generation**

    **Critical Rules**

    Follow these rules to create a correct hash value:

    - [x] Never generate the hash in the browser or mobile app.
    - [x] Keep all pipe separators (`|`) even if UDF fields are empty.
    - [x] Do not add spaces around the separators.
    - [x] Use UTF-8 encoding before hashing.
    - [x] Use SHA-512 (not SHA-256 or MD5).
  </Callout>

  <Accordion title="Step 2.1 Generate Hash using Other Language Bindings " icon="fad fa-code">
    ```node Node.js
    const crypto = require("crypto");

    const hashString = "YOUR_KEY|txn_123456|10.00|Test Product|Test|test@example.com|||||||||||YOUR_SALT";

    const hash = crypto
      .createHash("sha512")
      .update(hashString, "utf8")
      .digest("hex");

    console.log(hash);
    ```
    ```php
    ?php
        $hashString = "YOUR_KEY|txn_123456|10.00|iPhone|Aarav|aarav@example.com|||||||||||YOUR_SALT";
        $hash = strtolower(hash('sha512', $hashString));
        echo $hash;
        ?>
    ```
    ```python
    import hashlib
        hash_string = "YOUR_KEY|txn_123456|10.00|iPhone|Aarav|aarav@example.com|||||||||||YOUR_SALT"
        hash_value = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
        print(hash_value)
    ```

    For more language examples including Java and C#, see[ Generate Secure Hash](./integrate/build-integration#step-12-generate-secure-hash) in the Build Integration page.
  </Accordion>
</Accordion>

<Accordion title="Step 3: Create the payment HTML form" icon="fad fa-paper-plane">
  Create a file called `payment.html` with the form below, replacing the placeholder values with your test credentials and the hash you generated in Step 2.

  ```html
  <!doctype html>
    <html>
      <body onload="document.forms.payu.submit()">
        <form name="payu" method="post" action="https://test.payu.in/_payment">
          <input type="hidden" name="key"         value="YOUR_KEY" />
          <input type="hidden" name="txnid"       value="txn_123456" />
          <input type="hidden" name="amount"      value="10.00" />
          <input type="hidden" name="productinfo" value="iPhone" />
          <input type="hidden" name="firstname"   value="Aarav" />
          <input type="hidden" name="email"       value="aarav@example.com" />
          <input type="hidden" name="phone"       value="9999999999" />
          <input type="hidden" name="surl"        value="https://test-payment-middleware.payu.in/simulatorResponse" />
          <input type="hidden" name="furl"        value="https://test-payment-middleware.payu.in/simulatorResponse" />
          <input type="hidden" name="hash"        value="GENERATED_HASH" />
          <input type="submit" value="Pay Now" />
        </form>
      </body>
    </html>
  ```

  **Replace:**

  - `YOUR_KEY` with test key.
  - `GENERATED_HASH` with the generated hash.

  Open `payment.html` in your browser. The form auto-submits and redirects you to the PayU checkout page.
</Accordion>

<Accordion title="Step 4: Complete a Test Payment" icon="fad fa-credit-card-front">
  On the PayU test checkout page, select a payment method and use one of the following test credentials:

  <Tabs>
    <Tab title="NetBanking">
      **Username:** `payu` | **Password:** `payu` | **OTP:** `123456`
    </Tab>

    <Tab title="Debit Card">
      | Card Number         | Network    | Expiry | CVV | OTP    |
      | ------------------- | ---------- | ------ | --- | ------ |
      | 5118-7000-0000-0003 | Mastercard | 05/30  | 123 | 123456 |
      | 4594-5380-5063-9999 | VISA       | 05/30  | 123 | 123456 |
    </Tab>

    <Tab title="Credit Card">
      | Card Number      | Network    | Expiry | CVV | OTP    |
      | ---------------- | ---------- | ------ | --- | ------ |
      | 5123456789012346 | Mastercard | 05/30  | 123 | 123456 |
      | 4012001037141112 | VISA       | 05/30  | 123 | 123456 |
    </Tab>

    <Tab title="UPI">
      Use `anything@payu` or `999999999@payu` as the VPA.
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Errors and Troubleshooting" icon="fa-info-circle">
  **Invalid Hash**

  - Check parameter order
  - Ensure no extra spaces
  - Use UTF-8 encoding

  **Payment Page Not Loading**

  - Verify endpoint URL
  - Ensure form uses POST

  Refer to the Erors and Troubleshooting page for more information about errors and fixes.
</Accordion>

***

## What is Next?

After you complete the test payment:

- Handle payment response
- Verify transaction status
- Move to production

***

## Next Steps

Now that you have created your first test payment go to the

- Integration Guide for the detailed steps and different language bindings.
