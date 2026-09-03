---
title: Headers and Content Types
excerpt: >-
  Learn which HTTP headers and content types PayU APIs expect for Collect
  Payment, General APIs, OAuth products, and HMAC-authenticated endpoints.
deprecated: false
hidden: false
metadata:
  title: PayU API Headers and Content Types
  description: >-
    Reference for PayU API headers and content types, including
    form-urlencoded payment requests, JSON General API responses, OAuth bearer
    tokens, and HMAC authorization headers.
  keywords:
    - PayU API headers
    - PayU content-type
    - PayU authorization header
    - PayU HMAC authentication
    - PayU form-urlencoded
  robots: index
next:
  description: ''
---
PayU API families expect different header and content-type conventions. Sending the wrong `Content-Type` or missing auth headers is a common first-integration failure.

## Common content types

| API family | Typical `Content-Type` | Notes |
| :--------- | :--------------------- | :---- |
| Collect Payment (`_payment`) | `application/x-www-form-urlencoded` | Payment fields posted as form data |
| General APIs | `application/x-www-form-urlencoded` | `key`, `command`, `hash`, `var1…` as form fields; use `form=2` for JSON response |
| OAuth token APIs | Product-specific (often form or JSON) | Follow the token API Reference page |
| Product REST APIs | Often `application/json` | BBPS, some partner/onboarding, and newer product APIs |

## Headers for key + hash APIs

For most Collect Payment and General APIs, authentication values are part of the **request body** (`key`, `hash`), not an `Authorization` bearer header.

Recommended headers:

```http
Content-Type: application/x-www-form-urlencoded
Accept: application/json
```

General APIs still rely on `form=2` in the URL for JSON responses.

## Headers for OAuth APIs

After you generate an access token:

1. Store the token securely on your server.
2. Send it on resource requests exactly as documented by that product (commonly an `Authorization` header).
3. Regenerate/refresh on expiry.

Starting points:

* [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api)
* [Get Token API](ref:get_token_api)

## HMAC authorization headers

Selected PayU product APIs authenticate with signed headers:

| Header | Description |
| :----- | :---------- |
| `date` | Current date/time, for example `Wed, 28 Jun 2023 11:25:19 GMT` |
| `authorization` | HMAC signature string including username, algorithm, headers list, and signature |

### Authorization field components

| Field | Description |
| :---- | :---------- |
| `username` | Merchant/client identifier (merchant key) |
| `algorithm` | Hash algorithm — use `sha512` |
| `headers` | Header names included in the signature (commonly `date`) |
| `signature` | Hex digest of the hashed string |

### Hashing algorithm

```
sha512(<Body data> + '|' + date + '|' + merchant_secret)
```

Where `<Body data>` is the request body posted with the call.

### Sample authorization header construction

```javascript
var merchant_key = '<merchant_key>';
var merchant_secret = '<merchant_salt>';
var date = new Date().toUTCString();
var data = request['data'] || '';
var hash_string = data + '|' + date + '|' + merchant_secret;
var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
var authorization =
  'hmac username="' + merchant_key + '", ' +
  'algorithm="sha512", headers="date", signature="' + hash + '"';
```

Use this pattern only for APIs that document HMAC header authentication.

## Callback and webhook receiver expectations

Your `surl` / `furl` and webhook endpoints should:

* Accept PayU-posted form or JSON payloads as documented for that event
* Verify reverse hash / signature before updating business state
* Respond quickly with HTTP 2xx on successful receipt

See [Webhooks and Callbacks](doc:webhooks-and-callbacks).

## What to read next

* [API Authentication and Security](doc:api-authentication-and-security)
* [Request and Response Format](doc:rest-api-format)
* [Making Your First API Request](doc:making-your-first-api-request)

## Related APIs

* [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
* [Verify Payment API](ref:verify_payment_api)
* [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api)
