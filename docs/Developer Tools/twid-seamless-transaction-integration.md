---
title: '[BCKUP]TWID Seamless Transaction Integration'
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Twid Seamless Transaction Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  robots: index
---

This guide describes the complete integration workflow for Twid Seamless Transactions. The workflow involves fetching balances from multiple loyalty providers, holding the points for a transaction, and then redeeming them.

<Cards columns={3}>
<Card title="1. Fetch All Balance" href="#step-1-fetch-all-balance">
Fetch reward point balances from multiple loyalty providers
<br />
</Card>
<Card title="2. Hold TWID Points" href="#step-2-hold-twid-points">
Hold (reserve) reward points for the transaction
<br />
</Card>
<Card title="3. Redeem TWID Points" href="#step-3-redeem-twid-points">
Redeem the held points to complete the transaction
</Card>
</Cards>

## Step 1: Fetch All Balance

Use the Fetch All Balance API to retrieve reward point balances from multiple specified loyalty providers and determine how much users can save using their points.

<Accordion title="Request parameters" icon="fa-table">
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
</Accordion>

<Accordion title="Sample request" icon="fa-code">
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
</Accordion>

<Accordion title="Sample response" icon="fa-file-code">
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
</Accordion>

## Step 2: Hold TWID Points

After fetching the balance, use the Create Payment API to hold (reserve) the reward points for the transaction.

<Accordion title="Request parameters" icon="fa-table">
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
        merchantKey <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> PayU merchant key for authentication
      </td>
      <td style={{ textAlign: "left" }}>
        18001
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        parentPayuTxnId <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Parent transaction ID from main payment transaction
      </td>
      <td style={{ textAlign: "left" }}>
        65646400234509041
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        totalAmount <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>Number</code> Total monetary reward amount to be held/redeemed
      </td>
      <td style={{ textAlign: "left" }}>
        1000
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        mobile <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> User's mobile number
      </td>
      <td style={{ textAlign: "left" }}>
        9304204**
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        loyaltyProvider <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Loyalty provider identifier
      </td>
      <td style={{ textAlign: "left" }}>
        TWID
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        orderAmount <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>Number</code> Total order/bill amount for transaction
      </td>
      <td style={{ textAlign: "left" }}>
        10000
      </td>
    </tr>
  </tbody>
</Table>
`}</HTMLBlock>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
```curl
curl -X POST "{{loyalty-service-url}}/payment/v1/createPayment" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID" \
  -d '{
    "merchantKey": "18001",
    "parentPayuTxnId": "65646400234509041",
    "totalAmount": 1000,
    "mobile": "9304204**",
    "loyaltyProvider": "TWID",
    "orderAmount": 10000
  }'
```

```python
import requests
import json

url = "{{loyalty-service-url}}/payment/v1/createPayment"

headers = {
  "Content-Type": "application/json",
  "mid": "YOUR_MERCHANT_ID"
}

payload = {
  "merchantKey": "18001",
  "parentPayuTxnId": "65646400234509041",
  "totalAmount": 1000,
  "mobile": "9304204**",
  "loyaltyProvider": "TWID",
  "orderAmount": 10000
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
        var url = "{{loyalty-service-url}}/payment/v1/createPayment";
        
        client.DefaultRequestHeaders.Add("Content-Type", "application/json");
        client.DefaultRequestHeaders.Add("mid", "YOUR_MERCHANT_ID");

        var json = new
        {
            merchantKey = "18001",
            parentPayuTxnId = "65646400234509041",
            totalAmount = 1000,
            mobile = "9304204**",
            loyaltyProvider = "TWID",
            orderAmount = 10000
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
const url = "{{loyalty-service-url}}/payment/v1/createPayment";

const headers = {
  "Content-Type": "application/json",
  "mid": "YOUR_MERCHANT_ID"
};

const payload = {
  "merchantKey": "18001",
  "parentPayuTxnId": "65646400234509041",
  "totalAmount": 1000,
  "mobile": "9304204**",
  "loyaltyProvider": "TWID",
  "orderAmount": 10000
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

public class ApiRequest {
    public static void main(String[] args) throws Exception {
        URL url = new URL("{{loyalty-service-url}}/payment/v1/createPayment");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("mid", "YOUR_MERCHANT_ID");

        Gson gson = new Gson();
        String jsonInputString = "{\"merchantKey\":\"18001\",\"parentPayuTxnId\":\"65646400234509041\",\"totalAmount\":1000,\"mobile\":\"9304204**\",\"loyaltyProvider\":\"TWID\",\"orderAmount\":10000}";
        
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

$url = "{{loyalty-service-url}}/payment/v1/createPayment";

$headers = [
  "Content-Type" => "application/json",
  "mid" => "YOUR_MERCHANT_ID"
];

$payload = [
  "merchantKey" => "18001",
  "parentPayuTxnId" => "65646400234509041",
  "totalAmount" => 1000,
  "mobile" => "9304204**",
  "loyaltyProvider" => "TWID",
  "orderAmount" => 10000
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
</Accordion>

<Accordion title="Sample response" icon="fa-file-code">
```json
{
  "statusCode": 1,
  "status": "PENDING",
  "loyaltyTxnId": "d1dce98d-98ec-4b90-a7d8-853fee82a113",
  "rewardPartnerRefId": null
}
```
</Accordion>

## Step 3: Redeem TWID Points

After successfully holding the points, use the Redeem TWID Points API to finalize the transaction and redeem the points.

<Accordion title="Request parameters" icon="fa-table">
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
        loyaltyTxnId <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Reference ID provided by the Loyalty-Service during the Create Payment call
      </td>
      <td style={{ textAlign: "left" }}>
        bd1a77b6-1596-46e1-b79f-2770bcb636c7
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        loyaltyProvider <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> The loyalty provider identifier (e.g., TWID)
      </td>
      <td style={{ textAlign: "left" }}>
        TWID
      </td>
    </tr>
  </tbody>
</Table>
`}</HTMLBlock>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
```curl
curl -X POST "{{loyalty-service-url}}/payment/v1/continue" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID" \
  -d '{
    "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
    "loyaltyProvider": "TWID"
  }'
```

```python
import requests
import json

url = "{{loyalty-service-url}}/payment/v1/continue"

headers = {
  "Content-Type": "application/json",
  "mid": "YOUR_MERCHANT_ID"
}

payload = {
  "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
  "loyaltyProvider": "TWID"
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
        var url = "{{loyalty-service-url}}/payment/v1/continue";
        
        client.DefaultRequestHeaders.Add("Content-Type", "application/json");
        client.DefaultRequestHeaders.Add("mid", "YOUR_MERCHANT_ID");

        var json = new
        {
            loyaltyTxnId = "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
            loyaltyProvider = "TWID"
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
const url = "{{loyalty-service-url}}/payment/v1/continue";

const headers = {
  "Content-Type": "application/json",
  "mid": "YOUR_MERCHANT_ID"
};

const payload = {
  "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
  "loyaltyProvider": "TWID"
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

public class ApiRequest {
    public static void main(String[] args) throws Exception {
        URL url = new URL("{{loyalty-service-url}}/payment/v1/continue");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("mid", "YOUR_MERCHANT_ID");

        Gson gson = new Gson();
        String jsonInputString = "{\"loyaltyTxnId\":\"bd1a77b6-1596-46e1-b79f-2770bcb636c7\",\"loyaltyProvider\":\"TWID\"}";
        
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

$url = "{{loyalty-service-url}}/payment/v1/continue";

$headers = [
  "Content-Type" => "application/json",
  "mid" => "YOUR_MERCHANT_ID"
];

$payload = [
  "loyaltyTxnId" => "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
  "loyaltyProvider" => "TWID"
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
</Accordion>

<Accordion title="Sample response" icon="fa-file-code">
```json
{
  "status": "SUCCESS",
  "loyaltyTxnId": "1821b1e2-34dd-47e3-9b54-b56b9d352a6b",
  "rewardPartnerRefId": "7251637276230479872",
  "acsTemplate": null
}
```
</Accordion>