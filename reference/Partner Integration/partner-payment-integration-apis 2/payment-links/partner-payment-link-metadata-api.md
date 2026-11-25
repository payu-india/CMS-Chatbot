---
title: Payment link metadata API [New]
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
GET /partner/payment-link/metadata. The query parameter PartnerService reads is payment_link. merchant_id and txnid are not read. The JSON returned to the partner is amount, currency, description, payment_link_id, payment_link_status, and expiry_time.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `GET` | `https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/metadata?payment_link=https://u.payu.in/PAYUID` |
| **Production** | `GET` | `https://api.payu.in/partner/payment-link/metadata?payment_link=https://u.payu.in/PAYUID` |

## Request parameters

### Request headers

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| Authorization<br />**mandatory** | `String` Partner access token. Send as Authorization Bearer token. | Bearer YOUR_ACCESS_TOKEN |

### Query parameters

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| payment_link<br />**mandatory** | `String` Payment link URL. Empty values raise a bad-request MetaException. | https://u.payu.in/PAYUID |

## Sample request

```curl
curl --location --request GET 'https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/metadata?payment_link=https://u.payu.in/PAYUID' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN'
```

## Response parameters

### HTTP 200

Metadata mapped by processMetaDataResponse.

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| amount | `Number` Amount | 1000.00 |
| currency | `String` Currency | INR |
| description | `String` Description | Order 1001 |
| payment_link_id | `String` Payment link id | https://u.payu.in/PAYUID |
| payment_link_status | `String` Payment link status | active |
| expiry_time | `Integer` Expiry converted to epoch by convertStringDateToEpoch. | 1735689600 |

## Sample response

### HTTP 200 — success

```json
{
  "amount": 1000.0,
  "currency": "INR",
  "description": "Order 1001",
  "payment_link_id": "https://u.payu.in/PAYUID",
  "payment_link_status": "active",
  "expiry_time": 1735689600
}
```

### HTTP 401 — error

```json
{
  "error": "Invalid Auth token"
}
```
