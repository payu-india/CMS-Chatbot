---
title: Generate Dynamic QR - Partner QR Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
Generate Dynamic QR creates a Bharat QR (DBQR) string for display on a partner soundbox device. Call this API after Initiate Payment using the `mihpayId` returned in Step 1.

This is **Step 2** of the Partner QR integration flow.

***

## Environment

|           |                                                 |
| --------- | ----------------------------------------------- |
| UAT Host  | `https://apitest.payu.in/apilayer/partner/dbqr` |
| PROD Host | `https://api.payu.in/apilayer/partner/dbqr`     |

**Method:** `POST`

***

## Authentication

See [Authentication for Partner QR APIs](authentication-partner-qr-apis) for OAuth token and HMAC signing.

***

## Request headers

| Parameter            | Value                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------ |
| Content-Type         | `application/json`                                                                         |
| X-Partner-Token      | `Bearer {access_token}` — token with `partner_payments` scope                              |
| X-PayU-Reseller-UUID | Your PayU-issued partner/reseller UUID                                                     |
| X-PayU-Merchant-Key  | Merchant key (same value as `accountId` in Initiate Payment)                               |
| date                 | Current GMT timestamp (used in HMAC)                                                       |
| Authorization        | `hmac username="{client_id}", algorithm="sha512", headers="date", signature="{signature}"` |

***

## Request parameters

| Parameter                       | Description                                                                           | Example              |
| ------------------------------- | ------------------------------------------------------------------------------------- | -------------------- |
| mihpayId `mandatory`            | PayU payment ID from Initiate Payment response                                        | `403993715529984752` |
| vendorTransactionId `mandatory` | Your unique transaction reference (same as `txnId` from Initiate Payment recommended) | `PARTNER_TXN_001`    |
| transactionAmount `mandatory`   | Payment amount as a **decimal string** in rupees (e.g. `"100.00"` for ₹100)           | `100.00`             |
| expiryTime `mandatory`          | QR validity duration in seconds                                                       | `3600`               |
| soundBoxTerminalId `mandatory`  | Soundbox device serial / terminal ID                                                  | `ABCD1234`           |

> **Amount format:** Initiate Payment uses paise (`10000` = ₹100). Generate Dynamic QR uses a decimal rupee string (`"100.00"`).

***

## Sample request

### Step A: Generate HMAC signature (JavaScript)

```javascript
const crypto = require('crypto');

const CLIENT_ID = 'YOUR_CLIENT_ID';
const CLIENT_SECRET = 'YOUR_CLIENT_SECRET';

const requestBody = JSON.stringify({
  "mihpayId": "403993715529984752",
  "vendorTransactionId": "PARTNER_TXN_001",
  "transactionAmount": "100.00",
  "expiryTime": "3600",
  "soundBoxTerminalId": "ABCD1234"
});

const date = new Date().toUTCString();
const hashString = requestBody + '|' + date + '|' + CLIENT_SECRET;
const signature = crypto.createHash('sha512').update(hashString).digest('hex');
const authorization = `hmac username="${CLIENT_ID}", algorithm="sha512", headers="date", signature="${signature}"`;
```

### Step B: Call Generate Dynamic QR

```curl
curl --location --request POST 'https://apitest.payu.in/apilayer/partner/dbqr' \
--header 'Content-Type: application/json' \
--header 'X-Partner-Token: Bearer YOUR_ACCESS_TOKEN' \
--header 'X-PayU-Reseller-UUID: YOUR_RESELLER_UUID' \
--header 'X-PayU-Merchant-Key: MERCHANT_KEY' \
--header 'date: Tue, 15 Jul 2025 07:03:38 GMT' \
--header 'Authorization: hmac username="YOUR_CLIENT_ID", algorithm="sha512", headers="date", signature="YOUR_SIGNATURE"' \
--data-raw '{
  "mihpayId": "403993715529984752",
  "vendorTransactionId": "PARTNER_TXN_001",
  "transactionAmount": "100.00",
  "expiryTime": "3600",
  "soundBoxTerminalId": "ABCD1234"
}'
```

***

## Sample response

### Success

```json
{
  "status": "success",
  "result": {
    "qrString": "00020101021226580014..."
  }
}
```

| Field           | Description                                          |
| --------------- | ---------------------------------------------------- |
| status          | `success` on successful QR generation                |
| result.qrString | Bharat QR payload string — render on soundbox device |

Display the `qrString` on the soundbox. The customer scans the QR and completes payment via their UPI app.

***

## Failed responses

### Wrapper authentication and validation errors

| Code | Reason                                                                     | Response                                                    |
| ---- | -------------------------------------------------------------------------- | ----------------------------------------------------------- |
| 400  | Required header `X-PayU-Merchant-Key` missing                              | Spring default 400 (see below)                              |
| 400  | Merchant key not found                                                     | `{ "error": "Merchant not found for key: {merchant_key}" }` |
| 400  | Could not load merchant salt                                               | `{ "error": "Failed to fetch merchant credentials" }`       |
| 400  | Merchant salt missing                                                      | `{ "error": "Merchant salt not found" }`                    |
| 401  | Invalid/expired token, wrong scope, reseller mismatch, merchant not linked | `{ "error": "Invalid Auth token" }`                         |
| 401  | Malformed HMAC header or missing `date`                                    | `{ "error": "Invalid HMAC header" }`                        |
| 403  | HMAC signature mismatch                                                    | `{ "error": "Invalid Hash" }`                               |
| 500  | Downstream proxy failure                                                   | `{ "error": "Internal error while generating dynamic QR" }` |
| 500  | Internal dependency failure                                                | `{ "error": "PayU Internal Server Error" }`                 |

### Missing required header (framework)

**HTTP Status:** `400 Bad Request`

```json
{
  "timestamp": "2026-08-19T07:30:00.000+00:00",
  "status": 400,
  "error": "Bad Request",
  "message": "Required header 'X-PayU-Merchant-Key' is not present",
  "path": "/apilayer/partner/dbqr"
}
```

### Downstream errors (after auth succeeds)

When authentication passes but the QR service returns an error, the downstream status code and response body are returned **as-is** (no wrapper envelope).

***

## Next step

After the customer scans and pays, poll **Check BQR Transaction Status - Partner QR Integration** (`POST /transaction/verifyStatus`) until the transaction reaches a terminal state.
