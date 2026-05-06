---
title: Sample Error Responses
excerpt: >-
  Sample PayU response payloads for successful payments, failed transactions,
  invalid hash errors, and authentication failures.
deprecated: false
hidden: true
metadata:
  robots: index
---
The following examples are shown as JSON for readability. Depending on your integration, PayU may return fields through browser redirect, form post, webhook, or API response.

## Payment Success

Below is the sample payment success payload.

<Accordion title="Sample Success Payload" icon="fa-code">
  ```json Success Sample
  {
    "mihpayid": "403993715525079998",
    "mode": "CC",
    "status": "success",
    "unmappedstatus": "captured",
    "key": "gtKFFx",
    "txnid": "txn_10005",
    "amount": "10.00",
    "productinfo": "Test Product",
    "firstname": "John",
    "email": "john@example.com",
    "phone": "9999999999",
    "error": "E000",
    "error_Message": "No Error",
    "bank_ref_num": "123456789",
    "PG_TYPE": "CC-PG",
    "hash": "response_hash"
  }
  ```
</Accordion>

Use this response only after:

* Response hash is valid.
* `txnid` matches your order attempt.
* `amount` matches your expected payable amount.
* No later verified webhook/status response contradicts it.

| Success code | Success message as returned by PayU | Next Step                                                                     |
| ------------ | ----------------------------------- | ----------------------------------------------------------------------------- |
| `E000`       | `No Error`                          | Validate response hash, match `txnid` and `amount`, then mark the order paid. |

## Failed Transaction

Below is the sample transaction failure payload.

<Accordion title="Sample Failure Payload" icon="fa-code">
  ```json Failure Sample
  {
    "mihpayid": "403993715525080001",
    "mode": "DC",
    "status": "failure",
    "unmappedstatus": "failed",
    "key": "gtKFFx",
    "txnid": "txn_10006",
    "amount": "250.00",
    "productinfo": "Test Product",
    "firstname": "John",
    "email": "john@example.com",
    "phone": "9999999999",
    "error": "E500",
    "error_Message": "Bank failed to authenticate the customer",
    "PG_TYPE": "DC-PG",
    "field7": "AUCNEGATIVE",
    "field8": "Message Received Invalid",
    "field9": "UNKNOWN",
    "hash": "response_hash"
  }
  ```
</Accordion>

Recommended fix:

* Verify response hash.
* Store `mihpayid`, `error`, `error_Message`, `field7`, `field8`, and `field9`.
* Show a retry option.
* Use a new `txnid` for a new payment attempt.

| Error code / type | Error message as returned by PayU          | Recommended fix                                                                                                           |
| ----------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| `E500`            | `Bank failed to authenticate the customer` | Verify final status through webhook/status API, then let the customer retry with a new `txnid` or another payment method. |
| `AUCNEGATIVE`     | Authentication stage failed                | Ask the customer to retry OTP/3DS or use another payment method.                                                          |

## Invalid Hash

Below is the invalid hash error sample.

<Accordion title="Invalid Hash Sample" icon="fa-code">
  ```json Invalid Hash
  {
    "status": "failure",
    "unmappedstatus": "failed",
    "txnid": "txn_10007",
    "error": "E700",
    "error_Message": "Validation of secure hash failed"
  }
  ```
</Accordion>

Recommended fix:

* Do not retry from the frontend.
* Fix backend hash generation.
* Compare raw request values with the hash string.
* Confirm key, salt, endpoint, and environment.

| Error code / type | Error message as returned by PayU  | Recommended fix                                                                                            |
| ----------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `E700`            | `Validation of secure hash failed` | Regenerate the request hash on the backend using the exact posted values and correct key/salt environment. |

### PayU Hash Generator

<br />

## Authentication failure

```json
{
  "mihpayid": "403993715525080002",
  "status": "failure",
  "unmappedstatus": "failed",
  "txnid": "txn_10008",
  "amount": "999.00",
  "error": "E300",
  "error_Message": "Card failed 3D authentication as 3 D Secure signatures did not match",
  "PG_TYPE": "CC-PG",
  "field7": "3DS_CHALLENGE_NEGATIVE",
  "field8": "Authentication failed",
  "field9": "SECURE_3D_PASSWORD_ERROR",
  "hash": "response_hash"
}
```

Recommended fix:

* Verify hash before trusting the response.
* Ask customer to retry OTP/3DS.
* Offer another payment method.
* Do not expose raw issuer payloads if they are unclear.

| Error code / type        | Error message as returned by PayU                                      | Recommended fix                                                                                  |
| ------------------------ | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `E300`                   | `Card failed 3D authentication as 3 D Secure signatures did not match` | Verify final status, then ask the customer to retry authentication or use another card.          |
| `3DS_CHALLENGE_NEGATIVE` | Authentication failed                                                  | Treat as customer/issuer authentication failure and provide a retry or alternate payment method. |
