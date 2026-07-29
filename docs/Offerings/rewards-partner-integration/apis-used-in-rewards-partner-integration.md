---
title: APIs used in Rewards Partner Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  robots: index
---
The following APIs are used for Rewards Partner integration:

### Balance and Payment

| Use case → Reference                                                                                    | `command` / primary value                     | Description                                                                       |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------- |
| Fetch reward balances — [Fetch Balance All API](ref:rewards-fetch-balance-all-api)                      | `POST /loyalty-points/v1/balance/all`         | Retrieves usable TWID and Zillion reward balances for a customer before checkout. |
| Collect payment with rewards — [Collect Payment with Rewards API](ref:_payment-merchant-hosted-rewards) | `_payment` with `pg=SPLITPAY` and `splitInfo` | Initiates a split payment to burn or earn reward points along with Card or UPI.   |

### Verify Payment

| Use case → Reference                                            | `command` / primary value | Description                                                |
| --------------------------------------------------------------- | ------------------------- | ---------------------------------------------------------- |
| Verify a payment — [Verify Payment API](ref:verify_payment_api) | `verify_payment`          | Reconciles the transaction status with PayU after payment. |

### Decoupled Card Flow

| Use case → Reference                                                                          | `command` / primary value             | Description                                                                   |
| --------------------------------------------------------------------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------- |
| Initiate decoupled card payment — [Cards Decoupled Flow API](ref:_payment_s2s_decoupled_flow) | `POST _payment` (S2S decoupled)       | Initiates a server-to-server decoupled card payment for RewardX transactions. |
| Submit the OTP — [Submit OTP API](ref:submit-otp-to-payu)                                     | `POST ResponseHandler.php` with `otp` | Submits the OTP entered by the customer during decoupled card authentication. |

### Refunds

| Use case → Reference                                                                                                 | `command` / primary value              | Description                                                                       |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | --------------------------------------------------------------------------------- |
| Refund a split-payment transaction — [Refund Transaction API](ref:refund_transaction_api)                            | `cancel_refund_transaction`            | Initiates refunds for split-payment transactions across Card/UPI and reward legs. |
| Check split-payment refund status — [Refund Status API for Split Payments](ref:refund-status-api-for-split-payments) | `aggregator_check_action_status_txnid` | Retrieves the refund status of split-payment child transactions.                  |

<br />
