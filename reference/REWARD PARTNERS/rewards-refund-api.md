---
title: Refund API - TWID
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Refund API - TWID
deprecated: false
hidden: true
metadata:
  robots: index
---

***

The **Refund** API is used to initiate a refund request for a loyalty-based transaction.

## Environment

|            |                                                                                                      |
| :--------- | :--------------------------------------------------------------------------------------------------- |
| Production | [https://api.payu.in/loyalty-points/refund/v1](https://api.payu.in/loyalty-points/refund/v1)         |
| Test       | [https://apitest.payu.in/loyalty-points/refund/v1](https://apitest.payu.in/loyalty-points/refund/v1) |

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
        parentTxnId <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Parent PayU transaction ID
      </td>
      <td style={{ textAlign: "left" }}>
        bd1a77b6-1596-46e1-b79f-2770bcb636c7
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        merchantReferenceId <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Merchant reference ID
      </td>
      <td style={{ textAlign: "left" }}>
        56as67ds7678asd
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        refundAmount <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>Number</code> Amount requested for refund
      </td>
      <td style={{ textAlign: "left" }}>
        200
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        refundId <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Unique refund ID
      </td>
      <td style={{ textAlign: "left" }}>
        4656526
      </td>
    </tr>
  </tbody>
</Table>
`}</HTMLBlock>

## Sample request

### Non-seamless integration

```curl
curl -X POST "https://apitest.payu.in/loyalty-points/refund/v1" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID" \
  -d '{
    "parentTxnId": "9090909090909111",
    "merchantReferenceId": "56as67ds7678asd",
    "refundAmount": 200,
    "refundId": "4656526"
  }'
```
```python
import requests
import json

url = "https://apitest.payu.in/loyalty-points/refund/v1"

headers = {
  "Content-Type": "application/json",
  "mid": "YOUR_MERCHANT_ID"
}

payload = {
  "parentTxnId": "9090909090909111",
  "merchantReferenceId": "56as67ds7678asd",
  "refundAmount": 200,
  "refundId": "4656526"
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
        var url = "https://apitest.payu.in/loyalty-points/refund/v1";
        
        client.DefaultRequestHeaders.Add("Content-Type", "application/json");
        client.DefaultRequestHeaders.Add("mid", "YOUR_MERCHANT_ID");

        var json = new
        {
            parentTxnId = "9090909090909111",
            merchantReferenceId = "56as67ds7678asd",
            refundAmount = 200,
            refundId = "4656526"
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
const url = "https://apitest.payu.in/loyalty-points/refund/v1";

const headers = {
  "Content-Type": "application/json",
  "mid": "YOUR_MERCHANT_ID"
};

const payload = {
  "parentTxnId": "9090909090909111",
  "merchantReferenceId": "56as67ds7678asd",
  "refundAmount": 200,
  "refundId": "4656526"
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
        URL url = new URL("https://apitest.payu.in/loyalty-points/refund/v1");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("mid", "YOUR_MERCHANT_ID");

        Gson gson = new Gson();
        String jsonInputString = "{\"parentTxnId\":\"9090909090909111\",\"merchantReferenceId\":\"56as67ds7678asd\",\"refundAmount\":200,\"refundId\":\"4656526\"}";
        
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

$url = "https://apitest.payu.in/loyalty-points/refund/v1";

$headers = [
  "Content-Type" => "application/json",
  "mid" => "YOUR_MERCHANT_ID"
];

$payload = [
  "parentTxnId" => "9090909090909111",
  "merchantReferenceId" => "56as67ds7678asd",
  "refundAmount" => 200,
  "refundId" => "4656526"
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
curl -X POST "https://apitest.payu.in/loyalty-points/refund/v1" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{
    "parentTxnId": "9090909090909111",
    "merchantReferenceId": "56as67ds7678asd",
    "refundAmount": 200,
    "refundId": "4656526"
  }'
```
```python
import requests
import json

url = "https://apitest.payu.in/loyalty-points/refund/v1"

headers = {
  "Content-Type": "application/json",
  "Date": "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization": "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
}

payload = {
  "parentTxnId": "9090909090909111",
  "merchantReferenceId": "56as67ds7678asd",
  "refundAmount": 200,
  "refundId": "4656526"
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
        var url = "https://apitest.payu.in/loyalty-points/refund/v1";
        
        client.DefaultRequestHeaders.Add("Content-Type", "application/json");
        client.DefaultRequestHeaders.Add("Date", "Wed, 08 Sep 2025 13:22:43 GMT");
        client.DefaultRequestHeaders.Add("Authorization", "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"");

        var json = new
        {
            parentTxnId = "9090909090909111",
            merchantReferenceId = "56as67ds7678asd",
            refundAmount = 200,
            refundId = "4656526"
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
const url = "https://apitest.payu.in/loyalty-points/refund/v1";

const headers = {
  "Content-Type": "application/json",
  "Date": "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization": "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
};

const payload = {
  "parentTxnId": "9090909090909111",
  "merchantReferenceId": "56as67ds7678asd",
  "refundAmount": 200,
  "refundId": "4656526"
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
        URL url = new URL("https://apitest.payu.in/loyalty-points/refund/v1");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("Date", "Wed, 08 Sep 2025 13:22:43 GMT");
        conn.setRequestProperty("Authorization", "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"");

        Gson gson = new Gson();
        String jsonInputString = "{\"parentTxnId\":\"9090909090909111\",\"merchantReferenceId\":\"56as67ds7678asd\",\"refundAmount\":200,\"refundId\":\"4656526\"}";
        
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

$url = "https://apitest.payu.in/loyalty-points/refund/v1";

$headers = [
  "Content-Type" => "application/json",
  "Date" => "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization" => "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
];

$payload = [
  "parentTxnId" => "9090909090909111",
  "merchantReferenceId" => "56as67ds7678asd",
  "refundAmount" => 200,
  "refundId" => "4656526"
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

| Parameter       | Description                                     | Example    |
| --------------- | ----------------------------------------------- | ---------- |
| message         | `String` - Status message of the refund request | `"Queued"` |
| loyaltyRefundId | `String` - Loyalty refund ID for tracking       | `"1213"`   |

## Sample response

```json
{
  "message": "Queued",
  "loyaltyRefundId": "1213"
}
```

<Callout icon="📘" theme="info">
  **Notes:**

  * When the refund is queued, the status must be verified using the **Refund Status API** for confirmation.
  * The `loyaltyRefundId` returned should be used to check the refund status
</Callout>
