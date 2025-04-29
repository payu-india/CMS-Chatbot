---
title: Bulk Process File API
excerpt: ''
api:
  file: new-payouts-api-collection-2.json
  operationId: BulkProcessFileAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **smartSend** API is used to process the uploaded .csv/.xlsx/.xls file from the dashboard. You need to use the **Bulk File Upload** API to upload the file containing the Smart Send Links. For more information, refer to [Bulk File Upload API](ref:bulk-upload-api).

HTTP Method: **POST**

**Environment**

|                            |                                                                                  |
| -------------------------- | -------------------------------------------------------------------------------- |
| **Test Environment**       | &lt;https://staging.payu.in/payout/v2/smartSend/bulkUpload/transfers/`{fileId}`&gt;      |
| **Production Environment** | &lt;https://payout.payumoney.com/payout/v2/smartSend/bulkUpload/transfers/`{fileId}`&gt; |

<details>
  <summary>Sample request</summary>

```curl
curl --location --request PUT 'https://uatoneapi.payu.in/payout/v2/smartSend/bulkUpload/transfers/1' \
--header 'Content-Type: application/json' \
--header 'authorization: Bearer 6e47dc301158318020af04917b256422cf7f8e11147807102abe5b984c7a03e7' \
--header 'pid: 2223553'
```

</details>

<details>
  <summary>Sample response</summary>

```
{
	"status": 0,
	"msg": null,
	"code": null,
	"data": {
		"id": 267,
		"fileName": "560f7a80-c7b4-4bce-8124-8ab926420a1e1626256058980.xlsx",
		"merchantId": 1111161,
		"displayName": "sampleBulkSmartSend.xlsx",
		"totalRows": 3,
		"successfulRows": 0,
		"failedRows": 0,
		"status": "IN_PROGRESS",
		"addedOn": "2021-07-14T09:47:39.000+0000",
		"updatedOn": "2021-07-14T10:01:44.135+0000",
		"uploadedBy": "11eb-07b8-d41d2154-b089-02f413145cce",
		"fileExportId": 26632,
		"fileSource": "DASHBOARD_SMART_SEND"
	}
}

```

</details>

## Request header and parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "Authorization`\nmandatory`",
    "0-1": "`String` Specify the access token generated earlier in this parameter.",
    "0-2": "Bearer `access_token`",
    "1-0": "pid`\nmandatory`",
    "1-1": "`String` Specify the payout merchant id provided while onboarding or creating Payout account.",
    "1-2": "1111126",
    "2-0": "Content-Type  \n`mandatory`",
    "2-1": "`String` Indicates the format in which the request is sent.",
    "2-2": "application/json"
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

> 📘 Note:
> 
> The **pid** is **payoutMerchantId**, however it is different from the PayU merchant id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your **payoutsMerchantID**.

> 📘 Reference
> 
> For the list of error messages and their description that you may encounter when Smart Send APIs integration, refer to [Error Codes](ref:error-codes-for-payouts).