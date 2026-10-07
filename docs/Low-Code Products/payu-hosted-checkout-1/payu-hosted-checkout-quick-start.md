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

Use PayU Hosted Checkout if you want to:

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

  ```Hash Logic
  key|txnid|amount|productinfo|firstname|email|||||||||||salt
  ```
  ```Example Values
  YOUR_KEY|txn_123456|10.00|TestProduct|Test|test@example.com|||||||||||salt_value
  ```

  <Callout icon="⚠️" theme="warn">
    **Critical Rules**

    Follow these rules to create a correct hash value:

    - Do not change the parameter order
    - Do not skip pipes (|). Even if fields are empty, you must include separators.
    - Keep the empty fields. Fields like `udf1`– `udf5` are optional, but their positions should remain empty even if you are not passing any values.
    - No Extra Spaces or Hidden Characters. They will break the hash.
    - Encode the string using UTF-8 before hashing.
  </Callout>

  <Callout icon="📘" theme="info">
    **Look For:**

    - [ ] Extra spaces: Example `"Test "`
    - [ ] Newline characters
    - [ ] Missing pipes `(|)`
    - [ ] Incorrect order

    These may break the hash.
  </Callout>

  <Accordion title="Step 2.1 Generate SHA-512 Hash using Node " icon="fa-info-circle">
    ```node Node.js
    const crypto = require("crypto");

    const hashString = "YOUR_KEY|txn_123456|10.00|Test Product|Test|test@example.com|||||||||||YOUR_SALT";

    const hash = crypto
      .createHash("sha512")
      .update(hashString, "utf8")
      .digest("hex");

    console.log(hash);
    ```
  </Accordion>

  <Accordion title="Step 2.2 Debug Your Hash (Highly Recommended)" icon="fa-info-circle">
    Before using the hash, print the exact string using the following JS code:

    ```javascript
    console.log(JSON.stringify(hashString));
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 3: Create an HTML File to Accept The Payment" icon="fa-info-circle">
  Now that you have all the parameters and the hash value, the next step is to create an HTML file using the below code.

  ```html
  <!doctype html>
  <html>
    <body onload="document.forms.payu.submit()">
      <form name="payu" method="post" action="https://test.payu.in/_payment">
        
        <input type="hidden" name="key" value="YOUR_KEY" />
        <input type="hidden" name="txnid" value="txn_123456" />
        <input type="hidden" name="amount" value="10.00" />
        <input type="hidden" name="productinfo" value="Test Product" />
        <input type="hidden" name="firstname" value="Test" />
        <input type="hidden" name="email" value="test@example.com" />
        <input type="hidden" name="phone" value="9999999999" />

        <input type="hidden" name="surl" value="https://yourwebsite.com/success" />
        <input type="hidden" name="furl" value="https://yourwebsite.com/failure" />

        <input type="hidden" name="hash" value="GENERATED_HASH" />

        <input type="submit" value="Pay Now" />
      </form>
    </body>
    </html>
  ```

  **Replace:**

  - `YOUR_KEY` with test key.
  - `GENERATED_HASH` with the generated hash.
</Accordion>

<Accordion title="Step 4: Complete the Test Payment" icon="fa-info-circle">
  To complete the test payment:

  1. Open payment.html in your browser
  2. The form will auto-submit to PayU and redirected to a payment page.
  3. Choose any payment method and provide the <a href="https://docs.payu.in/docs/test-cards-upi-id-and-wallets" title="Access Test Credentials">test credentials</a>.
  4. Complete the payment.
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
