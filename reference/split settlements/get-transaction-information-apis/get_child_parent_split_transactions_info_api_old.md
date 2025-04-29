---
title: Get Child/Parent Split Transaction Info
excerpt: ''
api:
  file: get-aggregatorparent-transaction-info-3.json
  operationId: GetChildParentSplitTransactionInfo
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The** Get Aggregator Transactions **API is for getting the transaction info of parent merchants in the Aggregator flow.

### Environment

<table style="border:0.1rem solid rgb(242, 242, 242);"><tbody><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Test Environment</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">https://uat-onepayuonboarding.payu.in</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Production Environment</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">https://onboarding.payu.in</td></tr></tbody></table>

## Response parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "status",
    "0-1": "This parameter contains the status of response. It can be any of the following:  \n- **0:** Failed  \n- **1:**Success",
    "1-0": "msg",
    "1-1": "This parameter contains the response or error message.",
    "2-0": "Transaction\\_details",
    "2-1": "This parameter contains the transaction details in an array format and it is displayed only when the **status** field returns the value as **1**. For more information on each field in the array, refer to [Additional Info for Split Settlements APIs](ref:additional-info-for-split-settlements-apis)."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    null,
    null
  ]
}
[/block]


## Request parameters