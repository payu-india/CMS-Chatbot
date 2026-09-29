---
title: 'Fetch Order Status API '
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Fetch Order Status** API retrieves the real-time status of an order, including all payment attempts, transaction IDs, SKU fulfillment state, and callback/webhook delivery URLs.

Use this API:

- To verify payment status on your order confirmation page.
- As a server-to-server reconciliation check when webhooks or browser redirects are delayed.
- To inspect all payment attempts and intermediate states for an order.

**Environment**

|                            |                                      |
| -------------------------- | ------------------------------------ |
| **Test Environment**       | `https://apitest.payu.in/cart/order` |
| **Production Environment** | `https://api.payu.in/cart/order`     |

## Request Parameters
### Request Headers

| Header                                         | Description                                                                                                                             | Example                                                                      |
| :--------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| <Glossary>Date</Glossary> `mandatory`          | `String` Current date and time in RFC 1123 format.                                                                                      | Wed, 15 Jan 2025 10:30:00 GMT                                                |
| <Glossary>Authorization</Glossary> `mandatory` | `String` HMAC SHA-512 signature header format: `hmac username="{merchantKey}", algorithm="sha512", headers="date", signature="{hash}"`. | hmac username="smsplus", algorithm="sha512", headers="date", signature="..." |

### Request Parameters

**Mandatory Parameters**

| Parameter     | Description                                                                                                                                                                                                                                                 | Example                                                                          |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------- |
| Date          | `String` Current date and time in RFC 1123 format (EEE, dd MMM yyyy HH:mm:ss 'GMT').                                                                                                                                                                        | Wed, 15 Jan 2025 10:30:00 GMT                                                    |
| Authorization | `String` HMAC SHA-512 signature header in the format: `hmac username="{merchantKey}", algorithm="sha512", headers="date", signature="{hash}"`. The signature is computed as HMAC-SHA512 over the signed header string using the merchant secret as the key. | hmac username="smsplus", algorithm="sha512", headers="date", signature="d260..." |
| orderId       | `String` The unique merchant order ID provided during order creation.                                                                                                                                                                                       | RDU2a6PSKX                                                                       |
## Sample Request

```bash
curl -X GET "https://apitest.payu.in/cart/order?orderId=RDU2a6PSKX" \
  -H "Date: Wed, 15 Jan 2025 10:30:00 GMT" \
  -H "Authorization: hmac username=\"smsplus\", algorithm=\"sha512\", headers=\"date\", signature=\"d260...\""
```
```python
import requests
import json

url = "https://apitest.payu.in/cart/order?orderId=RDU2a6PSKX"

headers = {
    "Date": "Wed, 15 Jan 2025 10:30:00 GMT",
    "Authorization": "hmac username=\",
}

response = requests.get(url, headers=headers)

print(f'Status Code: {response.status_code}')
print(f'Response: {response.text}')
```
```javascript
const axios = require('axios');

const url = 'https://apitest.payu.in/cart/order?orderId=RDU2a6PSKX';

const headers = {
  'Date': 'Wed, 15 Jan 2025 10:30:00 GMT',
  'Authorization': 'hmac username=\',
};

axios.get(url, { headers })
  .then(response => {
    console.log('Status Code:', response.status);
    console.log('Response:', response.data);
  })
  .catch(error => {
    console.error('Error:', error.response ? error.response.data : error.message);
  });
```
```java
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;

public class PayUAPIRequest {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://apitest.payu.in/cart/order?orderId=RDU2a6PSKX");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Date", "Wed, 15 Jan 2025 10:30:00 GMT");
            conn.setRequestProperty("Authorization", "hmac username=\");
            int responseCode = conn.getResponseCode();
            System.out.println("Status Code: " + responseCode);

            BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String inputLine;
            StringBuilder response = new StringBuilder();

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();

            System.out.println("Response: " + response.toString());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```
```php
<?php

$url = 'https://apitest.payu.in/cart/order?orderId=RDU2a6PSKX';

$headers = array(
    'Date: Wed, 15 Jan 2025 10:30:00 GMT',
    'Authorization: hmac username=\',
);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";

?>
```

<br />

## Sample Response

```json
{
  "message": "Order Fetched Successfully",
  "status": 1,
  "traceId": "3ee1f3dc-c1a1-490b-a9e4-3ab8a60ed94c",
  "data": {
    "orderReferenceId": 167,
    "orderId": "RDU2a6PSKX",
    "merchantId": 180012,
    "txnId": "jyo1SC3Aql",
    "finalAmount": 550.0,
    "originalAmount": 500.0,
    "cartAmount": 500.0,
    "orderStatus": "PAYMENT_INITIATED",
    "skus": [
      {
        "skuId": "124",
        "skuName": "Order2",
        "amountPerSku": 300.0,
        "originalQuantity": 1,
        "finalQuantity": 1,
        "maxInventory": 22,
        "enforcedOfferKeys": [],
        "skuStatus": "PAYMENT_INITIATED",
        "logo": "https://www.jhajistore.com/cdn/shop/files/SpicyGreenChilli_500gm_800x.jpg?v82608493"
      },
      {
        "skuId": "123",
        "skuName": "Order1",
        "amountPerSku": 100.0,
        "originalQuantity": 2,
        "finalQuantity": 2,
        "maxInventory": 10,
        "enforcedOfferKeys": [],
        "skuStatus": "PAYMENT_INITIATED",
        "logo": "https://www.jhajistore.com/cdn/shop/products/DSC0064_720x.jpg?v57574131"
      }
    ],
    "addressVersion": "193ac16c267c585d4139ab",
    "address": [
      {
        "shippingAddress": {
          "id": 26,
          "name": "Shashi Kumar Gupta",
          "email": "skgtouch@gmail.com",
          "addressLine": "Test22",
          "addressLine2": "Lalpur, Pandeypur",
          "addressPhoneNumber": "9458706597",
          "pincode": 221002,
          "city": "Varanasi",
          "state": "Uttar Pradesh",
          "tag": "work",
          "isDefault": true,
          "isCodAvailable": true,
          "version": "193ac16c267c585d4139ab"
        },
        "consent": false
      }
    ],
    "enforcedOfferKeys": [],
    "extraCharges": {
      "shippingCharges": 20.0,
      "codFee": 40.0,
      "otherCharges": 10.0,
      "taxInfo": {
        "total": 20.0,
        "breakup": {
          "CGST": 10.0,
          "SGST": 10.0
        }
      },
      "carrierCode": "Express Delivery",
      "methodCode": "Express Delivery"
    },
    "isUpdated": false,
    "platform": "WooCommerce",
    "transactionDetails": [
      {
        "txnId": "jyo1SC3Aql",
        "referenceId": "ref-cart-001",
        "payuId": "613345778913146240",
        "status": "success",
        "mode": "CC",
        "transactionAmount": 550.0,
        "action_id": "jyo1SC3Aql",
        "action_type": "auth",
        "stage": "AUTH_C",
        "payment_record_id_pri": "jyo1SC3Aql",
        "order_id": "RDU2a6PSKX",
        "amount": 550.0,
        "currency": "INR",
        "method_of_payment": "Card"
      }
    ],
    "orderPaymentMiscDetails": {
      "key": "KOEfPI",
      "firstname": "Payu-Admin",
      "lastname": "",
      "email": "test@example.com",
      "phone": "9087650461",
      "productinfo": "Product Info",
      "surl": "https://pp75admin.payu.in/test_response",
      "furl": "https://pp75admin.payu.in/test_response",
      "isCheckoutExpress": true,
      "partnerWebhookSuccess": "http://abc.com",
      "partnerWebhookFailure": "http://abc.com",
      "udf4": "udf4",
      "udf5": "udf5"
    }
  }
}
## Response Parameters

| Parameter                    | Description                                                                                                                            | Example           |
| :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- | :---------------- |
| status                       | `Number` Response status indicator (`1` for success).                                                                                  | 1                 |
| data.orderId                 | `String` Merchant order ID.                                                                                                            | RDU2a6PSKX        |
| data.orderStatus             | `String` Overall order state (e.g., `PAYMENT_INITIATED`, `SUCCESS`, `FAILED`).                                                         | PAYMENT_INITIATED |
| data.finalAmount             | `Number` Final charged amount for the order.                                                                                           | 550.00            |
| data.txnId                   | `String` Latest transaction ID associated with this order.                                                                             | jyo1SC3Aql        |
| data.transactionDetails      | `Array` Chronological list of all payment attempts (newest first) with attempt status, gateway reference ID, mode, and charged amount. |                   |
| data.orderPaymentMiscDetails | `Object` Contains merchant key, customer details, return URLs, and effective partner webhook URLs.                                     |                   |
```