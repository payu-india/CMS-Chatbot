---
title: Request and Response Format
excerpt: >-
  Understand PayU request and response formats for General APIs and how they
  differ from Collect Payment (_payment) and OAuth product APIs.
deprecated: false
hidden: false
metadata:
  title: PayU API Request and Response Format
  description: >-
    Learn PayU REST API request and response formats for General APIs, including
    key, command, hash, var parameters, JSON responses, and how _payment
    requests differ.
  keywords:
    - PayU REST API format
    - PayU API request format
    - PayU API response format
    - PayU General API command
    - PayU postservice API
  robots: index
next:
  description: ''
---
PayU exposes multiple API styles. This page explains the shared **General API** request/response contract and how it differs from Collect Payment (`_payment`) and OAuth product APIs.

PayU General APIs are server-to-server calls from your server to PayU. The basic execution pattern is consistent across many web-service commands, while each command has its own `var` parameter meanings.

> 📘 cURL walkthrough
>
> For a hands-on walkthrough of making API calls with cURL, see the [cURL Walkthrough recipe](https://payu-hosted-checkout.readme.io/v1/recipes/curl-walkthrough).

## General APIs — base URLs

| Environment | Base URL |
| :---------- | :------- |
| Test | `https://test.payu.in/merchant/postservice.php?form=2` |
| Production | `https://info.payu.in/merchant/postservice.php?form=2` |

> 📘 Note
>
> These base URLs are for **General APIs**. For `_payment` endpoints, use:
>
> * [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
> * [Collect Payment API — Merchant Hosted Checkout](ref:_payment_merchant_hosted)
> * [Collect Payment API — S2S](ref:_payment_server_to_server)
>
> Full host map: [API Environments and Base URLs](doc:api-environments-and-base-urls).

## General APIs — request format

| Parameter | Description | Sample value |
| :-------- | :---------- | :----------- |
| `key` | Merchant key provided by PayU. See [Access Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy). | `Ibibo` |
| `command` | Name of the web service to execute. | `verify_payment` |
| `hash` | SHA-512 hash calculated at your end. For General APIs: `sha512(key\|command\|var1\|salt)`. For `_payment` hashing, see [Generate Hash](doc:hashing-request-and-response). | `ajh84ba8abvav` |
| `var1` … `var15` | Command-specific variable parameters. Definitions are documented on each API Reference page. | Depends on command |

### Example General API request shape

```bash
curl -X POST 'https://test.payu.in/merchant/postservice.php?form=2' \
  -d 'key=<YOUR_KEY>' \
  -d 'command=verify_payment' \
  -d 'hash=<YOUR_HASH>' \
  -d 'var1=<TXNID>'
```

## General APIs — response format

To receive JSON, append **`form=2`** to the General API endpoint:

`https://test.payu.in/merchant/postservice.php?form=2`

| Parameter | Description | Example |
| :-------- | :---------- | :------ |
| `status` | Web service call status: `1` succeeded, `0` failed | `0` |
| `msg` | Reason string | `Parameter missing or token is empty...` |
| `transaction_details` | Present for many transaction commands; may include `mihpayid`, `request_id`, `bank_ref_num`, and more | Object / map of txn details |
| `request_id` | PayU request ID for an action within a transaction (for example, a refund request) | `7800456` |
| `bank_ref_num` | Bank reference number when provided after a successful action | `204519474956` |

Exact response fields vary by `command`. Always validate using the corresponding API Reference response schema.

## Collect Payment (`_payment`) request format

Collect Payment requests use payment fields rather than `command`/`var1` style parameters.

Common fields include:

* `key`, `txnid`, `amount`, `productinfo`
* `firstname`, `email`, `phone`
* `surl`, `furl`
* `hash`
* payment-method fields such as `pg`, `bankcode`, and mode-specific values

Content type is typically `application/x-www-form-urlencoded`.

See:

* [Headers and Content Types](doc:headers-and-content-types)
* [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)

## OAuth product request format

OAuth products usually:

1. Call a token endpoint with client/merchant credentials.
2. Call resource endpoints with the issued access token.
3. Use JSON request/response bodies more often than form-encoded General APIs.

Start with the product’s token API, for example [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api).

## Pagination, idempotency, and rate behavior

PayU APIs are product-specific for these concerns:

| Concern | What to know |
| :------ | :----------- |
| **Pagination** | Some list APIs (for example, payment links or settlement/on-hold queries) accept page/offset parameters. Use the parameters documented on that API page. |
| **Idempotency** | Use a unique `txnid` for every new payment attempt. Treat webhook deliveries as at-least-once and process them idempotently. |
| **Rate limiting** | Exceeding request burst limits can return temporary throttling errors. Back off and retry safely. |

## What to read next

* [API Authentication and Security](doc:api-authentication-and-security)
* [Headers and Content Types](doc:headers-and-content-types)
* [Making Your First API Request](doc:making-your-first-api-request)
* [Error Handling for APIs](doc:error-handling-for-apis)

## Related APIs

* [Verify Payment API](ref:verify_payment_api)
* [Check Transaction APIs](ref:check-transaction-apis)
* [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
