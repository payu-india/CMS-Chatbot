---
name: Parttner_Payment_Auth
---
## Step 1 OAuth Authentication

### Step 1.1 Receiving the auth_code on the redirect URI

The `auth_code` is received on the configured redirect URI.

### Step 1.2 Validate this auth_code

Validate this auth_code using the [Validate Auth Code and Client API](https://docs.payu.in/reference-link/validate-auth-code-and-client).

You will receive an access_token.
<Accordion title="Request Parameters" icon="fa-info-table">
| Parameter | Required | Description | Example value |
| --- | --- | --- | --- |
| `client_id` | Yes | Client identifier. | `{{client_id}}` |
| `client_secret` | Yes | Client secret code. | `{{client_secret}}` |
| `grant_type` | Yes | Grant type used to obtain an access token in this flow. Must be `authorization_code`. | `authorization_code` |
| `code` | Yes | Authorization code received on the redirect URI. | `{{authorization_code}}` |
| `redirect_uri` | Yes | Redirect URL associated with the authorization request. It must match the redirect URI used for the authorization request. | `{{redirect_uri}}` |

</Accordion>

<Accordion title="Samp[e request" icon="fa-code">
```bash
curl --location '{{accounts_base_url}}/oauth/token' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'client_id={{client_id}}' \
  --data-urlencode 'client_secret={{client_secret}}' \
  --data-urlencode 'grant_type=authorization_code' \
  --data-urlencode 'code={{authorization_code}}' \
  --data-urlencode 'redirect_uri={{redirect_uri}}'
```
</Accordion>

<Accordion title="Sample response" icon="fa-info-reply">
```json
{
  "access_token": "{{access_token}}",
  "token_type": "Bearer",
  "expires_in": {{expires_in}},
  "refresh_token": "{{refresh_token}}",
  "scope": "{{scope}}",
  "created_at": {{created_at}},
  "user_uuid": "{{user_uuid}}"
}
```
</Accordion>
## Step 1.3 Use the access_token

Send the access token as a bearer token when calling Partner Integration APIs.

