---
title: Quick Start Integration - Merchant Hosted Checkout [Cards]
deprecated: false
hidden: true
metadata:
  robots: index
---
## When to Use Merchant Hosted Checkout for Cards

Use this approach if you want to:

- Keep customers on **your** branded checkout while collecting card details
- Control how card fields and order summary appear
- Post card parameters (`pg`, `bankcode`, `ccnum`, and related fields) directly to PayU

Know more about [Merchant Hosted Checkout](doc:merchant-hosted-checkout) and the full [Cards Integration](doc:collect-payments-with-cards-seamless) guide.

<Callout icon="⚠️" theme="warn">
  ### **PCI-DSS Certification**

  Collecting card data on your page increases PCI scope. Generate hash only on your server, never store CVV, and do not log full PAN. Prefer HTTPS everywhere.
</Callout>

***

<Accordion title="What it looks like after integration" icon="far fa-check-to-slot">
  The following sample screens use a fictitious merchant, **Nimbus Mart**, to show a typical Merchant Hosted Cards experience after you integrate.

  ### 1. Card checkout on your website

  Customers stay on **Nimbus Mart** and enter card details next to the order summary. You control this UI; PayU receives the posted payment request.

  ![](https://files.readme.io/885ee54d0bb0b25b9ea1584b6b13cadf03e710a52e326175a8d9246181cd4102-nimbus-mart-card-checkout.png)

  ### 2. Card authentication (OTP / 3-D Secure)

  When the issuer requires authentication, the customer completes OTP or 3-D Secure. Your return URLs must be reachable so PayU can send the customer back after authentication.

  ![](https://files.readme.io/73e4b2dff67dae8877f975da455056e465e964c7e7b90f0f79a6e762968fc15c-nimbus-mart-otp-challenge.png)

  ### 3. Payment success on your website

  After PayU processes the payment, the customer returns to your success page. Mark the order paid only after reverse hash validation and Verify Payment / webhook confirmation.

  ![](https://files.readme.io/414295fecb5baa482d60a4bf9c2906122d08ec89c7c06a0790f4b84e10ab5378-nimbus-mart-payment-success.png)
</Accordion>

***

## Prerequisites

Before you begin with Merchant Hosted Cards integration:

- Create a PayU account.
- Get your merchant key and salt for test and production environment.
- Make sure HTTPS success (`surl`) and failure (`furl`) URLs are reachable from the public internet.
- Ability to generate SHA-512 on the server (not in the browser).
- Make sure you have a unique transaction ID (`txnid`) for each attempt.
- Cards enabled on your MID.

***

## Make your Test Payment

Follow the below steps to make your test card payment:

| **Environment**            | **URL**                                                             |
| :------------------------- | :------------------------------------------------------------------ |
| **Test Environment**       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
| **Production Environment** | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

<Accordion title="Step 1: Prepare Request Parameters" icon="far fa-table-list">
  Define these mandatory parameters for cards. You can also send optional parameters. Refer to the [Cards Integration](doc:collect-payments-with-cards-seamless) guide for the full list.

  ```Mandatory Parameters
  key=YOUR_KEY
  txnid=txn_123456
  amount=10.00
  productinfo=Wireless Earbuds
  firstname=Aarav
  email=aarav@testmail.com
  phone=9999999999
  surl=https://nimbusmart.example.com/success
  furl=https://nimbusmart.example.com/failure
  pg=CC
  bankcode=CC
  ccnum=5123456789012346
  ccname=Aarav Sharma
  ccvv=123
  ccexpmon=12
  ccexpyr=2026
  salt={{salt_value}}
  ```

  | **Parameters**  | **Description**                                                                                                                              | **Example**            |
  | :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
  | **key**         | `string` Merchant key provided by PayU during onboarding.                                                                                    | `JPG****k`             |
  | **txnid**       | `string` Unique reference for this order. Must be unique for every attempt.                                                                  | `txn_123456`           |
  | **amount**      | `string` Amount in INR, up to 2 decimal places, no commas.                                                                                   | `10.00`                |
  | **productinfo** | `string` Short product description.                                                                                                          | `Wireless Earbuds`     |
  | **firstname**   | `string` Customer first name.                                                                                                                | `Aarav`                |
  | **email**       | `string` Customer email.                                                                                                                     | `aarav@testmail.com`   |
  | **phone**       | `string` Customer phone (10-digit).                                                                                                          | `9999999999`           |
  | **surl**        | `string` Success URL after payment.                                                                                                          | Your HTTPS success URL |
  | **furl**        | `string` Failure URL after payment.                                                                                                          | Your HTTPS failure URL |
  | **pg**          | `string` Payment mode for cards.                                                                                                             | `CC`                   |
  | **bankcode**    | `string` Card bank/scheme code as applicable (for example `CC` or `MAST`).                                                                   | `CC`                   |
  | **ccnum**       | `string` Card number (validate with Luhn). Use [test cards](doc:test-cards-upi-id-and-wallets) in sandbox.                                   | `5123456789012346`     |
  | **ccname**      | `string` Name on card.                                                                                                                       | `Aarav Sharma`         |
  | **ccvv**        | `string` CVV / security code. Never store this after the request.                                                                            | `123`                  |
  | **ccexpmon**    | `string` Expiry month (`MM`).                                                                                                                | `12`                   |
  | **ccexpyr**     | `string` Expiry year (`YYYY`).                                                                                                               | `2026`                 |
  | **salt**        | `string` Merchant salt — use only on the server when generating hash (do not put Salt in the browser form as a visible field in production). | From PayU dashboard    |

  <Callout icon="📘" theme="info">
    ### **Tips:**

    - `txnid` must be unique
    - No extra spaces in values
    - In production, collect card fields on HTTPS and post hash from your backend (do not expose Salt in client-side JavaScript)
  </Callout>
</Accordion>

<Accordion title="Step 2: Generate SHA-512 Hash (Critical Step)" icon="far fa-lock-a">
  Hash generation is required to **secure your payment request**. If the hash is incorrect, PayU will reject the transaction with an `Invalid Hash` error.

  Create a hash value by concatenating the following parameters in a specific order:

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
  YOUR_KEY|txn_123456|10.00|Wireless Earbuds|Aarav|aarav@testmail.com|||||||||||salt_value
  ```

  <Callout icon="⚠️" theme="warn">
    ### **Critical Rules**

    - Do not change the parameter order
    - Do not skip pipes (`|`). Even if fields are empty, you must include separators.
    - Keep empty UDF positions (`udf1`–`udf5`) even when unused
    - No extra spaces or hidden characters
    - Encode the string using UTF-8 before hashing
    - Generate hash only on your backend
  </Callout>

  <Callout icon="📘" theme="info">
    ### **Look For:**

    - [ ] Extra spaces: Example `"Aarav "`
    - [ ] Newline characters
    - [ ] Missing pipes `(|)`
    - [ ] Incorrect order

    These may break the hash.
  </Callout>

  <Accordion title="Step 2.1 Generate SHA-512 Hash using Node.js" icon="far fa-lock-hashtag">
    ```node
    const crypto = require("crypto");

    const hashString =
      "YOUR_KEY|txn_123456|10.00|Wireless Earbuds|Aarav|aarav@testmail.com|||||||||||YOUR_SALT";

    const hash = crypto
      .createHash("sha512")
      .update(hashString, "utf8")
      .digest("hex");

    console.log(hash);
    ```
  </Accordion>

  <Accordion title="Step 2.2 Debug Your Hash (Highly Recommended)" icon="far fa-computer-mouse-button-left">
    Before using the hash, print the exact string:

    ```javascript
    console.log(JSON.stringify(hashString));
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 3: Post Payment Request" icon="fa-info-circle">
  Use the sample below as a starting point for a **Nimbus Mart**-style Merchant Hosted card form. In production, prefer rendering the form from your server after computing `hash` server-side (never ship Salt to the browser).

  ```curl
   curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=YOUR_KEY&txnid=EaE4ZO3vU4iPsp&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cc&bankcode=MAST&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=undefined&hash=GENERATED_HASH
  ```

  **Replace:**

  - `YOUR_KEY` with your test key
  - `GENERATED_HASH` with the hash from Step 2
  - `surl` / `furl` with your reachable HTTPS URLs
  - Card values with [PayU test cards](doc:test-cards-upi-id-and-wallets) for sandbox
</Accordion>

<Accordion title="Step 4: Complete the Test Payment" icon="fa-info-circle">
  To complete the test payment:

  1. Serve the checkout HTML from your local or test server (HTTPS recommended)
  2. Submit the card form to PayU test endpoint
  3. Complete OTP / 3-D Secure if prompted, using [test credentials](doc:test-cards-upi-id-and-wallets)
  4. Confirm you land on `surl` or `furl`
  5. Validate reverse hash and call Verify Payment before marking the Nimbus Mart (or your) order as paid
</Accordion>

<Accordion title="Errors and Troubleshooting" icon="fa-info-circle">
  **Invalid Hash**

  - Check parameter order
  - Ensure no extra spaces
  - Use UTF-8 encoding
  - Confirm Salt is correct for the environment

  **Payment not starting / page errors**

  - Verify endpoint URL (`https://test.payu.in/_payment`)
  - Ensure form uses POST
  - Confirm `pg`, `bankcode`, and card fields are present

  **Success page shown but order unpaid**

  - Do not trust browser redirect alone
  - Validate reverse hash and Verify Payment / webhooks

  For the full mode guide, see [Cards Integration](doc:collect-payments-with-cards-seamless).
</Accordion>

***

## What is Next?

After you complete the test payment:

- Handle payment response (reverse hashing)
- Verify transaction status
- Harden PCI handling on your checkout
- Move to production

***

## Next Steps

- [Cards Integration](doc:collect-payments-with-cards-seamless) — full Build / Test / Go-live guide
- [Test the Integration](doc:test-integration)
- [Production Checklist](doc:integration-checklist-merchant-hosted-checkout)
- [Best Practices](doc:best-practices)
