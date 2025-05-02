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
This API is used to generate the authentication token using the merchant's credentials like username and password. You must pass the generated token as the value of the **Authorization** header for all Payout APIs.

HTTP Method: **POST**



## Request parameters

| Parameters | Description | Example |
| ---------- | ----------- | ------- |
| client_id `mandatory` | `String` Pass the public Client ID which is same for every Payout merchant. Refer to example column for the Client ID of Production and Test environment. * **Note**: In the **Example** column, there is only one client ID. | * **Production**: ccbb70745faad9c06092bb5c79bfd919b6f45fd454f34619d83920893e90ae6b  * **Test**: 6f8bb4951e030d4d7349e64a144a534778673585f86039617c167166e9154f7e |
| grant_type `mandatory` | `String` This parameter will contain the Constant value | password |
| username `mandatory` | `String` This parameter will contain the registered mobile number or Email ID. | [payouttest5@mailinator.com](mailto:payouttest5@mailinator.com) |
| password `mandatory` | `String` This parameter will contain the registered Account password | Tester@123 |
| scope `mandatory` | `String` This parameter will contain the Constant value. | create_payout_transactions |

> 📘 Note:
>
> Use the following client_id value to proceed because the public Client ID remains the same for all Payouts Merchants:
>
> * **Test**: 6f8bb4951e030d4d7349e64a144a534778673585f86039617c167166e9154f7e
> * **Production**: ccbb70745faad9c06092bb5c79bfd919b6f45fd454f34619d83920893e90ae6b

## Sample Request

```curl
curl -X POST \
 https://uat-accounts.payu.in/oauth/token \
 -H 'cache-control: no-cache' \
 -H 'content-type: application/x-www-form-urlencoded' \
 -d 'grant_type=password&scope=create_payout_transactions&client_id=6f8bb4951e030d4d7349e64a144a534778673585f86039617c167166e9154f7e&username=payouttest4%40mailinator.com&password=Tester%40123&='
```

## Response parameters

| Key | Description |
| --- | ----------- |
| access_token | Indicates the Security Token used to get access in Payouts API calls. |
| token_type | Type of authorization token |
| expire_in | Indicates the TTL, i.e., the time limit (in seconds) after which the Security Token will expire |
| refresh_token | Used to refresh the access_token. For more information, refer to Refresh Token. |
| scope | Represents the allowed scopes in the generated security token. For example, the generated token can be used only for Payouts API requests |
| created_at | Indicates the Time of Creation in milliseconds |
| user_uuid | Indicates the Unique Identifier for the user. |

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
