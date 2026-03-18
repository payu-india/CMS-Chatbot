---
title: Get Issuing Bank Status API
excerpt: Issuing Bank Status
api:
  file: getIssuingBankStatus.json
  operationId: IssuingBankStatus
hidden: false
metadata:
  title: ' Get Issuing Bank Status API'
  description: >-
    The **Get Issuing Bank Status** API (**getIssuingBankStatus**) helps handle
    credit or debit card issuing bank downtime by providing information on the
    status of the bank.
  keywords:
    - getIssuingBankStatus API Command
    - Issuing Bank of Credit Card Status API
    - Issuing Bank of Debit Card Status API
    - Check issuing bank health that issued credit card API
    - Check issuing bank health that issued debit card API
    - Health check of card issuing bank API
    - Health check of credit card issuing bank API
    - Health check of debit card issuing bank API
    - API Command getIssuingBankStatus
---
---
title: Get Issuing Bank Status API
excerpt: Issuing Bank Status
api:
  file: getIssuingBankStatus.json
  operationId: IssuingBankStatus
hidden: false
metadata:
  title: ' Get Issuing Bank Status API'
  description: >-
    The **Get Issuing Bank Status** API (**getIssuingBankStatus**) helps handle
    credit or debit card issuing bank downtime by providing information on the
    status of the bank.
  keywords:
    - getIssuingBankStatus API Command
    - Issuing Bank of Credit Card Status API
    - Issuing Bank of Debit Card Status API
    - Check issuing bank health that issued credit card API
    - Check issuing bank health that issued debit card API
    - Health check of card issuing bank API
    - Health check of credit card issuing bank API
    - Health check of debit card issuing bank API
    - API Command getIssuingBankStatus
---
The **Get Issuing Bank Status** API (**getIssuingBankStatus**) is used to help you handle the credit card or debit card issuing bank downtime.

| Environment            | URL                                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| Test Environment       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice?form=2](https://info.payu.in/merchant/postservice?form=2)         |

<Accordion title="Sample request" icon="fa-code">

<span id="sample-request" />

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
-H "accept: application/json" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "key=J****g&command=getIssuingBankStatus&var1=512345&hash=190908741314524c922d9587298eb64a076d058c085c66229f5acfeac4fb8a11dcd41f3f566cdb2e14a12f486a598a4e56943a2390c258384add9aeed1885e9d"
```
```python
import requests

url = "https://test.payu.in/merchant/postservice?form=2"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "key": "J****g",
    "command": "getIssuingBankStatus",
    "var1": "512345",
    "hash": "190908741314524c922d9587298eb64a076d058c085c66229f5acfeac4fb8a11dcd41f3f566cdb2e14a12f486a598a4e56943a2390c258384add9aeed1885e9d"
}

try:
    response = requests.post(url, headers=headers, data=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
```javascript
async function makeRequest() {
    const url = "https://test.payu.in/merchant/postservice?form=2";
    
    const headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    };

    const formData = new URLSearchParams({
        "key": "J****g",
        "command": "getIssuingBankStatus",
        "var1": "512345",
        "hash": "190908741314524c922d9587298eb64a076d058c085c66229f5acfeac4fb8a11dcd41f3f566cdb2e14a12f486a598a4e56943a2390c258384add9aeed1885e9d"
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
            
            String formData = "key=J****g&command=getIssuingBankStatus&var1=512345&hash=190908741314524c922d9587298eb64a076d058c085c66229f5acfeac4fb8a11dcd41f3f566cdb2e14a12f486a598a4e56943a2390c258384add9aeed1885e9d";
            
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
                new KeyValuePair<string, string>("key", "J****g"),
                new KeyValuePair<string, string>("command", "getIssuingBankStatus"),
                new KeyValuePair<string, string>("var1", "512345"),
                new KeyValuePair<string, string>("hash", "190908741314524c922d9587298eb64a076d058c085c66229f5acfeac4fb8a11dcd41f3f566cdb2e14a12f486a598a4e56943a2390c258384add9aeed1885e9d")
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
```php
<?php
$url = "https://test.payu.in/merchant/postservice?form=2";

$headers = [
    "accept: application/json",
    "Content-Type: application/x-www-form-urlencoded"
];

$postData = [
    "key" => "J****g",
    "command" => "getIssuingBankStatus",
    "var1" => "512345",
    "hash" => "190908741314524c922d9587298eb64a076d058c085c66229f5acfeac4fb8a11dcd41f3f566cdb2e14a12f486a598a4e56943a2390c258384add9aeed1885e9d"
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
</Accordion>

<Accordion title="Sample response" icon="fa-file-code">

<span id="sample-response" />

**Success scenario**

```json
{
      "issuing_bank": "HDFC",
      "up_status": "1"
}
```

* **up\_status** with value **0** — the issuing bank option is down at the moment.
* **up\_status** with value **1** — the issuing bank option is up at the moment.

**Failure scenario**

If issuing bank data is not available for the BIN:

```json
{
      "msg": "No information available",
      "status": 0
}
```

</Accordion>

<Accordion title="Response parameters" icon="fa-table">

<span id="response-parameters" />

For the BIN (first six digits) passed in **var1**, a successful response includes the fields below. If no data is available for that BIN, the API returns **msg** and **status** as in the failure sample.

<Table>
  <thead>
    <tr>
      <th>
        **Parameter/JSON field**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        issuing\_bank
      </td>

      <td>
        Name of the card issuing bank for the BIN.
      </td>

      <td>
        HDFC
      </td>
    </tr>

    <tr>
      <td>
        up\_status
      </td>

      <td>
        Issuing bank service status:

        * **0** — down at the moment
        * **1** — up at the moment
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        msg
      </td>

      <td>
        Returned on failure when no issuing bank information is available for the BIN.
      </td>

      <td>
        No information available
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        Returned on failure; **0** indicates the lookup did not succeed.
      </td>

      <td>
        0
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

## Request parameters

<span id="request-parameters" />

Use the following sample values while trying out the API:

<Accordion title="Reference information" icon="fa-table">

<span id="reference-information" />

<Table align={["left", "left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Parameter
      </th>

      <th style={{ textAlign: "left" }}>
        Reference
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        key
      </td>

      <td style={{ textAlign: "left" }}>
        For more information on how to generate the Key and Salt, refer to any of the following:

        * **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
        * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        hash
      </td>

      <td style={{ textAlign: "left" }}>
        Hash logic for this API is:

        `sha512(key|command|var1|salt) sha512`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        var1
      </td>

      <td style={{ textAlign: "left" }}>
        For JSON fields description, refer to [Additional Info for General APIs](ref:addl-info-general-apis)
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

**Example values**:

* **var1** (first 6 digits of the card): First six digits of any card (e.g. 512345).
