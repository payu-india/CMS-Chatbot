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

**Environment**

|                            |                                                                        |
| :------------------------- | :--------------------------------------------------------------------- |
| **Production Environment** | <https://onepayuonboarding.payu.in/dvs/bank_accounts/acc_verification> |

> 📘 Note:
> 
> The access token with the scope as **verify_bank_account ** and grant type as **client_credentials** are required on the header. For more information on getting the access token, refer to [Get Token API - Bank Verification](ref:gettoken-bank-verification).

## Request parameters

### Header

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "Bearer token  \n`mandatory`",
    "0-1": "The access token with the scope as **verify_bank_account ** and grant type as **client_credentials** are required on the header. For more information on getting the access token, refer to [Get Token API - Bank Verification](ref:gettoken-bank-verification) .",
    "1-0": "",
    "1-1": ""
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]


### Body

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "account_number  \n`mandatory`",
    "0-1": "`String `This parameter must contain the account number to be verified.",
    "1-0": "ifsc  \n`mandatory`",
    "1-1": "`String` This parameter must contain the bank IFSC code.",
    "2-0": "name  \n`mandatory`",
    "2-1": "`String` This parameter must contain the account holder name.",
    "3-0": "name_match_required  \n`optional`",
    "3-1": "`Boolean` This parameter must be set to `true` if the name must match along with bank account verification.",
    "4-0": "leniency  \n`optional`",
    "4-1": "`String` If name_match_required is set to `true`, this parameter must contain any of the following:  \n  \n- Medium\n- High\n- Lo"
  },
  "cols": 2,
  "rows": 5,
  "align": [
    null,
    null
  ]
}
[/block]


## Sample request

```
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

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "payuRequestId",
    "0-1": "This parameter returns the PayU request ID.",
    "1-0": "result",
    "1-1": "This parameter returns the results of the verification in a JSON format. For more information, refer to[ result JSON fields description](#result-json-fields-description) table.",
    "2-0": "requestAttributes",
    "2-1": "This parameter contains the following details posted in the request in a JSON format:  \n  \n- name\n- ifsc\n- accountNumber"
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


### result JSON fields description

| Field         | Description                                                          | Example                |
| ------------- | -------------------------------------------------------------------- | ---------------------- |
| accountName   | The masked name of the account holder for privacy.                   | Ashish                 |
| bankResponse  | The response message from the bank regarding the transaction status. | Transaction successful |
| bankTxnStatus | A boolean value indicating if the bank transaction was successful.   | true                   |
| accountStatus | The current status of the account.                                   | ACTIVE                 |

## Sample response

#### Success scenario

```
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

#### Failure scenario

- Missing client_id value in header

```
{
  "error": "Missing required client_id header"
}
```

- Invalid account number

```
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

</details>