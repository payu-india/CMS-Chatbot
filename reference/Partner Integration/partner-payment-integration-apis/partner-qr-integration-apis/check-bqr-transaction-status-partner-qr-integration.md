---
title: Check BQR Transaction Status - Partner QR Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
Check BQR Transaction Status returns the current status of a Bharat QR transaction. Poll this API after the customer scans the QR and initiates payment until the transaction reaches a terminal state (`success` or `failure`).

This is **Step 3** of the Partner QR integration flow.

***

## Environment

|           |                                                                     |
| --------- | ------------------------------------------------------------------- |
| UAT Host  | `https://apitest.payu.in/apilayer/partner/transaction/verifyStatus` |
| PROD Host | `https://api.payu.in/apilayer/partner/transaction/verifyStatus`     |

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

| Parameter         | Description                                                                           | Example               |
| ----------------- | ------------------------------------------------------------------------------------- | --------------------- |
| txnId `mandatory` | Array of partner transaction IDs to check. Pass the `txnId` used in Initiate Payment. | `["PARTNER_TXN_001"]` |

***

## Sample request

### Step A: Generate HMAC signature (JavaScript)

```javascript
const crypto = require('crypto');

const CLIENT_ID = 'YOUR_CLIENT_ID';
const CLIENT_SECRET = 'YOUR_CLIENT_SECRET';

const requestBody = JSON.stringify({
  "txnId": ["PARTNER_TXN_001"]
});

const date = new Date().toUTCString();
const hashString = requestBody + '|' + date + '|' + CLIENT_SECRET;
const signature = crypto.createHash('sha512').update(hashString).digest('hex');
const authorization = `hmac username="${CLIENT_ID}", algorithm="sha512", headers="date", signature="${signature}"`;
```

### Step B: Call Check BQR Transaction Status

```curl
curl --location --request POST 'https://apitest.payu.in/apilayer/partner/transaction/verifyStatus' \
--header 'Content-Type: application/json' \
--header 'X-Partner-Token: Bearer YOUR_ACCESS_TOKEN' \
--header 'X-PayU-Reseller-UUID: YOUR_RESELLER_UUID' \
--header 'X-PayU-Merchant-Key: MERCHANT_KEY' \
--header 'date: Tue, 15 Jul 2025 07:03:38 GMT' \
--header 'Authorization: hmac username="YOUR_CLIENT_ID", algorithm="sha512", headers="date", signature="YOUR_SIGNATURE"' \
--data-raw '{
  "txnId": ["PARTNER_TXN_001"]
}'
```

***

## Sample response

### Success

```json
{
  "message": "Success",
  "status": 1,
  "result": [
    {
      "mihpayId": 21612493009,
      "txnId": "PARTNER_TXN_001",
      "status": "success",
      "unmappedStatus": "captured",
      "originalAmount": 100.00,
      "netDebitAmount": 100.00,
      "mode": "UPI",
      "field9": "Transaction is Successful",
      "errorCode": "E000",
      "errorMessage": "No Error",
      "addedOn": "2024-11-19 21:17:55"
    }
  ]
}
```

| Field                    | Description                                                |
| ------------------------ | ---------------------------------------------------------- |
| status                   | `1` indicates API call succeeded                           |
| result\[].txnId          | Partner transaction ID                                     |
| result\[].mihpayId       | PayU payment ID                                            |
| result\[].status         | Transaction status (`success`, `failure`, `pending`, etc.) |
| result\[].unmappedStatus | Detailed status (e.g. `captured`, `failed`)                |
| result\[].originalAmount | Original transaction amount in rupees                      |
| result\[].netDebitAmount | Net debited amount in rupees                               |
| result\[].mode           | Payment mode (e.g. `UPI`)                                  |
| result\[].errorCode      | Error code (`E000` = no error on success)                  |
| result\[].errorMessage   | Error description                                          |
| result\[].addedOn        | Transaction timestamp                                      |

### Polling guidance

| status / unmappedStatus | Action                                               |
| ----------------------- | ---------------------------------------------------- |
| `pending`               | Continue polling (recommended interval: 3–5 seconds) |
| `success` / `captured`  | Payment complete — stop polling                      |
| `failure` / `failed`    | Payment failed — stop polling                        |

Recompute HMAC with a fresh `date` header on each poll request.

***

## Failed responses

### Wrapper authentication and validation errors

| Code | Reason                                                                     | Response                                                           |
| ---- | -------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| 400  | Required header `X-PayU-Merchant-Key` missing                              | Spring default 400 (see below)                                     |
| 400  | Merchant key not found                                                     | `{ "error": "Merchant not found for key: {merchant_key}" }`        |
| 400  | Could not load merchant salt                                               | `{ "error": "Failed to fetch merchant credentials" }`              |
| 400  | Merchant salt missing                                                      | `{ "error": "Merchant salt not found" }`                           |
| 401  | Invalid/expired token, wrong scope, reseller mismatch, merchant not linked | `{ "error": "Invalid Auth token" }`                                |
| 401  | Malformed HMAC header or missing `date`                                    | `{ "error": "Invalid HMAC header" }`                               |
| 403  | HMAC signature mismatch                                                    | `{ "error": "Invalid Hash" }`                                      |
| 500  | Downstream proxy failure                                                   | `{ "error": "Internal error while verifying transaction status" }` |
| 500  | Internal dependency failure                                                | `{ "error": "PayU Internal Server Error" }`                        |

### Missing required header (framework)

**HTTP Status:** `400 Bad Request`

```json
{
  "timestamp": "2026-08-19T07:30:00.000+00:00",
  "status": 400,
  "error": "Bad Request",
  "message": "Required header 'X-PayU-Merchant-Key' is not present",
  "path": "/apilayer/partner/transaction/verifyStatus"
}
```

### Downstream errors (after auth succeeds)

When authentication passes but the Info / transaction service returns an error, the downstream status code and response body are returned **as-is** (no wrapper envelope).

***

## Complete integration checklist

- [ ] OAuth token with `partner_payments` scope obtained
- [ ] Merchant linked to partner account
- [ ] Initiate Payment called — `mihpayId` received
- [ ] Generate Dynamic QR called — `qrString` displayed on soundbox
- [ ] Customer scanned QR and paid
- [ ] Check BQR Status polled until terminal state
