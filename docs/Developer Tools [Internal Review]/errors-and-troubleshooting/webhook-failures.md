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

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'error_code': '`Webhook delivery failed`',
        'error_message': '`PayU delivery status is Failed.`',
        'recommended_fix': 'Check endpoint reachability, HTTP status, content type handling, and application logs.'
      },
      {
        'error_code': '`401`, `403`, `404`, `405`, `500`, `502`, `503`, `504`',
        'error_message': '`response_code contains an HTTP failure.`',
        'recommended_fix': 'Use the HTTP failure table below to fix auth, route, method, firewall, or server issues.'
      },
      {
        'error_code': '`Delivery message present`',
        'error_message': '`webhook_delivery_message contains HTTP error text.`',
        'recommended_fix': 'Inspect the response body and fix the endpoint behavior reported by PayU.'
      },
      {
        'error_code': '`Missing server callback`',
        'error_message': '`Browser redirect was received, but server-side webhook was not.`',
        'recommended_fix': 'Verify webhook configuration, allow PayU IPs, and confirm the endpoint accepts PayU POST callbacks.'
      }
    ]}
  />
</Accordion>

## Sample Webhook Delivery Failure

<Accordion title="Sample Payload" icon="far fa-code">
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

<Accordion title="Common Causes" icon="fab fa-creative-commons">
  - Endpoint does not allow `POST`.
  - Endpoint accepts `application/json` only; PayU may send form data or `application/x-www-form-urlencoded`.
  - WAF/firewall blocks PayU IPs.
  - Endpoint requires browser session authentication.
  - Handler performs slow business logic before returning response.
  - Duplicate webhook caused a database uniqueness error.
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

<Callout icon="👍" theme="info">
  ### **Handy Tips**

  A webhook handler should be boring: authenticate, validate hash, persist, return `2xx`, then process asynchronously.
</Callout>

## Common HTTP Failures

These are some common HTTP failures.

<Accordion title="Error and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'error_code': 'Webhook delivery failed',
        'error_message': 'Delivery status = `Failed`',
        'description': 'PayU could not deliver webhook.',
        'possible_cause': 'Endpoint unreachable, server down, invalid response handling.',
        'recommended_fix': 'Ensure endpoint is publicly reachable, returns 2xx, and logs requests.'
      },
      {
        'error_code': 'Missing server callback',
        'error_message': 'No webhook received',
        'description': 'Browser redirect occurred but webhook missing.',
        'possible_cause': 'Webhook URL misconfigured or blocked.',
        'recommended_fix': 'Verify webhook URL, allow PayU IPs, and accept POST requests.'
      },
      {
        'error_code': 'Delivery message present',
        'error_message': '`webhook_delivery_message` contains error',
        'description': 'Webhook failure details returned by endpoint.',
        'possible_cause': 'Endpoint returned error response.',
        'recommended_fix': 'Inspect response body and fix endpoint logic.'
      },
      {
        'error_code': '`401`',
        'error_message': '`401 Unauthorized`',
        'description': 'Merchant endpoint rejected authentication.',
        'possible_cause': 'Endpoint requires auth not supported by PayU.',
        'recommended_fix': 'Remove auth or use webhook-compatible validation.'
      },
      {
        'error_code': '`403`',
        'error_message': '`403 Forbidden`',
        'description': 'Merchant endpoint blocked PayU.',
        'possible_cause': 'Firewall, WAF, or IP restrictions.',
        'recommended_fix': 'Allowlist PayU IPs and review firewall rules.'
      },
      {
        'error_code': '`404`',
        'error_message': '`404 Not Found`',
        'description': 'Webhook route not found.',
        'possible_cause': 'Incorrect URL or route not deployed.',
        'recommended_fix': 'Fix endpoint URL and redeploy service.'
      },
      {
        'error_code': '`405`',
        'error_message': '`405 Method Not Allowed`',
        'description': 'Endpoint does not accept POST.',
        'possible_cause': 'Route configured for wrong HTTP method.',
        'recommended_fix': 'Enable POST on webhook endpoint.'
      },
      {
        'error_code': '`415`',
        'error_message': '`415 Unsupported Media Type`',
        'description': 'Content type rejected.',
        'possible_cause': 'Server expects JSON only.',
        'recommended_fix': 'Accept `application/x-www-form-urlencoded`.'
      },
      {
        'error_code': '`5xx`',
        'error_message': '`500`, `502`, `503`, `504`',
        'description': 'Server error while processing webhook.',
        'possible_cause': 'Backend failure, timeout, dependency issue.',
        'recommended_fix': 'Check logs, implement retries, process async.'
      },
      {
        'error_code': '`94`',
        'error_message': 'DUPLICATE_TRANSACTION',
        'description': 'Duplicate transaction detected.',
        'possible_cause': 'Same transaction attempted multiple times.',
        'recommended_fix': 'Use unique transaction IDs and idempotency checks.'
      },
      {
        'error_code': '`E202`',
        'error_message': 'INVALID_REQUEST (duplicate mismatch)',
        'description': 'Transaction already processed with different parameters.',
        'possible_cause': 'Parameter mismatch for same txn ID.',
        'recommended_fix': 'Ensure consistent parameters for retries.'
      },
      {
        'error_code': '`E4150`',
        'error_message': 'THE REQUEST IS DUPLICATE',
        'description': 'Duplicate API request.',
        'possible_cause': 'Repeated submission.',
        'recommended_fix': 'Prevent duplicate retries using idempotency keys.'
      },
      {
        'error_code': '`E1206`',
        'error_message': 'Order already exists',
        'description': 'Duplicate order creation attempt.',
        'possible_cause': 'Same order ID reused.',
        'recommended_fix': 'Check before creating new order.'
      },
      {
        'error_code': '`91`',
        'error_message': 'Issuer unavailable',
        'description': 'Bank not reachable.',
        'possible_cause': 'Network or bank downtime.',
        'recommended_fix': 'Retry with exponential backoff.'
      },
      {
        'error_code': '`E4013`',
        'error_message': 'Beneficiary timeout',
        'description': 'Transaction timed out.',
        'possible_cause': 'Slow bank response.',
        'recommended_fix': 'Retry safely with timeout handling.'
      },
      {
        'error_code': '`3DS_METHOD_NEGATIVE`',
        'error_message': '3DS method no response',
        'description': '3DS authentication timeout.',
        'possible_cause': 'Network/browser delay.',
        'recommended_fix': 'Ensure proper 3DS handling and fallback.'
      },
      {
        'error_code': '`E214`',
        'error_message': 'CURL_CALL_FAILURE',
        'description': 'Network/API communication failure.',
        'possible_cause': 'Connectivity issues with bank.',
        'recommended_fix': 'Retry with backoff and monitor failures.'
      },
      {
        'error_code': '`E310`',
        'error_message': 'Card declined (lost/stolen)',
        'description': 'Transaction declined by bank.',
        'possible_cause': 'Card flagged by issuer.',
        'recommended_fix': 'Ask user to use another payment method.'
      },
      {
        'error_code': '`AUTHNEGATIVE`',
        'error_message': 'Authorization failed',
        'description': 'Bank declined transaction.',
        'possible_cause': 'Risk rules or insufficient funds.',
        'recommended_fix': 'Retry or use alternate method.'
      },
      {
        'error_code': '`E1703`',
        'error_message': 'Blocked cardholder',
        'description': 'Card blocked due to risk.',
        'possible_cause': 'Security restriction.',
        'recommended_fix': 'Retry after verification or use different card.'
      },
      {
        'error_code': '`E205`',
        'error_message': 'Invalid parameter',
        'description': 'Invalid request fields.',
        'possible_cause': 'Incorrect CVV, expiry, or format.',
        'recommended_fix': 'Validate input before sending request.'
      },
      {
        'error_code': '`E4154`',
        'error_message': 'FORMATION IS NOT PROPER',
        'description': 'Malformed request.',
        'possible_cause': 'Incorrect payload structure.',
        'recommended_fix': 'Fix request formatting.'
      },
      {
        'error_code': '`E4047`',
        'error_message': 'Invalid amount',
        'description': 'Amount format incorrect.',
        'possible_cause': 'Wrong decimal or mismatch.',
        'recommended_fix': 'Validate amount before request.'
      },
      {
        'error_code': '`E4048`',
        'error_message': 'Amount mismatch',
        'description': 'Payer and payee mismatch.',
        'possible_cause': 'Calculation inconsistency.',
        'recommended_fix': 'Ensure totals match exactly.'
      },
      {
        'error_code': '`E4011`',
        'error_message': 'Payment details mismatch',
        'description': 'Request data inconsistent.',
        'possible_cause': 'Incorrect parameter mapping.',
        'recommended_fix': 'Validate request data consistency.'
      },
      {
        'error_code': '`E000`',
        'error_message': 'AUTHERROR',
        'description': 'Authentication or state issue.',
        'possible_cause': 'Invalid request state.',
        'recommended_fix': 'Verify transaction flow and credentials.'
      },
      {
        'error_code': '`15005`',
        'error_message': 'Command not authorized',
        'description': 'Permission issue.',
        'possible_cause': 'Merchant config restriction.',
        'recommended_fix': 'Check account configuration.'
      },
      {
        'error_code': '`E4042`',
        'error_message': 'Invalid verification token',
        'description': 'Token validation failed.',
        'possible_cause': 'Incorrect token generation.',
        'recommended_fix': 'Regenerate and validate token.'
      },
      {
        'error_code': '`E2401`',
        'error_message': 'Customer not eligible',
        'description': 'User not eligible for transaction.',
        'possible_cause': 'Risk or lender rules.',
        'recommended_fix': 'Offer alternate payment options.'
      },
      {
        'error_code': '`E2403`',
        'error_message': 'KYC pending',
        'description': 'User verification incomplete.',
        'possible_cause': 'Missing KYC.',
        'recommended_fix': 'Prompt user to complete KYC.'
      },
      {
        'error_code': '`E2405`',
        'error_message': 'Invalid tenure',
        'description': 'Selected tenure unavailable.',
        'possible_cause': 'Invalid option selection.',
        'recommended_fix': 'Show valid tenure options.'
      },
      {
        'error_code': '`E2415`',
        'error_message': 'Account blocked',
        'description': 'Customer account restricted.',
        'possible_cause': 'Lender block.',
        'recommended_fix': 'Contact provider or use different method.'
      },
      {
        'error_code': '`E4010`',
        'error_message': 'Transaction not permitted',
        'description': 'Account restriction.',
        'possible_cause': 'Bank limitation.',
        'recommended_fix': 'Use another account/payment method.'
      },
      {
        'error_code': '`E4040`',
        'error_message': 'International disabled',
        'description': 'Cross-border not enabled.',
        'possible_cause': 'Feature not activated.',
        'recommended_fix': 'Enable international transactions.'
      },
      {
        'error_code': '`E1903`',
        'error_message': 'Invalid pg_instance_id',
        'description': 'Configuration error.',
        'possible_cause': 'Incorrect PayU setup.',
        'recommended_fix': 'Verify merchant configuration.'
      },
      {
        'error_code': '`SYSTEM_ERROR`',
        'error_message': 'System failure',
        'description': 'Internal processing error.',
        'possible_cause': 'Platform instability.',
        'recommended_fix': 'Retry with monitoring and logging.'
      },
      {
        'error_code': '`E1500`',
        'error_message': 'Retry not allowed',
        'description': 'Retry blocked due to state.',
        'possible_cause': 'Invalid retry attempt.',
        'recommended_fix': 'Avoid retrying completed/failed txn incorrectly.'
      },
      {
        'error_code': '`50305`',
        'error_message': 'Invalid transaction state',
        'description': 'Wrong lifecycle state.',
        'possible_cause': 'Incorrect API sequence.',
        'recommended_fix': 'Follow correct transaction flow.'
      },
      {
        'error_code': '`E4153`',
        'error_message': 'REQUEST NOT FOUND',
        'description': 'Missing transaction reference.',
        'possible_cause': 'Invalid request ID.',
        'recommended_fix': 'Verify request identifiers.'
      },
      {
        'error_code': '`E207`',
        'error_message': 'Connection failure',
        'description': 'API communication issue.',
        'possible_cause': 'Network or endpoint failure.',
        'recommended_fix': 'Retry with proper error handling.'
      }
    ]}
  />
</Accordion>
