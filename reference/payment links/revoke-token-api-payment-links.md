---
title: Revoke Token API
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
The Revoke Token API (**revoke_token**) is used to revoke or delete the token generated earlier using the Get Token API. For more information, refer to [Get Access Token](ref:get-token-api-for-payment-links).

HTTP Method: **POST**

**Environment**

|                            |                                                                                              |
| -------------------------- | -------------------------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://uat-accounts.payu.in/payment-links>](https://uat-accounts.payu.in/payment-links>) |
| **Production Environment** | \<[https://accounts.payu.in/payment-links>](https://accounts.payu.in/payment-links>)         |

## Request parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameters</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>client_id<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the public identifier of the client to access the platform.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>{client\_id}</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>client_secret<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain a unique secret of the client for authorization.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>{client\_secret}</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>token</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter must contain the token that must be revoked.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>{token}</code></p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```curl
curl --location -g --request POST 'https://uat-accounts.payu.in/revoke' \
--header 'merchantId: `{merchantId}`' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer `{access_token}`'
```
