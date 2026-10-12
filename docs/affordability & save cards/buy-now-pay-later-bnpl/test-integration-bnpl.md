---
title: Test Integration - BNPL
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

Use this page to test your BNPL integration end to end in the PayU sandbox before you go live.

<Callout icon="⚠️" theme="warn">
  ### **Use Test Credentials Only**

  Everything on this page is for the test environment (`<redacted URL>`). Never use test keys or salts in production, and never use production keys in the test environment.
</Callout>

***

## Before You Test

- You're using your **test** merchant key and salt. See [Generate Test Key and Salt](<redacted URL>).
- BNPL and the lenders you want to test are enabled on your **test** account. For Link and Pay, Link and Pay must be enabled too.
- Your `_payment` URL is `<redacted URL>`.
- Your `surl` and `furl` are publicly reachable HTTPS URLs (not localhost). For initial testing, you can use `https://test-payment-middleware.payu.in/simulatorResponse`.
- The `phone` in the payment request matches the `phone` you used in the eligibility check.

<Callout icon="fad fa-exclamation" theme="error">
  ### **Important:**

  The most common test failure is an incorrect hash. Print the exact string you pass to SHA-512 and check it follows `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT`.
</Callout>

***

## Test Credentials

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Phone number | `9876543210`                                        |
| OTP          | Use the OTP shown or sent in the lender's test flow |
| Lender       | `LAZYPAY` (recommended for Link and Pay testing)    |

{/* REVIEW: Confirm a sandbox OTP value and any lender-specific test numbers (for example, Simpl, HDFC FlexiPay) with Product/QA before publishing. */}

***

## Test Scenarios

### PayU Hosted Checkout

<Accordion title="Scenario 1: Successful BNPL Payment" icon="fa-circle-check">
  1. Post your payment form to `<redacted URL>`.
  2. On the PayU checkout page, select **Pay Later** and choose a lender.
  3. Enter the test phone number and complete OTP authentication.
  4. Check that you're redirected to your `surl`.

  **Expected results:** `status=success`, `unmappedstatus=captured`, `mode=BNPL`, `error=E000`, and the reverse hash matches.
</Accordion>

<Accordion title="Scenario 2: Customer Cancels During OTP" icon="fa-person-running">
  1. Start a BNPL payment on the PayU checkout page.
  2. On the OTP step, cancel or go back.

  **Expected results:** Redirect to `furl`, with `status=failure`, `unmappedstatus=userCancelled`, and `field9=cancelled by user`. The order stays unpaid.
</Accordion>

### Merchant Hosted Checkout

<Accordion title="Scenario 3: Eligibility Check" icon="fa-user-check">
  1. Call the eligibility API with the test phone number and amount.
  2. Check that your UI shows only the eligible lenders.

  **Expected results:** Eligible lenders are shown. Lenders that aren't eligible are hidden or disabled, with the failure reason.
</Accordion>

<Accordion title="Scenario 4: Native OTP — Successful Payment" icon="fa-mobile-screen-button">
  1. Post `_payment` with `pg=BNPL`, `bankcode=LAZYPAY`, and `txn_s2s_flow=4`.
  2. Check that the response has `txnStatus=pending` with `referenceId` and `otpPostUrl`.
  3. Submit the OTP to `otpPostUrl` with `referenceId`.

  **Expected results:** `metaData.statusCode=E000`, `submitOtp.status=success`, and `result.status=success`.
</Accordion>

<Accordion title="Scenario 5: Native OTP — Incorrect OTP" icon="fa-rotate-right">
  1. Repeat Scenario 4, but submit a wrong OTP.
  2. Check that `submitOtp.status=in progress` and `retryAttemptCount` decreases with each wrong attempt.
  3. Submit the correct OTP.

  **Expected results:** The payment succeeds with the same `referenceId`. Your UI shows the attempts left.
</Accordion>

<Accordion title="Scenario 6: Fallback to PayU's OTP Page" icon="fa-window-restore">
  1. When the `_payment` response has no `otpPostUrl`, Base64-decode `acsTemplate` and render it.

  **Expected results:** PayU's OTP page opens. After OTP entry, the result is posted to your `surl` or `furl`.
</Accordion>

<Accordion title="Scenario 7: Payment Failure" icon="fa-vial">
  1. Trigger a lender decline (for example, an amount above the customer's limit).

  **Expected results:** `txnStatus=failed` with a non-`E000` `statusCode` (for example, `E308` or an `E24xx` lender code). The order stays unpaid.
</Accordion>

### Link and Pay

<Accordion title="Scenario 8: First-Time Linking" icon="fa-link">
  1. Call the eligibility API for a customer who isn't linked yet. Check for `isEligible=true` and `isLinked=false`.
  2. Post `_payment` with `txn_s2s_flow=4`, `linkAndPayFlowType=1`, and `user_credentials`.
  3. Complete the OTP step.
  4. Call the eligibility API again.

  **Expected results:** The payment succeeds, and the second eligibility call returns `isLinked=true` with a `payuToken`.
</Accordion>

<Accordion title="Scenario 9: Repeat Payment Without OTP" icon="fa-bolt">
  1. With the same `user_credentials` and `phone`, post `_payment` with `store_card_token=<payuToken>`.

  **Expected results:** You get a final success result without an OTP step.
</Accordion>

<Accordion title="Scenario 10: OTP Fallback on a Repeat Payment" icon="fa-shield-halved">
  1. De-link the account (or use a customer whose link has expired) and post a repeat payment.

  **Expected results:** The response has `txnStatus=pending` with `otpPostUrl` or `acsTemplate`. Your app shows the OTP step instead of failing.
</Accordion>

***

## Verify the Test Response

<Accordion title="Reverse Hash Matches" icon="fad fa-equals">
  Compute `sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)` and check it matches the response `hash`.
</Accordion>

<Accordion title="Amount and txnid Match" icon="fad fa-circle-indian-rupee">
  The `amount` and `txnid` in the response match what you sent and stored.
</Accordion>

<Accordion title="Status Is Handled Correctly" icon="fad fa-list-check">
  Your system treats `pending` (OTP required) as not final, and updates the order only on a verified `success` or `failure`.
</Accordion>

You can also confirm any test result with the [Verify Payment API](ref:verify_payment_api).

***

## Test Webhook Delivery

If you've configured webhooks, check that your endpoint receives a POST after each test transaction. See <Anchor target="_blank" href="<redacted URL>">Manage Webhooks</Anchor>.

***

## Common Test Failures

<Cards>
  <Card title="Hash Mismatch" icon="fad fa-not-equal">
    Check the parameter order and empty UDF pipes, and that you're using the test salt.
  </Card>

  <Card title="BNPL Not Shown" icon="fad fa-eye-slash">
    BNPL or the lender isn't enabled on your test account, or the customer isn't eligible.
  </Card>

  <Card title="Phone Mismatch" icon="fad fa-phone-xmark">
    The `phone` in `_payment` must match the phone you used in the eligibility check.
  </Card>

  <Card title="No otpPostUrl Returned" icon="fad fa-window-restore">
    This is expected in some cases (for example, a first Simpl payment). Render `acsTemplate` instead.
  </Card>
</Cards>

See [BNPL Errors and Troubleshooting](doc:bnpl-errors-and-troubleshooting) for the full list.

***

## What's Next

- When all the scenarios pass, go through the Going Live checklist on your [Merchant Hosted](doc:bnpl-merchant-hosted-integration#going-live-final-checklist) or [Link and Pay](doc:bnpl-link-and-pay-merchant-hosted#going-live-final-checklist) page.
