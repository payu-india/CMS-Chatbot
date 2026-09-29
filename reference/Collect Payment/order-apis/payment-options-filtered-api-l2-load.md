---
title: Payment Options Filtered API [L2 Load]
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Payment Options Filtered (L2 Load)** API returns detailed, sub-instrument level payment configurations (such as EMI tenure options, monthly installment calculations, and eligibility flags) filtered by specific payment methods or bank codes.

Use this API after the customer selects a specific payment mode or issuing bank (e.g., selecting EMI on HDFC Bank) to fetch tenure options (3, 6, 9, 12, 18, 24 months) and verify whether the order amount is eligible.

**Environment**

|                            |                                                 |
| -------------------------- | ----------------------------------------------- |
| **Test Environment**       | `https://apitest.payu.in/v1/payment-options/l2` |
| **Production Environment** | `https://api.payu.in/v1/payment-options/l2`     |

## Request Parameters

**Mandatory Parameters**

| Parameter  | Description                                                                                          | Example                                                          |
| :--------- | :--------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------- |
| encOrderId | `String` Encrypted order identifier from the Create Order response (`transaction.encryptedOrderId`). | c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312 |

**Optional Parameters**

| Parameter      | Description                                                                                          | Example |
| :------------- | :--------------------------------------------------------------------------------------------------- | :------ |
| paymentMethods | `String` Comma-separated list of payment methods to filter the response by (e.g. `emi`, `cc`, `dc`). | emi     |
| bankCode       | `String` Specific bank code to query tenure plans for.                                               | HDFC    |

## Sample Request

```bash
curl -X GET "https://apitest.payu.in/v1/payment-options/l2?encOrderId=c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312&paymentMethods=emi&bankCode=HDFC"
```
```python
import requests
import json

url = "https://apitest.payu.in/v1/payment-options/l2?encOrderId=c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312&paymentMethods=emi&bankCode=HDFC"

headers = {
}

response = requests.get(url, headers=headers)

print(f'Status Code: {response.status_code}')
print(f'Response: {response.text}')
```
```javascript
const axios = require('axios');

const url = 'https://apitest.payu.in/v1/payment-options/l2?encOrderId=c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312&paymentMethods=emi&bankCode=HDFC';

const headers = {
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
            URL url = new URL("https://apitest.payu.in/v1/payment-options/l2?encOrderId=c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312&paymentMethods=emi&bankCode=HDFC");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
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

$url = 'https://apitest.payu.in/v1/payment-options/l2?encOrderId=c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312&paymentMethods=emi&bankCode=HDFC';

$headers = array(
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
  "paymentMethods": {
    "emi": {
      "all": {
        "dc": {
          "all": {
            "HDFC": {
              "tenureOptions": {
                "HDFCD06": {
                  "tenure": 6.0,
                  "eligibility": {
                    "status": true
                  }
                },
                "HDFCD12": {
                  "tenure": 12.0,
                  "eligibility": {
                    "status": true
                  }
                },
                "HDFCD18": {
                  "tenure": 18.0,
                  "eligibility": {
                    "status": true
                  }
                }
              },
              "eligibility": {
                "status": true
              }
            }
          },
          "hasEligible": true
        }
      }
    }
  }
}
```

## Response Parameters

| Parameter          | Description                                                                                                              | Example |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------- | :------ |
| paymentMethods.emi | `Object` Container for EMI configuration breakdown across Credit Card (`cc`) and Debit Card (`dc`).                      |         |
| tenureOptions      | `Object` Map of available tenure keys (e.g. `HDFCD06`, `HDFCD12`) with tenure duration in months and eligibility status. |         |
| hasEligible        | `Boolean` Indicates whether at least one eligible tenure option exists for the order amount.                             | true    |

