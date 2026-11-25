---
title: Dynamic Bharat QR API
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
POST /partner/dbqr. Headers match verifyStatus. PartnerService does not reject a missing body field. updateOmniChannelTransactionForDbqr reads vendorTransactionId, soundBoxTerminalId, expiryTime, and mihpayId when they are present, and swallows a parse error. The body is forwarded to POST /v1/partner/qr/dbqr.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `POST` | `https://test-partnerapilayer.payu.in/apilayer/partner/dbqr` |
| **Production** | `POST` | `https://api.payu.in/partner/dbqr` |

## Request parameters

### Request headers

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| Content-Type<br />**mandatory** | `String` Send the body as `application/json`. | application/json |
| X-PayU-Reseller-UUID<br />**mandatory** | `String` X-PayU-Reseller-UUID | YOUR_RESELLER_UUID |
| X-Partner-Token<br />**mandatory** | `String` Partner access token. The Partner QR guides send this as `Bearer <token>`. | Bearer YOUR_ACCESS_TOKEN |
| Authorization<br />**mandatory** | `String` HMAC value. Partner QR guides use `hmac username="<client_id>", algorithm="sha512", headers="date", signature="<signature>"`. | Bearer YOUR_ACCESS_TOKEN |
| X-PayU-Merchant-Key<br />**optional** | `String` X-PayU-Merchant-Key | VALUE |
| X-PayU-Merchant-ID<br />**optional** | `String` X-PayU-Merchant-ID | VALUE |
| date<br />**optional** | `String` Date | Wed, 25 Nov 2026 06:00:00 GMT |

### Request body

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| mihpayId | `String` MihpayId | 403993715529984752 |
| vendorTransactionId | `String` VendorTransactionId | PARTNER_TXN_001 |
| transactionAmount | `String` Decimal rupee string, for example "100.00". | 100.00 |
| expiryTime | `String` QR validity in seconds. | 3600 |
| soundBoxTerminalId | `String` SoundBoxTerminalId | ABCD1234 |

## Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/dbqr' \
--header 'Content-Type: application/json' \
--header 'X-PayU-Reseller-UUID: YOUR_RESELLER_UUID' \
--header 'X-Partner-Token: Bearer YOUR_ACCESS_TOKEN' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--data '{
  "mihpayId": "403993715529984752",
  "vendorTransactionId": "PARTNER_TXN_001",
  "transactionAmount": "100.00",
  "expiryTime": "3600",
  "soundBoxTerminalId": "ABCD1234"
}'
```

## Response parameters

| HTTP status | Description |
| :---------- | :---------- |
| `200` | Dynamic QR payload. The published page returns status and result.qrString. |

## Sample response

### HTTP 200 — success

```json
{
  "status": "success",
  "result": {
    "qrString": "000201010212..."
  }
}
```
