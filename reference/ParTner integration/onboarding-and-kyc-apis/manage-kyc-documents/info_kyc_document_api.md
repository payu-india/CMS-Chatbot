---
title: Info KYC Document API
api:
  file: Info_KYC_Document_API_With_BusinessEntity.json
  operationId: InfoKYCdocument
hidden: false
metadata:
  title: Info KYC Document API
---
This API is used to fetch a list of documents required for completing the KYC of the merchant. The access token is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get-token-api).

The merchant ID in the request header must be included as a query parameter in the mid field.

## Authentication

> The access token with the scope as **refer\_merchant** from is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

> 📘 Notes:
>
> * You can pass either the business entity type or the merchant ID in the request. However, ensure that the Merchant ID that you are passing is referred by you. If both business entity & merchant Id is passed in info KYC API, MID takes precedence.
> * PayU recommends using merchant ID to get specific KYC docs for the merchant.

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