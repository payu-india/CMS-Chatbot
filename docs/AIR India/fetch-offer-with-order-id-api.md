---
title: Fetch Offer with Order ID API
deprecated: false
hidden: false
metadata:
  robots: index
---
Retrieves applicable offers for an existing order created via the Create Order API. This API uses the order context from headers to fetch relevant offers.

## Endpoint

| Environment | Base URL |
|-------------|----------|
| UAT / Test | `https://apitest.payu.in/v1/offers` |
| Production | `https://api.payu.in/v1/offers` |

## Sample Request

```bash
curl -X POST 'https://apitest.payu.in/v1/offers' \
  -H 'accessToken: <access_token>' \
  -H 'orderId: <encrypted_order_id>' \
  -H 'X-Credential-Username: <merchant_key>'
```

## Sample Response

```json
{
  "code": "200",
  "message": "Offer Retrieved Successfully",
  "status": 1,
  "result": {
    "failureReason": null,
    "clientId": 42693,
    "mid": 180012,
    "amount": null,
    "couponsAvailable": true,
    "personalizedOffersAvailable": false,
    "offers": [
      {
        "offerKey": "AIParamTesting01",
        "type": "MERCHANT",
        "title": "AIParamTesting",
        "description": "AIParamTesting",
        "tnc": "AIParamTesting",
        "minTxnAmount": 10.00,
        "maxTxnAmount": 99999999.00,
        "offerType": "INSTANT",
        "validFrom": "2026-07-23 00:00:00",
        "validTo": "2026-07-24 23:59:59",
        "discountDetail": {
          "discountType": "PERCENTAGE",
          "discountPercentage": 10.00,
          "maxDiscount": 99999999.00
        },
        "isNoCostEmi": false,
        "isSubvented": false,
        "creditCard": [
          {
            "banks": [
              {
                "code": "ICICI",
                "title": "Icici Bank"
              }
            ]
          }
        ],
        "netBanking": [
          {
            "title": "HDFC NetBanking",
            "paymentCode": "HDFB"
          }
        ]
      }
    ]
  },
  "traceId": "2c013e72-df35-42ec-a47e-7404b94780e6"
}
```

## Request Parameters
### Header Authentication Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| accessToken<br/>`mandatory` | `string` Access token from the Create Order response (`transaction.accessToken`). | `<access_token>` |
| orderId<br/>`mandatory` | `string` Encrypted order ID from the Create Order response (`transaction.orderid`). | `<encrypted_order_id>` |
| X-Credential-Username<br/>`mandatory` | `string` Merchant key configured for Air India. | `<merchant_key>` |

### Body Parameters

This API does not require a request body. The order context is obtained from the headers.

## Response Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| code | `string` Response code. `200` indicates success. | `200` |
| message | `string` Response message. | `Offer Retrieved Successfully` |
| status | `number` Status indicator. `1` = success, `0` = failure. | `1` |
| result | `object` Contains offer details. See [result object description](#result-object-description) for details. | - |
| traceId | `string` Unique trace ID for debugging. | `2c013e72-df35-42ec-a47e-7404b94780e6` |

### result object description

| Parameter | Description | Example |
|-----------|-------------|---------|
| failureReason | `string` Failure reason if any (null on success). | `null` |
| clientId | `number` Client ID. | `42693` |
| mid | `number` Merchant ID. | `180012` |
| amount | `number` Transaction amount. | `null` |
| couponsAvailable | `boolean` Whether coupons are available. | `true` |
| personalizedOffersAvailable | `boolean` Whether personalized offers are available. | `false` |
| offers | `array` List of available offers. Each offer object contains offer details. See [offers array description](#offers-array-description) for details. | - |

### offers array description

| Parameter | Description | Example |
|-----------|-------------|---------|
| offerKey | `string` Unique offer identifier (used in Validate Offer API). | `AIParamTesting01` |
| type | `string` Offer type. | `MERCHANT` |
| title | `string` Offer title. | `AIParamTesting` |
| description | `string` Offer description. | `AIParamTesting` |
| tnc | `string` Terms and conditions. | `AIParamTesting` |
| tncLink | `string` Link to detailed terms and conditions. | `null` |
| minTxnAmount | `number` Minimum transaction amount for offer. | `10.00` |
| maxTxnAmount | `number` Maximum transaction amount for offer. | `99999999.00` |
| offerType | `string` Offer type: `INSTANT` or `CASHBACK`. | `INSTANT` |
| validFrom | `string` Offer start date/time (yyyy-MM-dd HH:mm:ss). | `2026-07-23 00:00:00` |
| validTo | `string` Offer end date/time (yyyy-MM-dd HH:mm:ss). | `2026-07-24 23:59:59` |
| discountDetail | `object` Discount details including discountType, discountPercentage, maxDiscount. | - |
| isNoCostEmi | `boolean` Whether this is a no-cost EMI offer. | `false` |
| isSubvented | `boolean` Whether the offer is subvented. | `false` |
| isSkuOffer | `boolean` Whether this is a SKU-specific offer. | `false` |
| creditCard | `array` Applicable credit card banks. | - |
| debitCard | `array` Applicable debit card banks. | - |
| netBanking | `array` Applicable net banking options. | - |
| wallet | `array` Applicable wallet options. | - |
| upi | `array` Applicable UPI options. | - |
| emi | `object` EMI-specific offer details. | - |
| priority | `number` Display priority. | `1` |
| offerIcon | `string` Icon URL for the offer. | `https://ddfkkf6aho2sr.cloudfront.net/...` |
