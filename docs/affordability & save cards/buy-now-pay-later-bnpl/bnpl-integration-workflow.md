---
title: BNPL Integration Workflow
deprecated: false
hidden: true
metadata:
  robots: index
---
In a BNPL payment, the customer pays with credit from a BNPL lender instead of a card or bank account. Your application sends the payment request to PayU, the lender authenticates the customer (usually with an OTP), and PayU returns the result to your application.

***

## How Does the Payment Flow Work?

### PayU Hosted Checkout

1. **Initiation:** Your application posts the payment request to PayU and redirects the customer to the PayU checkout page.
2. **Lender selection:** The customer selects **Pay Later**, picks a lender, and enters their mobile number.
3. **Authentication:** The customer enters the lender OTP on PayU's page.
4. **Processing:** PayU sends the transaction to the lender and receives the result.
5. **Return:** PayU redirects the customer to your `surl` or `furl` and posts the payment result.

### Merchant Hosted Checkout

1. **Eligibility check (recommended):** Your server checks which BNPL lenders the customer is eligible for, and you show only those lenders.
2. **Initiation:** Your server posts the payment request with `pg=BNPL` and the lender's `bankcode`.
3. **Authentication:** The lender authenticates the customer in one of two ways:
   - **Redirect:** The customer is redirected to the lender's or PayU's OTP page.
   - **Native OTP (**`txn_s2s_flow=4`**):** PayU returns an `otpPostUrl`. You collect the OTP on your own UI and submit it to that URL. If no `otpPostUrl` is returned, you render the `acsTemplate` (PayU's OTP page) instead.
4. **Return:** PayU returns the final payment result.

### Link and Pay (Merchant Hosted)

1. **Eligibility check:** Your server checks whether the customer is eligible and whether their BNPL account is already linked.
2. **Initiation:** Your server posts the payment request with `txn_s2s_flow=4` and `linkAndPayFlowType=1`.
3. **Authentication:**
   - **First payment, or link no longer valid:** The OTP flow runs (native OTP or fallback page). Once the payment succeeds, the customer's account is linked.
   - **Repeat payment with a valid link:** PayU debits the linked account without an OTP.
4. **Return:** PayU returns the final payment result.

***

## What Happens After the Payment?

| Outcome       | Where you receive it                      | What it means                                                                |
| ------------- | ----------------------------------------- | ---------------------------------------------------------------------------- |
| **Success**   | `surl` / final API response / webhook     | The lender approved the payment (`status=success`, `error=E000`).            |
| **Failure**   | `furl` / final API response / webhook     | The lender declined the payment or authentication failed.                    |
| **Pending**   | Native OTP response (`txnStatus=pending`) | OTP authentication is needed. This isn't a final status.                     |
| **Cancelled** | `furl`                                    | The customer cancelled during the OTP flow (`unmappedstatus=userCancelled`). |

<Callout icon="⚠️" theme="warn">
  ### **Pending Isn't Final**

  In the native OTP flow, the first `_payment` response has `txnStatus=pending`. It means OTP authentication is required. Don't mark the order as failed or paid until you have the final result.
</Callout>

***

## Responsibilities

<Accordion title="What Does PayU Handle?" icon="fa-server">
  - Routing the transaction to the right BNPL lender.
  - Checking eligibility and linking status with the lender.
  - Triggering and validating the lender OTP.
  - Storing the customer's linked BNPL account securely for Link and Pay.
  - Returning the payment result to your callback URLs and webhooks.
</Accordion>

<Accordion title="What Does Your Application Handle?" icon="fa-code">
  - Calling the eligibility API and showing only the lenders the customer is eligible for (Merchant Hosted and Link and Pay).
  - Generating the payment request hash on your server.
  - Collecting and submitting the OTP when you use native OTP.
  - Verifying the response with reverse hashing and confirming the status with the Verify Payment API or webhooks.
  - Updating the order status based on the verified result.
</Accordion>

***

## Key Concepts

<Accordion title="bankcode" icon="fa-building-columns">
  The code of the BNPL lender, for example, `LAZYPAY` or `SIMPL`. Pass it with `pg=BNPL`.
</Accordion>

<Accordion title="user_credentials" icon="fa-id-badge">
  A unique customer identifier in the format `merchantKey:userIdentifier`. Link and Pay uses it to find the customer's linked BNPL account. Keep it consistent for the same customer.
</Accordion>

<Accordion title="payuToken" icon="fa-key">
  A token PayU returns for a linked BNPL account. Pass it in `store_card_token` on repeat Link and Pay payments.
</Accordion>

<Accordion title="referenceId" icon="fa-hashtag">
  An identifier returned in the native OTP `_payment` response. Send it with the OTP when you submit the OTP to `otpPostUrl`.
</Accordion>

<Accordion title="otpPostUrl and acsTemplate" icon="fa-mobile-screen-button">
  - `otpPostUrl`: the URL you submit the customer's OTP to in the native OTP flow.
  - `acsTemplate`: a Base64-encoded HTML page. Decode and render it to send the customer to PayU's OTP page when `otpPostUrl` isn't returned.
</Accordion>

***

## Next Steps

- [BNPL with PayU Hosted Checkout](doc:bnpl-payu-hosted-integration): the fastest way to go live.
- [BNPL with Merchant Hosted Checkout](doc:bnpl-merchant-hosted-integration): full control, with optional native OTP.
- [BNPL Link and Pay](doc:bnpl-link-and-pay-merchant-hosted): one-click repeat checkout.
