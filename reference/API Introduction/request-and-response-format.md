---
title: Request and Response Format
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU exposes multiple API styles. This page explains the shared **General API** request/response contract and how it differs from Collect Payment (`_payment`) and OAuth product APIs.

PayU General APIs are server-to-server calls from your server to PayU. The basic execution pattern is consistent across many web-service commands, while each command has its own `var` parameter meanings.

<Callout icon="📘" theme="info">
  ### cURL Walkthrough

  For a hands-on walkthrough of making API calls with cURL, see the [cURL Walkthrough recipe](https://payu-hosted-checkout.readme.io/v1/recipes/curl-walkthrough).
</Callout>

## General API Base URLs

Go through the base URLs of general APIs before proceeding with the next section.

<Accordion title="General API Request Format" icon="far fa-code">
  ```curl cURL - Example Request
  curl -X POST 'https://test.payu.in/merchant/postservice.php?form=2' \
    -d 'key=<YOUR_KEY>' \
    -d 'command=verify_payment' \
    -d 'hash=<YOUR_HASH>' \
    -d 'var1=<TXNID>'
  ```
</Accordion>

<Accordion title="Parameter and Description" icon="far fa-table">
  | Parameter        | Description                                                                                                                                                               | Sample value       |
  | :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------- |
  | `key`            | Merchant key provided by PayU. Refer to [Access Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy) for more information.                                     | `Ibibo`            |
  | `command`        | Name of the web service to execute.                                                                                                                                       | `verify_payment`   |
  | `hash`           | SHA-512 hash calculated at your end. For General APIs: `sha512(key\|command\|var1\|salt)`. For `_payment` hashing, see [Generate Hash](doc:hashing-request-and-response). | `ajh84ba8abvav`    |
  | `var1` … `var15` | Command-specific variable parameters. Definitions are documented on each API Reference page.                                                                              | Depends on command |
</Accordion>

<Accordion title="General API Response Format" icon="far fa-code">
  To receive JSON, append `form=2` to the General API endpoint. For example:

  ```text Example
  https://test.payu.in/merchant/postservice.php?form=2
  ```
</Accordion>

<Accordion title="Parameter and Description" icon="far fa-table">
  | Parameter             | Description                                                                                           | Example                                  |
  | :-------------------- | :---------------------------------------------------------------------------------------------------- | :--------------------------------------- |
  | `status`              | Web service call status: `1` succeeded, `0` failed                                                    | `0`                                      |
  | `msg`                 | Reason string                                                                                         | `Parameter missing or token is empty...` |
  | `transaction_details` | Present for many transaction commands; may include `mihpayid`, `request_id`, `bank_ref_num`, and more | Object / map of txn details              |
  | `request_id`          | PayU request ID for an action within a transaction (for example, a refund request)                    | `7800456`                                |
  | `bank_ref_num`        | Bank reference number when provided after a successful action                                         | `204519474956`                           |
</Accordion>

Exact response fields vary by `command`. Always validate using the corresponding API reference response schema.

## Collect Payment (`_payment`) Request Format

Collect Payment requests use payment fields rather than `command`/`var1` style parameters.

Common fields include:

- `key`, `txnid`, `amount`, `productinfo`
- `firstname`, `email`, `phone`
- `surl`, `furl`
- `hash`
- payment-method fields such as `pg`, `bankcode`, and mode-specific values

Content type is typically `application/x-www-form-urlencoded`.

## OAuth Product Request Format

OAuth products usually:

1. Call a token endpoint with client/merchant credentials.
2. Call resource endpoints with the issued access token.
3. Use JSON request/response bodies more often than form-encoded general APIs.

## Pagination, Idempotency, and Rate Behavior

PayU APIs are product-specific for these concerns:

| Concern           | What to know                                                                                                                                             |
| :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pagination**    | Some list APIs (for example, payment links or settlement/on-hold queries) accept page/offset parameters. Use the parameters documented on that API page. |
| **Idempotency**   | Use a unique `txnid` for every new payment attempt. Treat webhook deliveries as at-least-once and process them idempotently.                             |
| **Rate limiting** | Exceeding request burst limits can return temporary throttling errors. Back off and retry safely.                                                        |
