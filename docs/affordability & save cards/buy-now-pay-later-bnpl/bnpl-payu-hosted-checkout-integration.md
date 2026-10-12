---
title: BNPL PayU Hosted Checkout Integration
deprecated: false
hidden: true
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

With PayU Hosted Checkout, PayU hosts the payment page. The customer selects **Pay Later**, picks a lender, and completes OTP authentication on PayU's page. You only send the payment request and verify the response.

<Callout icon="📘" theme="info">
  ### **API References:**

  - [Collect Payment API](ref:collect-payments-with-payu-hosted-checkout)
  - [Verify Payment API](ref:verify_payment_api)
</Callout>

***

## Prerequisites

- A PayU merchant account with **BNPL enabled**. If BNPL doesn't appear on your checkout page, contact your PayU Key Account Manager or [PayU Support](https://help.payu.in/raise-ticket).
- A working [PayU Hosted Checkout integration](doc:payu-hosted-checkout-build-integration), or the ability to build one.
- Your test merchant key and salt. See [Generate Test Key and Salt](https://docs.payu.in/docs/generate-test-merchant-key-and-salt).

***

## Overview of Steps

1. [Check that BNPL is enabled](#step-1-check-that-bnpl-is-enabled) on your account.
2. [Prepare the payment request and generate the hash](#step-2-prepare-the-payment-request-and-generate-the-hash).
3. [Redirect the customer to PayU Checkout](#step-3-redirect-the-customer-to-payu-checkout).
4. [Verify the response with reverse hashing](#step-4-verify-the-response-with-reverse-hashing).
5. [Verify the payment](#step-5-verify-the-payment).

***

## Build Integration Steps

### Step 1: Check That BNPL Is Enabled

BNPL and its lenders (for example, LazyPay and Simpl) must be active on your merchant account. Ask your PayU Key Account Manager or [PayU Support](https://help.payu.in/raise-ticket) to enable them.

**Checkpoint:** ✅ **Pay Later** appears as a payment option on the PayU test checkout page.

***

### Step 2: Prepare the Payment Request and Generate the Hash

The request is the same as a standard PayU Hosted Checkout request. Don't pass `pg` or `bankcode`. The customer picks the lender on PayU's page.

<Tabs>
  <Tab title="Mandatory Parameters">
    | Parameter     | Description                                                                                                |
    | ------------- | ---------------------------------------------------------------------------------------------------------- |
    | `key`         | `string` Merchant key provided by PayU. For example, `JPG****k`.                                           |
    | `txnid`       | `string` Unique transaction ID that you generate. For example, `tran_1234`.                                |
    | `amount`      | `string` Payment amount. For example, `10.00`.                                                             |
    | `productinfo` | `string` Brief product description. For example, `iPhone`.                                                 |
    | `firstname`   | `string` Customer's first name. For example, `Aarav`.                                                      |
    | `email`       | `string` Customer's email address. For example, `aarav@example.com`.                                       |
    | `phone`       | `string` Customer's mobile number. BNPL lenders use it for eligibility and OTP. For example, `9876543210`. |
    | `surl`        | `string` Success URL.                                                                                      |
    | `furl`        | `string` Failure URL.                                                                                      |
    | `hash`        | `string` SHA-512 hash of the request. See below.                                                           |
  </Tab>

  <Tab title="Optional Parameters">
    | Parameter            | Description                                                                      |
    | -------------------- | -------------------------------------------------------------------------------- |
    | `lastname`           | `string` Customer's last name.                                                   |
    | `curl`               | `string` Cancel URL.                                                             |
    | `address1`–`zipcode` | `string` Billing address fields. They help with fraud detection and chargebacks. |
    | `udf1`–`udf5`        | `string` User-defined fields. Include them in the hash, even when empty.         |
  </Tab>
</Tabs>

<Accordion title="Hash Logic" icon="fa-key">
  ```Text Logic
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
  ```

  For code samples in PHP, Java, C#, Python, and JavaScript, see [Generate Secure Hash](doc:payu-hosted-checkout-build-integration#step-2-generate-secure-hash).

  <Callout icon="⚠️" theme="warn">
    ### **Critical Rules**

    - Generate the hash on your server only.
    - Keep all pipe (`|`) separators, even for empty fields.
    - No extra spaces in any value. Use UTF-8 encoding and SHA-512.
  </Callout>
</Accordion>

***

### Step 3: Redirect the Customer to PayU Checkout

POST the parameters and hash to PayU's `_payment` endpoint with an auto-submitting HTML form.

<Accordion title="POST the HTML Form" icon="fa-paper-plane">
  #### Environment

  |                |                                   |
  | -------------- | --------------------------------- |
  | **Test**       | `https://test.payu.in/_payment`   |
  | **Production** | `https://secure.payu.in/_payment` |

  ```html
  <!doctype html>
  <html>
    <body onload="document.forms.payu.submit()">
      <form name="payu" method="post" action="https://test.payu.in/_payment">
        <input type="hidden" name="key" value="JP***g">
        <input type="hidden" name="txnid" value="t6svtqtjRdl4ws">
        <input type="hidden" name="amount" value="499.00">
        <input type="hidden" name="productinfo" value="Pro Plan">
        <input type="hidden" name="firstname" value="Aditi">
        <input type="hidden" name="email" value="test@example.com">
        <input type="hidden" name="phone" value="9876543210">
        <input type="hidden" name="surl" value="https://yourapp.com/payu/success">
        <input type="hidden" name="furl" value="https://yourapp.com/payu/failure">
        <input type="hidden" name="hash" value="YOUR_GENERATED_HASH">
      </form>
    </body>
  </html>
  ```
</Accordion>

#### What Next: Customer Journey

1. The customer selects **Pay Later** on the PayU payment page.
2. The customer picks a lender (for example, LazyPay) and confirms their mobile number.
3. The customer enters the OTP from the lender and completes the payment.
4. PayU redirects the customer to your `surl` or `furl` with the result.

<Accordion title="BNPL Success and Error Responses" icon="fa-circle-check">
  ```json Success Response
  mihpayid=403993715537577231
  mode=BNPL
  status=success
  unmappedstatus=captured
  key=ISgdHG
  txnid=6decc0fffa5c60c7cbce
  amount=10.00
  productinfo=Product Info
  firstname=Payu-Admin
  email=test@example.com
  phone=1234567890
  udf1=
  udf2=
  udf3=
  udf4=
  udf5=
  field9=Transaction is successful
  PG_TYPE=BNPL-PG
  bank_ref_num=TXN558633373
  bankcode=LAZYPAY
  error=E000
  error_Message=No Error
  net_amount_debit=10
  hash=caa5b6398fe72ae9a07bc5e2d140fb2872db8f95bfe997de214f7f4cbc14e0933c153db986f029f76b69c12a37589d59ce9fe4c56d1bc713ac9851593563425e
  ```
  ```json Error Response - Cancelled During OTP Flow
  mihpayid=403993715537573947
  mode=BNPL
  status=failure
  unmappedstatus=userCancelled
  key=a4vGC2
  txnid=TXN_NS_1780297112_4289
  amount=1500.00
  net_amount_debit=0.00
  productinfo=Test
  firstname=Sunit
  email=sunit.kumar@mail.com
  phone=9876543210
  field9=cancelled by user
  PG_TYPE=BNPL-PG
  bankcode=LAZYPAY
  error=
  error_Message=
  hash=79c624327255af38af22d10005f43a6afaaa9cf212ddb2998becd56d1dd9c1f5eae1d587ab82543f53ed005eb3d752f67b445a8523153f4bea969cb3e765b5dd
  ```

  For error codes, see [BNPL Errors and Troubleshooting](doc:bnpl-errors-and-troubleshooting).
</Accordion>

***

### Step 4: Verify the Response with Reverse Hashing

PayU POSTs the result to your `surl` or `furl` with a `hash`. Verify it on your server before you mark the order as paid.

<Accordion title="Reverse Hashing Logic" icon="fa-arrow-rotate-left">
  ```Text Reverse Hash Logic
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```
</Accordion>

<Callout icon="✅" theme="okay">
  ### **Validation Rules:**

  - The hash you generate must match the response `hash`.
  - The `amount` must match the original order.
  - The `txnid` must exist in your system and must not already be marked paid.
</Callout>

If the hash doesn't match, reject the callback, log it as a security alert, and don't mark the payment as successful.

***

### Step 5: Verify the Payment

Confirm the final status with one or more of these methods:

<Verify_Payment_Tabs />

<br />

***

## Security

| Requirement                                                  | Why                                               |
| ------------------------------------------------------------ | ------------------------------------------------- |
| Generate the hash **server-side only**                       | Client-side hashing exposes your salt.            |
| Store the salt in environment variables or a secrets manager | Treat the salt like a password. Never log it.     |
| Use **HTTPS** for `surl`, `furl`, and webhook URLs           | Protects payment data in transit.                 |
| Verify the reverse hash on **every** callback and webhook    | Browser redirects can be spoofed.                 |
| Make your handling of `txnid` idempotent                     | Callbacks and webhooks may arrive more than once. |

***

## Next Steps

<Cards columns="2">
  <Card title="Test Integration" href="doc:bnpl-test-integration" icon="fa-flask">
    Test BNPL success, failure, and cancellation scenarios.
  </Card>

  <Card title="Errors and Troubleshooting" href="doc:bnpl-errors-and-troubleshooting" icon="fa-triangle-exclamation">
    Lender error codes and how to fix them.
  </Card>
</Cards>
