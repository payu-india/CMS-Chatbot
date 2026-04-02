---
title: Transaction Details API
api:
  file: updated_settlement_devguide_api_postman_collection_v1.json
  operationId: get_treasury-v1-settlement-transactiondetails
hidden: false
---
This API retrieves detailed information about a specific transaction using the merchant transaction ID. This API provides comprehensive transaction data including status, amount, settlement details, and associated metadata.

**Environment**

|                  |                                                                |
| :--------------- | :------------------------------------------------------------- |
| Test Environment | http://info.payu.in/treasury/v1/settlement/transactionDetails  |
| Production URL   | http://info.payu.in/treasury/v1/settlement/transactionDetails` |

## Request Parameter
## Authentication Header


## Header Parameters*

| Parameter             | Type   | Required | Description                                          |
| --------------------- | ------ | -------- | ---------------------------------------------------- |
| merchantTransactionId | String | Yes      | Merchant transaction/reference ID (1-100 characters) |

##Saample Request
```curl
curl --location 'http://info.payu.in/treasury/v1/settlement/transactionDetails?merchantTransactionId=W49OV6KQXR4H' \
--header 'mid: 180012'
--header 'Authorization: Bearer <token>'
```
```python
import requests
import json

url = "http://info.payu.in/treasury/v1/settlement/transactionDetails"
headers = {
    'Authorization': 'Bearer <your_token>',
    'mid': '<your_merchant_id>',
    'Accept': 'application/json'
}
params = {
    'merchantTransactionId': 'TXN123456789'
}

try:
    response = requests.get(url, headers=headers, params=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
```csharp
using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        var client = new HttpClient();
        var url = "http://info.payu.in/treasury/v1/settlement/transactionDetails?merchantTransactionId=TXN123456789";
        
        client.DefaultRequestHeaders.Add("Authorization", "Bearer <your_token>");
        client.DefaultRequestHeaders.Add("mid", "<your_merchant_id>");
        client.DefaultRequestHeaders.Add("Accept", "application/json");
        
        try
        {
            var response = await client.GetAsync(url);
            var content = await response.Content.ReadAsStringAsync();
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {content}");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}
```
```javascript
async function getTransactionDetails() {
    const url = "http://info.payu.in/treasury/v1/settlement/transactionDetails?merchantTransactionId=TXN123456789";
    
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Authorization': 'Bearer <your_token>',
                'mid': '<your_merchant_id>',
                'Accept': 'application/json'
            }
        });
        
        const data = await response.text();
        console.log(`Status: ${response.status}`);
        console.log(`Response: ${data}`);
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

getTransactionDetails();
```
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class TransactionDetailsAPI {
    public static void main(String[] args) {
        try {
            String urlString = "http://info.payu.in/treasury/v1/settlement/transactionDetails?merchantTransactionId=TXN123456789";
            URL url = new URL(urlString);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer <your_token>");
            connection.setRequestProperty("mid", "<your_merchant_id>");
            connection.setRequestProperty("Accept", "application/json");
            
            int statusCode = connection.getResponseCode();
            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder response = new StringBuilder();
            String line;
            
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
            reader.close();
            
            System.out.println("Status Code: " + statusCode);
            System.out.println("Response: " + response.toString());
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
$url = "http://info.payu.in/treasury/v1/settlement/transactionDetails?merchantTransactionId=TXN123456789";

$headers = [
    'Authorization: Bearer <your_token>',
    'mid: <your_merchant_id>',
    'Accept: application/json'
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if (curl_errno($ch)) {
    echo 'Error: ' . curl_error($ch);
} else {
    echo "Status Code: " . $httpCode . "\n";
    echo "Response: " . $response;
}

curl_close($ch);
?>
```

**Sample Response**

```json
{
    "status": 1,
    "msg": "Transaction details retrieved successfully",
    "result": {
        "transactionId": "TXN123456789",
        "payuId": "403993715525901741",
        "amount": "1000.00",
        "status": "success",
        "settlementId": "SETT123456",
        "settlementAmount": "980.00",
        "fees": "20.00",
        "tax": "3.60",
        "settlementDate": "2023-06-28"
    }
}
```
