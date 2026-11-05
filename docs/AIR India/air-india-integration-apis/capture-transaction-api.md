---
title: Capture Transaction API
deprecated: false
hidden: true
metadata:
  robots: index
---
Captures an authorized (pre-authorized) transaction. Used after a successful pre-auth to collect the funds. Supports full and partial captures.

## Endpoint

| Environment | Base URL |
|-------------|----------|
| Test | `https://test.payu.in/v1/transaction/capture` |
| Production | `https://info.payu.in/v1/transaction/capture` |

## Sample Request

```bash
curl -X POST 'https://test.payu.in/v1/transaction/capture' \
  -H 'Date: Wed, 15 Jan 2025 10:30:00 GMT' \
  -H 'Authorization: hmac username="merchantKey", algorithm="sha512", headers="date", signature="abc123..."' \
  -H 'Content-Type: application/json' \
  -d '{
    "amount": 1000.50,
    "payuId": "22919645299",
    "referenceId": "5ea2ed7ac7756f12a0a1"
  }'
```

## Sample Response

### Success Response

```json
{
  "status": 1,
  "requestId": "139128152"
}
```

### Failure Response

```json
{
  "status": 0,
  "message": "Transaction not found",
  "error_code": "TXN_NOT_FOUND"
}
```

## Request Parameters
## Header Authentication Parameters

<HeaderAuthentication />

### Body Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| amount<br/>`mandatory` | `number` Amount to capture (supports partial capture). | `1000.50` |
| payuId<br/>`conditional` | `string` **PayU transaction ID** from authorization response. Exactly one of `payuId` or `txnId` is required. | `22919645299` |
| txnId<br/>`conditional` | `string` **Merchant transaction ID** used during authorization. Exactly one of `payuId` or `txnId` is required. | `77626dhjhabc` |
| referenceId<br/>`mandatory` | `string` Merchant reference ID for this capture request. | `5ea2ed7ac7756f12a0a1` |

## Response Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| status | `number` `1` = success, `0` = failure. | `1` |
| requestId | `string` **Unique PayU capture request ID** - use for tracking. | `139128152` |
| message | `string` Error message (only on failure). | `Transaction not found` |
| error_code | `string` Error code (only on failure). | `TXN_NOT_FOUND` |
