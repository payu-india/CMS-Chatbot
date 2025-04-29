---
title: Add or Update Bank Details API
excerpt: ''
api:
  file: partner-integration-updated-2.json
  operationId: AddorUpdateBankDetails
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to perform the following:

- Used to add or update the bank account details, only after a successful verification of merchant’s PAN card details.
- Authorized using the user token received from verify OTP API

> 📘 Note:
> 
> The access token with the scope as **create_bank_details** (to create bank details) or **update_bank_details** (to update bank details) is required on the header. For more information on getting the access token, refer to [User Token APIs](ref:user-token-apis).

<PARTNEROnboardingEnvironment />

<details><summary>Sample request</summary>

```curl
curl --location -g --request POST '{{partner_base_url}}/api/v1/merchants/{{merchant_uuid}}/add_bank_detail' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "bank_detail": {
        "bank_account_number": "91234567894",
        "ifsc_code": "UTIB0000367",
        "holder_name": "kapil kumar"
    }
}'
```

</details>

<details><summary>Sample response</summary>

```
{
    "bank_detail": {
        "branch_name": "DAHOD GUJARAT",
        "bank_account_number": "91234567896",
        "ifsc_code": "UTIB0000367",
        "holder_name": "kapil kumar",
        "bank_verification_status": "Pending",
        "uuid": "11ea-b455-b8d8cf3a-b32e-38f9d3c7f51b",
        "created_at": "2020-06-22T06:58:05.000Z",
        "updated_at": "2020-06-22T06:58:05.000Z",
        "bank_name": "AXIS BANK",
    }
}
```

<br>

</details>

## Request parameters