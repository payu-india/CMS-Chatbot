---
title: Split During Transaction using v2 _payment
excerpt: 'API command: **_payment**'
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This section describes the **\_payment** API contract for getting split info of the parent transaction in the Aggregator flow.

* [Absolute Split During Transaction](https://docs.payu.in/v2/reference/absolute-split-during-transaction-v2_payment)
* [Split by Percentage During Transaction](https://docs.payu.in/v2/reference/split-by-percentage-during-transaction-v2_payment)

## Scenarios

If a Parent Merchant has two child merchants: Merchant A (Key: `P****Y`) and Merchant B (Key: `P***K`). If a customer buys two products from each of the merchants and involves the following:

* Merchant **A** (Product Cost: 60)
* Merchant **B** (Product Cost: 40)
* Customer paid **Cost: 100** on PayU Gateway.

The following cases can occur:

* **Case 1:**&#x4D;erchant wants the commission amount from Merchant A (Commission amount: 15) and B (Commission Amount: 10).

So In the final, Merchant wants to settle Amount: 45 to Merchant A and Amount: 30 to Merchant B and Amount: 25 to self account (parent part).

The split JSON Structure for the above scenarios is similar to the following:

```plaintext
{
   "type":"absolute",
   "splitInfo":{
      "P****Y":{
         "aggregatorSubTxnId":"9a70ea0155268101001ba",
         "aggregatorSubAmt":"45",
         "aggregatorCharges":"15"
      },
      "P***K":{
         "aggregatorSubTxnId":"9a70ea0155268101001bb",
         "aggregatorSubAmt":"30",
         "aggregatorCharges":"10"
      }
   }
}
```

* **Case 2:** Merchant wants the commission amount from Merchant A (Commission amount: 15) and Nothing from Merchant B (Commission Amount: 0).

So, the merchant wants to settle an amount: 45 to Merchant A and amount: 40 to Merchant B and an amount: 15 to self account (parent part).

The split JSON Structure for the above scenario is similar to the following:

```plaintext
{
   "type":"absolute",
   "splitInfo":{
      "P****Y":{
         "aggregatorSubTxnId":"9a70ea0155268101001ba",
         "aggregatorSubAmt":"45",
         "aggregatorCharges":"15"
      },
      "P***K":{
         "aggregatorSubTxnId":"9a70ea0155268101001bb",
         "aggregatorSubAmt":"40"
      }
   }
}
```

* **Case 3:** Merchant does not want any commission amount from Child Merchant A (Commission amount: 0) and B (Commission Amount: 0).

So In the final, Merchant wants to settle Amount: 60 to child merchant **A** and Amount: 40 to Child Merchant **B** and Amount: 0 to Self account (Parent Part).

The split JSON Structure for the above scenario is similar to the following:

```plaintext
{
   "type":"absolute",
   "splitInfo":{
      "P****Y":{
         "aggregatorSubTxnId":"9a70ea0155268101001ba",
         "aggregatorSubAmt":"60"
      },
      "P***K":{
         "aggregatorSubTxnId":"9a70ea0155268101001bb",
         "aggregatorSubAmt":"40"
      }
   }
}
```

## Split Transaction with Only Single Child

You may choose to settle 100% for a single child. In such cases, you can pass zero (0) in the child’s key and 100% amount for others. For example, in the following JSON structure:

* The amount is Rs.10 for **aggregatorSubAmt**.
* The amount of Rs.0 (or no amount settlement) for **aggregatorCharges**

```plaintext
{
"childKey1":{
    "aggregatorSubTxnId":"txnIdForChild",
    "aggregatorSubAmt":"10",
    "aggregatorCharges":"0"
  }
}
```

## Passing parent merchant key in the splitInfo parameter

You can pass the parent merchant key along and the child merchant key with the corresponding **aggregatorSubTxnId**, **aggregatorSubAmt**, and **aggregatorCharges** (can be used by only for parent merchants to collect charges) parameters in a JSON format.

### Sample Request

A sample value in JSON format for the **splitInfo** parameter:

```plaintext
{
   "P41sCY":{
      "aggregatorSubTxnId":"0e7411799c9f0e96620c1",
      "aggregatorSubAmt":"3",
      "aggregatorCharges":"2"
   },
   "P41sCK":{
      "aggregatorSubTxnId":"0e7411799c9f0e96620c2",
      "aggregatorSubAmt":"5"
   }
}
```

> 📘 Refunds for Split Transactions:
>
> You must include the var8 parameter similar to the following JSON array format with the refund details of split where **child\_merchant\_key\_x** must be substituted with the child merchant key. For more information, refer to  [Refund Transaction API > Other request parameters](ref:refund_transaction_api#other-request-parameters)
>
> ```plaintext
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
