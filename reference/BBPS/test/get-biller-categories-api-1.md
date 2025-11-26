---
title: Get Biller Categories API
deprecated: false
hidden: true
metadata:
  robots: index
---
This API fetches all available biller categories from PayU's BBPS system.

***

## API Endpoint

|            |                                                           |
| :--------- | :-------------------------------------------------------- |
| **URL**    | `https://<hostName>/payu-nbc/v1/nbc/getAllBillerCategory` |
| **Method** | GET                                                       |
| **Scope**  | `read_biller_categories`                                  |

***

## Headers

| Parameter                      | Description                            | Example                    |
| :----------------------------- | :------------------------------------- | :------------------------- |
| Authorization<br />`mandatory` | `String` - Bearer token from OAuth API | Bearer eyJhbGciOiJIUzI1... |
| Content-Type<br />`mandatory`  | `String` - Content type of the request | application/json           |

***

## Response Parameters

| Parameter                                 | Description                                   | Example               |
| :---------------------------------------- | :-------------------------------------------- | :-------------------- |
| code<br />`mandatory`                     | `Integer` - Global response code              | 200                   |
| status<br />`mandatory`                   | `String` - SUCCESS or FAILURE                 | SUCCESS               |
| payload<br />`mandatory`                  | `Object` - Contains the response data         |                       |
| payload.billerCategories<br />`mandatory` | `Array` - List of available biller categories | ["INSURANCE", "LOAN"] |

***

## Sample Request

```bash
curl -X GET \
  'https://bbps-sb.payu.in/payu-nbc/v1/nbc/getAllBillerCategory' \
  -H 'Authorization: Bearer <access_token>' \
  -H 'Content-Type: application/json'
```

```python
import requests

url = "https://bbps-sb.payu.in/payu-nbc/v1/nbc/getAllBillerCategory"

headers = {
    'Authorization': 'Bearer <access_token>',
    'Content-Type': 'application/json'
}

try:
    response = requests.get(url, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

```csharp
using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://bbps-sb.payu.in/payu-nbc/v1/nbc/getAllBillerCategory";
            
            client.DefaultRequestHeaders.Clear();
            client.DefaultRequestHeaders.Add("Authorization", "Bearer <access_token>");
            
            HttpResponseMessage response = await client.GetAsync(url);
            string responseContent = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseContent}");
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}
```

```javascript
async function getBillerCategories() {
    const url = 'https://bbps-sb.payu.in/payu-nbc/v1/nbc/getAllBillerCategory';
    
    const requestOptions = {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer <access_token>',
            'Content-Type': 'application/json'
        }
    };
    
    try {
        const response = await fetch(url, requestOptions);
        const responseData = await response.json();
        
        console.log(`Status: ${response.status}`);
        console.log(`Response:`, responseData);
        
        return responseData;
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

// Usage
getBillerCategories()
    .then(result => console.log('Categories:', result.payload.billerCategories))
    .catch(error => console.error('Failed:', error));
```

```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class GetBillerCategories {
    
    public static void main(String[] args) {
        try {
            getBillerCategories();
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
    
    public static void getBillerCategories() throws IOException {
        String url = "https://bbps-sb.payu.in/payu-nbc/v1/nbc/getAllBillerCategory";
        
        URL urlObj = new URL(url);
        HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
        
        connection.setRequestMethod("GET");
        connection.setRequestProperty("Authorization", "Bearer <access_token>");
        connection.setRequestProperty("Content-Type", "application/json");
        
        int responseCode = connection.getResponseCode();
        System.out.println("Status Code: " + responseCode);
        
        try (BufferedReader br = new BufferedReader(new InputStreamReader(
                responseCode >= 200 && responseCode < 300 
                    ? connection.getInputStream() 
                    : connection.getErrorStream(), StandardCharsets.UTF_8))) {
            
            StringBuilder response = new StringBuilder();
            String responseLine;
            while ((responseLine = br.readLine()) != null) {
                response.append(responseLine.trim());
            }
            System.out.println("Response: " + response.toString());
        }
        
        connection.disconnect();
    }
}
```

```php
<?php

function getBillerCategories() {
    $url = 'https://bbps-sb.payu.in/payu-nbc/v1/nbc/getAllBillerCategory';
    
    $curl = curl_init();
    
    curl_setopt_array($curl, array(
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPGET => true,
        CURLOPT_HTTPHEADER => array(
            'Authorization: Bearer <access_token>',
            'Content-Type: application/json'
        ),
        CURLOPT_TIMEOUT => 30,
        CURLOPT_SSL_VERIFYPEER => true,
        CURLOPT_SSL_VERIFYHOST => 2
    ));
    
    $response = curl_exec($curl);
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    $error = curl_error($curl);
    
    curl_close($curl);
    
    if ($error) {
        echo "cURL Error: " . $error . PHP_EOL;
        return false;
    }
    
    echo "Status Code: " . $httpCode . PHP_EOL;
    echo "Response: " . $response . PHP_EOL;
    
    return json_decode($response, true);
}

// Usage
$result = getBillerCategories();
if ($result && isset($result['payload']['billerCategories'])) {
    print_r($result['payload']['billerCategories']);
}

?>
```

***

## Sample Response

### Success Response

```json
{
  "code": 200,
  "status": "SUCCESS",
  "payload": {
    "billerCategories": [
      "INSURANCE",
      "LOAN",
      "EDUCATION",
      "SOCIETY BILLER",
      "ELECTRICITY",
      "GAS",
      "WATER",
      "BROADBAND",
      "DTH",
      "MOBILE POSTPAID",
      "MOBILE PREPAID",
      "LANDLINE",
      "FASTAG"
    ]
  }
}
```

### Failure Response

```json
{
  "code": 600,
  "status": "FAILURE",
  "payload": {
    "errors": [
      {
        "reason": "Invalid authorization token",
        "errorCode": "AUTH_001"
      }
    ],
    "refId": null,
    "type": "category_response",
    "message": "category_response_failed",
    "additionalParams": null
  }
}
```

***

## Error Response Parameters

| Parameter                                   | Description                                       | Example                     |
| :------------------------------------------ | :------------------------------------------------ | :-------------------------- |
| code<br />`mandatory`                       | `Integer` - Global response code                  | 600                         |
| status<br />`mandatory`                     | `String` - SUCCESS or FAILURE                     | FAILURE                     |
| payload.errors<br />`mandatory`             | `Array` - List of error objects                   |                             |
| payload.errors[].reason<br />`mandatory`    | `String` - Error description                      | Invalid authorization token |
| payload.errors[].errorCode<br />`mandatory` | `String` - Error code                             | AUTH_001                    |
| payload.refId<br />`optional`               | `String` - Reference ID (null for category fetch) | null                        |
| payload.type<br />`mandatory`               | `String` - Type of error                          | category_response           |
| payload.message<br />`mandatory`            | `String` - Error message                          | category_response_failed    |
| payload.additionalParams<br />`optional`    | `Object` - Additional fields if available         | null                        |