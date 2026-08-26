---
api:
  file: payu_partner_gettoken.postman_collection.json
  operationId: post_oauth-token
hidden: false
---
The **GetToken** API obtains an OAuth bearer token for Partner Onboarding APIs. Call this first (Step 00); use the returned `access_token` as `Authorization: Bearer {token}` on all later steps (Step 1 to Step 16).

**HTTP Method**: POST

**Environment**

|                        | URL                                        |
| :--------------------- | :----------------------------------------- |
| Test Environment       | `https://uat-accounts.payu.in/oauth/token` |
| Production Environment | `https://accounts.payu.in/oauth/token`     |

## Sample Request

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://uat-accounts.payu.in/oauth/token' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'client_id={{client_id}}' \
  --data-urlencode 'client_secret={{client_secret}}' \
  --data-urlencode 'grant_type=client_credentials' \
  --data-urlencode 'scope=refer_merchant'
  ```
</Accordion>

## Sample Response

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "access_token": "7b5843b39e5532bc...",
    "token_type": "Bearer",
    "expires_in": 7199,
    "scope": "refer_merchant",
    "created_at": 1723498499
  }
  ```
</Accordion>

<Accordion title="Failure scenario" icon="fa-file-code">
  - **401 Unauthorized** — Invalid `client_id` or `client_secret`

  ```json
  {
    "error": "invalid_client",
    "error_description": "Client authentication failed"
  }
  ```

  - **400 Bad Request** — Invalid `grant_type` or `scope`

  ```json
  {
    "error": "invalid_request",
    "error_description": "Missing or invalid grant_type"
  }
  ```
</Accordion>

## Response Parameters

<Accordion title="Response parameters" icon="fa-table">
  | Parameter    | Description                                              | Example               |
  | :----------- | :------------------------------------------------------- | :-------------------- |
  | access_token | `string` — Bearer token for subsequent Partner API calls | `7b5843b39e5532bc...` |
  | token_type   | `string` — Always `Bearer`                               | `Bearer`              |
  | expires_in   | `integer` — Token validity in seconds                    | `7199`                |
  | scope        | `string` — Granted OAuth scopes                          | `refer_merchant`      |
  | created_at   | `integer` — Unix timestamp when the token was issued     | `1723498499`          |
</Accordion>

## Additional Request Parameters Info

<Accordion title="Header parameters" icon="fa-table">
  | Header                                   | Description                                            | Example                             |
  | :--------------------------------------- | :----------------------------------------------------- | :---------------------------------- |
  | Content-Type<br /><code>mandatory</code> | `string` — Must be `application/x-www-form-urlencoded` | `application/x-www-form-urlencoded` |
</Accordion>

<Accordion title="Body parameters" icon="fa-table">
  | Parameter                                 | Description                                                  | Example              |
  | :---------------------------------------- | :----------------------------------------------------------- | :------------------- |
  | client_id<br /><code>mandatory</code>     | `string` — Partner OAuth client ID (from PayU KAM)           | `a1b2c3...`          |
  | client_secret<br /><code>mandatory</code> | `string` — Partner OAuth client secret                       | `d4e5f6...`          |
  | grant_type<br /><code>mandatory</code>    | `string` — Must be `client_credentials`                      | `client_credentials` |
  | scope<br /><code>mandatory</code>         | `string` — Space-separated scopes (include `refer_merchant`) | `refer_merchant`     |
</Accordion>
