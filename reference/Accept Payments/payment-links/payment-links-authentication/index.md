---
title: Authentication
excerpt: Generate and revoke OAuth 2.0 Bearer tokens.
hidden: true
link:
  new_tab: false
metadata:
  title: Authentication
  description: Generate and revoke OAuth 2.0 Bearer tokens.
next:
  description: Explore related information and resources.
---
Payment Links APIs use OAuth 2.0 client credentials. Every API call requires a Bearer token in the `Authorization` header.

<Callout icon="📘" theme="info">
  ### Getting your credentials

  Go to PayU Dashboard → **Developers** → **Client ID & Client secret details** to find your `client_id` and `client_secret`. See [Get Client ID and Secret](doc:get-client-id-and-secret-from-dashboard) for a walkthrough.
</Callout>

<Callout icon="⚠️" theme="warn">
  ### Different Base URL

  Authentication endpoints use `accounts.payu.in`, not `oneapi.payu.in`.

  | Environment | Auth base URL                  |
  | :---------- | :----------------------------- |
  | Test        | `https://uat-accounts.payu.in` |
  | Production  | `https://accounts.payu.in`     |
</Callout>

***

## Scopes

A single token can carry up to three scopes simultaneously. You should pass them space-separated in the `scope` parameter.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Scope
      </th>

      <th>
        Grants access to
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `create_payment_links`
      </td>

      <td>
        Create a Payment Link
      </td>
    </tr>

    <tr>
      <td>
        `update_payment_links`
      </td>

      <td>
        Update or Cancel a Payment Link
      </td>
    </tr>

    <tr>
      <td>
        `read_payment_links`
      </td>

      <td>
        - Fetch a Payment Link
        - Fetch All Payment Links
        - Share a Payment Link
        - Fetch Transaction Details
      </td>
    </tr>
  </tbody>
</Table>

<Callout icon="👍" theme="okay">
  ### Request All Scopes in One Call

  You can individual scope or add all scopes in one call as shown below:

  `scope=create_payment_links update_payment_links read_payment_links`
</Callout>

***

## Endpoints

These are the authentication APIs

<Cards>
  <Card title="Get an Access Token" href="https://docs.payu.in/v3.0/reference/get-access-token" target="_blank">
    Exchange your `client_id` and `client_secret` for a scoped Bearer token. Call this before any Payment Links API.
  </Card>

  <Card title="Revoke a Token" href="ref:revoke-token-api-payment-links">
    Invalidate a token before it naturally expires. Use this when rotating credentials or if a token may have been exposed.
  </Card>
</Cards>

***

## How It Works

<Accordion title="1. Generate a Token" icon="fa-key">
  Call Get an Access Token API with your `client_id`, `client_secret`, `grant_type: client_credentials`, and the scopes your integration needs.
</Accordion>

<Accordion title="2. Cache the Token" icon="fa-database">
  Store `access_token` and calculate its expiry as `created_at + expires_in`.&#x20;
</Accordion>

<Accordion title="3. Use the Token" icon="fa-paper-plane">
  Pass the token in the `Authorization` header of every Payment Links API call as shown below:

  ```
  Authorization: Bearer {access_token}
  ```
</Accordion>

<Accordion title="4. Refresh Before Expiry" icon="fa-rotate">
  Regenerate the token before it expires. The previous token stays valid until its exact expiry time, so there is no gap in service during rotation.
</Accordion>

<Accordion title="5. Revoke if Needed" icon="fa-ban">
  Call the Revoke a Token API to invalidate a token early if needed. For example, when rotating credentials or if a token may have been exposed.
</Accordion>

##
