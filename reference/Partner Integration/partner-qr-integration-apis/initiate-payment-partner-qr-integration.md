---
title: Initiate Payment - Partner QR Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
Initiate Payment creates a payment transaction and returns a `mihpayId`. Use this value in the Generate Dynamic QR API to produce the Bharat QR string for the soundbox device.

This is **Step 1** of the Partner QR integration flow.

***

## Environment

|           |                                                            |
| --------- | ---------------------------------------------------------- |
| UAT Host  | `https://apitest.payu.in/apilayer/partner/initiatePayment` |
| PROD Host | `https://api.payu.in/apilayer/partner/initiatePayment`     |

**Method:** `POST`

***

## Authentication

See [Authentication for Partner QR APIs](authentication-partner-qr-apis) for OAuth token and HMAC signing.

> Partner QR APIs require `X-Partner-Token` (Bearer) **and** HMAC `Authorization` — not Bearer-only auth used by Hosted Checkout.

***

## Request headers

| Parameter            | Value                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------ |
| Content-Type         | `application/json`                                                                         |
| X-Partner-Token      | `Bearer {access_token}` — token with `partner_payments` scope                              |
| X-PayU-Reseller-UUID | Your PayU-issued partner/reseller UUID                                                     |
| date                 | Current GMT timestamp (used in HMAC)                                                       |
| Authorization        | `hmac username="{client_id}", algorithm="sha512", headers="date", signature="{signature}"` |

> **Note:** Do **not** send `X-PayU-Merchant-Key` on this API. Pass the merchant key as `accountId` in the request body.

***

## Request parameters

| Parameter                                          | Description                                                                                                               | Example                       |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| accountId `mandatory`                              | Merchant key provided by PayU. Sent in body only for this API.                                                            | `MERCHANT_KEY`                |
| txnId `mandatory`                                  | Unique transaction reference generated at partner end. Must be unique per merchant; reusing a successful txnId will fail. | `PARTNER_TXN_001`             |
| amount `mandatory`                                 | Payment amount in **paise** (e.g. `10000` = ₹100.00)                                                                      | `10000`                       |
| currency `mandatory`                               | Transaction currency                                                                                                      | `INR`                         |
| order `mandatory`                                  | Order details object                                                                                                      | See sample request            |
| order.productInfo `mandatory`                      | Brief product description                                                                                                 | `Product description`         |
| order.paymentChargeSpecification.price `mandatory` | Price in paise (should match `amount`)                                                                                    | `10000`                       |
| additionalInfo `mandatory`                         | Transaction flow configuration                                                                                            | See sample request            |
| additionalInfo.txnFlow `mandatory`                 | Transaction flow type                                                                                                     | `nonseamless`                 |
| additionalInfo.createOrder `mandatory`             | Whether to create an order                                                                                                | `false`                       |
| callBackActions `mandatory`                        | Redirect URLs for payment outcomes                                                                                        | See sample request            |
| callBackActions.successAction `mandatory`          | URL on payment success                                                                                                    | `https://example.com/success` |
| callBackActions.failureAction `mandatory`          | URL on payment failure                                                                                                    | `https://example.com/failure` |
| callBackActions.cancelAction `mandatory`           | URL on payment cancel                                                                                                     | `https://example.com/cancel`  |
| callBackActions.returnAction `mandatory`           | Return URL                                                                                                                | `https://example.com/return`  |
| billingDetails `mandatory`                         | Customer billing information                                                                                              | See sample request            |
| billingDetails.firstName `mandatory`               | Customer first name                                                                                                       | `John`                        |
| billingDetails.phone `mandatory`                   | Customer phone number                                                                                                     | `8800108522`                  |
| billingDetails.email `mandatory`                   | Customer email                                                                                                            | `customer@example.in`         |
| billingDetails.address1 `mandatory`                | Address line 1                                                                                                            | `Address line 1`              |
| billingDetails.city `mandatory`                    | City                                                                                                                      | `Gurgaon`                     |
| billingDetails.state `mandatory`                   | State                                                                                                                     | `Haryana`                     |
| billingDetails.country `mandatory`                 | Country                                                                                                                   | `India`                       |
| billingDetails.zipCode `mandatory`                 | PIN / zip code                                                                                                            | `122001`                      |

***

## Sample request

### Step A: Generate HMAC signature (JavaScript)

```javascript
const crypto = require('crypto');

const CLIENT_ID = 'YOUR_CLIENT_ID';
const CLIENT_SECRET = 'YOUR_CLIENT_SECRET';

const requestBody = JSON.stringify({
  "accountId": "MERCHANT_KEY",
  "txnId": "PARTNER_TXN_001",
  "amount": 10000,
  "currency": "INR",
  "order": {
    "productInfo": "Product description",
    "paymentChargeSpecification": { "price": 10000 }
  },
  "additionalInfo": {
    "txnFlow": "nonseamless",
    "createOrder": "false"
  },
  "callBackActions": {
    "successAction": "https://example.com/success",
    "failureAction": "https://example.com/failure",
    "cancelAction": "https://example.com/cancel",
    "returnAction": "https://example.com/return"
  },
  "billingDetails": {
    "firstName": "John",
    "phone": "8800108522",
    "email": "customer@example.in",
    "address1": "Address line 1",
    "city": "Gurgaon",
    "state": "Haryana",
    "country": "India",
    "zipCode": "122001"
  }
});

const date = new Date().toUTCString();
const hashString = requestBody + '|' + date + '|' + CLIENT_SECRET;
const signature = crypto.createHash('sha512').update(hashString).digest('hex');
const authorization = `hmac username="${CLIENT_ID}", algorithm="sha512", headers="date", signature="${signature}"`;
```

### Step B: Call Initiate Payment

```curl
curl --location --request POST 'https://apitest.payu.in/apilayer/partner/initiatePayment' \
--header 'Content-Type: application/json' \
--header 'X-Partner-Token: Bearer YOUR_ACCESS_TOKEN' \
--header 'X-PayU-Reseller-UUID: YOUR_RESELLER_UUID' \
--header 'date: Tue, 15 Jul 2025 07:03:38 GMT' \
--header 'Authorization: hmac username="YOUR_CLIENT_ID", algorithm="sha512", headers="date", signature="YOUR_SIGNATURE"' \
--data-raw '{
  "accountId": "MERCHANT_KEY",
  "txnId": "PARTNER_TXN_001",
  "amount": 10000,
  "currency": "INR",
  "order": {
    "productInfo": "Product description",
    "paymentChargeSpecification": {
      "price": 10000
    }
  },
  "additionalInfo": {
    "txnFlow": "nonseamless",
    "createOrder": "false"
  },
  "callBackActions": {
    "successAction": "https://example.com/success",
    "failureAction": "https://example.com/failure",
    "cancelAction": "https://example.com/cancel",
    "returnAction": "https://example.com/return"
  },
  "billingDetails": {
    "firstName": "John",
    "phone": "8800108522",
    "email": "customer@example.in",
    "address1": "Address line 1",
    "city": "Gurgaon",
    "state": "Haryana",
    "country": "India",
    "zipCode": "122001"
  }
}'
```

> Use the **exact same** `date`, `Authorization`, and request body string that were used when computing the HMAC signature.

***

## Sample response

### Success

```json
{
  "result": {
    "mihpayId": "403993715529984752",
    "paymentId": "403993715529984752"
  },
  "status": "success"
}
```

| Field            | Description                                       |
| ---------------- | ------------------------------------------------- |
| result.mihpayId  | PayU payment ID — pass to Generate Dynamic QR API |
| result.paymentId | Same as mihpayId                                  |
| status           | `success` on successful initiation                |

***

## Failed responses

### Wrapper authentication and validation errors

| Code | Reason                                                                     | Response                                                           |
| ---- | -------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| 400  | `accountId` missing from JSON body                                         | `{ "error": "accountId is required in request body" }`             |
| 400  | `accountId` is blank                                                       | `{ "error": "accountId cannot be empty" }`                         |
| 400  | Invalid JSON or missing `accountId`                                        | `{ "error": "Invalid JSON or missing accountId in request body" }` |
| 400  | Merchant key not found                                                     | `{ "error": "Merchant not found for key: {merchant_key}" }`        |
| 400  | Could not load merchant salt                                               | `{ "error": "Failed to fetch merchant credentials" }`              |
| 400  | Merchant salt missing                                                      | `{ "error": "Merchant salt not found" }`                           |
| 401  | Invalid/expired token, wrong scope, reseller mismatch, merchant not linked | `{ "error": "Invalid Auth token" }`                                |
| 401  | Malformed HMAC header or missing `date`                                    | `{ "error": "Invalid HMAC header" }`                               |
| 403  | HMAC signature mismatch                                                    | `{ "error": "Invalid Hash" }`                                      |
| 500  | Downstream proxy failure                                                   | `{ "error": "Internal error while processing payment request" }`   |
| 500  | Internal dependency failure                                                | `{ "error": "PayU Internal Server Error" }`                        |

### Missing required header (framework)

**HTTP Status:** `400 Bad Request`

```json
{
  "timestamp": "2026-08-19T07:30:00.000+00:00",
  "status": 400,
  "error": "Bad Request",
  "message": "Required header 'X-Partner-Token' is not present",
  "path": "/apilayer/partner/initiatePayment"
}
```

### Downstream errors (after auth succeeds)

When authentication passes but the Core Payments API returns an error, the downstream status code and response body are returned **as-is** (no wrapper envelope).

***

## Next step

Use `mihpayId` from the success response in **Generate Dynamic QR - Partner QR Integration** (`POST /dbqr`).
