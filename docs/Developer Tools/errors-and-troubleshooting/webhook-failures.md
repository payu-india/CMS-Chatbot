---
title: Webhook Failures
excerpt: >-
  Debug PayU payment webhook delivery failures, HTTP errors, content-type
  issues, hash validation, and idempotency.
deprecated: false
hidden: true
metadata:
  robots: index
---
Webhook failures occur when PayU sends a server-to-server callback but your endpoint does not accept or process it successfully.

## When these Errors Occur

<Accordion title="My Accordion Title" icon="fa-info-circle">

<SearchableTable
  headers={['Error code / type', 'Error message or HTTP response', 'Recommended fix']}
  rows={[
    ['`Webhook delivery failed`', '`PayU delivery status is Failed.`', 'Check endpoint reachability, HTTP status, content type handling, and application logs.'],
    ['`401`, `403`, `404`, `405`, `500`, `502`, `503`, `504`', '`response_code contains an HTTP failure.`', 'Use the HTTP failure table below to fix auth, route, method, firewall, or server issues.'],
    ['`Delivery message present`', '`webhook_delivery_message contains HTTP error text.`', 'Inspect the response body and fix the endpoint behavior reported by PayU.'],
    ['`Missing server callback`', '`Browser redirect was received, but server-side webhook was not.`', 'Verify webhook configuration, allow PayU IPs, and confirm the endpoint accepts PayU POST callbacks.'],
  ]}
  placeholder="Search errors..."
/>
</Accordion>

## Sample Webhook Delivery Failure

<Accordion title="Sample Payload" icon="fa-code">

Here is the sample payload of the webhook delivery failure.

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

</Accordion>

## Root Cause

The root cause of the failure is, your webhook endpoint rejected PayU's request or failed while processing it. Below are the common causes of such issues.

<Accordion title="Common Causes" icon="fa-error">
  * Endpoint does not allow `POST`.
  * Endpoint accepts `application/json` only; PayU may send form data or `application/x-www-form-urlencoded`.
  * WAF/firewall blocks PayU IPs.
  * Endpoint requires browser session authentication.
  * Handler performs slow business logic before returning response.
  * Duplicate webhook caused a database uniqueness error.
</Accordion>

## Troubleshooting

Now that you know the issue and the root cause, let's see how to troubleshoot the issue.

<Accordion title="Troubleshooting Steps" icon="fa-wrench">
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
</Accordion>

<Callout icon="👍">
  **Handy Tips**

  A webhook handler should be boring: authenticate, validate hash, persist, return `2xx`, then process asynchronously.
</Callout>

## Common HTTP Failures

These are some common HTTP failures.

<Accordion title="Errors and Fixes" icon="fa-wrench">
  <SearchableTable
  headers={['Error code / type', 'Error message as returned by PayU', 'Description', 'Possible cause', 'Recommended fix']}
  rows={[
    ['`401`', '`401 Unauthorized`', 'Merchant endpoint rejected authentication.', 'Endpoint requires browser session, bearer token, or basic auth that PayU does not send.', 'Use webhook-specific authentication that PayU can satisfy, or allowlist PayU delivery safely.'],
    ['`403`', '`403 Forbidden`', 'Merchant endpoint blocked PayU.', 'Firewall, WAF, IP allowlist, or authorization rule blocked the callback.', 'Allow PayU IPs and check WAF rules.'],
    ['`404`', '`404 Not Found`', 'Webhook route was not found.', 'URL is incorrect, environment points to old route, or deployment is missing the route.', 'Correct the configured URL and redeploy the webhook route.'],
    ['`405`', '`HTTP/2 405` / `405 Method Not Allowed`', 'Endpoint does not accept PayU\'s HTTP method.', 'Route only accepts `GET` or another method.', 'Enable `POST` on the webhook route.'],
    ['`415`', '`415 Unsupported Media Type`', 'Endpoint rejected PayU\'s content type.', 'Handler accepts JSON only.', 'Accept form data and `application/x-www-form-urlencoded`.'],
    ['`5xx`', '`500 Internal Server Error`, `502`, `503`, `504`', 'Merchant server failed while handling webhook.', 'Handler exception, timeout, dependency outage, database failure.', 'Check application logs and dependencies. Persist payload first and process asynchronously.'],
  ]}
  placeholder="Search errors..."
/>
</Accordion>

## Webhook, Callback, and Endpoint Errors

These are webhook, callback, and endpoint errors, their description and recommended fixes.

<Accordion title="Errors and Fixes" icon="fa-wrench">
  <SearchableTable
  headers={['Error code / type', 'Error message as returned by PayU', 'Description', 'Possible cause', 'Recommended fix']}
  rows={[
    ['Webhook delivery failed', 'Delivery status = `Failed`', 'PayU could not deliver webhook.', 'Endpoint unreachable, server down, invalid response handling.', 'Ensure endpoint is publicly reachable, returns 2xx, and logs requests.'],

    ['Missing server callback', 'No webhook received', 'Browser redirect occurred but webhook missing.', 'Webhook URL misconfigured or blocked.', 'Verify webhook URL, allow PayU IPs, and accept POST requests.'],

    ['Delivery message present', '`webhook_delivery_message` contains error', 'Webhook failure details returned by endpoint.', 'Endpoint returned error response.', 'Inspect response body and fix endpoint logic.'],

    ['`401`', '`401 Unauthorized`', 'Merchant endpoint rejected authentication.', 'Endpoint requires auth not supported by PayU.', 'Remove auth or use webhook-compatible validation.'],

    ['`403`', '`403 Forbidden`', 'Merchant endpoint blocked PayU.', 'Firewall, WAF, or IP restrictions.', 'Allowlist PayU IPs and review firewall rules.'],

    ['`404`', '`404 Not Found`', 'Webhook route not found.', 'Incorrect URL or route not deployed.', 'Fix endpoint URL and redeploy service.'],

    ['`405`', '`405 Method Not Allowed`', 'Endpoint does not accept POST.', 'Route configured for wrong HTTP method.', 'Enable POST on webhook endpoint.'],

    ['`415`', '`415 Unsupported Media Type`', 'Content type rejected.', 'Server expects JSON only.', 'Accept `application/x-www-form-urlencoded`.'],

    ['`5xx`', '`500`, `502`, `503`, `504`', 'Server error while processing webhook.', 'Backend failure, timeout, dependency issue.', 'Check logs, implement retries, process async.'],

    ['`94`', 'DUPLICATE_TRANSACTION', 'Duplicate transaction detected.', 'Same transaction attempted multiple times.', 'Use unique transaction IDs and idempotency checks.'],

    ['`E202`', 'INVALID_REQUEST (duplicate mismatch)', 'Transaction already processed with different parameters.', 'Parameter mismatch for same txn ID.', 'Ensure consistent parameters for retries.'],

    ['`E4150`', 'THE REQUEST IS DUPLICATE', 'Duplicate API request.', 'Repeated submission.', 'Prevent duplicate retries using idempotency keys.'],

    ['`E1206`', 'Order already exists', 'Duplicate order creation attempt.', 'Same order ID reused.', 'Check before creating new order.'],

    ['`91`', 'Issuer unavailable', 'Bank not reachable.', 'Network or bank downtime.', 'Retry with exponential backoff.'],

    ['`E4013`', 'Beneficiary timeout', 'Transaction timed out.', 'Slow bank response.', 'Retry safely with timeout handling.'],

    ['`3DS_METHOD_NEGATIVE`', '3DS method no response', '3DS authentication timeout.', 'Network/browser delay.', 'Ensure proper 3DS handling and fallback.'],

    ['`E214`', 'CURL_CALL_FAILURE', 'Network/API communication failure.', 'Connectivity issues with bank.', 'Retry with backoff and monitor failures.'],

    ['`E310`', 'Card declined (lost/stolen)', 'Transaction declined by bank.', 'Card flagged by issuer.', 'Ask user to use another payment method.'],

    ['`AUTHNEGATIVE`', 'Authorization failed', 'Bank declined transaction.', 'Risk rules or insufficient funds.', 'Retry or use alternate method.'],

    ['`E1703`', 'Blocked cardholder', 'Card blocked due to risk.', 'Security restriction.', 'Retry after verification or use different card.'],

    ['`E205`', 'Invalid parameter', 'Invalid request fields.', 'Incorrect CVV, expiry, or format.', 'Validate input before sending request.'],

    ['`E4154`', 'FORMATION IS NOT PROPER', 'Malformed request.', 'Incorrect payload structure.', 'Fix request formatting.'],

    ['`E4047`', 'Invalid amount', 'Amount format incorrect.', 'Wrong decimal or mismatch.', 'Validate amount before request.'],

    ['`E4048`', 'Amount mismatch', 'Payer and payee mismatch.', 'Calculation inconsistency.', 'Ensure totals match exactly.'],

    ['`E4011`', 'Payment details mismatch', 'Request data inconsistent.', 'Incorrect parameter mapping.', 'Validate request data consistency.'],

    ['`E000`', 'AUTHERROR', 'Authentication or state issue.', 'Invalid request state.', 'Verify transaction flow and credentials.'],

    ['`15005`', 'Command not authorized', 'Permission issue.', 'Merchant config restriction.', 'Check account configuration.'],

    ['`E4042`', 'Invalid verification token', 'Token validation failed.', 'Incorrect token generation.', 'Regenerate and validate token.'],

    ['`E2401`', 'Customer not eligible', 'User not eligible for transaction.', 'Risk or lender rules.', 'Offer alternate payment options.'],

    ['`E2403`', 'KYC pending', 'User verification incomplete.', 'Missing KYC.', 'Prompt user to complete KYC.'],

    ['`E2405`', 'Invalid tenure', 'Selected tenure unavailable.', 'Invalid option selection.', 'Show valid tenure options.'],

    ['`E2415`', 'Account blocked', 'Customer account restricted.', 'Lender block.', 'Contact provider or use different method.'],

    ['`E4010`', 'Transaction not permitted', 'Account restriction.', 'Bank limitation.', 'Use another account/payment method.'],

    ['`E4040`', 'International disabled', 'Cross-border not enabled.', 'Feature not activated.', 'Enable international transactions.'],

    ['`E1903`', 'Invalid pg_instance_id', 'Configuration error.', 'Incorrect PayU setup.', 'Verify merchant configuration.'],

    ['`SYSTEM_ERROR`', 'System failure', 'Internal processing error.', 'Platform instability.', 'Retry with monitoring and logging.'],

    ['`E1500`', 'Retry not allowed', 'Retry blocked due to state.', 'Invalid retry attempt.', 'Avoid retrying completed/failed txn incorrectly.'],

    ['`50305`', 'Invalid transaction state', 'Wrong lifecycle state.', 'Incorrect API sequence.', 'Follow correct transaction flow.'],

    ['`E4153`', 'REQUEST NOT FOUND', 'Missing transaction reference.', 'Invalid request ID.', 'Verify request identifiers.'],

    ['`E207`', 'Connection failure', 'API communication issue.', 'Network or endpoint failure.', 'Retry with proper error handling.']
  ]}
  placeholder="Search errors..."
/>
</Accordion>