---
title: APIs used in Refunds integration
deprecated: false
hidden: false
icon: fab fa-cash-app
metadata:
  title: APIs used in Refunds integration
  robots: index
---
| API                                                                                    | Purpose                                                                                             |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [Refund Transaction API](ref:refund_transaction_api)                                   | Initiate a full or partial refund (`cancel_refund_transaction` command) for a captured transaction. |
| [Check Refund Status API with PayU ID](ref:check_action_status_api_with_payu_id)       | Poll refund status using the PayU transaction ID (`check_action_status_txn_id`).                    |
| [Check Refund Status API with Request ID](ref:check_action_status_api_with_request_id) | Poll refund status using the merchant request ID.                                                   |
| [Get All Refunds from Transaction IDs](ref:get_all_refunds_from_transaction_ids_api)   | Retrieve all refund requests associated with one or more transaction IDs.                           |
| [Refund Status API for Split Payments](ref:refund-status-api-for-split-payments)       | Check refund status for split-payment child transactions.                                           |

<br />
