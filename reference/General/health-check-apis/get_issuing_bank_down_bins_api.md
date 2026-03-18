---
title: Get Issuing Bank Down BINs API
api:
  file: updated_gettingissuingbankdownbins.json
  operationId: GetIssuingBankDownBINs
hidden: false
metadata:
  description: >-
    The Getting Issuing Bank Down Bins API retrieves card BINs for banks
    experiencing downtime, with the ability to specify a specific bank or
    retrieve all banks in JSON format.
  keywords:
    - gettingIssuingBankDownBins API Command
    - Issuing Bank Down BINs API
    - Check issuing bank status API
    - Issuing bank downtime API
    - Bank outage verification API
    - API Command gettingIssuingBankDownBins
---
---
title: Get Issuing Bank Down BINs API
api:
  file: updated_gettingissuingbankdownbins.json
  operationId: GetIssuingBankDownBINs
hidden: false
metadata:
  description: >-
    The Getting Issuing Bank Down Bins API retrieves card BINs for banks
    experiencing downtime, with the ability to specify a specific bank or
    retrieve all banks in JSON format.
  keywords:
    - gettingIssuingBankDownBins API Command
    - Issuing Bank Down BINs API
    - Check issuing bank status API
    - Issuing bank downtime API
    - Bank outage verification API
    - API Command gettingIssuingBankDownBins
---
The **Getting Issuing Bank Down Bins** API (**gettingIssuingBankDownBins**) is used to retrieve the card BINs for all the banks that are observing either full downtime or partial downtime at an instance.



<Accordion title="Sample request" icon="fa-code">

<span id="sample-request" />

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
-H "accept: application/json" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "key=JP***g&command=getIssuingBankDownBins&var1=ALLBD&var2=1&hash=efc4452469091d4d6061fcf6bce45c8116675972a89ddcba6bdd27dce613ca6e48e703e3ba7f6015ef128eda60ed61a3307795c5dd7e284a7691f0c6dc3812a8"
```
Here are the equivalent code snippets for your CURL request in different programming languages:

```python
import requests

url = "https://test.payu.in/merchant/postservice?form=2"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "key": "JP***g",
    "command": "getIssuingBankDownBins",
    "var1": "ALLBD",
    "var2": "1",
    "hash": "efc4452469091d4d6061fcf6bce45c8116675972a89ddcba6bdd27dce613ca6e48e703e3ba7f6015ef128eda60ed61a3307795c5dd7e284a7691f0c6dc3812a8"
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
        "key": "JP***g",
        "command": "getIssuingBankDownBins",
        "var1": "ALLBD",
        "var2": "1",
        "hash": "efc4452469091d4d6061fcf6bce45c8116675972a89ddcba6bdd27dce613ca6e48e703e3ba7f6015ef128eda60ed61a3307795c5dd7e284a7691f0c6dc3812a8"
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
            
            String formData = "key=JP***g&command=getIssuingBankDownBins&var1=ALLBD&var2=1&hash=efc4452469091d4d6061fcf6bce45c8116675972a89ddcba6bdd27dce613ca6e48e703e3ba7f6015ef128eda60ed61a3307795c5dd7e284a7691f0c6dc3812a8";
            
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
                new KeyValuePair<string, string>("key", "JP***g"),
                new KeyValuePair<string, string>("command", "getIssuingBankDownBins"),
                new KeyValuePair<string, string>("var1", "ALLBD"),
                new KeyValuePair<string, string>("var2", "1"),
                new KeyValuePair<string, string>("hash", "efc4452469091d4d6061fcf6bce45c8116675972a89ddcba6bdd27dce613ca6e48e703e3ba7f6015ef128eda60ed61a3307795c5dd7e284a7691f0c6dc3812a8")
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
    "key" => "JP***g",
    "command" => "getIssuingBankDownBins",
    "var1" => "ALLBD",
    "var2" => "1",
    "hash" => "efc4452469091d4d6061fcf6bce45c8116675972a89ddcba6bdd27dce613ca6e48e703e3ba7f6015ef128eda60ed61a3307795c5dd7e284a7691f0c6dc3812a8"
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

```json
[
      {
            "issuing_bank": "ALLBD",
            "status": 2,
            "title": "ALLAHABAD BANK",
            "bins_arr": [
                  "421337",
                  "608219",
                  "608218",
                  "608171",
                  "608102",
                  "607352",
                  "607137",
                  "607038",
                  "607091",
                  "607016",
                  "607117",
                  "430450",
                  "652204"
            ]
      }
]
```

</Accordion>

<Accordion title="Response parameters" icon="fa-table">

<span id="response-parameters" />

The API returns a **JSON array**. Each object describes one issuing bank and the BINs that are down (full or partial downtime per your **var2** filter). If **var1** is **default**, you get entries for all applicable banks; if **var1** is a specific bank code, the response is scoped to that bank.

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
        Issuing bank code for this entry.
      </td>

      <td>
        ALLBD
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        Status code for this bank’s downtime entry (as returned by PayU).
      </td>

      <td>
        2
      </td>
    </tr>

    <tr>
      <td>
        title
      </td>

      <td>
        Display name of the issuing bank.
      </td>

      <td>
        ALLAHABAD BANK
      </td>
    </tr>

    <tr>
      <td>
        bins\_arr
      </td>

      <td>
        List of card BINs under this bank that are in downtime (full or partial, per **var2**).
      </td>

      <td>
        ["421337", "608219", …]
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

## Request parameters

<span id="request-parameters" />

Use the following sample values while trying out the API:

<Accordion title="Reference information for request parameters" icon="fa-table">

<span id="reference-information-for-request-parameters" />

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
        command
      </td>

      <td style={{ textAlign: "left" }}>
        Must be **getIssuingBankDownBins**.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        var1
      </td>

      <td style={{ textAlign: "left" }}>
        Bank name code (as provided by PayU) or **default** for all banks.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        var2
      </td>

      <td style={{ textAlign: "left" }}>
        **0** — BINs that are fully down; **1** — BINs that are partially down.
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
  </tbody>
</Table>

</Accordion>

**Example values**:

* **var1**: Pass **default** for downtime across all banks, or a specific bank code (e.g. **ALLBD**) for one bank.
* **var2**: **0** for fully down BINs, **1** for partially down BINs (see sample request).
