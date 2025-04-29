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
The **Get Client Token** API is used to create the token from the Hub with the scope (refer\_child\_merchant).

HTTP Method: **POST**

**Environment**

|                |                                |
| :------------- | :----------------------------- |
| **Test**       | <https://uat-accounts.payu.in> |
| **Production** | <https://accounts.payu.in>     |

Base URL: {{base\_url}}/oauth/token

## Request parameters

> 📘 Notes:
> 
> - Caller client service should be registered on Hub (PayU’s oAuth2 Service )
> - **refer_child_merchant** scope should be whitelisted on caller client on Hub
> - Get Aggregator flag enabled on parent merchant

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "client\\_id",
    "0-1": "The unique client identifier for the client.",
    "1-0": "client\\_secret",
    "1-1": "The client secret code is passed in this parameter.",
    "2-0": "grant\\_type",
    "2-1": "The client credentials is posted in this parameter.",
    "3-0": "scope",
    "3-1": "The scope is posted in this parameter. The scope can be any of the following:  \n- **refer_child_merchant:** Use this scope when you want to refer and create a child merchant  \n- **fetch_child_merchants**: Use this scope when you want to fetch the child merchants under a merchant  \n  \n**Note**: Use this API with the scope as refer_child_merchant to create client token from Hub."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    null,
    null
  ]
}
[/block]


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

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "access\\_token",
    "0-1": "This parameter contains the access token.",
    "0-2": "453226e88f0e6d1  \n8b24fe4eedb817b  \n0ff096cb740f0354  \ne4b133188555d2b151",
    "1-0": "token\\_type",
    "1-1": "This parameter contains any of the following token type:",
    "1-2": "Bearer",
    "2-0": "expires\\_in",
    "2-1": "This parameter contains the time (in seconds) at which the token shall expire from the creation time. The creation time can be found in the **created\\_at** time.",
    "2-2": "2591999",
    "3-0": "scope",
    "3-1": "This parameter contains the scope as specified in the request.",
    "3-2": "refer\\_child\\_merchant",
    "4-0": "created\\_at",
    "4-1": "This parameter contains the time stamp when the token was created.",
    "4-2": "1642509515"
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


## Sample response

The following sample response for each scenario is in JSON format:

- Create Child Merchant is Successful

```plaintext
{
    "access_token": "453226e88f0e6d18b24fe4eedb817b0ff096cb740f0354e4b133188555d2b151",
    "token_type": "Bearer",
    "expires_in": 2591999,
    "scope": "refer_child_merchant",
    "created_at": 1642509515
}
```

- When the client\_ID or secret code is unauthorised:

```plaintext
{
    "error": "invalid_client",
    "error_description": "Client authentication failed due to unknown client, no client authentication included, or unsupported authentication method."
}
```

- Incorrect scope or non-whitelisted scope

```plaintext
{
    "error": "invalid_scope",
    "error_description": "The requested scope is invalid, unknown, or malformed."
}
```