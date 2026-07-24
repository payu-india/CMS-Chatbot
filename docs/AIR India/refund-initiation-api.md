---
title: Refund Initiation API
deprecated: false
hidden: true
metadata:
  robots: index
---
Initiates a refund for a captured transaction. Supports full refunds, partial refunds, closed-loop wallet (CLW) refunds, and split settlement refunds.

## Endpoint

| Environment | Base URL |
|-------------|----------|
| Test | `https://apitest.payu.in/v2/refund/` |
| Production | `https://secure.payu.in/v2/refund/` |

**Important:** The trailing slash (`/`) at the end of the endpoint is **mandatory**.

## Sample Request

### Basic Refund

```bash
curl -X POST 'https://apitest.payu.in/v2/refund/' \
  -H 'Date: Wed, 15 Jan 2025 10:30:00 GMT' \
  -H 'Authorization: hmac username="merchantKey", algorithm="sha512", headers="date", signature="abc123..."' \
  -H 'Content-Type: application/json' \
  -d '{
    "payuId": "403993715537366555",
    "amount": 100,
    "refundToken": "Refund-403993715537322",
    "source": 1
  }'
```

### With Callback URL

```bash
curl -X POST 'https://apitest.payu.in/v2/refund/' \
  -H 'Date: Wed, 15 Jan 2025 10:30:00 GMT' \
  -H 'Authorization: hmac username="merchantKey", algorithm="sha512", headers="date", signature="abc123..."' \
  -H 'Content-Type: application/json' \
  -d '{
    "payuId": "403993715537366555",
    "amount": 500,
    "refundToken": "REF_ORD123_001",
    "source": 1,
    "merchantCallbackUrl": "https://merchant.example.com/refund/callback"
  }'
```

### Closed Loop Wallet (CLW) Refund

```bash
curl -X POST 'https://apitest.payu.in/v2/refund/' \
  -H 'Date: Wed, 15 Jan 2025 10:30:00 GMT' \
  -H 'Authorization: hmac username="merchantKey", algorithm="sha512", headers="date", signature="abc123..."' \
  -H 'Content-Type: application/json' \
  -d '{
    "payuId": "403993715537366555",
    "amount": 100,
    "refundToken": "CLW_REF_001",
    "source": 1,
    "customerPhone": "9876543210",
    "refundDetail": {
      "refundType": "wallet"
    }
  }'
```

## Sample Response

### Success Response

```json
{
  "status": 1,
  "statusCode": 102,
  "message": "Refund request accepted",
  "payuId": 403993715535614124,
  "requestId": "139136064",
  "refundToken": "435239928"
}
```

### Failure Response

```json
{
  "status": 0,
  "statusCode": 106,
  "message": "Error code 106",
  "payuId": 403993715535614400,
  "refundToken": "43221129280909"
}
```

## Request Parameters
### Header Authentication Parameters

<HeaderAuthentication />


### Body Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| payuId<br/>`mandatory` | `string` **PayU transaction ID** from successful payment. | `403993715537366555` |
| token or refundToken<br/>`mandatory` | `string` **Unique refund request identifier** (max 50 characters). | `Refund-403993715537322` |
| amount<br/>`mandatory` | `number` Refund amount (supports partial refunds). | `100` |
| source<br/>`optional` | `number` Source identifier (typically `1`). | `1` |
| merchantCallbackUrl<br/>`optional` | `string` Webhook URL for refund status notifications. | `https://merchant.example.com/refund/callback` |
| customerPhone<br/>`optional` | `string` 10-digit phone number (required for CLW refunds). | `9876543210` |
| refundDetail<br/>`optional` | `object` Refund detail object for special refund types. Set `refundType` to `wallet` for CLW refunds. | `{"refundType": "wallet"}` |
| refundSplitRequest<br/>`optional` | `object` Split refund configuration with `splits` array. Each split contains merchantId and amount. | - |

## Response Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| status | `number` `1` = accepted, `0` = rejected. | `1` |
| statusCode | `number` Status code. `102` = Refund request accepted. See status codes table below. | `102` |
| message | `string` Response message. | `Refund request accepted` |
| payuId | `number` PayU transaction ID (echo of request). | `403993715535614124` |
| requestId | `string` **Refund request ID** - use to track refund status. | `139136064` |
| refundToken | `string` Refund token (echo of request). | `435239928` |
