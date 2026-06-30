---
title: Bank Verification API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Bank Verification API
  description: >-
    The Bank Verification API allows for the verification of bank accounts using
    a penny drop or penniless transaction, requiring an access token with
    specific scopes and client credentials for authentication.
  robots: index
next:
  description: ''
---
The **Bank Verification** API is used to verify bank account using penny drop/penniless transaction.

### Environment

| Environment            | URL                                                                                                                             |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Production Environment | [[https://onboarding.payu.in/dvs/bank_accounts/acc_verification](https://onboarding.payu.in/dvs/bank_accounts/acc_verification) |

<Callout icon="📘" theme="info">
  **Note:** The access token with the scope as **verify_bank_account** and grant type as **client_credentials** are required on the header. For more information on getting the access token, refer to [Get Token API - Bank Verification](ref:gettoken-bank-verification).
</Callout>

## Request parameters

### Header

| Parameter                                | Description                                                                                                                                                                                                                                                     |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bearer token<br /><code>mandatory</code> | The access token with the scope as **verify_bank_account** and grant type as **client_credentials** are required on the header. For more information on getting the access token, refer to [Get Token API - Bank Verification](ref:gettoken-bank-verification). |

### Body

| Parameter                                      | Description                                                                                                                                   |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| account_number<br /><code>mandatory</code>     | <code>String</code> This parameter must contain the account number to be verified.                                                            |
| ifsc<br /><code>mandatory</code>               | <code>String</code> This parameter must contain the bank IFSC code.                                                                           |
| name<br /><code>mandatory</code>               | <code>String</code> This parameter must contain the account holder name.                                                                      |
| name_match_required<br /><code>optional</code> | <code>Boolean</code> This parameter must be set to <code>true</code> if the name must match along with bank account verification.             |
| leniency<br /><code>optional</code>            | <code>String</code> If name_match_required is set to <code>true</code>, this parameter must contain any of the following:- Medium - High - Lo |

## Sample request

```curl
curl --location 'https://uat-onepayuonboarding.payu.in/dvs/bank_accounts/acc_verification' \
--header 'clientId: <client Id>' \
--header 'Content-Type: application/json' \
--header 'Authorization: ••••••' \
--header 'Cookie: Path=/' \
--data '{
"account_number": "0514100000****",
"ifsc": "HDFC0000514",
"name" : "R******* P"
}
'
```
```python
import requests
import json

url = "https://uat-onepayuonboarding.payu.in/dvs/bank_accounts/acc_verification"

headers = {
    "clientId": "<client Id>",
    "Content-Type": "application/json",
    "Authorization": "••••••",
    "Cookie": "Path=/"
}

data = {
    "account_number": "0514100000****",
    "ifsc": "HDFC0000514",
    "name": "R******* P"
}

try:
    response = requests.post(url, headers=headers, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
```javascript
async function makeRequest() {
    const url = "https://uat-onepayuonboarding.payu.in/dvs/bank_accounts/acc_verification";
    
    const headers = {
        "clientId": "<client Id>",
        "Content-Type": "application/json",
        "Authorization": "••••••",
        "Cookie": "Path=/"
    };

    const requestData = {
        "account_number": "0514100000****",
        "ifsc": "HDFC0000514",
        "name": "R******* P"
    };

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: headers,
            body: JSON.stringify(requestData)
        });
        
        const responseText = await response.text();
        console.log(`Status Code: ${response.status}`);
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

makeRequest();
```
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;

public class ApiRequest {
    public static void main(String[] args) {
        try {
            String url = "https://uat-onepayuonboarding.payu.in/dvs/bank_accounts/acc_verification";
            
            String jsonData = "{\"account_number\":\"0514100000****\",\"ifsc\":\"HDFC0000514\",\"name\":\"R******* P\"}";
            
            HttpClient client = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(10))
                .build();

            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("clientId", "<client Id>")
                .header("Content-Type", "application/json")
                .header("Authorization", "••••••")
                .header("Cookie", "Path=/")
                .POST(HttpRequest.BodyPublishers.ofString(jsonData))
                .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            
            System.out.println("Status Code: " + response.statusCode());
            System.out.println("Response: " + response.body());
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://uat-onepayuonboarding.payu.in/dvs/bank_accounts/acc_verification";
            
            client.DefaultRequestHeaders.Add("clientId", "<client Id>");
            client.DefaultRequestHeaders.Add("Authorization", "••••••");
            client.DefaultRequestHeaders.Add("Cookie", "Path=/");

            var requestData = new
            {
                account_number = "0514100000****",
                ifsc = "HDFC0000514",
                name = "R******* P"
            };

            string jsonContent = JsonConvert.SerializeObject(requestData);
            var content = new StringContent(jsonContent, Encoding.UTF8, "application/json");

            HttpResponseMessage response = await client.PostAsync(url, content);
            string responseBody = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseBody}");
        }
        catch (HttpRequestException ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
```
```php
<?php
$url = "https://uat-onepayuonboarding.payu.in/dvs/bank_accounts/acc_verification";

$headers = [
    "clientId: <client Id>",
    "Content-Type: application/json",
    "Authorization: ••••••",
    "Cookie: Path=/"
];

$requestData = [
    "account_number" => "0514100000****",
    "ifsc" => "HDFC0000514",
    "name" => "R******* P"
];

$jsonData = json_encode($requestData);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if (curl_errno($ch)) {
    echo "Error: " . curl_error($ch) . "\n";
} else {
    echo "Status Code: " . $httpCode . "\n";
    echo "Response: " . $response . "\n";
}

curl_close($ch);
?>
```


## Response parameters

| Parameter         | Description                                                                                                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| payuRequestId     | This parameter returns the PayU request ID.                                                                                                                                                 |
| result            | This parameter returns the results of the verification in a JSON format. For more information, refer to <a href="#result-json-fields-description">result JSON fields description</a> table. |
| requestAttributes | This parameter contains the following details posted in the request in a JSON format: - name - ifsc - accountNumber                                                                         |

### result JSON fields description

| Field         | Description                                                          | Example                |
| :------------ | :------------------------------------------------------------------- | :--------------------- |
| accountName   | The masked name of the account holder for privacy.                   | Ashish                 |
| bankResponse  | The response message from the bank regarding the transaction status. | Transaction successful |
| bankTxnStatus | A boolean value indicating if the bank transaction was successful.   | true                   |
| accountStatus | The current status of the account.                                   | ACTIVE                 |

## Sample response

### Success scenario

```json
{
  "payuRequestId": "ba659237-34de-4805-a5cf-ef9dd7a1cda2",
  "result": {
    "accountName": "P R*******",
    "bankResponse": "Transaction successful",
    "bankTxnStatus": "true",
    "accountStatus": "ACTIVE"
  },
  "requestAttributes": {
    "name": "R******* P",
    "ifsc": "HDFC0000514",
    "accountNumber": "0514100000****"
  }
}
```

### Failure scenario

* Missing client_id value in header

```json
{
  "error": "Missing required client_id header"
}
```

* Invalid account number

```json
{
  "payuRequestId": "0aeb7a65-cea3-4e81-9355-38548bb8f795",
  "error": {
    "reason": "Invalid account number or IFSC provided"
  },
  "requestAttributes": {
    "name": "test",
    "ifsc": "HDFC0000514",
    "accountNumber": "0514100000***",
    "verficationMode": 1
  }
}
```