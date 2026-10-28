---
title: Domestic Cards Error Details
deprecated: false
hidden: true
metadata:
  robots: index
---
When a domestic card transaction fails, PayU adds an `error_details` object to the transaction response. This object contains:

- A standard PayU error code
- A message for the end user
- A more technical message for the merchant
- The raw gateway error

The `error_details` object is added alongside the existing response fields. PayU still returns `field9` and `error_Message`, so your existing integration keeps working.

On PayU Hosted Checkout, PayU shows `userMessage` on the failure screen automatically.

<Callout icon="far fa-circle-info" theme="info">
  ### **Note:**&#x20;

  The response is always complete. If PayU can't classify an error, it still returns a generic `userMessage` with `newErrorCode` as `NA` and the category as `Unknown`. You don't need to build any fallback logic.
</Callout>

### Sample Response

The following sample shows the `error_details` object for a failed transaction:

```json
"error_details": {
  "step": "authorisationFailure",
  "source": "Risk decline",
  "responsibility": "Issuer",
  "userMessage": "Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours.",
  "merchantMessage": "The bank declined the authorization because they suspected fraudulent activity. Please ask the customer to contact their bank or try a different payment method.",
  "newErrorCode": "EN613",
  "optional": {
    "pgError": "05 | Do not honor",
    "issuerErrorCode": "",
    "apiLayer": ""
  }
}
```

### Field Reference

The following table describes the fields in the `error_details` object and who each field is meant for:

| Field                      | Description                                                                                                       | Audience     |
| :------------------------- | :---------------------------------------------------------------------------------------------------------------- | :----------- |
| `userMessage`              | Curated message for the end user. PayU Hosted Checkout shows it on the failure screen.                            | **End user** |
| `merchantMessage`          | More technical explanation of the failure, with a suggested action, for analysis and support.                     | Merchant     |
| `newErrorCode`             | Standard PayU error code (EN…). `NA` when the error couldn't be classified.                                       | Merchant     |
| `source`                   | Failure category, for example, Risk decline or Business decline. `Unknown` when the error couldn't be classified. | Merchant     |
| `responsibility`           | Where the failure occurred, for example, Issuer.                                                                  | Merchant     |
| `step`                     | Payment stage where the failure happened.                                                                         | Merchant     |
| `optional.pgError`         | Raw gateway or acquirer response code and description.                                                            | Merchant     |
| `optional.issuerErrorCode` | Error code returned by the issuer, when available.                                                                | Merchant     |
| `optional.apiLayer`        | Layer where the failure was raised. `Unknown` when the error couldn't be classified.                              | Merchant     |

> **Important:** Only `userMessage` is meant for end users. All other fields are for merchants only. Do not show them to your customers.

### Error Code Reference

Every failed payment response includes an error code, for example, EN3126.

**Format:** `EN` + Category (1st digit) + Source (2nd digit) + Message number (any length). For example, EN311, EN3126, or EN30505.

#### Category (1st digit)

| Digit | Category                 | What it means                                                                        | Suggested action                                                                |
| :---- | :----------------------- | :----------------------------------------------------------------------------------- | :------------------------------------------------------------------------------ |
| 1     | Customer error           | The customer entered something incorrectly, cancelled, or didn't finish.             | Ask the customer to check their details and try again.                          |
| 2     | Internal technical error | A technical problem on PayU's side.                                                  | Retry. If it keeps happening, contact PayU support.                             |
| 3     | External technical error | A technical problem at the bank, card network, or another partner.                   | Retry, or ask the customer to use another payment method.                       |
| 4     | Configuration error      | Your account or integration isn't set up for this payment.                           | Contact your PayU account manager or PayU support.                              |
| 5     | Business decline         | Declined for a business reason, such as insufficient funds or a limit being reached. | Ask the customer to use another payment method or contact their bank.           |
| 6     | Risk decline             | Declined by the bank or by risk checks for security reasons.                         | Don't retry with the same card. Ask the customer to use another payment method. |
| 0     | Unclassified             | The failure couldn't be categorised.                                                 | Retry. If it keeps happening, contact PayU support.                             |

#### Source (2nd digit)

| Digit | Source      | Where the failure occurred         |
| :---- | :---------- | :--------------------------------- |
| 1     | Issuer      | The customer's bank                |
| 2     | Network     | The card network or payment scheme |
| 3     | Merchant    | Your account or integration setup  |
| 4     | Customer    | The customer's action or input     |
| 5     | PayU        | PayU systems                       |
| 0     | Unspecified | The source couldn't be determined  |

#### Examples

| Code   | Read as                                                             |
| :----- | :------------------------------------------------------------------ |
| EN3126 | External technical error (3) at the customer's bank (1), message 26 |
| EN6145 | Risk decline (6) by the customer's bank (1), message 45             |
| EN4312 | Configuration error (4) in the merchant's setup (3), message 12     |
| EN1408 | Customer error (1) caused by customer input (4), message 8          |

<Callout icon="far fa-circle-info" theme="info">
  ### Notes:

  - **Analytics and reporting:** Group failures by `newErrorCode`, or by its category and source digits, instead of parsing the free text in `field9`.
  - **Triage:** Use the category digit to decide what to do next. For example, 6 (Risk decline) means don't retry with the same card, and 4 (Configuration error) means contact your PayU account manager.
  - **Custom failure pages:** Show only `userMessage` to end users. Never show `merchantMessage` or `pgError`.
  - **Message updates:** PayU updates error messages often to cover new errors in the ecosystem. Make sure any logic you build on this data accounts for these updates.
</Callout>

### Full Error Code List

The full list of error codes maps each `newErrorCode` to its category, source, user message, and merchant description.

### Domestic Cards Error List

| status | field7 | field8 | user_message |
| :--- | :--- | :--- | :--- |
| failed | AUCNEGATIVE | E-Commerce is not enabled for this card | E-Commerce is not enabled for this card. Please enable E-commerce on your bank app and retry the transaction. |
| failed | AUCINVALID | Invalid Otp | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP |
| failed | AUCNEGATIVE | 12 \| Transaction not permitted to cardholder | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHERROR | N/A | Payment could not be processed. Please try again or use a different payment method. |
| failed | AUTHERROR | \| | Payment could not be processed. Please try again or use a different payment method. |
| failed | AUCNEGATIVE | Invalid Otp | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP |
| failed | AUCNEGATIVE | AUTHENTICATION_FAILED\|Encountered a Payer Authentication problem. Payer could not be authenticated. \| CONSUMER_AUTHENTICATION_FAILED | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUCNEGATIVE | 01 \| Card authentication failed | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 12 \| Invalid transaction | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 51 \| Retry the transaction later | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 93 \| Transaction cannot be completed | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 50305 \| Referenced transaction is not in the correct transaction state | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 99993 \| Transaction cannot be completed | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 00 \| \| Failed to process message | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 10024 \| Transaction is in _3ds_start status, cannot authorize | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 30 \| Format Error | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | FSS0001 \| Authentication Not Available | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 87 \| No Envelope Inserted | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 500 \| SYSTEM_ERROR \| Request failed due to system error. | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | N7 \| Customer selected negative file reason | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | T5 \| CAF status = 0 or 9 | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 96 \| System malfunction \| Payment processor error System malfunction | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 96 \| System malfunction, System malfunction or certain field error conditions | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | SCA required under PSD2 | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 96 \| System malfunction | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Initiate Failure | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 90 \| Cut-off in Progress | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Error - General system failure | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 400 \| GENERAL ERROR | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | CM90000 \| Problem occured while validating xml message format | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15400 \| General error | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | GenerateOtp Failure - 96 : SYSTEM ERROR | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | VERIP03 \| UNKNOWN | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | GenerateOtp Failure - 400 : GENERAL ERROR | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 410 \| Error - General system failure | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | NPCI07 \| NPCI07 - Invalid Parameter Value - tranCtx | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Authorise Failure : 400 : General Error | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | VERTKN04 \| UNKNOWN | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15399 \| system unavailable | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | VerifyOTP Failure - 96 : SYSTEM ERROR | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15092 \| no routing available | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Blc\|204 \| Exception occured durinf retry with Enquiry API | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 96 \| SYSTEM ERROR | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 89 \| TID not present on host | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | CTO \| Network Connect Time Out | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | System Error | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 65 \| SCA required under PSD2 | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Authorise Failure : 96 : SYSTEM ERROR | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 2032 \| Error - General system failure | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | NPCI01 \| NPCI01 - Missing Parameter tranCtx | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | VerifyOTP Failure - 400 : General Error | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 86 \| ATM Malfunction | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 10024 \| ALT ID PAN should not be blank or empty | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 10024 \| MRN passed in request is duplicate | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 13 \| Invalid amount | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Invalid Amount | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 12001 \| Invalid AuthenticationValue | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 70013 \| Invalid amount | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | ISSHNM \| Hash Mismatched with Issuer | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | IER \| Internal error | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | IPAY0100159 - External message system error | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | INVALID_REQUEST | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | \| INVALID_REQUEST | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | INVALID_REQUEST \| Invalid credentials. | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Invalid credentials. | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 20 \| Invalid response | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 12001 \| Invalid response | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | INVALID_INPUT \| Invalid request input. Please see details below. | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 155008 \| Verification data failed \| Verification data failed | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 10004 \| Encryption Of Sensitive Information Failed | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_METHOD_ERROR | N/A | Payment could not be completed. Please try again later or use a different payment method. |
| failed | AUCERROR | N/A | A technical error occurred. Please try again or use a different payment method. |
| failed | AUCERROR | \| | A technical error occurred. Please try again or use a different payment method. |
| failed | AUCERROR | 0 \| | A technical error occurred. Please try again or use a different payment method. |
| failed | AUCERROR | E101 | A technical error occurred. Please try again or use a different payment method. |
| failed |  | N/A | Payment failed. Please try again later or use a different payment method. |
| failed | AUCNEGATIVE | SERVER_ERROR\| | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUCNEGATIVE | Session timed out | Session timed out error, Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUCNEGATIVE | N/A | We couldn't verify your payment. Please try again. |
| failed | AUCERROR | AUTHENTICATION_FAILED\|UNKNOWN_ERROR | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUCERROR | 00 \| Authentication Request Successful | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 9107 \| 9107 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | N/A | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 9005 \| 9005 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 9004 \| 9004 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 59 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 13006 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 13004 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 13008 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 5 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 51 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 155009 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 62 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 13007 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 155007 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | N7 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 15120 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 14001 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 155008 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | \| | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 4 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 41 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 91 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 10004 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 61 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 7 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 12008 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 43 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 10024 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 57 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 93 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 12009 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 14 | Payment declined by bank. Please contact your bank or try another card. |
| failed | AUTHNEGATIVE | 19 | Payment declined by bank. Please contact your bank or try another card. |
| failed | REDIRECT | Unable to authorize | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Unable to get payer authentication | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Issuer authentication failure | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Authentication Failed | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | 00 \| Authentication Request Successful | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | 3DSecure authentication failed | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | ECI 1 and ECI6 | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Restricted card | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | 3D Secure authentication failed | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Do not honour | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Transaction not permitted to cardholder | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | ECI 7 | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | DECLINED (fraud) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | DECLINED (cardholder not allowed) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | No checking account | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | 05 \| Do not honor | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | FRAUD - card function blocked | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | DECLINED (restricted card) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | DECLINED (terminal not allowed) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Issuer Compliance | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | 62 \| Restricted card | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Compliance error code for LMM | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | 63 \| Security violation | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | 57 \| Transaction not permitted to issuer/cardholder | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Transactions declined by Issuer based on Risk Score | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | DECLINED (no account) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Suspected fraud | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Failed - Tampered Transaction | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA080\|Internal system error | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA03\|Technical error. Please try again | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA080\|Technical error. Please try again | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA03 \| Technical error. Please try again | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA083\|encrypted_payload_decryption_failed | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | MOF001\| | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA080\|Exceeded configured rate limit for the API, please try again later | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA11\|internal_api_error | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 93 \| Transaction cannot be completed; violation of law \| Transaction cannot be completed; violation of law | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 58 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15407 \| NOT AUTHORIZED ErrMsg details the problem: â€œIP Address is not authorized for User | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 52 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 12001 \| No savings account | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15412 \| AUTHORIZATION_FAILED_BY_BANK | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 36 \| Restricted card | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 80 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 20 \| Invalid response \| Decline - General decline of the card. No other information provided by the issuing bank. | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 3DS212 \| Transaction not permitted to cardholder | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 03 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 58 \| DECLINED (terminal not allowed) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Authorise Failure : 62 : DECLINED (restricted card) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Authorise Failure : CI : Issuer Compliance | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | GW00990 \| Card encryption failed | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 99905 \| Do not honour | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 12008 \| Txn not permitted to acquirer | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 75 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 53 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 72 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 12001 \| Restricted card | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 01 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Authorise Failure : 74 : Transactions declined by Issuer based on Risk Score | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Refer to card issuer | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 06 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15058 \| DECLINED (not terminal) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 96 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 62 \| DECLINED (restricted card) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Authorise Failure : 57 : DECLINED (cardholder not allowed) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15014 \| AUTHORIZATION_FAILED_BY_BANK | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 74 \| Decline - Generic Decline. | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 16011 \| AUTHORIZATION_FAILED_BY_BANK | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 91 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 12001 \| No checking account | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 16012 \| AUTHORIZATION_FAILED_BY_BANK | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Restricted card | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | CA \| Compliance error code for acquirer | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | BANK_DENIED | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 6P \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 16011 \| Compliance error code for issuer | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Authorise Failure : 05 : Do not honour | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15075 \| AUTHORIZATION_FAILED_BY_BANK | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 16010 \| AUTHORIZATION_FAILED_BY_BANK | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 88 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 82 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 58 \| Transaction not allowed at terminal | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 59 \| DECLINED (fraud) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 43 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 06 \| Payment could not be authorised | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 12001 \| Transactions declined by Issuer based on Risk Score | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 57 \| DECLINED (cardholder not allowed) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 74 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 53 \| No savings account | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 16010 \| Compliance error code for acquirer | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 13 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | M6 \| Compliance error code for LMM \| We encountered a problem with Rupay processor: Compliance error code for LMM | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 30 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | DENIED BY RISK | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 36 \| Restricted Card, Retain Card | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 65 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 12001 \| Suspected fraud | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | CA \| Acquirer compliance \| We encountered a problem with Rupay processor: Acquirer compliance | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15012 \| AUTHORIZATION_FAILED_BY_BANK | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | P1 \| Over Daily Limit | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 12 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 34 \| Suspected Fraud—Pick Up | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 07 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 58 \| Transaction not permitted to acquirer/terminal | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 201 \| DAGGDENIED \| Your aggregator or acquirer is not allowing requested service from you at this point in time. | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 99 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 70057 \| Transaction not permitted to cardholder | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 04 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | M6 \| Compliance error code for LMM | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 46 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | CI \| Compliance error code for issuer \| We encountered a problem with Rupay processor: Issuer Compliance | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 70062 \| Restricted card | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 70005 \| Do not honour | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 50716 \| Transaction declined. 3D Secure authentication failed. | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 34 \| Suspected Fraud, Retain Card | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Cancel api failed with response decision as and reason code | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15043 \| transaction declined because card is stolen | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Security violation | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | CI \| Compliance error code for issuer | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 01 \| Refer to card issuer | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 03 \| Invalid Merchant \| Decline - General decline of the card. No other information provided by the issuing bank. | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 78 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 52 \| No Checking Account | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 41 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 61 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 54 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15062 \| restricted card used | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Authorise Failure : CA : Acquirer compliance | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 19 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15062 \| you are using restricted card | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 6P \| AUTHORIZATION_FAILED_BY_BANK \| Account number did not pass a verification check | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Transaction not permitted to cardholder | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 13008 \| Suspected fraud \| Suspected fraud | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15059 \| transaction declined fraud is suspected | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15057 \| transaction declined because you are not the card holder | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 62 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15057 \| DECLINED (not cardholder) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 14 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 57 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 73 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 63 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Authorise Failure : 59 : DECLINED (fraud) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 93 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | N7 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 62 \| Restricted card (for example, in Country Exclusion table) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Do not honour | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 5C \| AUTHORIZATION_FAILED_BY_BANK \| Decline - General decline of the card. No other information provided by the issuing bank. | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 57 \| Transaction not permitted to cardholder | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 05 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 63 \| Security violation | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 155009 \| Transaction cannot be completed - violation of law \| Transaction cannot be completed violation of law | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15093 \| AUTHORIZATION_FAILED_BY_BANK | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 19 \| Re-enter Transaction \| Decline - General decline of the card. No other information provided by the issuing bank. | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15093 \| violation | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 51 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 59 \| Authorisation declined by bank | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 1 \| AUTHORIZATION_FAILED_BY_BANK | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15059 \| fraud suspected | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | DECLINED \| DAGGREJECTED \| Acquirer or another higher control Denies processing of transactions based on Custom Rules Set | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 63 \| Security violation \| Decline - General decline of the card. No other information provided by the issuing bank. | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 57 \| Transaction not permitted to issuer/cardholder | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 62 \| Restricted card \| Decline - General decline of the card. No other information provided by the issuing bank. | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | AUTHORIZATION_FAILED_BY_BANK | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 9G \| AUTHORIZATION_FAILED_BY_BANK \| Decline - Blocked by cardholder/contact cardholder. | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 201 \| DAGGREJECTED \| Acquirer or another higher control Denies processing of transactions based on Custom Rules Set | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 155009 \| Transaction cannot be completed - violation of law | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 93 \| Transaction cannot be completed, violation of law | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15005 \| command not authorized | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 13008 \| Suspected fraud | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | CA \| Acquirer compliance | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 62 \| Restricted card | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 05 \| Do not honour | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 05 \| Do not honor | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 93 \| Transaction cannot be completed; violation of law \| The customer matched the Denied Parties List | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 59 \| Suspected fraud | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 13004 \| Issuer Declined \| Issuer Declined | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 93 \| Transaction cannot be completed; violation of law | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 05 \| Do not honor \| Decline - General decline of the card. No other information provided by the issuing bank. | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 59 \| Suspected fraud \| Decline - General decline of the card. No other information provided by the issuing bank. | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | NPCI412 \| NPCI412 - Issuer Authentication Server failure | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | SERVER_ERROR | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 10004 \| Internal Server Error | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 10004 \| Encryption Of Sensitive Information Failed \| Internal Server Error | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Error - The request was received but there was a server timeout. | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 10004 \| INTERNAL_SERVER_ERROR | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Transaction denied due to BEPG OTP page refresh. | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 92 \| Destination cannot be found for routing | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | \| SERVER_FAILED | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 10004 \| INTERNAL_SERVER_ERROR \| Internal Server Error | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 10024 \| Internal Server Error | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_METHOD_POSITIVE | UNKNOWN_ERROR | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVERROR | 10004 \| INTERNAL_SERVER_ERROR | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVERROR | 10004 \| Internal server error in card info service | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVERROR | 10004 \| Internal Server Error | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVERROR | 15096 \| SYSTEM ERROR or PREVIOUSLY AUTHORIZED or PREVIOUSLY DECLINED | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVERROR | 15093 \| violation | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVERROR | 15056 \| No card so declined | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | EVERROR | 410 \| Invalid BIN | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | EVERROR | 10004 \| Unable to reach card information service | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | EVERROR | 10024 \| Card Information not found | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | EVERROR | 15400 \| general | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVERROR | 15013 \| amount error | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | 101 \| RReq is not available | Transaction failed as the card has expired please use another paymode. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Expired card | Transaction failed as the card has expired please use another paymode. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | ACS response received | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Internal Error | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | 0 \| OTP Generated Successfully | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP |
| failed | REDIRECT | Invalid merchant | This card is not supported on this merchant, please use another card or another paymode. |
| failed | REDIRECT | Rupay transaction error | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Rupay authentication error | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Rupay communication error | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Secure Hash Mismatch | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | INVALID_REQUEST \| Invalid credentials. | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Validation problem | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Invalid amount | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Invalid data was posted to Issuer | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | N:-5014:Validation problem | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | 13 \| Invalid amount | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Session validation failed | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | SYSTEM ERROR | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | 101 \| CRes is not available | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | General Error | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | 96 \| System malfunction | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | NO ROUTING AVAILABLE | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Lost card | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | REDIRECT | DECLINED (stolen) | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | REDIRECT | DECLINED (lost card) | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | REDIRECT | Pick-up | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | REDIRECT | 04 \| Pick Up Card | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | REDIRECT | Processing error while provisioning Guest Checkout Token | Wrong Expiry date/CVV entered, please recheck and try again. |
| failed | REDIRECT | Issuer not available | Transaction failed due to bank server error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Issuer or switch is inoperative | Transaction failed due to bank server error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | 91 \| Issuer unavailable or switch inoperative | Transaction failed due to bank server error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | DECLINED (Exceeds withdrawal amount limit) | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | REDIRECT | Exceeds withdrawal frequency limit | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | REDIRECT | 61 \| Exceeds withdrawal amount limit(s) / Withdrawal amount limit exc | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | REDIRECT | Allowable number of PIN tries exceeded | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | REDIRECT | 65 \| Exceeds withdrawal count limit / Withdrawal count limit exceeded | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | REDIRECT | Invalid account | No account found for this card. You can retry on another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | 42 \| No Universal Account | No account found for this card. You can retry on another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | User Pressed cancel button | Session timed out error, Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | User was Inactive | Session timed out error, Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Invalid card number (no such number) | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | REDIRECT | Rupay check bin error | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | REDIRECT | No card record | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | REDIRECT | Unable to verify card enrollment | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | REDIRECT | Invalid BIN | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | REDIRECT | DECLINED (exceeds frequency) | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | REDIRECT | Incorrect personal identification number | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | REDIRECT | 14 \| Invalid card number | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | REDIRECT | Mobile number record not found/ mis-match | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | REDIRECT | NON SUFFICIENT FUNDS | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |
| failed | REDIRECT | 51 \| Insufficient funds/over credit limit / Not sufficient funds | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |
| failed | EVNEGATIVE | NOT_ENROLLED_FAILURE | This card is currently not supported by your card network. Please use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | 07 \| Pickup Card | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | EVNEGATIVE | 905 \| Expired card | Transaction failed as the card has expired please use another paymode. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | 402 \| Transaction timed-out. | Session timed out error, Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | 10004 \| Something went wrong in generate otp request | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP |
| failed | EVNEGATIVE | 10004 \| Invalid response from npci | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | 10004 \| Could not get the proper response from NPCI | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | 10004 \| Timed out at NPCI | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | IR \| InValid Response Parameter from NPCI | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | DOI \| Validation Error-Duplicate Order Id Received | This payment was already processed. If charged twice, money will be refunded within 48 hours. |
| failed | EVNEGATIVE | 454 \| Duplicate requestID | This payment was already processed. If charged twice, money will be refunded within 48 hours. |
| failed | EVNEGATIVE | 93 \| Ecommerce Not Enabled | E-Commerce not enable for this card. Please enable E-commerce on your bank app and retry the transaction. |
| failed | EVNEGATIVE | INVALID_REQUEST \| Invalid credentials. | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | ERROR \| Error - General system failure | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | 400 \| GENERAL ERROR | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | 96 \| SYSTEM ERROR | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | 96 \| Issuer System Failure | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | 10024 \| MRN passed in request is duplicate | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | IER \| Unknown Host | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | RTO \| Network Read Time Out | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | CTO \| Network Connect Time Out | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | 405 \| System connection failure. | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | 413 \| INVALID CVD2 | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | EVNEGATIVE | 10024 \| Bad cvd2 passed! | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | EVNEGATIVE | 2032 \| Invalid tavv value | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | EVNEGATIVE | Invalid association id passed in request | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | EVNEGATIVE | 10024 \| Merchant is not active | This card is not supported on this merchant, please use another card or another paymode. |
| failed | EVNEGATIVE | VERMCC04 \| Validation Error-MCC MisMatched | This card is not supported on this merchant, please use another card or another paymode. |
| failed | EVNEGATIVE | BNF \| Bin Not Found | This card is not supported on this merchant, please use another card or another paymode. |
| failed | EVNEGATIVE | 10024 \| This Card type is not allowed !! | This card is not supported on this merchant, please use another card or another paymode. |
| failed | EVNEGATIVE | 10004 \| INTERNAL_SERVER_ERROR | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | ERROR \| Error - The request was received but there was a server timeout. | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | 922 \| ACS technical issue | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | 10004 \| Internal server error in card info service | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | Payment failed during authorisation (Switch) due to an internal server error | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | ERROR \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | VERCARDGC \| | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | REJECT \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | 101 \| Message not recognised | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | VERCARDT03 \| | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | 56 \| DECLINED (no card) | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | EVNEGATIVE | 10004 \| Unable to reach card information service | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | EVNEGATIVE | 908 \| No Card record | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | EVNEGATIVE | 56 \| | Payment failed due to a technical issue. Please try again or use a different payment method. |
| failed | EVNEGATIVE | N/A | Payment failed due to a technical issue. Please try again or use a different payment method. |
| failed | EVNEGATIVE | 2032 \| | Payment failed due to a technical issue. Please try again or use a different payment method. |
| failed | EVNEGATIVE | 408 \| | Payment failed due to a technical issue. Please try again or use a different payment method. |
| failed | EVNEGATIVE | 412 \| Transaction got declined at issuer. | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVNEGATIVE | 912 \| Transaction not permitted to cardholder | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Session validation failed | This card is not supported on this merchant, please use another card or another paymode. |
| failed |  | Invalid merchant | This card is not supported on this merchant, please use another card or another paymode. |
| failed |  | order currently being processed | This card is not supported on this merchant, please use another card or another paymode. |
| failed |  | 922 \| ACS technical issue | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 914 \| Transaction timed out at the ACS | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 402 \| CReq message with this ACS Transaction ID has already been received and processed. | This payment was already processed. If charged twice, money will be refunded within 48 hours. |
| failed |  | 42 \| No Universal Account | No account found for this card. You can retry on another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 46 \| Closed account | No account found for this card. You can retry on another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 70 \| PIN data required | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP |
| failed |  | Transaction Completed | Transaction Succesful |
| failed | REDIRECT | Retry the transaction later | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Bad Track Data | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Check for New information before retry | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | General exception | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | UNKNOWN_ERROR | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Communication Error | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Format error | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | No security module | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Application error | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | ERROR | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | REDIRECT | Store is not open | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | EVERROR | 15001 \| Some parameters are missing. Please contact merchant | This card is not supported on this merchant, please use another card or another paymode. |
| failed |  | N:-5014:Validation problem | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | DV call failed: Invalid Transaction | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | NO ROUTING AVAILABLE | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Validation problem | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Invalid data was posted to Issuer | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Invalid amount | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 13 \| Invalid amount | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Transaction cannot be completed | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 12 \| Invalid transaction | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Secure Hash Mismatch | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 101 \| CRes is not available | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | SYSTEM ERROR | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 96 \| System malfunction | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | N:-BEPG-0000017:Issuer authentication failure | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 3DSecure authentication failed | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | ?:waiting authentication | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Issuer authentication failure | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Unable to get payer authentication | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Authentication Failed | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Unable to authorize | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 901 \| Card authentication failed | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | N:51:NON SUFFICIENT FUNDS | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |
| failed |  | NON SUFFICIENT FUNDS | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |
| failed |  | 51 \| Insufficient funds/over credit limit / Not sufficient funds | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |
| failed |  | SYSTEM UNAVALIABLE | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Application error | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 907 \| Invalid transaction | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Format error | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Bad Track Data | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Invalid transaction | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | UNKNOWN_ERROR | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Retry the transaction later | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Check for New information before retry | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | General exception | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Communication Error | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 30 \| Format error | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 43 \| Stolen Card - Pick Up | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed |  | DECLINED (stolen) | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed |  | Pick-up | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed |  | DECLINED (lost card) | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed |  | 04 \| Pick Up Card | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed |  | 41 \| Lost Card - Pick Up | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed |  | Invalid BIN | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed |  | 14 \| Invalid card number | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed |  | Invalid card number (no such number) | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed |  | Rupay check bin error | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed |  | Unable to verify card enrollment | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed |  | 908 \| No Card record | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed |  | DECLINED (exceeds frequency) | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed |  | No card record | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed |  | Transaction timed out | Session timed out error, Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | User Pressed cancel button | Session timed out error, Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | User was Inactive | Session timed out error, Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Issuer or switch is inoperative | Transaction failed due to bank server error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Issuer not available | Transaction failed due to bank server error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 54 \| Expired card | Transaction failed as the card has expired please use another paymode. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | EXPIRED CARD | Transaction failed as the card has expired please use another paymode. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 101 \| RReq is not available | Transaction failed as the card has expired please use another paymode. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Failed - Tampered Transaction | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 3D Secure authentication failed | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Do not honour | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Restricted card | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Transaction not permitted to cardholder | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | DECLINED (fraud) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 05 \| Do not honor | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | DECLINED (cardholder not allowed) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | ECI 7 | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | DECLINED (restricted card) | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Issuer Compliance | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 63 \| Security violation | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 57 \| Transaction not permitted to issuer/cardholder | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 62 \| Restricted card | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Compliance error code for LMM | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | No checking account | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Suspected fraud | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 01 \| Refer to card issuer | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | ECI 1 and ECI6 | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA086\|Not a mastercard or maestro | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | UNKNOWN_ERROR | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | MOF001\|City name is invalid | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA080\|GENERIC_ERROR | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA080\|400 | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA080\|I9001 | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA080\|P9001 | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA080\|I0001 | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA081\|Invalid / Missing Field :: card expiry | Transaction failed as the card has expired please use another paymode. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA080\|cardType is not supported :: cardType | This card is not supported on this merchant, please use another card or another paymode. |
| failed | ALT_ID_PROV_ERROR | EA09\|Invalid merchant ID configuration. Please reachout to PayU support team | This card is not supported on this merchant, please use another card or another paymode. |
| failed | ALT_ID_PROV_ERROR | EA04\|Invalid merchant ID configuration. Please reachout to PayU support team | This card is not supported on this merchant, please use another card or another paymode. |
| failed | ALT_ID_PROV_ERROR | EA081\|card_not_eligible | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | ALT_ID_PROV_ERROR | EA06\|AUTHREFNO_INVALID | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 - 72 hours. |
| failed | ALT_ID_PROV_ERROR | EA084\|Card can currently not be used with issuer for tokenization | The card used cannot be saved currently due to bank's rules. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA080\|Tokenization failed | The card used cannot be saved currently due to bank's rules. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA088\|Card can currently not be used with card association for tokenization | The card used cannot be saved currently due to bank's rules. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA080\|card_market_not_supported | The card used cannot be saved currently due to bank's rules. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA084\|PAN Ineligible | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA081\|The network token provision request contained data that could not be verified | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | ALT_ID_PROV_ERROR | EA081\|One or more fields in the request are either missing or does not have correct value. | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | ALT_ID_PROV_ERROR | EA087\|Invalid body values | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | ALT_ID_PROV_ERROR | EA087\|INVALID_VALUE | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | ALT_ID_PROV_ERROR | EA11\|The network token service was unavailable or timed out | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | ALT_ID_PROV_ERROR | EA022\|Expiry year is Invalid. Please check and initiate again | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUCNEGATIVE | UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | 919 \| Exceeds ACS maximum challenges | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP. |
| failed |  | DECLINED (Exceeds withdrawal amount limit) | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed |  | Exceeds withdrawal frequency limit | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed |  | 61 \| Exceeds withdrawal amount limit(s) / Withdrawal amount limit exc | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed |  | 65 \| Exceeds withdrawal count limit / Withdrawal count limit exceeded | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed |  | Allowable number of PIN tries exceeded | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | 3DS_METHOD_NEGATIVE | INVALID_REQUEST \| Value '&lt;transaction ID&gt;.auth' is invalid. There is already an authentication outcome associated with the supplied transaction ID. To perform another authentication on the order, provide a new transaction ID. | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | TRANSACTION_INVALID | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | 101 \| CRes is not available | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | AUTHENTICATION_INVALID_REQUEST_ERROR | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | 908 \| No Card record | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | 3DS_CHALLENGE_NEGATIVE | UNKNOWN_ERROR | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | AUTHENTICATION_FAILED \| Cardholder did not complete authentication \| Cardholder selected Cancel | Transaction has been cancelled by the user, Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | AUTHENTICATION_FAILED \| Cardholder did not complete authentication | Transaction has been cancelled by the user, Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | AUTHENTICATION_FAILED \| Cardholder did not complete authentication \| Transaction Error | Transaction has been cancelled by the user, Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | DO_NOT_PROCEED | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | 901 \| Blc\|Not Authenticated /Account Not Verified; Transaction denied | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | 914 \| Blc\|Not Authenticated /Account Not Verified; Transaction denied | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | 908 \| Blc\|Not Authenticated /Account Not Verified; Transaction denied | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | 402 \| Blc\|Not Authenticated /Account Not Verified; Transaction denied | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | 101 \| Blc\|Not Authenticated /Account Not Verified; Transaction denied | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | 919 \| Blc\|Not Authenticated /Account Not Verified; Transaction denied | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | 912 \| Transaction not permitted to cardholder | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | AUTHENTICATION_FAILED \| Issuer unable to perform authentication | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | 914 \| Transaction timed out at the ACS | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | SERVER_ERROR | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | 901 \| Card authentication failed | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | SECURE_3D_AUTHENTICATION_ERROR | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_VERIFICATION_NEGATIVE | Expired card | Transaction failed as the card has expired please use another paymode. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_VERIFICATION_NEGATIVE | RREQ_NOT_RECEIVED | Transaction failed as the card has expired please use another paymode. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_VERIFICATION_NEGATIVE | 0 | Payment verification failed. Please try again. |
| failed | 3DS_VERIFICATION_NEGATIVE | Transaction timed out at the ACS | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_VERIFICATION_NEGATIVE | System Error response from ACS | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_VERIFICATION_NEGATIVE | Exceeds ACS maximum challenges | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP. |
| failed | 3DS_VERIFICATION_NEGATIVE | No Card Record | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | 3DS_VERIFICATION_NEGATIVE | Invalid card number | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | 3DS_VERIFICATION_NEGATIVE | Card authentication failed | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_VERIFICATION_NEGATIVE | AUTHENTICATION_FAILED \| 01 \| Card authentication failed | User authentication failed due to a technical error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Rupay transaction error | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Rupay authentication error | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Rupay communication error | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed |  | Processing error while provisioning Guest Checkout Token | Wrong Expiry date/CVV entered, please recheck and try again. |
| failed | AUCNEGATIVE | INVALID_REQUEST \| Value '&lt;transaction ID&gt;.auth' is invalid. A transaction with this transaction ID has already been processed but the request parameters do not match. To process a new transaction for this order, the transaction.id must be unique for the order. | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUCNEGATIVE | INVALID_REQUEST \| Value '&lt;transaction ID&gt;...&lt;transaction ID&gt;' is invalid. A transaction with this transaction ID has already been processed but the request parameters do not match. To process a new transaction for this order, the transaction.id must be unique for the | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUCNEGATIVE | INVALID_REQUEST \| Value '&lt;transaction ID&gt;.auth' is invalid. A transaction with this transaction ID has already been processed but the request parameters do not match. To process a new transaction for this order, the transaction.id must be unique for the order. | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUCNEGATIVE | INVALID_REQUEST \| Value '&lt;transaction ID&gt;...&lt;transaction ID&gt;' is invalid. A transaction with this transaction ID has already been processed but the request parameters do not match. To process a new transaction for this order, the transaction.id must be unique for the | Transaction failed due to a technical issue. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA086\|Action cannot be performed as the payment-credential request for the token was declined | Transaction declined due to Wrong CVV or expiry. Please retry with correct card details or use another paymode. |
| failed | ALT_ID_PROV_ERROR | EA089\|Request not permitted | Transaction declined due to Wrong CVV or expiry. Please retry with correct card details or use another paymode. |
| failed | ALT_ID_PROV_ERROR | EA080\|API is currently not available, please try again later | Transaction failed due to technical issues. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA11\|Service unavailable. Typically the server not able to serve the request temporarily. Retry after sometime. | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA085\|Issuer did not respond in time. Retry the request. | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA085\|issuer_not_supported | Bank server is down. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | ALT_ID_PROV_ERROR | EA087\|invalid_crypto_response | Transaction failed due to some technical issues. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_VERIFICATION_NEGATIVE | Transaction not permitted to cardholder | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_VERIFICATION_NEGATIVE | Low confidence | Transaction failed as bank suspected fraud. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_VERIFICATION_NEGATIVE | Cardholder not enrolled in service | This card is currently not supported by your card network. Please use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_VERIFICATION_NEGATIVE | E303 \| SUCCESS | Transaction Succesful |
| failed | 3DS_VERIFICATION_NEGATIVE | UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | 101 \| RReq is not available | Transaction failed as the card has expired please use another paymode. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | 3DS_CHALLENGE_NEGATIVE | 919 \| Exceeds ACS maximum challenges | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP. |
| failed | AUTHNEGATIVE | NPCI56 \| NPCI56 - DECLINED (no card) | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 410 \| AUTHORIZATION_FAILED_BY_BANK \| We encountered a problem with Rupay processor: Invalid BIN | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 14 \| Invalid card number \| Decline - Invalid account number | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 14 \| Invalid card number | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 78 \| Invalid/nonexistent account specified (general) \| Decline - General decline of the card. No other information provided by the issuing bank. | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 46 \| Closed account \| Decline - Inactive card or card not authorized for card-not-present transactions. | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 56 \| No Card Record | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | Invalid Input Parameter For Guest Checkout Transaction \| UNKNOWN | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | Invalid card number | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 10024 \| Couldn't verify the card, card number seems to be invalid \| Bad Input Data in Request | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 15041 \| transaction declined because card is lost | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 55 \| Invalid PIN \| Decline - Inactive card or card not authorized for card-not-present transactions. | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 52 \| No Checking Account \| Decline - Invalid account number | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 14 \| Invalid card number (no such number) | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 55 \| Invalid PIN | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 15065 \| exceeded frequency | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | PAN Ineligible | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 70014 \| Invalid card number (no such number) | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | GW00881 \| Invalid card holder name | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 15014 \| card number is wrong | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 70056 \| No card record | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 15410 \| invalid bin or error with check bin | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 12001 \| Mobile number record not found/ mis-match | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 42 \| No Universal Account \| Decline - General decline of the card. No other information provided by the issuing bank. | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | Authorise Failure : 54 : EXPIRED CARD | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | CheckBinFailure - 410:Invalid BIN | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | GW00852 \| Invalid card number | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 69 \| Mobile number record not found / mis-match \| Decline - General decline of the card. No other information provided by the issuing bank. | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 15 \| No such issuer | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 412 \| Invalid BIN | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 50655 \| Unable to verify card enrollment | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 56 \| No Card Record \| Decline - Invalid account number | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 65 \| DECLINED (exceeds frequency) | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | INVALID_PIN | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 410 \| Invalid BIN | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 69 \| Mobile number record not found / mis-match | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 15056 \| No card so declined | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 10024 \| Invalid Pan | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | 12001 \| No such issuer | The card details entered were incorrect. Please re-enter correct card details and try again. |
| failed | AUTHNEGATIVE | NPCI96 \| NPCI96 - SYSTEM ERROR | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | IPAY0100357 \| IPAY0100357-Transaction declined due to OTP Page refreshed. | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | NPCI400 \| NPCI400 - GENERAL ERROR | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 96 \| System malfunction \| We encountered a problem with Rupay processor: SYSTEM ERROR | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | IPAY0100126 - Brand not enabled. | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 13 \| Invalid amount \| We encountered a problem with Rupay processor: Amount Error | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | IPAY0100120 - Transaction denied due to invalid payment instrument for brand data. | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | IPAY0200301 \| IPAY0200301-Invalid transaction details | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 400 \| GENERAL ERROR \| We encountered a problem with Rupay processor: GENERAL ERROR | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 58 \| Transaction not permitted to acquirer/terminal \| We encountered a problem with Rupay processor: DECLINED (terminal not allowed) | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 10004 \| Could not get the proper response from NPCI | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | IPAY0100189 - Transaction denied due to brand directory unavailable | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | rupay response Timeout | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 412 \| Invalid BIN \| We encountered a problem with Rupay processor: Issuer Authentication Server failure | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 399 \| SYSTEM UNAVALIABLE \| We encountered a problem with Rupay processor: SYSTEM UNAVALIABLE | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | IPAY0100293 \| Transaction denied due to duplicate Merchant trackid | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 96 \| System malfunction \| We encountered a problem with Rupay processor: Session expired for this transaction | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 2032 \| AUTHORIZATION_FAILED_BY_BANK \| We encountered a problem with Rupay processor: Invalid tavv value | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 96 \| System malfunction \| We encountered a problem with Rupay processor: PREVIOUSLY AUTHORIZED | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 00 \| \| Payment processor error (100004) General System Error | Transaction Failed due to technical error from the card scheme. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 61 \| Exceeds withdrawal amount limit(s) / Withdrawal amount limit exc \| Decline - The card has reached the credit limit. | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | 61 \| Exceeds withdrawal amount limit(s) / Withdrawal amount limit exc | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | 65 \| Exceeds withdrawal count limit / Withdrawal count limit exceeded \| Allowable number of PIN entry tries exceeded. | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | 61 \| Activity amount limit exceeded | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | 13 \| Invalid amount \| Invalid amt or Currency conversion field overflow | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | 15061 \| DECLINED (exceeds with) | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | 13 \| Invalid amount (currency conversion field overflow) or amount exceeds maximum for card program | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | 15061 \| DECLINED (Exceeds withdrawal amount limit) | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | 65 \| Exceeds withdrawal count limit / Withdrawal count limit exceeded | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | 65 \| Activity count limit exceeded | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | 75 \| Allowable number of PIN tries exceeded | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | 61 \| DECLINED (Exceeds withdrawal amount limit) | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | Authorise Failure : 61 : DECLINED (Exceeds withdrawal amount limit) | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | Exceeds withdrawal amount limits | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | 15075 \| pin exceeded | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | 16012 \| Amount limit exceeded by merchant bank | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | 65 \| Exceeds withdrawal frequency limit | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | N4 \| Maximum off-line refund reached \| Decline - The card has reached the credit limit. | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | 70065 \| Exceeds withdrawal frequency limit | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | Allowable number of PIN tries exceeded | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | T7 \| Cash back exceeds daily limit | Amount limit has been reached. Please contact your bank, increase the limit or use another paymode. |
| failed | AUTHNEGATIVE | 57 \| Transaction not permitted to issuer/cardholder \| Decline - Inactive card or card not authorized for card-not-present transactions. | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 41 \| Lost Card - Pick Up \| Decline - Stolen or lost card. | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 12 \| Invalid transaction \| Decline - Inactive card or card not authorized for card-not-present transactions. | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 04 \| Pick Up Card \| Decline - Stolen or lost card. | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 07 \| Pick Up Card, Special Conditions \| Decline - Stolen or lost card. | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 41 \| Lost Card - Pick Up | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 43 \| Stolen Card - Pick Up \| Decline - Stolen or lost card. | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 04 \| Pick Up Card | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 04 \| Pick Up Card \| We encountered a problem with Rupay processor: Pick-up | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 41 \| Pickup card (lost card) | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 43 \| Stolen Card - Pick Up | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 04 \| Pickup card | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 15043 \| DECLINED (stolen) | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 07 \| Pickup card, special condition (other than lost/stolen card) | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 12001 \| Pick-up | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | Pick up card | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 43 \| Pickup card (stolen card) | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 15041 \| DECLINED(lost card) | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | Lost Card | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 36 \| Restricted Card—Pick Up | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 70041 \| Lost card | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 41 \| Lost card | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 07 \| Pick Up Card, Special Conditions | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | Stolen Card, Pick up | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 60 \| Contact Card Acquirer | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 43 \| DECLINED (stolen) | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 04 \| Pick-up | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 41 \| DECLINED (lost card) | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | Authorise Failure : 43 : DECLINED (stolen) | Card has been reported as stolen/lost. Please contact your bank and unblock your card or retry using another paymode. |
| failed | AUTHNEGATIVE | 12 \| Invalid transaction \| Decline - General decline of the card. No other information provided by the issuing bank. | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 30 \| Format error \| Decline - General decline of the card. No other information provided by the issuing bank. | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 58 \| Transaction not permitted to acquirer/terminal \| Decline - Inactive card or card not authorized for card-not-present transactions. | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | GV00013 \| Invalid payment id | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 10024 \| Couldn't verify the card, card number seems to be invalid | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 5002 \| The merchant is not setup to support the requested service. | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | P9 \| Enter lesser amount | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 03 \| Invalid Merchant | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 15096 \| system error/ PREVIOUSLY AUTHORIZED /PREVIOUSLY DECLINED | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 03 \| Invalid merchant or service provider | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 15096 \| SYSTEM ERROR or PREVIOUSLY AUTHORIZED or PREVIOUSLY DECLINED | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 001 \| Shop is in REFUND_ONLY mode. Transactions are not allowed. | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | FSS00003 \| Only Debit Card Allowed | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 5102 \| Transaction failed. ECI-7 transactions are not supported by merchant. | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 10024 \| This Card type is not allowed !! | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | Account Not Yet Activated | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 5111 \| Transaction failed. ECI1 and ECI6 transactions are not supported by merchant. | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | L3 \| International Acceptance not enabled | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 15001 \| Some parameters are missing. Please check / contact the merchant | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 10024 \| Invalid Merchant Id | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 92 \| Destination cannot be found for routing / Unable to route transa \| Payment processor error Receiving institution ID is invalid | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 10024 \| Invalid Merchant Id \| Bad Input Data in Request | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | VERMCC04 \| Validation Error-MCC MisMatched | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | Warning: 490 Missing or Invalid Merchant Category Code | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | GW00160 \| Brand not enabled | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 001 \| Shop does not exist | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | FSS00003 \| FSS00003-Only Debit Card Allowed. | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | IPAY0100207 - Bin range not enabled | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 92 \| Destination cannot be found for routing / Unable to route transa \| We encountered a problem with Rupay processor: NO ROUTING AVAILABLE | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 70003 \| Invalid merchant | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | Blc\|204 \| Response unknown - Missing parameter. Transaction source must be INTERNET or MERCHANT for payments using a scheme token. | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | BNF \| Bin Not Found | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | Blc\|204 \| Transaction failed. Please try again later. | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 30 \| Format error \| Payment processor error System malfunction | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | CANCELED | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | T1 \| Payment Gateway timed out | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | ACCU200: Canceled by User | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | INVALID_REQUEST \| Value 'PAY' is invalid. Pay request not permitted for this merchant. | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 10024 \| This Card type is not allowed !! \| Bad Input Data in Request | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 74 \| AUTHORIZATION_FAILED_BY_BANK \| Decline - Generic Decline. | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 53 \| No Savings Account \| Payment processor error No savings account | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 78 \| ’Blocked, first used’—The transaction is from a new cardholder, and the card has not been properly unblocked. | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 13004 \| Issuer Declined | This card is not supported on this merchant, please use another card or another paymode. |
| failed | AUTHNEGATIVE | 54 \| Expired card \| Decline - Expired card. You might also receive this if the expiration date you provided does not match the date the issuing bank has on file. | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | N7 \| Negative online CAM, dCVV, iCVV, CVV, or CAVV results or Offline \| Decline - Invalid Card Verification Number (CVN). | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | 13007 \| INVALID CVV2 | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | 13007 \| INVALID CVV2 \| INVALID CVV2 | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | 62 \| Restricted card \| Decline - Invalid Card Verification Number (CVN). | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | N7 \| Negative online CAM, dCVV, iCVV, CVV, or CAVV results or Offline | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | NPCI413 \| NPCI413 - INVALID CVD2 | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | 82 \| Negative online CAM, dCVV, iCVV, CVV, or CAVV results or Offlin \| Decline - Invalid Card Verification Number (CVN). | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | GenerateOtp Failure - 56 : DECLINED (no card) | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | 82 \| Negative CAM, dCVV, iCVV, or CVV results | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | 82 \| Negative online CAM, dCVV, iCVV, CVV, or CAVV results or Offlin | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | DECLINED \| EXPIRED_CARD \| Decline - Expired card. You might also receive this if the expiration date you provided does not match the date the issuing bank has on file. | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | DUE \| CardVerificationFailed- Invalid card number / CVV / expiry date | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | 10024 \| Bad Expiry Year passed! \| Bad Input Data in Request | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | 10024 \| Bad Expiry Date passed! | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | 12001 \| DECLINED (Invalid CAVV) | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | CardVerificationFailed- Invalid card number / CVV / expiry date | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | Blc\|102 \| Blc\|CVV/CVV2 is invalid. Please check and try again. | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | IPAY0100073 - Transaction denied due to invalid CVV. | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | NPCI07 \| NPCI07 - Invalid Parameter Value - card_cvd | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | GW00856 \| Invalid cvv | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | NPCI408 \| NPCI408 - XML Data Error - Invalid Parameter Value - cvd2 | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | 12001 \| Missing Parameter cvd2 | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | 10024 \| Bad CVV2 passed! | Wrong Expiry date/CVV entered, please recheck and try again |
| failed | AUTHNEGATIVE | NPCI453 \| NPCI453 - Exhausted OTP resend count | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP. |
| failed | AUTHNEGATIVE | NPCI452 \| NPCI452 - Exhausted OTP verification | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP. |
| failed | AUTHNEGATIVE | NPCI451 \| NPCI451 - EXPIRED OTP | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP. |
| failed | AUTHNEGATIVE | 75 \| Allowable number of PIN tries exceeded \| Decline - Inactive card or card not authorized for card-not-present transactions. | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP. |
| failed | AUTHNEGATIVE | 75 \| Allowable number of PIN tries exceeded \| Allowable number of PIN entry tries exceeded. | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP. |
| failed | AUTHNEGATIVE | 75 \| Allowable number of PIN-entry tries exceeded | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP. |
| failed | AUTHNEGATIVE | Authorise Failure : 75 : Allowable number of PIN tries exceeded | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP. |
| failed | AUTHNEGATIVE | 81 \| Cryptographic Error \| Cryptographic error found in PIN | Transaction failed due to some technical issues. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 10024 \| Not a token card txn but cryptogram is sent in request | Transaction failed due to some technical issues. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 10024 \| Cryptogram should not be null or blank | Transaction failed due to some technical issues. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Cryptogram Expired \| UNKNOWN | Transaction failed due to some technical issues. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 10024 \| Cryptogram should not be null or blank \| Bad Input Data in Request | Transaction failed due to some technical issues. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 002 \| Invalid or missing token cryptogram | Transaction failed due to some technical issues. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | IPAY0200085 \| IPAY0200085-Checkbin Failure | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Blc\| \| Blc\| | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Declined - One or more fields in the request contains invalid da | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | ITO \| Late Authorization Request | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Checkbin Failure | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Blc\|0 \| Blc\|SUCCESS | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Invalid Transaction | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Blc\|399 \| Blc\| | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 70012 \| Invalid transaction | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | INVALID_REQUEST \| Unexpected failure | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Authorise Failure : 91 : Issuer not available | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Value 'PAY' is invalid. Pay request not permitted for this merchant. | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 001 \| Field [amount] with value &lt;amount&gt; has been rejected. Cause: Amount should be numeric and at least 100 | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 0494 \| AUTHORIZATION_FAILED_BY_BANK \| Declined - One or more fields in the request contains invalid data. | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 9G \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 70087 \| Bad Track Data | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 19 \| Re-enter transaction | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | K \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | T8 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | J \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | H \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 30 \| Format error | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | DECAUTH \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | GW00555 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 5C \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 70051 \| Retry the transaction later | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Q1 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | PY20014 \| Invalid user defined field | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 3DS2008 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | NOT CAPTURED | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 6P \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15400 \| general | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 3DS2006 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | CM90000 \| CM90000-Problem occured during transaction. | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 3DS2005 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 74 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 12001 \| Format error | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 88 \| Unable to Dispense | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 72 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 700T5 \| Check for New information before retry | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | P1107 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 410 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | T5 \| Check for New information before retry | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | IPAY0200085 \| IPAY0200085-Rupay Initiate Failure | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 407 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 06 \| Error | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 3DS214 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 87 \| Bad Track Data | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 02 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15013 \| amount error | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 399 \| SYSTEM UNAVALIABLE | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 70030 \| Format error | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 3DS219 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | D1 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | T2 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 30051 \| Communication Error | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | UNKNOWN_ERROR | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 2032 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 31 \| Bank Not Supported by Switch | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 30052 \| Communication Error | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 3DS2004 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | N4 \| Maximum off-line refund reached | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 12001 \| Bank not supported by switch | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 3DS207 \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 70082 \| No security module | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | IRI \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | ISSPMR \| UNKNOWN | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 21 \| No Action Taken | Transaction failed due to a generic error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 12009 \| Acquirer Switch Timeout | Transaction timed out at the Payment Gateway, please retry. |
| failed | AUTHNEGATIVE | 12009 \| Acquirer Switch Timeout \| Acquirer Switch Timeout | Transaction timed out at the Payment Gateway, please retry. |
| failed | AUTHNEGATIVE | 12002 \| Acquirer Timeout | Transaction timed out at the Payment Gateway, please retry. |
| failed | AUTHNEGATIVE | 12009 \| ACQUIRER_TIMEOUT | Transaction timed out at the Payment Gateway, please retry. |
| failed | AUTHNEGATIVE | 12002 \| Acquirer Timeout \| Acquirer Timeout | Transaction timed out at the Payment Gateway, please retry. |
| failed | AUTHNEGATIVE | RREQ_NOT_RECEIVED | Transaction failed as the card has expired please use another paymode. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 54 \| Expired card | Transaction failed as the card has expired please use another paymode. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Expired card | Transaction failed as the card has expired please use another paymode. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | GW00854 \| Card expired | Transaction failed as the card has expired please use another paymode. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 70054 \| Expired card | Transaction failed as the card has expired please use another paymode. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 155007 \| Blocked first used-transaction from new cardholder and card not properly unblocked | E-Commerce is not enabled for this card. Please enable E-commerce on your bank app and retry the transaction. |
| failed | AUTHNEGATIVE | 155007 \| Blocked first used-transaction from new cardholder and card not properly unblocked \| Blocked first used-transaction from new cardholder and card not properly unblocked | E-Commerce is not enabled for this card. Please enable E-commerce on your bank app and retry the transaction. |
| failed | AUTHNEGATIVE | NPCI93 \| NPCI93 - Ecommerce Not Enabled | E-Commerce not enable for this card. Please enable E-commerce on your bank app and retry the transaction. |
| failed | AUTHNEGATIVE | GenerateOtp Failure - 93 : Ecommerce Not Enabled | E-Commerce not enable for this card. Please enable E-commerce on your bank app and retry the transaction. |
| failed | AUTHNEGATIVE | 14 \| Invalid account number (no such number) | No account found for this card. You can retry on another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15120 \| account closed | No account found for this card. You can retry on another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15120 \| account closed \| account closed | No account found for this card. You can retry on another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 52 \| No Checking Account \| Payment processor error No checking account | No account found for this card. You can retry on another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 53 \| No Savings Account \| We encountered a problem with Rupay processor: No savings account | No account found for this card. You can retry on another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 46 \| Closed account | No account found for this card. Please contact your issuer. You can retry on another paymode. If money is debited it will be refunded within 48 - 72 hours. |
| failed | AUTHNEGATIVE | Closed Account | No account found for this card. Please contact your issuer. You can retry on another paymode. If money is debited it will be refunded within 48 - 72 hours. |
| failed | AUTHNEGATIVE | T8 \| Invalid account | No account found for this card. Please contact your issuer. You can retry on another paymode. If money is debited it will be refunded within 48 - 72 hours. |
| failed | AUTHNEGATIVE | 78 \| Invalid/nonexistent account specified (general) | No account found for this card. Please contact your issuer. You can retry on another paymode. If money is debited it will be refunded within 48 - 72 hours. |
| failed | AUTHNEGATIVE | 700T8 \| Invalid account | No account found for this card. Please contact your issuer. You can retry on another paymode. If money is debited it will be refunded within 48 - 72 hours. |
| failed | AUTHNEGATIVE | 42 \| No Universal Account | No account found for this card. Please contact your issuer. You can retry on another paymode. If money is debited it will be refunded within 48 - 72 hours. |
| failed | AUTHNEGATIVE | 42 \| No Universal Amount | No account found for this card. Please contact your issuer. You can retry on another paymode. If money is debited it will be refunded within 48 - 72 hours. |
| failed | AUTHNEGATIVE | Authorise Failure : 52 : No checking account | No account found for this card. Please contact your issuer. You can retry on another paymode. If money is debited it will be refunded within 48 - 72 hours. |
| failed | AUTHNEGATIVE | HOST TIMEOUT | Session timed out error, Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | OTPCAN \| User Pressed Cancel Button | Session timed out error, Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | CANCELLED | Session timed out error, Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 8 \| Transaction Timed Out | Session timed out error, Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | IPAY0100042 - Transaction time limit exceeds. | Session timed out error, Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | ACCU400: Inactive User | Session timed out error, Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15001 \| missing parameter | Transaction failed due to technical issues. Please retry or use another paymode. If money is debited it will be refunded within 48 - 72 hours |
| failed | AUTHNEGATIVE | 92 \| Destination cannot be found for routing / Unable to route transa | Transaction failed due to technical issues. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 55 \| Incorrect PIN | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP |
| failed | AUTHNEGATIVE | NPCI450 \| NPCI450 - INVALID OTP | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP |
| failed | AUTHNEGATIVE | IPAY0100049 \| IPAY0100049-Transaction Declined Due To Exceeding OTP Resend Attempts | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP |
| failed | AUTHNEGATIVE | 70 \| PIN data required | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP |
| failed | AUTHNEGATIVE | GenerateOtp Failure - 453 : Exhausted OTP resend count | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP |
| failed | AUTHNEGATIVE | 86 \| Cannot verify PIN \| Cannot verify PIN; for example, no PVV | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP |
| failed | AUTHNEGATIVE | VerifyOTP Failure - 452 : Exhausted OTP verification | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP |
| failed | AUTHNEGATIVE | VerifyOTP Failure - 451 : EXPIRED OTP | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP |
| failed | AUTHNEGATIVE | VerifyOTP Failure - 450 : INVALID OTP | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP |
| failed | AUTHNEGATIVE | Invalid Otp | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP |
| failed | AUTHNEGATIVE | OTP Resend Attempts Exceeded | Transaction Failed due to wrong OTP entered. Please retry and enter the correct OTP |
| failed | AUTHNEGATIVE | GW02016 \| !ERROR!-PAYMENT_ID_EXPIRED:GW02016-PaymentId Expired. | This payment was already processed. If charged twice, money will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | GW02016 \| PaymentId Expired | This payment was already processed. If charged twice, money will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | NPCI454 \| NPCI454 - Duplicate requestID | This payment was already processed. If charged twice, money will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 10024 \| duplicate request, another txn already processing with same details | This payment was already processed. If charged twice, money will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | CM90004 \| CM90004-Duplicate Record | This payment was already processed. If charged twice, money will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | CM90004 \| DUPLICATE TRANSACTION REQUEST | This payment was already processed. If charged twice, money will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 94 \| Duplicate Transaction | This payment was already processed. If charged twice, money will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 12001 \| Duplicate transmission | This payment was already processed. If charged twice, money will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 10024 \| duplicate request, another txn already SUCCESS with same details | This payment was already processed. If charged twice, money will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | GenerateOtp Failure - 454 : Duplicate requestID | This payment was already processed. If charged twice, money will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Token status is not active \| UNKNOWN | The card used cannot be saved currently due to bank's rules. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Problem occured in Tokenize | The card used cannot be saved currently due to bank's rules. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction \| UNKNOWN | The card used cannot be saved currently due to bank's rules. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | NPCI07 \| NPCI07 - Invalid Parameter Valuetoken_authenticationValue | The card used cannot be saved currently due to bank's rules. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|1079\|R\|C\| \| UNKNOWN | The card used cannot be saved currently due to bank's rules. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|4418\|R\|C\| \| UNKNOWN | The card used cannot be saved currently due to bank's rules. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|5025\|V\|D\| \| UNKNOWN | The card used cannot be saved currently due to bank's rules. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|7282\|M\|C\| \| UNKNOWN | The card used cannot be saved currently due to bank's rules. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|9689\|V\|D\| \| UNKNOWN | The card used cannot be saved currently due to bank's rules. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | IPAY0100295 - Problem occured during ALT ID Generation | Wrong Expiry date/CVV entered, please recheck and try again. |
| failed | AUTHNEGATIVE | 10024 \| ALT ID is mandatory for Domestic transactions | Wrong Expiry date/CVV entered, please recheck and try again. |
| failed | AUTHNEGATIVE | 50822 \| Processing error while provisioning Guest Checkout Token | Wrong Expiry date/CVV entered, please recheck and try again. |
| failed | AUTHNEGATIVE | 31 \| Bank Not Supported by Switch \| Decline - Issuing bank unavailable. | Transaction failed due to bank server error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15 \| Invalid issuer \| No such issuer | Transaction failed due to bank server error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15 \| Invalid issuer \| Decline - Issuing bank unavailable. | Transaction failed due to bank server error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | Issuer or switch inoperative | Transaction failed due to bank server error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 91 \| Issuer not available | Transaction failed due to bank server error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 91 \| Issuer unavailable or switch inoperative \| Payment processor error Issuer inoperative or some other system problem | Transaction failed due to bank server error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 15091 \| Issuer or switch is inoperative | Transaction failed due to bank server error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 91 \| Issuer unavailable or switch inoperative | Transaction failed due to bank server error. Please retry or use another paymode. If money is debited it will be refunded within 48 hours. |
| failed | AUTHNEGATIVE | 99951 \| NON SUFFICIENT FUNDS | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |
| failed | AUTHNEGATIVE | 51 \| Not sufficient funds | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |
| failed | AUTHNEGATIVE | Authorise Failure : 51 : NON SUFFICIENT FUNDS | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |
| failed | AUTHNEGATIVE | 51 \| NON SUFFICIENT FUNDS | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |
| failed | AUTHNEGATIVE | Not sufficient funds | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |
| failed | AUTHNEGATIVE | 15051 \| insufficient funds | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |
| failed | AUTHNEGATIVE | 15051 \| no sufficient funds | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |
| failed | AUTHNEGATIVE | 13006 \| Issuer Insufficient Funds \| Issuer Insufficient Funds | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |
| failed | AUTHNEGATIVE | 51 \| Insufficient funds | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |
| failed | AUTHNEGATIVE | 51 \| Insufficient funds/over credit limit / Not sufficient funds | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |
| failed | AUTHNEGATIVE | 51 \| Insufficient funds/over credit limit / Not sufficient funds \| Decline - Insufficient funds in the account. | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |
| failed | AUTHNEGATIVE | 13006 \| Issuer Insufficient Funds | Transaction Failed due to insufficient fund in your account. Kindly use another card or another payment mode. |