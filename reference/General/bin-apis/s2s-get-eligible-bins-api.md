---
title: S2S Get Eligible BINs API
excerpt: 'API Command: s2sEligibleBins'
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
---
title: S2S Get Eligible BINs API
excerpt: 'API Command: s2sEligibleBins'
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The S2S Eligible BINs API (**s2sEligibleBins**) API is similar to the **Get BIN Info** API, but used in S2S environment. For more information on Get BIN Info API, refer to [Get Bin Info API](ref:get_bin_info_api).

###Environment

| Environment            | URL                                                                                                  |
| :--------------------- | :--------------------------------------------------------------------------------------------------- |
| Production Environment | [https://info.payu.in/merchant/postservice?form=2](https://info.payu.in/merchant/postservice?form=2) |



<Accordion title="Request parameters" icon="fa-table">

<span id="request-parameters" />

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Reference
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
        `mandatory`
      </td>

      <td>
        For more information on how to generate the Key and Salt, refer to any of the following:  - **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard) - **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>
    </tr>

    <tr>
      <td>
        var1
        `mandatory`
      </td>

      <td>
        Specify the value as "**2**" for S2S flow.
      </td>
    </tr>

    <tr>
      <td>
        var2
        `mandatory`
      </td>

      <td>
        Specify any of the following values in this field based on the output you required: -
        0 - Specify this value to fetch all the active and inactive bins.
        1 - Specify this value to fetch the active bins only.
      </td>
    </tr>

    <tr>
      <td>
        var3
        `mandatory`
      </td>

      <td>
        Specify the bank Name to be passed to get Bins of specific Bank.
      </td>
    </tr>

    <tr>
      <td>
        var4
        `mandatory`
      </td>

      <td>
        Specify the categories of the card need to be passed. For example, **creditcard**.
      </td>
    </tr>

    <tr>
      <td>
        var5
        `mandatory`
      </td>

      <td>
        Specify the card schemes should be passed in this field. For example; **VISA**, **MAST**.
      </td>
    </tr>

    <tr>
      <td>
        hash
        `mandatory`
      </td>

      <td>
        The hash logic that must be used by merchants to calculate the hash:
        Hash logic for this API is:
        <code>sha512(key|command|var1|salt) sha512</code>
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

<Accordion title="Sample request" icon="fa-code">

<span id="sample-request" />
```curl
curl --location 'https://info.payu.in/merchant/postservice.php?form=2' \
--form 'key=smsplus' \
--form 'command=s2sEligibleBins' \
--form 'var1=2' \
--form 'var2=1' \
--form 'var3=KOTAK' \
--form 'var4=debitcard' \
--form 'var5=RUPAY' \
--form 'hash=aksduhfksdjhjkdskkfdsjkdfkjshfkjhadsjkfsdfsdf'
```
```python
import requests

url = "https://info.payu.in/merchant/postservice.php?form=2"

files = {
    'key': (None, 'smsplus'),
    'command': (None, 's2sEligibleBins'),
    'var1': (None, '2'),
    'var2': (None, '1'),
    'var3': (None, 'KOTAK'),
    'var4': (None, 'debitcard'),
    'var5': (None, 'RUPAY'),
    'hash': (None, 'aksduhfksdjhjkdskkfdsjkdfkjshfkjhadsjkfsdfsdf')
}

try:
    response = requests.post(url, files=files)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
```javascript
async function makeRequest() {
    const url = "https://info.payu.in/merchant/postservice.php?form=2";
    
    const formData = new FormData();
    formData.append('key', 'smsplus');
    formData.append('command', 's2sEligibleBins');
    formData.append('var1', '2');
    formData.append('var2', '1');
    formData.append('var3', 'KOTAK');
    formData.append('var4', 'debitcard');
    formData.append('var5', 'RUPAY');
    formData.append('hash', 'aksduhfksdjhjkdskkfdsjkdfkjshfkjhadsjkfsdfsdf');

    try {
        const response = await fetch(url, {
            method: "POST",
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
import java.util.HashMap;
import java.util.Map;

public class ApiRequest {
    public static void main(String[] args) {
        try {
            String url = "https://info.payu.in/merchant/postservice.php?form=2";
            String boundary = "----boundary" + System.currentTimeMillis();
            
            Map<String, String> formData = new HashMap<>();
            formData.put("key", "smsplus");
            formData.put("command", "s2sEligibleBins");
            formData.put("var1", "2");
            formData.put("var2", "1");
            formData.put("var3", "KOTAK");
            formData.put("var4", "debitcard");
            formData.put("var5", "RUPAY");
            formData.put("hash", "aksduhfksdjhjkdskkfdsjkdfkjshfkjhadsjkfsdfsdf");
            
            StringBuilder body = new StringBuilder();
            for (Map.Entry<String, String> entry : formData.entrySet()) {
                body.append("--").append(boundary).append("\r\n");
                body.append("Content-Disposition: form-data; name=\"").append(entry.getKey()).append("\"\r\n\r\n");
                body.append(entry.getValue()).append("\r\n");
            }
            body.append("--").append(boundary).append("--\r\n");
            
            HttpClient client = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(10))
                .build();

            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Content-Type", "multipart/form-data; boundary=" + boundary)
                .POST(HttpRequest.BodyPublishers.ofString(body.toString()))
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
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://info.payu.in/merchant/postservice.php?form=2";
            
            var formContent = new MultipartFormDataContent();
            formContent.Add(new StringContent("smsplus"), "key");
            formContent.Add(new StringContent("s2sEligibleBins"), "command");
            formContent.Add(new StringContent("2"), "var1");
            formContent.Add(new StringContent("1"), "var2");
            formContent.Add(new StringContent("KOTAK"), "var3");
            formContent.Add(new StringContent("debitcard"), "var4");
            formContent.Add(new StringContent("RUPAY"), "var5");
            formContent.Add(new StringContent("aksduhfksdjhjkdskkfdsjkdfkjshfkjhadsjkfsdfsdf"), "hash");

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
$url = "https://info.payu.in/merchant/postservice.php?form=2";

$postData = [
    "key" => "smsplus",
    "command" => "s2sEligibleBins",
    "var1" => "2",
    "var2" => "1",
    "var3" => "KOTAK",
    "var4" => "debitcard",
    "var5" => "RUPAY",
    "hash" => "aksduhfksdjhjkdskkfdsjkdfkjshfkjhadsjkfsdfsdf"
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $postData);
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
{
   "data":[
      {
         "issuingBank":"HDFC",
         "schemes":[
            {
               "scheme":"MAST",
               "categories":[
                  {
                     "bins":[
                        "515470517",
                        "51166608",
                        "515470541"
                     ],
                     "category":"creditcard"
                  },
                  {
                     "bins":[
                        "535375995",
                        "535376757",
                        "54191904"
                     ],
                     "category":"debitcard"
                  }
               ]
            },
            {
               "scheme":"VISA",
               "categories":[
                  {
                     "bins":[
                        "478971945",
                        "432001408",
                        "434415570"
                     ],
                     "category":"debitcard"
                  }
               ]
            },
            {
               "scheme":"RUPAY",
               "categories":[
                  {
                     "bins":[
                        "652166040",
                        "607311",
                        "65254243"
                     ],
                     "category":"debitcard"
                  }
               ]
            }
         ]
      }
   ],
   "statusCode":200
}
```

</Accordion>