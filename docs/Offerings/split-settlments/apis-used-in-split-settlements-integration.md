---
title: APIs used in Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in Split Settlements integration
  robots: index
---
Use these APIs to onboard child merchants, create and inspect payment splits, release settlements, and manage split refunds.

### Onboard child merchants

| Use case → Reference                                       | `command` / primary value                                     | Description                                                                                                                                                                                                                          |
| ---------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Get Client Token API](ref:get-client-token-api)           | OAuth scopes: `refer_child_merchant`, `fetch_child_merchants` | Generate a Hub OAuth token for child-merchant onboarding or listing.                                                                                                                                                                 |
| [Create Child Merchant API](ref:create-child-merchant-api) | `refer_child_merchant` scope                                  | Onboard child merchants (sub-accounts) and update their bank details.                                                                                                                                                                |
| [Sub Account Listing API](ref:sub-account-listing-api)     | `fetch_child_merchants` scope                                 | Fetch child merchant details linked to a parent merchant. **Used in:** [Fetch Child Merchants Details](doc:fetch-child-merchants-details-1) and [Integration APIs for Split Settlements](doc:api-integration-for-split-settlements). |

### Split payments

| Use case → Reference                                                                 | `command` / primary value | Description                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------ | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Absolute Split During Transaction](ref:absolute-split-during-transaction)           | `_payment`                | Split a payment by fixed amount among child merchants at transaction time. **Used in:** [Absolute Split During Transaction Integration](doc:absolute-split-during-transaction-integration) and [Create the Split](doc:create-the-split).         |
| [Split by Percentage During Transaction](ref:split-by-percentage-during-transaction) | `_payment`                | Split a payment by percentage among child merchants at transaction time. **Used in:** [Split by Percentage During Transaction Integration](doc:split-by-percentage-during-transaction-integration) and [Create the Split](doc:create-the-split). |
| [Absolute Split After Transaction](ref:absolute-split-after-transaction)             | `payment_split`           | Split a completed transaction by fixed amount.                                                                                                                                                                                                   |
| [Split by Percentage after Transaction](ref:split-by-percentage-after-transaction)   | `payment_split`           | Split a completed transaction by percentage.                                                                                                                                                                                                     |

### Release and reconcile settlements

| Use case → Reference                                           | `command` / primary value | Description                                                                             |
| -------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------- |
| [Release Settlement API](ref:release_settlement_api)           | `release_settlement`      | Release blocked settlement amounts for child merchants in the aggregator workflow.      |
| [Settlement Detail Range API](ref:settlement-detail-range-api) | `GET /settlement/range`   | Retrieve paginated transaction-level settlement details for a given date or date range. |

### Retrieve transaction information

| Use case → Reference                                                                            | `command` / primary value     | Description                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Get Aggregator/Parent Transaction Info API](ref:get_aggregator_parent_transaction_info_api)    | `get_aggregator_transactions` | Retrieve split allocation details for a parent transaction.                                                                                                                               |
| [Get Child/Parent Split Transaction Info API](ref:get_child_parent_split_transactions_info_api) | `get_split_transactions`      | Retrieve split transaction details for child or parent merchants.                                                                                                                         |
| [Get Split Info API](ref:get_split_info_api)                                                    | `get_split_info`              | Fetch split information for a transaction. **Used in:** [Integration APIs for Split Settlements](doc:api-integration-for-split-settlements) and [Create the Split](doc:create-the-split). |

### Manage refunds

| Use case → Reference                                                                 | `command` / primary value              | Description                                                           |
| ------------------------------------------------------------------------------------ | -------------------------------------- | --------------------------------------------------------------------- |
| [Refund Transaction API](ref:refund_transaction_api)                                 | `cancel_refund_transaction`            | Process refunds with `var8` JSON specifying per-child refund amounts. |
| [Refund Status API for Split Payments](ref:refund-status-api-for-split-payments)     | `aggregator_check_action_status_txnid` | Check refund status for split-payment transactions.                   |
| [Get All Refunds from Transaction IDs](ref:get_all_refunds_from_transaction_ids_api) | `getAllRefundsFromTxnIds`              | Retrieve all refunds associated with the supplied transaction IDs.    |

<br />
