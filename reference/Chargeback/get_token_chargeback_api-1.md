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

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        email
        **mandatory**
      </td>

      <td>
        The parameter must contain the email registered with PayU.
      </td>

      <td>
        [user@example.com](mailto:user@example.com) 
      </td>
    </tr>

    <tr>
      <td>
        password\
        **mandatory**
      </td>

      <td>
        The parameter must contain the password provided by PayU.
      </td>

      <td>
        Test\@1234
      </td>
    </tr>

    <tr>
      <td>
        refresh\_token\
        **optional**
      </td>

      <td>
        This parameter must contain the flag for refreshing the token. It can contain any of the following;  

        * **1** is passed so that old token will expire and new token with 1 week validity will be shared.
        * **0** is the default value and old token will not expire.
      </td>

      <td>
        1
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

### Without refresh\_token

```
curl --location --request POST 'localhost:3000/api_auth' \
--header 'X-User-Email: mohammad.farhan@payu.in' \
--header 'X-User-Password: Payu@1234' \
--header 'Cookie: BetterErrors-2.9.1-CSRF-Token=dcf11311-df3c-40f9-924b-44ef7aab0aa4; __profilin=p%3Dt; _bank_portal_session=65cd749b113f80ae6bbc3b2dc405068c'
```

### With refresh\_token=1

```
curl --location --request POST 'localhost:3000/api_auth?refresh_token=1' \
--header 'X-User-Email: mohammad.farhan@payu.in' \
--header 'X-User-Password: Payu@1234' \
--header 'Cookie: BetterErrors-2.9.1-CSRF-Token=dcf11311-df3c-40f9-924b-44ef7aab0aa4; __profilin=p%3Dt; _bank_portal_session=65cd749b113f80ae6bbc3b2dc405068c''
```

## Sample response

### Success scenario

* Without refresh\_token

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

* With refresh\_token=1

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

* Unauthorized (401)

```
{
    "error": "Invalid email or password"
}
```
