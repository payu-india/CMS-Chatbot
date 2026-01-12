---
title: MCP Lookup API
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: MCP Lookup V2 API
deprecated: false
hidden: false
metadata:
  title: MCP Lookup V2 API
  description: >-
    API documentation for MCP Lookup V2 for Seamless and SDK merchants to fetch MCP lookup ID.
  keywords:
    - MCP Lookup
    - Multi-Currency Pricing
    - MCP 2.0
    - Cross-border Payments
  robots: index
---

The MCP Lookup V2 API allows merchants to fetch MCP (Multi-Currency Pricing) lookup IDs for seamless and SDK integrations. 

<Callout icon="📘" theme="info">
  **Notes**:

  * The signature must be calculated using the exact order of parameters . For more information, refer to [Signature Calculation](#signature-calculation).
  * For 3DS2 compliance, ensure your integration supports the latest authentication flow.
</Callout>

## Environment

| Environment | URL                                  |
| ----------- | ------------------------------------ |
| Production  | `https://secure.payu.in/McpLookupV2` |

## Request Parameters

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
        key <br /> <code>mandatory</code>
      </td>

      <td>
        <code>String</code> Your merchant key provided by PayU
      </td>

      <td>
        MERCHANT_KEY
      </td>
    </tr>

    <tr>
      <td>
        baseAmount <br /> <code>mandatory</code>
      </td>

      <td>
        <code>Object</code> Contains value and currency fields for the base transaction amount. For more information, refer to base [baseAmount JSON Object](baseamount-json-object).
      </td>

      <td>
        \{"value": 100, "currency": "INR"}
      </td>
    </tr>

    <tr>
      <td>
        ccNum <br /> <code>mandatory</code>
      </td>

      <td>
        <code>String</code> The card number for MCP lookup
      </td>

      <td>
        4111111111111111
      </td>
    </tr>

    <tr>
      <td>
        merchantOrderId <br /> <code>mandatory</code>
      </td>

      <td>
        <code>String</code> Unique merchant reference for the order.   
        **Note**:  Use the same **txnId** value, that you will be sending to PayU for payment processing.
      </td>

      <td>
        63d8bf8c8b95a999000000000740
      </td>
    </tr>

    <tr>
      <td>
        productType <br /> <code>mandatory</code>
      </td>

      <td>
        <code>String</code> Type of product. Must be set to MCP.  <br /> **Note:**
        Ensure the `productType` is always set to `MCP`.
      </td>

      <td>
        MCP
      </td>
    </tr>

    <tr>
      <td>
        signature <br /> <code>mandatory</code>
      </td>

      <td>
        <code>String</code> SHA512 hash signature for authentication. For more information, refer to [Signature Calculation](#signature-calculation) .
      </td>

      <td>
        \<Your_Signature>
      </td>
    </tr>
  </tbody>
</Table>

### baseAmount JSON Object

#### Sample JSON object

```
{"value": 100, "currency": "INR"}
```

#### Field Descriptions

| Field                                             | Description                                               |     |
| ------------------------------------------------- | --------------------------------------------------------- | --- |
| baseAmount.value <br /> <code>mandatory</code>    | <code>Integer</code> The transaction amount value         | 100 |
| baseAmount.currency <br /> <code>mandatory</code> | <code>String</code> The currency code for the transaction | INR |

### Signature Calculation

The signature is calculated using SHA512 hash of the pipe-separated values of the request body concatenated with the merchant salt.

#### Sample Code for Signature Calculation (JavaScript)

```javascript
// Variables
var salt = "YOUR_MERCHANT_SALT";
var body = JSON.parse(pm.request.body);
console.log("Request body", body);

function getPipeSeparatedValues(jsonObj) {
    let pipeSeparatedValuesStr = '';
    for (const key in jsonObj) {
        if (typeof jsonObj[key] === 'object') {
            for (const innerKey in jsonObj[key]) {
                pipeSeparatedValuesStr += `${jsonObj[key][innerKey]}|`;
            }
        } else {
            pipeSeparatedValuesStr += `${jsonObj[key]}|`;
        }
    }
    return pipeSeparatedValuesStr;
}

console.log(getPipeSeparatedValues(body));
delete body.signature;
var dataString = getPipeSeparatedValues(body) + salt;
console.log("Plain string to be encrypted", dataString);
var result = CryptoJS.SHA512(dataString);
postman.setGlobalVariable("mpiBIZSignature", result);
```

### Hash Formula

```
signature = SHA512(key|baseAmount.value|baseAmount.currency|ccNum|merchantOrderId|productType|salt)
```

## Sample Request

```curl
curl -X POST "https://secure.payu.in/McpLookupV2" \
-H "Content-Type: application/json" \
-d '{
  "key": "YOUR_MERCHANT_KEY",
  "baseAmount": {
    "value": 100,
    "currency": "INR"
  },
  "ccNum": "4111111111111111",
  "merchantOrderId": "63d8bf8c8b95a999000000000740",
  "productType": "MCP",
  "signature": "YOUR_SIGNATURE"
}'
```
```python
import requests
import json

url = "https://secure.payu.in/McpLookupV2"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "key": "YOUR_MERCHANT_KEY",
    "baseAmount": {
        "value": 100,
        "currency": "INR"
    },
    "ccNum": "4111111111111111",
    "merchantOrderId": "63d8bf8c8b95a999000000000740",
    "productType": "MCP",
    "signature": "YOUR_SIGNATURE"
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
        var client = new HttpClient();
        var url = "https://secure.payu.in/McpLookupV2";
        
        var payload = @"{
            ""key"": ""YOUR_MERCHANT_KEY"",
            ""baseAmount"": {
                ""value"": 100,
                ""currency"": ""INR""
            },
            ""ccNum"": ""4111111111111111"",
            ""merchantOrderId"": ""63d8bf8c8b95a999000000000740"",
            ""productType"": ""MCP"",
            ""signature"": ""YOUR_SIGNATURE""
        }";
        var content = new StringContent(payload, Encoding.UTF8, "application/json");
        
        var response = await client.PostAsync(url, content);
        var responseBody = await response.Content.ReadAsStringAsync();
        
        Console.WriteLine($"Status Code: {(int)response.StatusCode}");
        Console.WriteLine($"Response: {responseBody}");
    }
}
```
```javascript
const url = "https://secure.payu.in/McpLookupV2";

const headers = {
    "Content-Type": "application/json"
};

const payload = {
    "key": "YOUR_MERCHANT_KEY",
    "baseAmount": {
        "value": 100,
        "currency": "INR"
    },
    "ccNum": "4111111111111111",
    "merchantOrderId": "63d8bf8c8b95a999000000000740",
    "productType": "MCP",
    "signature": "YOUR_SIGNATURE"
};

const makeRequest = async () => {
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
};

makeRequest();
```
```java
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

public class McpLookupRequest {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://secure.payu.in/McpLookupV2");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        conn.setRequestProperty("Content-Type", "application/json");
        
        String jsonInputString = "{\"key\":\"YOUR_MERCHANT_KEY\",\"baseAmount\":{\"value\":100,\"currency\":\"INR\"},\"ccNum\":\"4111111111111111\",\"merchantOrderId\":\"63d8bf8c8b95a999000000000740\",\"productType\":\"MCP\",\"signature\":\"YOUR_SIGNATURE\"}";
        
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

$url = "https://secure.payu.in/McpLookupV2";

$headers = array(
    "Content-Type: application/json"
);

$payload = json_encode(array(
    "key" => "YOUR_MERCHANT_KEY",
    "baseAmount" => array(
        "value" => 100,
        "currency" => "INR"
    ),
    "ccNum" => "4111111111111111",
    "merchantOrderId" => "63d8bf8c8b95a999000000000740",
    "productType" => "MCP",
    "signature" => "YOUR_SIGNATURE"
));

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```

## Response Parameters

| Parameter                                                            | Description                                                                     | Example                              |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------ |
| resultCode <br /> <code>mandatory</code>                             | <code>Integer</code> Result code of the API call. 0 indicates success.          | 0                                    |
| resultMessage <br /> <code>mandatory</code>                          | <code>String</code> Description of the result                                   | SUCCESS                              |
| baseAmount <br /> <code>mandatory</code>                             | <code>Object</code> The base amount echoed back with value and currency         | \{"value": 10000, "currency": "INR"} |
| supportedCardSchemes <br /> <code>optional</code>                    | <code>Array</code> List of supported card schemes for MCP                       | []                                   |
| mcpConversionBeans <br /> <code>mandatory</code>                     | <code>Array</code> Array of MCP conversion details containing offer information | See sample response                  |
| mcpConversionBeans[].offerAmount <br /> <code>mandatory</code>       | <code>Float</code> The converted offer amount in the target currency            | 182.3                                |
| mcpConversionBeans[].offerCurrency <br /> <code>mandatory</code>     | <code>String</code> The target currency code for the offer                      | USD                                  |
| mcpConversionBeans[].offerExchangeRate <br /> <code>mandatory</code> | <code>Float</code> The exchange rate used for conversion                        | 0.01823                              |
| mcpConversionBeans[].merchantOrderId <br /> <code>mandatory</code>   | <code>String</code> The merchant order ID echoed back                           | 63d8bf8c8b95a999000000000740         |
| mcpConversionBeans[].lookupId <br /> <code>mandatory</code>          | <code>String</code> The unique MCP lookup ID for this conversion                | MCP6913813325270050797               |
| mcpConversionBeans[].createdAt <br /> <code>mandatory</code>         | <code>Integer</code> Timestamp of when the lookup was created                   | 1675149047431                        |

## Sample Response

### Success Response

<Callout icon="📘" theme="info">
  **Note**: `lookupId` should be passed during the **_payment** API, under the UDF to identify the conversion lookup specifically.
</Callout>

```json
{
    "resultCode": 0,
    "resultMessage": "SUCCESS",
    "baseAmount": {
        "value": 10000,
        "currency": "INR"
    },
    "supportedCardSchemes": [],
    "mcpConversionBeans": [
        {
            "offerAmount": 182.3,
            "offerCurrency": "USD",
            "offerExchangeRate": 0.01823,
            "merchantOrderId": "63d8bf8c8b95a999000000000740",
            "lookupId": "MCP6913813325270050797",
            "createdAt": 1675149047431
        }
    ]
}
```

> **Note**: The token value in mcpConversionBeans has been trimmed in this example.
