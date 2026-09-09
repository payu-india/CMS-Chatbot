---
title: Reseller Client Credentials Token
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Reseller Client Credentials Token** API obtains an access token for a reseller using the OAuth `client_credentials` grant. Use this token to call the payment and verify-payment APIs on behalf of merchants linked to the reseller. This avoids the per-merchant authorization-code flow.

<Callout icon="📘" theme="info">
  ### Notes:

  - **Purpose:** This flow is for linked merchants only.
  - **Prerequisite:** The merchant must be linked to the reseller.
  - The OAuth application must have the appropriate scopes for the APIs the reseller will call.
</Callout>

**HTTP Method**: POST

**Environment**

| Environment | URL                                        |
| :---------- | :----------------------------------------- |
| UAT         | `https://uat-accounts.payu.in/oauth/token` |
| Production  | `https://accounts.payu.in/oauth/token`     |

## Request parameters&#x20;

### Header parameters

<Accordion title="Header parameters" icon="fa-table">
  | Header                                     | Description            | Example                             |
  | :----------------------------------------- | :--------------------- | :---------------------------------- |
  | `Content-Type`<br /><code>mandatory</code> | Request body encoding. | `application/x-www-form-urlencoded` |
</Accordion>

### Body parameters

<Accordion title="Body parameters" icon="fa-table">
  | Parameter                                   | Description                                                                     | Example                                  |
  | :------------------------------------------ | :------------------------------------------------------------------------------ | :--------------------------------------- |
  | `client_id`<br /><code>mandatory</code>     | Reseller OAuth client ID.                                                       | `<RESELLER_CLIENT_ID>`                   |
  | `client_secret`<br /><code>mandatory</code> | Reseller OAuth client secret.                                                   | `<RESELLER_CLIENT_SECRET>`               |
  | `grant_type`<br /><code>mandatory</code>    | Must be `client_credentials`.                                                   | `client_credentials`                     |
  | `scope`<br /><code>mandatory</code>         | Space-separated scopes. For payments: `partner_payment_links partner_payments`. | `partner_payment_links partner_payments` |
</Accordion>

## Using the Reseller Token

Pass the returned token in the `Authorization` header when calling both `/partner/payments` and `/partner/verifyPayment`:

```http
Authorization: Bearer <RESELLER_ACCESS_TOKEN>
```

The system validates the token against the reseller portal and verifies that the `merchant_id` supplied in the request body is linked to the reseller before processing the request. If the merchant is not linked, the request is rejected with an authentication failure.

<Callout icon="📘" theme="info">
  **Scope note:** The `scope` request parameter description lists `partner_payment_links` and `partner_payments`. The Notes section of the PDF additionally says that partner payments require `create_payment_links`, `partner_payment_links`, and `partner_payments`, and that the OAuth application must have appropriate scopes. Confirm that the OAuth application has the scopes required for the APIs you will use; this reference preserves both statements rather than resolving the difference.
</Callout>

## Token usage and prerequisites

Use the reseller client credentials token when the merchant is already linked to the reseller and the reseller wants a single server-to-server token for multiple linked merchants. The token is not the per-merchant authorization-code token described elsewhere in the integration guide.

Before requesting the token, ensure that:

- The merchant is linked to the reseller.
- The OAuth application has appropriate scopes, subject to the scope note above.

## Sample Request

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://uat-accounts.payu.in/oauth/token' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'client_id=<RESELLER_CLIENT_ID>' \
  --data-urlencode 'client_secret=<RESELLER_CLIENT_SECRET>' \
  --data-urlencode 'grant_type=client_credentials' \
  --data-urlencode 'scope=partner_payment_links partner_payments'
  ```

  The request uses `POST` and sends the four form parameters with `Content-Type: application/x-www-form-urlencoded`.
</Accordion>

## Sample Response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
  "access_token": "<RESELLER_ACCESS_TOKEN>",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "partner_payment_links partner_payments"
  }
  ```
</Accordion>

## Response parameters

<Accordion title="Response parameters" icon="fa-table">
  | Parameter      | Description                                              | Example                                  |
  | :------------- | :------------------------------------------------------- | :--------------------------------------- |
  | `access_token` | Reseller access token to use in subsequent API requests. | `<RESELLER_ACCESS_TOKEN>`                |
  | `token_type`   | Token type returned by the OAuth server.                 | `Bearer`                                 |
  | `expires_in`   | Token lifetime in seconds.                               | `3600`                                   |
  | `scope`        | Scopes granted to the token.                             | `partner_payment_links partner_payments` |
</Accordion>

##
