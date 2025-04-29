---
title: Get Split Info API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Get Split Info API
  description: ''
  keywords:
    - Get Split Info API
    - ' Split Information API for Split Settlemements'
    - Get Information on Split Transactions
    - Information on Split Transactions
    - Split Transaction Information
  robots: index
next:
  description: ''
---
The **Get Split Info **API is used for getting split info of the parent transaction in the aggregator flow.

<GENERALAPIsEnvironment />

## Request parameters

The request body contains the following parameters:

[block:parameters]
{
  "data": {
    "h-0": "**Params**",
    "h-1": "**Description**",
    "h-2": "Example",
    "0-0": "key  \n`mandatory`",
    "0-1": "Merchant key provided by PayU",
    "0-2": "JPM\\*\\*\\*g",
    "1-0": "command  \n`mandatory`",
    "1-1": "This parameter must contain the API Command for getting Transaction. It should be `get_split_info` for **Get Split Info** API.",
    "1-2": "",
    "2-0": "var1  \n`mandatory`",
    "2-1": "This parameter must contain the PayU ID",
    "2-2": " 403993715532325577",
    "3-0": "hash  \n`mandatory`",
    "3-1": "This parameter must contain the hash value to be calculated at your end. Hash logic for this API is:  `\nsha512(key\\|command\\|payuId\\|salt) sha512`",
    "3-2": ""
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


## Sample request

```
curl --location 'https://test.payu.in/merchant/postservice.php?form=1' \
--header 'Cookie: PHPSESSID=j601h8g2u1cofo4u5it8v1lk8r; PHPSESSID=670cf11080b74' \
--form 'key="JPM***g"' \
--form 'command="get_split_info"' \
--form 'var1="403993715532325577"' \
--form 'hash="49fa996d81f66374fbe2eedfc494b48149f1abb9555afa0b0c03d671d7a769efd07e40eabee6571fba124966b1a2d219b8118ff9500456effb1e0ae63d94a3e2"' \
```

## Response parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "status",
    "0-1": "This parameter returns the status of web service call. The status can be any of the following:  \n_ 0 - If web service call failed.  \n_ 1 - If web service call succeeded",
    "0-2": "0",
    "1-0": "payuId",
    "1-1": "This parameter returns the parent merchant PayU ID that was posted in the API request.",
    "1-2": "403993715532325577",
    "2-0": "splitStatus",
    "2-1": "This parameter returns the reason string. For a list of error codes for failure scenarios, refer to [Error codes for failure scenario](#error-codes-for-failure-scenario)",
    "2-2": "success",
    "3-0": "splits",
    "3-1": "This parameter contains the response in a JSON array format. Each JSON object contains the following:  \n  \n- merchant key\n- aggregator sub-transaction ID\n- amount\n- Transaction_details field.",
    "3-2": "`{\n            \"merchantKey\": \"iC***G\",\n            \"aggregatorSubTxnId\": \"dkjgfrfgnfm\",\n            \"amount\": 900.00,\n            \"splitType\": \"split\"\n  }`"
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


<br />

## Sample response

### Success scenariro

```
{
    "status": 1,
    "payuId": 403993715532325577,
    "splitStatus": "success",
    "splits": [
        {
            "merchantKey": "iC***G",
            "aggregatorSubTxnId": "dkjgfrfgnfm",
            "amount": 900.00,
            "splitType": "split"
        },
        {
            "merchantKey": "ut***U",
            "aggregatorSubTxnId": "dkfhdgfcdcddfn",
            "amount": 100.00,
            "splitType": "commission"
        }
    ]
}
```

## Error codes for failure scenario

[block:parameters]
{
  "data": {
    "h-0": "**Condition**",
    "h-1": "**error\\_code**",
    "h-2": "**error\\_message**",
    "0-0": "Hash validation failed",
    "0-1": "AGG-300",
    "0-2": "Hash validation failed",
    "1-0": "invalid parent transaction Payu ID:  \n  \n- non-existent PayuID\n- PayuID is not a parent transaction of aggregator flow\n- Payu ID belongs to some other merchant.",
    "1-1": "AGG-301",
    "1-2": "Invalid PayuID",
    "2-0": "Split doesn’t exist for the transaction",
    "2-1": "AGG-302",
    "2-2": "Split doesn't exist for this transaction"
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