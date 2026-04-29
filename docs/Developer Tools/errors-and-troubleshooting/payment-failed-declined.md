---
title: Payment Failed or Declined
excerpt: >-
  Troubleshoot PayU failed or declined transactions using status, error codes,
  field7, field8, and field9.
deprecated: false
hidden: true
metadata:
  description: >-
    Debug issuer declines, bank failures, user cancellations, and payment method
    failures.
  robots: index
---
Payment failures occur after the customer is redirected to PayU, issuer, bank, wallet, or UPI app and the payment cannot be completed.

## When it occurs

<Accordion title="Error and Fixes" icon="fa-info-circle">

| Error code / type                                           | Error message or response indicator     | Recommended fix                                                                                                           |
| ----------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `status=failure`                                            | Payment attempt failed.                 | Verify response hash and final status before showing retry options.                                                       |
| `unmappedstatus=failed`                                     | Bank/issuer/PayU status maps to failed. | Treat as failed after reconciliation and create a new `txnid` for any retry.                                              |
| `E308`, `E348`, `E500`, `E306`, `E300`, `E1000`             | Common failure or decline codes.        | Use the code-specific table below to decide customer retry, alternate payment method, or pending reconciliation.          |
| `AUCNEGATIVE`, `AUTHNEGATIVE`, `TXNNEGATIVE`, `VERNEGATIVE` | Failed transaction stage in `field7`.   | Use the field-stage table below to identify whether authentication, authorization, bank response, or verification failed. |

</Accordion>

<Accordion title="field7 Errors and Fixes" icon="fa-table">
  | Error code / type | Error message or response indicator | Description                                | Possible cause                                                                                   | Recommended fix                                                                                         |
| ----------------- | ----------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| `AUCNEGATIVE`     | `field7=AUCNEGATIVE`                | Authentication failed.                     | Incorrect OTP/3DS challenge failure, user abandonment, or issuer authentication decline.         | Ask the customer to retry authentication or use another payment method after final status verification. |
| `AUTHNEGATIVE`    | `field7=AUTHNEGATIVE`               | Authorization failed after authentication. | Issuer declined authorization because of limits, risk, card restrictions, or insufficient funds. | Show issuer-decline guidance and offer another payment method.                                          |
| `TXNNEGATIVE`     | `field7=TXNNEGATIVE`                | Bank/wallet returned failed status.        | Bank, wallet, or PSP declined the transaction.                                                   | Treat as failed after hash/status verification and allow a new attempt with a new `txnid`.              |
| `VERNEGATIVE`     | `field7=VERNEGATIVE`                | Verification confirmed failed status.      | PayU verification with bank/wallet confirmed failure.                                            | Mark the attempt failed and show retry options.                                                         |
</Accordion>

### Sample Error Response

Below is the sample error response of a transaction declined by an issuer.

<Accordion title="Sample Request" icon="fa-code">

```json
{
  "mihpayid": "403993715525079998",
  "txnid": "txn_10002",
  "amount": "499.00",
  "status": "failure",
  "unmappedstatus": "failed",
  "error": "E348",
  "error_Message": "Transaction declined by the issuer",
  "PG_TYPE": "CC-PG",
  "field7": "AUTHNEGATIVE",
  "field8": "Refer to card issuer",
  "field9": "ISSUER_DECLINED",
  "bank_ref_num": "",
  "hash": "RESPONSE_HASH_VALUE"
}
```

</Accordion>

## Root cause

Now let us understand the root cause of this error. Failures are commonly caused by customer action, issuer/bank rules, payment instrument restrictions, or technical timeouts.

<Accordion title="Examples" icon="fa-info-circle">
  * Customer entered wrong OTP/CVV.
  * Customer cancelled or abandoned payment.
  * Issuer declined due to risk, limits, insufficient funds, or card restrictions.
  * Bank/PSP was unavailable.
  * Payment method is not enabled for the merchant.
</Accordion>

## Troubleshooting

Now that we know the root cause let's troubleshoot the error.

<Accordion title="Error Fix" icon="fa-info-circle">
  1. Verify response hash before using the payload.
  2. Match `txnid`, `amount`, and `key` with your order record.
  3. Read `status`, `unmappedstatus`, `error`, `error_Message`, `field7`, `field8`, and `field9`.
  4. Use `field7` to identify the failed stage.
  5. If failure is issuer/customer driven, show an actionable message and offer another payment method.
  6. If failure is technical or timeout driven, verify final status before creating another attempt.
  7. For repeated failures on one method, test another payment mode and check merchant configuration.
</Accordion>

| Error code / type | Error message or response indicator | Description                                | Possible cause                                                                                   | Recommended fix                                                                                         |
| ----------------- | ----------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| `AUCNEGATIVE`     | `field7=AUCNEGATIVE`                | Authentication failed.                     | Incorrect OTP/3DS challenge failure, user abandonment, or issuer authentication decline.         | Ask the customer to retry authentication or use another payment method after final status verification. |
| `AUTHNEGATIVE`    | `field7=AUTHNEGATIVE`               | Authorization failed after authentication. | Issuer declined authorization because of limits, risk, card restrictions, or insufficient funds. | Show issuer-decline guidance and offer another payment method.                                          |
| `TXNNEGATIVE`     | `field7=TXNNEGATIVE`                | Bank/wallet returned failed status.        | Bank, wallet, or PSP declined the transaction.                                                   | Treat as failed after hash/status verification and allow a new attempt with a new `txnid`.              |
| `VERNEGATIVE`     | `field7=VERNEGATIVE`                | Verification confirmed failed status.      | PayU verification with bank/wallet confirmed failure.                                            | Mark the attempt failed and show retry options.                                                         |
