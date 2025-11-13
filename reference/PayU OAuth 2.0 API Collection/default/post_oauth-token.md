---
title: OAuth 2.0 Token Request
excerpt: >-
  OAuth 2.0 Client Credentials Grant Token Request


  This endpoint is used to obtain an access token using the client credentials
  grant type. The token can then be used to authenticate subsequent API
  requests.


  **Equivalent cURL:**

  ```bash

  curl --location 'https://uat-accounts.payu.in/oauth/token' \

  --header 'Content-Type: application/x-www-form-urlencoded' \

  --data-urlencode
  'client_id=b5ff863b120f59dbf386e5e066903c2b7791473e5a2d46d9a38712e629728c91' \

  --data-urlencode
  'client_secret=27294d65c636f205ac5cf232f65c6b231a21ec89f249e0f5866a36feb25faab6'
  \

  --data-urlencode 'grant_type=client_credentials' \

  --data-urlencode 'scope=create_payment_links update_payment_links
  read_payment_links'

  ```


  **Parameters:**

  - client_id: b5ff863b120f59dbf386e5e066903c2b7791473e5a2d46d9a38712e629728c91

  - client_secret:
  27294d65c636f205ac5cf232f65c6b231a21ec89f249e0f5866a36feb25faab6

  - grant_type: client_credentials

  - scope: create_payment_links update_payment_links read_payment_links


  **Response:**

  Returns an access token that should be used in the Authorization header for
  authenticated requests.
api:
  file: PayU_OAuth2_Collection.json
  operationId: post_oauth-token
hidden: false
---