---
title: Get Access Token - Partner Integration
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
To get access token to be used in Partner integration:

1. Receiving the **auth_code** on the redirect URI

2. Validate this **auth_code** using the [Validate Auth Code and Client API](ref:validate-auth-code-and-client).

   You will receive an accesss_token.

3. Use the access token in the following APIs:

   * [Hosted Checkout Integration](ref:hosted-checkout-api-partner-integration)
   * [UPI S2S Integration API](ref:upi-s2s-partner-integration-api)

<Callout icon="📘" theme="info">
  **Note**: [Refresh Token API](ref:refresh_token_api) is used to fetch new access_token using the refresh_token received in the **Validate Auth Code and Client** API.
</Callout>