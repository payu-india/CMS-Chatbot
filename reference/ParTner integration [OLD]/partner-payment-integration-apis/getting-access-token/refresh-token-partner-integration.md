---
title: Refresh Token API - Partner Integration
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
This API is used to generate a refresh token to obtain a renewed access token using client ID.

<Callout icon="📘" theme="info">
  **Note**: You can use this API when the token generated using the** Get Token **API has expired. The expiry period of the token generated using this API is configurable by you (partner). The expiry period (in seconds) of the token is displayed in the **expires_in** parameter of the response.
</Callout>

**Environment**

|                |                                                                  |
| :------------- | :--------------------------------------------------------------- |
| **Test**       | \<[https://uat-accounts.payu.in>](https://uat-accounts.payu.in>) |
| **Production** | \<[https://accounts.payu.in>](https://accounts.payu.in>)         |

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>client_ID<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter will contain the public Client ID.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>6f8bb4951e030d4d7349e64a144a53477 8673585f86039617c167166e9154f7e</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>client_secret<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter will contain the client secret.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>grant_type<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter will contain the value as <strong>refresh_token</strong>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>refresh_token</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>refresh_token<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Indicates the refresh token. This is the token that was generated using the  <a href="http://docs.payu.in/reference/getting-access-token">Get Access Token - WhatsApp</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```curl
curl --location -g --request POST 'https://uat-accounts.payu.in/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id={{client_id}}' \
--data-urlencode 'client_secret={{client_secret}}' \
--data-urlencode 'grant_type=refresh_token' \
--data-urlencode 'refresh_token={{refresh_token}}'
```

## Response parameters

<PartnerAuthenticationResponseParameters />

## Sample response

### Successful transaction

Success

```plaintext
{
  "access_token": "8703474d8779483d9a298666faafa1ee5c1fc24c71dc1890dc7484e19cf27c9e",
  "token_type": "Bearer",
  "expires_in": 7199,
  "refresh_token": "249fbf69a7841aa28cc494984b45efcb22537c0cedbb672c6fa18ba8eb21d8ce",
  "scope": "hub_session",
  "created_at": 1553511296,
  "user_uuid": "11e7-a7f6-f0494f6c-bbb7-4a020b6b2b14"
}
```

### Failure scenarios

<RefreshTokenSampleResponse />