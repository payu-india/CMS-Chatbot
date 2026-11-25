---
title: Static QR callback API [New]
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
POST /partner/staticQrCallback is received by PayU. The handler rejects a blank field4 (merchant VPA) or a blank key. txnid is used only to detect a duplicate callback. A blank txnid is not rejected. The hash is the standard PayU response hash checked with validatePayUBizResponseHash and the merchant salt.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `POST` | `https://test-partnerapilayer.payu.in/apilayer/partner/staticQrCallback` |
| **Production** | `POST` | `https://api.payu.in/partner/staticQrCallback` |

## Request parameters

### Request headers

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| Content-Type<br />**mandatory** | `String` Send the body as `application/json`. | application/json |

### Request body

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| txnid<br />**optional** | `String` Used to detect a duplicate callback. A blank value is not rejected. | TXN1001 |
| field4<br />**mandatory** | `String` Merchant VPA. The handler rejects the call when this is blank. | merchant@payu |
| key<br />**mandatory** | `String` Merchant key used to load the salt for hash verification. | YOUR_MERCHANT_KEY |
| mihpayid<br />**optional** | `String` Mihpayid | 403993715521855092 |
| amount<br />**optional** | `String` Amount | 1000.00 |
| status<br />**optional** | `String` Status | success |
| mode<br />**optional** | `String` Mode | CC |
| hash<br />**optional** | `String` Hash | YOUR_HASH |
| bank_ref_num<br />**optional** | `String` Bank ref num | 1234567890 |

## Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/staticQrCallback' \
--header 'Content-Type: application/json' \
--data '{
  "txnid": "TXN1001",
  "field4": "merchant@payu",
  "key": "YOUR_MERCHANT_KEY",
  "mihpayid": "403993715521855092",
  "amount": "1000.00",
  "status": "success",
  "mode": "CC",
  "hash": "YOUR_HASH",
  "bank_ref_num": "1234567890"
}'
```

## Response parameters

| HTTP status | Description |
| :---------- | :---------- |
| `200` | Accepted, including a duplicate txnid. Empty body. |
| `400` | field4 or key is missing, or no static QR is registered for the VPA. |

## Sample response

### HTTP 200

Accepted, including a duplicate txnid. Empty body.

### HTTP 400 — error

```
field4 (merchantVpa) is required
```
