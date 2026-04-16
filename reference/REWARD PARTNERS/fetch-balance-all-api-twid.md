---
title: Fetch Balance All API
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Fetch Balance All API - TWID
deprecated: false
hidden: false
metadata:
  robots: index
---

## Environment

|            |                                                                                                                |
| :--------- | :------------------------------------------------------------------------------------------------------------- |
| Production | [https://api.payu.in/loyalty-points/v1/balance/all](https://api.payu.in/loyalty-points/v1/balance/all)         |
| Test       | [https://apitest.payu.in/loyalty-points/v1/balance/all](https://apitest.payu.in/loyalty-points/v1/balance/all) |

HTTP Method: **POST**

## Request header

<V2_paymentHeader />

<br />

## Request parameters

<HTMLBlock>{`
<style>
/* Target only the second column in the table */
.markdown-body table td:nth-child(2) {
  word-break: break-word !important;
}

/* Keep the first column from breaking unnecessarily */
.markdown-body table td:nth-child(1) {
  word-break: normal;
  white-space: nowrap;
}
</style>
<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Parameter
      </th>
      <th style={{ textAlign: "left" }}>
        Description
      </th>
      <th style={{ textAlign: "left" }}>
        Example
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        loyaltyProviders <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>Array</code> Array of loyalty provider names to fetch rewards from
      </td>
      <td style={{ textAlign: "left" }}>
        ["TWID", "ZILLION"]
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        mobileNumber <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> User's mobile number (masked for privacy)
      </td>
      <td style={{ textAlign: "left" }}>
        88001085**
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        orderAmount <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>Number</code> Order amount for which reward points are applicable
      </td>
      <td style={{ textAlign: "left" }}>
        1000
      </td>
    </tr>
  </tbody>
</Table>
`}</HTMLBlock>

## Sample request

### Non-seamless integration

```curl
curl -X POST "{{loyalty-service-url}}/v1/balance/all" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID" \
  -d '{
    "loyaltyProviders": ["TWID", "ZILLION"],
    "mobileNumber": "88001085**",
    "orderAmount": 1000
  }'
```
```python
import requests
import json

url = "{{loyalty-service-url}}/v1/balance/all"

headers = {
  "Content-Type": "application/json",
  "mid": "YOUR_MERCHANT_ID"
}

payload = {
  "loyaltyProviders": ["TWID", "ZILLION"],
  "mobileNumber": "88001085**",
  "orderAmount": 1000
}

response = requests.post(url, headers=headers, json=payload)
print("Status Code:", response.status_code)
print("Response:", response.text)
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var client = new HttpClient();
        var url = "{{loyalty-service-url}}/v1/balance/all";
        
        client.DefaultRequestHeaders.Add("Content-Type", "application/json");
        client.DefaultRequestHeaders.Add("mid", "YOUR_MERCHANT_ID");

        var json = new
        {
            loyaltyProviders = new[] { "TWID", "ZILLION" },
            mobileNumber = "88001085**",
            orderAmount = 1000
        };
        var jsonString = JsonSerializer.Serialize(json);
        var content = new StringContent(jsonString, Encoding.UTF8, "application/json");
        
        var response = await client.PostAsync(url, content);
        var responseBody = await response.Content.ReadAsStringAsync();
        
        Console.WriteLine($"Status Code: {(int)response.StatusCode}");
        Console.WriteLine($"Response: {responseBody}");
    }
}
```

```javascript
const url = "{{loyalty-service-url}}/v1/balance/all";

const headers = {
  "Content-Type": "application/json",
  "mid": "YOUR_MERCHANT_ID"
};

const payload = {
  "loyaltyProviders": ["TWID", "ZILLION"],
  "mobileNumber": "88001085**",
  "orderAmount": 1000
};

async function makeRequest() {
    try {
        const response = await fetch(url, {
            method: "POST",
            headers: headers,
            body: JSON.stringify(payload)
        });
        
        const data = await response.text();
        console.log("Status Code:", response.status);
        console.log("Response:", data);
    } catch (error) {
        console.error("Error:", error);
    }
}

makeRequest();
```

```java
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import com.google.gson.Gson;
import java.util.Arrays;
import java.util.List;

public class ApiRequest {
    public static void main(String[] args) throws Exception {
        URL url = new URL("{{loyalty-service-url}}/v1/balance/all");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("mid", "YOUR_MERCHANT_ID");

        Gson gson = new Gson();
        String jsonInputString = "{\"loyaltyProviders\":[\"TWID\",\"ZILLION\"],\"mobileNumber\":\"88001085**\",\"orderAmount\":1000}";
        
        try (OutputStream os = conn.getOutputStream()) {
            byte[] input = jsonInputString.getBytes(StandardCharsets.UTF_8);
            os.write(input, 0, input.length);
        }
        
        int responseCode = conn.getResponseCode();
        System.out.println("Status Code: " + responseCode);
        
        try (BufferedReader br = new BufferedReader(
                new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
            StringBuilder response = new StringBuilder();
            String responseLine;
            while ((responseLine = br.readLine()) != null) {
                response.append(responseLine.trim());
            }
            System.out.println("Response: " + response.toString());
        }
    }
}
```
```php
<?php

$url = "{{loyalty-service-url}}/v1/balance/all";

$headers = [
  "Content-Type" => "application/json",
  "mid" => "YOUR_MERCHANT_ID"
];

$payload = [
  "loyaltyProviders" => ["TWID", "ZILLION"],
  "mobileNumber" => "88001085**",
  "orderAmount" => 1000
];

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, array_map(function($key, $value) {
    return "$key: $value";
}, array_keys($headers), $headers));

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```

### Seamless integration

```curl
curl -X POST "{{loyalty-service-url}}/v1/balance/all" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{
    "loyaltyProviders": ["TWID", "ZILLION"],
    "mobileNumber": "88001085**",
    "orderAmount": 1000
  }'
```
```python
import requests
import json

url = "{{loyalty-service-url}}/v1/balance/all"

headers = {
  "Content-Type": "application/json",
  "Date": "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization": "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
}

payload = {
  "loyaltyProviders": ["TWID", "ZILLION"],
  "mobileNumber": "88001085**",
  "orderAmount": 1000
}

response = requests.post(url, headers=headers, json=payload)
print("Status Code:", response.status_code)
print("Response:", response.text)
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var client = new HttpClient();
        var url = "{{loyalty-service-url}}/v1/balance/all";
        
        client.DefaultRequestHeaders.Add("Content-Type", "application/json");
        client.DefaultRequestHeaders.Add("Date", "Wed, 08 Sep 2025 13:22:43 GMT");
        client.DefaultRequestHeaders.Add("Authorization", "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"");

        var json = new
        {
            loyaltyProviders = new[] { "TWID", "ZILLION" },
            mobileNumber = "88001085**",
            orderAmount = 1000
        };
        var jsonString = JsonSerializer.Serialize(json);
        var content = new StringContent(jsonString, Encoding.UTF8, "application/json");
        
        var response = await client.PostAsync(url, content);
        var responseBody = await response.Content.ReadAsStringAsync();
        
        Console.WriteLine($"Status Code: {(int)response.StatusCode}");
        Console.WriteLine($"Response: {responseBody}");
    }
}
```
```javascript
const url = "{{loyalty-service-url}}/v1/balance/all";

const headers = {
  "Content-Type": "application/json",
  "Date": "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization": "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
};

const payload = {
  "loyaltyProviders": ["TWID", "ZILLION"],
  "mobileNumber": "88001085**",
  "orderAmount": 1000
};

async function makeRequest() {
    try {
        const response = await fetch(url, {
            method: "POST",
            headers: headers,
            body: JSON.stringify(payload)
        });
        
        const data = await response.text();
        console.log("Status Code:", response.status);
        console.log("Response:", data);
    } catch (error) {
        console.error("Error:", error);
    }
}

makeRequest();
```
```java
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import com.google.gson.Gson;
import java.util.Arrays;
import java.util.List;

public class ApiRequest {
    public static void main(String[] args) throws Exception {
        URL url = new URL("{{loyalty-service-url}}/v1/balance/all");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("Date", "Wed, 08 Sep 2025 13:22:43 GMT");
        conn.setRequestProperty("Authorization", "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"");

        Gson gson = new Gson();
        String jsonInputString = "{\"loyaltyProviders\":[\"TWID\",\"ZILLION\"],\"mobileNumber\":\"88001085**\",\"orderAmount\":1000}";
        
        try (OutputStream os = conn.getOutputStream()) {
            byte[] input = jsonInputString.getBytes(StandardCharsets.UTF_8);
            os.write(input, 0, input.length);
        }
        
        int responseCode = conn.getResponseCode();
        System.out.println("Status Code: " + responseCode);
        
        try (BufferedReader br = new BufferedReader(
                new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
            StringBuilder response = new StringBuilder();
            String responseLine;
            while ((responseLine = br.readLine()) != null) {
                response.append(responseLine.trim());
            }
            System.out.println("Response: " + response.toString());
        }
    }
}
```
```php
<?php

$url = "{{loyalty-service-url}}/v1/balance/all";

$headers = [
  "Content-Type" => "application/json",
  "Date" => "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization" => "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
];

$payload = [
  "loyaltyProviders" => ["TWID", "ZILLION"],
  "mobileNumber" => "88001085**",
  "orderAmount" => 1000
];

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, array_map(function($key, $value) {
    return "$key: $value";
}, array_keys($headers), $headers));

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```

## Response parameters

| Parameter                   | Description                                                    | Example                                    |
| --------------------------- | -------------------------------------------------------------- | ------------------------------------------ |
| data[].loyaltyProvider      | `String` - Loyalty provider identifier for this response entry | `"TWID"`                                   |
| data[].usableAmount         | `Number` - Maximum monetary amount that can be saved           | `500.0`                                    |
| data[].usablePoints         | `Number` - Required reward points for maximum savings          | `500`                                      |
| data[].title                | `String` - Display title describing the reward offer           | `"Save Rs 500 using 500 TWID Cash Points"` |
| data[].earnConfig.points    | `Number` - Points that can be earned                           | `0`                                        |
| data[].issuerDetailDTO.logo | `String` - Logo URL of the brand/issuer                        | `"https://cdn.twidpay.com/brand_logo.png"` |
| data[].holdApplicable       | `Boolean` - Indicates if points can be held for the reward     | `false`                                    |
| data[].customErrorMessage   | `String` - Error message for specific provider (if applicable) | `"Unable to process request for provider"` |

## Sample response

```json
{
  "data": [
    {
      "loyaltyProvider": "TWID",
      "usableAmount": 500.0,
      "usablePoints": 500,
      "title": "Save Rs 500 using 500 TWID Cash Points",
      "earnConfig": { 
        "points": 0, 
        "amount": null, 
        "title": null 
      },
      "issuerDetailDTO": {
        "brandName": "TWID Cash",
        "logo": "https://cdn.twidpay.com/brand_image.png",
        "issuerType": "brand"
      },
      "holdApplicable": false
    },
    {
      "loyaltyProvider": "ZILLION",
      "customErrorMessage": "Unable to process request for provider",
      "usableAmount": null,
      "usablePoints": null
    }
  ]
}
```
