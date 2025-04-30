---
title: Get Token API - Bank Verification
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
# Get Token API

This **Get Token API** returns the authentication token generated using the client ID and client secret where, `grant_type` is **client_credentials** and `scope` is **verify_bank_account**.

## Environment

<Table>
  <thead>
    <tr>
      <th>Environment</th>
      <th>URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Production</td>
      <td>https://accounts.payu.in</td>
    </tr>
  </tbody>
</Table>

## Request parameters

<Table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>client_id<br/><code>mandatory</code></td>
      <td>String: This field is the Client ID that was provided by PayU while onboarding.</td>
    </tr>
    <tr>
      <td>client_secret<br/><code>mandatory</code></td>
      <td>String: This field is the Client secret that was provided by PayU while onboarding.</td>
    </tr>
    <tr>
      <td>grant_type<br/><code>mandatory</code></td>
      <td>String: This parameter contains a constant value used to get the access token. For Bank Verification API, it is <code>client_credentials</code>.</td>
    </tr>
    <tr>
      <td>scope<br/><code>mandatory</code></td>
      <td>String: This parameter will vary based on the use case. For Bank Verification API, it is <code>verify_bank_account</code>.</td>
    </tr>
  </tbody>
</Table>

## Sample request

```bash
curl --request POST \
     --url https://uat-accounts.payu.in/oauth/token \
     --header 'accept: application/json' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --data grant_type=client_credentials \
     --data scope=verify_bank_account \
     --data 'client_id=<client_id>' \
     --data 'client_secret=<client_secret>'
```

## Response parameters

<Table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>access_token</td>
      <td>The access token to be used in Partner Integration APIs.</td>
    </tr>
    <tr>
      <td>token_type</td>
      <td>The token type of the access token.</td>
    </tr>
    <tr>
      <td>expires_in</td>
      <td>The expiry time in seconds of the access token.</td>
    </tr>
    <tr>
      <td>scope</td>
      <td>The scope of the access token.</td>
    </tr>
    <tr>
      <td>created_at</td>
      <td>The UNIX time stamp when the access token was created.</td>
    </tr>
  </tbody>
</Table>

> 📘 **Note:**
> 
> The expiry period of the token generated using this API is configurable by you (partner). The expiry period (in seconds) of the token is displayed in the **expires_in** parameter of the response. For example, in the following response, the value of the **expires_in** is 7200 seconds:
> 
> ```json
> {
>   "access_token": "82c38b64e072f3d64da6e4e6efee9789ffe1250f0cd04c20753d6e6f25df9cc7",
>   "token_type": "Bearer",
>   "expires_in": 7200,
>   "scope": "send_sign_in_otp",
>   "created_at": 1595411399
> }
> ```

## Sample response

```json
{
  "access_token": "82c38b64e072f3d64da6e4e6efee9789ffe1250f0cd04c20753d6e6f25df9cc7",
  "token_type": "Bearer",
  "expires_in": 7200,
  "scope": "send_sign_in_otp",
  "created_at": 1595411399
}
```