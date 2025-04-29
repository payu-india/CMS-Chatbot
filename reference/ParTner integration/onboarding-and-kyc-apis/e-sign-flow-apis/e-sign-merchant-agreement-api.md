---
title: E-Sign Merchant Agreement API
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
This API is used to e-sign merchant agreements, and it is used while E-Sign PayU Service Agreement is generated and signed.

This API requires an access token using the **Get Token** API with the scope as **client\_manage\_agreement**. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

**Environment**

|                            |                             |
| :------------------------- | :-------------------------- |
| **Test Environment**       | <https://uatoneapi.payu.in> |
| **Production Environment** | <https://oneapi.payu.in>    |

## Request Headers

> 📘 Note:
>
> The access token with the scope as **refer\_merchant** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

|               |                         |
| ------------- | ----------------------- |
| Authorization | Bearer {{access_token}} |
| Content-Type  | multipart/form-data     |

## Request Parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "otp  \n**mandatory** ",
    "0-1": "This parameter must include the OTP that is received by merchant when you initiate the Send OTP to Signatory Email API. For more information, refer to [Send OTP to Signatory Email API](ref:send-otp-to-signatory-email-api)"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    null,
    null
  ]
}
[/block]

## Sample Request

```curl
curl --location --request POST '{{onboarding_url}}/api/v1/merchants/{{merchant_uuid}}/kyc_documents/{{kyc_doc_uuid}}/esign_merged_document' \
--header 'Authorization: Bearer {{access_token}}' \
--data-urlencode 'otp=0025'
```

Where **{{onboarding\_url}}** is substituted with the URL specified in the Test or Production environment as mentioned in the _Environment_ section.

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

- Merchant is not found with the given merchant\_uuid

Merchant is not found with the given merchant\_uuid

```plaintext
{
  "status": "NotFound"
}
```

- OTP has expired

OTP has expired

```plaintext
{
  "error": "OTP Expired, Please send new OTP."
}
```

- OTP is incorrect

OTP is incorrect

```plaintext
{
  "error": "Entered OTP is incorrect. Otp attempts remaining are 9."
}
```

- KYC document not found with the given merged\_document\_uuid

KYC document not found with the given merged\_document\_uuid

```plaintext
{
  "status": "NotFound"
}
```

- Unauthorized response

Unauthorized response

```plaintext
{
  "status": "Unauthorized"
}
```