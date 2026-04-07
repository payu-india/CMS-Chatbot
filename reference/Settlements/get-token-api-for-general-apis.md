---
title: Get Access Token API
excerpt: >-
  Obtain an access token using OAuth 2.0 Client Credentials flow for API
  authentication
api:
  file: PayU_OAuth2_Collection.json
  operationId: getAccessToken-1
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
The **Get Token API** returns the authentication token generated using the client ID and client secret.

### Environment

| Test           | [https://uat-accounts.payu.in](https://uat-accounts.payu.in) |
| :------------- | :----------------------------------------------------------- |
| **Production** | [https://accounts.payu.in](https://accounts.payu.in)         |

<Accordion title="Additional information for request parameters" icon="fa-info-circle">
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
          client\_id
        </td>

        <td>
          For getting your client ID, refer to [Get Client ID and Secret from Dashboard](doc:get-client-id-and-secret-from-dashboard)
        </td>
      </tr>

      <tr>
        <td>
          client\_secret
        </td>

        <td>
          For getting your client secret, refer to [Get Client ID and Secret from Dashboard](doc:get-client-id-and-secret-from-dashboard)
        </td>
      </tr>

      <tr>
        <td>
          scope
        </td>

        <td>
          The scope that must be used for payment links are:<br />

          * **Create Link**: create\_payment\_links<br />
          * **Change status and expiry**: update\_payment\_links<br />
          * **Get a single payment link**: read\_payment\_links<br />
          * **Get all payment links**: read\_payment\_links<br />
          * **Share payment links**: read\_payment\_links<br />
            **Note**: Merchant can pass up to three scopes simultaneously for an access token value. This is done by passing scopes separated by a space between them. For example:<br />
            create\_payment\_links update\_payment\_links read\_payment\_links
        </td>
      </tr>

      <tr>
        <td>
          grant\_type
        </td>

        <td>
          This parameter contains a constant value used to get the access token. The grant\_type used across the partner integration is **client\_credentials**.
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

<Accordion title="Response parameters" icon="fa-download">
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
</Accordion>

<Accordion title="Sample request" icon="fa-info-circle">
  ```curl
  curl --location -g --request POST '{{hub_base_url}}/oauth/token' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'client_id={{client_id}}' \
  --data-urlencode 'client_secret={{client_secret}}' \
  --data-urlencode 'grant_type=client_credentials' \
  --data-urlencode 'scope=read_payment_links'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-info-circle">
  ### Success scenario

  ```json
  {
  "access_token": "ea4ed864b4d2a04b90c1e987a5d25a5da1d43fa5f7d123be6814a1e973f196c4",
  "token_type": "Bearer",
  "expires_in": 7011,
  "scope": "create_payment_links",
  "created_at": 1763036368
  }
  ```

  ### Failure scenarios

  * **Client authentication failed**

  ```json
  {
  "error": "invalid_client",
  "error_description": "Client authentication failed due to unknown client, no client authentication included, or unsupported authentication method."
  }
  ```

  * **Invalid Scope**

  ```json
  {
  "error": "invalid_scope",
  "error_description": "The requested scope is invalid, unknown, or malformed."
  }
  ```

  * **Unauthorised client**
  ```json
  {
  "error": "unauthorized_client",
  "error_description": "The authenticated client is not authorized to use this authorization grant type."
  }
  ```
  * **Rate limit exceeded** 
  ```json
{
  "error": "rate_limit_exceeded",
  "error_description": "Too many requests. Please retry after some time.",
  "retry_after": 60
}
```
 *  **Server error**
  ```json
{
  "error": "server_error",
  "error_description": "The authorization server encountered an unexpected condition that prevented it from fulfilling the request."
}
  ```
</Accordion>

## Request parameters