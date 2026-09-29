---
title: 'Fetch Offer API '
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Fetch Offer** API retrieves all active and applicable offers, instant discounts, cashbacks, and coupon codes available for an order created via the Create Order API.

Use this API to display promotional banners, payment mode-specific savings (such as bank discounts or card brand offers), and available coupon inputs to the customer during checkout.

**Environment**

|                            |                                     |
| -------------------------- | ----------------------------------- |
| **Test Environment**       | `https://apitest.payu.in/v1/offers` |
| **Production Environment** | `https://api.payu.in/v1/offers`     |
## Sample Request

```bash
curl -X POST "https://apitest.payu.in/v1/offers" \
  -H "Content-Type: application/json" \
  -H "encOrderId: c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312" \
  -H "accessToken: FFF3D2D1-5B20-C1BC-728B-08E47A374D00" \
  -d '{}'
```
```python
import requests
import json

url = "https://apitest.payu.in/v1/offers"

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

const url = 'https://apitest.payu.in/v1/offers';

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
            URL url = new URL("https://apitest.payu.in/v1/offers");
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

$url = 'https://apitest.payu.in/v1/offers';

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

You can authenticate using either the session tokens or merchant credential headers:

#### Option 1: Session Token Authentication (Recommended)

| Header                                        | Description                                                                                          | Example                                                          |
| :-------------------------------------------- | :--------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------- |
| <Glossary>encOrderId</Glossary> `mandatory`   | `String` Encrypted order identifier from the Create Order response (`transaction.encryptedOrderId`). | c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312 |
| <Glossary>accessToken</Glossary> `mandatory`  | `String` Session access token from Create Order response (`transaction.accessToken`).                | FFF3D2D1-5B20-C1BC-728B-08E47A374D00                             |
| <Glossary>Content-Type</Glossary> `mandatory` | `String` Content type.                                                                               | application/json                                                 |

#### Option 2: Order ID & Merchant Key Authentication

| Header                                                 | Description                                               | Example                              |
| :----------------------------------------------------- | :-------------------------------------------------------- | :----------------------------------- |
| <Glossary>orderId</Glossary> `mandatory`               | `String` Order ID supplied during order creation.         | ORD123446789                         |
| <Glossary>X-Credential-Username</Glossary> `mandatory` | `String` Merchant key.                                    | smsplus                              |
| <Glossary>accessToken</Glossary> `mandatory`           | `String` Session access token from Create Order response. | FFF3D2D1-5B20-C1BC-728B-08E47A374D00 |

## Body Parameters

**Mandatory Parameters**

| Parameter    | Description                                                                                          | Example                                                          |
| :----------- | :--------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------- |
| encOrderId   | `String` Encrypted order identifier from the Create Order response (`transaction.encryptedOrderId`). | c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312 |
| accessToken  | `String` Session access token from Create Order response (`transaction.accessToken`).                | FFF3D2D1-5B20-C1BC-728B-08E47A374D00                             |
| Content-Type | `String` Content type of the request body.                                                           | application/json                                                 |

> **Note:** Alternatively, authenticate using Order ID & Merchant Key by passing `orderId` (the order ID supplied during order creation), `X-Credential-Username` (merchant key), and `accessToken` as headers.

**Optional Parameters**

| Parameter    | Description                                                                                                      | Example |
| :----------- | :--------------------------------------------------------------------------------------------------------------- | :------ |
| Request Body | `Object` Can be sent as an empty JSON object `{}`. No additional body parameters are required for this endpoint. | {}      |


## Sample Response

```json
{
  "code": "SUCCESS",
  "message": "Offers retrieved successfully",
  "status": 200,
  "result": {
    "clientId": "merchant123",
    "mid": "123456",
    "amount": 1000.0,
    "couponsAvailable": true,
    "isUserPersonalizedOffersAvailable": true,
    "offers": [
      {
        "offerKey": "FLAT10CC",
        "type": "INSTANT_DISCOUNT",
        "title": "10% Off on Credit Cards",
        "description": "Get 10% instant discount on all credit card payments above Rs 500",
        "minTxnAmount": "500.00",
        "maxTxnAmount": "10000.00",
        "offerType": "INSTANT",
        "discountDetail": {
          "discountType": "PERCENTAGE",
          "discountPercentage": 10.0,
          "maxDiscount": 1000.0
        },
        "cc": [
          {
            "title": "HDFC Credit Card",
            "paymentCode": "HDFC",
            "networks": [
              "VISA",
              "MASTERCARD"
            ],
            "banks": [
              "HDFC"
            ]
          }
        ]
      }
    ]
  }
}
```
## Response Parameters

| Parameter                                | Description                                                                                                                                               | Example                       |
| :--------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------- |
| code                                     | `String` Status code (e.g. `SUCCESS`).                                                                                                                    | SUCCESS                       |
| message                                  | `String` Status description.                                                                                                                              | Offers retrieved successfully |
| result.amount                            | `Number` Base order amount eligible for offer calculation.                                                                                                | 1000.00                       |
| result.couponsAvailable                  | `Boolean` Indicates whether manual coupon codes are configured for the merchant.                                                                          | true                          |
| result.isUserPersonalizedOffersAvailable | `Boolean` Indicates if targeted user offers exist for this customer.                                                                                      | true                          |
| result.offers                            | `Array` List of applicable offer objects including `offerKey`, `title`, `description`, `minTxnAmount`, `maxTxnAmount`, `offerType`, and `discountDetail`. |                               |
| <Glossary>result.amount</Glossary>                            | `Number`  | Base order amount eligible for offer calculation.                                                                                                 |
| <Glossary>result.couponsAvailable</Glossary>                  | `Boolean` | Indicates whether manual coupon codes are configured for the merchant.                                                                            |
| <Glossary>result.isUserPersonalizedOffersAvailable</Glossary> | `Boolean` | Indicates if targeted user offers exist for this customer.                                                                                        |
| <Glossary>result.offers</Glossary>                            | `Array`   | List of applicable offer objects including `offerKey`, `title`, `description`, `minTxnAmount`, `maxTxnAmount`, `offerType`, and `discountDetail`. |