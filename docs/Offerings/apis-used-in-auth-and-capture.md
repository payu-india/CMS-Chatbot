---
title: APIs used in Integration
excerpt: ''
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in Auth and Capture Integration
  description: ''
  robots: index
next:
  description: ''
---
Use these APIs to authorize, capture, cancel, and track card or UPI pre-authorized payments.

### Authorize, capture, or cancel payment

| Use case → Reference                                                                     | `command` / primary value         | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Pre-Authorize Payment API – PayU Hosted](ref:pre_authorize_payment)                     | `_payment` with `pre_authorize=1` | Hold card funds without capturing them on PayU Hosted Checkout.                                                                                                                    |
| [Pre-Authorize Payment API – Merchant Hosted](ref:pre_authorize_payment_merchant_hosted) | `_payment` with `pre_authorize=1` | Hold card funds without capturing them on merchant-hosted checkout.                                                                                                                |
| [Capture a Pre-Authorized Payment API](ref:capture_a_payment)                            | `capture_transaction`             | Capture all or part of the held funds after authorization.                                                                                                                         |
| [Cancel a Pre-Authorized Transaction API](ref:cancel-a-pre-authorized-transaction)       | `cancel_transaction`              | Cancel an authorization and release held funds. **Used in:** [Cancel a Pre-Authorized Payment](doc:cancel-a-pre-authorized-payment) and the card and UPI pre-authorization guides. |

### Verify the payment

| Use case → Reference                         | `command` / primary value | Description                                                                                       |
| -------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------- |
| [Verify Payment API](ref:verify_payment_api) | `verify_payment`          | Check transaction status; an `unmappedstatus` value of `auth` indicates successful authorization. |

### Check action status

| Use case → Reference                                                                   | `command` / primary value | Description                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------ |
| [Check Action Status API with Request ID](ref:check_action_status_api_with_request_id) | `check_action_status`     | Check the status of authorization, capture, or refund requests queued at PayU. |

### UPI one-time mandates

| Use case → Reference                                                                                       | `command` / primary value | Description                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------ |
| [UPI One-Time Mandate API – PayU Hosted](ref:upi-one-time-mandate-transaction-api-payu-hosted)             | `_payment`                | Initiate a UPI one-time mandate pre-authorization on PayU Hosted Checkout.     |
| [UPI One-Time Mandate API – Merchant Hosted](ref:_payment-upi-one-time-mandate-transaction-api)            | `_payment`                | Initiate a UPI one-time mandate pre-authorization on merchant-hosted checkout. |
| [UPI OTM Status Check API](ref:upi-otm-status-check-api)                                                   | OTM status endpoint       | Check the status of a UPI one-time mandate transaction.                        |
| [Validate VPA API](ref:validate_vpa_api)                                                                   | `validateVpa`             | Validate the customer's UPI VPA before initiating a UPI Collect mandate.       |
| [UPI Reserve Pay One-Time Mandate – PayU Hosted](ref:upi-reserve-pay-one-time-mandate-payu-hosted)         | `_payment`                | Pre-authorize a UPI Reserve Pay transaction on PayU Hosted Checkout.           |
| [UPI Reserve Pay One-Time Mandate – Merchant Hosted](ref:upi-reserve-pay-one-time-mandate-merchant-hosted) | `_payment`                | Pre-authorize a UPI Reserve Pay transaction on merchant-hosted checkout.       |

<br />
