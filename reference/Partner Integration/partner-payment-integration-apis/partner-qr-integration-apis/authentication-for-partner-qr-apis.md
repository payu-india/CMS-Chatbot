---
title: Authentication for Partner QR APIs
deprecated: false
hidden: false
metadata:
  robots: index
---
Every Partner QR wrapper API request requires **two** authentication mechanisms:

| Mechanism         | Header                                   | Purpose                                                  |
| ----------------- | ---------------------------------------- | -------------------------------------------------------- |
| OAuth token       | `X-Partner-Token: Bearer {access_token}` | Identifies the partner; scope must be `partner_payments` |
| Request signature | `date` + `Authorization`                 | Proves request body integrity                            |

Also required on every call: `Content-Type: application/json`, `X-PayU-Reseller-UUID: {your_uuid}`.

***

## Step 1: Get OAuth access token

Use the client credentials flow to obtain an access token with `partner_payments` scope.

### Environment

|                |                                            |
| -------------- | ------------------------------------------ |
| UAT Token URL  | `https://uat-accounts.payu.in/oauth/token` |
| PROD Token URL | `https://accounts.payu.in/oauth/token`     |

### Request headers

| Parameter    | Value                               |
| ------------ | ----------------------------------- |
| Content-Type | `application/x-www-form-urlencoded` |

### Request parameters

| Parameter                 | Description                       | Example              |
| ------------------------- | --------------------------------- | -------------------- |
| grant_type `mandatory`    | OAuth grant type                  | `client_credentials` |
| client_id `mandatory`     | PayU-issued partner client ID     | `YOUR_CLIENT_ID`     |
| client_secret `mandatory` | PayU-issued partner client secret | `YOUR_CLIENT_SECRET` |
| scope `mandatory`         | Required scope for QR APIs        | `partner_payments`   |

### Sample request

```curl
curl --location --request POST 'https://uat-accounts.payu.in/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'client_id=YOUR_CLIENT_ID' \
--data-urlencode 'client_secret=YOUR_CLIENT_SECRET' \
--data-urlencode 'scope=partner_payments'
```

### Sample response

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 1800
}
```

Send the token on every QR API call as:

```
X-Partner-Token: Bearer {access_token}
```

Tokens typically expire in **30 minutes** (`expires_in: 1800`). Obtain a fresh token before it expires.

***

## Step 2: Set required headers

| Header               | Required        | Description                                       |
| -------------------- | --------------- | ------------------------------------------------- |
| Content-Type         | Yes             | `application/json`                                |
| X-Partner-Token      | Yes             | `Bearer {access_token}` from Step 1               |
| X-PayU-Reseller-UUID | Yes             | Your PayU-issued partner/reseller UUID            |
| date                 | Yes             | Current GMT timestamp — used in HMAC (see Step 3) |
| Authorization        | Yes             | HMAC signature (see Step 3)                       |
| X-PayU-Merchant-Key  | APIs 2 & 3 only | Merchant key (not included in HMAC hash)          |

### X-PayU-Reseller-UUID

Your PayU-issued partner identifier, provided during onboarding.

```
X-PayU-Reseller-UUID: 11ed-933c-ece48d50-a41d-023f883eb17c
```

### date header

Current UTC/GMT time. Recommended format:

```
EEE, dd MMM yyyy HH:mm:ss GMT
```

**Example:** `Tue, 15 Jul 2025 07:03:38 GMT`

**JavaScript:** `new Date().toUTCString()`

The server uses the **exact string** sent in the `date` header when verifying the signature. The `date` value in the hash string must match character-for-character.

***

## Step 3: Compute HMAC signature

Sign the request **before** sending. The HMAC is computed over the **exact JSON request body only** — headers (including `X-PayU-Merchant-Key`) are **not** part of the hash.

### Hash input

```
{request_body} + "|" + {date} + "|" + {client_secret}
```

| Component     | Notes                                                               |
| ------------- | ------------------------------------------------------------------- |
| request_body  | Exact raw JSON string you will send (do not reformat after signing) |
| date          | Same value as the `date` request header                             |
| client_secret | Your PayU-issued client secret                                      |

### Signature

```
signature = SHA512(hash_input) → lowercase hexadecimal (128 characters)
```

> This is a plain SHA-512 hash of the string — not HMAC-SHA512.

### Authorization header

```
Authorization: hmac username="{client_id}", algorithm="sha512", headers="date", signature="{signature}"
```

| Field     | Value                                      |
| --------- | ------------------------------------------ |
| username  | Your PayU **client ID** (must match token) |
| algorithm | `sha512`                                   |
| headers   | `date`                                     |
| signature | Output from hash step above                |

### Reference implementation (JavaScript)

```javascript
const crypto = require('crypto');

const clientId     = 'YOUR_CLIENT_ID';
const clientSecret = 'YOUR_CLIENT_SECRET';
const requestBody  = '{"txnId":["abc123"]}'; // exact string you will send

const date = new Date().toUTCString();
const hashInput = requestBody + '|' + date + '|' + clientSecret;
const signature = crypto.createHash('sha512').update(hashInput).digest('hex');

const authorization =
  'hmac username="' + clientId +
  '", algorithm="sha512", headers="date", signature="' + signature + '"';
```

### Complete signed request example

```http
POST /apilayer/partner/transaction/verifyStatus HTTP/1.1
Host: apitest.payu.in
Content-Type: application/json
X-Partner-Token: Bearer eyJhbGciOiJIUzI1NiIs...
X-PayU-Reseller-UUID: 11ed-933c-ece48d50-a41d-023f883eb17c
X-PayU-Merchant-Key: MERCHANT_KEY
date: Tue, 15 Jul 2025 07:03:38 GMT
Authorization: hmac username="YOUR_CLIENT_ID", algorithm="sha512", headers="date", signature="a1b2c3..."

{"txnId":["PARTNER_TXN_001"]}
```

***

***

## Failed responses

| Code | Reason                                                                                            | Response                             |
| ---- | ------------------------------------------------------------------------------------------------- | ------------------------------------ |
| 401  | Invalid or expired token; wrong scope; reseller UUID mismatch; merchant not linked                | `{ "error": "Invalid Auth token" }`  |
| 401  | Malformed `Authorization` header; missing `date` header; wrong `username`; algorithm not `sha512` | `{ "error": "Invalid HMAC header" }` |
| 403  | HMAC signature does not match body + date + client secret                                         | `{ "error": "Invalid Hash" }`        |
| 400  | Required header missing at controller binding                                                     | Spring default body (see below)      |

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

> A missing `date` header surfaces as **401** with `"Invalid HMAC header"` (not a framework 400).

### Invalid Auth token — common causes

- Token expired (typically 30 minutes)
- Token missing `partner_payments` scope
- `X-PayU-Reseller-UUID` does not match token's reseller
- Merchant not linked to partner in reseller portal

**Resolution:** Obtain a new token with `scope=partner_payments`.

### Invalid Hash — common causes

- Wrong `client_secret` in hash calculation
- `date` header value differs from date used when signing
- Request body modified after signing
- Signature not lowercase hex SHA-512

***

## Checklist before calling QR APIs

- [ ] Token obtained with `scope=partner_payments`
- [ ] Merchant linked to your partner account
- [ ] Sign the **exact** JSON body bytes you send (no pretty-print after signing)
- [ ] `date` header value = `date` used in hash string
- [ ] Fresh `date` + signature per request
- [ ] `username` in Authorization = your client ID
- [ ] `X-PayU-Merchant-Key` sent on Generate Dynamic QR and Check Status APIs only
