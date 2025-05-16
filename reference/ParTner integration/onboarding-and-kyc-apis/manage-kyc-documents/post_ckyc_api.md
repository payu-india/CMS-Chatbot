---
title: Post CKYC API
excerpt: ''
api:
  file: partner-integration-updated-2.json
  operationId: PostCKYCAPI
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to submit the post the CKYC details of your partner. The access token is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api)

<PARTNEROnboardingEnvironment />

<details>
  <summary>Sample request</summary>

```curl
curl --location -g --request POST '{{onboarding_url}}/api/v3/merchants/kyc_document/ckyc_data' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dob": "01-01-1990",
    "merchant_id": "{{merchant_id}}"
}'
```

</details>

<details>
  <summary>Sample response</summary>

```
{
  "name": "Sardar Khan",
  "gender": "M",
  "dob": "1996-02-14",
  "address": " rz-276,ph-2, gopal nagar, NAJAFGARH, South West Delhi, Delhi, India, 110043",
  "pincode": 110043
}
```

</details>

## Request headers

> 📘 Note:
>
> The access token with the scope as **client\_manage\_kyc\_details** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).