---
title: Fetch Quick Pay Options API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Fetch Quick Pay Options** API retrieves previously saved payment methods (such as tokenized credit/debit cards and recent UPI IDs) linked to the customer's phone number or account.

Display these instruments prominently at the top of your checkout interface ("Quick Pay" / "Saved Options") to minimize customer friction and boost transaction conversion rates.

**Environment**

|                            |                                            |
| -------------------------- | ------------------------------------------ |
| **Test Environment**       | `https://apitest.payu.in/v1/saved-options` |
| **Production Environment** | `https://api.payu.in/v1/saved-options`     |
## Sample Request

```bash
curl -X GET "https://apitest.payu.in/v1/saved-options" \
  -H "encOrderId: c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312" \
  -H "accessToken: FFF3D2D1-5B20-C1BC-728B-08E47A374D00"
```
```python
import requests
import json

url = "https://apitest.payu.in/v1/saved-options"

headers = {
    "encOrderId": "c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312",
    "accessToken": "FFF3D2D1-5B20-C1BC-728B-08E47A374D00",
}

response = requests.get(url, headers=headers)

print(f'Status Code: {response.status_code}')
print(f'Response: {response.text}')
```
```javascript
const axios = require('axios');

const url = 'https://apitest.payu.in/v1/saved-options';

const headers = {
  'encOrderId': 'c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312',
  'accessToken': 'FFF3D2D1-5B20-C1BC-728B-08E47A374D00',
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
            URL url = new URL("https://apitest.payu.in/v1/saved-options");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("encOrderId", "c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312");
            conn.setRequestProperty("accessToken", "FFF3D2D1-5B20-C1BC-728B-08E47A374D00");
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

$url = 'https://apitest.payu.in/v1/saved-options';

$headers = array(
    'encOrderId: c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312',
    'accessToken: FFF3D2D1-5B20-C1BC-728B-08E47A374D00',
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

## Request Parameters

**Mandatory Parameters**

| Parameter   | Description                                                                                          | Example                                                          |
| :---------- | :--------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------- |
| encOrderId  | `String` Encrypted order identifier from the Create Order response (`transaction.encryptedOrderId`). | c422540c33ef9f12<br/>59f15f7b9164<br/>69b7227dc1d41<br/>a767965368854<br/>74ddadf312 |
| accessToken | `String` Session access token from the Create Order response (`transaction.accessToken`).            | FFF3D2D1-5B20-C1BC-728B-08E47A374D00                             |

> **Note:** Alternatively, authenticate using Order ID & Merchant Key by passing `orderId` (the order ID supplied during order creation), `X-Credential-Username` (merchant key), and `accessToken` as headers.

## Sample Response

```json
{
  "status": true,
  "authenticated": true,
  "globalVaultPhoneNumber": "9876543210",
  "payment_options": {
    "CC": [
      {
        "pgTitle": "HDFC Bank Credit Card",
        "pgDetails": "**** **** **** 1234",
        "ibiboCode": "HDFC",
        "cvvRequired": true,
        "paymentMode": "CC"
      }
    ],
    "DC": [],
    "NB": [],
    "UPI": [
      {
        "pgDetails": "user@okhdfcbank",
        "paymentMode": "UPI"
      }
    ]
  },
  "pg_recency": [
    101,
    201,
    301
  ]
}
```

## Response Parameters

| Parameter               | Description                                                                                                                                                       | Example          |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------- |
| authenticated           | `Boolean` Indicates whether the customer is authenticated against the PayU global vault.                                                                          | true             |
| globalVaultPhoneNumber  | `String` Customer phone number registered with the vault.                                                                                                         | 9876543210       |
| payment_options.CC / DC | `Array` List of tokenized card objects containing masked card number (`pgDetails`), card title (`pgTitle`), bank code (`ibiboCode`), and `cvvRequired` indicator. |                  |
| payment_options.UPI     | `Array` List of saved UPI VPAs previously used by the customer.                                                                                                   |                  |
| pg_recency              | `Array<Number>` Recency sorting ranking for prioritizing preferred payment options.                                                                               | \[101, 201, 301] |

<br />

##