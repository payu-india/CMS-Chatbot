---
title: Get Client Token API
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
The **Get Client Token** API is used to create the token from the Hub with the scope (refer_child_merchant).

HTTP Method: **POST**

**Environment**

|                |                                                                  |
| :------------- | :--------------------------------------------------------------- |
| **Test**       | \<[https://uat-accounts.payu.in>](https://uat-accounts.payu.in>) |
| **Production** | \<[https://accounts.payu.in>](https://accounts.payu.in>)         |

Base URL: `{{base_url}}/oauth/token`

## Request parameters

<Callout icon="📘" theme="info">
  **Notes**:

  * Caller client service should be registered on Hub (PayU’s oAuth2 Service )
  * **refer_child_merchant** scope should be whitelisted on caller client on Hub
  * Get Aggregator flag enabled on parent merchant
</Callout>

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>client_id</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The unique client identifier for the client.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>client_secret</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The client secret code is passed in this parameter.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>grant_type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The client credentials is posted in this parameter.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>scope</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The scope is posted in this parameter. The scope can be any of the following:  </p>
<ul>
<li><strong>refer_child_merchant:</strong> Use this scope when you want to refer and create a child merchant  </li>
<li><strong>fetch_child_merchants</strong>: Use this scope when you want to fetch the child merchants under a merchant</li>
</ul>
<p><strong>Note</strong>: Use this API with the scope as refer_child_merchant to create client token from Hub.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```curl
curl --location -g --request POST '{{hub_base_url}}/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id={{client_id}}' \
--data-urlencode 'client_secret={{client_secret}}' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'scope=refer_child_merchant'
```

## Response parameters

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>access_token</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the access token.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>453226e88f0e6d1<br>8b24fe4eedb817b<br>0ff096cb740f0354<br>e4b133188555d2b151</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>token_type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains any of the following token type:</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Bearer</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>expires_in</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the time (in seconds) at which the token shall expire from the creation time. The creation time can be found in the <strong>created_at</strong> time.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2591999</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>scope</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the scope as specified in the request.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>refer_child_merchant</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>created_at</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the time stamp when the token was created.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1642509515</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample response

The following sample response for each scenario is in JSON format:

* Create Child Merchant is Successful

```plaintext
{
    "access_token": "453226e88f0e6d18b24fe4eedb817b0ff096cb740f0354e4b133188555d2b151",
    "token_type": "Bearer",
    "expires_in": 2591999,
    "scope": "refer_child_merchant",
    "created_at": 1642509515
}
```

* When the client_ID or secret code is unauthorised:

```plaintext
{
    "error": "invalid_client",
    "error_description": "Client authentication failed due to unknown client, no client authentication included, or unsupported authentication method."
}
```

* Incorrect scope or non-whitelisted scope

```plaintext
{
    "error": "invalid_scope",
    "error_description": "The requested scope is invalid, unknown, or malformed."
}
```
