---
title: '[Step 3] Exchange Authorization Code API - Partner Integration'
deprecated: false
hidden: true
metadata:
  robots: index
---
This endpoint is the third and final step in the OAuth authentication flow. Exchange the authorization code from Step 2 for the final access token that you'll use in all Partner Payments API calls.

## Endpoint

**HTTP Method:** POST

**Environment URLs:**

| Environment | URL                                        |
| ----------- | ------------------------------------------ |
| Test        | `https://uat-accounts.payu.in/oauth/token` |
| Production  | `https://accounts.payu.in/oauth/token`     |

***

## Request Headers

```
Content-Type: application/x-www-form-urlencoded
```

***

## Request Parameters

| Parameter       | Type & Description                        | Example                                                    |
| --------------- | ----------------------------------------- | ---------------------------------------------------------- |
| `client_id`     | string — Your OAuth client ID             | YOUR_CLIENT_ID                                             |
| `client_secret` | string — Your OAuth client secret         | YOUR_CLIENT_SECRET                                         |
| `grant_type`    | string — Must be `authorization_code`     | authorization_code                                         |
| `code`          | string — Authorization code from Step 2   | a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6                           |
| `redirect_uri`  | string — Same redirect URI used in Step 2 | [https://uat-partner.payu.in](https://uat-partner.payu.in) |

***

## Sample Request

```bash
curl --location 'https://uat-accounts.payu.in/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=YOUR_CLIENT_ID' \
--data-urlencode 'client_secret=YOUR_CLIENT_SECRET' \
--data-urlencode 'grant_type=authorization_code' \
--data-urlencode 'code=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6' \
--data-urlencode 'redirect_uri=https://uat-partner.payu.in'
```

***

## Sample Response

```json
{
  "access_token": "039e0d1d70f467f946e2d73bd43868df856cfaa352ea54591a76bfc4a08d3487",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

***

## Response Parameters

| Parameter      | Type    | Description                                                         |
| -------------- | ------- | ------------------------------------------------------------------- |
| `access_token` | string  | **Final access token** — Use this in all Partner Payments API calls |
| `token_type`   | string  | Always "Bearer"                                                     |
| `expires_in`   | integer | Token validity duration in seconds (typically 3600 = 1 hour)        |

***

## Error Codes

| HTTP Status | Error                   | Description                                         |
| ----------- | ----------------------- | --------------------------------------------------- |
| 400         | `invalid_request`       | Missing required parameters                         |
| 401         | `invalid_client`        | Invalid `client_id` or `client_secret`              |
| 400         | `invalid_grant`         | Invalid or expired authorization code               |
| 400         | `redirect_uri_mismatch` | `redirect_uri` doesn't match the one used in Step 2 |

***

## Using the Final Access Token

Include this token in the `Authorization` header for all Partner Payments API requests:

```
Authorization: Bearer 039e0d1d70f467f946e2d73bd43868df856cfaa352ea54591a76bfc4a08d3487
```

**Applicable APIs:**

- [POST /partner/payments](ref:partner-payments-api) — Initiate partner payment
- [POST /partner/verifyPayment](ref:verify-payment-partner-api) — Verify payment status

***

## Token Expiry and Refresh

**Expiry:**

- Tokens typically expire after 3600 seconds (1 hour)
- When you receive a `401 Unauthorized` error, the token has expired

**Refresh Strategy:**

- There is no refresh token flow for Partner Payments
- When the token expires, repeat all three OAuth steps to generate a new token

**Best Practice:**

```python
class TokenManager:
    def __init__(self):
        self.token = None
        self.expiry_time = 0
    
    def get_token(self):
        if time.time() >= self.expiry_time:
            # Token expired, regenerate
            self.token = self.generate_new_token()
            self.expiry_time = time.time() + 3600
        return self.token
    
    def generate_new_token(self):
        # Execute all 3 OAuth steps
        step1_token = password_grant()
        auth_code = get_auth_code(step1_token)
        final_token = exchange_code(auth_code)
        return final_token
```

<Success>
**OAuth Flow Complete!** You now have the final access token to call Partner Payments APIs. Proceed to [POST /partner/payments](ref:partner-payments-api) to initiate your first payment.
</Success>