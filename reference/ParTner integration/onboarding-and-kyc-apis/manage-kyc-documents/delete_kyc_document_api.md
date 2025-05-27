---
title: Delete KYC Document API
excerpt: |-
  It is used to delete document for a merchant.

  Test Environment: `https://uat-partner.payu.in`

  Production Environment: `https://partner.payu.in`

  Scope present in Token: `refer_merchant`
api:
  file: partner-apis-6.json
  operationId: delete_document
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to delete the document for a merchant.

> 📘 Note:
>
> The access token with the scope as **refer\_merchant** is required on the header. For more information on getting the access token, refer to o [Get Token API](ref:get_token_api).

<PARTNEROnboardingEnvironment/>

<details>
  <summary>Sample request</summary>

```curl
curl --location -g --request DELETE '{{partner_base_url}}/api/v3/merchants/{{mid}}/kyc_document/{{kyc_document_uuid}}' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/x-www-form-urlencoded'
```

</details>

## Request parameters