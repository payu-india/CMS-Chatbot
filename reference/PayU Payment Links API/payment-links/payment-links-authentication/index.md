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
Payment Links APIs use OAuth 2.0 client credentials for authentication. Before calling any Payment Links endpoint, you need a Bearer token. Every API call then passes that token in the `Authorization` header.

<Callout icon="📘" theme="info">
  ### **Where do I get my Client ID and Secret?**

  Go to your PayU Dashboard → **Developers** → **OAuth Apps**. See [Get Client ID and Secret](doc:get-client-id-and-secret-from-dashboard) for a step-by-step walkthrough.
</Callout>

***

## Environments

| Environment | Base URL                       |
| :---------- | :----------------------------- |
| Test        | `https://uat-accounts.payu.in` |
| Production  | `https://accounts.payu.in`     |

<Callout icon="⚠️" theme="warn">
  ### The authentication endpoints use a **different base URL** (`accounts.payu.in`) from the Payment Links endpoints (`oneapi.payu.in`). Make sure you're hitting the right host for each call.
</Callout>

***

## Endpoints

<Cards>
  <Card title="Get Access Token" href="ref:get-token-api-for-payment-links">
    `POST /oauth/token`

    Exchange your `client_id` and `client_secret` for a Bearer token. Specify the scopes you need. Required before calling any Payment Links API.
  </Card>

  <Card title="Revoke Token API" href="ref:revoke-token-api-payment-links">
    `POST /oauth/revoke`

    Invalidate an existing token before it naturally expires. Use when rotating credentials or if a token may have been exposed.
  </Card>
</Cards>

***

## Scopes

A single token can carry up to three scopes simultaneously. Pass them space-separated in the `scope` parameter when generating the token.

| Scope                  | Grants access to                                                                            |
| :--------------------- | :------------------------------------------------------------------------------------------ |
| `create_payment_links` | Create Payment Link                                                                         |
| `update_payment_links` | Update / Cancel Payment Link                                                                |
| `read_payment_links`   | Fetch Payment Link · Fetch All Payment Links · Share Payment Link · Get Transaction Details |

<Callout icon="📘" theme="info">
  ### **Tip:** Request all the scopes your integration needs in one token call rather than generating separate tokens per operation.

  `scope=create_payment_links update_payment_links read_payment_links`
</Callout>

***

## How it works

1. **Generate a token** — Call `POST /oauth/token` with your `client_id`, `client_secret`, `grant_type: client_credentials`, and the scopes you need.
2. **Store the token** — Save `access_token` and calculate its expiry as `created_at + expires_in` (both in the response). Do not call this endpoint before every API request.
3. **Use the token** — Pass the token in the `Authorization` header of every Payment Links API call: `Authorization: Bearer {access_token}`.
4. **Refresh before expiry** — When the token is within a few seconds of expiring, generate a new one. The previous token continues to work until its exact expiry time.
5. **Revoke if needed** — If a token is no longer needed or may have been exposed, call `POST /oauth/revoke` to invalidate it immediately.

***

## Token lifecycle

| Parameter      | Description                                                                                                |
| :------------- | :--------------------------------------------------------------------------------------------------------- |
| `access_token` | The Bearer token string to pass in the `Authorization` header.                                             |
| `expires_in`   | Validity period in seconds (typically `7200` — 2 hours). Configurable per OAuth app in the PayU Dashboard. |
| `created_at`   | UNIX timestamp when the token was issued. Compute absolute expiry: `created_at + expires_in`.              |
| `scope`        | Scopes granted. Verify this matches your request — a mismatch indicates a misconfigured app.               |

<Callout icon="👍" theme="okay">
  ### **Cache your token**

  Generating a new token before every API call is wasteful and will trigger rate limits. Cache the token in memory, check expiry before each call, and only regenerate when needed.
</Callout>

***

## Using the token

Include the token in the `Authorization` header of every Payment Links API call:

```
Authorization: Bearer ea4ed864b4d2a04b90c1e987a5d25a5da1d43fa5f7d123be6814a1e973f196c4
```

Example — creating a payment link with the token:

```curl
curl --location --request POST 'https://uatoneapi.payu.in/payment-links' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'merchantId: {{merchantId}}' \
--header 'Content-Type: application/json' \
--data-raw '{ "subAmount": 1499, "description": "Test order", "source": "API" }'
```

***

## Error handling

| Error                              | Cause                                                             | Fix                                                                                   |
| :--------------------------------- | :---------------------------------------------------------------- | :------------------------------------------------------------------------------------ |
| `invalid_client`                   | Wrong `client_id` or `client_secret`.                             | Verify credentials in PayU Dashboard → OAuth Apps.                                    |
| `invalid_scope`                    | Scope value is misspelled or not permitted for this app.          | Check the scopes table above. Values are case-sensitive and space-separated.          |
| `unauthorized_client`              | App is not configured for `client_credentials` grant.             | Contact PayU support to verify your app's grant type.                                 |
| `rate_limit_exceeded`              | Too many token requests in a short window.                        | Cache tokens and reuse until `expires_in` elapses. Retry after `retry_after` seconds. |
| `invalid_token` (on API call)      | Token has expired or been revoked.                                | Generate a new token via [Get Access Token](ref:get-token-api-for-payment-links).     |
| `insufficient_scope` (on API call) | Token does not include the scope required by the endpoint called. | Regenerate the token with the correct scope for the operation.                        |

***

## Related APIs

- [Get Access Token](ref:get-token-api-for-payment-links) — Generate a Bearer token
- [Revoke Token API](ref:revoke-token-api-payment-links) — Invalidate a token early
- [Payment Links API Overview](ref:payment-links-api-overview) — Full list of Payment Links endpoints
- [Get Client ID and Secret from Dashboard](doc:get-client-id-and-secret-from-dashboard)
