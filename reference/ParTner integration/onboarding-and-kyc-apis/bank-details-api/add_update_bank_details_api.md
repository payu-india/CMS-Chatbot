---
title: Add or Update Bank Details API
api:
  file: Add_Update_Bank_Details_API_Collection.json
  operationId: Add/UpdateBankDetails
hidden: true
metadata:
  title: Add or Update Bank Details
---
This API is used to perform the following:

* Used to add or update the bank account details, only after a successful verification of merchant’s PAN card details.
* Authorized using the user token received from verify OTP API

> 📘 Note:
>
> To get the bearer token for this API,
>
> * Use the Send OTP API with scope as **create_bank_details** to trigger an OTP to the merchants registered number.
> * Verify the OTP using the Verify OTP API.
> * Use the token returned in the Verify OTP API as a bearer token of the Add or update Bank Details API.
>
> For more information, refer to [User Token APIs](ref:partner-integration-user-token-apis).

<PARTNEROnboardingEnvironment />

<details>
  <summary>Sample request</summary>

  ```curl
  curl --location -g --request POST 'https://partner.payu.in/api/v3/merchants/{{merchant_uuid}}/add_bank_detail' \
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

<details>
  <summary>Sample response</summary>

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
          "bank_name": "AXIS BANK"
      }
  }
  ```
</details>

## Request parameters