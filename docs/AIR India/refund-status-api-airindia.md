---
title: Refund Status API
deprecated: false
hidden: true
metadata:
  robots: index
---
Checks refund status for one or more refund requests. Supports lookup by `requestId`, `payuId`, or `tokenId` (refundToken). Provides parent-child transaction visibility for split payments.

## Endpoint

| Environment | Base URL |
|-------------|----------|
| Test | `https://apitest.payu.in/v2/refunds/status` |
| Production | `https://info.payu.in/v2/refunds/status` |

## Sample Request

### Check by Request ID

```bash
curl -X POST 'https://apitest.payu.in/v2/refunds/status' \
  -H 'Date: Wed, 15 Jan 2025 10:30:00 GMT' \
  -H 'Authorization: hmac username="merchantKey", algorithm="sha512", headers="date", signature="abc123..."' \
  -H 'Content-Type: application/json' \
  -d '{
    "requestId": ["139128152", "139128153"]
  }'
```

### Check by PayU ID

```bash
curl -X POST 'https://apitest.payu.in/v2/refunds/status' \
  -H 'Date: Wed, 15 Jan 2025 10:30:00 GMT' \
  -H 'Authorization: hmac username="merchantKey", algorithm="sha512", headers="date", signature="abc123..."' \
  -H 'Content-Type: application/json' \
  -d '{
    "payuId": ["403993715535600711"]
  }'
```

### Check by Refund Token

```bash
curl -X POST 'https://apitest.payu.in/v2/refunds/status' \
  -H 'Date: Wed, 15 Jan 2025 10:30:00 GMT' \
  -H 'Authorization: hmac username="merchantKey", algorithm="sha512", headers="date", signature="abc123..."' \
  -H 'Content-Type: application/json' \
  -d '{
    "tokenId": ["REF_ORD123_001", "REF_ORD123_002"]
  }'
```

## Sample Response

### Success Response

```json
{
  "message": "Success",
  "status": 1,
  "result": [
    {
      "payuId": 403993715535600711,
      "transactionDetails": {
        "id": 403993715535600711,
        "status": "captured",
        "amount": 121.51,
        "mode": "NB"
      },
      "transactionActionDetails": [
        {
          "id": 139128152,
          "token": "3528998",
          "actionType": "refund",
          "amount": 2.0,
          "status": "queued",
          "refundMode": "Back to Source",
          "createdAt": "2025-12-26 15:44:02"
        },
        {
          "id": 139128153,
          "token": "REF_ORD123_002",
          "actionType": "refund",
          "amount": 50.0,
          "status": "success",
          "refundMode": "Back to Source",
          "createdAt": "2025-12-26 16:10:15",
          "completedAt": "2025-12-27 10:30:00"
        }
      ]
    }
  ]
}
```

### Not Found Response

```json
{
  "message": "Success",
  "status": 1,
  "result": []
}
```

## Request Parameters
### Header Authentication Parameters

<HeaderAuthentication />

### Additional Headers

| Parameter | Description | Example |
|-----------|-------------|---------|
| Content-Type<br/>`mandatory` | `string` Media type of the request body. Must be set to `application/json`. | `application/json` |
| Info-Command<br/>`optional` | `string` Set to `check_action_status` for action-level details. | `check_action_status` |

### Body Parameters

**At least one of `requestId`, `payuId`, or `tokenId` is required.**

| Parameter | Description | Example |
|-----------|-------------|---------|
| requestId<br/>`conditional` | `array` Refund request IDs from Refund Initiation response. At least one lookup field is required. | `["139128152"]` |
| payuId<br/>`conditional` | `array` PayU transaction IDs. At least one lookup field is required. | `["403993715535600711"]` |
| tokenId<br/>`conditional` | `array` Merchant refund tokens (max 23 chars). At least one lookup field is required. | `["REF_ORD123_001"]` |

## Response Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| message | `string` Response message. | `Success` |
| status | `number` `1` = success, `0` = failure. | `1` |
| result | `array` Array of refund status objects. Empty array if no matching refunds found. See [result array description](#result-array-description) for details. | - |

### result array description

| Parameter | Description | Example |
|-----------|-------------|---------|
| payuId | `number` PayU transaction ID. | `403993715535600711` |
| transactionDetails | `object` Original transaction details with fields: id, status, amount, mode. | - |
| transactionActionDetails | `array` **Refund action details**. See [transactionActionDetails array description](#transactionactiondetails-array-description) for details. | - |

### transactionActionDetails array description

| Parameter | Description | Example |
|-----------|-------------|---------|
| id | `number` **Refund action ID** (same as `requestId` from Refund Initiation). | `139128152` |
| token | `string` Refund token. | `3528998` |
| actionType | `string` Always `refund`. | `refund` |
| amount | `number` Refund amount. | `2.0` |
| status | `string` **Refund status**: `queued`, `pending`, `success`, `failed`, `cancelled`. | `queued` |
| refundMode | `string` Refund mode: `Back to Source`, `Wallet`, etc. | `Back to Source` |
| createdAt | `string` Refund initiation timestamp (yyyy-MM-dd HH:mm:ss). | `2025-12-26 15:44:02` |
| completedAt | `string` Refund completion timestamp (if completed). | `2025-12-27 10:30:00` |