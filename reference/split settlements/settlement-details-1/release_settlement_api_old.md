---
title: Release Settlement API
excerpt: ''
api:
  file: payu-biz-aggregator.json
  operationId: releasesettlement
deprecated: false
hidden: true
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

**Environment**

| Test Environment       | <https://test.payu.in/merchant/> |
| :--------------------- | :------------------------------- |
| Production Environment | <https://info.payu.in/merchant/> |

## Request Parameters

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