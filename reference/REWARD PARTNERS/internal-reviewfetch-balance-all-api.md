---
title: '[Internal Review]Fetch Balance All API'
deprecated: false
hidden: true
metadata:
  robots: index
---
This API is used to fetch all the reward balances for a customer. It can be used before calling the Collect Payment API (\_payment) to check if the customer has the balance. &#x20;

## Environment

|            |                                                                                                                |
| :--------- | :------------------------------------------------------------------------------------------------------------- |
| Production | [https://api.payu.in/loyalty-points/v1/balance/all](https://api.payu.in/loyalty-points/v1/balance/all)         |
| Test       | [https://apitest.payu.in/loyalty-points/v1/balance/all](https://apitest.payu.in/loyalty-points/v1/balance/all) |

HTTP Method: **POST**

## Request header

<LoyaltyPointsHeaderAuthentication />

<br />

## Request Parameters

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
        mobileNumber <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> User's mobile number (can be masked for privacy)
      </td>
      <td style={{ textAlign: "left" }}>
        "930420****"
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        loyaltyProviders <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>Array</code> Array of loyalty provider names to fetch rewards from. Supported values: "TWID", "ZILLION"
      </td>
      <td style={{ textAlign: "left" }}>
        ["TWID"]
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        orderAmount <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>Number</code> Order amount (in INR) for which reward points are applicable
      </td>
      <td style={{ textAlign: "left" }}>
        5000
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        loyaltyApiVersion <br/>
        <code>mandatory</code> <span style={{ color: "red" }}>NEW</span>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>Number</code> Identifies the TWID API flow. 0 = legacy path; 1 = new routing. <strong>Note:</strong> This field may be deprecated in the future.
      </td>
      <td style={{ textAlign: "left" }}>
        1
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        sessionId <br/>
        <code>mandatory</code> <span style={{ color: "red" }}>NEW</span>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Required to fetch the balance from TWID. <strong>The same sessionId must also be passed in the _payment request inside the loyaltyDetails block of the split-info JSON.</strong>
      </td>
      <td style={{ textAlign: "left" }}>
        "sessionId11323"
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        merchantTxnId <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Merchant-generated transaction reference identifier for tracking the balance lookup against the order
      </td>
      <td style={{ textAlign: "left" }}>
        "123merchantTxnId"
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        fetchRevisedEarn <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>Boolean</code> When set to true, the response includes the revised earn configuration (revisedEarnConfig) for each reward
      </td>
      <td style={{ textAlign: "left" }}>
        true
      </td>
    </tr>
  </tbody>
</Table>
`}</HTMLBlock>

<Callout icon="⚠️" theme="warn">
  ### **Notes**

  The Fetch Balance API remains the same as the older version, with **two additional parameters** required for the new TWID flow:

  - `loyaltyApiVersion`: Identifies the new TWID API flow. This field may be deprecated in the future.
  - `sessionId`: Required to fetch the balance from TWID. **The same&#x20;**`sessionId`**&#x20;must also be passed in the&#x20;**`_payment`**&#x20;request inside the&#x20;**`loyaltyDetails`**&#x20;block of the&#x20;**`split-info`**&#x20;JSON.**
</Callout>

## Sample request

### TWID Flow (Recommended)

```curl
curl --location 'https://apitest.payu.in/loyalty-points/v1/balance/all' \
--header 'mid: YOUR_MERCHANT_ID' \
--header 'Content-Type: application/json' \
--data '{
  "mobileNumber": "930420****",
  "loyaltyProviders": ["TWID"],
  "orderAmount": 5000,
  "loyaltyApiVersion": 1,
  "sessionId": "sessionId11323"
}'
```
```python
import requests
import json

url = "https://apitest.payu.in/loyalty-points/v1/balance/all"

headers = {
  "mid": "YOUR_MERCHANT_ID",
  "Content-Type": "application/json"
}

payload = {
  "mobileNumber": "930420****",
  "loyaltyProviders": ["TWID"],
  "orderAmount": 5000,
  "loyaltyApiVersion": 1,
  "sessionId": "sessionId11323"
}

response = requests.post(url, headers=headers, json=payload)
print("Status Code:", response.status_code)
print("Response:", response.json())
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
        var url = "https://apitest.payu.in/loyalty-points/v1/balance/all";
        
        var client = new HttpClient();
        client.DefaultRequestHeaders.Add("mid", "YOUR_MERCHANT_ID");
        
        var payload = new
        {
            mobileNumber = "930420****",
            loyaltyProviders = new[] { "TWID" },
            orderAmount = 5000,
            loyaltyApiVersion = 1,
            sessionId = "sessionId11323"
        };
        
        var jsonString = JsonSerializer.Serialize(payload);
        var content = new StringContent(jsonString, Encoding.UTF8, "application/json");
        
        var response = await client.PostAsync(url, content);
        var responseBody = await response.Content.ReadAsStringAsync();
        
        Console.WriteLine($"Status Code: {(int)response.StatusCode}");
        Console.WriteLine($"Response: {responseBody}");
    }
}
```
```javascript
const url = "https://apitest.payu.in/loyalty-points/v1/balance/all";

const headers = {
  "mid": "YOUR_MERCHANT_ID",
  "Content-Type": "application/json"
};

const payload = {
  "mobileNumber": "930420****",
  "loyaltyProviders": ["TWID"],
  "orderAmount": 5000,
  "loyaltyApiVersion": 1,
  "sessionId": "sessionId11323"
};

async function makeRequest() {
    try {
        const response = await fetch(url, {
            method: "POST",
            headers: headers,
            body: JSON.stringify(payload)
        });
        
        const data = await response.json();
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

public class FetchAllBalanceAPI {
    public static void main(String[] args) throws Exception {
        String urlString = "https://apitest.payu.in/loyalty-points/v1/balance/all";
        
        URL url = new URL(urlString);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        
        conn.setRequestProperty("mid", "YOUR_MERCHANT_ID");
        conn.setRequestProperty("Content-Type", "application/json");
        
        String jsonInputString = "{\"mobileNumber\":\"930420****\",\"loyaltyProviders\":[\"TWID\"],\"orderAmount\":5000,\"loyaltyApiVersion\":1,\"sessionId\":\"sessionId11323\"}";
        
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

$url = "https://apitest.payu.in/loyalty-points/v1/balance/all";

$headers = [
    "mid: YOUR_MERCHANT_ID",
    "Content-Type: application/json"
];

$payload = [
    "mobileNumber" => "930420****",
    "loyaltyProviders" => ["TWID"],
    "orderAmount" => 5000,
    "loyaltyApiVersion" => 1,
    "sessionId" => "sessionId11323"
];

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```

### TWID and ZILLION Combined

```json
{
  "mobileNumber": "9876543210",
  "loyaltyProviders": ["TWID", "ZILLION"],
  "orderAmount": 5000,
  "loyaltyApiVersion": 1,
  "sessionId": "84664h99870030988ccr"
}
```

### With Optional Parameters

```json
{
  "mobileNumber": "930420****",
  "loyaltyProviders": ["TWID"],
  "orderAmount": 10000,
  "loyaltyApiVersion": 1,
  "sessionId": "sessionId11323",
  "merchantTxnId": "TXN-TWID-001",
  "fetchRevisedEarn": true
}
```

### Legacy Flow (Backward Compatibility)

```json
{
  "mobileNumber": "8800108522",
  "loyaltyProviders": ["TWID", "ZILLION"],
  "orderAmount": 1000,
  "loyaltyApiVersion": 0
}
```

### ZILLION Only

```json
{
  "mobileNumber": "9988776655",
  "loyaltyProviders": ["ZILLION"],
  "orderAmount": 3000,
  "loyaltyApiVersion": 1,
  "sessionId": "zillion_session_001"
}
```

### High Value Order

```json
{
  "mobileNumber": "88001085**",
  "loyaltyProviders": ["TWID"],
  "orderAmount": 25000,
  "loyaltyApiVersion": 1,
  "sessionId": "session_high_value_001"
}
```

## Response parameters

| Parameter                         | Description                                                         | Example                                    |
| --------------------------------- | ------------------------------------------------------------------- | ------------------------------------------ |
| data\[].loyaltyProvider           | `String` - Loyalty provider identifier for this response entry      | `"TWID"`                                   |
| data\[].usableAmount              | `Number` - Maximum monetary amount that can be saved                | `500.0`                                    |
| data\[].usablePoints              | `Number` - Required reward points for maximum savings               | `500`                                      |
| data\[].title                     | `String` - Display title describing the reward offer                | `"Save Rs 500 using 500 TWID Cash Points"` |
| data\[].earnConfig.points         | `Number` - Points that can be earned                                | `0`                                        |
| data\[].issuerDetailDTO.logo      | `String` - Logo URL of the brand/issuer                             | `"https://cdn.twidpay.com/brand_logo.png"` |
| data\[].holdApplicable            | `Boolean` - Indicates if points can be held for the reward          | `false`                                    |
| data\[].customErrorMessage        | `String` - Error message for specific provider (if applicable)      | `"Unable to process request for provider"` |
| data\[].rewardId                  | `Number` - Unique identifier for the reward                         | `270943`                                   |
| data\[].issuerDetailDTO.brandName | `String` - Name of the brand/issuer (used as rewardName in payment) | `"twid Cash"`, `"Woodland"`                |

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
        "brandName": "twid Cash",
        "logo": "https://cdn.twidpay.com/co/brand_images/brand_image_14b20_1651155946.png",
        "issuerType": "brand"
      },
      "rewardId": 270943,
      "holdApplicable": false,
      "rewards": [
        {
          "loyaltyProvider": "TWID",
          "usableAmount": 250.0,
          "usablePoints": 1000,
          "title": "Save Rs 250 using 1000 Woodland Points",
          "earnConfig": {
            "points": 50,
            "amount": null,
            "title": "Earn 50 Woodland Points"
          },
          "issuerDetailDTO": {
            "brandName": "Woodland",
            "logo": "https://cdn.twidpay.com/co/s2s_issuer_images/Woodland.jpg",
            "issuerType": "brand"
          },
          "rewardId": 270940,
          "holdApplicable": false
        },
        {
          "loyaltyProvider": "TWID",
          "usableAmount": 125.0,
          "usablePoints": 125,
          "title": "Save Rs 125 using 125 HDFC Bank Points",
          "earnConfig": {
            "points": 0,
            "amount": null,
            "title": null
          },
          "issuerDetailDTO": {
            "brandName": "HDFC Bank",
            "logo": "https://cdn.twidpay.com/co/s2s_issuer_images/hdfc_square.svg",
            "issuerType": "bank"
          },
          "rewardId": 270942,
          "holdApplicable": false,
          "applicableBinList": [
            "531849",
            "536303",
            "524167"
          ]
        }
      ]
    }
  ]
}
```

## Important Notes

<Callout icon="📘" theme="info">
  ### **TWID Reward Name Mapping**

  The `issuerDetailDTO.brandName` returned in the Fetch Balance response (for example, `"Woodland"`, `"HDFC Bank"`) is the value you **must pass** as `rewardName` in the `childPaymentInstruments` / `earnPaymentInstruments` array of the `_payment` request when the reward provider is **TWID**.

  **Note:** The `rewardName` field is **NOT applicable for Zillion** rewards.
</Callout>

<Callout icon="⚠️" theme="warn">
  ### **Session Consistency Requirement**

  The `sessionId` used in the Fetch Balance API request **MUST be identical** to the `sessionId` passed in the `_payment` request within the `loyaltyDetails` block of the `split-info` JSON. TWID validates this sessionId during redemption.
</Callout>

## Related Documentation

- [Collect Payment with Rewards API](_payment-merchant-hosted-rewards.md)
- [TWID Integration Guide](https://docs.payu.in)

***

**Last Updated:** August 2026<br />**Version:** 2.0 (New TWID Flow)
