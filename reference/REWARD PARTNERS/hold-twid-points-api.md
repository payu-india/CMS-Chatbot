---
title: Hold TWID Points API
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Hold TWID Points API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Hold TWID Points** API is used to hold (reserve) reward points for a specific transaction before proceeding to final payment.

## Environment

|            |                                                          |
| :--------- | :------------------------------------------------------- |
| Production | https://api.payu.in/loyalty-points/payment/v1/createPayment |
| Test       | https://apitest.payu.in/loyalty-points/payment/v1/createPayment |

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
        surl <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Success URL after holding points
      </td>
      <td style={{ textAlign: "left" }}>
        http://api.payu.in/success
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        furl <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Failure URL after holding points
      </td>
      <td style={{ textAlign: "left" }}>
        http://api.payu.in/failure
      </td>
    </tr>
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
        email <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> User's email address
      </td>
      <td style={{ textAlign: "left" }}>
        test@gmail.com
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        merchantTxnId <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Merchant transaction ID
      </td>
      <td style={{ textAlign: "left" }}>
        23645445001793
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        currency <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Currency code
      </td>
      <td style={{ textAlign: "left" }}>
        INR
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
        firstName <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> User's first name
      </td>
      <td style={{ textAlign: "left" }}>
        First name
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        lastName <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> User's last name
      </td>
      <td style={{ textAlign: "left" }}>
        Last name
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        rewardId <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>Number</code> Twid reward ID
      </td>
      <td style={{ textAlign: "left" }}>
        270940
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
    <tr>
      <td style={{ textAlign: "left" }}>
        cardLastFour <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Last four digits of the payment card
      </td>
      <td style={{ textAlign: "left" }}>
        2321
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        cardBin <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Bank Identification Number of the payment card
      </td>
      <td style={{ textAlign: "left" }}>
        213213
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        authCode <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Authorization code from payment processing
      </td>
      <td style={{ textAlign: "left" }}>
        213213
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        twidMode <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Payment mode indicator (CC=Credit Card, DC=Debit Card, OTHERS)
      </td>
      <td style={{ textAlign: "left" }}>
        CC
      </td>
    </tr>
  </tbody>
</Table>
`}</HTMLBlock>

## Sample request

### Non-seamless Integration

```curl
curl -X POST "{{loyalty-service-url}}/payment/v1/createPayment" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID" \
  -d '{
    "surl": "http://api.payu.in/success",
    "furl": "http://api.payu.in/failure",
    "merchantKey": "18001",
    "parentPayuTxnId": "65646400234509041",
    "totalAmount": 1000,
    "mobile": "9304204**",
    "email": "test@gmail.com",
    "merchantTxnId": "23645445001793",
    "currency": "INR",
    "loyaltyProvider": "TWID",
    "firstName": "First name",
    "lastName": "Last name",
    "rewardId": 270940,
    "orderAmount": 10000,
    "cardLastFour": "2321",
    "cardBin": "213213",
    "authCode": "213213",
    "twidMode": "CC"
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
  "surl": "http://api.payu.in/success",
  "furl": "http://api.payu.in/failure",
  "merchantKey": "18001",
  "parentPayuTxnId": "65646400234509041",
  "totalAmount": 1000,
  "mobile": "9304204**",
  "email": "test@gmail.com",
  "merchantTxnId": "23645445001793",
  "currency": "INR",
  "loyaltyProvider": "TWID",
  "firstName": "First name",
  "lastName": "Last name",
  "rewardId": 270940,
  "orderAmount": 10000,
  "cardLastFour": "2321",
  "cardBin": "213213",
  "authCode": "213213",
  "twidMode": "CC"
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
            surl = "http://api.payu.in/success",
            furl = "http://api.payu.in/failure",
            merchantKey = "18001",
            parentPayuTxnId = "65646400234509041",
            totalAmount = 1000,
            mobile = "9304204**",
            email = "test@gmail.com",
            merchantTxnId = "23645445001793",
            currency = "INR",
            loyaltyProvider = "TWID",
            firstName = "First name",
            lastName = "Last name",
            rewardId = 270940,
            orderAmount = 10000,
            cardLastFour = "2321",
            cardBin = "213213",
            authCode = "213213",
            twidMode = "CC"
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
  "surl": "http://api.payu.in/success",
  "furl": "http://api.payu.in/failure",
  "merchantKey": "18001",
  "parentPayuTxnId": "65646400234509041",
  "totalAmount": 1000,
  "mobile": "9304204**",
  "email": "test@gmail.com",
  "merchantTxnId": "23645445001793",
  "currency": "INR",
  "loyaltyProvider": "TWID",
  "firstName": "First name",
  "lastName": "Last name",
  "rewardId": 270940,
  "orderAmount": 10000,
  "cardLastFour": "2321",
  "cardBin": "213213",
  "authCode": "213213",
  "twidMode": "CC"
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
        String jsonInputString = "{\"surl\":\"http://api.payu.in/success\",\"furl\":\"http://api.payu.in/failure\",\"merchantKey\":\"18001\",\"parentPayuTxnId\":\"65646400234509041\",\"totalAmount\":1000,\"mobile\":\"9304204**\",\"email\":\"test@gmail.com\",\"merchantTxnId\":\"23645445001793\",\"currency\":\"INR\",\"loyaltyProvider\":\"TWID\",\"firstName\":\"First name\",\"lastName\":\"Last name\",\"rewardId\":270940,\"orderAmount\":10000,\"cardLastFour\":\"2321\",\"cardBin\":\"213213\",\"authCode\":\"213213\",\"twidMode\":\"CC\"}";
        
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
  "surl" => "http://api.payu.in/success",
  "furl" => "http://api.payu.in/failure",
  "merchantKey" => "18001",
  "parentPayuTxnId" => "65646400234509041",
  "totalAmount" => 1000,
  "mobile" => "9304204**",
  "email" => "test@gmail.com",
  "merchantTxnId" => "23645445001793",
  "currency" => "INR",
  "loyaltyProvider" => "TWID",
  "firstName" => "First name",
  "lastName" => "Last name",
  "rewardId" => 270940,
  "orderAmount" => 10000,
  "cardLastFour" => "2321",
  "cardBin" => "213213",
  "authCode" => "213213",
  "twidMode" => "CC"
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
curl -X POST "{{loyalty-service-url}}/payment/v1/createPayment" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{
    "surl": "http://api.payu.in/success",
    "furl": "http://api.payu.in/failure",
    "merchantKey": "18001",
    "parentPayuTxnId": "65646400234509041",
    "totalAmount": 1000,
    "mobile": "9304204**",
    "email": "test@gmail.com",
    "merchantTxnId": "23645445001793",
    "currency": "INR",
    "loyaltyProvider": "TWID",
    "firstName": "First name",
    "lastName": "Last name",
    "rewardId": 270940,
    "orderAmount": 10000,
    "cardLastFour": "2321",
    "cardBin": "213213",
    "authCode": "213213",
    "twidMode": "CC"
  }'
```

```python
import requests
import json

url = "{{loyalty-service-url}}/payment/v1/createPayment"

headers = {
  "Content-Type": "application/json",
  "Date": "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization": "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
}

payload = {
  "surl": "http://api.payu.in/success",
  "furl": "http://api.payu.in/failure",
  "merchantKey": "18001",
  "parentPayuTxnId": "65646400234509041",
  "totalAmount": 1000,
  "mobile": "9304204**",
  "email": "test@gmail.com",
  "merchantTxnId": "23645445001793",
  "currency": "INR",
  "loyaltyProvider": "TWID",
  "firstName": "First name",
  "lastName": "Last name",
  "rewardId": 270940,
  "orderAmount": 10000,
  "cardLastFour": "2321",
  "cardBin": "213213",
  "authCode": "213213",
  "twidMode": "CC"
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
        client.DefaultRequestHeaders.Add("Date", "Wed, 08 Sep 2025 13:22:43 GMT");
        client.DefaultRequestHeaders.Add("Authorization", "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"");

        var json = new
        {
            surl = "http://api.payu.in/success",
            furl = "http://api.payu.in/failure",
            merchantKey = "18001",
            parentPayuTxnId = "65646400234509041",
            totalAmount = 1000,
            mobile = "9304204**",
            email = "test@gmail.com",
            merchantTxnId = "23645445001793",
            currency = "INR",
            loyaltyProvider = "TWID",
            firstName = "First name",
            lastName = "Last name",
            rewardId = 270940,
            orderAmount = 10000,
            cardLastFour = "2321",
            cardBin = "213213",
            authCode = "213213",
            twidMode = "CC"
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
  "Date": "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization": "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
};

const payload = {
  "surl": "http://api.payu.in/success",
  "furl": "http://api.payu.in/failure",
  "merchantKey": "18001",
  "parentPayuTxnId": "65646400234509041",
  "totalAmount": 1000,
  "mobile": "9304204**",
  "email": "test@gmail.com",
  "merchantTxnId": "23645445001793",
  "currency": "INR",
  "loyaltyProvider": "TWID",
  "firstName": "First name",
  "lastName": "Last name",
  "rewardId": 270940,
  "orderAmount": 10000,
  "cardLastFour": "2321",
  "cardBin": "213213",
  "authCode": "213213",
  "twidMode": "CC"
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
        conn.setRequestProperty("Date", "Wed, 08 Sep 2025 13:22:43 GMT");
        conn.setRequestProperty("Authorization", "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"");

        Gson gson = new Gson();
        String jsonInputString = "{\"surl\":\"http://api.payu.in/success\",\"furl\":\"http://api.payu.in/failure\",\"merchantKey\":\"18001\",\"parentPayuTxnId\":\"65646400234509041\",\"totalAmount\":1000,\"mobile\":\"9304204**\",\"email\":\"test@gmail.com\",\"merchantTxnId\":\"23645445001793\",\"currency\":\"INR\",\"loyaltyProvider\":\"TWID\",\"firstName\":\"First name\",\"lastName\":\"Last name\",\"rewardId\":270940,\"orderAmount\":10000,\"cardLastFour\":\"2321\",\"cardBin\":\"213213\",\"authCode\":\"213213\",\"twidMode\":\"CC\"}";
        
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
  "Date" => "Wed, 08 Sep 2025 13:22:43 GMT",
  "Authorization" => "hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
];

$payload = [
  "surl" => "http://api.payu.in/success",
  "furl" => "http://api.payu.in/failure",
  "merchantKey" => "18001",
  "parentPayuTxnId" => "65646400234509041",
  "totalAmount" => 1000,
  "mobile" => "9304204**",
  "email" => "test@gmail.com",
  "merchantTxnId" => "23645445001793",
  "currency" => "INR",
  "loyaltyProvider" => "TWID",
  "firstName" => "First name",
  "lastName" => "Last name",
  "rewardId" => 270940,
  "orderAmount" => 10000,
  "cardLastFour" => "2321",
  "cardBin" => "213213",
  "authCode" => "213213",
  "twidMode" => "CC"
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

| Parameter          | Description                                              | Example                                  |
| ------------------ | -------------------------------------------------------- | ---------------------------------------- |
| statusCode         | `Number` - Indicates successful transaction (1=success)  | `1`                                      |
| status             | `String` - Transaction status (PENDING, SUCCESS, FAILED) | `"PENDING"`                              |
| loyaltyTxnId       | `String` - Unique loyalty transaction ID for tracking    | `"d1dce98d-98ec-4b90-a7d8-853fee82a113"` |
| rewardPartnerRefId | `String` - Reference ID from the reward provider         | `null`                                   |

## Sample response

```json
{
  "statusCode": 1,
  "status": "PENDING",
  "loyaltyTxnId": "d1dce98d-98ec-4b90-a7d8-853fee82a113",
  "rewardPartnerRefId": null
}
```
