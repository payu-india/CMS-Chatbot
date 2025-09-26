---
title: Redeem TWID Points API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Redeem TWID Points** API is used to redeem or finalize TWID points that have previously been put on hold via the `Create Payment` API.

## Environment

|            |                                               |
| :--------- | :-------------------------------------------- |
| Production | \{\{loyalty-service-url}}/payment/v1/continue |

HTTP Method: **POST**

## Request header

<V2_paymentHeader />

## Request parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| loyaltyTxnId <br/> `mandatory` | `String` - Reference ID provided by the Loyalty-Service during the Create Payment call | `"bd1a77b6-1596-46e1-b79f-2770bcb636c7"` |
| loyaltyProvider <br/> `mandatory` | `String` - The loyalty provider identifier (e.g., TWID) | `"TWID"` |
<br />

## Response Parameters

| Parameter          | Description                                                                           | Example                                       |
| ------------------ | ------------------------------------------------------------------------------------- | --------------------------------------------- |
| status             | `String` - Outcome of the transaction (e.g., SUCCESS or validation error information) | `"SUCCESS"`                                   |
| loyaltyTxnId       | `String` - Reference ID used to confirm the redemption transaction                    | `"1821b1e2-34dd-47e3-9b54-b56b9d352a6b"`      |
| rewardPartnerRefId | `String` - A partner reference ID, which can also be used for reconciliation purposes | `"7251637276230479872"`                       |
| acsTemplate        | `String` - Reserved API field (currently unused)                                      | `null`                                        |
| issueCode          | `String` - Error code (for failure responses)                                         | `"LS404-401"`                                 |
| errorMessage       | `String` - Error description (for failure responses)                                  | `"Transaction details not present in the DB"` |
| errorType          | `String` - Type of error (for failure responses)                                      | `"VALIDATION_EXCEPTION"`                      |

## Request Example

<br />

<br />

### JSON Payload

```json
{
  "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
  "loyaltyProvider": "TWID"
}
```

<br />

### Non-seamless Integration

```bash
curl -X POST "{{loyalty-service-url}}/payment/v1/continue" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID" \
  -d '{
    "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
    "loyaltyProvider": "TWID"
  }'
```

<br />

### Seamless Integration

```bash
curl -X POST "{{loyalty-service-url}}/payment/v1/continue" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{
    "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
    "loyaltyProvider": "TWID"
  }'
```

## Sample response

### Success scenario

```json
{
  "status": "SUCCESS",
  "loyaltyTxnId": "1821b1e2-34dd-47e3-9b54-b56b9d352a6b",
  "rewardPartnerRefId": "7251637276230479872",
  "acsTemplate": null
}
```

### Failure scenario

```json
{
  "issueCode": "LS404-401",
  "errorMessage": "Transaction details not present in the DB",
  "errorType": "VALIDATION_EXCEPTION"
}
```
