---
title: '[Hidden]Penny Verify API'
excerpt: ''
api:
  file: partner-apis-6.json
  operationId: penny_verify
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to verify the bank accounts, and the purposes of this API are:

* Used to verify the bank account when it is not verified automatically.
* Used to submit the penny value deposited by PayU in the merchant account.
* Authorization through the user token received using User Token APIs

> 📘 Note:
>
> The access token with the scope as **user\_token** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

<PARTNEROnboardingEnvironment />

<details>
  <summary>Sample request</summary>

```curl
curl --location -g --request POST '{{onboarding_url}}/api/v1/merchants/{{merchant_uuid}}/verify_penny' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '{    "penny_amount": "1.03"}'
```

</details>

<details>
  <summary>Sample response</summary>

```
{  
        "message": "Bank verification successful"
}
```

</details>

## Request parameters