---
title: '[NEW] Get Authorization Code - Partner Integration'
deprecated: false
hidden: true
metadata:
  robots: index
---
This endpoint is the second step in the three-step OAuth authentication flow. Use the access token from Step 1 to obtain an authorization code for a specific merchant.

## Endpoint

**HTTP Method:** POST

**Environment URLs:**

| Environment | URL                                                      |
| ----------- | -------------------------------------------------------- |
| Test        | `https://uat-partner.payu.in/api/v1/merchants/auth_code` |
| Production  | `https://partner.payu.in/api/v1/merchants/auth_code`     |

***

## Request Headers

```
Authorization: Bearer <ACCESS_TOKEN_FROM_STEP_1>
Content-Type: application/x-www-form-urlencoded
```

***

## Request Parameters

| Parameter       | Type & Description                                                  | Example                                                     |
| --------------- | ------------------------------------------------------------------- | ----------------------------------------------------------- |
| `merchant_id`   | integer — PayU merchant ID for whom payment will be initiated       | 8739528                                                     |
| `reseller_uuid` | string — Your partner/reseller UUID                                 | 11ee-0e7e-5403fde2-9523-0a696b110fde                        |
| `redirect_uri`  | string — OAuth redirect URI (typically your partner dashboard URL)  | [https://uat-partner.payu.in](https://uat-partner.payu.in)  |
| `scopes`        | string — Space-separated OAuth scopes required for Partner Payments | create_payment_links partner_payment_links partner_payments |

***

## Sample Request

```bash
curl --location 'https://uat-partner.payu.in/api/v1/merchants/auth_code' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'merchant_id=8739528' \
--data-urlencode 'reseller_uuid=11ee-0e7e-5403fde2-9523-0a696b110fde' \
--data-urlencode 'redirect_uri=https://uat-partner.payu.in' \
--data-urlencode 'scopes=create_payment_links partner_payment_links partner_payments'
```

> **Note:** Replace the Bearer token with the `access_token` received from Step 1.

***

## Sample Response

```json
{
  "data": {
    "id": "1340444",
    "type": "authorization-codes",
    "attributes": {
      "code": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
      "redirect-uri": "https://uat-partner.payu.in"
    }
  }
}
```

***

## Response Parameters

| Parameter                      | Type   | Description                                                                    |
| ------------------------------ | ------ | ------------------------------------------------------------------------------ |
| `data.id`                      | string | Internal authorization code ID                                                 |
| `data.type`                    | string | Always "authorization-codes"                                                   |
| `data.attributes.code`         | string | **Authorization code** — Use this in Step 3 to exchange for final access token |
| `data.attributes.redirect-uri` | string | Echo of the redirect URI provided in request                                   |

***

## Error Codes

| HTTP Status | Error                | Description                                                 |
| ----------- | -------------------- | ----------------------------------------------------------- |
| 401         | `Unauthorized`       | Invalid or expired access token from Step 1                 |
| 400         | `invalid_request`    | Missing required parameters                                 |
| 404         | `merchant_not_found` | `merchant_id` doesn't exist or isn't linked to this partner |
| 403         | `scope_not_allowed`  | Requested scopes are not enabled for this partner           |

***

## Next Steps

After obtaining the authorization code:

1. Extract the `data.attributes.code` value
2. Use it immediately in [POST /oauth/token (Authorization Code Exchange)](ref:exchange-authorization-code-api)
3. Complete Step 3 to get the final access token for Partner Payments API calls

<Warning>
**Authorization Code Expiry:** Authorization codes are typically valid for a short duration (5-10 minutes). Exchange it immediately for the final access token.
</Warning>
