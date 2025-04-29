---
title: Generate Token using Merchant's Credentials API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to generate the authentication token using the merchant's credentials like username and password. You must pass the generated token as the value of the **Authorization** header for all Payout APIs.

HTTP Method: **POST**

<PAYOUTSEnvironment />

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameters**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "client\\_id  \n`mandatory`",
    "0-1": "`String`Pass the public Client ID which is same for every Payout merchant. Refer to example column for the Client ID of Production and Test environment.  \n**Note**: In the **Example** column, there is only one client ID.",
    "0-2": "**Production**: ccbb70745faad9c06092bb5c79bfd919b6f45fd45  \n4f34619d83920893e90ae6b  \n**Test**:6f8bb4951e030d4d7349e64a144a53477  \n8673585f86039617c167166e9154f7e",
    "1-0": "grant\\_type  \n`mandatory`",
    "1-1": "`String`This parameter will contain the Constant value",
    "1-2": "password",
    "2-0": "username  \n`mandatory`",
    "2-1": "`String`This parameter will contain the registered mobile number or Email ID.",
    "2-2": "[payouttest5@mailinator.com](mailto:payouttest5@mailinator.com)",
    "3-0": "password  \n`mandatory`",
    "3-1": "`String`This parameter will contain the registered Account password",
    "3-2": "Tester@123",
    "4-0": "scope  \n`mandatory`",
    "4-1": "`String`This parameter will contain the Constant value.",
    "4-2": "create\\_payout\\_transactions"
  },
  "cols": 3,
  "rows": 5,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


> 📘 Note:
> 
> Use the following client\_id value to proceed because the public Client ID remains the same for all Payouts Merchants:
> 
> - **Test**:6f8bb4951e030d4d7349e64a144a534778673585f86039617c167166e9154f7e
> - **Production**: ccbb70745faad9c06092bb5c79bfd919b6f45fd45  
>   4f34619d83920893e90ae6b

## Sample Request

```curl
curl -X POST \
 https://uat-accounts.payu.in/oauth/token \
 -H 'cache-control: no-cache' \
 -H 'content-type: application/x-www-form-urlencoded' \
 -d 'grant_type=password&scope=create_payout_transactions&client_id=6f8bb4951e030d4d7349e64a144a534778673585f86039617c167166e9154f7e&username=payouttest4%40mailinator.com&password=Tester%40123&='
```

## Response parameters

| **Key**        | **Description**                                                                                                                           |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| access\_token  | Indicates the Security Token used to get access in Payouts API calls.                                                                     |
| token\_type    | Type of authorization token                                                                                                               |
| expire\_in     | Indicates the TTL, i.e., the time limit (in seconds) after which the Security Token will expire                                           |
| refresh\_token | Used to refresh the access\_token. For more information, refer to Refresh Token.                                                          |
| scope          | Represents the allowed scopes in the generated security token. For example, the generated token can be used only for Payouts API requests |
| created\_at    | Indicates the Time of Creation in milliseconds                                                                                            |
| user\_uuid     | Indicates the Unique Identifier for the user.                                                                                             |

## Sample response

```
{
 "access_token": "581b0657b38a56bb4296f774852f208f6d84a23d8f1bf61c63c15de60d43ee76",
 "token_type": "Bearer",
 "expires_in": 7199,
 "refresh_token": "ff8e094ecfa11fb390931f779ae62c0836f97bbaedcf5551c88eff826da3239a",
 "scope": "create_payout_transactions",
 "created_at": 1585216027,
 "user_uuid": "11e8-5a8f-05faaaa4-84a5-020d245326e4"
}
```