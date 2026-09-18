---
title: Initiate Payment Link API - Partner Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
Initiate a PayU payment using a pre-generated payment link. Supports both Hosted Payment Page (HPP) and UPI Intent flows.

***

## Endpoint

**POST** `/apilayer/partner/payment-link/payment`

| Environment | URL                                                                                                                            |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------ |
| UAT         | [https://uat-api.payu.in/apilayer/partner/payment-link/payment](https://uat-api.payu.in/apilayer/partner/payment-link/payment) |
| Production  | \\<Require Info>                                                                                                               |

***

## Authentication

Requires OAuth2 Bearer token with `partner_payment_links` scope.

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

***

## Sample Request

**Hosted Checkout (HPP) Flow**

```bash
curl --location 'https://uat-api.payu.in/apilayer/partner/payment-link/payment' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...' \
--header 'Content-Type: application/json' \
--data '{
  "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
  "phone_number": "9876543210",
  "redirect_url": "https://yourpartnersite.com/payment/callback",
  "amount": 10000,
  "currency": "INR",
  "description": "Order #12345 payment",
  "payment_link_status": "PENDING",
  "expiry_time": 1735689600
}'
```

***

## Sample Response

**HPP Flow Response**

```json
{
  "order_ref_id": "ORD_PARTNER_20240101_001",
  "hpp_url": "https://secure.payu.in/checkout?token=abc123xyz456",
  "expiry_time": 1735689600
}
```

**UPI Intent Flow Response**

```json
{
  "order_ref_id": "ORD_PARTNER_20240101_002",
  "upi_intent_url": "upi://pay?pa=payu@icici&pn=PayU&am=100.00&tr=ORD_PARTNER_20240101_002",
  "expiry_time": 1735689600
}
```

***

## Request Parameters
### Mandatory Parameters

**Header Parameters**

| Parameter                     | Type & Description                                                | Example                           |
| :---------------------------- | :---------------------------------------------------------------- | :-------------------------------- |
| `Authorization Bearer Token`  | `string` — OAuth2 Bearer token with `partner_payment_links` scope | `Bearer eyJhbGciOi...`            |
| `Content-Type`                | `string` — Must be `application/json`                             | `application/json`                |
| `payment_link_id`             | `string` — Full PayU payment link URL from metadata response      | `https://v.payu.in/PAYUMN/abc123` |

**Body Parameters**

| Parameter              | Type & Description                                  | Example                |
| :--------------------- | :-------------------------------------------------- | :--------------------- |
| `phone_number`         | `string` — Customer phone number (5-16 digits only) | `9876543210`           |
| `amount`               | `number` — Payment amount in smallest currency unit | `10000`                |
| `currency`             | `string` — Three-letter ISO 4217 currency code      | `INR`                  |
| `description`          | `string` — Payment description from metadata        | `Order #12345 payment` |
| `payment_link_status`  | `string` — Must be `PENDING` from metadata          | `PENDING`              |
| `expiry_time`          | `integer` — Unix timestamp from metadata            | `1718000000`           |

### Conditional Parameters \[Body]**

| Parameter       | Type & Description                                                                                    | Example                        |
| :-------------- | :---------------------------------------------------------------------------------------------------- | :----------------------------- |
| `redirect_url`  | `string` — Required for HPP flow; omit for UPI Intent flow. Partner redirect URL for hosted checkout. | `https://partner.com/callback` |

***

## Response Schema

| Field            | Type    | Description                                        |
| ---------------- | ------- | -------------------------------------------------- |
| `order_ref_id`   | string  | PayU transaction reference ID for tracking         |
| `hpp_url`        | string  | Hosted checkout URL (present for HPP flow)         |
| `upi_intent_url` | string  | UPI Intent deep link (present for UPI Intent flow) |
| `expiry_time`    | integer | Transaction expiry as Unix epoch timestamp         |

***

## Error Codes

| HTTP Status | Error Message             | Cause                                   | Resolution                  |
| ----------- | ------------------------- | --------------------------------------- | --------------------------- |
| 401         | `Auth token is not valid` | Invalid or expired OAuth access token   | Generate a new access token |
| 404         | `Payment link not found`  | Payment link URL doesn't exist          | Verify the payment link URL |
| 400         | `Payment link expired`    | Payment link has passed its expiry time | Request a new payment link  |
| 400         | `Invalid phone number`    | Phone number format is incorrect        | Use 5-16 digits only        |
