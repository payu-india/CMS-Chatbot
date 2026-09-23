---
title: Authentication
excerpt: >-
  Payment Links APIs use OAuth 2.0 Bearer tokens. Generate a scoped token before
  calling any Payment Links endpoint.
hidden: true
link:
  new_tab: false
metadata:
  title: Authentication — PayU Payment Links API
  description: >-
    PayU Payment Links APIs use OAuth 2.0 client credentials. Learn how to
    generate and revoke Bearer tokens, manage scopes, and handle token expiry
    for Payment Links API calls.
  keywords:
    - PayU OAuth
    - payment links authentication
    - Bearer token PayU
    - client credentials grant
    - access token payment links
next:
  description: Explore related information and resources.
  pages:
    - slug: payment-links
      title: Payment Links
      type: basic
    - slug: revoketokenapi
      title: Revoke Token API
      type: endpoint
---
Payment Links APIs use **OAuth 2.0 client credentials** — not the hash-based authentication used by PayU's General or Merchant Hosted APIs. Every API call requires a Bearer token in the `Authorization` header.

<Callout icon="📘" theme="info">
  ### Get Your Client ID and Secret

  Go to PayU Dashboard → **Developers** → **Client ID & Client secret details** to find your `client_id` and `client_secret`. See [Get Client ID and Secret](doc:get-client-id-and-secret-from-dashboard) for a walkthrough.
</Callout>

***

## Base URLs

| Environment | Auth base URL                  |
| :---------- | :----------------------------- |
| Test        | `https://uat-accounts.payu.in` |
| Production  | `https://accounts.payu.in`     |

***

## Scopes

A single token can carry up to three scopes simultaneously — pass them space-separated in the `scope` parameter.

| Scope                  | Grants access to                                                 |
| :--------------------- | :--------------------------------------------------------------- |
| `create_payment_links` | Create Payment Link                                              |
| `update_payment_links` | Update / Cancel Payment Link                                     |
| `read_payment_links`   | Fetch Payment Link · Fetch All · Share · Get Transaction Details |

## API Endpoints

These are the authentication APIs

<Cards>
  <Card title="Get Access Token" href="ref:get-token-api-for-payment-links">
    `POST /oauth/token`

    Exchange your `client_id` and `client_secret` for a scoped Bearer token. Call this before any Payment Links API.
  </Card>

  <Card title="Revoke Token API" href="ref:revoke-token-api-payment-links">
    `POST /oauth/revoke`

    Invalidate a token before it naturally expires. Use this when rotating credentials or if a token may have been exposed.
  </Card>
</Cards>

***

## How it works

<Accordion title="1. Generate a token" icon="fa-key">
  Call `POST /oauth/token` with your `client_id`, `client_secret`, `grant_type: client_credentials`, and the scopes your integration needs. </Accordion> <Accordion title="2. Cache the token" icon="fa-database"> Store `access_token` and calculate its expiry as `created_at + expires_in`. Do not call this endpoint before every API request — that is wasteful and will trigger rate limits.
</Accordion>

<Accordion title="3. Use the token" icon="fa-paper-plane"> Pass the token in the `Authorization` header of every Payment Links API call:

Authorization: Bearer {access_token} </Accordion> <Accordion title="4. Refresh before expiry" icon="fa-rotate"> Regenerate the token before it expires. The previous token stays valid until its exact expiry time, so there is no gap in service during rotation. </Accordion> <Accordion title="5. Revoke if needed" icon="fa-ban"> Call `POST /oauth/revoke` to invalidate a token early — for example, when rotating credentials or if a token may have been exposed. </Accordion>

## Using the token

<Tabs>
  <Tab title="cURL">
    ```curl
    curl --location --request POST 'https://uatoneapi.payu.in/payment-links' \
    --header 'Authorization: Bearer {{access_token}}' \
    --header 'merchantId: {{merchantId}}' \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "subAmount": 1499,
      "description": "Test order",
      "source": "API"
    }'
    ```
  </Tab>

  <Tab title="Python">
    ```python
    import requests

    headers = {
        "Authorization": "Bearer {{access_token}}",
        "merchantId": "{{merchantId}}",
        "Content-Type": "application/json"
    }
    payload = {"subAmount": 1499, "description": "Test order", "source": "API"}
    response = requests.post("https://uatoneapi.payu.in/payment-links", headers=headers, json=payload)
    print(response.json())
    ```
  </Tab>

  <Tab title="Node.js">
    ```javascript
    const axios = require('axios');

    const response = await axios.post(
      'https://uatoneapi.payu.in/payment-links',
      { subAmount: 1499, description: 'Test order', source: 'API' },
      {
        headers: {
          'Authorization': 'Bearer {{access_token}}',
          'merchantId': '{{merchantId}}',
          'Content-Type': 'application/json'
        }
      }
    );
    console.log(response.data);
    ```
  </Tab>

  <Tab title="PHP">
    ```php
    <?php
    $ch = curl_init('https://uatoneapi.payu.in/payment-links');
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST           => true,
        CURLOPT_POSTFIELDS     => json_encode([
            'subAmount'   => 1499,
            'description' => 'Test order',
            'source'      => 'API'
        ]),
        CURLOPT_HTTPHEADER => [
            'Authorization: Bearer {{access_token}}',
            'merchantId: {{merchantId}}',
            'Content-Type: application/json'
        ]
    ]);
    echo curl_exec($ch);
    ```
  </Tab>
</Tabs>

## Error reference

| Error                 | When                                          | Fix                                                                    |
| :-------------------- | :-------------------------------------------- | :--------------------------------------------------------------------- |
| `invalid_client`      | Wrong `client_id` or `client_secret`          | Verify credentials in Dashboard → OAuth Apps                           |
| `invalid_scope`       | Scope misspelled or not permitted             | Check scope values — case-sensitive, space-separated                   |
| `unauthorized_client` | App not configured for `client_credentials`   | Contact PayU support                                                   |
| `rate_limit_exceeded` | Too many token requests                       | Cache tokens; retry after `retry_after` seconds                        |
| `invalid_token`       | Token expired or revoked                      | Regenerate via [Get Access Token](ref:get-token-api-for-payment-links) |
| `insufficient_scope`  | Token missing required scope for the endpoint | Regenerate with the correct scope                                      |

## Related

- [Get Access Token](ref:get-token-api-for-payment-links)
- [Revoke Token API](ref:revoke-token-api-payment-links)
- [Payment Links API Overview](ref:payment-links-api-overview)
- [Get Client ID and Secret from Dashboard](doc:get-client-id-and-secret-from-dashboard)
