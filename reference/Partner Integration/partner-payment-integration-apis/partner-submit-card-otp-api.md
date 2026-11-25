---
title: Submit card OTP API
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
SubmitCardOtpDTO requires merchant_id, reseller_id, hash, reference_id, and otp. txnid is not a field. A verified OTP adds txnStatus, mihpayid, and message "OTP verified successfully". Failures use status "failed" and message.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `POST` | `https://test-partnerapilayer.payu.in/apilayer/partner/submitCardOtp` |
| **Production** | `POST` | `https://api.payu.in/partner/submitCardOtp` |

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
| reference_id<br />**mandatory** | `String` PayU reference id for the in-progress card transaction. | REFERENCE_ID |
| otp<br />**mandatory** | `String` Otp | 123456 |

## Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/submitCardOtp' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--data '{
  "merchant_id": 8739528,
  "reseller_id": "YOUR_RESELLER_UUID",
  "hash": "YOUR_HASH",
  "reference_id": "REFERENCE_ID",
  "otp": "123456"
}'
```

## Response parameters

| HTTP status | Description |
| :---------- | :---------- |
| `200` | OTP accepted. |
| `400` | Validation failed, or the OTP was rejected with attempts left. |
| `401` | Invalid bearer token. |

## Sample response

### HTTP 200 — success

```json
{
  "status": "success",
  "attemptsLeft": 2,
  "isSupported": true,
  "txnStatus": "success",
  "mihpayid": "403993715521855092",
  "message": "OTP verified successfully"
}
```

### HTTP 400 — validation

```json
{
  "errors": [
    "reference_id is mandatory."
  ]
}
```

### HTTP 400 — otp

```json
{
  "status": "failed",
  "message": "Invalid OTP",
  "attemptsLeft": 2
}
```

### HTTP 401 — error

```json
{
  "error": "Invalid Auth token"
}
```
