---
title: Check is Domestic API
excerpt: >-
  Determines whether a particular BIN number is international or domestic and
  provides detailed card information including issuing bank, card type, and
  category.
api:
  file: check_isdomestic.json
  operationId: checkisdomestic
hidden: false
metadata:
  title: Check is Domestic API
  description: >-
    The document describes the Check is Domestic or Card BIN API, which is used
    to determine if a BIN number is international or domestic, along with other
    card details like issuing bank and card type.
  keywords:
    - check_isDomestic API Command
    - Check is Domestic API
    - Domestic transaction check API
    - Domestic transaction identification API
    - Check domestic payment API
    - Verify domestic transaction API
    - Integrating PayU Check is Domestic API
---
The **Check is Domestic** or **Card BIN** API is used to detect whether a particular BIN number is international or domestic. It is also useful to determine:

* Card's issuing bank
* Card type such as, Visa, Master, etc.
* Card category such as Credit/Debit, etc.
* var1 is bin number which is the first 6 digits of a Credit/Debit card.

<GENERALAPIsEnvironment />

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&command=check_isDomestic&var1=462273&hash=df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2"
  ```
```python
import requests

url = "https://test.payu.in/merchant/postservice?form=2"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "key": "JP***g",
    "command": "check_isDomestic",
    "var1": "462273",
    "hash": "df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2"
}

try:
    response = requests.post(url, headers=headers, data=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://test.payu.in/merchant/postservice?form=2";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");

            var formData = new List<KeyValuePair<string, string>>
            {
                new KeyValuePair<string, string>("key", "JP***g"),
                new KeyValuePair<string, string>("command", "check_isDomestic"),
                new KeyValuePair<string, string>("var1", "462273"),
                new KeyValuePair<string, string>("hash", "df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2")
            };

            var formContent = new FormUrlEncodedContent(formData);
            HttpResponseMessage response = await client.PostAsync(url, formContent);
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
```javascript
async function makeRequest() {
    const url = "https://test.payu.in/merchant/postservice?form=2";
    
    const headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    };

    const formData = new URLSearchParams({
        "key": "JP***g",
        "command": "check_isDomestic",
        "var1": "462273",
        "hash": "df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2"
    });

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: headers,
            body: formData
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
            String url = "https://test.payu.in/merchant/postservice?form=2";
            
            String formData = "key=JP***g&command=check_isDomestic&var1=462273&hash=df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2";
            
            HttpClient client = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(10))
                .build();

            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
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
```php
<?php
$url = "https://test.payu.in/merchant/postservice?form=2";

$headers = [
    "accept: application/json",
    "Content-Type: application/x-www-form-urlencoded"
];

$postData = [
    "key" => "JP***g",
    "command" => "check_isDomestic",
    "var1" => "462273",
    "hash" => "df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2"
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
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

  **Example Values:**

  * `var1` (first six digit of the card): 512345
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ## If the card is domestic

  ```json
  {
    "isDomestic": "Y",
    "issuingBank": "SCB",
    "cardType": "VISA",
    "cardCategory": "CC"
  }
  ```

  ## If the card is international

  ```json
  {
    "isDomestic": "N",
    "issuingBank": "UNKNOWN",
    "cardType": "Unknown",
    "cardCategory": "CC"
  }
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  | **Parameter** | **Description**                                                                                                                                                                 |
  | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | isDomestic    | Response value can contain any of the following: • **Y** signifies that the particular BIN is domestic. • **N** signifies that the particular BIN is International.             |
  | cardType      | Response value can contain any of the following: • MAST • VISA • MAES • AMEX • DINER • Unknown                                                                                  |
  | issuingBank   | The issuing bank of the card used for the transaction.                                                                                                                          |
  | cardCategory  | Response value can contain any of the following: • **CC** signifies that the particular bin is a credit card BIN • **DC** signifies that the particular bin is a debit card BIN |

  To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).
</Accordion>

## Request parameters

<Accordion title="Additional information for request parameters" icon="fa-book">
  ## Reference Information for Request Parameters

  | Parameter                 | Reference                                                                                                                                                                                                                                                                                    |           |        |                |
  | :------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------ | -------------- |
  | <Glossary>key</Glossary>  | For more information on how to generate the Key and Salt, refer to any of the following: • **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard) • **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt) |           |        |                |
  | <Glossary>hash</Glossary> | Hash logic for this API is: \`sha512(key\\                                                                                                                                                                                                                                                   | command\\ | var1\\ | salt) sha512\` |
  | var1                      | For JSON fields description, refer to [Additional Info for General APIs](ref:addl-info-general-apis)                                                                                                                                                                                         |           |        |                |

  ## Request Parameters Description

  | Parameter | Description                                              |
  | :-------- | :------------------------------------------------------- |
  | key       | Merchant key provided by PayU for authentication         |
  | command   | Set to "check\_isDomestic" for this API                  |
  | var1      | The first 6 digits of the Credit/Debit card (BIN number) |
  | hash      | Security hash calculated using sha512 algorithm          |

  ## Example Values

  Use the following sample values while trying out the API:

  * `var1` (first six digit of the card): 512345

  **Important Notes:**

  1. **BIN Number**: The var1 parameter should contain exactly the first 6 digits of the card number
  2. **Domestic vs International**:
     * Domestic cards (isDomestic: "Y") will show detailed issuing bank information
     * International cards (isDomestic: "N") typically show "UNKNOWN" for issuing bank
  3. **Card Types**: The API supports detection of major card types including VISA, MAST, AMEX, MAES, DINER
  4. **Card Categories**: Distinguishes between Credit Cards (CC) and Debit Cards (DC)
  5. **Hash Calculation**: Use the sha512 algorithm with the format: key|command|var1|salt
</Accordion>
