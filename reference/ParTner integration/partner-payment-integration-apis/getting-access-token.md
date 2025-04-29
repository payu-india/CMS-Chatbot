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

1. Receiving the **auth\_code** on the redirect URI

2. Validate this **auth\_code** using the [Validate Auth Code and Client API](ref:validate-auth-code-and-client).

   You will receive an accesss\_token.  

3. Use the accesss\_token in the following integrations:
   - [UPI S2S Integration API - WhatsApp](ref:upi-s2s-integration-api) flow 
   - [Hosted Checkout API](doc:hosted-checkout-api-whatsapp-integration)flow

> 📘 Note:
> 
> [Refresh Token API for WhatsApp Integration](ref:refresh-token-whatsapp-integration) is used to fetch new access\_token using the refresh\_token received in the **Validate Auth Code and Client** API.