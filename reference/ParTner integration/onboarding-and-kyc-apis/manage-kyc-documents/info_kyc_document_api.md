---
title: Info KYC Document API
excerpt: ''
api:
  file: partner-apis-6.json
  operationId: DocInfoAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to fetch a list of documents required for completing the KYC of the merchant. The access token is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get-token-api).

The merchant ID in the request header must be included as a query parameter in the mid field.

> 📘 Note:
>
> The access token with the scope as **refer\_merchant** from is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

<PARTNEROnboardingEnvironment />

<details>
  <summary>Sample request</summary>

```
curl --location -g --request GET '{{partner_base_url}}/api/v3/merchants/kyc_document/info?business_entity=Individual' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json'
```

</details>

<details>
  <summary>Sample response</summary>

```
{
  "PAN Card of Signing Authority": [
    "PAN Card"
  ],
  "Address Proof of Signing Authority": [
    "Passport",
    "Aadhar",
    "Voter's ID",
    "Driving Licence",
    "Utilities Bill (electricity, water, landline, gas connection)",
    "Address Verification Letter from Bank"
  ],
  "Bank Account Proof": [
    "Cancelled Cheque",
    "Bank Verification Letter"
  ],
  "Service Agreement": [
    "Service Agreement"
  ]
}
```

</details>

## Request parameters