---
title: API Authentication and Security
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU uses multiple authentication types for every product. Most Payment Gateway APIs authenticate with your merchant key and a SHA-512 hash derived from your salt. Payouts and Partner APIs typically use OAuth. Some product APIs use HMAC signed headers.

This page is the unified authentication entry point for PayU APIs.

## Security Best Practices

Follow these best practices during authentication:

- [x] **Never expose salt or client secrets in frontend code**, mobile apps, or public repositories.

- [x] **Generate hashes on your server** for every payment and General API request.

- [x] **Validate reverse hash** on every surl/furl callback and webhook payload before trusting the status.

- [x] **Use test credentials for testing**; switch key, salt, and base URLs together at go-live.

- [x] **Rotate credentials** through the Dashboard if compromise is suspected.

- [x] **Enforce HTTPS** for all callbacks (`surl`, `furl`) and webhook endpoints.

- [x] **Treat browser redirects as untrusted** and confirm with Verify Payment or an equivalent server API.

## Authentication Models at a Glance

| Model                                               | How it works                                                               | Used by                                                        |
| :-------------------------------------------------- | :------------------------------------------------------------------------- | :------------------------------------------------------------- |
| `key`**&#x20;+&#x20;**`salt`**&#x20;+&#x20;**`hash` | Send `key` in the request body and a `hash` computed with your salt        | Collect Payment (`_payment`), General APIs, other PG features  |
| **OAuth 2.0**                                       | Exchange credentials for an access token, and call product APIs            | Payouts and Partner integration / onboarding                   |
| **HMAC headers**                                    | Sign request body + date with merchant secret; send `authorization` header | Selected product APIs (for example, some wallet/rewards flows) |

<Callout icon="📘" theme="info">
  ### Get Your Credentials First

  Generate your Test and Production key and salt from the PayU Dashboard:

  - [Generate Test Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard)
  - [Generate Production Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard)

  For Integration API testing, documentation examples may use a static Test key such as `JPTXg`. Always replace sample keys with your own credentials before go-live.
</Callout>

## `key` + `salt` + `hash` Authentication

When you post requests to Payment or General APIs, you include the merchant key as a request parameter. Requests are accompanied by a `hash` calculated on your server using your salt. A separate HTTP Basic authentication is not required for these APIs. Below are the different hash logics available:

<Accordion title="Payment API (_payment) Hash Logic" icon="far fa-hashtag-lock">
  This is the hash logic for posting Collect Payment (`_payment`) parameters.

  ```text _payment Hash Logic
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
  ```

  Refer to [Generate Hash](doc:hashing-request-and-response) for more information about complete hashing rules, optional fields, and reverse hashing.
</Accordion>

<Accordion title="General APIs Hash Logic" icon="far fa-grip-lines-vertical">
  Below is the hash logic for command-based General APIs such as Verify Payment, Get BIN Info, and Refund Transaction.

  ```
  sha512(key|command|var1|salt)
  ```
</Accordion>

<Accordion title="Feature-specific Hash Logics" icon="far fa-file-signature">
  These are the feature-specific hash logics.

  | **Feature**           | Logic                                                                                                                        |
  | --------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
  | **SI / Subscription** | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|si_details\|SALT)`        |
  | **TPV**               | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|beneficiarydetail\|SALT)` |
  | **Split Settlements** | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT\|splitRequest)`      |
</Accordion>

<Accordion title="_payment with api_version=19 Hash Logic " icon="far fa-gear-complex-api">
  This is the hash logic for `_payment` with `api_version=19` . Hash formulas can change with API version and enabled features.

  ```
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|user_token|offer_key|offer_auto_apply|cart_details|extra_charges|phone)
  ```
</Accordion>

## OAuth Authentication

You should use OAuth when integrating products that issue access tokens. This is the OAuth flow

1. Obtain client credentials or merchant credentials for the product.
2. Call the token endpoint in Test or Production.
3. Send the access token with subsequent product API requests as required by that product.
4. Refresh or regenerate tokens according to product expiry rules.

<Accordion title="Products and APIs" icon="far fa-gear-complex-api">
  | Product                     | Token APIs                                                                                            |
  | :-------------------------- | :---------------------------------------------------------------------------------------------------- |
  | Payouts                     | [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api) |
  | Partner integration         | [Get Token API](ref:get_token_api)                                                                    |
  | Partner merchant onboarding | [Step 00 — Authentication](ref:step-00-authentication)                                                |
</Accordion>

OAuth hosts differ from `_payment` and General API hosts. Refer to [API Environments and Base URLs](doc:api-environments-and-base-urls) for more information.

## HMAC Header Authentication

Some PayU product APIs authenticate with signed headers instead of a body `hash` parameter.

<Accordion title="Common Headers" icon="far fa-table-cells-header-lock">
  | Header          | Purpose                                                                           |
  | :-------------- | :-------------------------------------------------------------------------------- |
  | `date`          | Current UTC date/time used in the signature input                                 |
  | `authorization` | HMAC signature payload including username, algorithm, headers list, and signature |
</Accordion>

<Accordion title="Signature Input Pattern" icon="far fa-file-signature">
  ```
    sha512(<Body data> + '|' + date + '|' + merchant_secret)
  ```
</Accordion>
