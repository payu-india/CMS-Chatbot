---
title: Invoice Upload API
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
The **Invoice Upload** API is used to collect Invoices or AWB from Cross-Border Payments merchants through upload from the Merchant Dashboard. Invoice ID and Invoice file will be passed by merchants selling software, whereas, for merchants selling goods, there will be separate requests for passing Invoice ID, Invoice file, and AWB number, AWB file.

> 📘 Reference:
>
> For Cross Border Payments using the **_payment** API, You can use the **Try It** experience with the following integrations:
>
> * [PayU Hosted Checkout](https://docs.payu.in/reference/_payment_cross-border_payu_hosted_checkout)
> * [Merchant Hosted Integration](https://docs.payu.in/reference/merchant-hosted-integration-cb)
>   * [Cards](https://docs.payu.in/reference/_payment_cross-border_merchant_hosted_cards)
>   * [UPI](https://docs.payu.in/reference/_payment_cross-border_merchant_hosted_upi)

HTTP Method: **POST**

The **Invoice Upload** API expects only the Invoice ID and Invoice file for merchants selling services. However, for merchants selling goods, different requests must be made to pass the Invoice ID and Invoice file, as well as AWB no. and AWB file; thus, the **Invoice Upload** API would need to be called twice.

Merchant calls the **Invoice Upload** API with the file to be uploaded, PayU ID (mihpayuid), and other mandatory parameters to access the info API. For merchants who have to include the AWB details (AWB no. and AWB file), they need to use the Invoice Upload API as mentioned in the following subsections:

* [Including Single AWB Details](#including-single-awb-details)
* [Including Multiple AWB Details](#including-multiple-awb-details)

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

<GENERALAPIsEnvironment />

## Request Parameters

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
        key
      </td>
      <td>
        Merchant key provided by PayU. For more information on checking your key and Salt, refer to [Generate Merchant Key and Salt on PayUBiz Dashboard](https://devguide.payu.in/merchant-integration/getting-started-with-web-checkout/generate-key-and-salt-payubiz/).
      </td>
      <td>
        Your Test Key
      </td>
    </tr>
    <tr>
      <td>
        command
      </td>
      <td>
        The API command for this API, that is, **opgsp_upload_invoice_awb** must be specified for this parameter.
      </td>
      <td>
        opgsp_upload_invoice_awb
      </td>
    </tr>
    <tr>
      <td>
        var1\
        (primaryKey)\
        **mandatory**
      </td>
      <td>
        The PayU ID (mihpayuid) of the transaction must be specified in this field. The Invoice or AWB will be uploaded basis of the PayU ID.
      </td>
      <td>
        `403993715521937565`
      </td>
    </tr>
    <tr>
      <td>
        var2\
        (uniqueNumber)\
        **mandatory**
      </td>
      <td>
        The invoice ID or AWB ID is specified in this parameter. Alphanumeric with special characters is allowed.
      </td>
      <td>
        `9eec02ac9e2efc335bdda2d7486121ce03de24c2fa7d32d17462ad5a6a9058db`
      </td>
    </tr>
    <tr>
      <td>
        var3\
        (uploadType)\
        **mandatory**
      </td>
      <td>
        The type of document to be uploaded is specified in this field, and it can be any of the following:
        * Invoice
        * AWB
      </td>
      <td>
        AWB
      </td>
    </tr>
    <tr>
      <td>
        file\
        (attachment)\
        **mandatory**
      </td>
      <td>
        The absolute path of the file to be uploaded is specified in this parameter. The maximum size supported is 2 MB and the following formats are supported:
        * PDF (.pdf)
        * Document (.doc or .docx)
        * Image (.jpg, .jpeg)
        * **Note**: The Merchant Dashboard supports only the .pdf and .docx formats.
      </td>
      <td>
        C:\\invoice.docx
      </td>
    </tr>
    <tr>
      <td>
        hash
      </td>
      <td>
        The hash is generated in the following format:\
        sha512(key|command|var1|salt) sha512
      </td>
      <td>
      </td>
    </tr>
  </tbody>
</Table>

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

* When a file is uploaded successfully:

```plaintext
{
"responseCode":"00",
"responseMsg":"File Uploaded Successfully"
}
```

### Failure Scenarios

* When there is an error in uploading the file:

```plaintext
{ 
“responseCode”: “103”, 
“responseMsg”: “Failed to Upload” 
} 
```

* When the file format is not supported:

```plaintext
{ 
“responseCode”: “105”, 
“responseMsg”: “Not an PACB merchant, contact KAM” 
} 
```

* When the payuid is invalid:

```plaintext
{
"responseCode":"107",
"responseMsg":"The PayuID in request is invalid"
}
```

* When a mandatory field is missing:

```plaintext
{
"responseCode":"109",
"responseMsg":"All fields are mandatory, please check!"
} 
```

## Response Code and Description

Refer to [Response Code and Description - Invoice Upload API](ref:response-code-and-description-invoice-upload-api).