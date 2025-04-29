---
title: Other Related APIs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Other Related APIs for Split Settlements
  description: ''
  keywords:
    - Other Related APIs for Split Settlements
  robots: index
next:
  description: ''
---
The following general APIs can be used while Split Settlements integration:

- [Refund Transaction API](ref:refund_transaction_api)

> 📘 Include var8 in Refund Transaction API:
> 
> You must include the var8 parameter similar to the following JSON array format with the refund details of split where **child_merchant_key_x** must be substituted with the child merchant key. For more information, refer to **Refund Transaction API** > [Other request parameters](ref:refund_transaction_api#other-request-parameters)
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

<br />

- [Get All Refunds from Transaction IDs](ref:get_all_refunds_from_transaction_ids_api)