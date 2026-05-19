---
api:
  file: Generate_Merchant_Agreement_For_ESign_API_v0.json
  operationId: GenerateMerchantAgreementForEsign
hidden: false
metadata:
  title: Generate Merchant Agreement For E-Sign
---
This API is used to generate merchant agreements used while E-Sign PayU Service Agreement is generated and signed.

<Callout icon="📘" theme="info">
  **Prerequisite**: All KYC docs and website has to be in approved state for the merchant.
</Callout>

<br />

<Partner_Postman />

<br />

<br />

<PartnerKYCEnv />

## Request Headers

> 📘 Notes:
>
> * The access token with the scope as **generate_merged_document_for_esign** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).
> * uuid value can be found in the response of the  **Create Merchant** API that must be used as the path parameter. For more information, refer to [Create Merchant API](ref:create_merchant_api).

|               |                         |
| ------------- | ----------------------- |
| Authorization | Bearer `{access_token}` |
| Content-Type  | multipart/form-data     |

## Sample Request

```curl
curl --location --request GET '{onboarding_url}/api/v3/merchants/{uuid}/generate_merged_document_for_esign' \
--header 'Authorization: Bearer {access_token}'
```

Where **`{onboarding_url}`** is substituted with the URL specified in the Test or Production environment as mentioned in the _Environment_ section.

## Sample Response

### Success Scenario

Successful response

```plaintext
{
  "kyc_document": {
    "id": 273,
    "document_category_id": 13,
    "document_type_id": null,
    "account_id": null,
    "remarks": null,
    "status": "accepted",
    "uuid": "11eb-de10-3a450888-a354-a483e7015be5",
    "active": true,
    "created_at": "2021-07-06T04:11:24.000Z",
    "updated_at": "2021-07-06T04:14:41.000Z",
    "kyc_document_type": "Agreement",
    "document_format": "Soft Copy",
    "e_stamp_number": null,
    "temp_account_id": null,
    "error": null,
    "record_type": "Merchant",
    "record_id": 1,
    "processed_document": {
      "id": 505,
      "metadata": {
        "identified": true
      },
      "filename": "merged_doc_6.pdf",
      "byte_size": 433824,
      "path": "/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBdG9CIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--206157392f9c6564fe16971b9783ef352030ac40/merged_doc_6.pdf",
      "kyc_document_uuid": "11eb-de10-3a450888-a354-a483e7015be5"
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

* The agreement could not be generated for the merchant

Agreement could not be generated for the merchant

```plaintext
{
  "error": "Agreement could not be generated"
}
```

* Unauthorized request

Unauthorized request

```plaintext
{
  "status": "Unauthorized"
}
```

* The agreement is not found

Agreement not found

```plaintext
{
  "kyc_document": "Agreement Not Found"
}
```
