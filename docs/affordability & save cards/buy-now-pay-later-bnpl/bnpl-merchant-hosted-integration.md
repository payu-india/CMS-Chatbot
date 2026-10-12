---
title: BNPL Merchant Hosted Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: BNPL with Merchant Hosted Checkout
excerpt: >-
  Integrate BNPL on your own checkout page: check customer eligibility, post
  the payment with pg=BNPL, handle the lender OTP with a redirect or native OTP,
  and verify the response.
deprecated: false
hidden: true
metadata:
  title: BNPL Merchant Hosted Integration | PayU Docs
  description: >-
    Technical guide to integrating Buy Now Pay Later on your own checkout page
    with PayU: eligibility check, request parameters, SHA-512 hash, native OTP
    with otpPostUrl and acsTemplate, reverse hash, and payment verification.
  keywords:
    - payu bnpl merchant hosted integration
    - payu bnpl seamless integration
    - bnpl native otp txn_s2s_flow 4
    - payu otpPostUrl acsTemplate
    - payu bnpl eligibility check
    - lazypay simpl hdfc flexipay api integration
    - payu bnpl hash generation
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: bnpl-link-and-pay-merchant-hosted
      title: BNPL Link and Pay (Merchant Hosted)
      type: basic
    - slug: bnpl-test-integration
      title: Test BNPL Integration
      type: basic
    - slug: bnpl-errors-and-troubleshooting
      title: BNPL Errors and Troubleshooting
      type: basic
---
<Banner
  isInline={true}
  message="Integration effort: Moderate — server-side integration required"
  color="#FF9800"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

With Merchant Hosted Checkout, you show BNPL lenders on your own checkout page and post the payment request to PayU from your server. The lender OTP can run on the lender's or PayU's page (redirect), or on your own UI (native OTP).

<Callout icon="📘" theme="info">
  ### **API References:**

  - [Check BNPL Eligibility API](ref:get_checkout_details)
  - [Collect Payment API (Merchant Hosted)](ref:collect-payments-with-merchant-hosted-checkout)
  - [Verify Payment API](ref:verify_payment_api)
</Callout>

{/* REVIEW: Confirm the eligibility and Merchant Hosted Collect Payment API reference slugs. */}

***

## Prerequisites

- A PayU merchant account with **BNPL and the lenders you need enabled**. Contact your PayU Key Account Manager or [PayU Support](https://help.payu.in/raise-ticket).
- Your test merchant key and salt. See [Generate Test Key and Salt](https://docs.payu.in/docs/generate-test-merchant-key-and-salt).
- A backend server for hash generation, API calls, and response verification.

<Callout icon="💡" theme="info">
  ### **Want One-Click Repeat Payments?**

  To let returning customers pay without an OTP, use [BNPL Link and Pay](doc:bnpl-link-and-pay-merchant-hosted) instead.
</Callout>

***

## Overview of Steps

1. [Check customer eligibility](#step-1-check-customer-eligibility) so you only show lenders the customer can use.
2. [Prepare the payment request parameters](#step-2-prepare-payment-request-parameters).
3. [Generate a secure hash](#step-3-generate-secure-hash).
4. [Post the payment request](#step-4-post-the-payment-request), with a redirect or native OTP.
   1. [Handle the native OTP response](#step-41-handle-the-native-otp-response) if you use native OTP.
5. [Verify the response with reverse hashing](#step-5-verify-the-response-with-reverse-hashing).
6. [Verify the payment](#step-6-verify-the-payment).

***

## Build Integration Steps

### Step 1: Check Customer Eligibility

Before you show BNPL on your checkout page, check which lenders the customer is eligible for. Show only the eligible lenders. If the customer isn't eligible, hide BNPL or show the reason the API returns.

<Accordion title="Eligibility Request Parameters" icon="fa-user-check">
  | Parameter                              | Description                                                                                         | Example                                   |
  | -------------------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------- |
  | `requestId` <br />_mandatory_          | `string` Unique ID for the eligibility request.                                                     | `Test1234`                                |
  | `transactionDetails` <br />_mandatory_ | `JSON` Transaction amount.                                                                          | `{"amount":"10000"}`                      |
  | `customerDetails` <br />_mandatory_    | `JSON` Customer's mobile number. Use the same number in the `phone` parameter of the payment request. | `{"mobile":"9999999999"}`               |
  | `paymentOptions` <br />_mandatory_     | `JSON` The BNPL lender codes to check, or `all`.                                                    | `{"bnpl":"all"}`                          |
  | `useCase` <br />_mandatory_            | `JSON` Set to check customer eligibility.                                                           | `{"checkCustomerEligibility":true}`       |

  For the endpoint, headers, and response schema, see the [Check BNPL Eligibility API](ref:get_checkout_details).
</Accordion>

**Checkpoint:** ✅ You show only the BNPL lenders the customer is eligible for.

***

### Step 2: Prepare Payment Request Parameters

<Tabs>
  <Tab title="Mandatory Parameters">
    | Parameter     | Description                                                                                                         |
    | ------------- | ------------------------------------------------------------------------------------------------------------------- |
    | `key`         | `string` Merchant key provided by PayU. For example, `JPg***r`.                                                     |
    | `txnid`       | `string` Unique transaction ID. PayU doesn't accept duplicates. For example, `ypl938459435`.                        |
    | `amount`      | `string` Payment amount. For example, `10.00`.                                                                      |
    | `productinfo` | `string` Product description (up to 100 characters). For example, `iPhone`.                                        |
    | `firstname`   | `string` Customer's first name (up to 60 characters). For example, `Ashish`.                                        |
    | `lastname`    | `string` Customer's last name (up to 60 characters). For example, `Verma`.                                          |
    | `email`       | `string` Customer's email (up to 50 characters). For example, `abc@payu.in`.                                        |
    | `phone`       | `string` Customer's mobile number. **Must match the number you used in the eligibility check.** For example, `9876543210`. |
    | `pg`          | `string` Payment category. Use `BNPL`.                                                                              |
    | `bankcode`    | `string` Lender code. For example, `LAZYPAY`, `SIMPL`. See [BNPL Codes](doc:bnpl-codes).                            |
    | `surl`        | `string` Success URL.                                                                                               |
    | `furl`        | `string` Failure URL.                                                                                               |
    | `hash`        | `string` SHA-512 hash. See [Step 3](#step-3-generate-secure-hash).                                                  |
  </Tab>

  <Tab title="Conditional and Optional Parameters">
    | Parameter            | Description                                                                                                          |
    | -------------------- | -------------------------------------------------------------------------------------------------------------------- |
    | `txn_s2s_flow`       | `string` **Mandatory for native OTP.** Pass `4` to get the OTP response back on your server instead of a redirect. `2` isn't supported for BNPL. |
    | `s2s_device_info`    | `string` The customer's browser user agent. Recommended when `txn_s2s_flow=4`.                                       |
    | `ccnum`              | `string` **Mandatory for HDFC FlexiPay.** The customer's full credit card number that's eligible for FlexiPay.       |
    | `address1`–`zipcode` | `string` Billing address fields. They help with fraud detection and chargebacks.                                     |
    | `udf1`–`udf5`        | `string` User-defined fields (up to 255 characters). Include them in the hash, even when empty.                      |
    | `curl`               | `string` Cancel URL.                                                                                                 |
  </Tab>
</Tabs>

<Callout icon="📘" theme="info">
  ### **Lender Notes**

  - **HDFC FlexiPay** uses separate bank codes by tenure: `HDFCF15`, `HDFCF30`, `HDFCF60`, `HDFCF90`. Always pass `ccnum`.
  - **Simpl:** On a customer's first Simpl payment, the customer links their account on Simpl's page. In native OTP, you get an `acsTemplate` to render instead of an `otpPostUrl`.
</Callout>

***

### Step 3: Generate Secure Hash

<Accordion title="Steps to Generate Hash" icon="fa-key">
  ```Text Logic
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
  ```
  ```Text Example Values
  sha512(JPg***r|ypl938459435|10.00|iPhone|Ashish|abc@payu.in|||||||||||salt_value)
  ```
  ```python
  import hashlib

  def generate_hash(p, salt):
      seq = [p['key'], p['txnid'], p['amount'], p['productinfo'], p['firstname'], p['email'],
             p.get('udf1', ''), p.get('udf2', ''), p.get('udf3', ''), p.get('udf4', ''), p.get('udf5', '')]
      hash_string = '|'.join(seq) + '||||||' + salt
      return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
  ```
  ```javascript
  const crypto = require('crypto');

  function generateHash(p, salt) {
    const seq = [p.key, p.txnid, p.amount, p.productinfo, p.firstname, p.email,
      p.udf1 || '', p.udf2 || '', p.udf3 || '', p.udf4 || '', p.udf5 || ''];
    const hashString = seq.join('|') + '||||||' + salt;
    return crypto.createHash('sha512').update(hashString, 'utf8').digest('hex');
  }
  ```
  ```php
  <?php
  function generateHash($p, $salt) {
    $seq = [$p['key'], $p['txnid'], $p['amount'], $p['productinfo'], $p['firstname'], $p['email'],
            $p['udf1'] ?? '', $p['udf2'] ?? '', $p['udf3'] ?? '', $p['udf4'] ?? '', $p['udf5'] ?? ''];
    $hashString = implode('|', $seq) . '||||||' . $salt;
    return strtolower(hash('sha512', $hashString));
  }
  ?>
  ```
  ```java
  import java.nio.charset.StandardCharsets;
  import java.security.MessageDigest;
  import java.util.Map;

  public class HashGenerator {
    public static String generateHash(Map<String, String> p, String salt) throws Exception {
      String hashString = String.join("|",
          p.get("key"), p.get("txnid"), p.get("amount"), p.get("productinfo"),
          p.get("firstname"), p.get("email"),
          p.getOrDefault("udf1", ""), p.getOrDefault("udf2", ""), p.getOrDefault("udf3", ""),
          p.getOrDefault("udf4", ""), p.getOrDefault("udf5", "")) + "||||||" + salt;
      byte[] bytes = MessageDigest.getInstance("SHA-512").digest(hashString.getBytes(StandardCharsets.UTF_8));
      StringBuilder sb = new StringBuilder();
      for (byte b : bytes) sb.append(String.format("%02x", b));
      return sb.toString();
    }
  }
  ```

  For C# and full examples, see [Generate Secure Hash](doc:payu-hosted-checkout-build-integration#step-2-generate-secure-hash).

  <Callout icon="⚠️" theme="warn">
    ### **Critical Rules**

    - Generate the hash on your server only. Never in browser or mobile app code.
    - Keep all pipe (`|`) separators, even for empty fields.
    - No extra spaces. Use UTF-8 encoding and SHA-512.
    - BNPL-specific parameters (`pg`, `bankcode`, `txn_s2s_flow`, `ccnum`) aren't part of the hash.
  </Callout>

  <Callout icon="🚧" theme="warn">
    ### **Common Causes of Invalid Hash:**

    - Wrong parameter order
    - Missing pipe separators
    - Wrong salt (test vs production)
    - Extra spaces or a different `amount` format than the one you post
  </Callout>
</Accordion>

***

### Step 4: Post the Payment Request

#### Environment

|                |                                   |
| -------------- | --------------------------------- |
| **Test**       | `<redacted URL>`   |
| **Production** | `https://secure.payu.in/_payment` |

Choose how the lender OTP is handled:

<Tabs>
  <Tab title="Option A: Redirect">
    Post the request without `txn_s2s_flow`. PayU redirects the customer to the OTP page. After authentication, PayU posts the result to your `surl` or `furl`.

    ```bash
    curl -X POST "<redacted URL>" \
      -H "Content-Type: application/x-www-form-urlencoded" \
      --data-urlencode "key=JPg***r" \
      --data-urlencode "txnid=ypl938459435" \
      --data-urlencode "amount=10.00" \
      --data-urlencode "productinfo=iPhone" \
      --data-urlencode "firstname=Ashish" \
      --data-urlencode "lastname=Verma" \
      --data-urlencode "email=abc@payu.in" \
      --data-urlencode "phone=9876543210" \
      --data-urlencode "pg=BNPL" \
      --data-urlencode "bankcode=LAZYPAY" \
      --data-urlencode "surl=https://your-surl.com" \
      --data-urlencode "furl=https://your-furl.com" \
      --data-urlencode "hash=YOUR_GENERATED_HASH"
    ```

    In a browser flow, post these fields with an auto-submitting HTML form, as shown in [PayU Hosted Checkout](doc:bnpl-payu-hosted-integration#step-3-redirect-the-customer-to-payu-checkout).
  </Tab>

  <Tab title="Option B: Native OTP (txn_s2s_flow=4)">
    Post the request from your server with `txn_s2s_flow=4`. PayU returns a JSON response instead of redirecting. You then collect the OTP on your own UI. See [Step 4.1](#step-41-handle-the-native-otp-response).

    ```bash
    curl -X POST "<redacted URL>" \
      -H "Content-Type: application/x-www-form-urlencoded" \
      --data-urlencode "key=JPg***r" \
      --data-urlencode "txnid=5b7d06c6bf7d4dc2d3a8" \
      --data-urlencode "amount=10.00" \
      --data-urlencode "productinfo=Product Info" \
      --data-urlencode "firstname=Payu-Admin" \
      --data-urlencode "lastname=User" \
      --data-urlencode "email=test@example.com" \
      --data-urlencode "phone=9876543210" \
      --data-urlencode "pg=BNPL" \
      --data-urlencode "bankcode=LAZYPAY" \
      --data-urlencode "txn_s2s_flow=4" \
      --data-urlencode "s2s_device_info=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36" \
      --data-urlencode "surl=https://your-surl.com" \
      --data-urlencode "furl=https://your-furl.com" \
      --data-urlencode "hash=YOUR_GENERATED_HASH"
    ```
  </Tab>
</Tabs>

<Callout icon="✅" theme="success">
  ### **Best Practices:**

  - Generate a unique `txnid` for every attempt and store it before you post the request.
  - Use the same `phone` you used in the eligibility check.
</Callout>

#### Step 4.1: Handle the Native OTP Response

With `txn_s2s_flow=4`, the `_payment` response tells you what to do next:

| Response                                                   | What to do                                                                                     |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `txnStatus=pending` and `result.otpPostUrl` is present     | Show your OTP screen, then submit the OTP to `otpPostUrl` (native OTP).                        |
| `txnStatus=pending` and no `otpPostUrl`                    | Base64-decode `result.acsTemplate` and render the HTML. It opens PayU's OTP page (fallback).   |
| `txnStatus=failed` with an empty `result`                  | The payment failed. Read `statusCode` and `message`. There's no OTP step.                      |

<Accordion title="Sample _payment Responses" icon="fa-code">
  ```json Pending — OTP Required
  {
    "metaData": {
      "message": null,
      "referenceId": "6a037a290af9253a1d300c8ad0b24c94",
      "statusCode": null,
      "txnId": "5b7d06c6bf7d4dc2d3a8",
      "txnStatus": "pending",
      "unmappedStatus": "pending"
    },
    "result": {
      "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0Ii...",
      "otpPostUrl": "<redacted URL>"
    }
  }
  ```
  ```json Failure
  {
    "metaData": {
      "message": "Transaction Failed at bank end.",
      "referenceId": "ea68a970115a9d87c6ece8d0218e6c2a",
      "statusCode": "E308",
      "txnId": "54d2d883f8e4a3fff6ba",
      "txnStatus": "failed",
      "unmappedStatus": "failure"
    },
    "result": {}
  }
  ```
</Accordion>

{/* REVIEW: Confluence samples use a pre-production host for otpPostUrl. Always use the URL returned in the response; confirm the test host shown above. */}

<Accordion title="Submit the OTP" icon="fa-key">
  POST the `referenceId` from the `_payment` response and the OTP the customer entered to the `otpPostUrl`, as form-urlencoded data.

  ```bash
  curl -X POST "<otpPostUrl from the _payment response>" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    --data-urlencode "referenceId=6a037a290af9253a1d300c8ad0b24c94" \
    --data-urlencode "otp=<customer-entered OTP>"
  ```

  ```json Success Response
  {
    "metaData": {
      "message": "No Error",
      "referenceId": "6a037a290af9253a1d300c8ad0b24c94",
      "statusCode": "E000",
      "txnId": "5b7d06c6bf7d4dc2d3a8",
      "unmappedStatus": "success",
      "submitOtp": { "status": "success" }
    },
    "result": {
      "mihpayid": "999000000000582",
      "mode": "BNPL",
      "status": "success",
      "key": "JPg***r",
      "txnid": "5b7d06c6bf7d4dc2d3a8",
      "amount": "10.00",
      "productinfo": "Product Info",
      "firstname": "Payu-Admin",
      "email": "test@example.com",
      "phone": "9876543210",
      "udf1": "", "udf2": "", "udf3": "", "udf4": "", "udf5": "",
      "PG_TYPE": "BNPL-PG",
      "error": "E000",
      "error_Message": "No Error",
      "unmappedstatus": "captured",
      "bank_ref_num": "TXN1288577",
      "bankcode": "LAZYPAY",
      "hash": "781e999b0e7944a91815434d8429ade60882173702211453f7ee3772417009121c67f08a085c450787e1597700334b75477e6b3574cd84e9e4ffb18171183ab5"
    }
  }
  ```
  ```json Incorrect OTP — Retry Allowed
  {
    "metaData": {
      "message": "Unauthorized",
      "referenceId": "ac2155676982514fd2e3199e83a9c9ec",
      "txnId": "ad5a54b6af3e52ab24d6",
      "unmappedStatus": "in progress",
      "submitOtp": {
        "status": "in progress",
        "retryAttemptCount": "2"
      }
    },
    "result": null
  }
  ```

  <Callout icon="⚠️" theme="warn">
    ### **Handling Incorrect OTPs**

    If `submitOtp.status` is `in progress`, the OTP was wrong. `retryAttemptCount` shows how many attempts are left. Ask the customer to re-enter the OTP and submit again with the same `referenceId`. Don't create a new transaction.
  </Callout>
</Accordion>

**Checkpoint:** ✅ You receive a final result with `status=success` (or `failure`) and a `hash`.

***

### Step 5: Verify the Response with Reverse Hashing

Verify the `hash` in the final response (posted to `surl`/`furl`, or in the Submit OTP response `result`) before you mark the order as paid.

<Accordion title="Reverse Hashing Logic" icon="fa-arrow-rotate-left">
  ```Text Reverse Hash Logic
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  Use the values from the response. If your hash matches the response `hash`, the response is authentic.
</Accordion>

<Callout icon="✅" theme="okay">
  ### **Validation Rules:**

  - The hash you generate must match the response hash.
  - The `amount` must match the original order.
  - The `txnid` must exist and must not already be marked paid.
</Callout>

<Callout icon="⚠️" theme="warn">
  ### **If the Hash Doesn't Match:**

  Reject the response, log it as a security alert, and don't mark the payment as successful.
</Callout>

***

### Step 6: Verify the Payment

<Accordion title="Verify Payment Methods" icon="fa-check-double">
  <Tabs>
    <Tab title="1. Webhooks">
      Configure webhooks to get server-to-server payment notifications that don't depend on the customer's browser. See [Manage Webhooks](https://docs.payu.in/docs/webhook-events-and-sample-payloads).
    </Tab>

    <Tab title="2. Verify Payment API">
      Call the [Verify Payment API](ref:verify_payment_api) from your server. This is especially useful if the native OTP flow times out or the final response doesn't arrive.
    </Tab>

    <Tab title="3. Dashboard">
      Log in to the [PayU Dashboard](https://onboarding.payu.in/app/account/signin) → **Transactions** and check that the status is **Success**.
    </Tab>
  </Tabs>
</Accordion>

***

## Security

| Requirement                                                  | Where it applies | Why                                                           |
| ------------------------------------------------------------ | ---------------- | ------------------------------------------------------------- |
| Generate the hash **server-side only**                       | Step 3           | Client-side hashing exposes your salt.                        |
| Call `_payment` with `txn_s2s_flow=4` from your server only  | Step 4           | Keeps your key, hash, and responses off the client.           |
| Send the OTP over HTTPS straight to `otpPostUrl`; never store or log it | Step 4.1 | The OTP is a customer authentication credential.            |
| Verify the reverse hash on **every** final response and webhook | Step 5        | Prevents spoofed or tampered responses.                       |
| Check that `amount` and `txnid` match your stored order      | Step 5           | Prevents amount tampering and replay.                         |
| Make your handling of `txnid` idempotent                     | Order management | Callbacks and webhooks may arrive more than once.             |

***

## Going Live: Final Checklist

- [ ] Switch `_payment` from `<redacted URL>` to `https://secure.payu.in/_payment`.
- [ ] Switch the eligibility API to its production endpoint (see the [API reference](ref:get_checkout_details)).
- [ ] Replace the test key and salt with production credentials.
- [ ] Confirm the lenders you need are enabled on your production account.
- [ ] Configure and test webhooks on production.
- [ ] Confirm reverse hash validation is on for every response.

***

## Next Steps

<Cards columns="2">
  <Card title="Test Integration" href="doc:bnpl-test-integration" icon="fa-flask">
    Test eligibility, native OTP, incorrect OTP, failure, and cancellation.
  </Card>

  <Card title="Link and Pay" href="doc:bnpl-link-and-pay-merchant-hosted" icon="fa-link">
    Add one-click repeat payments for linked customers.
  </Card>
</Cards>
