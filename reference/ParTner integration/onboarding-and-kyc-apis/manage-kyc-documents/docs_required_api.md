---
api:
  file: Documents_Required_API_Collection.json
  operationId: DocumentsrequiredforKYC
hidden: false
metadata:
  title: Documents Required for KYC API
  keywords:
    - Documents Required for KYC API
    - Doc Required for KYC
---
This API is used to fetch list of documents required for completing KYC of merchant.

> 📘 Notes:
>
> * The access token with the scope as refer_merchant is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).
> * The merchant ID in the request header must be included as a query parameter in the **mid** field. This can found in the [Create Merchant API](ref:create_merchant_api) response.

<br />

<Partner_Postman />

<br />

<PARTNEROnboardingEnvironment />

<details>
  <summary>Sample request</summary>

  ```
  curl --location --request GET 'https://uat-partner.payu.in/api/v3/merchants/8011767/kyc_document/required_docs' \
  --header 'Authorization: Bearer 8881fa7eb0943423e0a136b44d44f7ec2632991f34302947659654515a1e7965'
  ```
</details>

<details>
  <summary>Sample request</summary>

  ```
  {
    "business_entity": null,
    "document_categories": []
  }
  ```
</details>
