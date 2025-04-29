---
title: Get Token API - Partner Integration
excerpt: ''
api:
  file: partner-apis-16.json
  operationId: get_token
deprecated: false
hidden: false
metadata:
  title: Get Token API - Partner Integration
  description: >-
    The Get Token API generates an authentication token for Payment Link API
    Integration and Partner Integration API Integration, using client ID and
    client secret. The token has configurable expiry time and various scopes for
    different functionalities.
  keywords:
    - Get Token API for Partner Integration
    - ' Get Token API for Payment Links'
    - Get Token API for Partner Integration
    - Get Token API for Partner Onboarding
    - Get Token API for refer_merchant scope
    - ' Get Token API for send_sign_in_otp scope'
    - Get Token API for verify_sign_in_otp
    - Get Token API for client_manage_agreement scope
    - Get Token API for client_manage_kyc_details
    - Get Token API for create_bank_details
    - Get Token API for user_token scope
    - Get Token API for create_payment_links
  robots: index
next:
  description: ''
---
The **Get Token API** returns the authentication token generated using the client ID and client secret for the following products: 

* [Payment Link API Integration](doc:integration-api-for-payment-links)
* [Partner Integration API Integration](doc:refer-merchants)

### Environment

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
        client\_id
      </td>
      <td>
        For getting your client ID, refer to [Download Client Credentials](doc:download-client-credentials).
      </td>
    </tr>
    <tr>
      <td>
        client\_secret
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
        The scopes to be used for various use cases in Parter Integration are:  
        * Refer Merchant, Verify Link Merchant, Get Merchant, and Update Merchant: **refer\_merchant**
        * Send Sign In OTP: **send\_sign\_in\_otp**
        * Verify Sign In OTP: **verify\_sign\_in\_otp**
        * Client Manage Agreement (Used in E-Sign flow): **client\_manage\_agreement**
        * Client Manage KYC Details (Used in managing KYC documents): **client\_manage\_kyc\_details**
        * Create Bank Details: **create\_bank\_details**
        * Penny Verify - **user\_token**
        * Manage Payment Links: **create\_payment\_links**
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

<details>
  <summary>Response parameters</summary>
  <table>
    <thead>
      <tr>
        <th>Parameter</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>access\_token</td>
        <td>The access token to be used in Partner Integration APIs.</td>
      </tr>
      <tr>
        <td>token\_type</td>
        <td>The token type of the access token.</td>
      </tr>
      <tr>
        <td>expires\_in</td>
        <td>The expiry time in seconds of the access token.</td>
      </tr>
      <tr>
        <td>scope</td>
        <td>The scope of the access token.</td>
      </tr>
      <tr>
        <td>created\_at</td>
        <td>The UNIX time stamp when the access token was created.</td>
      </tr>
    </tbody>
  </table>
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