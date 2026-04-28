---
title: Webhook Failures
excerpt: Debug PayU payment webhook delivery and processing issues.
deprecated: false
hidden: false
metadata:
  title: Webhook Failures
  description: Debug PayU payment webhook delivery failures, HTTP errors, content-type issues, hash validation, and idempotency.
  robots: index
next:
  description: ''
---

Webhook failures occur when PayU sends a server-to-server callback but your endpoint does not accept or process it successfully.

## When it occurs

Typical symptoms:

* PayU delivery status is `Failed`.
* `response_code` is `401`, `403`, `404`, `405`, `500`, `502`, `503`, or `504`.
* `webhook_delivery_message` contains HTTP error text.
* Browser redirect was received, but server-side webhook was not.

## Sample webhook delivery failure

```json
{
  "timestamp": "2026-02-27 14:24:45.000000",
  "event_type": "payment",
  "status": "Failed",
  "webhook_delivery_message": "HTTP/2 405",
  "http_method": "POST",
  "endpoint": "https://example.com/payu/webhook",
  "response_code": 405,
  "endpoint_latency": 7,
  "event_payload": {
    "mihpayid": "27472524682",
    "txnid": "txn_10004",
    "amount": "1.00",
    "status": "failure",
    "unmappedstatus": "failed",
    "error": "E500",
    "error_Message": "Bank failed to authenticate the customer",
    "hash": "response_hash"
  }
}
```

## Root cause

Your webhook endpoint rejected PayU's request or failed while processing it.

Common causes:

* Endpoint does not allow `POST`.
* Endpoint accepts `application/json` only; PayU may send form data or `application/x-www-form-urlencoded`.
* WAF/firewall blocks PayU IPs.
* Endpoint requires browser session authentication.
* Handler performs slow business logic before returning response.
* Duplicate webhook caused a database uniqueness error.

## Debugging guide

1. Confirm the webhook URL is configured for the correct merchant key.
2. Confirm endpoint is reachable publicly over HTTPS.
3. Allow PayU webhook IPs listed in [Webhooks for Payments](doc:webhooks).
4. Accept `POST` requests.
5. Accept form data and `application/x-www-form-urlencoded`.
6. Verify response hash and match `txnid`/`amount`.
7. Store the webhook payload durably before processing.
8. Return `2xx` after durable receipt.
9. Process fulfillment asynchronously.
10. Make updates idempotent using `mihpayid`, `txnid`, and event status.

> **Pro Tip**
>
> A webhook handler should be boring: authenticate, validate hash, persist, return `2xx`, then process asynchronously.

## Common HTTP failures

| HTTP status | Meaning | Fix |
| --- | --- | --- |
| `401` | Endpoint requires authentication PayU does not provide. | Use webhook-specific authentication that PayU can satisfy, or allowlist PayU delivery safely. |
| `403` | Firewall, WAF, or authorization rule blocked PayU. | Allow PayU IPs and check WAF rules. |
| `404` | Webhook URL is wrong or route is not deployed. | Correct the configured URL. |
| `405` | Endpoint does not accept `POST`. | Enable `POST` on the webhook route. |
| `415` | Unsupported content type. | Accept form data and `application/x-www-form-urlencoded`. |
| `5xx` | Merchant server failed. | Check application logs and dependencies. Queue processing. |
