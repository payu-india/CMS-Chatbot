---
title: Headers and Content Types
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU API families expect different header and content-type conventions. Sending the wrong `Content-Type` or missing auth headers is a common first-integration failure.

## Common Content Types

| API family                   | Typical `Content-Type`                | Notes                                                                            |
| :--------------------------- | :------------------------------------ | :------------------------------------------------------------------------------- |
| Collect Payment (`_payment`) | `application/x-www-form-urlencoded`   | Payment fields posted as form data                                               |
| General APIs                 | `application/x-www-form-urlencoded`   | `key`, `command`, `hash`, `var1…` as form fields. Use `form=2` for JSON response |
| OAuth token APIs             | Product-specific (often form or JSON) | Follow the token API Reference page                                              |
| Product REST APIs            | Often `application/json`              | BBPS, some partner/onboarding, and newer product APIs                            |

## Headers for `key` + `hash` APIs

For most Collect Payment and General APIs, authentication values are part of the **request body** (`key`, `hash`), not an `Authorization` bearer header.

<Accordion title="Recommended Headers" icon="far fa-table-cells-header-unlock">
  ```http
    Content-Type: application/x-www-form-urlencoded
    Accept: application/json
  ```
</Accordion>

General APIs still rely on `form=2` in the URL for JSON responses.

## Headers for OAuth APIs

After you generate an access token:

- Store the token securely on your server.
- Send it on resource requests exactly as documented by that product (commonly an `Authorization` header).
- Regenerate/refresh on expiry.

## HMAC Authorization Headers

Selected PayU product APIs authenticate with signed headers:

<Accordion title="Header and Description" icon="far fa-heading">
  | Header          | Description                                                                      |
  | :-------------- | :------------------------------------------------------------------------------- |
  | `date`          | Current date/time, for example `Wed, 28 Jun 2023 11:25:19 GMT`                   |
  | `authorization` | HMAC signature string including username, algorithm, headers list, and signature |
</Accordion>

<Accordion title="Authorization Field Components" icon="far fa-pen-field">
  | Field       | Description                                              |
  | :---------- | :------------------------------------------------------- |
  | `username`  | Merchant/client identifier (merchant key)                |
  | `algorithm` | Hash algorithm — use `sha512`                            |
  | `headers`   | Header names included in the signature (commonly `date`) |
  | `signature` | Hex digest of the hashed string                          |
</Accordion>

<Accordion title="Hashing Algorithm" icon="far fa-hashtag-lock">
  ```
  sha512(<Body data> + '|' + date + '|' + merchant_secret)
  ```

  Where `<Body data>` is the request body posted with the call.
</Accordion>

<Accordion title="Sample Authorization Header Construction" icon="far fa-space-station-moon-construction">
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
</Accordion>

Use this pattern only for APIs that document HMAC header authentication.