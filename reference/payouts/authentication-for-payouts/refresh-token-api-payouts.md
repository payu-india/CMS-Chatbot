---
title: Refresh Token API - Payouts
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
This API used to refresh the validity of token which is already generated

HTTP Method: **POST**

**Environment**  

|                            |                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------- |
| **Test Environment**       | [https\://uat-accounts.payu.in/oauth/token](https://uat-accounts.payu.in/oauth/token) |
| **Production Environment** | [https\://accounts.payu.in/oauth/token](https://accounts.payu.in/oauth/token)         |

## Request parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>client_id<code> mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter will contain the public Client ID which is identical for and used by all Payouts Merchants. For getting your client_id , refer to <a href="doc:get-client-id-and-secret-from-dashboard">Get Client ID and Secret from Dashboard</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>grant_type<code> mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter will contain the grant type and for this API, it is <strong>refresn_token</strong>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>refresh_token</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>refresh_token<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Refresh Token received in Authentication Token Generation APIs.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```curl
curl -X POST \
 https://uat-accounts.payu.in/oauth/token \
 -H 'cache-control: no-cache' \
 -H 'content-type: application/x-www-form-urlencoded' \
 -d 'grant_type=refresh_token&client_id=6f8bb4951e030d4d7349e64a144a534778673585f86039617c167166e9154f7e&refresh_token=ff8e094ecfa11fb390931f779ae62c0836f97bbaedcf5551c88eff826da3239a'
```

## Response parameters

| **Parameters** | **Description**                                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| access\_token  | Indicates the Security Token used to get access in Payouts API calls.                                                              |
| token\_type    | Type of authorization token                                                                                                        |
| expire\_in     | Indicates the TTL i.e., the time limit (in seconds) after which the Security Token will expire                                     |
| refresh\_token | Used to refresh the access\_token. To know more, read Refresh Token section                                                        |
| scope          | Represents the allowed scopes in generated security token. For e.g., the generated token can be used only for Payouts API requests |
| created\_at    | Indicates the Time of Creation in milliseconds                                                                                     |
| user\_uuid     | Indicates the Unique Identifier for the user.                                                                                      |

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