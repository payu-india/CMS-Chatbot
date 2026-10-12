---
title: Errors and Troubleshooting - BNPL
deprecated: false
hidden: true
metadata:
  robots: index
---
<br />

Something not right with your <Anchor target="_blank" href="<redacted URL>">BNPL integration</Anchor>? Use this page to find the most common issues and how to fix them.

***

## What Do the Lender Error Codes Mean?

<Accordion title="BNPL Error Codes" icon="far fa-triangle-exclamation">
  | PayU Error Code | Meaning                                                       | What to Do                                                                                          |
  | --------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
  | `E2401`         | The customer isn't eligible for this transaction.             | Hide the lender for this customer and offer another payment method.                                 |
  | `E2408`         | The amount is more than the customer's available credit line. | Ask the customer to use a lower amount or another payment method.                                   |
  | `E2415`         | The lender has blocked the customer's account.                | The customer must contact the lender. Offer another payment method.                                 |
  | `E2416`         | One or more mandatory parameters are missing.                 | Check that you sent `firstname`, `lastname`, `email`, `phone`, and the address fields where needed. |
  | `E2417`         | One or more parameters are invalid.                           | Check the email, mobile number, and name formats.                                                   |
  | `E2418`         | The customer's previous bill is overdue.                      | The customer must clear their dues with the lender.                                                 |
  | `E2420`         | The lender has disabled the merchant.                         | Contact your PayU Key Account Manager.                                                              |
  | `E2421`         | Possible fraud risk. The transaction isn't allowed.           | Offer another payment method.                                                                       |
  | `E2422`         | The amount is over the lender's per-transaction limit.        | Lower the amount or offer another payment method.                                                   |
  | `E308`          | The transaction failed at the lender's end.                   | Ask the customer to retry or use another payment method.                                            |
</Accordion>

***

## Why Is the Customer Not Eligible or Not Linked?

<Accordion title="Eligibility and Linking Messages" icon="far fa-user-xmark">
  These messages are returned in `eligibilityFailureReason` / `linkFailureReason`, or as errors from the Link and Pay eligibility API.

  | Message                                                                                | Cause                                                    | Recommended Fix                                                            |
  | -------------------------------------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------- |
  | `Never Linked`                                                                         | The customer hasn't linked this lender yet.              | Run the first-time flow. The customer links the account with an OTP.       |
  | `Token Expired. Relink Required`                                                       | The saved link has expired.                              | Run the OTP flow again. The account is relinked once the payment succeeds. |
  | `No Access Token Available. Relink Required`                                           | The link details are incomplete.                         | Run the OTP flow again.                                                    |
  | `payuToken OR phone is mandatory`                                                      | You sent neither `phone` nor `payuToken`.                | Send at least one.                                                         |
  | `phone must be a valid 10 digit mobile number`                                         | The phone format is invalid.                             | Send a 10-digit number without the country code.                           |
  | `userCredentials not in correct format...`                                             | `userCredentials` isn't in the `string1:string2` format. | Use `merchantKey:userIdentifier`.                                          |
  | `amount cannot be empty` / `userCredentials cannot be empty`                           | A mandatory field is missing.                            | Send `amount` and `userCredentials`.                                       |
  | `The given PayuToken does not match with stored records`                               | The token doesn't belong to this customer.               | Use the `payuToken` returned for this `userCredentials`.                   |
  | `The given BankCode does not match with stored records`                                | `bankCode` doesn't match the linked lender.              | Leave out `bankCode` or pass the linked lender's code.                     |
  | `The given Request does not match with any stored records`                             | Nothing is linked for this `userCredentials`.            | Treat the customer as first-time.                                          |
  | `The given BankCode is inactive on merchant`                                           | The lender isn't enabled on your account.                | Contact your PayU Key Account Manager.                                     |
  | Lender-specific text (for example, `Clear your previous dues on the SIMPL to Proceed`) | The lender declined eligibility.                         | Show the message to the customer and hide the lender.                      |
</Accordion>

***

## Why Isn't My OTP Flow Working?

<Accordion title="Native OTP Issues" icon="far fa-mobile-screen-button">
  | Symptom                                                   | Likely Cause                                                                           | Recommended Fix                                                                                        |
  | --------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
  | You get an HTML redirect instead of JSON                  | `txn_s2s_flow=4` is missing                                                            | Add `txn_s2s_flow=4`. `txn_s2s_flow=2` isn't supported for BNPL.                                       |
  | No `otpPostUrl` in the response                           | Native OTP isn't available for this transaction (for example, the first Simpl payment) | Base64-decode `acsTemplate` and render it.                                                             |
  | Submit OTP returns `in progress` with `retryAttemptCount` | Wrong OTP                                                                              | Ask the customer to re-enter it. Use the same `referenceId`.                                           |
  | Submit OTP fails right away                               | Wrong URL or format                                                                    | POST form-urlencoded `referenceId` and `otp` to the `otpPostUrl` returned. Don't use a hard-coded URL. |
  | `txnStatus=failed` with an empty `result`                 | The lender declined before the OTP step                                                | Read `statusCode` and `message`. Offer another payment method.                                         |
</Accordion>

<Accordion title="Link and Pay Asks for an OTP on a Repeat Payment" icon="far fa-shield-halved">
  This is expected behaviour, not an error. A repeat payment falls back to OTP when the saved link has expired or was de-linked, or when the transaction needs extra verification. Handle the `pending` response the same way as a first-time payment.

  Also check that:

  - `linkAndPayFlowType=1` and `txn_s2s_flow=4` are both sent.
  - `user_credentials` and `phone` exactly match the values used when the account was linked.
  - `store_card_token` has the latest `payuToken` from the eligibility API.
</Accordion>

***

## Lender-Specific Issues

<Accordion title="HDFC FlexiPay" icon="far fa-credit-card">
  - Pass `ccnum` with the customer's eligible credit card number. Without it, the transaction can't start.
  - Use the bank code for the tenure: `HDFCF15`, `HDFCF30`, `HDFCF60`, or `HDFCF90`.
</Accordion>

<Accordion title="Simpl" icon="far fa-link">
  On a customer's first Simpl payment, the customer links their account on Simpl's own page. Render `acsTemplate` for that payment. Later payments behave like other lenders.
</Accordion>

***

## Why Is My Hash Rejected?

<Accordion title="Hash Mismatch" icon="far fa-not-equal">
  - Check the order: `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT`.
  - Keep empty pipes for unused UDFs.
  - Use the salt for the right environment (test or production).
  - Hash the same `amount` string you post (for example, `10.00`).
  - BNPL parameters (`pg`, `bankcode`, `txn_s2s_flow`, `linkAndPayFlowType`, `ccnum`) aren't part of the hash.
</Accordion>

***

## Still Stuck?

Contact PayU Support with these details:

- [x] Your merchant key (never the salt)
- [x] `txnid` and `mihpayid` (if one was created)
- [x] Lender `bankcode`
- [x] The full API response (`metaData` and `result`) or the error code
- [x] Date and time of the issue

Raise a ticket at [PayU Support](https://help.payu.in/raise-ticket) or contact your PayU Key Account Manager.
