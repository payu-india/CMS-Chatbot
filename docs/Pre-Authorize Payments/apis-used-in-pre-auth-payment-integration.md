---
title: APIs used in Pre-Auth Payment Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: APIs Used in Auth and Capture Integration
excerpt: API quick reference for pre-authorization, capture, cancellation, and transaction verification, with complete test and production endpoint URLs.
deprecated: false
hidden: false
metadata:
  title: Auth and Capture API Reference - PayU
  description: Merchant-facing API reference for Auth and Capture, UPI one-time mandates, and UPI Reserve Pay.
  robots: index
---

# APIs Used in Auth and Capture Integration

Use this reference to identify the API for each step of your Auth and Capture integration. Each Endpoint column contains the complete URL as literal text, including the path and query string.

## 1. Authorize, Capture, or Cancel a Payment

| Operation | HTTP method | Test Endpoint | Production Endpoint | Command / primary value | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Pre-Authorize Payment — PayU Hosted | POST | `https://test.payu.in/_payment` | `https://secure.payu.in/_payment` | `_payment` with `pre_authorize=1` | Initiate a card authorization through PayU Hosted Checkout. |
| Pre-Authorize Payment — Merchant Hosted Cards | POST | `https://test.payu.in/_payment` | `https://secure.payu.in/_payment` | `_payment` with `pre_authorize=1` | Initiate a card authorization through your merchant-hosted checkout. |
| Pre-Authorize Payment — S2S | POST | `https://test.payu.in/_payment` | `https://secure.payu.in/_payment` | `_payment` with `pre_authorize=1` | Initiate pre-authorization using the S2S integration guide. |
| Capture a Pre-Authorized Payment | POST | `https://test.payu.in/merchant/postservice.php?form=2` | `https://info.payu.in/merchant/postservice.php?form=2` | `capture_transaction` | Request capture of all or part of the authorized amount. |
| Cancel a Pre-Authorized Payment | POST | `https://test.payu.in/merchant/postservice.php?form=2` | `https://info.payu.in/merchant/postservice.php?form=2` | `cancel_transaction` | Request cancellation of an authorization and release of held funds. |

### Related API References

- [Pre-Authorize Payment API — PayU Hosted](ref:pre_authorize_payment)
- [Pre-Authorize Payment API — Merchant Hosted](ref:pre_authorize_payment_merchant_hosted)
- [Capture a Pre-Authorized Payment API](ref:capture_a_payment)
- [Cancel a Pre-Authorized Transaction API](ref:cancel-a-pre-authorized-transaction)

## 2. Verify Payment and Track Action Status

| Operation | HTTP method | Test Endpoint | Production Endpoint | Command | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Verify Payment Status | POST | `https://test.payu.in/merchant/postservice.php?form=2` | `https://info.payu.in/merchant/postservice.php?form=2` | `verify_payment` | Check the transaction status. An `unmappedstatus` value of `auth` indicates successful authorization. |
| Check Action Status | POST | `https://test.payu.in/merchant/postservice.php?form=2` | `https://info.payu.in/merchant/postservice.php?form=2` | `check_action_status` | Track a queued action using the request ID returned for that action. |

### Related API References

- [Verify Payment API](ref:verify_payment_api)
- [Check Action Status API with Request ID](ref:check_action_status_api_with_request_id)

## 3. UPI One-Time Mandates and Reserve Pay

| Operation | HTTP method | Test Endpoint | Production Endpoint | Command / primary value | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| UPI Intent One-Time Mandate — PayU Hosted | POST | `https://test.payu.in/_payment` | `https://secure.payu.in/_payment` | `_payment` with `pre_authorize=1` | Initiate a UPI Intent authorization through PayU Hosted Checkout. |
| UPI Intent One-Time Mandate — Merchant Hosted | POST | `https://test.payu.in/_payment` | `https://secure.payu.in/_payment` | `_payment` with `pre_authorize=1` | Initiate a UPI Intent authorization from your merchant-hosted integration. |
| UPI Collect One-Time Mandate — PayU Hosted | POST | `https://test.payu.in/_payment` | `https://secure.payu.in/_payment` | `_payment` with `pre_authorize=1` | Initiate a UPI Collect authorization through PayU Hosted Checkout. |
| UPI Collect One-Time Mandate — Merchant Hosted | POST | `https://test.payu.in/_payment` | `https://secure.payu.in/_payment` | `_payment` with `pre_authorize=1` | Initiate a UPI Collect authorization using the customer's VPA. |
| Validate VPA | POST | `https://test.payu.in/merchant/postservice.php?form=2` | `https://info.payu.in/merchant/postservice.php?form=2` | `validateVpa` | Validate a customer's UPI VPA before initiating a UPI Collect mandate. |
| UPI Reserve Pay — PayU Hosted | POST | `https://test.payu.in/_payment` | `https://secure.payu.in/_payment` | `_payment` | Initiate a Reserve Pay authorization through PayU Hosted Checkout. |
| UPI Reserve Pay — Merchant Hosted | POST | `https://test.payu.in/_payment` | `https://secure.payu.in/_payment` | `_payment` | Initiate a Reserve Pay authorization through your merchant-hosted checkout. |

### Related API References

- [UPI One-Time Mandate API — PayU Hosted](ref:upi-one-time-mandate-transaction-api-payu-hosted)
- [UPI One-Time Mandate API — Merchant Hosted](ref:_payment-upi-one-time-mandate-transaction-api)
- [UPI OTM Status Check API](ref:upi-otm-status-check-api)
- [Validate VPA API](ref:validate_vpa_api)
- [UPI Reserve Pay One-Time Mandate — PayU Hosted](ref:upi-reserve-pay-one-time-mandate-payu-hosted)
- [UPI Reserve Pay One-Time Mandate — Merchant Hosted](ref:upi-reserve-pay-one-time-mandate-merchant-hosted)

## Integration Notes

- Use the test endpoints for sandbox requests and the production endpoints for live requests. Use credentials for the matching environment.
- An authorization is not a completed capture. Confirm the transaction state before updating your order's payment status.
- A queued action response is not confirmation that the requested operation has completed. Check its subsequent status.
- This page is an endpoint directory, not a complete request schema. Follow the relevant integration guide and API reference for mandatory, optional, and flow-specific parameters, request signing, and response handling.
- The `ref:` links are documentation-platform references retained from the source documentation. The endpoint URLs in the tables are complete and do not depend on resolving those links.
