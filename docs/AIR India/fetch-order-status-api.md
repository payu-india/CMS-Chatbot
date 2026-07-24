---
title: Fetch Order Status API
deprecated: false
hidden: true
metadata:
  robots: index
---
Retrieves the current status of an order including payment state, SKU details, and detailed transaction information with action history (auth, capture, refund).

## Endpoint

| Environment | Base URL |
|-------------|----------|
| UAT / Test | `https://apitest.payu.in/cart/order?orderId={orderId}&actionType=verify` |
| Production | `https://api.payu.in/cart/order?orderId={orderId}&actionType=verify` |

## Sample Request

```bash
curl -X GET 'https://apitest.payu.in/cart/order?orderId=<merchant_order_id>&actionType=verify' \
  -H 'accessToken: <access_token>' \
  -H 'orderId: <encrypted_order_id>' \
  -H 'X-Credential-Username: <merchant_key>'
```

## Sample Response

```json
{
  "message": "Order Fetched Successfully",
  "status": 1,
  "traceId": "22f3d627-ac03-432b-86b0-f086143de646",
  "data": {
    "orderReferenceId": 215,
    "orderId": "6n2cj3MTXI",
    "merchantId": 2,
    "finalAmount": 500,
    "originalAmount": 500,
    "orderStatus": "PAYMENT_INITIATED",
    "skus": [
      {
        "skuId": "SKU456",
        "skuName": "Order2",
        "amountPerSku": 150,
        "finalQuantity": 2,
        "skuStatus": "PAYMENT_INITIATED"
      }
    ],
    "transactionDetails": [
      {
        "txnId": "1v5ZcS9MKA",
        "status": "PAYMENT_INITIATED",
        "mode": "CC",
        "transactionAmount": 500,
        "actions": [
          {
            "actionId": 34567876567,
            "actionType": "auth",
            "status": "success",
            "amount": 443,
            "card_number": "525303XXXXXX1234",
            "card_issuer": "AXIS BANK LIMITED",
            "three_ds_version": "2.2.0",
            "timestamp": "11/08/2025 00:07"
          },
          {
            "actionId": 34567876568,
            "actionType": "capture",
            "status": "queued",
            "amount": 300,
            "timestamp": "11/08/2025 00:02"
          }
        ]
      }
    ]
  }
}
```

## Request Parameters
## Header Authentication Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| accessToken<br/>`mandatory` | `string` Access token from the Create Order response (`transaction.accessToken`). | `<access_token>` |
| orderId<br/>`mandatory` | `string` Encrypted order ID from the Create Order response (`transaction.orderid`). This differs from the merchant order ID in the query string. | `<encrypted_order_id>` |
| X-Credential-Username<br/>`mandatory` | `string` Merchant key configured for Air India. | `<merchant_key>` |

### Query Parameters

The `orderId` query parameter is the merchant order ID. It is distinct from the encrypted `orderId` sent in the request header.

| Parameter | Description | Example |
|-----------|-------------|---------|
| orderId<br/>`mandatory` | `string` Merchant order ID passed in the query string. | `6n2cj3MTXI` |
| actionType<br/>`mandatory` | `string` Must be `verify`. | `verify` |

## Response Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| message | `string` Response message. | `Order Fetched Successfully` |
| status | `number` `1` = success, `0` = failure. | `1` |
| traceId | `string` Trace ID for debugging. | `22f3d627-ac03-432b-86b0-f086143de646` |
| data | `object` Order details. See [data object description](#data-object-description) for details. | - |

### data object description

| Parameter | Description | Example |
|-----------|-------------|---------|
| orderReferenceId | `number` Internal order reference ID. | `215` |
| orderId | `string` Merchant order ID. | `6n2cj3MTXI` |
| merchantId | `number` Merchant ID. | `2` |
| finalAmount | `number` Final order amount. | `500` |
| originalAmount | `number` Original order amount. | `500` |
| orderStatus | `string` Order status. Values: `PAYMENT_INITIATED`, `PAYMENT_SUCCESS`, `PAYMENT_FAILED`, `PAYMENT_PENDING`, `AUTHORIZED`, `CAPTURED`, `REFUNDED`, `CANCELLED`. | `PAYMENT_INITIATED` |
| skus | `array` SKU/product details. See [skus array description](#skus-array-description) for details. | - |
| addressVersion | `string` Address version identifier. | `1dedce514c0646279ade6` |
| address | `array` Customer address(es) with shippingAddress and billingAddress objects. | - |
| enforcedOfferKeys | `array` Enforced offer keys. | `["qwerty", "asdfgh"]` |
| isUpdated | `boolean` Whether order was updated. | `false` |
| transactionDetails | `array` **Transaction and action details**. See [transactionDetails array description](#transactiondetails-array-description) for details. | - |
| orderPaymentMiscDetails | `object` Miscellaneous payment details including firstname, lastname, email, phone, productinfo. | - |

### skus array description

| Parameter | Description | Example |
|-----------|-------------|---------|
| skuId | `string` SKU identifier. | `SKU456` |
| skuName | `string` SKU name. | `Order2` |
| amountPerSku | `number` Price per SKU unit. | `150` |
| originalQuantity | `number` Original quantity ordered. | `2` |
| finalQuantity | `number` Final quantity. | `2` |
| maxInventory | `number` Maximum inventory available. | `10` |
| enforcedOfferKeys | `array` Offers applied to this SKU. | `[]` |
| skuStatus | `string` SKU-level status. | `PAYMENT_INITIATED` |
| logo | `string` Product image URL. | `https://example.com/image.jpg` |

### transactionDetails array description

| Parameter | Description | Example |
|-----------|-------------|---------|
| txnId | `string` Transaction ID. | `1v5ZcS9MKA` |
| status | `string` Transaction status. | `PAYMENT_INITIATED` |
| mode | `string` Payment mode (CC, DC, NB, UPI, etc.). | `CC` |
| transactionAmount | `number` Transaction amount. | `500` |
| actions | `array` **Action history (auth, capture, refund)**. See [actions array description](#actions-array-description) for details. | - |

### actions array description

| Parameter | Description | Example |
|-----------|-------------|---------|
| actionId | `number` Unique action identifier. | `34567876567` |
| actionType | `string` Action type: `auth`, `capture`, `refund`. | `auth` |
| status | `string` Action status: `success`, `queued`, `pending`, `failed`, `bounced`. | `success` |
| amount | `number` Action amount. | `443` |
| stage | `string` Processing stage (e.g., FSR = First Settlement Report). | `FSR` |
| timestamp | `string` Action timestamp. | `11/08/2025 00:07` |
| acquirer_mid | `number` Acquirer merchant ID (for auth actions). | `542515` |
| approval_code | `string` Approval code from bank. | `NA` |
| authentication_method | `string` Authentication method (e.g., `3DS`). | `3DS` |
| bin | `number` Bank Identification Number (first 6 digits of card). | `525303` |
| card_issuer | `string` Issuing bank name. | `AXIS BANK LIMITED` |
| card_number | `string` Masked card number. | `525303XXXXXX1234` |
| cvv_status | `string` CVV verification status. | `A` |
| eci | `number` Electronic Commerce Indicator. | `2` |
| three_ds_version | `string` 3DS version used. | `2.2.0` |
| fraud_result | `string` Fraud check result. | `Accept` |
| fraud_score | `number` Fraud risk score. | `-8626` |
| document_number | `string` Document/ticket number (for capture actions). | `9.82177E+11` |
| documents_type | `string` Document type. | `Ticket` |