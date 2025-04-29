---
title: Create the Split
excerpt: >-
  Before diving into the specifics of using the Marketplace solution, you need
  to understand a few terms used throughout this document and in the API.  1.
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Creating a split involves the following:

- The marketplace owners are referred to as the “aggregator merchant”
- The individual providers or sub-sellers of that marketplace are referred to as “child merchants”
- The fee that the parent Merchant can optionally apply per Sub Merchant transaction is called the “aggregatorCharges”.
- The amount that will be settled to given child merchants is referred to as the “amountToBeSettled”.

## Procedure to create a split

To perform a basic API setup for adding a payment, adding splits (sub-payment) for payment, and releasing a sub-payment:

1. Implement any of the following split APIs to split at your end using the transaction id generated:
   - [Split After Transaction API](https://docs.payu.in/v1/reference/split_after_transaction_api) under API Reference
   - [Split During Transaction using \_payment](ref:v2-split-during-transaction-using-_payment) under API Reference

> **Note**: You can implement the convenience fee for any of the above Split APIs. For more information on convenience fee, refer to [Convenience Fee Handling](https://docs.payu.in/v1/docs/convenience-fee-handling).

2. [Get Aggregator/Parent Transaction Info](https://docs.payu.in/v1/reference/get_aggregator_parent_transaction_info_api)  Get the split information of the parent transaction in the Aggregator flow.
3. [Release Settlement API](https://docs.payu.in/v1/reference/release_settlement_api): Implement the release payment API.