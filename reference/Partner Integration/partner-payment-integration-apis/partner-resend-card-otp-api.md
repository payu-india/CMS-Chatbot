---
title: Resend card OTP API
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
ResendCardOtpDTO requires merchant_id, reseller_id, hash, and reference_id. On success the message is "OTP resent successfully".

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `POST` | `https://test-partnerapilayer.payu.in/apilayer/partner/resendCardOtp` |
| **Production** | `POST` | `https://api.payu.in/partner/resendCardOtp` |

## Request parameters

### Request headers

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| Content-Type<br />**mandatory** | `String` Send the body as `application/json`. | application/json |
| Authorization<br />**mandatory** | `String` Partner access token. Send as Authorization Bearer token. | Bearer YOUR_ACCESS_TOKEN |

### Request body

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| merchant_id<br />**mandatory** | `Integer` Merchant id | 8739528 |
| reseller_id<br />**mandatory** | `String` Reseller id | YOUR_RESELLER_UUID |
| hash<br />**mandatory** | `String` Hash | YOUR_HASH |
| reference_id<br />**mandatory** | `String` Reference id | REFERENCE_ID |

## Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/resendCardOtp' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--data '{
  "merchant_id": 8739528,
  "reseller_id": "YOUR_RESELLER_UUID",
  "hash": "YOUR_HASH",
  "reference_id": "REFERENCE_ID"
}'
```

## Response parameters

| HTTP status | Description |
| :---------- | :---------- |
| `200` | OTP resent. |
| `400` | Validation failed or the resend was rejected. |
| `401` | Invalid bearer token. |

## Sample response

### HTTP 200 — success

```json
{
  "status": "success",
  "message": "OTP resent successfully",
  "attemptsLeft": 2,
  "isSupported": true
}
```

### HTTP 400 — error

```json
{
  "errors": [
    "reference_id is mandatory."
  ]
}
```

### HTTP 401 — error

```json
{
  "error": "Invalid Auth token"
}
```
