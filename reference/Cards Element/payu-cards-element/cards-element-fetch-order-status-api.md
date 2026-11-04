---
title: Cards Element - Fetch Order Status API
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Fetch Order Status API
excerpt: Retrieve transaction status, payment amounts, and order state for order reconciliation.
api:
  method: GET
  url: <redacted URL>
---

The **Fetch Order Status API** allows merchant systems to query the current lifecycle state of an order placed via PayU Cards Element. Use this endpoint for server-side verification, order fulfillment confirmation, and nightly payment reconciliation.

---

## Endpoint & Environments

```http
GET /cart/order?orderId={orderId}
```

| Environment | Base URL |
| :--- | :--- |
| **Sandbox / Test** | `<redacted URL>` |
| **Production** | `<redacted URL>` |

---

## Authentication & Request Signing

Like the Create Order API, this endpoint requires HMAC-SHA512 authentication using your merchant credentials.

### Header Format

```http
Authorization: hmac username="<merchantKey>", algorithm="sha512", headers="date", signature="<hexSignature>"
Date: Tue, 03 Nov 2026 15:25:00 GMT
```

### Mandatory Headers

| Header | Description |
| :--- | :--- |
| Authorization | _String_<br>HMAC-SHA512 authorization header formatted as:<br>`hmac username="<merchantKey>", algorithm="sha512", headers="date", signature="<signature>"` |
| Date | _String_<br>Current timestamp in RFC 1123 format (e.g. `Tue, 03 Nov 2026 15:25:00 GMT`). Must match the server clock within ±15 minutes. |

---

## Query Parameters

### Mandatory Parameters

| Parameter | Description |
| :--- | :--- |
| orderId | _String_<br>The merchant order identifier passed during order creation (`POST /v1/checkout/l1`). |

---

## Sample Request

```bash cURL
DATE_RFC1123=$(date -u +"%a, %d %b %Y %H:%M:%S GMT")
curl -X GET "<redacted URL>" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"COMPUTED_HMAC_SHA512\"" \
  -H "Date: ${DATE_RFC1123}"
```

---

## Response Structure

### Sample Success Response

```json
{
  "status": 0,
  "message": "Order details retrieved successfully",
  "result": {
    "orderReferenceId": "18492048291",
    "orderId": "ORD_TEST_20261103_001",
    "finalAmount": 1500.00,
    "originalAmount": 1500.00,
    "orderStatus": "CAPTURED",
    "skus": [
      {
        "skuId": "SKU_PRO_ANNUAL",
        "skuName": "Annual Membership",
        "quantity": 1,
        "price": 1500.00
      }
    ]
  }
}
```

### Response Parameters

| Field | Description |
| :--- | :--- |
| status | _Integer_<br>Response status code (`0` indicates success). |
| message | _String_<br>Descriptive outcome message. |
| result.orderReferenceId | _String_<br>PayU internal transaction reference identifier. |
| result.orderId | _String_<br>Merchant order ID passed during checkout initiation. |
| result.finalAmount | _Number_<br>Net authorized/captured amount after promotional offers or convenience fees. |
| result.originalAmount | _Number_<br>Gross amount initiated prior to offer calculations. |
| result.orderStatus | _String_<br>Current lifecycle state of the transaction. See table below. |

---

## Order Status State Mapping

| Status Code | Description | Recommended Merchant Action |
| :--- | :--- | :--- |
| `PAYMENT_INITIATED` | Order session initiated; customer currently on checkout page or in 3DS authentication. | Wait for callback or webhook notification. |
| `CAPTURED` | Payment successfully authorized and captured by the card issuer. | Mark order as paid and fulfill services/goods. |
| `FAILED` | Payment declined by card issuer or customer authentication failed. | Prompt customer to retry with another card or payment method. |
| `CANCELLED` | Customer explicitly abandoned checkout on the payment page. | Release reserved inventory or update cart status. |
