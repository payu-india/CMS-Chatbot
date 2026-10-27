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

> **Note:** The response is always complete. If PayU can't classify an error, it still returns a generic `userMessage` with `newErrorCode` as `NA` and the category as `Unknown`. You don't need to build any fallback logic.

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

### Notes:

- **Analytics and reporting:** Group failures by `newErrorCode`, or by its category and source digits, instead of parsing the free text in `field9`.
- **Triage:** Use the category digit to decide what to do next. For example, 6 (Risk decline) means don't retry with the same card, and 4 (Configuration error) means contact your PayU account manager.
- **Custom failure pages:** Show only `userMessage` to end users. Never show `merchantMessage` or `pgError`.
- **Message updates:** PayU updates error messages often to cover new errors in the ecosystem. Make sure any logic you build on this data accounts for these updates.

### Full Error Code List

The full list of error codes maps each `newErrorCode` to its category, source, user message, and merchant description.

\\<Error Code Table>
