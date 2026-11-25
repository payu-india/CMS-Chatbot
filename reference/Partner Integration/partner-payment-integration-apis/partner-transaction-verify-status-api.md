---
title: Verify omnichannel transaction status API
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
POST /partner/transaction/verifyStatus. Required headers: X-PayU-Reseller-UUID, X-Partner-Token, Authorization. Optional headers on the controller: X-PayU-Merchant-Key, X-PayU-Merchant-ID. PartnerService does not validate the body. txnId is forwarded with the rest of the body to the Bharat QR status command.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `POST` | `https://test-partnerapilayer.payu.in/apilayer/partner/transaction/verifyStatus` |
| **Production** | `POST` | `https://api.payu.in/partner/transaction/verifyStatus` |

## Request parameters

### Request headers

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| Content-Type<br />**mandatory** | `String` Send the body as `application/json`. | application/json |
| X-PayU-Reseller-UUID<br />**mandatory** | `String` X-PayU-Reseller-UUID | YOUR_RESELLER_UUID |
| X-Partner-Token<br />**mandatory** | `String` Partner access token. The Partner QR guides send this as `Bearer <token>`. | Bearer YOUR_ACCESS_TOKEN |
| Authorization<br />**mandatory** | `String` HMAC value. Partner QR guides use `hmac username="<client_id>", algorithm="sha512", headers="date", signature="<signature>"`. | Bearer YOUR_ACCESS_TOKEN |
| X-PayU-Merchant-Key<br />**optional** | `String` X-PayU-Merchant-Key | VALUE |
| X-PayU-Merchant-ID<br />**optional** | `String` Header name in PartnerConstants is X-PayU-Merchant-ID. | VALUE |
| date<br />**optional** | `String` Date | Wed, 25 Nov 2026 06:00:00 GMT |

### Request body

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| txnId | `Array of String` Transaction ids forwarded to the Bharat QR status command. PartnerService does not require this field. | ["PARTNER_TXN_001"] |

## Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/transaction/verifyStatus' \
--header 'Content-Type: application/json' \
--header 'X-PayU-Reseller-UUID: YOUR_RESELLER_UUID' \
--header 'X-Partner-Token: Bearer YOUR_ACCESS_TOKEN' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--data '{
  "txnId": [
    "PARTNER_TXN_001"
  ]
}'
```

## Response parameters

| HTTP status | Description |
| :---------- | :---------- |
| `200` | Bharat QR status JSON, passed through. |

## Sample response

### HTTP 200

Bharat QR status JSON, passed through.
