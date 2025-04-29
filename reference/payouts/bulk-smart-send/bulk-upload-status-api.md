---
title: Bulk Upload Status API
excerpt: ''
api:
  file: new-payouts-api-collection-2.json
  operationId: BulkUploadStatusAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Bulk Upload Status** API is used to get the status of the bulk files uploaded and processed.

**Environment**

|                            |                                                                        |
| -------------------------- | ---------------------------------------------------------------------- |
| **Test Environment**       | <https://staging.payu.in/payout/v2/bulkUpload/transfers/{fileId}>      |
| **Production Environment** | <https://payout.payumoney.com/payout/v2/bulkUpload/transfers/{fileId}> |

<details><summary>Sample request</summary>

```curl
curl --location 'https://uatoneapi.payu.in/payout/v2/bulkUpload/transfers/1' \
--header 'Content-Type: application/json' \
--header 'authorization: Bearer 6e47dc301158318020af04917b256422cf7f8e11147807102abe5b984c7a03e7' \
--header 'pid: 2225335'
```

</details>

<details><summary>Sample response</summary>

```
{
    "status": 0,
    "msg": null,
    "code": null,
    "data": {
        "id": 60841,
        "fileName": "onepayu-payout/2023-02-09_16-58-05_388356c1-fe02-41f6-9284-a3db8d5037571675942085303.xlsx",
        "merchantId": 1111893,
        "displayName": "sampleBulkSmartSend.xlsx",
        "totalRows": 3,
        "successfulRows": 0,
        "failedRows": 3,
        "status": "COMPLETED",
        "addedOn": "2023-02-09T11:28:05.000+0000",
        "updatedOn": "2023-02-09T11:28:15.000+0000",
        "uploadedBy": "11e9-2af7-c3ab6604-8e42-024f56162d44",
        "fileExportId": 198833,
        "fileSource": "DASHBOARD_SMART_SEND"
    }
}
```

</details>

## Request header and parameters

> 📘 Note:
> 
> The **pid** is **payoutMerchantId**, however it is different from the PayU merchant id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your **payoutsMerchantID**.

> 📘 Reference
> 
> For the list of error messages and their description that you may encounter when Smart Send APIs integration, refer to [Error Codes](ref:error-codes-for-payouts).