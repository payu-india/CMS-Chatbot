---
title: Delete KYC document
api:
  file: Delete_KYC_Document_API_Collection_v2.json
  operationId: DeleteKYCdocument
hidden: false
---
This API is used to delete the document for a merchant.

> 📘 Note:
>
> The access token with the scope as **refer\_merchant** is required on the header. For more information on getting the access token, refer to o [Get Token API](ref:get_token_api).

<PARTNEROnboardingEnvironment />

> 📘 Notes:
>
> This API involves the **mid** and **kyc\_document\_uuid** values as path parameters. Refer to the following for these parameter values:
>
> * **mid** value in the response of the [Create Merchant API](ref:create_merchant_api) for the merchant must be used as the path parameter.
> * **kyc\_document\_uuid** value is in the response for the [Create KYC Document](ref:create_kyc_document_api)API must be used as the path parameter.

<details>
  <summary>Sample request</summary>

  ```curl
  curl --location -g --request DELETE '{{partner_base_url}}/api/v3/merchants/{{mid}}/kyc_document/{{kyc_document_uuid}}' \
  --header 'Authorization: Bearer {{access_token}}' \
  --header 'Content-Type: application/x-www-form-urlencoded'
  ```
</details>

## Request parameters