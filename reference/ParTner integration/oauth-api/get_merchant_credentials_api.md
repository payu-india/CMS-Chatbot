---
title: Get Merchant Credentials API
excerpt: ''
api:
  file: partner-apis-27.json
  operationId: Getmerchantcredentials
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Get Merchant Credentials** API is used to perform the following:

- Used to get the merchant credentials to generate the API Key and Salt
- Authorized using the Client ID and Client Secret to generate the access token

The merchant ID in the request header must be included as a query parameter in the **mid** field.

**Environment**

|                        |                               |
| :--------------------- | :---------------------------- |
| Test Environment       | &lt;https://uat-partner.payu.in&gt; |
| Production Environment | &lt;https://partner.payu.in&gt;     |

> 📘 Note:
>
> The access token with the scope as **read_merchant_reseller** from is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

<details>
  <summary>Sample request</summary>

```curl
curl --location --request GET '{{partner_base_url}}api/v1/merchants/{{merchant_id}}/credential' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer w0282c38b64e072f3d66e4e6efee9789ffe1250f0cd04c20753d6e6f25df9cc7'
```

</details>

<details>
  <summary>Sample response</summary>

**Success Scenario**

```
{
  "data": {
    "credentials": {
      "prod_key": "JPM7Fg",
      "prod_salt": "a*******"
    }
  }
}
```

**Failure Scenarios**

- When the token is invalid

```plaintext
{
  "status": "Unauthorized"
}
```

- When credentials were incorrect for a referred merchant

```plaintext
{
  "status": "Unauthorized"
}
```

</details>

## Request parameters