---
title: Absolute Split After Transaction
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

## Request structure for var1 to be included in payment\_split API

```plaintext
{  "type": "absolute",  
    "payuId": "xxxxxxxx", # PayuID of parent transaction which needs to be split.  
   "splitInfo": 
    {    
       "merchantKey1": 
       {
       "aggregatorSubTxnId": "30nknyhkhib",
       "aggregatorSubAmt": "8",
       "aggregatorCharges": "2" // parent merchant commission (Optional)    
       },
      "merchantKey2":
      {
       "aggregatorSubTxnId": "13u0nknou0",
       "aggregatorSubAmt": "2"
      },
       "merchantKey3":
       {
        "aggregatorSubTxnId": "13u0nknou02",
        "aggregatorSubAmt": "2",
        "aggregatorCharges": "1" // parent merchant commission (Optional)
       }
     }
}
```

## Sample response

Sample response for a successful split:

```plaintext
{  
 "status": 1,  
 "message": "Splits creation successful.",  
 "splitStatus": "success",  "splitSegments": 
   [
         {
           "merchantKey": "merchantKey1",
           "amount": 8,
           "subvention_amount": 0,
            "txnId": "30nknyhkhib",
           "additional_charges": 0,
           "transaction_fee": 8    },
           {
             "merchantKey": "merchantKey2",
            "amount": 2,
```