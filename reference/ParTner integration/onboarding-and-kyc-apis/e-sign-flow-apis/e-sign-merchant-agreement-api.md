---
api:
  file: ESign_Merchant_Agreement_API.json
  operationId: EsignMerchantAgreement
hidden: false
metadata:
  title: E-Sign Merchant Agreement API
---
This API is used to e-sign merchant agreements, and it is used while E-Sign PayU Service Agreement is generated and signed.

This API requires an access token using the **Get Token** API with the scope as **EsignMergedDocument**. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

<Callout icon="📘" theme="info">
  **Prerequisite**: All KYC docs and website has to be in approved state for the merchant.
</Callout>

<br />

<Partner_Postman />

<br />

**Environment**

|                            |                                                            |
| :------------------------- | :--------------------------------------------------------- |
| **Test Environment**       | \<[https://uatoneapi.payu.in>](https://uatoneapi.payu.in>) |
| **Production Environment** | \<[https://oneapi.payu.in>](https://oneapi.payu.in>)       |

## Request Headers

> 📘 Note:
>
> * The access token with the scope as **EsignMergedDocument** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).
> * uuid value can be found in the response of the **Create Merchant ** API that must be used as the path parameter. For more information, refer to [Create Merchant API](ref:create_merchant_api).

|               |                           |
| ------------- | ------------------------- |
| Authorization | Bearer \{\{access_token}} |
| Content-Type  | multipart/form-data       |

## Request Parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>otp<br><strong>mandatory</strong> </p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter must include the OTP that is received by merchant when you initiate the Send OTP to Signatory Email API. For more information, refer to <a href="http://docs.payu.in/reference/send-otp-to-signatory-email-api">Send OTP to Signatory Email API</a></p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample Request

```curl
curl --location --request POST '{{onboarding_url}}/api/v3/merchants/{{merchant_uuid}}/kyc_documents/{{kyc_doc_uuid}}/esign_merged_document' \
--header 'Authorization: Bearer {{access_token}}' \
--data-urlencode 'otp=0025'
```

Where **\{\{onboarding_url}}** is substituted with the URL specified in the Test or Production environment as mentioned in the _Environment_ section.

## Sample Response

### Success Scenario

Successful response

```plaintext
{
  "kyc_document": {
    "id": 276,
    "document_category_id": 13,
    "document_type_id": null,
    "account_id": null,
    "remarks": null,
    "status": "Counter Signed Received",
    "uuid": "11eb-de39-fdc897e2-ade0-a483e7015be5",
    "active": true,
    "created_at": "2021-07-06T09:10:21.000Z",
    "updated_at": "2021-07-06T09:23:49.000Z",
    "kyc_document_type": "Agreement",
    "document_format": "Soft Copy",
    "e_stamp_number": null,
    "temp_account_id": null,
    "error": null,
    "record_type": "Merchant",
    "record_id": 1,
    "processed_document": {
      "id": 524,
      "metadata": {
        "identified": true
      },
      "filename": "Service Agreemente_stamp.pdf",
      "byte_size": 463727,
      "path": "/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBdW9CIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--a85cda277088a85f7d0f53c9bbe502d24c784f63/Service%20Agreemente_stamp.pdf",
      "kyc_document_uuid": "11eb-de39-fdc897e2-ade0-a483e7015be5"
    },
    "document_category_name": "Service Agreement",
    "document_type_name": null,
    "uploaded_documents": [],
    "document_category": {
      "id": 13,
      "name": "Service Agreement",
      "name_on_frontend": "SERVICE_AGREEMENT"
    }
  }
}
```

### Failure Scenarios

* Merchant is not found with the given merchant_uuid

Merchant is not found with the given merchant_uuid

```plaintext
{
  "status": "NotFound"
}
```

* OTP has expired

OTP has expired

```plaintext
{
  "error": "OTP Expired, Please send new OTP."
}
```

* OTP is incorrect

OTP is incorrect

```plaintext
{
  "error": "Entered OTP is incorrect. Otp attempts remaining are 9."
}
```

* KYC document not found with the given merged_document_uuid

KYC document not found with the given merged_document_uuid

```plaintext
{
  "status": "NotFound"
}
```

* Unauthorized response

Unauthorized response

```plaintext
{
  "status": "Unauthorized"
}
```
