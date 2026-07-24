---
title: Validate Offer API
deprecated: false
hidden: false
metadata:
  robots: index
---
Validates selected offer keys/promocodes against the order and payment method before transaction creation. Ensures the offer is applicable and calculates the final discount.

## Endpoint

| Environment | Base URL |
|-------------|----------|
| UAT / Test | `https://apitest.payu.in/v1/offers/validate` |
| Production | `https://api.payu.in/v1/offers/validate` |

## Sample Request

```bash
curl -X POST 'https://apitest.payu.in/v1/offers/validate' \
  -H 'accessToken: <access_token>' \
  -H 'orderId: <encrypted_order_id>' \
  -H 'X-Credential-Username: <merchant_key>' \
  -H 'Content-Type: application/json' \
  -d '{
    "offerKeys": ["OfferTest2ZLHN@T23WBwMVnHw7"],
    "autoApply": false,
    "userDetail": {
      "email": "customer@email.com",
      "phoneNo": "9599928310"
    },
    "paymentDetail": {
      "category": "EMI",
      "paymentCode": "EMIA6",
      "cardNumber": "4808550000000000"
    }
  }'
```

## Sample Response

```json
{
  "code": "200",
  "message": "Offer Validated Successfully",
  "status": 1,
  "result": {
    "orderId": "AAAAAA",
    "clientId": 42693,
    "mid": 180012,
    "amount": 10000,
    "paymentCode": "EMIA6",
    "category": "EMI",
    "isValid": true,
    "flagToFail": false,
    "offerDiscount": {
      "offerKey": "OfferTest2ZLHN@T23WBwMVnHw7",
      "offerType": "INSTANT",
      "discount": 1.00,
      "discountedAmount": 9999.00,
      "discountType": "ABSOLUTE"
    },
    "offerDetail": {
      "offerId": 122550,
      "offerKey": "OfferTest2ZLHN@T23WBwMVnHw7",
      "offerType": "INSTANT",
      "title": "OfferTest2ZLHN",
      "description": "OfferTest223",
      "validFrom": "2026-01-08 19:16:14",
      "validTo": "2026-01-09 19:16:14",
      "discountType": "ABSOLUTE",
      "maxDiscountPerTxn": 1.00,
      "minTxnAmount": 1.00,
      "maxTxnAmount": 11111111.00,
      "amount": 10000,
      "discount": 1.00,
      "discountedAmount": 9999.00,
      "isValid": true
    },
    "totalDiscountDetail": {
      "totalCashbackDiscount": 0,
      "totalInstantDiscount": 1.00,
      "totalDiscountedAmount": 9999.00
    }
  },
  "traceId": "cabc009e-ae22-4a79-8f58-f727fb6563ec"
}
```

## Headers

| Parameter | Description | Example |
|-----------|-------------|---------|
| accessToken<br/>`mandatory` | `string` Access token from the Create Order response (`transaction.accessToken`). | `<access_token>` |
| orderId<br/>`mandatory` | `string` Encrypted order ID from the Create Order response (`transaction.orderid`). | `<encrypted_order_id>` |
| X-Credential-Username<br/>`mandatory` | `string` Merchant key configured for Air India. | `<merchant_key>` |
| Content-Type<br/>`mandatory` | `string` Media type of the JSON request body. | `application/json` |

## Request Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| offerKeys<br/>`mandatory` | `array` Array containing single offer key to validate. | `["OfferTest2ZLHN@T23WBwMVnHw7"]` |
| autoApply<br/>`mandatory` | `boolean` Auto-apply flag. Default: `false`. | `false` |
| userDetail<br/>`optional` | `object` User information for personalized offers. See [userDetail object parameters](#userdetail-object-parameters) for details. | - |
| paymentDetail<br/>`optional` | `object` Payment method details. See [paymentDetail object parameters](#paymentdetail-object-parameters) for details. | - |

### userDetail object parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| phoneNo<br/>`optional` | `string` Customer phone number. | `9599928310` |
| email<br/>`optional` | `string` Customer email. | `customer@email.com` |
| userToken<br/>`optional` | `string` User token. | `33512` |
| loggedInPhoneNumber<br/>`optional` | `string` Logged-in user's phone number. | `9599928309` |

### paymentDetail object parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| category<br/>`conditional` | `string` Payment category: `CREDITCARD`, `DEBITCARD`, `NETBANKING`, `WALLET`, `UPI`, `EMI`, `BNPL`, `CLW`. Required when `paymentDetail` is sent. | `EMI` |
| paymentCode<br/>`conditional` | `string` Payment code. Required when `paymentDetail` is sent. | `EMIA6` |
| cardNumber<br/>`conditional` | `string` Card number. Required for card transactions unless `cardToken` is provided. | `4808550000000000` |
| cardToken<br/>`optional` | `string` Tokenized card identifier. | `abc123tokenXYZ` |
| cardTokenType<br/>`conditional` | `number` Card token type. Required when `cardToken` is provided; set to `1` for PayU tokens. | `1` |
| vpa<br/>`conditional` | `string` UPI Virtual Payment Address. Required for UPI transactions. | `user@paytm` |

## Response Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| code | `string` Response code. `200` indicates success. | `200` |
| message | `string` Response message. | `Offer Validated Successfully` |
| status | `number` `1` = success, `0` = failure. | `1` |
| result | `object` Validation result. See [result object description](#result-object-description) for details. | - |
| traceId | `string` Unique trace ID for debugging. | `cabc009e-ae22-4a79-8f58-f727fb6563ec` |

### result object description

| Parameter | Description | Example |
|-----------|-------------|---------|
| orderId | `string` Echo of request order ID. | `AAAAAA` |
| clientId | `number` Client ID. | `42693` |
| mid | `number` Merchant ID. | `180012` |
| amount | `number` Original request amount. | `10000` |
| paymentCode | `string` Echo from paymentDetail.paymentCode. | `EMIA6` |
| category | `string` Echo from paymentDetail.category. | `EMI` |
| isValid | `boolean` `true` if offer validation passed. | `true` |
| failureReason | `string` Failure reason; null on success. | `null` |
| flagToFail | `boolean` `true` = block transaction if offer invalid. | `false` |
| autoApply | `boolean` Echo of request. | `false` |
| offerDiscount | `object` Calculated discount summary with fields: offerKey, offerType, discount, discountedAmount, discountType. | - |
| offerDetail | `object` Detailed offer information. Includes offerId, offerKey, title, description, validFrom, validTo, discountType, maxDiscountPerTxn, minTxnAmount, maxTxnAmount, etc. | - |
| totalDiscountDetail | `object` Total discount breakdown with fields: totalCashbackDiscount, totalInstantDiscount, totalDiscountedAmount. | - |
| offers | `array` Array of validated offers. | - |
