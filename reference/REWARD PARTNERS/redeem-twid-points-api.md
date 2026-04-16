---
title: Redeem TWID Points API
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Redeem TWID Points API
deprecated: false
hidden: true
metadata:
  robots: index
---

The **Redeem TWID Points** API is used to redeem or finalize TWID points that have previously been put on hold via the `Create Payment` API.

## Environment

|            |                                                                                                                          |
| :--------- | :----------------------------------------------------------------------------------------------------------------------- |
| Production | [https://api.payu.in/loyalty-points/payment/v1/continue](https://api.payu.in/loyalty-points/payment/v1/continue)         |
| Test       | [https://apitest.payu.in/loyalty-points/payment/v1/continue](https://apitest.payu.in/loyalty-points/payment/v1/continue) |

HTTP Method: **POST**

## Request header

<V2_paymentHeader />

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

## Sample Request

### Non-seamless Integration

```curl
curl -X POST "https://apitest.payu.in/loyalty-points/payment/v1/continue" \
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

url = "https://apitest.payu.in/loyalty-points/payment/v1/continue"

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
        var url = "https://apitest.payu.in/loyalty-points/payment/v1/continue";
        
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
const url = "https://apitest.payu.in/loyalty-points/payment/v1/continue";

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
        URL url = new URL("https://apitest.payu.in/loyalty-points/payment/v1/continue");
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

$url = "https://apitest.payu.in/loyalty-points/payment/v1/continue";

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

### Seamless Integration

```curl
curl -X POST "https://apitest.payu.in/loyalty-points/payment/v1/continue" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{
    "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
    "loyaltyProvider": "TWID"
  }'
```
```python
import requests
import json

url = "https://apitest.payu.in/loyalty-points/payment/v1/continue"

headers = {
  "Content-Type": "application/json",
  "Date": "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization": "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
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
        var url = "https://apitest.payu.in/loyalty-points/payment/v1/continue";
        
        client.DefaultRequestHeaders.Add("Content-Type", "application/json");
        client.DefaultRequestHeaders.Add("Date", "Wed, 08 Sep 2025 13:22:43 GMT");
        client.DefaultRequestHeaders.Add("Authorization", "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"");

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
const url = "https://apitest.payu.in/loyalty-points/payment/v1/continue";

const headers = {
  "Content-Type": "application/json",
  "Date": "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization": "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
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
        URL url = new URL("https://apitest.payu.in/loyalty-points/payment/v1/continue");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("Date", "Wed, 08 Sep 2025 13:22:43 GMT");
        conn.setRequestProperty("Authorization", "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"");

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

$url = "https://apitest.payu.in/loyalty-points/payment/v1/continue";

$headers = [
  "Content-Type" => "application/json",
  "Date" => "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization" => "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
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

## Response Parameters

| Parameter          | Description                                                                           | Example                                       |
| ------------------ | ------------------------------------------------------------------------------------- | --------------------------------------------- |
| status             | `String` - Outcome of the transaction (e.g., SUCCESS or validation error information) | `"SUCCESS"`                                   |
| loyaltyTxnId       | `String` - Reference ID used to confirm the redemption transaction                    | `"1821b1e2-34dd-47e3-9b54-b56b9d352a6b"`      |
| rewardPartnerRefId | `String` - A partner reference ID, which can also be used for reconciliation purposes | `"7251637276230479872"`                       |
| acsTemplate        | `String` - Reserved API field (currently unused)                                      | `null`                                        |
| issueCode          | `String` - Error code (for failure responses)                                         | `"LS404-401"`                                 |
| errorMessage       | `String` - Error description (for failure responses)                                  | `"Transaction details not present in the DB"` |
| errorType          | `String` - Type of error (for failure responses)                                      | `"VALIDATION_EXCEPTION"`                      |

## Sample response

### Success scenario

```json
{
  "status": "SUCCESS",
  "loyaltyTxnId": "1821b1e2-34dd-47e3-9b54-b56b9d352a6b",
  "rewardPartnerRefId": "7251637276230479872",
  "acsTemplate": null
}
```

### Failure scenario

```json
{
  "issueCode": "LS404-401",
  "errorMessage": "Transaction details not present in the DB",
  "errorType": "VALIDATION_EXCEPTION"
}
```
