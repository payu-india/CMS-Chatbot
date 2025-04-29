---
title: Introduction
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Split Settlements Introduction
  description: >-
    PayU Split Settlements APIs enable businesses to make, collect, and receive
    payments using bank accounts. The Split Settlements API allows customers to
    split a transaction based on the number of sellers involved in the
    particular transaction. This page from the PayU Developer Documentation
    Portal provides information on how to use the Split Settlements API,
    including authentication requirements and use cases such as taxi aggregators
    and eCommerce platforms.
  keywords:
    - PayU Split Settlements
    - ' payment distribution platform'
    - ' multi-vendor payment processing'
    - ' marketplace payment solutions'
    - ' automated payment splitting'
    - ' automated payment distribution system'
    - ' custom payment allocation rules'
    - ' vendor payment management'
    - ' payment reconciliation for marketplaces'
    - ' multi-party transaction processing'
    - ' e-commerce marketplace payment solutions'
    - ' service aggregator payment distribution'
    - ' subscription revenue splitting'
    - ' franchise payment management'
    - ' event platform payment distribution'
    - ' payment split API integration'
    - ' sub-merchant settlement system'
    - ' merchant payout automation'
    - ' payment distribution workflow'
    - ' settlement cycle configuration'
    - ' simplified payment reconciliation system'
    - ' reduce payment operations overhead'
    - ' compliant payment distribution'
    - ' streamlined vendor payments'
    - ' automated commission settlement'
  robots: index
next:
  description: ''
---
Split Settlements APIs enable your business to make, collect and receive payments using bank accounts. PayU overlaid a simple REST API, enabling all your online accounts with other account payment flows through an easy integration process.

Using Split Settlements API, PayU helps merchants split a transaction based on the number of sellers involved in the particular transaction.

You can split payments using any of the following:

- **Dashboard**: PayU offers the following features with Dashboard:
  - [Activate Split Settlements](doc:activate-split-settlements)
  - [Adding Sub-Accounts](doc:adding-sub-accounts)
  - [Manage Sub-Accounts](doc:manage-sub-accounts)
  - [Split a Transaction on Dashboard](doc:split-a-transaction-on-dashboard)
  - [View Split Transaction Details](doc:view-split-transaction-details)
  - [Initiate a Settlement for Sub-Account](doc:initiate-a-settlement-for-sub-account)
- **APIs**: PayU overlaid a simple REST API, enabling all your online accounts with other account payment flows through an easy integration process. Using Split Settlements API, PayU helps your customers split a transaction based on the number of sellers involved in the particular transaction. PayU offers Split Settlements APIs secured by an authentication mechanism. To make a call to an API, you first need to authenticate to the API by providing your API key in the request header. It’s a unique key for every marketplace account and will be generated on demand when your test account is created. All API requests must be made over HTTPS. Calls made over plain HTTP will fail. You must authenticate for all requests. For more information, refer to [Integration APIs for Split Settlements](doc:api-integration-for-split-settlements).

## Use cases

- **Taxi Aggregators**: The Aggregator app collects digital payments from the passenger and splits the payment and settles the major part to the driver to themselves based on the vehicle ownership. Also, the taxes are allocated in a separate bucket.
- **eCommerce Platforms**: After the customer makes a purchase, the platform owners automatically split the payments received from the customer to pay the seller and commission (absolute amount). The amount to be split is done after applying the offers or discounts applied by the customer. For example, Policybazaar.com. In this example, the insurance companies may further split payments to pay the insurance advisor or financial institutions that successfully enrolled the customers.