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

| Parameter | Reference |
|-----------|-----------|
| key | For more information on how to generate the Key and Salt, refer to any of the following:<br/>• **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)<br/>• **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt) |
| hash | Hash logic for this API is:<br/>sha512(key\|command\|var1\|salt) |

## Response parameters description and sample response

| **Parameter** | **Description** | **Example** |
|---------------|-----------------|-------------|
| status | The status of the response can be any of the following:<br/>• **1:** Success<br/>• **2:** Failure | 1 |
| msg | The description of the response whether the card details were stored successfully or not. | Refunds fetched successfully. |
| Refund Details | The details are sent by PayU in JSON format for the successful response. For more information, refer to [Additional Info for General APIs](ref:addl-info-general-apis#description-of-the-refund-details-json-fields). | |

> 📘 **Reference:**
>
> For sample response, refer to [Additional Info for General APIs](addl-info-general-apis#description-of-the-refund-details-json-fields).

## Request parameters

**Example values**

Use the following sample values while trying out the API:

* `var1` (txnid): db97dd56eff7296e5061
