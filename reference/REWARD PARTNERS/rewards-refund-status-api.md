---
title: Refund Status API - Rewards
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Refund Status API
deprecated: false
hidden: true
metadata:
  robots: index
---

***

The **Refund Status** API is used to fetch the status of a previously initiated refund.

### Response States

* **Success**: Refund is processed successfully
* **Pending**: Refund is still under process
* **Failed**: Refund could not be processed

## Environment

|            |                                                                                                                                            |
| :--------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Production | [https://api.payu.in/loyalty-points/refund/v1/\{loyaltyRefundId}](https://api.payu.in/loyalty-points/refund/v1/\{loyaltyRefundId})         |
| Test       | [https://apitest.payu.in/loyalty-points/refund/v1/\{loyaltyRefundId}](https://apitest.payu.in/loyalty-points/refund/v1/\{loyaltyRefundId}) |

HTTP Method: **GET**

## Request header

<V2_paymentHeader />

## Request path parameters

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
        loyaltyRefundId <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Unique loyalty refund ID returned by Refund API
      </td>
      <td style={{ textAlign: "left" }}>
        1213
      </td>
    </tr>
  </tbody>
</Table>
`}</HTMLBlock>

## Sample request

### Non-seamless integration

```curl
curl -X GET "https://apitest.payu.in/loyalty-points/refund/v1/1213" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID"
```
```python
import requests
import json

url = "https://apitest.payu.in/loyalty-points/refund/v1/1213"

headers = {
  "Content-Type": "application/json",
  "mid": "YOUR_MERCHANT_ID"
}

response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.text)
```
```csharp
using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var client = new HttpClient();
        var url = "https://apitest.payu.in/loyalty-points/refund/v1/1213";
        
        client.DefaultRequestHeaders.Add("Content-Type", "application/json");
        client.DefaultRequestHeaders.Add("mid", "YOUR_MERCHANT_ID");
        
        var response = await client.GetAsync(url);
        var responseBody = await response.Content.ReadAsStringAsync();
        
        Console.WriteLine($"Status Code: {(int)response.StatusCode}");
        Console.WriteLine($"Response: {responseBody}");
    }
}
```
```javascript
const url = "https://apitest.payu.in/loyalty-points/refund/v1/1213";

const headers = {
  "Content-Type": "application/json",
  "mid": "YOUR_MERCHANT_ID"
};

async function makeRequest() {
    try {
        const response = await fetch(url, {
            method: "GET",
            headers: headers
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

public class ApiRequest {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://apitest.payu.in/loyalty-points/refund/v1/1213");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("mid", "YOUR_MERCHANT_ID");
        
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

$url = "https://apitest.payu.in/loyalty-points/refund/v1/1213";

$headers = [
  "Content-Type" => "application/json",
  "mid" => "YOUR_MERCHANT_ID"
];

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "GET");
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
curl -X GET "https://apitest.payu.in/loyalty-points/refund/v1/1213" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
```
```python
import requests
import json

url = "https://apitest.payu.in/loyalty-points/refund/v1/1213"

headers = {
  "Content-Type": "application/json",
  "Date": "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization": "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
}

response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.text)
```
```csharp
using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var client = new HttpClient();
        var url = "https://apitest.payu.in/loyalty-points/refund/v1/1213";
        
        client.DefaultRequestHeaders.Add("Content-Type", "application/json");
        client.DefaultRequestHeaders.Add("Date", "Wed, 08 Sep 2025 13:22:43 GMT");
        client.DefaultRequestHeaders.Add("Authorization", "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"");
        
        var response = await client.GetAsync(url);
        var responseBody = await response.Content.ReadAsStringAsync();
        
        Console.WriteLine($"Status Code: {(int)response.StatusCode}");
        Console.WriteLine($"Response: {responseBody}");
    }
}
```
```javascript
const url = "https://apitest.payu.in/loyalty-points/refund/v1/1213";

const headers = {
  "Content-Type": "application/json",
  "Date": "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization": "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
};

async function makeRequest() {
    try {
        const response = await fetch(url, {
            method: "GET",
            headers: headers
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

public class ApiRequest {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://apitest.payu.in/loyalty-points/refund/v1/1213");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("Date", "Wed, 08 Sep 2025 13:22:43 GMT");
        conn.setRequestProperty("Authorization", "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"");
        
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

$url = "https://apitest.payu.in/loyalty-points/refund/v1/1213";

$headers = [
  "Content-Type" => "application/json",
  "Date" => "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization" => "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
];

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "GET");
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

| Parameter          | Description                                                            | Example                                |
| ------------------ | ---------------------------------------------------------------------- | -------------------------------------- |
| message            | `String` - Refund process status (`Success`, `Failed`, or `Pending`)   | `"Success"` / `"Failed"` / `"Pending"` |
| loyaltyRefundId    | `String` - Loyalty refund ID                                           | `"1213"`                               |
| rewardPartnerRefId | `String` - Reference ID provided by the reward partner (if successful) | `"7251637276230479872"`                |

## Sample response

### Success scenario

```json
{
  "message": "Success",
  "loyaltyRefundId": 83,
  "rewardPartnerRefId": "7251637276230479872"
}
```

### Failure scenario

* Failed refund

```json
{
  "message": "Failed",
  "loyaltyRefundId": "1213"
}
```

* Pending refund

```json
{
  "message": "Pending",
  "loyaltyRefundId": "1213"
}
```

<br />

<Callout icon="📘" theme="info">
  **Notes:**

  * Both APIs are part of the **Loyalty Points Network** and must be called within a secure server-to-server (S2S) framework
  * Regular status checks are recommended for pending refunds
</Callout>

<br />