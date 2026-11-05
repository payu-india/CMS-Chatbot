---
title: Payment Options API
deprecated: false
hidden: true
metadata:
  robots: index
---
Returns available payment methods for the order at L1 (checkout load). Used to render payment options on the checkout page with configuration details for each payment method.

## Endpoint

| Environment | Base URL |
|-------------|----------|
| UAT / Test | `https://apitest.payu.in/v1/payment-options?encOrderId={encOrderId}` |
| Production | `https://api.payu.in/v1/payment-options?encOrderId={encOrderId}` |

## Sample Request

```bash
curl -X POST 'https://apitest.payu.in/v1/payment-options?encOrderId=<encrypted_order_id>' \
  -H 'accessToken: <access_token>' \
  -H 'orderId: <encrypted_order_id>' \
  -H 'X-Credential-Username: <merchant_key>'
```

## Sample Response

```json
{
  "paymentMethods": {
    "emi": {
      "cc": {
        "all": [
          {
            "title": "ICICI Bank",
            "bank_code": "ICIC",
            "minimum_amount": 1500,
            "has_nocostemi": false
          }
        ],
        "top": ["BARB", "UTIB", "ICIC"]
      }
    },
    "nb": {
      "all": [
        {
          "title": "HDFC Bank",
          "ibibo_code": "HDFB",
          "up_status": 1
        }
      ],
      "top": ["HDFB", "ICIB", "SBIN"]
    },
    "upi": {
      "recommendations": ["googlepay", "phonepe", "paytm"]
    },
    "cc": {
      "all": [
        {
          "ibibo_code": "CC",
          "category": "CreditCard"
        }
      ]
    },
    "dc": {
      "all": [
        {
          "ibibo_code": "VISA",
          "category": "DebitCard"
        }
      ]
    }
  },
  "downInfo": {
    "downIssuingBanks": []
  },
  "broker": "PAYU"
}
```

## Request Parameters
### Header Authentication Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| accessToken<br/>`mandatory` | `string` Access token from the Create Order response (`transaction.accessToken`). | `<access_token>` |
| orderId<br/>`mandatory` | `string` Encrypted order ID from the Create Order response (`transaction.orderid`). | `<encrypted_order_id>` |
| X-Credential-Username<br/>`mandatory` | `string` Merchant key configured for Air India. | `<merchant_key>` |

### Query Parameters

Query parameters in the URL:

| Parameter | Description | Example |
|-----------|-------------|---------|
| encOrderId<br/>`mandatory` | `string` Encrypted order ID (from Create Order response `transaction.orderid`). | `yiekt` |

## Response Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| paymentMethods | `object` Available payment methods. See [paymentMethods object description](#paymentmethods-object-description) for details. | - |
| downInfo | `object` Information about payment methods/banks currently unavailable. | - |
| downInfo.downIssuingBanks | `array` List of bank codes that are currently down. | `[]` |
| broker | `string` Payment broker identifier. | `PAYU` |
| order | `object` Order details (amount, productinfo, orderId). | - |
| transaction | `object` Transaction details (accessToken, orderid, txnId). | - |
| customer | `object` Customer information. | - |
| bankLogosUrl | `string` Base URL for bank logo images. | `https://web-assets.payu.in/web/images/assets/bankLogo/` |

### paymentMethods object description

| Parameter | Description | Example |
|-----------|-------------|---------|
| emi | `object` EMI payment options with nested objects: `cc` (credit card EMI), `dc` (debit card EMI), `other` (other EMI providers like Bajaj). Each contains `all` array and `top` array. | - |
| nb | `object` Net Banking options. Contains `all` array (all available banks) and `top` array (recommended banks). Each bank has: title, ibibo_code, up_status (1=up, 0=down). | - |
| wallet | `object` Wallet options. Contains `all` array and `recommendations` array. Each wallet has: title, ibibo_code. | - |
| upi | `object` UPI options. Contains `upil2Apps` (UPI app configurations), `upil2AppsOrder` (display order), `recommendations`, and `all` array. | - |
| cc | `object` Credit card options. Contains `all` array with card networks (CC, RUPAYCC). | - |
| dc | `object` Debit card options. Contains `all` array with card networks (MAST, VISA, RUPAY). | - |
| standinginstruction | `object` Standing instruction/mandate options. Contains `all` array with bank codes. | - |
| codnew | `object` Cash on Delivery options. Contains `all` array. | - |
| RD | `object` Rewards/other payment options. Contains `all` array. | - |
