---
title: '[OLD]Invoice Upload API'
excerpt: ''
api:
  file: invoice-upload-api-1.json
  operationId: InvoiceAPI
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Invoice Upload** API is used to collect Invoices or AWB from Cross-Border Payments merchants through upload from the Merchant Dashboard. Invoice ID and Invoice file will be passed by merchants selling software, whereas, for merchants selling goods, there will be separate requests for passing Invoice ID, Invoice file, and AWB number, AWB file.

The **Invoice Upload** API expects only the Invoice ID and Invoice file for merchants selling services. However, for merchants selling goods, different requests must be made to pass the Invoice ID and Invoice file, as well as AWB no. and AWB file; thus, the **Invoice Upload** API would need to be called twice.

Merchant calls the **Invoice Upload** API with the file to be uploaded, PayU ID (mihpayuid), and other mandatory parameters to access the info API. For merchants who have to include the AWB details (AWB no. and AWB file), they need to use the Invoice Upload API as mentioned in the following subsections:

- [Including Single AWB Details](#including-single-awb-details)
- [Including Multiple AWB Details](#including-multiple-awb-details)

## Including single AWB details

The **Invoice Upload** API expects only the Invoice ID and Invoice file for merchants selling services. However, for merchants selling goods, different requests must be made to pass the Invoice ID and Invoice file, as well as AWB no. and AWB file; thus, the **Invoice Upload** API would need to be called twice.

## Including multiple AWB details

If a merchant is shipping multiple physical goods through various vendors on an invoice, you need to post multiple requests.

For example, you have a customer ordered from two vendors, where vendorA is shipping the product from London and vendorB is shipping the product from Amsterdam. Here, the AWB no. and corresponding AWB file are different for both vendors. Hence, you need to post three requests using the **Invoice Upload** API. Where the first request contains the invoice, the second request contains vendorA AWB no. & AWB file, and the third request contains vendorB AWB no. & AWB file.

To include multiple AWB details using the **Invoice Upload** API:

1. Post the first request using the **Invoice Upload** API with the Invoice ID and Invoice file as mentioned in the [Request Parameters](#request-parameters) table.
2. Post the request using the **Invoice Upload** API for the next AWB no. and corresponding AWB file.
3. Repeat Step 2 until you have posted for all the AWB no. and the corresponding AWB file.

> 📘 Note
>
> You need to ensure that the Invoice ID and Invoice file are posted only once in the above procedure.

**Environment**

|                            |                                  |
| :------------------------- | :------------------------------- |
| **Test Environment**       | <https://test.payu.in/merchant/> |
| **Production Environment** | <https://info.payu.in/merchant/> |

## Request Parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "key",
    "0-1": "Merchant key provided by PayU. For more information on checking your key and Salt, refer to [Generate Merchant Key and Salt on PayUBiz Dashboard](https://devguide.payu.in/merchant-integration/getting-started-with-web-checkout/generate-key-and-salt-payubiz/).",
    "0-2": "Your Test Key",
    "1-0": "command",
    "1-1": "The API command for this API, that is, **opgsp\\_upload\\_invoice\\_awb** must be specified for this parameter.",
    "1-2": "opgsp\\_upload\\_invoice\\_awb",
    "2-0": "var1  \n(primaryKey)  \n**mandatory**",
    "2-1": "The PayU ID (mihpayuid) of the transaction must be specified in this field. The Invoice or AWB will be uploaded basis of the PayU ID.",
    "2-2": "`403993715521937565`",
    "3-0": "var2  \n(uniqueNumber)  \n**mandatory**",
    "3-1": "The invoice ID or AWB ID is specified in this parameter. Alphanumeric with special characters is allowed.",
    "3-2": "`9eec02ac9e2efc335bdda2d7486121ce03de24c2fa7d32d17462ad5a6a9058db`",
    "4-0": "var3  \n(uploadType)  \n**mandatory**",
    "4-1": "The type of document to be uploaded is specified in this field, and it can be any of the following:  \n   - Invoice  \n   - AWB",
    "4-2": "AWB",
    "5-0": "file   \n(attachment)  \n**mandatory**",
    "5-1": "The absolute path of the file to be uploaded is specified in this parameter. The maximum size supported is 2 MB and the following formats are supported:  \n   - PDF (.pdf)  \n   - Document (.doc or.docx)  \n   - Image (.jpg, .jpeg)  \n**Note**: The Merchant Dashboard supports only the .pdf and .docx formats.",
    "5-2": "C:\\\\invoice.docx",
    "6-0": "hash",
    "6-1": "The hash is generated in the following format:  \nsha512(key|command|var1|salt) sha512",
    "6-2": " "
  },
  "cols": 3,
  "rows": 7,
  "align": [
    null,
    null,
    null
  ]
}
[/block]

## Sample request

```curl
curl --location -g --request POST '{{baseUrl}}/merchant/postservice?form=2' \
--form 'key="{{merchantKey}}"' \
--form 'command="opgsp_upload_invoice_awb"' \
--form 'var1="403993715525825059"' \  - PayuId
--form 'var2="TestInv0001234568"' \ - invoice Id
--form 'var3="Invoice"' \ - type of upload - Invoice/AWB
--form 'file=@"/path/to/file"' \ - file
--form 'hash="{{hash}}"'
```

## Sample response

### Success Scenario

- When a file is uploaded successfully:

```plaintext
{
"responseCode":"00",
"responseMsg":"File Uploaded Successfully"
}
```

### Failure Scenarios

- When there is an error in uploading the file:

```plaintext
{
"responseCode": "103",
"responseMsg": "Failed to Upload"
}
```

- When the file format is not supported:

```plaintext
{
"responseCode": "105",
"responseMsg": "Not an OPGSP merchant, contact KAM"
}
```

- When the payuid is invalid:

```plaintext
{
"responseCode":"107",
"responseMsg":"The PayuID in request is invalid"
}
```

- When a mandatory field is missing:

```plaintext
{
"responseCode":"109",
"responseMsg":"All fields are mandatory, please check!"
}
```

## Response Code and Description

| **Response Code** | **Response Message**                | **Description**                                     |
| ----------------- | ----------------------------------- | --------------------------------------------------- |
| 00                | Uploaded Successfully               | AWB/Invoice has been uploaded successfully          |
| 101               | Invalid Format                      | When format is not pdf, .doc, .docx, .jpg or .jpeg  |
| 102               | Invalid Transaction Status          | If the transaction is not captured/auto-refunded    |
| 103               | Failed to Upload                    | In case of some error in uploading the file         |
| 104               | Invalid upload type                 | Only invoice and AWB are allowed                    |
| 105               | Not an OPGSP merchant, contact KAM  | If the merchant is not mapped as an OPGSP merchant  |
| 106               | Size exceeding 5 MB                 | When file size is greater than 2 MB                 |
| 107               | Invalid PayU ID                     | The PayU ID in the request is missing or invalid    |
| 108               | Empty Invoice/AWB ID                | The invoice/AWB ID is missing                       |
| 109               | Empty file name                     | Mandatory field(s) is/are missing                   |