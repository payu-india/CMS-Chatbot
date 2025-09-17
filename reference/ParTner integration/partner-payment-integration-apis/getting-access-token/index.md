---
title: Get Access Token - Partner Integration
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
To get access token to be used in WhatsApp integration:

1. Receiving the **auth_code** on the redirect URI

2. Validate this **auth_code** using the [Validate Auth Code and Client API](ref:validate-auth-code-and-client).

   You will receive an accesss_token.

3. Use the accesss_token in the following integrations:
   * [UPI S2S Integration API - WhatsApp](ref:upi-s2s-integration-api) flow
   * [Hosted Checkout API](doc:hosted-checkout-api-whatsapp-integration)flow

<Callout icon="📘" theme="info">
  **Note**: [Refresh Token API for WhatsApp Integration](ref:refresh-token-whatsapp-integration) is used to fetch new access_token using the refresh_token received in the **Validate Auth Code and Client** API.
</Callout>
