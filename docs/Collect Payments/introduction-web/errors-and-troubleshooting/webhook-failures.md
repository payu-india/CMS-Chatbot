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

| Error code / type | Error message or HTTP response | Recommended fix |
| --- | --- | --- |
| Webhook delivery failed | PayU delivery status is `Failed`. | Check endpoint reachability, HTTP status, content type handling, and application logs. |
| `401`, `403`, `404`, `405`, `500`, `502`, `503`, `504` | `response_code` contains an HTTP failure. | Use the HTTP failure table below to fix auth, route, method, firewall, or server issues. |
| Delivery message present | `webhook_delivery_message` contains HTTP error text. | Inspect the response body and fix the endpoint behavior reported by PayU. |
| Missing server callback | Browser redirect was received, but server-side webhook was not. | Verify webhook configuration, allow PayU IPs, and confirm the endpoint accepts PayU POST callbacks. |

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

| Error code / type | Error message as returned by PayU | Description | Possible cause | Recommended fix |
| --- | --- | --- | --- | --- |
| `401` | `401 Unauthorized` | Merchant endpoint rejected authentication. | Endpoint requires browser session, bearer token, or basic auth that PayU does not send. | Use webhook-specific authentication that PayU can satisfy, or allowlist PayU delivery safely. |
| `403` | `403 Forbidden` | Merchant endpoint blocked PayU. | Firewall, WAF, IP allowlist, or authorization rule blocked the callback. | Allow PayU IPs and check WAF rules. |
| `404` | `404 Not Found` | Webhook route was not found. | URL is incorrect, environment points to old route, or deployment is missing the route. | Correct the configured URL and redeploy the webhook route. |
| `405` | `HTTP/2 405` / `405 Method Not Allowed` | Endpoint does not accept PayU's HTTP method. | Route only accepts `GET` or another method. | Enable `POST` on the webhook route. |
| `415` | `415 Unsupported Media Type` | Endpoint rejected PayU's content type. | Handler accepts JSON only. | Accept form data and `application/x-www-form-urlencoded`. |
| `5xx` | `500 Internal Server Error`, `502`, `503`, `504` | Merchant server failed while handling webhook. | Handler exception, timeout, dependency outage, database failure. | Check application logs and dependencies. Persist payload first and process asynchronously. |

<!-- PAYU_REPO_ERRORS_WEBHOOK_FAILURES_BEGIN -->

## Repo-backed webhook, callback, and endpoint errors

These rows are categorized from existing PayU repository error-code and troubleshooting documentation. Existing guidance on this page remains unchanged.

| Source doc | Error code / type | Error message / response indicator | Description | Recommended fix |
| --- | --- | --- | --- | --- |
| BNPL Error Codes | E2401 | The customer is not eligible for this transaction | - | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| BNPL Error Codes | E2415 | The customer’s account is blocked by the lender. | - | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | 3DS_METHOD_NEGATIVE | 3DS2 Method no response | Indicates that while the 3DS2 method data was sent successfully, no response was received at the notification URL within the expected timeframe. This could be due to network issues, timeout, or browser-related problems. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | 91 | E4158 | REQAUTH_TIME_ OUT_FOR_PAY | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | 94 | E504 | DUPLICATE_ TRANSACTION | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E000 | AUTHERROR | 50308 \| Wrong transaction state | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E1206 | AUCNEGATIVE | 5003 \| The order already exists in the database. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E1500 | Retry not allowed | RETRY_NOT_ALLOWED | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E1703 | AUTHNEGATIVE | 155007 \| Blocked first used-transaction from new cardholder and card not properly unblocked | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E1703 | AUTHNEGATIVE | 155008 \| Verification data failed | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E1903 | AUTHERROR | 50021 \| Bad pg_instance_id(null) passed! | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E1903 | AUTHERROR | 50021 \| unable to procees the transaction | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | 15005 \| Command not authorized. Please check / contact the merchant | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | 50305 \| Referenced transaction is not in the correct transaction state | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | 155007 \| Blocked first used-transaction from new cardholder and card not properly unblocked | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | 001 \| Shop 85997502 has been closed. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | 155008 \| Verification data failed | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | 15005 \| command not authorized | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | 001 \| Shop 72364500 has been closed. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | 500 \| SYSTEM_ERROR \| Request failed due to system error. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E202 | AUCNEGATIVE | INVALID_REQUEST \| Value '2741401246...1815942193' is invalid. A transaction with this transaction ID has already been processed but the request parameters do not match. To process a new transaction for this order, th... | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E202 | AUCNEGATIVE | INVALID_REQUEST \| Value '2741403236...1816062263' is invalid. A transaction with this transaction ID has already been processed but the request parameters do not match. To process a new transaction for this order, th... | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E205 | EVERROR | 50021 \| GENERAL ERROR | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E205 | EVERROR | 50021 \| XML Data Error - Invalid Parameter Value - card_exp_date | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E205 | EVERROR | 50021 \| Invalid cvd2 passed! | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E205 | EVERROR | 50021 \| Bad AcquiringBank configured for merchant_id(58853232) in pg_instance_id(37887779)! | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E205 | EVERROR | 50021 \| Bad AcquiringBank configured for merchant_id(36413568) in pg_instance_id(37887779)! | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E205 | EVERROR | 50021 \| XML Data Error - Invalid Parameter Value - ipaddress | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E205 | EVERROR | 50021 \| Bad Expiry year passed! | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E205 | EVERROR | 50021 \| Bad AcquiringBank configured for merchant_id(50756239) in pg_instance_id(37887779)! | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E205 | EVERROR | 50021 \| Issuer Authentication Server failure | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E205 | EVERROR | 50021 \| Bad AcquiringBank configured for merchant_id(83992952) in pg_instance_id(37887779)! | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E205 | EVERROR | 50021 \| Invalid tavv value | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E205 | EVERROR | 50021 \| SYSTEM ERROR | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E205 | Error at the Bank Server end | CURL_ERROR_ENROLLED | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E207 | AUCNEGATIVE | 5003 \| The order already exists in the database. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E207 | AUCNEGATIVE | 405 \| For example, the sending component is unable to establish connection to the receiving component. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E207 | AUCNEGATIVE | 404 \| Unkonwn Error. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E207 | AUCNEGATIVE | 5002 \| The merchant is not setup to support the requested service. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E207 | AUCNEGATIVE | 403 \| BANK API error occurred | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E207 | AUCNEGATIVE | 405 \| System Connection Failure | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E214 | 3DS_METHOD_ERROR | CURL_CALL_FAILURE | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E214 | 3DS_VERIFICATION_ERROR | CURL_CALL_FAILURE | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E214 | ACS_REDIRECT | CURL_CALL_FAILURE | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E214 | AUCERROR | CURL_CALL_FAILURE | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E214 | AUTHNEGATIVE | CURL_CALL_FAILURE | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E214 | AUTHNEGATIVE | 155009 | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E214 | The Bank servers are unreachable over the network | CURL_CALL_FAILURE | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E231 | 3DS_METHOD_NEGATIVE | CURL_CALL_FAILURE | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E231 | 3DS_VERIFICATION_NEGATIVE | CURL_CALL_FAILURE | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E231 | AUCNEGATIVE | 5003 \| The order already exists in the database. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E231 | AUCNEGATIVE | 405 \| System Connection Failure | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E231 | AUCNEGATIVE | 404 \| Unkonwn Error. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E231 | AUTHNEGATIVE | 50305 \| Referenced transaction is not in the correct transaction state | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E2401 | The customer is not eligible for this transaction | CUSTOMER_NOT_ELIGIBLE * FOR_THIS_TRANSACTION | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E2403 | Customer KYC is pending at Issuer's end | CUSTOMER_KYC_PENDING | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E2405 | Sorry, you are not eligible for the selected tenure. Please select another tenure | TENURE_NOT_FOUND | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E303 | AUCNEGATIVE | 5003 \| The order already exists in the database. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E307 | 404 | 404 | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E307 | 5006 | 5006 | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E308 | AUCNEGATIVE | 500\|Request failed due to system error. \| SYSTEM_ERROR | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E310 | AUTHNEGATIVE | 15041 \| transaction declined because card is lost | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E310 | AUTHNEGATIVE | 15043 \| DECLINED (stolen) | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E310 | AUTHNEGATIVE | 15043 \| transaction declined because card is stolen | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E310 | AUTHNEGATIVE | 15041 \| DECLINED(lost card) | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E335 | AUCNEGATIVE | 403 | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E335 | AUCNEGATIVE | 303 \| Access denied, invalid endpoint. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E335 | AUCNEGATIVE | 303 \| Access denied, invalid endpoint | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E335 | AUCNEGATIVE | 404 \| Permanent System Failure | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E335 | AUCNEGATIVE | 405 \| System connection failure. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E335 | AUCNEGATIVE | 404 \| Unkonwn Error. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E335 | AUCNEGATIVE | 405 | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E335 | AUCNEGATIVE | 405 \| System Connection Failure | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E335 | AUCNEGATIVE | 404 \| Failed to invoke CardData API | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E335 | EVNEGATIVE | 405 \| System connection failure. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E346 | 404 | 404 | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4010 | Transaction not allowed on/from the account | TRANSACTION NOT PERMITTED TO THE ACCOUNT | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4011 | MISMATCH IN PAYMENT DETAILS | MISMATCH IN PAYMENT DETAILS | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4012 | MOBILE NUMBER REGISTERED WITH MULTIPLE CUSTOMER IDS | MOBILE NUMBER REGISTERED WITH MULTIPLE CUSTOMER IDS | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4013 | Transaction failed due to beneficiary timeout | ACQUIRER/BENEFICIARY UNAVAILABLE(TIMEOUT) | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4014 | COMPLIANCE ERROR CODE FOR ACQUIRER | COMPLIANCE ERROR CODE FOR ACQUIRER | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4015 | COMPLIANCE ERROR CODE FOR ISSUER BD | COMPLIANCE ERROR CODE FOR ISSUER BD | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4016 | Transaction failed due to currency not supported | Country/ Currency not supported | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4019 | DUPLICATE RRN FOUND IN THE TRANSACTION. (BENEFICIARY) | DUPLICATE RRN FOUND IN THE TRANSACTION. (BENEFICIARY) | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4040 | International Service not activated/disabled | International Service not activated/disabled | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4042 | Invalid verification token | Invalid verification token | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4047 | PAYEE AMOUNTCUR IS INVALID | PAYEE AMOUNTCUR IS INVALID | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4048 | PAYER & PAYEE TOTAL AMOUNT NOT MATCHING | PAYER & PAYEE TOTAL AMOUNT NOT MATCHING | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4050 | PAYER AND PAYEE TOTAL AMOUNT NOT MATCHING | PAYER AND PAYEE TOTAL AMOUNT NOT MATCHING | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4052 | PAYER AMOUNT SHOULD BE GREATER THAN TOTAL PAYEE AMOUNT | PAYER AMOUNT SHOULD BE GREATER THAN TOTAL PAYEE AMOUNT | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4150 | Transaction declined due to duplicate request | THE REQUEST IS DUPLICATE | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4151 | Transaction failed due to amount limit on merchant exceeded | AMOUNT CAP IS EXCEEDED | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4153 | REQUEST IS NOT FOUND | REQUEST IS NOT FOUND | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4154 | FORMATION IS NOT PROPER | FORMATION IS NOT PROPER | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4157 | SYSTEM EXCEPTION | SYSTEM EXCEPTION | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4158 | AUCNEGATIVE | 96 \| SYSTEM ERROR | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4158 | AUTHNEGATIVE | 96 \| System malfunction | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4158 | AUTHNEGATIVE | 91 | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4158 | AUTHNEGATIVE | 96 \| System malfunction \| Payment processor error System malfunction | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4158 | AUTHNEGATIVE | 91 \| Issuer unavailable or switch inoperative | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4158 | AUTHNEGATIVE | 91 \| Issuer unavailable or switch inoperative \| Payment processor error Issuer inoperative or some other system problem | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4158 | AUTHNEGATIVE | 96 \| System malfunction, System malfunction or certain field error conditions | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4158 | AUTHNEGATIVE | 96 \| System malfunction \| We encountered a problem with Rupay processor: SYSTEM ERROR | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4158 | AUTHNEGATIVE | 96 \| SYSTEM ERROR | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4158 | AUTHNEGATIVE | 1 \| AUTHORIZATION_FAILED_BY_BANK | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4158 | AUTHNEGATIVE | 91 \| Authorisation declined by bank | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4158 | AUTHNEGATIVE | 96 \| Authorisation declined by bank | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4158 | AUTHNEGATIVE | 91 \| Issuer not available | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4158 | REDIRECT | 96 \| System malfunction | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4158 | Transaction failed due to timeout at acquirer's end | Issuer unavailable or switch inoperative | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4159 | ILLEGAL OPERATION | ILLEGAL OPERATION | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4174 | CM URL IS NOT FOUND | CM URL IS NOT FOUND | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E4649 | Ref Url is not valid or proper format. e.g. [http://www.yyy.zzz](http://www.yyy.zzz) | Ref Url is not valid or proper format. e.g. [http://www.yyy.zzz](http://www.yyy.zzz) | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | - | UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | 3DS_CHALLENGE_NEGATIVE | PG_FAILED \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | 3DS_METHOD_ERROR | 3DS_METHOD_ERROR | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | 3DS_METHOD_NEGATIVE | 56 \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | 3DS_METHOD_NEGATIVE | DAUTH \| Transaction Declined By Payment Gateway. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | 3DS_METHOD_NEGATIVE | 3DS206 \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | 3DS_METHOD_NEGATIVE | EMV3DSNS \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | 3DS_METHOD_NEGATIVE | 96 \| Issuer System Failure | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | 3DS_METHOD_NEGATIVE | 3DS222 \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | 3DS_METHOD_NEGATIVE | 3DS2ERR405 \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | 3DS_METHOD_NEGATIVE | VERCNTDTRAI01 \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | 3DS_METHOD_NEGATIVE | 3DS2001 \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | 3DS_VERIFICATION_NEGATIVE | UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | ACS_REDIRECT | Message Received Invalid | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | ACS_REDIRECT | Invalid Input Parameter For Guest Checkout Transaction \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | ACS_REDIRECT | ACS_REDIRECT | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | ACS_REDIRECT | UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | ALT_ID_PROV_ERROR | UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | 22 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | 87 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | ACS Technical failure | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | {"status":401,"message":"Authentication failed","error_type":"authentication_error","error_code":"GNAUE0003"} | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Message Received Invalid | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Transaction timed-out. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Cardholder Account Number is not in a range belonging to Issuer. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Transaction data not valid | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | 00 \| Authentication Request Successful | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | BIN Range inactive | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Transaction ID has already been received and processed. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Transaction ID is recognised as a duplicate. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Transaction Data Not Valid | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Retrieved transaction already used | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Transaction ID received is not valid for the receiving component. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Account number not validated | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Message Received Invalid. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Unkonwn Error. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | 82 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Merchant Category Code (MCC) not valid for Payment System | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | acctNumber | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Message not recognised | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | System Connection Failure | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Permanent system failure. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Cardholder Account Number is not in a range belonging to Issuer | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | ACS temporary unavailable | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Not a MasterCard supported card range. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Transaction data not valid. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Data element not in the required format | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Permanent System Failure | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Duplicate transaction | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Message received invalid | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Access denied, invalid endpoint | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | 02 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Transaction ID received is not valid for the receiving component | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | System connection failure. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Card range not found | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Call failed | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Card number is not in configured bin range. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | AUCNEGATIVE | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Bin range not configured | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | CAN is not in range | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | Internal error | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | If in response to an AReq message: Cardholder Account Number is not in a range belonging to Issuer. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUCNEGATIVE | invalid transaction data | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 3DS2008 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 5C \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 74 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | GW02016 \| !ERROR!-PAYMENT_ID_EXPIRED:GW02016-PaymentId Expired. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Guest Checkout Transaction \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 3DS2005 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 3DS2006 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | IPAY0200085 \| IPAY0200085-Checkbin Failure | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | K \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | NPCI452 \| NPCI452 - Exhausted OTP verification | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | NPCI412 \| NPCI412 - Issuer Authentication Server failure | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | NPCI56 \| NPCI56 - DECLINED (no card) | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | NPCI96 \| NPCI96 - SYSTEM ERROR | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | NPCI400 \| NPCI400 - GENERAL ERROR | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Token status is not active \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | T8 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 6P \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 9G \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | IPAY0100357 \| IPAY0100357-Transaction declined due to OTP Page refreshed. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | GW00555 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | NPCI413 \| NPCI413 - INVALID CVD2 | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | NPCI400 \| NPCI400 - General Error | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | H \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Q1 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | NPCI93 \| NPCI93 - Ecommerce Not Enabled | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | NPCI450 \| NPCI450 - INVALID OTP | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | D1 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 2032 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | CM90000 \| CM90000-Problem occured during transaction. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 72 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | VERIP03 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|1630\|M\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 3DS2004 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | C5 \| Retry Txn | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|6444\|V\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | T2 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|3505\|V\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|9820\|M\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|4751\|V\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | IRI \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | J \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | NPCI453 \| NPCI453 - Exhausted OTP resend count | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | DECAUTH \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | NPCI07 \| NPCI07 - Invalid Parameter Value - otp | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|8004\|V\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|0070\|V\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|5700\|M\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | IPAY0100348 \| IPAY0100348-Problem occured while doing Authentication | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 3DS214 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 9107 \| 9107 | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | NPCI07 \| NPCI07 - Invalid Parameter Value - card_cvd | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | CM90004 \| CM90004-Duplicate Record | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 407 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 9002 \| 9002 | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | ISSPMR \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | IPAY0200085 \| IPAY0200085-Rupay Initiate Failure | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | O6 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 9005 \| 9005 | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | F \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid UDF3 Original Amount. \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 410 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 3DS219 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | NPCI454 \| NPCI454 - Duplicate requestID | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | IPAY0200301 \| IPAY0200301-Invalid transaction details | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | IPAY0100049 \| IPAY0100049-Transaction Declined Due To Exceeding OTP Resend Attempts | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 9004 \| 9004 | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Tokenization failed \| Tokenization failed | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|6404\|V\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | NPCI408 \| NPCI408 - XML Data Error - Invalid Parameter Value - cvd2 | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|0963\|V\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|4864\|M\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|0305\|M\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|9617\|R\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | NPCI07 \| NPCI07 - Invalid Parameter Valuetoken_authenticationValue | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|1283\|V\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | NPCI451 \| NPCI451 - EXPIRED OTP | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Cryptogram Expired \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | 02 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Transaction not allowed with clear card number \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | D2 \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|6409\|V\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|7634\|V\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | AUTHNEGATIVE | Invalid Input Parameter For Tokenized Transaction:T\|\|1964\|M\|C\| \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | Bank failed to authenticate the customer | UNKNOWN_ERROR_PG | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | EVNEGATIVE | 400 \| General Error | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | EVNEGATIVE | 400 \| GENERAL ERROR | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | EVNEGATIVE | ERROR \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | EVNEGATIVE | 96 \| Issuer System Failure | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | EVNEGATIVE | REJECT \| UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | EVNEGATIVE | 56 \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | EVNEGATIVE | 413 \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | EVNEGATIVE | 410 \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | EVNEGATIVE | 93 \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | EVNEGATIVE | \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | EVNEGATIVE | 07 \| Pickup Card | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | EVNEGATIVE | 2032 \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E500 | REDIRECT | UNKNOWN | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E501 | 3DS_METHOD_ERROR | CURL_CALL_FAILURE | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E501 | 3DS_METHOD_NEGATIVE | CURL_CALL_FAILURE | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | - | - | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | 3DS_CHALLENGE_NEGATIVE | TRANSACTION_INVALID | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | ACS_REDIRECT | ACS_REDIRECT | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | ACS_REDIRECT | 000 \| Blc\|SUCCESS | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | ACS_REDIRECT | Invalid Otp | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | ACS_REDIRECT | 00 \| Authentication Request Successful | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | ACS_REDIRECT | \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | ACS_REDIRECT | 0 \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | AUCNEGATIVE | AUCNEGATIVE | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | AUCNEGATIVE | 0 \| OTP Generated Successfully | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | AUCNEGATIVE | 00 \| Authentication Request Successful | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | AUCNEGATIVE | Invalid Otp | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | AUCNEGATIVE | 0 \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | AUCNEGATIVE | UNKNOWN_ERROR | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | AUTHNEGATIVE | UNKNOWN_ERROR | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | AUTHNEGATIVE | Invalid credentials. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | REDIRECT | UNKNOWN_ERROR | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | REDIRECT | REDIRECT | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | REDIRECT | 0 \| OTP Generated Successfully | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | REDIRECT | 00 \| Authentication Request Successful | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | REDIRECT | 0 \| | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | REDIRECT | 000 \| Blc\|SUCCESS | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E502 | Transaction cancelled by customer | TRANSACTION_ABORTED | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E503 | ACS_REDIRECT | ACS_REDIRECT | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E503 | ACS_REDIRECT | Invalid Otp | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E503 | AUCNEGATIVE | AUCNEGATIVE | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E503 | AUCNEGATIVE | Invalid Otp | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E503 | REDIRECT | REDIRECT | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E504 | AUTHNEGATIVE | 94 \| Duplicate Transaction | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E504 | AUTHNEGATIVE | 1 \| AUTHORIZATION_FAILED_BY_BANK | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E504 | EVERROR | 15417 \| Duplicate requestID | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E504 | The transaction has been identified as duplicate transaction. | Duplicate Transaction | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E803 | 404 | FILTERED_DOMESTIC_PGS | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | E803 | 5006 | PG filtering based on AltId supported PGs | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | EX043 | Problem reading data from ? : ? | PROBLEM_READING_DATA_SENTROPI_URL | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | EX062 | Add Payment Call to payu_paisa_addpayment_url failed | PAYU_PAISA_ADDPAYMENT_URL_FAILED | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | EX148 | Invalid Request: ? Unable to parse URL. | INVALID_URL | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | EX200 | Something went wrong | V2_API_CURL_EXCEPTION | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | EX213 | Duplicate Callback. Please try after sometime | DUPLICATE_CALLBACK | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | EX215 | Invalid response from curl | INVALID_CURL_RESPONSE | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | EX306 | Invalid Webhook Url | INVALID_WEBHOOK_URL | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | EX401 | - | REDIS_DSN_ERROR | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | EX401 | - | REDIS_DSNKEY_NOT_CONFIGURED | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | EX403 | Invalid UDF Param | INVALID_UDF_PARAM | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | EX405 | Invalid More Info Param | INVALID_MORE_INFO_PARAM | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | TXNERROR | No or invalid bank callback | Indicates that either no callback was received from the bank or the response contained invalid or null values. This results in an uncertain transaction state requiring verification. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | TXNNEGATIVE | Failed bank callback | Occurs when the bank or wallet sends a failure callback indicating that the transaction was declined due to reasons like insufficient funds, incorrect details, or user cancellation. | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPI | E4010 | Transaction not allowed on/from the account | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPI | E4012 | MOBILE NUMBER REGISTERED WITH MULTIPLE CUSTOMER IDS | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPI | E4013 | Transaction failed due to beneficiary timeout | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPI | E4019 | DUPLICATE RRN FOUND IN THE TRANSACTION. (BENEFICIARY) | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPI | E4041 | Transaction failed due to internal exception at server/cbs end at customer's bank | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPI | E4150 | Transaction declined due to duplicate request | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPI | E4151 | Transaction failed due to amount limit on merchant exceeded | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPI | E4158 | Transaction failed due to timeout at acquirer's end | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPI | E500 | Transaction failed due to invalid params shared by the merchant | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPICC | E4010 | Transaction not allowed on/from the account | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPICC | E4013 | Transaction failed due to beneficiary timeout | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPICC | E4041 | Transaction failed due to internal exception at server/cbs end at customer's bank | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPICC | E4158 | Transaction failed due to timeout at acquirer's end | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPICC | E500 | Transaction failed due to invalid params shared by the merchant | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPIPPI | E4010 | Transaction not allowed on/from the account | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPIPPI | E4013 | Transaction failed due to beneficiary timeout | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPIPPI | E4158 | Transaction failed due to timeout at acquirer's end | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Collect Payment Error Codes | UPIPPI | E500 | Transaction failed due to invalid params shared by the merchant | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Issuer Decline Error Codes | E4158 / response 91 | Transaction failed due to timeout at acquirer's end | Issuer unavailable or switch inoperative | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Issuer Decline Error Codes | E504 / response 94 | The transaction has been identified as duplicate transaction. | Duplicate Transaction | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Partner Integration Errors | `401` | Unauthorized | Invalid or expired `resellerToken` | Invalid or expired `resellerToken` |
| Partner Integration Errors | `403` | Forbidden | No access to this merchant | No access to this merchant |
| Partner Integration Errors | `404` | Not found | Check `uuid`, `mid`, or `merchant_id` | Check `uuid`, `mid`, or `merchant_id` |
| Refund Initiation Error Codes | 500 | Some Exception Occurred. | 500 | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Refund Initiation Error Codes | 502 | Failed to update | 502 | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| Refund Status Error Codes | R500 | IN_PROGRESS | Refund status error | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| S2S Link and Pay Error Codes | E2401 | The customer is not eligible for this transaction | - | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |
| S2S Link and Pay Error Codes | E2415 | The customer’s account is blocked by the lender. | - | Fix endpoint URL, method, authentication, content type, firewall/WAF, or handler errors; return 2xx only after durable receipt. |

<!-- PAYU_REPO_ERRORS_WEBHOOK_FAILURES_END -->
