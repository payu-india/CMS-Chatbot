---
title: 'Validate Offer API '
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Validate Offer** API validates selected offer keys, promo codes, or SKU-level discounts against the order amount and specific payment method (Cards, UPI, Net Banking) before the final payment is initiated.

## Overview

Call this API when:

- The customer enters a promo code.
- The customer selects a payment method or bank where an instant discount applies.
- You want PayU to automatically evaluate and apply the best eligible offer (`autoApply: true`).

**Environment**

|                            |                                              |
| -------------------------- | -------------------------------------------- |
| **Test Environment**       | `https://apitest.payu.in/v1/offers/validate` |
| **Production Environment** | `https://api.payu.in/v1/offers/validate`     |

## Sample Request

```bash
curl -X POST "https://apitest.payu.in/v1/offers/validate" \
  -H "Content-Type: application/json" \
  -H "encOrderId: c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312" \
  -H "accessToken: FFF3D2D1-5B20-C1BC-728B-08E47A374D00" \
  -d '{
    "offerKeys": ["SPECIALOFFER@XSXedSdj1xN4"],
    "autoApply": true,
    "paymentDetail": {
      "category": "CreditCard",
      "paymentCode": "HDFC",
      "cardBin": "411111"
    }
  }'
```
```python
import requests
import json

url = "https://apitest.payu.in/v1/offers/validate"

headers = {
    "Content-Type": "application/json",
    "encOrderId": "c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312",
    "accessToken": "FFF3D2D1-5B20-C1BC-728B-08E47A374D00",
}

payload = json.dumps({
    # Add your request payload here
})

response = requests.post(url, headers=headers, data=payload)

print(f'Status Code: {response.status_code}')
print(f'Response: {response.text}')
```
```javascript
const axios = require('axios');

const url = 'https://apitest.payu.in/v1/offers/validate';

const headers = {
  'Content-Type': 'application/json',
  'encOrderId': 'c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312',
  'accessToken': 'FFF3D2D1-5B20-C1BC-728B-08E47A374D00',
};

const data = {
  // Add your request payload here
};

axios.post(url, data, { headers })
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
            URL url = new URL("https://apitest.payu.in/v1/offers/validate");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setRequestProperty("encOrderId", "c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312");
            conn.setRequestProperty("accessToken", "FFF3D2D1-5B20-C1BC-728B-08E47A374D00");
            conn.setDoOutput(true);

            String jsonInputString = "{}"; // Add JSON payload

            try (OutputStream os = conn.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }

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

$url = 'https://apitest.payu.in/v1/offers/validate';

$headers = array(
    'Content-Type: application/json',
    'encOrderId: c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312',
    'accessToken: FFF3D2D1-5B20-C1BC-728B-08E47A374D00',
);

$data = json_encode(array(
    // Add your request payload
));

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";

?>
```
## Request Parameters
### Request Headers

### Option 1: Session Token Authentication (Recommended)

| Header                                        | Description                                                     | Example                                                          |
| :-------------------------------------------- | :-------------------------------------------------------------- | :--------------------------------------------------------------- |
| <Glossary>encOrderId</Glossary> `mandatory`   | `String` Encrypted order identifier from Create Order response. | c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312 |
| <Glossary>accessToken</Glossary> `mandatory`  | `String` Session access token from Create Order response.       | FFF3D2D1-5B20-C1BC-728B-08E47A374D00                             |
| <Glossary>Content-Type</Glossary> `mandatory` | `String` Content type.                                          | application/json                                                 |

### Option 2: Order ID & Merchant Key Authentication

| Header                                                 | Description                                               | Example                              |
| :----------------------------------------------------- | :-------------------------------------------------------- | :----------------------------------- |
| <Glossary>orderId</Glossary> `mandatory`               | `String` Order ID supplied during order creation.         | ORD123446789                         |
| <Glossary>X-Credential-Username</Glossary> `mandatory` | `String` Merchant key.                                    | smsplus                              |
| <Glossary>accessToken</Glossary> `mandatory`           | `String` Session access token from Create Order response. | FFF3D2D1-5B20-C1BC-728B-08E47A374D00 |

### Body Parameters

**Mandatory Parameters**

| Parameter    | Description                                                                                          | Example                                                          |
| :----------- | :--------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------- |
| encOrderId   | `String` Encrypted order identifier from the Create Order response (`transaction.encryptedOrderId`). | c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312 |
| accessToken  | `String` Session access token from Create Order response (`transaction.accessToken`).                | FFF3D2D1-5B20-C1BC-728B-08E47A374D00                             |
| Content-Type | `String` Content type of the request body.                                                           | application/json                                                 |
| offerKeys    | `Array<String>` One or more offer keys to be evaluated.                                              | \["OFFER_KEY_1"]                                                 |
| autoApply    | `Boolean` If `true`, the offers engine auto-applies the best eligible offer for the transaction.     | true                                                             |

> **Note:** Alternatively, authenticate using Order ID & Merchant Key by passing `orderId` (the order ID supplied during order creation), `X-Credential-Username` (merchant key), and `accessToken` as headers.

**Optional Parameters**

| Parameter     | Description                                                                                                                                                                                                          | Example           |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------- |
| promocode     | `Array<String>` Promotional coupon codes entered by the customer.                                                                                                                                                    | \["SUMMERSALE20"] |
| skusDetail    | `Object` Item-level details for SKU-specific promotions. For more information, refer to [skusDetail JSON Object Fields Description](#skusdetail-json-object-fields-description).                                     | {"skus": [...]}   |
| paymentDetail | `Object` Payment instrument attributes required if validating payment-specific offers. For more information, refer to [paymentDetail JSON Object Fields Description](#paymentdetail-json-object-fields-description). | See below         |

***

## skusDetail JSON Object Fields Description

**Optional Fields**

| Field | Description                                                            | Example                                                       |
| :---- | :--------------------------------------------------------------------- | :------------------------------------------------------------ |
| skus  | `Array` List of SKU objects with `skuId`, `skuAmount`, and `quantity`. | \[{"skuId": "sku_001", "skuAmount": "500.00", "quantity": 2}] |

***

## paymentDetail JSON Object Fields Description

**Optional Fields**

| Field      | Description                                            | Example          |
| :--------- | :----------------------------------------------------- | :--------------- |
| cardNumber | `String` Plain card number (follow PCI-DSS standards). | 4111111111111111 |
| cardBin    | `String` First 6 digits of the card number.            | 411111           |
| cardHash   | `String` Hashed card reference.                        | hash_val_123     |
| cardToken  | `String` Saved tokenized card reference.               | token123         |

**Conditional Fields**

| Field       | Description                                                                                                                                  | Example    |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------- | :--------- |
| category    | `String` Mandatory if `paymentDetail` is provided. Payment instrument category (e.g. `CreditCard`, `DebitCard`, `UPI`, `NetBanking`, `EMI`). | CreditCard |
| paymentCode | `String` Bank code / payment code. Mandatory for non-card methods (e.g. `HDFC`, `ICIC`).                                                     | HDFC       |
| vpa         | `String` Virtual Payment Address (VPA). Mandatory if `category = UPI`.                                                                       | user\@upi  |

<br />

## Sample Response

```json
{
  "code": "200",
  "message": "Offer Validated Successfully",
  "status": 1,
  "result": {
    "amount": 473.0,
    "paymentCode": "CC",
    "category": "CREDITCARD",
    "isValid": true,
    "offerDiscount": {
      "offerKey": "SPECIALOFFER@XSXedSdj1xN4",
      "offerType": "INSTANT",
      "discount": 23.65,
      "discountedAmount": 449.35,
      "discountType": "PERCENTAGE"
    },
    "offerDetail": {
      "offerKey": "SPECIALOFFER@XSXedSdj1xN4",
      "title": "SPECIAL OFFER",
      "description": "Extra 5% off on all Debit Cards, Credit Cards, and UPI payments",
      "minTxnAmount": 100.0,
      "maxTxnAmount": 5000000.0,
      "status": "ACTIVE"
    },
    "totalDiscountDetail": {
      "totalCashbackDiscount": 0.0,
      "totalInstantDiscount": 23.65,
      "totalDiscountedAmount": 449.35
    },
    "autoApply": true
  }
}
```
## Response Parameters

| Parameter                             | Description                                                              | Example |
| :------------------------------------ | :----------------------------------------------------------------------- | :------ |
| code                                  | `String` Status code.                                                    | 200     |
| status                                | `Number` Status indicator (`1` for success, `0` for error).              | 1       |
| result.isValid                        | `Boolean` `true` if the offer was successfully validated and applied.    | true    |
| result.amount                         | `Number` Effective order amount before discount.                         | 473.0   |
| result.offerDiscount.discount         | `Number` Discount amount deducted.                                       | 23.65   |
| result.offerDiscount.discountedAmount | `Number` Final payable amount after deducting discount.                  | 449.35  |
| result.totalDiscountDetail            | `Object` Consolidated summary of instant discounts and cashback amounts. |         |

<br />

