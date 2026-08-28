---
title: Quick Start Partner Integration - OAuth Flow
deprecated: false
hidden: true
metadata:
  title: Quick Start Partner Integration - OAuth Flow
  robots: index
---
Onboard a merchant using Co-Branded OAuth flow with a few API calls. The Co-Branded OAuth onboarding flow allows partners to onboard merchants seamlessly using OAuth 2.0 authorization. This approach provides a branded experience where merchants authenticate directly with PayU, and partners receive the merchant credentials securely.

## Prerequisites

Before you begin, ensure you have:

- **Partner credentials**: Client ID and Client Secret.  For more information, refer to [Get Client ID and Secret from Dashboard.](doc:get-client-id-and-secret-from-dashboard)
- **Whitelisted redirect URL**: Your callback URL registered with PayU
- **OAuth scope enabled**: Contact your Key Account Manager (KAM) to enable OAuth onboarding

***

## Integration Flow

```mermaid
flowchart TD
    A[Start: Partner obtains <br> Client ID & Secret] --> B[Redirect merchant to <br> PayU Authorization Page]
    B --> C[Merchant logs in <br> & <br> grants consent]
    C --> D[PayU redirects to Partner <br> with auth_code]
    D --> E[Partner validates <br> auth_code]
    E --> F[Receive merchant <br> key & salt]
    F --> G[Merchant can now <br> collect payments]
    
    style A fill:#e1f5ff
    style G fill:#d4edda
```

## Steps to Integrate

<Cards columns={3}>
  <Card title="1. Build the Authorization URL" href="https://docs.payu.in/docs/refer-merchants-using-co-branded-oauth-onboarding#step-1-build-the-authorization-url">
    Construct the OAuth authorization URL with client_id and encoded redirect_url to send merchants to PayU

    <br />
  </Card>

  <Card title="2. Redirect Merchant to Authorization Page" href="https://docs.payu.in/docs/refer-merchants-using-co-branded-oauth-onboarding#step-2-redirect-merchant-to-authorization-page">
    Redirect the merchant to PayU where they log in, complete KYC, and grant consent

    <br />
  </Card>

  <Card title="3. Receive Authorization Code" href="https://docs.payu.in/docs/refer-merchants-using-co-branded-oauth-onboarding#step-3-receive-authorization-code">
    Receive a single-use auth_code on your redirect_url after merchant authorization

    <br />
  </Card>

  <Card title="4. Validate Authorization Code" href="https://docs.payu.in/docs/refer-merchants-using-co-branded-oauth-onboarding#step-4-validate-authorization-code">
    POST the auth_code with client credentials to the Validate Auth Code API to obtain merchant_key and salt

    <br />
  </Card>

  <Card title="5. Store Merchant Credentials Securely" href="https://docs.payu.in/docs/refer-merchants-using-co-branded-oauth-onboarding#step-5-store-merchant-credentials-securely">
    Persist merchant_key and salt securely on your server and never expose them client-side

    <br />
  </Card>

  <Card title="6. Retrieve Merchant Credentials Later" href="https://docs.payu.in/docs/refer-merchants-using-co-branded-oauth-onboarding#step-6-optional-retrieve-merchant-credentials-later">
    Use the Get Merchant Credentials API to fetch merchant_key and salt if needed later

    <br />
  </Card>

  <Card title="7. Collect Payments" href="https://docs.payu.in/docs/refer-merchants-using-co-branded-oauth-onboarding#step-7-collect-payments">
    Use the obtained merchant credentials to integrate payment flows via Hosted Checkout, Pre-Built Checkout, or UPI S2S
  </Card>

  <br />
</Cards>

<br />

### Step 1: Build the Authorization URL

Construct the authorization URL to redirect merchants to the PayU login page.

**URL Format:**

| Environment    | URL                                                                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------- |
| **Test**       | `https://onboardingtest.payu.in/merchant/partner-oauth?client_id={{client_id}}&redirect_url={{redirect_url}}` |
| **Production** | `https://onboarding.payu.in/merchant/partner-oauth?client_id={{client_id}}&redirect_url={{redirect_url}}`     |

**Required Parameters:**

- `client_id`: Your partner client ID
- `redirect_url`: Your whitelisted callback URL (must be URL-encoded)

<Accordion title="Sample Authorization URL" icon="fa-code">
  ```
  https://onboardingtest.payu.in/merchant/partner-oauth?client_id=ABC123&redirect_url=https%3A%2F%2Fpartner.example.com%2Fcallback
  ```
</Accordion>

***

### Step 2: Redirect Merchant to Authorization Page

Redirect the merchant to the authorization URL constructed in Step 1. The merchant will:

1. Log in to PayU (or create a new account).
2. Complete KYC if not already done.
3. Grant authorization to your partner application.

For detailed steps, refer to [Activate Account.](doc:complete-your-kyc)

***

### Step 3: Receive Authorization Code

After successful authorization, PayU redirects the merchant back to your `redirect_url` with an authorization code.

**Callback URL Format:**

```
{{redirect_url}}?auth_code={{authorization_code}}
```

**Example:**

```
https://partner.example.com/callback?auth_code=XYZ789ABC123
```

<Callout icon="⚠️" theme="warn">
  ### **Important**: The `auth_code` is single-use and expires after a short period. Exchange it immediately for merchant credentials.
</Callout>

***

### Step 4: Validate Authorization Code

Exchange the authorization code for merchant credentials using the **Validate Auth Code** API.

**HTTP Method:** `POST`

| Environment    | Endpoint                                                 |
| -------------- | -------------------------------------------------------- |
| **Test**       | `https://testdashboard.payu.in/oauth/validate-auth-code` |
| **Production** | `https://dashboard.payu.in/oauth/validate-auth-code`     |

​For more details, refer to[ Validate Auth Code API](/reference/validate_authcode_and_client_api)

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl --location 'https://testdashboard.payu.in/oauth/validate-auth-code' \
  --header 'Content-Type: application/json' \
  --data '{
      "client_id": "ABC123",
      "client_secret": "your_client_secret",
      "auth_code": "XYZ789ABC123"
  }'
  ```
</Accordion>

<Accordion title="Sample Response (Success)" icon="fa-shield-check">
  ```json
  {
      "status": 1,
      "msg": "Success",
      "merchant_key": "mK3j2L9p",
      "salt": "sA7x9B2c"
  }
  ```
</Accordion>

<Accordion title="Sample Response (Failure)" icon="fa-times-circle">
  ```json
  {
      "status": 0,
      "msg": "Invalid auth code"
  }
  ```
</Accordion>

**Response Parameters:**

| Parameter      | Description                                               |
| -------------- | --------------------------------------------------------- |
| `status`       | `1` for success, `0` for failure                          |
| `msg`          | Success or error message                                  |
| `merchant_key` | Merchant's API key (returned on success)                  |
| `salt`         | Merchant's salt for hash generation (returned on success) |

***

### Step 5: Store Merchant Credentials Securely

Once you receive the `merchant_key` and `salt`:

1. **Store them securely** in your database associated with the merchant.
2. **Never expose** these credentials in client-side code.
3. Use them to generate payment hashes on your server.

<Callout icon="🔒" theme="default">
  ### **Security Best Practice**: Encrypt sensitive credentials at rest and in transit.
</Callout>

***

### Step 6: Retrieve Merchant Credentials Later (Optional)

If you need to retrieve merchant credentials at a later time, use the **Get Merchant Credentials** API.

**HTTP Method:** `POST`

| Environment    | Endpoint                                                       |
| -------------- | -------------------------------------------------------------- |
| **Test**       | `https://testdashboard.payu.in/oauth/get-merchant-credentials` |
| **Production** | `https://dashboard.payu.in/oauth/get-merchant-credentials`     |

For detailed information, refer to [Get Merchant Details API.](ref:getmerchant)

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl --location 'https://testdashboard.payu.in/oauth/get-merchant-credentials' \
  --header 'Content-Type: application/json' \
  --data '{
      "client_id": "ABC123",
      "client_secret": "your_client_secret"
  }'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-shield-check">
  ```json
  {
      "status": 1,
      "msg": "Success",
      "merchant_key": "mK3j2L9p",
      "salt": "sA7x9B2c"
  }
  ```
</Accordion>

***

### Step 7: Collect Payments

After you complete the above steps, the merchant can start collecting payments. You can integrate using:

- **Hosted Checkout** - Redirect customers to PayU's payment page
- **UPI S2S (Server-to-Server)** - Direct UPI integration for seamless payments

Choose the integration method based on your requirements.

#### Hosted Checkout Integration

For detailed steps to integrate, refer to [Hosted Checkout Integration](ref:hosted-checkout-api-partner-integration)

<Accordion title="Sample Request" icon="fa-code">
  ```curl
  curl --location --request POST \
  'https://test-partnerapilayer.payu.in/apilayer/partner/payments' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer <ROTATED_BEARER_TOKEN>' \
  --data-raw '{
    "txnid": "nY3tkz3vciHFGTjblyFeycL2Zn1m",
    "amount": 1090.33,
    "productinfo": "whatsapp",
    "firstname": "Manikanta",
    "reseller_id": "83fe-eb64-021844d8-9397-26535b1bf0c2",
    "merchant_id": "8238480",
    "phone": 7036722360,
    "hash": "52f45927e221a16bd5372709516de5110c06c55e0057f8a18a3b9b9f2c2f176870af276274709910f27d7c5df44822777542e3d4b86f29e8304e17fcb373133c",
    "lastname": "CHeruku",
    "email": "manik.cr24@gmail.com",
    "curl": "<YOUR_CANCEL_URL>",
    "furl": "<YOUR_FAILURE_URL>",
    "surl": "<YOUR_SUCCESS_URL>",
    "udf1": "whatsapp"
  }'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-reply">
  ```text
  {
      "redirectUri": "https://apitest.payu.in/public/#/35de666bac018494a06205addba2962cdb8d03ca9c2fa7954807098709f1b6dc"
  }
  ```
</Accordion>

#### UPI S2S Integration

For detailed steps, refer to [UPI S2S Integration API.](ref:upi-s2s-partner-integration-api)

<Accordion title="Sample Request" icon="fa-code">
  ```curl
  curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/payments' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer 9d2ab8e1b99aa02f6b827af5b5000b277d9cb1cd037acb7cb31436a5b0da4f74' \
  --data-raw '{
      "txnid": "nY3tkz3vciHFGTjblyFeycL2Zn1m",
      "amount": 1090.33,
      "productinfo": "whatsapp",
      "firstname": "Manikanta",
      "reseller_id": "83fe-eb64-021844d8-9397-26535b1bf0c2",
      "merchant_id": 8238480,
      "phone": 7036722360,
      "hash": "5aadceaf6bec9158ccba8ec0dab32debcacbfd50e3587c077fa11107a5be0ac26712fae230522afb8908d068122c02f2d5c733a46c33ace0f66e5cc9d2ae4714",
      "lastname": "CHeruku",
      "email": "manik.cr24@gmail.com",
      "curl": "https://www.google.com",
      "furl": "https://www.google.com",
      "surl": "https://www.youtube.com",
      "txn_s2s_flow": "4",
      "s2s_device_info": "ewew",
      "s2s_client_ip": "ewew"
  }'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-reply">
  ```text
  {
      "metaData": {
          "message": null,
          "referenceId": "024d9afbdbf85bd35b25649ccf983e16ee3d4646c2cdcffada88bd2df371fd43",
          "statusCode": null,
          "txnId": "nY3tkz3vciHFGTjblyFeycL2Zn1m",
          "txnStatus": "pending",
          "unmappedStatus": "pending"
      },
      "result": {
          "paymentId": 403993715529028543,
          "merchantName": "Merchant",
          "merchantVpa": null,
          "amount": "1090.33",
          "intentURIData": "pa=&pn=&tr=403993715529028543&tid=PPPL403993715529028543290523133325&am=1090.33&cu=INR&tn=UPI Transaction for PPPL403993715529028543290523133325",
          "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vdGVzdC5wYXl1LmluLzAyNGQ5YWZiZGJmODViZDM1YjI1NjQ5Y2NmOTgzZTE2NGQ0YTUxYzYzNjcyODAxNjRkMDlkNDg2YjRkYWI1ZmEvaW50ZW50U2VhbWxlc3NIYW5kbGVyLnBocCIgbWV0aG9kPSJwb3N0Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJ0b2tlbiIgdmFsdWU9IjE2NTIyQTgxLTUwMjYtMUUyRi0zNDFCLTJFQ0MyQ0Y5RTE1QyI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iYW1vdW50IiB2YWx1ZT0iMTA5MC4zMyI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0ibWlocGF5aWQiIHZhbHVlPSIwMjRkOWFmYmRiZjg1YmQzNWIyNTY0OWNjZjk4M2UxNmVlM2Q0NjQ2YzJjZGNmZmFkYTg4YmQyZGYzNzFmZDQzIj48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJkaXNhYmxlSW50ZW50U2VhbWxlc3NGYWlsdXJlIiB2YWx1ZT0iMSI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0icGF5ZWVWcGEiIHZhbHVlPSIiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InBheWVlTmFtZSIgdmFsdWU9Ik1lcmNoYW50Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJhZGRpdGlvbmFsQ2hhcmdlcyIgdmFsdWU9IjAiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InRyYW5zYWN0aW9uRmVlIiB2YWx1ZT0iMTA5MC4zMyI+PC9mb3JtPjxzY3JpcHQgdHlwZT0ndGV4dC9qYXZhc2NyaXB0Jz4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdpbmRvdy5vbmxvYWQ9ZnVuY3Rpb24oKXsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkb2N1bWVudC5mb3Jtc1sncGF5bWVudF9wb3N0J10uc3VibWl0KCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgICAgIDwvc2NyaXB0PjwvYm9keT48L2h0bWw+",
          "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
      }
  }
  ```
</Accordion>

#### Verify Payment

<Verify_Payment_Tabs />

<br />

***

## Next Steps

✅ **Test your integration**: Use the test environment credentials to verify the OAuth flow
✅ **Review API documentation**: [Validate Auth Code API](/reference/validate_authcode_and_client_api) | [Get Merchant Credentials API](/reference/get_merchant_credentials_api)
✅ **Go Live**: Contact your KAM to enable production OAuth and whitelist your redirect URLs

📚 For complete details on OAuth onboarding, see the [Co-Branded OAuth Documentation](/docs/refer-merchants-using-co-branded-oauth-onboarding).
