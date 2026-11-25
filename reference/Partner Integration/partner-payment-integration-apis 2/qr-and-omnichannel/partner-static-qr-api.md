---
title: Static QR API [New]
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
POST /partner/staticQr. Creates a reusable static QR for a merchant VPA. Required headers from PartnerController: X-PayU-Reseller-UUID, X-PayU-Merchant-ID, X-Partner-Token, X-Partner-Hash, X-Partner-Request-ID. Hash input, quoted from PartnerUtils.validateStaticQrHash: merchantId|rawRequestBody|clientSecret, then SHA-512. That is not sha512(key|reseller_id|merchant_id|salt). The JSON body must include merchantVpa. qrType and udf5 are stored when present. A cached success returns qrString, qrId, and merchantVpa.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `POST` | `https://test-partnerapilayer.payu.in/apilayer/partner/staticQr` |
| **Production** | `POST` | `https://api.payu.in/partner/staticQr` |

## Request parameters

### Request headers

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| Content-Type<br />**mandatory** | `String` Send the body as `application/json`. | application/json |
| X-PayU-Reseller-UUID<br />**mandatory** | `String` X-PayU-Reseller-UUID | YOUR_RESELLER_UUID |
| X-PayU-Merchant-ID<br />**mandatory** | `String` X-PayU-Merchant-ID | VALUE |
| X-Partner-Token<br />**mandatory** | `String` X-Partner-Token | Bearer YOUR_ACCESS_TOKEN |
| X-Partner-Hash<br />**mandatory** | `String` SHA-512 of `merchantId\|rawRequestBody\|clientSecret`. See PartnerUtils.validateStaticQrHash. | YOUR_HASH |
| X-Partner-Request-ID<br />**mandatory** | `String` X-Partner-Request-ID | VALUE |

### Request body

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| merchantVpa<br />**mandatory** | `String` Uniqueness key for the static QR. | merchant@payu |
| qrType<br />**optional** | `String` QrType | UPI |
| udf5<br />**optional** | `String` Udf5 | web |
| amount<br />**optional** | `String` Passed through in the raw body to generateInstaAccount when you set it. Not validated in generateStaticQr. | 1000.00 |

## Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/staticQr' \
--header 'Content-Type: application/json' \
--header 'X-PayU-Reseller-UUID: YOUR_RESELLER_UUID' \
--header 'X-PayU-Merchant-ID: VALUE' \
--header 'X-Partner-Token: Bearer YOUR_ACCESS_TOKEN' \
--header 'X-Partner-Hash: YOUR_HASH' \
--header 'X-Partner-Request-ID: VALUE' \
--data '{
  "merchantVpa": "merchant@payu",
  "qrType": "UPI",
  "udf5": "web",
  "amount": "1000.00"
}'
```

## Response parameters

| HTTP status | Description |
| :---------- | :---------- |
| `200` | Stored or newly created QR. Cache payload fields are qrString, qrId, and merchantVpa. |
| `400` | merchantVpa is missing, or the merchant id is unknown. |
| `403` | X-Partner-Hash did not match. |

## Sample response

### HTTP 200 — success

```json
{
  "qrString": "merchant@payu",
  "qrId": "QR_1001",
  "merchantVpa": "merchant@payu"
}
```

### HTTP 400 — error

```json
{
  "error": "merchantVpa is required in request body"
}
```

### HTTP 403 — error

```json
{
  "error": "Invalid Hash"
}
```
