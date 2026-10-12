---
title: Test Integration
excerpt: >-
  Test credentials, payment scenarios, and verification steps for PayU Hosted
  Checkout. Validate your integration before going live.
deprecated: false
hidden: true
metadata:
  title: Test PayU Hosted Checkout Integration
  description: >-
    Test credentials and scenarios for PayU Hosted Checkout: NetBanking, debit
    card, credit card, UPI, and wallet. Verify success and failure flows.
  keywords:
    - payu hosted checkout test integration
    - payu test credentials netbanking card upi wallet
    - payu test card numbers india mastercard visa rupay
    - payu upi test vpa anything@payu
    - payu sandbox test environment
    - payu simulate success failure payment
    - payu test.payu.in payment testing
  robots: index
next:
  description: Explore related information and resources.
---
<Banner
  isInline={true}
  message="Integration effort: Minimal technical setup required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

Use this page to test your <Anchor target="_blank" href="https://docs.payu.in/docs/payu-hosted-checkout-build-integration">built PayU Hosted Checkout</Anchor> integration end-to-end in the sandbox environment before going live.

<Callout icon="⚠️" theme="warn">
  ### **Use Test Credentials Only**

  The credentials on this page are for the PayU test environment (`https://test.payu.in`). Never use test keys or salts in production, and never use production keys in the test environment.
</Callout>

***

## Before You Test

Verify the following before running test transactions:

- You are using your **test** merchant key and salt (not production). Get these from PayU Dashboard → **Developer** → **API Keys**. See [Generate Test Key and Salt](https://docs.payu.in/docs/generate-test-merchant-key-and-salt).
- Your HTML form `action` URL is `https://test.payu.in/_payment` and not the production URL.
- Your hash is generated with the test salt.
- Your `surl` and `furl` are publicly reachable HTTPS endpoints (not localhost). For initial testing, you can use `https://test-payment-middleware.payu.in/simulatorResponse`.

<Callout icon="fad fa-exclamation" theme="error">
  ### **Important:**

  The most common test failure is an incorrect hash. Print the exact string you pass to the SHA-512 function on your server, and verify it follows the formula `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT` with empty string placeholders for unused UDFs.
</Callout>

***

## Test Scenarios

### Scenario 1: Successful Payment

<Accordion title="Steps to Test the Successful Payment" icon="fa-circle-check">
  1. Open your payment HTML form in a browser.
  2. The form auto-submits and redirects you to the PayU test checkout page.
  3. Select a payment method.
  4. Enter the test credentials for that method. See the test credentials section below.
  5. Complete authentication (OTP where required).
  6. Verify you are redirected to your `surl`.
  7. On your server, verify the response hash using the reverse hash formula.

  **Expected Results:**

  - Customer redirected to `surl`
  - Response `status=success`
  - Response `error=E000` (no error)
  - Response `hash` matches your computed reverse hash
</Accordion>

### Scenario 2: Failed Payment

<Accordion title="Steps to Test the Failed Payment" icon="fa-vial">
  1. Open your payment HTML form in a browser.
  2. Select any payment method.
  3. Enter **invalid** test credentials (wrong OTP, wrong card number format, etc.).
  4. Verify you are redirected to your `furl`.

  **Expected results:**

  - Customer redirected to `furl`
  - Response `status=failure`
  - Response `error` contains a non-`E000` error code
  - Order remains unpaid in your system
</Accordion>

### Scenario 3: Customer Abandons Payment

<Accordion title="Steps to Test the Payment Abandoned by the Customer" icon="fa-person-running">
  1. Open your payment HTML form in a browser.
  2. On the PayU checkout page, click **Back** or close the browser tab without completing payment.
  3. Verify your order system handles this gracefully.

  **Expected results:**

  - Customer may or may not be redirected to `furl` depending on when they abandoned
  - No webhook or callback arrives (payment never initiated)
  - Order remains in a pending/unpaid state in your system
</Accordion>

***

## Test Credentials by a Payment Method

<Accordion title="NetBanking" icon="fa-building-columns">
  | Field    | Value    |
  | -------- | -------- |
  | Username | `payu`   |
  | Password | `payu`   |
  | OTP      | `123456` |
</Accordion>

<Accordion title="Debit Card" icon="fa-credit-card">
  | Card Number         | Network    | Expiry | CVV | OTP    |
  | ------------------- | ---------- | ------ | --- | ------ |
  | 5118-7000-0000-0003 | Mastercard | 05/30  | 123 | 123456 |
  | 4594-5380-5063-9999 | VISA       | 05/30  | 123 | 123456 |
</Accordion>

<Accordion title="Credit Card" icon="fa-credit-card">
  | Card Number      | Network    | Expiry | CVV  | OTP    |
  | ---------------- | ---------- | ------ | ---- | ------ |
  | 5123456789012346 | Mastercard | 05/30  | 123  | 123456 |
  | 4012001037141112 | VISA       | 05/30  | 123  | 123456 |
  | 6082015309577308 | RuPay      | 05/30  | 123  | 123456 |
  | 370295061673669  | Amex       | 03/30  | 1234 | 725356 |
</Accordion>

<Accordion title="UPI" icon="fa-mobile-screen-button">
  Use `anything@payu` or `999999999@payu` as the VPA (Virtual Payment Address).

  <Callout icon="📘" theme="info">
    The `anything@payu` VPA works on the `_payment` endpoint test environment. It does not work with the Validate VPA API (which requires a real VPA).
  </Callout>
</Accordion>

<Accordion title="Wallet" icon="fa-wallet">
  | Wallet | Mobile Number                | OTP    |
  | ------ | ---------------------------- | ------ |
  | PayTM  | 7777777777                   | 888888 |
  | Amazon | Use your real Amazon account | —      |
  | Airtel | Use your real mobile number  | —      |
</Accordion>

<Accordion title="BNPL (Buy Now Pay Later)" icon="fa-clock">
  BNPL must be enabled on your PayU account before it appears on the checkout page. Contact PayU support or enable it from your PayU Dashboard if eligible.

  **Test VPA / Phone:** Use `9876543210` as the phone number.

  **Expected success response fields:**

  ```
  status=success
  unmappedstatus=captured
  mode=BNPL
  bankcode=LAZYPAY
  error=E000
  error_Message=No Error
  ```

  **Expected failure response (user cancels OTP flow):**

  ```
  status=failure
  unmappedstatus=userCancelled
  mode=BNPL
  bankcode=LAZYPAY
  error_Message=cancelled by user
  ```
</Accordion>

<Callout icon="📘" theme="info">
  **Additional payment methods available on request**

  BNPL, EMI, and International Payments are not enabled by default. You can enable them from your PayU Dashboard (subject to eligibility). See [Customise PayU Hosted Checkout](../customise-payu-hosted-checkout) for configuration details.
</Callout>

***

## Verify the Test Response

After each test transaction, verify these on your server before marking the transaction as tested:

1. **Reverse hash matches** — Compute `sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)` on your server and confirm it matches the `hash` field in the response.

2. **Amount matches** — The `amount` in the response matches the amount you sent in the request.

3. **txnid matches** — The `txnid` in the response matches the one you stored in your database.

4. **Status is handled correctly** — Your system updates the order based on `status=success`, `status=failure`, or `status=pending`.

You can also confirm transaction status programmatically using the [Verify Payment API](ref:verify_payment_api) — useful if the callback didn't arrive or you want to double-check a specific test result from your server.

***

## Test Webhook Delivery

If you have configured webhooks, verify that your webhook endpoint receives a POST after the test transaction completes. The webhook payload mirrors the callback POST to `surl` / `furl`.

See [Manage Webhooks](https://docs.payu.in/docs/webhook-events-and-sample-payloads) for webhook setup and payload format.

***

## Common Test Failures

**Hash mismatch** — Check parameter order, confirm empty UDF pipes are present, verify you're using test salt not production salt.

**Page not loading** — Ensure `method="post"` in your form and the endpoint is `https://test.payu.in/_payment` (not production).

**Callback not arriving** — Your `surl`/`furl` must be a publicly reachable HTTPS URL. Localhost won't work — use `https://test-payment-middleware.payu.in/simulatorResponse` temporarily.

**Amount format issue** — Always send amount as `10.00` (decimal), not `10` or `₹10`. The hash is built with the exact string you pass.

For a full list, see [Errors and Troubleshooting](../errors-and-troubleshooting).

***

## What's Next

Once all test scenarios pass, go to [Go-live Checklist](./go-live-checklist) to verify you're production-ready.

For the full API reference used in this integration, see [PayU Hosted Checkout APIs](../payu-hosted-checkout-apis).
