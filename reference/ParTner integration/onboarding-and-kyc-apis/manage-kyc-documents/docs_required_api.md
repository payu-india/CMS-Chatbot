---
title: '[OLD]Documents Required API'
excerpt: ''
api:
  file: partner-apis-6.json
  operationId: DocsrequiredAPI
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to fetch list of documents required for completing KYC of merchant.

> 📘 Note:
>
> The access token with the scope as refer\_merchant is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

The merchant ID in the request header must be included as a query parameter in the **mid** field.

<PARTNEROnboardingEnvironment/>

<details>
  <summary>Sample request</summary>

```
curl --location --request GET 'https://test-partner.payu.in/api/v3/merchants/8011767/kyc_document/required_docs' \
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