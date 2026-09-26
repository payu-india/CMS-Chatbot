---
api:
  file: pl-test-oas.yaml
  operationId: RevokeTokenAPI
hidden: false
metadata:
  title: Revoke a Token API
---
Invalidate a Bearer token before its natural expiry. Use this endpoint when rotating credentials or if you suspect a token has been exposed.<br />

The revoked token becomes invalid immediately. After revoking, generate a newtoken via the Get A Access Token API.

***

## Environments

| Environment    | Base URL                       |
| :------------- | :----------------------------- |
| **Test**       | `https://uat-accounts.payu.in` |
| **Production** | `https://accounts.payu.in`     |

<Callout icon="📘" theme="info">
  ### **When Should I Revoke a Token?**

  You do not need to revoke tokens as part of a normal flow as they expire automatically after `expires_in` seconds. Revoke only when you need to invalidate a token early. For example, on user logout, credential rotation, or if a token may have been exposed.
</Callout>

***

## Sample Request

<Tabs>
  <Tab title="Request Payload">
    ```curl
    curl --location --request POST 'https://uat-accounts.payu.in/oauth/revoke' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'client_id={{client_id}}' \
    --data-urlencode 'client_secret={{client_secret}}' \
    --data-urlencode 'token={{access_token}}'
    ```
  </Tab>

  <Tab title="Parameter Description">

  </Tab>
</Tabs>
