---
title: BNPL Quick Start Integration
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
<Banner
  isInline={true}
  message="Integration effort: Minimal technical setup required"
  color="#FFC107"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

## When to Use LazyPay

Use LazyPay through PayU if you want to:<br />

- Let customers pay now and settle later through their LazyPay credit line
- Offer a fast checkout where the customer only confirms the payment with an OTP sent to their registered mobile number
- Add BNPL with the same `_payment` API and hash logic you already use for other PayU payment methods

<Callout icon="fad fa-comment-captions" theme="info">
  ### **Other Integration Options**

  - To show customers whether they're eligible for LazyPay before checkout, and to save their LazyPay account for repeat payments, see [BNPL Link and Pay](./bnpl-link-and-pay-merchant-hosted).
  - For the full parameter list, every response scenario and production-ready code, see [BNPL Merchant Hosted Integration](./bnpl-merchant-hosted-integration).
</Callout>

***

## What Do I Need Before I Start (Prerequisites)

- Create a <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signup">PayU account</Anchor>.
- Get your merchant key and salt for the test and production environments.
- Ask your PayU account manager to enable the **BNPL** payment category and **LazyPay** on your merchant account.
- Make sure your HTTPS success (`surl`) and failure (`furl`) URLs are reachable from the public internet.
- Generate the SHA-512 hash on your server, never in the browser or mobile app.
- Collect the customer's 10-digit mobile number. LazyPay uses it to identify the customer and send the OTP.

<Callout icon="📘" theme="info">
  ### **Test vs Production Credentials**

  Use test credentials (key and salt marked as **Test**) for all sandbox testing. Production credentials are separate and are available in your PayU Dashboard once your account is live.
</Callout>

***

## Overview of Steps

A LazyPay payment has five stages. This quick start walks through all five at a simplified level so you can make your first test payment now:<br />

1. Prepare the payment request with `pg=BNPL` and `bankcode=LAZYPAY`
2. Generate a SHA-512 hash on your server
3. Send the payment request to PayU
4. Let the customer confirm the payment with the LazyPay OTP
5. Verify the response on your server

<Callout icon="fad fa-grip-dots-vertical" theme="success">
  ### **Integration Guide**

  Once your test payment works end to end, go to the full [BNPL Merchant Hosted Integration](./bnpl-merchant-hosted-integration) guide. It covers all parameters, hash edge cases, multi-language code samples, OTP retries and error handling in detail.
</Callout>

***

## Make Your First Test Payment

| **Environment**            | **URL**                                                              |
| :------------------------- | :------------------------------------------------------------------- |
| **Test Environment**       | [<redacted URL>](<redacted URL>)                                     |
| **Production Environment** | [https://secure.payu.in//\_payment](https://secure.payu.in/_payment) |

<Accordion title="Step 1: Prepare Request Parameters" icon="fad fa-table">
  These are the minimum parameters for a LazyPay payment. All of them are required. If any are missing, the request fails.<br />

  <Tabs>
    <Tab title="Mandatory Parameters">
      ```text Parameters
      key=YOUR_KEY
      txnid=txn_123456
      amount=10.00
      productinfo=TestProduct
      firstname=Aarav
      email=aarav@example.com
      phone=9876543210
      surl=https://yourwebsite.com/success
      furl=https://yourwebsite.com/failure
      pg=BNPL
      bankcode=LAZYPAY
      hash=GENERATED_HASH
      ```
    </Tab>

    <Tab title="Parameter Description">
      | **Parameters** | **Description**                                                                                                                                                                                      |
      | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | `key`          | `string` Merchant key from the PayU Dashboard. For example, `JPG****.k`                                                                                                                              |
      | `txnid`        | `string` Unique transaction ID you generate. For example, `txn_123456`                                                                                                                               |
      | `amount`       | `string` The transaction amount in INR. The value must be: <ul><li>Numeric</li><li>Up to 2 decimal places</li><li>Without commas</li></ul> For example, `10.00`                                      |
      | `productinfo`  | `string` A brief description of the product. For example, `iPhone`                                                                                                                                   |
      | `firstname`    | `string` The first name of the customer. For example, `Aarav`                                                                                                                                        |
      | `email`        | `string` The email address of the customer. For example, `aarav@example.com`                                                                                                                         |
      | `phone`        | `string` The customer's 10-digit mobile number. LazyPay sends the OTP to this number. For example, `9876543210`                                                                                      |
      | `surl`         | `string` The success URL PayU redirects the customer to after a successful payment. <a href="https://test-payment-middleware.payu.in/simulatorResponse" title="Example surl">Success URL Example</a> |
      | `furl`         | `string` The failure URL PayU redirects the customer to after a failed payment. <a href="https://test-payment-middleware.payu.in/simulatorResponse" title="Example furl">Failure URL Example</a>     |
      | `pg`           | `string` The payment category. For LazyPay, always pass `BNPL`.                                                                                                                                      |
      | `bankcode`     | `string` The lender code. For LazyPay, always pass `LAZYPAY`.                                                                                                                                        |
      | `hash`         | `string` The SHA-512 hash you generate in Step 2.                                                                                                                                                    |
    </Tab>
  </Tabs>

  <Callout icon="📘" theme="info">
    ### **Tips:**

    - `txnid` must be unique for every payment attempt.
    - No trailing spaces in any parameter. They break the hash.
    - `amount` must be formatted consistently: `10.00`, not `10` or `₹10`.
    - If you check the customer's LazyPay eligibility before payment, pass the **same** `phone` number in the payment request.
  </Callout>
</Accordion>

<Accordion title="Step 2: Generate SHA-512 Hash (Critical)" icon="fad fa-key">
  The hash protects your payment request from tampering. PayU rejects any request with an invalid hash. LazyPay uses the same hash formula as every other PayU payment method. `pg`, `bankcode` and `phone` are **not** part of the hash.<br />

  <Tabs>
    <Tab title="Hash Formula">
      ```text Formula
      sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
      ```
    </Tab>

    <Tab title="Example with values">
      ```text Example Hash String
      sha512(YOUR_KEY|txn_123456|10.00|TestProduct|Aarav|aarav@example.com|||||||||||YOUR_SALT)
      ```
    </Tab>
  </Tabs>

  <Callout icon="⚠️" theme="warn">
    ### **Critical Rules of Hash Generation**

    Follow these rules to create a correct hash value:<br />

    - [x] Never generate the hash in the browser or mobile app.
    - [x] Keep all pipe separators (`|`) even if UDF fields are empty.
    - [x] Do not add spaces around the separators.
    - [x] Use UTF-8 encoding before hashing.
    - [x] Use SHA-512 (not SHA-256 or MD5).
  </Callout>

  <Accordion title="Step 2.1 Generate Hash using Other Language Bindings" icon="fad fa-code">
    ```javascript Node.js
    const crypto = require("crypto");

    const hashString = "YOUR_KEY|txn_123456|10.00|TestProduct|Aarav|aarav@example.com|||||||||||YOUR_SALT";

    const hash = crypto
      .createHash("sha512")
      .update(hashString, "utf8")
      .digest("hex");

    console.log(hash);
    ```
    ```php PHP
    <?php
    $hashString = "YOUR_KEY|txn_123456|10.00|TestProduct|Aarav|aarav@example.com|||||||||||YOUR_SALT";
    $hash = strtolower(hash('sha512', $hashString));
    echo $hash;
    ?>
    ```
    ```python Python
    import hashlib

    hash_string = "YOUR_KEY|txn_123456|10.00|TestProduct|Aarav|aarav@example.com|||||||||||YOUR_SALT"
    hash_value = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
    print(hash_value)
    ```

    For Java and C# examples, see [Generate Hash](./bnpl-merchant-hosted-integration#step-3-generate-hash) in the BNPL Merchant Hosted Integration page.
  </Accordion>
</Accordion>

<Accordion title="Step 3: Send the Payment Request" icon="fad fa-paper-plane">
  Choose how the customer enters the LazyPay OTP. Start with **Option A** for your first test payment. It needs no extra screens.<br />

  <Tabs>
    <Tab title="Option A: PayU OTP Page (HTML form)">
      Create a file called `payment.html` with the form below. Replace the placeholder values with your test credentials and the hash you generated in Step 2. PayU collects the LazyPay OTP on its own page.

      ```html
      <!doctype html>
      <html>
        <body onload="document.forms.payu.submit()">
          <form name="payu" method="post" action="<redacted URL>">
            <input type="hidden" name="key"         value="YOUR_KEY" />
            <input type="hidden" name="txnid"       value="txn_123456" />
            <input type="hidden" name="amount"      value="10.00" />
            <input type="hidden" name="productinfo" value="TestProduct" />
            <input type="hidden" name="firstname"   value="Aarav" />
            <input type="hidden" name="email"       value="aarav@example.com" />
            <input type="hidden" name="phone"       value="9876543210" />
            <input type="hidden" name="surl"        value="https://test-payment-middleware.payu.in/simulatorResponse" />
            <input type="hidden" name="furl"        value="https://test-payment-middleware.payu.in/simulatorResponse" />
            <input type="hidden" name="pg"          value="BNPL" />
            <input type="hidden" name="bankcode"    value="LAZYPAY" />
            <input type="hidden" name="hash"        value="GENERATED_HASH" />
            <input type="submit" value="Pay with LazyPay" />
          </form>
        </body>
      </html>
      ```

      Open `payment.html` in your browser. The form submits automatically and opens the LazyPay OTP page.
    </Tab>

    <Tab title="Option B: Your Own OTP Screen (Native OTP)">
      To collect the OTP on your own screen, call `_payment` from your server and add `txn_s2s_flow=4` and `s2s_device_info`.

      ```bash cURL
      curl --location --request POST '<redacted URL>' \
      --header 'Content-Type: application/x-www-form-urlencoded' \
      --data-urlencode 'key=YOUR_KEY' \
      --data-urlencode 'txnid=txn_123456' \
      --data-urlencode 'amount=10.00' \
      --data-urlencode 'productinfo=TestProduct' \
      --data-urlencode 'firstname=Aarav' \
      --data-urlencode 'email=aarav@example.com' \
      --data-urlencode 'phone=9876543210' \
      --data-urlencode 'surl=https://yourwebsite.com/success' \
      --data-urlencode 'furl=https://yourwebsite.com/failure' \
      --data-urlencode 'pg=BNPL' \
      --data-urlencode 'bankcode=LAZYPAY' \
      --data-urlencode 'txn_s2s_flow=4' \
      --data-urlencode 's2s_device_info=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36' \
      --data-urlencode 'hash=GENERATED_HASH'
      ```

      PayU returns a `pending` response with a `referenceId`, an `otpPostUrl` and an `acsTemplate`:

      ```json Payment Response (pending)
      {
        "metaData": {
          "message": null,
          "referenceId": "6a037a290af9253a1d300c8ad0b24c94",
          "statusCode": null,
          "txnId": "txn_123456",
          "txnStatus": "pending",
          "unmappedStatus": "pending"
        },
        "result": {
          "acsTemplate": "PGh0bWw+PGJvZHk+...PC9odG1sPg==",
          "otpPostUrl": "<redacted URL>"
        }
      }
      ```

      {/* REVIEW: Confirm the otpPostUrl host merchants receive in the test environment. Confluence sample shows an internal pre-prod host. */}

      <Callout icon="📘" theme="info">
        ### **Which one do I use?**

        - If the response contains `otpPostUrl`, show your OTP screen and post the OTP to that URL (see Step 4).
        - If `otpPostUrl` is missing, Base64-decode `acsTemplate` and render the HTML. It opens the PayU OTP page.
        - If `txnStatus` is `failed`, there's no OTP step. Show the customer another payment option.
      </Callout>
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Step 4: Complete the Test Payment with the OTP" icon="fad fa-mobile-screen-button">
  LazyPay sends an OTP to the customer's mobile number.<br />

  <Tabs>
    <Tab title="Option A: PayU OTP Page">
      Enter the OTP on the PayU OTP page. After the payment, PayU redirects the customer to your `surl` or `furl`.
    </Tab>

    <Tab title="Option B: Your Own OTP Screen">
      Post the OTP the customer enters, together with the `referenceId`, to the `otpPostUrl` from Step 3. Send it from your server as form-urlencoded data.

      ```bash cURL
      curl --location --request POST 'OTP_POST_URL_FROM_STEP_3' \
      --header 'Content-Type: application/x-www-form-urlencoded' \
      --data-urlencode 'referenceId=6a037a290af9253a1d300c8ad0b24c94' \
      --data-urlencode 'otp=OTP_ENTERED_BY_CUSTOMER'
      ```

      **If the OTP is correct**, `submitOtp.status` is `success` and `result` contains the payment details (trimmed below):

      ```json Submit OTP Response (success)
      {
        "metaData": {
          "message": "No Error",
          "referenceId": "6a037a290af9253a1d300c8ad0b24c94",
          "statusCode": "E000",
          "txnId": "txn_123456",
          "unmappedStatus": "success",
          "submitOtp": { "status": "success" }
        },
        "result": {
          "mihpayid": "999000000000582",
          "mode": "BNPL",
          "status": "success",
          "key": "YOUR_KEY",
          "txnid": "txn_123456",
          "amount": "10.00",
          "productinfo": "TestProduct",
          "firstname": "Aarav",
          "email": "aarav@example.com",
          "phone": "9876543210",
          "PG_TYPE": "BNPL-PG",
          "bankcode": "LAZYPAY",
          "bank_ref_num": "TXN1288577",
          "error": "E000",
          "error_Message": "No Error",
          "unmappedstatus": "captured",
          "hash": "781e999b0e7944a9...171183ab5"
        }
      }
      ```

      **If the OTP is wrong**, `submitOtp.status` is `in progress` and `retryAttemptCount` tells you how many attempts the customer has left. Ask the customer to enter the OTP again.

      ```json Submit OTP Response (incorrect OTP)
      {
        "metaData": {
          "message": "Unauthorized",
          "referenceId": "6a037a290af9253a1d300c8ad0b24c94",
          "txnId": "txn_123456",
          "unmappedStatus": "in progress",
          "submitOtp": { "status": "in progress", "retryAttemptCount": "2" }
        },
        "result": null
      }
      ```
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Step 5: Verify the Response" icon="fa-shield-check">
  Your server must verify every response with reverse hashing before marking the order as paid.<br />

  **Reverse hash formula:**<br />

  ```text
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  Generate this hash on your server and compare it with the `hash` field in the response. If they match, the response is authentic.<br />

  Check these fields too:<br />

  - `status` is `success` and `unmappedstatus` is `captured`
  - `bankcode` is `LAZYPAY` and `mode` is `BNPL`
  - `txnid` and `amount` match your order

  <Callout icon="⚠️" theme="warn">
    ### **Never Skip Response Verification**

    A browser redirect can be spoofed. Only a server-side reverse hash comparison can confirm the response came from PayU.
  </Callout>

  If the callback doesn't arrive, confirm the transaction status from your server with the [Verify Payment API](ref:verify_payment_api).
</Accordion>

## Common First-Time Errors

<Accordion title="Errors and Troubleshooting" icon="fab fa-first-order-alt">
  **Invalid Hash:**<br />

  Check the parameter order in your hash string and make sure there are no extra spaces. Confirm you're using your test salt, not your production salt. Don't add `pg`, `bankcode` or `phone` to the hash.

  **LazyPay isn't available or the payment fails straight away (**`E308`**,&#x20;**`txnStatus: failed`**):**<br />

  LazyPay may not be enabled on your account, or the customer may not be eligible. Ask PayU to confirm LazyPay is enabled. Then try a different test phone number, or use [Link and Pay](./bnpl-link-and-pay-merchant-hosted) to check eligibility before payment.

  **No&#x20;**`otpPostUrl`**&#x20;in the response:**<br />

  This is expected in some cases. Base64-decode `acsTemplate` and render it to open the PayU OTP page.

  **OTP rejected:**<br />

  Check `retryAttemptCount` and let the customer try again. When no attempts are left, offer another payment method.

  **Payment page doesn't load (Option A):**<br />

  Make sure your form uses `method="post"` and the action URL is `<redacted URL>`.

  For the full list of lender error codes and fixes, see [BNPL Errors and Troubleshooting](./bnpl-errors-and-troubleshooting).
</Accordion>

***

## Next Steps

Once your test payment works end to end, go to:<br />

- [BNPL Merchant Hosted Integration:](./bnpl-merchant-hosted-integration) The full guide, with all parameters, multi-language hash samples, OTP retries and response handling
- [BNPL Link and Pay:](./bnpl-link-and-pay-merchant-hosted) Check LazyPay eligibility before checkout and save the customer's LazyPay account for faster repeat payments
- [Test BNPL Integration:](./bnpl-test-integration) Test scenarios to run before you go live
- [BNPL Errors and Troubleshooting:](./bnpl-errors-and-troubleshooting) Lender error codes and fixes