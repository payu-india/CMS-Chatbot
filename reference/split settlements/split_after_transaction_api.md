---
title: Split After Transaction API
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
You must specify two decimal places for each split, but ensure the sum split amounts are equal to the transaction amount.

> 📘 Note:
> 
> You must specify two decimal places for each split, but ensure the sum of the percentage of all splits is equal to 100.

HTTP Method: **POST**

**Environment**

|                            |                                                        |
| :------------------------- | :----------------------------------------------------- |
| **Test Environment**       | <https://test.payu.in/merchant/postservice.php?form=2> |
| **Production Environment** | <https://info.payu.in/merchant/postservice.php?form=2> |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Sample Value**",
    "0-0": "key",
    "0-1": "`string` This parameter must include the Merchant key that was provided by PayU.",
    "0-2": "vDy3i7",
    "1-0": "command",
    "1-1": "`string` The parameter must contain the name of the web service.",
    "1-2": "payment\\_split",
    "2-0": "hash",
    "2-1": "`String` The hash string encryption is specified in this parameter. The format of the hash is:  \n|sha512(key|command|var1|salt)  \nWhere, var1 contains the fields as described in the var1 description.",
    "2-2": " ",
    "3-0": "var1",
    "3-1": "`string (JSON)` This parameter is in a JSON format and fields included in the JSON format are explained the [JSON request structure table](#json-request-structure).",
    "3-2": "For an example, refer the [Request Structure](#request-structure-for-var1-to-be-included-in--payment_split-api) subsection."
  },
  "cols": 3,
  "rows": 4,
  "align": [
    null,
    null,
    null
  ]
}
[/block]

## Request structure for var1 to be included in  payment\_split API

```plaintext
{  "type": "absolute",  
    "payuId": "<PayuID of parent transaction which needs to be split>",  
   "splitInfo": 
     {    
        "<Child Merchant 1 key>":{
         "aggregatorSubTxnId":"<unique transaction ID for this specific sub-transaction>",
         "aggregatorSubAmt":"<amount to be transferred to this child merchant>",
         "aggregatorCharges":"<charges associated with this entity's part of the transaction to be transferred to parent (optional)>"
      },
      "<Child merchant 2 key>":{
         "aggregatorSubTxnId":"<unique transaction ID for this specific sub-transaction>",
         "aggregatorSubAmt":"<amount to be transferred to this child merchant>"
      },
       "Child merchant 3 key":
       {
        "aggregatorSubTxnId": "<unique transaction ID for this specific sub-transaction>",
        "aggregatorSubAmt": "<amount to be transferred to this child merchant>",
        "aggregatorCharges": "<charges associated with this entity's part of the transaction to be transferred to parent (optional)>"
       }
    }
}
```

## JSON request structure

The **var1** parameter is in JSON format. The fields in the JSON format are described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "type",
    "0-1": "The type of split is specified in this field. Use **absolute** in this field. The absolute amount is specified for each part of the split. The absolute amount is specified in the aggregatorSubAmt field of the JSON for each child or aggregator.",
    "0-2": "absolute",
    "1-0": "payuid",
    "1-1": "The payment identifier provided by PayU for the transaction.",
    "1-2": "403993715525003544",
    "2-0": "splitInfo",
    "2-1": "This parameter must include the list of aggregator sub transaction IDs and sub amounts as specified in the [Request Structure for var1](#request-structure-for-var1-to-be-included-in--payment_split-api) subsection:  \n  \n- **aggregatorSubTxnId**: The aggregator sub transaction ID is specified in this field.\n- **aggregatorSubAmt**: The aggregator sub amount is specified in this field.\n- **aggregatorCharges**: The aggregator charges is specified in this field.**Note**: The aggregatorCharges field can only be used by parent merchant to get the aggregator commission.",
    "2-2": "Refer to [Request Structure for var1](#request-structure-for-var1-to-be-included-in--payment_split-api) subsection."
  },
  "cols": 3,
  "rows": 3,
  "align": [
    null,
    null,
    null
  ]
}
[/block]

## Sample request

```curl
curl -X POST "https://info.payu.in/merchant/postservice?form=2"
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
“key=A6lB8r&command=payment_splity&var1="type":"absolute","payuId":"403993715525003544","splitInfo":{"imAJ7I":{"aggregatorSubTxnId":"CHild101","aggregatorSubAmt":"50"},"qOoYIv":{"aggregatorSubTxnId":"Child202","aggregatorSubAmt":"50"}}}&hash=6692a8b560c51e8a4bb830206d3b8fac3678fb5b08443c7590047545beba66ec97257fec11775abbc339eabbaf1b1bf5e1c50d2c6bbf67e1a69ad597480d3691"
```

## Sample response

- Sample response for a successful split:

When split get saved & created

```plaintext
{
  "status": 1,
  "message": "Splits creation successful.",
  "splitStatus": "success",
  "splitSegments": [
    {
      "merchantKey": "imAJ7I",
      "amount": 50,
      "subvention_amount": 0,
      "txnId": "CHild101",
      "additional_charges": 0,
      "transaction_fee": 50    },
    {
      "merchantKey": "qOoYIv",
      "amount": 50,
      "subvention_amount": 0,
      "txnId": "Child202",
      "additional_charges": 0,
      "transaction_fee": 50    }
  ]
}
```

- Sample response when split gets saved but are not yet created:

When split get saved but aren’t yet created)

```plaintext
{
  "status": 2,
  "message": "Splits saved, but not created yet",
  "splitStatus": "PENDING"
}
```

- Split creation is failed:

In this sample response, the **error\_code** and **error\_desc** parameters display based on the failure. For the list of error\_codes, refer to [Error Codes & Error Messages](https://devguide.payu.in/split-apis/steps-to-create-the-split/payment_split-api/#Error).

```plaintext
{
  "status": 0,
  "error_code": "AGG-107",
  "error_desc": "Invalid split payload in payment request"
}
```

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

## Error codes & messages

| **Condition**                                           | **error\_code** | **error\_message**                                                    |
| ------------------------------------------------------- | --------------- | --------------------------------------------------------------------- |
| Invalid request posted by merchant in var1              | AGG-107         | Invalid split payload in payment request                              |
| Invalid parent payuId                                   | AGG-103         | This transaction is not a aggregator flow base transaction            |
| Split already exists for requested PayUId               | AGG-104         | Split info already exists for this transaction                        |
| Invalid Child merchant in split requeset                | AGG-102         | One or more child merchant-keys provided are invalid                  |
| If sum amount won’t match wrt parent transaction amount | AGG-108         | Total amount provided in split doesn\\'t match the transaction amount |
| If merchant is not Aggregator flow merchant.            | AGG-101         | This merchant is not an Aggregator flow merchant.                     |
| When transaction is locked in other process             | AGG-110         | Some exception occurred. Try after sometime.                          |

> 📘 Note:
> 
> API integration and authentication would be the same as that for general transaction flow.