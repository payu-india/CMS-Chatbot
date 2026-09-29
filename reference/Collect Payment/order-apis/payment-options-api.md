---
title: Payment Options API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Payment Options** API returns all eligible payment instruments (EMI, Net Banking, Wallets, Cards, UPI, Standing Instructions, COD) configured for the merchant and the specific order amount.

Call this API when rendering the checkout page or initial payment selector screen.

- Returns list of active net banking banks with uptime health indicators (`up_status`).
- Provides supported UPI apps, intent schemes, and custom collect configurations.
- Returns enabled card networks (Credit Card, Debit Card) and eligibility rules.
- Highlights down banks in `downInfo` to allow disabling down options or alerting customers proactively.

**Environment**

|                            |                                              |
| -------------------------- | -------------------------------------------- |
| **Test Environment**       | `https://apitest.payu.in/v1/payment-options` |
| **Production Environment** | `https://api.payu.in/v1/payment-options`     |

## Sample Request

```bash
curl -X GET "https://apitest.payu.in/v1/payment-options?encOrderId=c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312"
```
```python
import requests
import json

url = "https://apitest.payu.in/v1/payment-options?encOrderId=c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312"

headers = {
}

response = requests.get(url, headers=headers)

print(f'Status Code: {response.status_code}')
print(f'Response: {response.text}')
```
```javascript
const axios = require('axios');

const url = 'https://apitest.payu.in/v1/payment-options?encOrderId=c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312';

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
            URL url = new URL("https://apitest.payu.in/v1/payment-options?encOrderId=c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312");
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

$url = 'https://apitest.payu.in/v1/payment-options?encOrderId=c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312';

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
## Request Parameters

**Mandatory Parameters**

| Parameter  | Description                                                                                                   | Example                                                          |
| :--------- | :------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------- |
| encOrderId | `String` Encrypted order identifier obtained from the Create Order response (`transaction.encryptedOrderId`). | c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312 |

> **Note:** Alternatively, authenticate using Order ID & Merchant Key by passing `orderId` (the order ID supplied during order creation) and `X-Credential-Username` (merchant key) as headers.

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

| Parameter               | Description                                                                                                                                             | Example                                                                                                          |
| :---------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------- |
| paymentMethods.nb       | `Object` Contains all supported Net Banking banks (`all`) and prioritized banks (`top`) with bank codes (`ibibo_code`) and health status (`up_status`). |                                                                                                                  |
| paymentMethods.upi      | `Object` Contains UPI L1/L2 app configurations, package names, deep link schemes, and recommended UPI apps.                                             |                                                                                                                  |
| paymentMethods.emi      | `Object` Eligible credit and debit card EMI providers with minimum transaction thresholds.                                                              |                                                                                                                  |
| paymentMethods.cashcard | `Object` Supported mobile wallets (e.g. Amazon Pay, Airtel Money).                                                                                      |                                                                                                                  |
| paymentMethods.cc / dc  | `Object` Supported card schemes (VISA, MasterCard, RuPay, etc.).                                                                                        |                                                                                                                  |
| downInfo                | `Object` List of banks or channels currently experiencing server downtime.                                                                              |                                                                                                                  |
| bankLogosUrl            | `String` Base CDN URL to render bank and wallet logo icons.                                                                                             | [https://web-assets.payu.in/web/images/assets/bankLogo/](https://web-assets.payu.in/web/images/assets/bankLogo/) |