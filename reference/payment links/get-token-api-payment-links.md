---
title: Get Token API - Payment Links
excerpt: ''
api:
  file: payout-for-merchants-40.json
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
        client_id
      </td>

      <td>
        For getting your client ID, refer to [Get Client ID and Secret from Dashboard](doc:get-client-id-and-secret-from-dashboard)
      </td>
    </tr>

    <tr>
      <td>
        client_secret
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

        * **Create Link**: create_payment_links<br />
        * **Change status and expiry**: update_payment_links<br />
        * **Get a single payment link**: read_payment_links<br />
        * **Get all payment links**: read_payment_links<br />
        * **Share payment links**: read_payment_links<br />
          **Note**: Merchant can pass up to three scopes simultaneously for an access token value. This is done by passing scopes separated by a space between them. For example:<br />
          create_payment_links update_payment_links read_payment_links
      </td>
    </tr>

    <tr>
      <td>
        grant_type
      </td>

      <td>
        This parameter contains a constant value used to get the access token. The grant_type used across the partner integration is **client_credentials**.
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

## Request parameters
