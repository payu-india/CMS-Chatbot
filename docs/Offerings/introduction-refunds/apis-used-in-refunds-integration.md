---
title: APIs used in Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in Refunds integration
  robots: index
---
The following APIs initiate refunds and retrieve their status for standard and split-payment transactions.

## Refund Transaction

| Use case → Reference                                 | `command` / primary value   | Description                                                                                       |
| ---------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------- |
| [Refund Transaction API](ref:refund_transaction_api) | `cancel_refund_transaction` | Cancel an authorised transaction or initiate a full or partial refund for a captured transaction. |

## Check Refund&#x20;

| Use case → Reference                                                                   | `command` / primary value   | Description                                                                            |
| -------------------------------------------------------------------------------------- | --------------------------- | -------------------------------------------------------------------------------------- |
| [Check Refund Status API with PayU ID](ref:check_action_status_api_with_payu_id)       | `check_action_status`       | Retrieve capture, refund, and cancellation request statuses for a PayU transaction ID. |
| [Check Refund Status API with Request ID](ref:check_action_status_api_with_request_id) | `check_action_status_txnid` | Retrieve the processing status and details of a specific refund using its request ID.  |
| [Get All Refunds from Transaction IDs](ref:get_all_refunds_from_transaction_ids_api)   | `getAllRefundsFromTxnIds`   | Retrieve the status and details of all refund requests for a transaction ID.           |

## Refund Status

| Use case → Reference                                                             | `command` / primary value              | Description                                               |
| -------------------------------------------------------------------------------- | -------------------------------------- | --------------------------------------------------------- |
| [Refund Status API for Split Payments](ref:refund-status-api-for-split-payments) | `aggregator_check_action_status_txnid` | Retrieve the refund status of split-payment transactions. |

<br />
