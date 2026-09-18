---
title: Fetch Payment Link Metadata API
deprecated: false
hidden: true
metadata:
  robots: index
---
Retrieve payment link details including amount, currency, status, and expiry before initiating a payment.

***

## Endpoint

**GET** `/apilayer/partner/payment-link/metadata`

| Environment | URL                                                                                                                              |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------- |
| UAT         | [https://uat-api.payu.in/apilayer/partner/payment-link/metadata](https://uat-api.payu.in/apilayer/partner/payment-link/metadata) |
| Production  | ⚠️ **Contact PayU team for production API base URL**                                                                             |

***

## Authentication

Requires OAuth2 Bearer token with `partner_payment_links` scope.

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

***

## Sample Request

```bash
curl --location 'https://uat-api.payu.in/apilayer/partner/payment-link/metadata?payment_link=https://v.payu.in/PAYUMN/abc123' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...'
```

***

## Sample Response

```json
{
  "amount": 10000,
  "currency": "INR",
  "description": "Order #12345 payment",
  "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
  "payment_link_status": "PENDING",
  "expiry_time": 1735689600
}
```

***

## Request Parameters

**Mandatory Parameters**

| Parameter                 | Type & Description                                                                                                       | Example                           |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------------- | :-------------------------------- |
| `payment_link` 📍 Query   | `string` — The full PayU payment link URL. The URL host must be one of the configured PayU payment link allowed domains. | `https://v.payu.in/PAYUMN/abc123` |
| `Authorization` 📍 Header | `string` — OAuth2 Bearer token with `partner_payment_links` scope. Format: `Bearer <access_token>`                       | `Bearer eyJhbGciOiJSUzI1...`      |

**Optional Parameters**

> There are no optional parameters for this endpoint.

***

## Response Schema

| Field                 | Type    | Description                                                            |
| --------------------- | ------- | ---------------------------------------------------------------------- |
| `amount`              | number  | Payment link amount (in smallest currency unit, e.g., paise for INR)   |
| `currency`            | string  | Three-letter ISO 4217 currency code (e.g., `INR`)                      |
| `description`         | string  | Payment link description or order details                              |
| `payment_link_id`     | string  | Full PayU payment link URL                                             |
| `payment_link_status` | string  | Payment link status: `PENDING`, `CANCELLED`, `EXPIRED`, or `COMPLETED` |
| `expiry_time`         | integer | Link expiry as Unix epoch timestamp                                    |

***

## Error Codes

| HTTP Status | Error Message             | Cause                                        | Resolution                                                       |
| ----------- | ------------------------- | -------------------------------------------- | ---------------------------------------------------------------- |
| 401         | `Auth token is not valid` | Invalid or expired OAuth access token        | Generate a new access token using the OAuth Token Generation API |
| 404         | `Payment link not found`  | Payment link URL doesn't exist or is invalid | Verify the payment link URL is correct                           |
| 400         | `Payment link expired`    | Payment link has passed its expiry time      | Generate a new payment link for the customer                     |
