---
title: Cards Element - Create Order API
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Create Order API
excerpt: Initiate checkout, register order parameters, configure callback URLs, and generate encrypted session credentials for PayU Cards Element.
api:
  method: POST
  url: <redacted URL>
---

The **Create Order API** initiates a payment session on PayU's checkout platform. When integrating PayU Cards Element, your backend server invokes this endpoint to register order items, transaction amounts, customer profiles, and return URLs. 

The API generates a secure session returning `encryptedOrderId` and `accessToken`. Your frontend application passes `encryptedOrderId` to the Cards Element JS SDK (`PayuCheckout.init()`) to mount the secure card iframe.

---

## Environment

```http
POST /v1/checkout/l1
```

| Environment | Base URL |
| :--- | :--- |
| **Sandbox / Test** | `<redacted URL>` |
| **Production** | `<redacted URL>` |

---

## Authentication & Request Signing

The Create Order API requires HMAC-SHA512 signature authentication. Every request must include an `Authorization` header containing the computed digest and a matching RFC 1123 `Date` header.

### Signature Formula

$$\text{Signature} = \text{HMAC-SHA512}\Big(\text{JSON.stringify}(body) + "|" + date + "|" + merchantSecret\Big)$$

### Header Format

```http
Authorization: hmac username="<merchantKey>", algorithm="sha512", headers="date", signature="<hexSignature>"
Date: Tue, 03 Nov 2026 15:25:00 GMT
Content-Type: application/json
```

> 📘 **HMAC Signing Rules**
> - The body string used in the hash must exactly match the serialized JSON payload transmitted over the wire.
> - The timestamp in the `Date` header must be in GMT and within ±15 minutes of PayU server time.

---

## Request Headers

| Header | Description |
| :--- | :--- |
| Authorization | _String_<br>HMAC-SHA512 authorization header formatted as:<br>`hmac username="<merchantKey>", algorithm="sha512", headers="date", signature="<signature>"` |
| Date | _String_<br>Current timestamp in RFC 1123 format (e.g. `Tue, 03 Nov 2026 15:25:00 GMT`). Must match the server clock within ±15 minutes. |
| Content-Type | _String_<br>Must be set to `application/json`. |

---

## Request Parameters

### Mandatory Parameters

| Parameter | Description |
| :--- | :--- |
| orderId | _String_<br>A unique alphanumeric identifier for the merchant transaction/order. Special characters allowed: `-`, `_`. Maximum length: 50 characters. |
| currency | _String_<br>Three-letter ISO 4217 currency code. Pass `INR` for domestic checkouts. |
| paymentSource | _String_<br>Identifier indicating the client integration channel. For Cards Element, pass `CARD_ELEMENT` or `MERCHANT_HOSTED`. |
| order | _Object_<br>Container object encapsulating order financial values, line items, and promotional offer settings. For more information, refer to [order JSON field descriptions](#order-json-object-field-descriptions)|
| callBackActions | _Object_<br>Container defining customer redirect return URLs and asynchronous server notification endpoints. [callBackActions JSON field descriptions](#callbbackactions-json-object-field-descriptions) |

### Optional Parameters

| Parameter | Description |
| :--- | :--- |
| productinfo | _String_<br>A concise description or title of the product, service, or shopping cart being purchased. Maximum length: 100 characters. |
| customer | _Object_<br>Container object holding customer identity, contact information, billing/shipping addresses, and fraud screening metadata. [customer JSON field descriptions](#customer-json-object-field-descriptions) |
| merchantCacheExpiry | _Integer_<br>Session time-to-live duration in seconds for which the order cache and access token remain valid. Default is `1200` (20 minutes). |
| additionalPaymentParams | _Object_<br>Optional container for extended payment parameters, such as standing instructions (`si_details`) for recurring card mandate registration. |
| udf1 | _String_<br>User Defined Field 1 for custom merchant tracking or internal reconciliation. Maximum length: 255 characters. |
| udf2 | _String_<br>User Defined Field 2 for custom merchant metadata. Maximum length: 255 characters. |
| udf3 | _String_<br>User Defined Field 3 for custom merchant metadata. Maximum length: 255 characters. |
| udf4 | _String_<br>User Defined Field 4 for custom merchant metadata. Maximum length: 255 characters. |
| udf5 | _String_<br>User Defined Field 5 for custom merchant metadata. Maximum length: 255 characters. |

---

### order JSON Object Field Descriptions

#### Mandatory Parameters

| Parameter | Description |
| :--- | :--- |
| amount | _Number_<br>Gross transaction amount payable by the customer in major currency units (e.g., `1500.00` for INR 1,500.00). Must be greater than zero. |

#### Optional Parameters

| Parameter | Description |
| :--- | :--- |
| skus | _Array of Objects_<br>Itemized line items in the cart. Each object captures `skuId`, `skuName`, `quantity`, `price`, etc. |
| enforcedOfferKeys | _Array of Strings_<br>List of promotional offer keys configured in the PayU dashboard to be automatically evaluated or locked to this checkout session. |
| extraCharges | _Array of Objects_<br>Additional surcharges (e.g., convenience fees, delivery charges) applied to the order. |

---

#### customer JSON Object Field Descriptions

**Mandatory Parameters**

| Parameter | Description |
| :--- | :--- |
| email | _String_<br>Customer's email address used for transaction notifications and payment receipts. |
| phone | _String_<br>Customer's 10-digit mobile phone number (without country code prefix, e.g., `9876543210`). |

**Optional Parameters**

| Parameter | Description |
| :--- | :--- |
| name | _String_<br>Full legal name of the customer or cardholder. Maximum length: 100 characters. |
| billingAddress | _Object_<br>Customer billing address container (`address1`, `address2`, `city`, `state`, `country`, `postalCode`). |
| shippingAddress | _Object_<br>Physical destination address for goods fulfillment (`address1`, `city`, `state`, `country`, `postalCode`). |
| clientDeviceInfo | _Object_<br>Client environment metadata including `ipAddress` and `userAgent` for risk and fraud scoring. |

---

#### callBackActions JSON Object Field Descriptions

**Mandatory Parameters**

| Parameter | Description |
| :--- | :--- |
| successUrl | _String_<br>HTTPS URL to which the customer is redirected upon successful 3DS authorization and payment capture. |
| failureUrl | _String_<br>HTTPS URL to which the customer is redirected if the transaction fails or is declined by the issuer. |

**Optional Parameters**

| Parameter | Description |
| :--- | :--- |
| cancelUrl | _String_<br>HTTPS URL to redirect the customer if they voluntarily abandon or cancel the payment process. |
| webhookUrl | _String_<br>HTTPS server-to-server endpoint where PayU pushes asynchronous payment status notifications and signature payloads. |

---

## Sample Request

```json
{
  "orderId": "ORD_TEST_20261103_001",
  "currency": "INR",
  "productinfo": "Pro Subscription Plan",
  "paymentSource": "CARD_ELEMENT",
  "order": {
    "amount": 1500.00,
    "skus": [
      {
        "skuId": "SKU_PRO_ANNUAL",
        "skuName": "Annual Membership",
        "quantity": 1,
        "price": 1500.00
      }
    ]
  },
  "customer": {
    "name": "Jane Doe",
    "email": "jane.doe@example.com",
    "phone": "9876543210"
  },
  "callBackActions": {
    "successUrl": "<redacted URL>",
    "failureUrl": "<redacted URL>",
    "cancelUrl": "<redacted URL>",
    "webhookUrl": "<redacted URL>"
  },
  "merchantCacheExpiry": 1200,
  "udf1": "campaign_q4"
}
```

---

## Code Examples

```bash cURL
DATE_RFC1123=$(date -u +"%a, %d %b %Y %H:%M:%S GMT")
# Compute HMAC-SHA512 signature using payload | date | secret
curl -X POST "<redacted URL>" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"COMPUTED_HMAC_SHA512\"" \
  -H "Date: ${DATE_RFC1123}" \
  -H "Content-Type: application/json" \
  -d '{
    "orderId": "ORD_TEST_20261103_001",
    "currency": "INR",
    "productinfo": "Pro Subscription Plan",
    "paymentSource": "CARD_ELEMENT",
    "order": {
      "amount": 1500.00
    },
    "customer": {
      "name": "Jane Doe",
      "email": "jane.doe@example.com",
      "phone": "9876543210"
    },
    "callBackActions": {
      "successUrl": "<redacted URL>",
      "failureUrl": "<redacted URL>"
    }
  }'
```
```javascript Node.js
const crypto = require('crypto');
const axios = require('axios');

async function createPayUOrder() {
  const merchantKey = 'YOUR_MERCHANT_KEY';
  const merchantSecret = 'YOUR_MERCHANT_SECRET';
  const endpoint = '<redacted URL>';

  const dateStr = new Date().toUTCString();
  const payload = {
    orderId: `ORD_${Date.now()}`,
    currency: 'INR',
    productinfo: 'Pro Plan',
    paymentSource: 'CARD_ELEMENT',
    order: { amount: 1500.00 },
    customer: {
      name: 'Jane Doe',
      email: 'jane.doe@example.com',
      phone: '9876543210'
    },
    callBackActions: {
      successUrl: '<redacted URL>',
      failureUrl: '<redacted URL>'
    }
  };

  const payloadString = JSON.stringify(payload);
  const signatureString = `${payloadString}|${dateStr}|${merchantSecret}`;
  const signature = crypto.createHmac('sha512', merchantSecret).update(signatureString).digest('hex');

  const response = await axios.post(endpoint, payload, {
    headers: {
      'Content-Type': 'application/json',
      'Date': dateStr,
      'Authorization': `hmac username="${merchantKey}", algorithm="sha512", headers="date", signature="${signature}"`
    }
  });

  return response.data;
}
```

---

## Sample Response

### Success Scenario

```json
{
  "status": 0,
  "message": "Order created successfully",
  "result": {
    "merchant": {
      "merchantKey": "YOUR_MERCHANT_KEY",
      "merchantName": "Merchant Enterprise"
    },
    "transaction": {
      "orderid": "ORD_TEST_20261103_001",
      "encryptedOrderId": "e4f8a3c2b1d0...[token]...7a9f",
      "accessToken": "a1b2c3d4e5f6...[token]...890a",
      "amount": 1500.00,
      "currency": "INR",
      "paymentStatus": "INITIATED"
    }
  }
}
```

## Response Parameters

| Field | Description |
| :--- | :--- |
| status | _Integer_<br>Response status indicator (`0` indicates success). |
| message | _String_<br>Descriptive outcome message. |
| result.transaction.orderid | _String_<br>Merchant order ID passed in request. |
| result.transaction.encryptedOrderId | _String_<br>Encrypted token representing the session. Pass this value as `orderId` in `PayuCheckout.init()`. |
| result.transaction.accessToken | _String_<br>Bearer authorization token for subsequent server-to-server calls. |
| result.transaction.amount | _Number_<br>Gross authorized amount. |