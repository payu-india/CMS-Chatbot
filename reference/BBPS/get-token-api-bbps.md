---
title: Get Token API - BBPS
excerpt: ''
api:
  file: payout-for-merchants-41.json
  operationId: GenerateTokenusingMerchant'sCredentialsAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Get Token API** returns the authentication token generated using the client ID and client secret.

#### Environment

| Test           | [https://uat-accounts.payu.in](https://uat-accounts.payu.in) |
| :------------- | :----------------------------------------------------------- |
| **Production** | [https://accounts.payu.in](https://accounts.payu.in)         |

## Additional information for request parameters

<Table>
  <thead>
    <tr>
      <th>
        Parameters
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        client_id
      </td>

      <td>
        For getting your client ID, refer to [Download Client Credentials](doc:download-client-credentials).
      </td>
    </tr>

    <tr>
      <td>
        client_secret
      </td>

      <td>
        For getting your client secret, refer to [Download Client Credentials](doc:download-client-credentials).
      </td>
    </tr>

    <tr>
      <td>
        scope
      </td>

      <td>
        The scopes used in BBPS are:

        * read_bills
        * create_transactions
        * read_billers
        * read_biller_categories
        * read_transactions
        * read_plans  
          The scope varies for each BBPS API and refer the first "Note" of the API reference for the scope.
      </td>
    </tr>

    <tr>
      <td>
        grant_type
      </td>

      <td>
        This parameter contains a constant value used to get the access token. The grant_type used across the BBPS will be share by PayU.
      </td>
    </tr>
  </tbody>
</Table>

<details>
  <summary>Response parameters</summary>

  | Parameter     | Description                                              |
  | :------------ | :------------------------------------------------------- |
  | access\_token | The access token to be used in Partner Integration APIs. |
  | token\_type   | The token type of the access token.                      |
  | expires\_in   | The expiry time in seconds of the access token.          |
  | scope         | The scope of the access token.                           |
  | created\_at   | The UNIX time stamp when the access token was created.   |

  > 📘 Note:
  >
  > The expiry period of the token generated using this API is configurable by you (partner). The expiry period (in seconds) of the token is displayed in the **expires\_in** parameter of the response. For example, in the following response, the value of the **expires\_in** is 7200 seconds:
  >
  > ```
  > {
  >   "access_token": "82c38b64e072f3d64da6e4e6efee9789ffe1250f0cd04c20753d6e6f25df9cc7",
  >   "token_type": "Bearer",
  >   "expires_in": 7200,
  >   "scope": "send_sign_in_otp",
  >   "created_at": 1595411399
  > }
  > ```
</details>

## Request parameters
