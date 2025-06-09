---
title: Bank Verification API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Bank Verification API
  description: >-
    The Bank Verification API allows for the verification of bank accounts using
    a penny drop or penniless transaction, requiring an access token with
    specific scopes and client credentials for authentication.
  robots: index
next:
  description: ''
---
The **Bank Verification** API is used to verify bank account using penny drop/penniless transaction.

## Environment

| Environment            | URL                                                                                                                                |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Production Environment | \[[https://onboarding.payu.in/dvs/bank\_accounts/acc\_verification](https://onboarding.payu.in/dvs/bank_accounts/acc_verification) |

> 📘 **Note:**
>
> The access token with the scope as **verify\_bank\_account** and grant type as **client\_credentials** are required on the header. For more information on getting the access token, refer to [Get Token API - Bank Verification](ref:gettoken-bank-verification).

## Request parameters

### Header

| Parameter                                | Description                                                                                                                                                                                                                                                        |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Bearer token<br /><code>mandatory</code> | The access token with the scope as **verify\_bank\_account** and grant type as **client\_credentials** are required on the header. For more information on getting the access token, refer to [Get Token API - Bank Verification](ref:gettoken-bank-verification). |

### Body

| Parameter                                        | Description                                                                                                                                     |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| account\_number<br /><code>mandatory</code>      | <code>String</code> This parameter must contain the account number to be verified.                                                              |
| ifsc<br /><code>mandatory</code>                 | <code>String</code> This parameter must contain the bank IFSC code.                                                                             |
| name<br /><code>mandatory</code>                 | <code>String</code> This parameter must contain the account holder name.                                                                        |
| name\_match\_required<br /><code>optional</code> | <code>Boolean</code> This parameter must be set to <code>true</code> if the name must match along with bank account verification.               |
| leniency<br /><code>optional</code>              | <code>String</code> If name\_match\_required is set to <code>true</code>, this parameter must contain any of the following:- Medium - High - Lo |

## Sample request

```bash
curl --location 'https://uat-onepayuonboarding.payu.in/dvs/bank_accounts/acc_verification' \
--header 'clientId: <client Id>' \
--header 'Content-Type: application/json' \
--header 'Authorization: ••••••' \
--header 'Cookie: Path=/' \
--data '{
"account_number": "0514100000****",
"ifsc": "HDFC0000514",
"name" : "R******* P"
}
'
```

## Response parameters

| Parameter         | Description                                                                                                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| payuRequestId     | This parameter returns the PayU request ID.                                                                                                                                                 |
| result            | This parameter returns the results of the verification in a JSON format. For more information, refer to <a href="#result-json-fields-description">result JSON fields description</a> table. |
| requestAttributes | This parameter contains the following details posted in the request in a JSON format: - name - ifsc - accountNumber                                                                         |

### result JSON fields description

| Field         | Description                                                          | Example                |
| :------------ | :------------------------------------------------------------------- | :--------------------- |
| accountName   | The masked name of the account holder for privacy.                   | Ashish                 |
| bankResponse  | The response message from the bank regarding the transaction status. | Transaction successful |
| bankTxnStatus | A boolean value indicating if the bank transaction was successful.   | true                   |
| accountStatus | The current status of the account.                                   | ACTIVE                 |

## Sample response

### Success scenario

```json
{
  "payuRequestId": "ba659237-34de-4805-a5cf-ef9dd7a1cda2",
  "result": {
    "accountName": "P R*******",
    "bankResponse": "Transaction successful",
    "bankTxnStatus": "true",
    "accountStatus": "ACTIVE"
  },
  "requestAttributes": {
    "name": "R******* P",
    "ifsc": "HDFC0000514",
    "accountNumber": "0514100000****"
  }
}
```

### Failure scenario

* Missing client\_id value in header

```json
{
  "error": "Missing required client_id header"
}
```

* Invalid account number

```json
{
  "payuRequestId": "0aeb7a65-cea3-4e81-9355-38548bb8f795",
  "error": {
    "reason": "Invalid account number or IFSC provided"
  },
  "requestAttributes": {
    "name": "test",
    "ifsc": "HDFC0000514",
    "accountNumber": "0514100000***",
    "verficationMode": 1
  }
}
```