---
title: Bulk File Upload API
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
The **smartSend/bulkUpload/transfers** API is used to upload a .CSV, .XSLX or .XLS file from your Desktop with the correct format. You need to use the **Bulk Process File** API to process the uploaded file containing Smart Send Link APIs. For more information, refer to [Bulk Process File API](ref:bulk-process-file-api)

HTTP Method: **POST**

**Environment**

|                        |                                                                                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Test Environment       | [https://staging.payu.in/payout/v2/smartSend/bulkUpload/transfers>](https://staging.payu.in/payout/v2/smartSend/bulkUpload/transfers>)           |
| Production Environment | [https://payout.payumoney.com/payout/v2/smartSend/bulkUpload/transfers>](https://payout.payumoney.com/payout/v2/smartSend/bulkUpload/transfers>) |

## Request header and parameters

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Authorization
        `mandatory`
      </td>

      <td>
        `String` Specify the access token generated earlier in this parameter.
      </td>

      <td>
        Bearer `{access_token}`
      </td>
    </tr>

    <tr>
      <td>
        pid
        `mandatory`
      </td>

      <td>
        `String` Specify the payout merchant id provided while onboarding or creating Payout account.
      </td>

      <td>
        1111126
      </td>
    </tr>

    <tr>
      <td>
        Content-Type `mandatory`
      </td>

      <td>
        `String` Indicates the format in which the request is sent.
      </td>

      <td>
        application/json
      </td>
    </tr>

    <tr>
      <td>
        file
        `mandatory`
      </td>

      <td>
        `String`Specify the file name (with location) that contains the payouts information to be uploaded.
      </td>

      <td>
         
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Note:
>
> The **pid** is **payoutMerchantId**, however it is different from the PayU merchant id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your **payoutsMerchantID**.

For the list of error messages and their description that you may encounter when Smart Send APIs integration, refer to [Error Codes](ref:error-codes-for-payouts).

## Sample request

```curl
curl --location 'https://testoneapi.payu.in/payout/v2/smartSend/bulkUpload/transfers' \ 
--header 'accept: application/json, text/plain, */*' \ 
--header 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' \ 
--header 'authorization: Bearer 048cb60c19908bd6fa936f5174bf4057f1ae42ea74c38763a1d77bce3ce94942' \ 
--header 'mid: 6776849' \ 
--header 'pid: 1121861' \ 
--form 'file=@"/Users/dheeraj.tharwani/Downloads/sampleBulkSmartSend (1).xlsx"' 
```

## Sample response

```
{
    "status": 0,
    "msg": null,
    "code": null,
    "data": {
        "id": 268,
        "fileName": "57b829a0-0072-486f-b307-689d659b68c41626256208422.xlsx",
        "merchantId": 1111161,
        "displayName": "sampleBulkSmartSend.xlsx",
        "totalRows": 3,
        "successfulRows": 0,
        "failedRows": 0,
        "status": "REQUESTED",
        "addedOn": "2021-07-14T09:50:08.423+0000",
        "updatedOn": "2021-07-14T09:50:08.423+0000",
        "uploadedBy": "11eb-07b8-d41d2154-b089-02f413145cce",
        "fileExportId": null,
        "fileSource": "DASHBOARD_SMART_SEND"
    }
}
```