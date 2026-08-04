---
title: FAQs
deprecated: false
hidden: true
metadata:
  robots: index
---
## Getting started

### Where should I start with PayU APIs?

Start with [API Introduction](doc:api-introduction), then [Which API should I use?](doc:which-api-should-i-use), then [Making Your First API Request](doc:making-your-first-api-request). Use [API Reference](ref:introduction-api-reference) for exact endpoint schemas.

### What is the difference between Integration Guides and API Reference?

Integration Guides explain end-to-end product setup and UX flows. API Reference documents request/response contracts and Try It calls. API Introduction explains shared concepts used by both.

## Authentication

### Do all PayU APIs use the same authentication?

No. Most Payment Gateway APIs use merchant key + salt + SHA-512 hash. Payouts and Partner APIs typically use OAuth. Some product APIs use HMAC headers. See [API Authentication and Security](doc:api-authentication-and-security).

### Where do I get key and salt?

From the PayU Dashboard. See [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).

### Can I generate hash in the browser?

You can prototype there, but production hash generation must happen on your server so the salt is never exposed.

## Environments and URLs

### Is there one base URL for all PayU APIs?

No. Collect Payment, General APIs, OAuth products, BBPS, and others use different hosts. See [API Environments and Base URLs](doc:api-environments-and-base-urls).

### Can I use Test key with Production URL?

No. Keep environment, key, and salt matched as a set.

## Payments and verification

### Why do I need Verify Payment if I already got a success callback?

Callbacks can be delayed, duplicated, or manipulated in the browser channel. Verify Payment (or an equivalent server API) is the reliable source of truth.

### What should I do if the customer closes the app before redirect?

Store the `txnid`, listen for webhooks, and call Verify Payment / transaction detail APIs to reconcile.

## Webhooks

### Are webhooks mandatory?

Strongly recommended for production-grade reliability, especially for async payment modes and refunds. See [Webhooks and Callbacks](doc:webhooks-and-callbacks).

### Can the same webhook arrive more than once?

Yes. Design handlers to be idempotent.

## Versioning

### What is `api_version`?

A request parameter used by many Collect Payment/feature flows to select a capability set. It can change required fields and hash input. See [API Versioning](doc:api-versioning).

## Tools

### Does PayU provide SDKs and Postman collections?

Yes. See [SDKs, Postman, and Tools](doc:sdks-postman-and-tools).

### Why does Try It fail for my API?

Some APIs/flows are not supported in Test or in the Try It playground. Check limitations on [API Reference introduction](ref:introduction-api-reference).

## Support

### How do I get help?

1. Use [API Troubleshooting](doc:api-troubleshooting)
2. Check [Error Codes](ref:error-codes)
3. Raise a ticket at [https://help.payu.in](https://help.payu.in) with `txnid`/request IDs and sanitized logs

## What to read next

- [API Best Practices](doc:api-best-practices)
- [Common API Workflows](doc:common-api-workflows)
- [Testing PayU APIs](doc:testing-payu-apis)
- [API Reference](ref:introduction-api-reference)

## Related APIs

- [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
- [Verify Payment API](ref:verify_payment_api)
- [Create Payment Link API](ref:create-payment-links)