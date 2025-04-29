---
title: Integration APIs
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The recommended workflow for using Split Settlements using API Integration:

<V2BeforeYouBegin />

<br />

1. Register as a merchant with PayU.
2. Onboard child merchants with the following steps:
   1. [Get Client Token API](https://docs.payu.in/v1/reference/get-client-token-api)
   2. [Create Child Merchant API](https://docs.payu.in/v1/reference/create-child-merchant-api)
3. Create the split using any of the following methods:

- Split During Transaction
  - [Absolute Split During Transaction](https://docs.payu.in/v2/reference/absolute-split-during-transaction-v2_payment) using \/v2/payments API
  - [Split by Percentage During Transaction](https://docs.payu.in/v2/reference/split-by-percentage-during-transaction-v2_payment)using \/v2/payments API
- Split After Transaction
  - [Absolute Split After Transaction using **payment_split** API](https://docs.payu.in/v1/reference/absolute-split-after-transaction)
  - [Split by Percentage after Transaction using **payment_split** API](https://docs.payu.in/v1/reference/split-by-percentage-after-transaction)
- Release the settlement amount using the following APIs
  - [Release Settlement API](https://docs.payu.in/v1/reference/release_settlement_api)
  - [Settlement Reconciliation API](https://docs.payu.in/v1/reference/settlement-reconciliation-api)

4. Get the transaction information such as amount split for a given parent merchant:
   - [Get Aggregator/Parent Transaction Info API](https://docs.payu.in/v1/reference/get_aggregator_parent_transaction_info_api)
   - [Get Child/Parent Split Transaction Info API](https://docs.payu.in/v1/reference/get_child_parent_split_transactions_info_api)
   - [Get Split Info API](https://docs.payu.in/v1/reference/get_split_info_api)

Use the following APIs for refunds or other purposes:

- [Fetch Child Merchants Details](https://docs.payu.in/v1/docs/fetch-child-merchants-details-1)
  - [Sub Account Listing API](https://docs.payu.in/v1/reference/sub-account-listing-api)
- Refund API

  - [Refund Transaction API](https://docs.payu.in/v1/reference/refund_transaction_api)
    > 📘 Include var8 in Refund Transaction API:
    > 
    > You must include the var8 parameter similar to the following JSON array format with the refund details of split where **child_merchant_key_x** must be substituted with the child merchant key. For more information, refer to **Refund Transaction API** > [Other request parameters](https://docs.payu.in/v1/reference/refund_transaction_api#other-request-parameters)
    > 
    > ```
    > {
    >    "child_merchant_key_1":{
    >       "amount":100,
    >       "aggregatorRefundAmount":40
    >    },
    >    "child_merchant_key_2":{
    >       "amount":20,
    >       "aggregatorRefundAmount":0
    >    }
    > }
    > ```

  - [Refund Status API for Split Payments](https://docs.payu.in/v1/reference/refund-status-api-for-split-payments)

  - [Get All Refunds from Transaction IDs](https://docs.payu.in/v1/reference/get_all_refunds_from_transaction_ids_api) (same API used in general and split settlements)