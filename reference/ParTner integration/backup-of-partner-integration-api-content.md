---
title: Backup of Partner Integration API Content
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
# Get Token API

The **Get Token** API returns the authentication token generated using the client ID and client secret.

### Environment

| Test           | [https://uat-accounts.payu.in](https://uat-accounts.payu.in) |
| :------------- | :----------------------------------------------------------- |
| **Production** | [https://accounts.payu.in](https://accounts.payu.in)         |

## Additional Information for Request Parameters

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
        For getting your client ID, refer to [Download Client Credentials](https://devguide.payu.in/docs/download-client-credentials).
      </td>
    </tr>

    <tr>
      <td>
        client\_secret
      </td>

      <td>
        For getting your client secret, refer to [Download Client Credentials](https://devguide.payu.in/docs/download-client-credentials).
      </td>
    </tr>

    <tr>
      <td>
        scope
      </td>

      <td>
        The scope varies based on the any of the use case:  

        * **Refer Merchant**: refer\_merchant.  
        * **Send Sign In OTP**: send\_sign\_in\_otp  
        * **Verify Sign In OTP**: verify\_sign\_in\_otp  
        * **Client Manage Agreement (Used in E-Sign flow)**: client\_manage\_agreement  
        * **Client Manage KYC Details (Used in managing KYC documents)**: client\_manage\_kyc\_details
      </td>
    </tr>
  </tbody>
</Table>

## Response Parameters Description

| Parameter     | Description                                              |
| :------------ | :------------------------------------------------------- |
| access\_token | The access token to be used in Partner Integration APIs. |
| token\_type   | The token type of the access token.                      |
| expires\_in   | The expiry time in seconds of the access token.          |
| scope         | The scope of the access token.                           |
| created\_at   | The UNIX time stamp when the access token was created.   |

# Send OTP API

The **Send OTP** API is used to:

* Used to send the OTP to verify the merchant’s primary details or bank update details
* Used to generate the user token required for authorization

This is authorised through a client token generated using the client ID and secret.

### Environment

| Test           | [https://uat-accounts.payu.in](https://uat-accounts.payu.in) |
| :------------- | :----------------------------------------------------------- |
| **Production** | [https://accounts.payu.in](https://accounts.payu.in)         |

# Verify OTP API

The **Verify OTP** API involves the following:

* Used to verify the OTP received on the merchant’s (users) phone number/email address through Send OTP API
* On successful OTP verification, the user token is shared in the response along with the Merchant ID (mid).
* This OTP verification will also link the merchant to your partner account with PayU incase the merchant is not referred/created by you on PayU
* This merchant linking process is ideal for platforms using only invoicing products of PayU

### Environment

| Test           | [https://uat-accounts.payu.in](https://uat-accounts.payu.in) |
| :------------- | :----------------------------------------------------------- |
| **Production** | [https://accounts.payu.in](https://accounts.payu.in)         |

# Add or Update Bank Details

This API is used to perform the following:

* Used to add or update the bank account details, only after a successful verification of merchant’s PAN card details.
* Authorized using the user token received from verify OTP API

### Environment

| Test           | [https://uat-partner.payu.in/](https://uat-partner.payu.in/) |
| :------------- | :----------------------------------------------------------- |
| **Production** | [https://partner.payu.in/](https://partner.payu.in/)         |

The access token with the **scope** as create\_bank\_details (to create bank details) or update\_bank\_details (to update bank details) using the User Token APIs is required on the header. For more information on getting the access token, refer to [User Token APIs](ref:user-token-apis).
