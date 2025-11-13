---
title: Get Token API - Payment Links
excerpt: >-
  OAuth 2.0 Client Credentials Grant Token Request


  This endpoint is used to obtain an access token using the client credentials
  grant type. The token can then be used to authenticate subsequent API
  requests.


  **Parameters:**

  - client_id: Your OAuth 2.0 client identifier

  - client_secret: Your OAuth 2.0 client secret

  - grant_type: Must be 'client_credentials'

  - scope: The requested scope (read_payment_links)


  **Response:**

  Returns an access token that should be used in the Authorization header for
  authenticated requests.
api:
  file: PayU_OAuth2_Collection.json
  operationId: post_oauth-token
hidden: true
---