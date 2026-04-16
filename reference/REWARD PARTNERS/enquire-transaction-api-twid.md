---
title: Enquire Transaction API - TWID
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Enquire Transaction API - TWID
deprecated: false
hidden: false
metadata:
  robots: index
---

The **Enquire Transaction** API allows the merchant to verify the status of a specific loyalty transaction either using the `loyaltyTxnId` or `payuTxnId` parameter. Both parameters are optional but at least one must be provided. The use cases for this API are:

* Reconciliation or to confirm the final status of loyalty transactions
* Transaction status verification during payment processing

## Environment

|            |                                                                                                                        |
| :--------- | :--------------------------------------------------------------------------------------------------------------------- |
| Production | [https://api.payu.in/loyalty-points/payment/v1/enquiry](https://api.payu.in/loyalty-points/payment/v1/enquiry)         |
| Test       | [https://apitest.payu.in/loyalty-points/payment/v1/enquiry](https://apitest.payu.in/loyalty-points/payment/v1/enquiry) |

HTTP Method: **POST**

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
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Reference ID generated during Create Payment or Redeem TWID Points calls
      </td>
      <td style={{ textAlign: "left" }}>
        bd1a77b6-1596-46e1-b79f-2770bcb636c7
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        payuTxnId <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> PayU transaction ID
      </td>
      <td style={{ textAlign: "left" }}>
        89887897898
      </td>
    </tr>
  </tbody>
</Table>
`}</HTMLBlock>

<Callout icon="📘" theme="info">
  **Note**: At least one of the above parameters must be provided.
</Callout>

## Sample request

### Non-seamless integration

```curl
curl -X POST "https://apitest.payu.in/loyalty-points/payment/v1/enquiry" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID" \
  -d '{
    "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
    "payuTxnId": "89887897898"
  }'
```
```python
import requests
import json

url = "https://apitest.payu.in/loyalty-points/payment/v1/enquiry"

headers = {
  "Content-Type": "application/json",
  "mid": "YOUR_MERCHANT_ID"
}

payload = {
  "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
  "payuTxnId": "89887897898"
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
        var url = "https://apitest.payu.in/loyalty-points/payment/v1/enquiry";
        
        client.DefaultRequestHeaders.Add("Content-Type", "application/json");
        client.DefaultRequestHeaders.Add("mid", "YOUR_MERCHANT_ID");

        var json = new
        {
            loyaltyTxnId = "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
            payuTxnId = "89887897898"
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
const url = "https://apitest.payu.in/loyalty-points/payment/v1/enquiry";

const headers = {
  "Content-Type": "application/json",
  "mid": "YOUR_MERCHANT_ID"
};

const payload = {
  "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
  "payuTxnId": "89887897898"
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
        URL url = new URL("https://apitest.payu.in/loyalty-points/payment/v1/enquiry");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("mid", "YOUR_MERCHANT_ID");

        Gson gson = new Gson();
        String jsonInputString = "{\"loyaltyTxnId\":\"bd1a77b6-1596-46e1-b79f-2770bcb636c7\",\"payuTxnId\":\"89887897898\"}";
        
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

$url = "https://apitest.payu.in/loyalty-points/payment/v1/enquiry";

$headers = [
  "Content-Type" => "application/json",
  "mid" => "YOUR_MERCHANT_ID"
];

$payload = [
  "loyaltyTxnId" => "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
  "payuTxnId" => "89887897898"
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
curl -X POST "https://apitest.payu.in/loyalty-points/payment/v1/enquiry" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{
    "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
    "payuTxnId": "89887897898"
  }'
```
```python
import requests
import json

url = "https://apitest.payu.in/loyalty-points/payment/v1/enquiry"

headers = {
  "Content-Type": "application/json",
  "Date": "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization": "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
}

payload = {
  "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
  "payuTxnId": "89887897898"
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
        var url = "https://apitest.payu.in/loyalty-points/payment/v1/enquiry";
        
        client.DefaultRequestHeaders.Add("Content-Type", "application/json");
        client.DefaultRequestHeaders.Add("Date", "Wed, 08 Sep 2025 13:22:43 GMT");
        client.DefaultRequestHeaders.Add("Authorization", "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"");

        var json = new
        {
            loyaltyTxnId = "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
            payuTxnId = "89887897898"
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
const url = "https://apitest.payu.in/loyalty-points/payment/v1/enquiry";

const headers = {
  "Content-Type": "application/json",
  "Date": "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization": "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
};

const payload = {
  "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
  "payuTxnId": "89887897898"
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
        URL url = new URL("https://apitest.payu.in/loyalty-points/payment/v1/enquiry");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("Date", "Wed, 08 Sep 2025 13:22:43 GMT");
        conn.setRequestProperty("Authorization", "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"");

        Gson gson = new Gson();
        String jsonInputString = "{\"loyaltyTxnId\":\"bd1a77b6-1596-46e1-b79f-2770bcb636c7\",\"payuTxnId\":\"89887897898\"}";
        
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

$url = "https://apitest.payu.in/loyalty-points/payment/v1/enquiry";

$headers = [
  "Content-Type" => "application/json",
  "Date" => "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization" => "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
];

$payload = [
  "loyaltyTxnId" => "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
  "payuTxnId" => "89887897898"
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

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        status
      </td>

      <td>
        `String` - Transaction processing status. For example, SUCCESS, PENDING, or FAILED
      </td>

      <td>
        `"SUCCESS"`
      </td>
    </tr>

    <tr>
      <td>
        merchantKey
      </td>

      <td>
        `String` - Unique merchant key for tracking purposes
      </td>

      <td>
        `"123ParentMerchantKey"`
      </td>
    </tr>

    <tr>
      <td>
        loyaltyTxnId
      </td>

      <td>
        `String` - Reference ID used for the loyalty transaction
      </td>

      <td>
        `"1821b1e2-
                34dd-
                47e3-
                9b54-
                b56b9d352a6b"`
      </td>
    </tr>

    <tr>
      <td>
        payuTxnId
      </td>

      <td>
        `String` - PayU transaction ID linked to the loyalty transaction
      </td>

      <td>
        `"89887897898111"`
      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        `Number` - Amount being processed in the transaction
      </td>

      <td>
        `10.00`
      </td>
    </tr>

    <tr>
      <td>
        phoneNumber
      </td>

      <td>
        `String` - Masked mobile number of the user
      </td>

      <td>
        `"88001085**"`
      </td>
    </tr>

    <tr>
      <td>
        rewardPartnerRefId
      </td>

      <td>
        `String` - Partner reference ID used for reconciliation
      </td>

      <td>
        `"7251650385664368640"`
      </td>
    </tr>

    <tr>
      <td>
        checksum
      </td>

      <td>
        `String` - SHA-512 hash for validation and verification
      </td>

      <td>
        `"fdcd69afce1ac4910d89772
                7f9c2beb372b9569df7fcad37
                4be52ab1d6ee6588771783e0e1
                574c49dc40d65d8bca5baf4787
                f2515d4cba6ebf1dc1d859f98c8f"`
      </td>
    </tr>

    <tr>
      <td>
        issueCode
      </td>

      <td>
        `String` - Error code (for failure responses)
      </td>

      <td>
        `"LS404-401"`
      </td>
    </tr>

    <tr>
      <td>
        errorMessage
      </td>

      <td>
        `String` - Error description (for failure responses)
      </td>

      <td>
        `"Transaction details not present in the DB"`
      </td>
    </tr>

    <tr>
      <td>
        errorType
      </td>

      <td>
        `String` - Type of error (for failure responses)
      </td>

      <td>
        `"VALIDATION_EXCEPTION"`
      </td>
    </tr>
  </tbody>
</Table>

## Sample response

### Success scenario

```json
{
  "status": "SUCCESS",
  "merchantKey": "123ParentMerchantKey",
  "payuTxnId": "89887897898111",
  "loyaltyTxnId": "1821b1e2-34dd-47e3-9b54-b56b9d352a6b",
  "amount": 10.00,
  "phoneNumber": "88001085**",
  "rewardPartnerRefId": "7251650385664368640",
  "checksum": "fdcd69afce1ac4910d897727f9c2beb372b9569df7fcad374be52ab1d6ee6588771783e0e1574c49dc40d65d8bca5baf4787f2515d4cba6ebf1dc1d859f98c8f"
}
```

## Failure scenario

```json
{
  "issueCode": "LS404-401",
  "errorMessage": "Transaction details not present in the DB",
  "errorType": "VALIDATION_EXCEPTION"
}
```
