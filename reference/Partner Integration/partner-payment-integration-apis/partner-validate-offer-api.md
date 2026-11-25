---
title: Validate offer API
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
Validate an offer. Fields are ValidateOfferDTO. Required: merchant_id, reseller_id, hash, paymentDetail (category is required inside it), and userDetail (userToken is required inside it). txnid, offerKey, and bankcode are not fields on this DTO. Offer keys are offerKeys. The response is the Offers validate endpoint JSON, passed through.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `POST` | `https://test-partnerapilayer.payu.in/apilayer/partner/validateOffer` |
| **Production** | `POST` | `https://api.payu.in/partner/validateOffer` |

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
| autoApply<br />**optional** | `Boolean` AutoApply | False |
| merchantNceParamActive<br />**optional** | `Boolean` MerchantNceParamActive | False |
| offerKeys<br />**optional** | `Array of String` OfferKeys | ["OFFER_KEY_1"] |
| paymentId<br />**optional** | `Integer` PaymentId | 403993715521855092 |
| paymentDetail<br />**mandatory** | `Object` PaymentDetail | {"category": "creditcard", "paymentCode": "CC", "cardNumber": 411111, "cardHash": "CARD_HASH", "cardToken": "CARD_TOKEN", "cardTokenType": 0, "cardMask": 1111, "vpa": "customer@upi"} |
| paymentDetail.category<br />**mandatory** | `String` Category | creditcard |
| paymentDetail.paymentCode<br />**optional** | `String` PaymentCode | CC |
| paymentDetail.cardNumber<br />**optional** | `Integer` CardNumber | 411111 |
| paymentDetail.cardHash<br />**optional** | `String` CardHash | CARD_HASH |
| paymentDetail.cardToken<br />**optional** | `String` CardToken | CARD_TOKEN |
| paymentDetail.cardTokenType<br />**optional** | `Integer` CardTokenType | 0 |
| paymentDetail.cardMask<br />**optional** | `Integer` CardMask | 1111 |
| paymentDetail.vpa<br />**optional** | `String` Vpa | customer@upi |
| userDetail<br />**mandatory** | `Object` UserDetail | {"userToken": "USER_TOKEN", "email": "customer@example.com", "phoneNo": "9999999999"} |
| userDetail.userToken<br />**mandatory** | `String` UserToken | USER_TOKEN |
| userDetail.email<br />**optional** | `String` Email | customer@example.com |
| userDetail.phoneNo<br />**optional** | `String` PhoneNo | 9999999999 |
| skusDetail<br />**optional** | `Object` SkusDetail | {"skus": [{"skuId": "SKU1", "skuAmount": "100.00", "quantity": "1", "offerKeys": ["OFFER_KEY_1"], "autoApply": false}]} |
| skusDetail.skus | `Array of Object` SkusDetail.skus | [{"skuId": "SKU1", "skuAmount": "100.00", "quantity": "1", "offerKeys": ["OFFER_KEY_1"], "autoApply": false}] |
| skusDetail.skus[].skuId<br />**mandatory** | `String` SkuId | SKU1 |
| skusDetail.skus[].skuAmount<br />**optional** | `String` SkuAmount | 100.00 |
| skusDetail.skus[].quantity<br />**optional** | `String` Quantity | 1 |
| skusDetail.skus[].offerKeys<br />**optional** | `Array of String` SkusDetail.skus[].offerKeys | ["OFFER_KEY_1"] |
| skusDetail.skus[].autoApply<br />**optional** | `Boolean` AutoApply | False |

## Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/validateOffer' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--data '{
  "merchant_id": 8739528,
  "reseller_id": "YOUR_RESELLER_UUID",
  "hash": "YOUR_HASH",
  "amount": "1000.00",
  "autoApply": false,
  "merchantNceParamActive": false,
  "offerKeys": [
    "OFFER_KEY_1"
  ],
  "paymentId": 403993715521855092,
  "paymentDetail": {
    "category": "creditcard",
    "paymentCode": "CC",
    "cardNumber": 411111,
    "cardHash": "CARD_HASH",
    "cardToken": "CARD_TOKEN",
    "cardTokenType": 0,
    "cardMask": 1111,
    "vpa": "customer@upi"
  },
  "userDetail": {
    "userToken": "USER_TOKEN",
    "email": "customer@example.com",
    "phoneNo": "9999999999"
  },
  "skusDetail": {
    "skus": [
      {
        "skuId": "SKU1",
        "skuAmount": "100.00",
        "quantity": "1",
        "offerKeys": [
          "OFFER_KEY_1"
        ],
        "autoApply": false
      }
    ]
  }
}'
```

## Response parameters

| HTTP status | Description |
| :---------- | :---------- |
| `200` | Offers validate JSON, passed through. |
| `400` | Bean validation failed. |
| `401` | Invalid bearer token. |

## Sample response

### HTTP 200

Offers validate JSON, passed through.

### HTTP 400 — error

```json
{
  "errors": [
    "paymentDetail is mandatory"
  ]
}
```

### HTTP 401 — error

```json
{
  "error": "Invalid Auth token"
}
```
