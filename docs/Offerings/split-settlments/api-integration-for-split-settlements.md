---
title: Integration APIs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The recommended workflow for using Split Settlements using API Integration:

> 👍
>
> Experience the end-to-end **PayU Hosted > Split Settlements** flow and instantly generate the complete code for seamless, zero-coding integration into your website.
>
> <HTMLBlock>{`
>                           <style>
>                           .tooltip-btn {
>                               position: relative;
>                               background-color: #4CAF50;
>                               color: white;
>                               padding: 10px 20px;
>                               border: none;
>                               border-radius: 5px;
>                               cursor: pointer;
>                               font-weight: bold; /* Added this line */
>                           }
>                           .tooltip-btn:hover::after {
>                               content: attr(data-tooltip);
>                               position: absolute;
>                               bottom: 125%;
>                               left: 50%;
>                               transform: translateX(-50%);
>                               background-color: #333;
>                               color: white;
>                               padding: 5px 10px;
>                               border-radius: 4px;
>                               white-space: nowrap;
>                               font-size: 12px;
>                               z-index: 1;
>                           }
>                           </style>
>
>                           <button onclick="window.open('https://payu.in/integrationlab/split', '_blank')" 
>                                   class="tooltip-btn" 
>                                   data-tooltip="Automatically generate code including hashing for your eCommerce website to integrate Offers - PayU Hosted Checkout with zero coding knowledge.">
>                                Experience the flow and get the code
>                           </button>
> `}</HTMLBlock>

> 👍
>
> **Before you begin**: Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

1. Register as a merchant with PayU.
2. Onboard child merchants with the following steps:
   1. [Get Client Token API](ref:get-client-token-api)
   2. [Create Child Merchant API](ref:create-child-merchant-api)
3. Create the split using any of the following methods:

- Split During Transaction
  - [Absolute Split During Transaction using **\_payment** API](/reference/absolute-split-during-transaction)
  - [Split by Percentage During Transaction using **\_payment** API](/reference/split-by-percentage-during-transaction)
- Split After Transaction
  - [Absolute Split After Transaction using **payment\_split** API](/reference/absolute-split-after-transaction)
  - [Split by Percentage after Transaction using **payment\_split** API](/reference/split-by-percentage-after-transaction)
- Release the settlement amount using the following APIs
  - [Release Settlement API](ref:release_settlement_api)

4. Get the transaction information such as amount split for a given parent merchant:
   - [Get Aggregator/Parent Transaction Info API](https://docs.payu.in/reference/get_aggregator_parent_transaction_info_api)
   - [Get Child/Parent Split Transaction Info API](https://docs.payu.in/reference/get_child_parent_split_transactions_info_api)
   - [Get Split Info API](https://docs.payu.in/reference/get_split_info_api)

Use the following APIs for refunds or other purposes:

- [Fetch Child Merchants Details](doc:fetch-child-merchants-details-1)
  - [Sub Account Listing API](ref:sub-account-listing-api)
- Refund API

  - [Refund Transaction API](ref:refund_transaction_api)
    > 📘 Include var8 in Refund Transaction API:
    >
    > You must include the var8 parameter similar to the following JSON array format with the refund details of split where **child\_merchant\_key\_x** must be substituted with the child merchant key. For more information, refer to **Refund Transaction API** > [Other request parameters](ref:refund_transaction_api#other-request-parameters)
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

  - [Refund Status API for Split Payments](ref:refund-status-api-for-split-payments)

  - [Get All Refunds from Transaction IDs](ref:get_all_refunds_from_transaction_ids_api) (same API used in general and split settlements)

> 📮
>
> **Postman Collection**: Download the **Split Settlements Postman Collection** from the following location:
>
> [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/collection/phkf7uf/split-settlments](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/collection/phkf7uf/split-settlments)

<br />
