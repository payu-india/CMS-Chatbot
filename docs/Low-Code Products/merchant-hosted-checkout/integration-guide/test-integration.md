---
title: Test Integration
excerpt: >-
  Test credentials, payment scenarios, and verification steps for Merchant
  Hosted Checkout.
deprecated: false
hidden: false
next:
  pages: []
metadata:
  title: Test Merchant Hosted Checkout Integration
  description: >-
    Test PayU Merchant Hosted Checkout: net banking login, UPI VPAs, EMI test
    cards, and wallet numbers from the Merchant Hosted test page.
  keywords:
    - payu merchant hosted test integration
    - payu test net banking otp 123456
    - payu upi test vpa anything@payu
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

Use this page to test Merchant Hosted Checkout in the test environment before going live.<br />

Before you test, make sure your integration is built:

<Cards columns="1">
  <Card title="Build Integration" href="./build-integration" icon="fa-code">
    Request parameters, hash generation, HTML form POST, response handling, and server-side verification.
  </Card>
</Cards>

<Callout icon="⚠️" theme="warn">
  ### **Use Test Credentials Only**

  Use the test merchant key and test salt. Never use live credentials in test.
</Callout>

***

## Before You Test

- You are using your **test** merchant key and salt.
- Your form posts to `https://test.payu.in/_payment`.
- Your hash is generated with the test salt.
- Your `surl` and `furl` are URLs PayU can redirect to.

<KeySaltReference />

<Callout icon="⚠️" theme="warn">
  ### **Important:**

  An incorrect hash means the parameters are in the wrong order. The method-page formula is `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT`.
</Callout>

***

## Test Scenarios

### Scenario 1: Successful Payment

<Accordion title="Steps to Test the Successful Payment" icon="fa-circle-check">
  1. Open your payment form.
  2. For net banking, post `pg=TESTPG` and `bankcode=TESTPGNB`.
  3. Enter the test credentials for that method below.
  4. Complete the OTP when the test page asks for one.
  5. Confirm PayU redirects to your `surl`.
  6. Verify the reverse hash on your server.

  **Expected Results:**

  - Success samples show `status=success`
  - Success samples show `error=E000` and `error_Message=No Error`
</Accordion>

### Scenario 2: Failed Payment

<Accordion title="Steps to Test the Failed Payment" icon="fa-xmark">
  The cards failure sample is the failed outcome in this folder.

  **Expected results from that sample:**

  - `status=failure`
  - `unmappedstatus=failed`
  - `error=E1903`
  - `error_Message=Authorization failed at Bank`

  <!-- DOCUMENTATION GAP: The source does not say which test input produces this failure. -->
</Accordion>

### Scenario 3: Customer Abandons Payment

<Accordion title="Steps to Test the Payment Abandoned by the Customer" icon="fa-clock">
  <!-- DOCUMENTATION GAP: The Merchant Hosted pages do not describe what PayU returns if the customer closes the browser. Confirm the payment with Verify Payment if the callback does not arrive. -->
</Accordion>

***

## Test Credentials by a Payment Method

<Accordion title="NetBanking" icon="fa-building-columns">
  | Field | Value |
  | --- | --- |
  | Username | `payu` |
  | Password | `payu` |
  | OTP | `123456` |
</Accordion>

<Accordion title="Debit Card" icon="fa-credit-card">
  <!-- DOCUMENTATION GAP: No plain debit test cards are in the Merchant Hosted test page. These are the EMI debit cards from that page. -->

  | Card | Number | Expiry | CVV | OTP | Mobile |
  | --- | --- | --- | --- | --- | --- |
  | Kotak DC EMI | 4706-1378-0509-9594 | Any future date | 123 | 111111 | 9123412345 |
  | AXIS DC EMI | 4011-5100-0000-0007 | Any future date | 123 | 111111 | 9123412345 |
</Accordion>

<Accordion title="Credit Card" icon="fa-credit-card">
  <!-- DOCUMENTATION GAP: No plain credit test cards are in the Merchant Hosted test page. HDFC and ICICI list the same number. -->

  | Card | Number | Expiry | CVV | OTP | Mobile |
  | --- | --- | --- | --- | --- | --- |
  | HDFC CC EMI | 4453-3410-65876437 | Any future date | 123 | 111111 | 9123412345 |
  | ICICI CC EMI | 4453-3410-65876437 | Any future date | 123 | 111111 | 9123412345 |
</Accordion>

<Accordion title="UPI" icon="fa-mobile-screen">
  Use `anything@payu` or `9999999999@payu.in`.

  <Callout icon="📘" theme="info">
    The legacy test page says UPI in-app and UPI Intent are not available in test mode.
  </Callout>
</Accordion>

<Accordion title="Wallet" icon="fa-wallet">
  | Wallet | Test details |
  | --- | --- |
  | Paytm | Mobile `7777777777`, OTP `888888` |
  | PhonePe | PhonePe pre-prod app |
  | Amazon Pay | Your original Amazon account |
  | Airtel | Wallets page only: use your mobile number |

  Advantage Club has no test environment in the source.
</Accordion>

<Accordion title="BNPL (Buy Now Pay Later)" icon="fa-clock">
  <!-- DOCUMENTATION GAP: The BNPL page only links to other guides. No test phone or sample response is in this folder. -->
</Accordion>

***

## Verify the Test Response

<Accordion title="Reverse Hash Matches" icon="fa-equals">
  Compute `sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)` and compare it with `hash`.
</Accordion>

<Accordion title="Amount Matches" icon="fa-indian-rupee-sign">
  Success samples return `amount`. The source does not say to compare it with your order amount.
</Accordion>

<Accordion title="txnid Matches" icon="fa-fingerprint">
  Response samples include the `txnid` you posted.
</Accordion>

<Accordion title="Status is Handled Correctly" icon="fa-circle-check">
  Success samples use `status=success`. The cards failure sample uses `status=failure`. Pending is not defined in this folder.
</Accordion>

Confirm status with the [Verify Payment API](https://docs.payu.in/reference/verify_payment_api) when the callback does not arrive.

***

## Handle Retries After a Failed Payment

The saved-card text says PayU will not accept a duplicate transaction id. Use a new `txnid` for another attempt.

***

## Test Webhook Delivery

The legacy test steps say to verify that webhooks receive updates. Event names are not in this folder. See [Webhooks](https://docs.payu.in/docs/webhooks).

***

## Sandbox for Testing

- Net banking: https://payu.in/integrationlab/seamless/sm-nb-status
- UPI Collect: https://payu.in/integrationlab/seamless/sm-upiflow

***

## Common Test Failures

<Cards>
  <Card title="Hash Mismatch" icon="fa-not-equal" href="../errors-and-troubleshooting">
    Check that the hash parameters are in the documented order.
  </Card>
  <Card title="Wrong environment" icon="fa-link-slash" href="../errors-and-troubleshooting">
    The key and salt must match test or production.
  </Card>
  <Card title="Method not enabled" icon="fa-ban" href="../errors-and-troubleshooting">
    The method must be enabled on the PayU merchant account.
  </Card>
  <Card title="UPI Intent in test" icon="fa-mobile-screen" href="./build-integration/upi-collect">
    UPI in-app and UPI Intent are not available in test mode.
  </Card>
</Cards>

***

## What's Next

- Go to the [Go-Live Checklist](./go-live-checklist) after the scenarios you can run have passed.
- See [Merchant Hosted Checkout APIs](../merchant-hosted-checkout-apis) for the API list.
