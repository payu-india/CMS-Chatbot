---
title: Release Settlement API
excerpt: 'API Command: **release\_settlement**'
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The** Release Settlement** API is used to flag the sub-payment you want to settle; after adding splits for a particular payment, the money will not be settled directly into the child merchants account unless you call a release event corresponding to the individual suborder you want to settle.

**Use Case**: Most marketplace model owners wait for the delivery or dispatch to happen first from the sub-seller’s end. Only after the successful dispatch, the owner will release the funds into the sub-seller’s bank account. This API gives them the flexibility to do so.

The Release Settlement API can be used to release the settlement of all the blocked child transactions in the aggregator workflow.

HTTP Method: **POST**

**Environment**

|                        |                                  |
| :--------------------- | :------------------------------- |
| Test Environment       | <https://test.payu.in/merchant/> |
| Production Environment | <https://info.payu.in/merchant/> |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "key  \n**mandatory**",
    "0-1": "`varchar` The merchant key is included in this parameter.",
    "0-2": "Your Test Key",
    "1-0": "command  \n**mandatory**",
    "1-1": "`varchar` The **release\\_settlement** must be included in this parameter",
    "1-2": "release\\_settlement",
    "2-0": "hash  \n**mandatory**",
    "2-1": "`varchar` The hash string encryption is specified in this parameter.  \nThe format of the hash is:  \nstring key|command|var1|salt  \nWhere var1 is your mihpayuid",
    "2-2": "",
    "3-0": "var1  \n**mandatory**",
    "3-1": "`varchar` The mihpayuId is specified in this parameter",
    "3-2": "8000123",
    "4-0": "var2  \n**mandatory**",
    "4-1": "`varchar` The childMid is specified in this parameter.",
    "4-2": "393437"
  },
  "cols": 3,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Sample request

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2"
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
"key=A****r&command=release_settlement&var1=8000123&var2=8000123&hash=6692a8b560c51e8a4bb830206d3b8fac3678fb5b0844"
```

## Response parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "status",
    "0-1": "The status can contain any of the following values:  \n-    Status will be 1 if API call is a success  \n-    Status will be 0 in case of failure you'll get system handled failure reasons in this case",
    "1-0": "msg",
    "1-1": "Message string for both success and failure cases. "
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


## Sample Response

### Success Scenario

- Successful Transaction

Sample Success Response for Release Settlement

```plaintext
{"status":1,"msg":"Release request is accepted"}
```

## Failure Scenarios

- Failure Response when PayU ID is empty

Failure Response when PayUID is empty

```plaintext
{"status":0,"msg":"payuId is empty"}
```

- Failure response when child merchant ID is empty

Failure response when child merchant ID is empty

```plaintext
{"status":0,"msg":"Mid passed is empty"}
```

- Failure Response when child merchant ID and PayU ID do not match

Failure Response when child merchant ID and PayU ID do not match

```plaintext
{"status":0,"msg":"Invalid childMid and payuId"}
```

- Failure response when attempting to release an already released sub-payment

Failure response when attempt to release an already released sub- payment

```plaintext
{"status":0,"msg":"Release request is already accepted"}
```