---
title: '[Bckup]Get All Refunds from Transaction IDs'
excerpt: 'API Command: **getAllRefundsFromTxnIds**'
api:
  file: get-all-refunds-for-txnid-1.json
  operationId: GetAllRefundsfromTransactionIDs
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Get All Refunds for a Transaction ID** API (getAllRefundsFromTxnIds) command is used to retrieve the status of all the refund requests fired for a particular Transaction ID. The output of this API provides the request ID, and the PG used the status of a refund request and the creation of refund date information.

<GENERALAPIsEnvironment />

## Reference information for request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "0-0": "key",
    "0-1": "For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  \n- **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "1-0": "hash",
    "1-1": "Hash logic for this API is:  \n`sha512(key\\|command\\|var1\\|salt) sha512`"
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Response parameters description and sample response

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "status",
    "0-1": "The status of the response can be any of the following:  \n-   **1:** Success  \n-  ** 2:** Failure",
    "0-2": "1",
    "1-0": "msg",
    "1-1": "The description of the response whether the card details were stored successfully or not.",
    "1-2": "Refunds fetched successfully.",
    "2-0": "Refund Details",
    "2-1": "The details are sent by PayU in JSON format for the successful response. For more information, refer to [Additional Info for General APIs](ref:addl-info-general-apis#description-of-the-refund-details-json-fields).",
    "2-2": ""
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


> 📘 Reference:
> 
> For sample response, refer to[ Additional Info for General APIs](addl-info-general-apis#description-of-the-refund-details-json-fields).

## Request parameters

**Example values ** 

Use the following sample values while trying out the API:

- `var1` (txnid): db97dd56eff7296e5061