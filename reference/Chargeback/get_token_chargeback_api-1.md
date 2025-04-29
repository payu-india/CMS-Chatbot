---
title: Get Token API - Chargeback
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Get Token** API authenticates a merchant user with email and password, and returns a access token if credentials are correct.

HTTP Method: **GET**

<ChargebackEnvironment />

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "email  \n**mandatory**",
    "0-1": "The parameter must contain the email registered with PayU.",
    "0-2": "[user@example.com](mailto:user@example.com) ",
    "1-0": "password  \n**mandatory**",
    "1-1": "The parameter must contain the password provided by PayU.",
    "1-2": "Test@1234",
    "2-0": "refresh_token  \n**optional**",
    "2-1": "This parameter must contain the flag for refreshing the token. It can contain any of the following;  \n  \n- **1** is passed so that old token will expire and new token with 1 week validity will be shared.\n- **0** is the default value and old token will not expire.",
    "2-2": "1"
  },
  "cols": 3,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Sample request

### Without refresh_token

```
curl --location --request POST 'localhost:3000/api_auth' \
--header 'X-User-Email: mohammad.farhan@payu.in' \
--header 'X-User-Password: Payu@1234' \
--header 'Cookie: BetterErrors-2.9.1-CSRF-Token=dcf11311-df3c-40f9-924b-44ef7aab0aa4; __profilin=p%3Dt; _bank_portal_session=65cd749b113f80ae6bbc3b2dc405068c'
```

### With refresh_token=1

```
curl --location --request POST 'localhost:3000/api_auth?refresh_token=1' \
--header 'X-User-Email: mohammad.farhan@payu.in' \
--header 'X-User-Password: Payu@1234' \
--header 'Cookie: BetterErrors-2.9.1-CSRF-Token=dcf11311-df3c-40f9-924b-44ef7aab0aa4; __profilin=p%3Dt; _bank_portal_session=65cd749b113f80ae6bbc3b2dc405068c''
```

## Sample response

### Success scenario

- Without refresh_token

```
{
    "status": 200,
    "message": "Success",
    "token": "0ec164a4_1884_4c63_ba0b_87e5545c0e3e",
    "expires_at": "2024-06-28 17:37:31",
    "organization": {
        "id": 17909,
        "name": "Root",
        "uuid": "root",
        "description": "Root",
        "created_by_id": null,
        "updated_by_id": null,
        "created_at": "2017-04-06T19:18:11.000+05:30",
        "updated_at": "2017-04-06T19:18:11.000+05:30",
        "ancestry": null,
        "payubiz_id": null,
        "hide_name": false,
        "url": null,
        "product": "na",
        "header_mappings": null
    }
}
```

- With refresh_token=1

```
{
    "status": 200,
    "message": "Success",
    "token": "76bb2a3b_5595_47bb_a239_da2b37af780b",
    "expires_at": "2024-06-28 17:53:50",
    "organization": {
        "id": 17909,
        "name": "Root",
        "uuid": "root",
        "description": "Root",
        "created_by_id": null,
        "updated_by_id": null,
        "created_at": "2017-04-06T19:18:11.000+05:30",
        "updated_at": "2017-04-06T19:18:11.000+05:30",
        "ancestry": null,
        "payubiz_id": null,
        "hide_name": false,
        "url": null,
        "product": "na",
        "header_mappings": null
    }
}
```

<br />

### Failure scenario

- Unauthorized (401)

```
{
    "error": "Invalid email or password"
}
```