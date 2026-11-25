---
title: Verify payment link transaction API [New]
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
GET /partner/payment-link/verifyPayment. Query parameters read by PartnerService are order_ref_id and payment_link_id. Both are required. The response keys are order_ref_id, payment_link_id, order_status, and payments. Each payment item is PaymentLinkVerifyPaymentResponseDTO: payment_id, status, method, pg_error_message.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `GET` | `https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment?order_ref_id=ORDER_1001&payment_link_id=https://u.payu.in/PAYUID` |
| **Production** | `GET` | `https://api.payu.in/partner/payment-link/verifyPayment?order_ref_id=ORDER_1001&payment_link_id=https://u.payu.in/PAYUID` |

## Request parameters

### Request headers

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| Authorization<br />**mandatory** | `String` Partner access token. Send as Authorization Bearer token. | Bearer YOUR_ACCESS_TOKEN |

### Query parameters

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| order_ref_id<br />**mandatory** | `String` Order_ref_id | ORDER_1001 |
| payment_link_id<br />**mandatory** | `String` Payment_link_id | https://u.payu.in/PAYUID |

## Sample request

```curl
curl --location --request GET 'https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment?order_ref_id=ORDER_1001&payment_link_id=https://u.payu.in/PAYUID' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN'
```

## Response parameters

### HTTP 200

Verification result from processVerifyPaymentLinkResponse.

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| order_ref_id | `String` Order ref id | ORDER1001 |
| payment_link_id | `String` Payment link id | https://u.payu.in/PAYUID |
| order_status | `String` Order status | success |
| payments | `Array of Object` Payments | [{"payment_id": "403993715521855092", "status": "success", "method": "UPI"}] |
| payments[].payment_id<br />**optional** | `String` Payment id | 403993715521855092 |
| payments[].status<br />**optional** | `String` Status | success |
| payments[].method<br />**optional** | `String` Method | UPI |
| payments[].pg_error_message<br />**optional** | `String` Pg error message |  |

## Sample response

### HTTP 200 — success

```json
{
  "order_ref_id": "ORDER1001",
  "payment_link_id": "https://u.payu.in/PAYUID",
  "order_status": "success",
  "payments": [
    {
      "payment_id": "403993715521855092",
      "status": "success",
      "method": "UPI"
    }
  ]
}
```

### HTTP 401 — error

```json
{
  "error": "Invalid Auth token"
}
```
