---
title: Fetch offers API [New]
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
Fetch payment offers for a merchant. Request fields are FetchOfferDTO. Required fields are merchant_id, reseller_id, and hash. amount, offerKeys, paymentId, userToken, and skusDetail are optional. The handler forwards the body to the PayU Offers service and returns that JSON. Hash input in PartnerUtils.getWhatsappOfferRequestHashSequence is merchant_id, then the client secret is appended (`merchant_id|` + client secret), SHA-512.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `POST` | `https://test-partnerapilayer.payu.in/apilayer/partner/fetchOffer` |
| **Production** | `POST` | `https://api.payu.in/partner/fetchOffer` |

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
| amount<br />**optional** | `String` Amount | 1000.00 |
| offerKeys<br />**optional** | `Array of String` OfferKeys | ["OFFER_KEY_1"] |
| paymentId<br />**optional** | `Integer` PaymentId | 403993715521855092 |
| userToken<br />**optional** | `String` UserToken | USER_TOKEN |
| skusDetail<br />**optional** | `Array of Object` SkusDetail | [{"skuId": "SKU1", "skuAmount": "100.00", "quantity": "1", "offerKeys": ["OFFER_KEY_1"]}] |
| skusDetail[].skuId<br />**mandatory** | `String` SkuId | SKU1 |
| skusDetail[].skuAmount<br />**optional** | `String` SkuAmount | 100.00 |
| skusDetail[].quantity<br />**optional** | `String` Quantity | 1 |
| skusDetail[].offerKeys<br />**optional** | `Array of String` SkusDetail[].offerKeys | ["OFFER_KEY_1"] |

## Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/fetchOffer' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--data '{
  "merchant_id": 8739528,
  "reseller_id": "YOUR_RESELLER_UUID",
  "hash": "YOUR_HASH",
  "amount": "1000.00",
  "offerKeys": [
    "OFFER_KEY_1"
  ],
  "paymentId": 403993715521855092,
  "userToken": "USER_TOKEN",
  "skusDetail": [
    {
      "skuId": "SKU1",
      "skuAmount": "100.00",
      "quantity": "1",
      "offerKeys": [
        "OFFER_KEY_1"
      ]
    }
  ]
}'
```

## Response parameters

| HTTP status | Description |
| :---------- | :---------- |
| `200` | Offers service JSON, passed through. The partner layer does not define an offers array schema. |
| `400` | Validation failed. Body is `errors`, a list of bean-validation messages. |
| `401` | Invalid bearer token. |

## Sample response

### HTTP 200

Offers service JSON, passed through. The partner layer does not define an offers array schema.

### HTTP 400 — error

```json
{
  "errors": [
    "merchant_id is mandatory"
  ]
}
```

### HTTP 401 — error

```json
{
  "error": "Invalid Auth token"
}
```
