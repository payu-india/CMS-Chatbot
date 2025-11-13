---
title: OAuth 2.0 Token Request
excerpt: >-
  OAuth 2.0 Token Request


  Generates this exact cURL:

  ```

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
api:
  file: PayU_OAuth2_Collection.json
  operationId: post_oauth-token
hidden: false
---