---
title: Check Payment API
api:
  file: check_transaction_api.json
  operationId: CheckPaymentAPI
hidden: false
metadata:
  title: Check Payment API
  description: >-
    The Check Payment API is similar to the Verify Payment API but uses PayUID
    or mihpayuID as input instead of TxnID, and it returns all transaction
    parameters.
  keywords:
    - check_payment API Command
    - Check Payment Status API
    - Payment Checking API
    - Check Payment Status using PayU ID
    - PayU ID payment status
---
The Check Payment (**check_payment**) API functions similar to the [Verify Payment API](ref:verify_payment_api). However, the input parameter in this API is the PayUID or mihpayuID generated at PayU's Server unlike **verify_payment** API where the input parameter is the TxnID (Transaction ID generated at merchant's server). It returns all the parameters for a given transaction.

<GENERALAPIsEnvironment />

<Accordion title="Sample request" icon="fa-code">
```curl
curl --location 'https://secure.payu.in/merchant/postservice'   --header 'Content-Type: application/x-www-form-urlencoded'   --header 'Cookie: PHPSESSID=6i6633s3gknq1kvph6dtijoabu; USERTXNINFO=68ed4df291d9b7.27710642'   --data-urlencode 'key=BmTY3G'   --data-urlencode 'command=get_TDR'   --data-urlencode 'var1="25779819010"'   --data-urlencode 'hash=9ba8c5c14b1d8643053b121ce7beb556b1e81fe7f4685048008bcc9f81a35f2b03f879704c10e0999e84923701219fc507c53a57c5ea8ff033ccd4148fb3366c'   --data-urlencode 'form=2'
```
```python
import requests

try:
    url = "https://secure.payu.in/merchant/postservice"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'PHPSESSID=6i6633s3gknq1kvph6dtijoabu; USERTXNINFO=68ed4df291d9b7.27710642'
    }
    data = {
        'key': 'BmTY3G',
        'command': 'get_TDR',
        'var1': '"25779819010"',
        'hash': '9ba8c5c14b1d8643053b121ce7beb556b1e81fe7f4685048008bcc9f81a35f2b03f879704c10e0999e84923701219fc507c53a57c5ea8ff033ccd4148fb3366c',
        'form': '2'
    }
    
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
    static async Task Main(string[] args)
    {
        try
        {
            using var client = new HttpClient();
            var url = "https://secure.payu.in/merchant/postservice";
            
            var postData = new List<KeyValuePair<string, string>>
            {
                new("key", "BmTY3G"),
                new("command", "get_TDR"),
                new("var1", "\"25779819010\""),
                new("hash", "9ba8c5c14b1d8643053b121ce7beb556b1e81fe7f4685048008bcc9f81a35f2b03f879704c10e0999e84923701219fc507c53a57c5ea8ff033ccd4148fb3366c"),
                new("form", "2")
            };
            
            var content = new FormUrlEncodedContent(postData);
            content.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue("application/x-www-form-urlencoded");
            
            client.DefaultRequestHeaders.Add("Cookie", "PHPSESSID=6i6633s3gknq1kvph6dtijoabu; USERTXNINFO=68ed4df291d9b7.27710642");
            
            var response = await client.PostAsync(url, content);
            var responseContent = await response.Content.ReadAsStringAsync();
            
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
async function makeRequest() {
    try {
        const url = 'https://secure.payu.in/merchant/postservice';
        
        const postData = new URLSearchParams({
            'key': 'BmTY3G',
            'command': 'get_TDR',
            'var1': '"25779819010"',
            'hash': '9ba8c5c14b1d8643053b121ce7beb556b1e81fe7f4685048008bcc9f81a35f2b03f879704c10e0999e84923701219fc507c53a57c5ea8ff033ccd4148fb3366c',
            'form': '2'
        });
        
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'PHPSESSID=6i6633s3gknq1kvph6dtijoabu; USERTXNINFO=68ed4df291d9b7.27710642'
            },
            body: postData
        });
        
        const responseText = await response.text();
        
        console.log(`Status Code: ${response.status}`);
        console.log(`Response: ${responseText}`);
        
    } catch (error) {
        console.error('Error:', error);
    }
}

makeRequest();
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class TDRRequest {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://secure.payu.in/merchant/postservice");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            connection.setRequestProperty("Cookie", "PHPSESSID=6i6633s3gknq1kvph6dtijoabu; USERTXNINFO=68ed4df291d9b7.27710642");
            connection.setDoOutput(true);
            
            String postData = "key=" + URLEncoder.encode("BmTY3G", StandardCharsets.UTF_8) +
                            "&command=" + URLEncoder.encode("get_TDR", StandardCharsets.UTF_8) +
                            "&var1=" + URLEncoder.encode("\"25779819010\"", StandardCharsets.UTF_8) +
                            "&hash=" + URLEncoder.encode("9ba8c5c14b1d8643053b121ce7beb556b1e81fe7f4685048008bcc9f81a35f2b03f879704c10e0999e84923701219fc507c53a57c5ea8ff033ccd4148fb3366c", StandardCharsets.UTF_8) +
                            "&form=" + URLEncoder.encode("2", StandardCharsets.UTF_8);
            
            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = postData.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }
            
            int statusCode = connection.getResponseCode();
            System.out.println("Status Code: " + statusCode);
            
            BufferedReader reader;
            if (statusCode >= 200 && statusCode < 300) {
                reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            } else {
                reader = new BufferedReader(new InputStreamReader(connection.getErrorStream()));
            }
            
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
            reader.close();
            
            System.out.println("Response: " + response.toString());
            
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
$url = 'https://secure.payu.in/merchant/postservice';

$postData = array(
    'key' => 'BmTY3G',
    'command' => 'get_TDR',
    'var1' => '"25779819010"',
    'hash' => '9ba8c5c14b1d8643053b121ce7beb556b1e81fe7f4685048008bcc9f81a35f2b03f879704c10e0999e84923701219fc507c53a57c5ea8ff033ccd4148fb3366c',
    'form' => '2'
);

$ch = curl_init();

curl_setopt_array($ch, array(
    CURLOPT_URL => $url,
    CURLOPT_POST => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POSTFIELDS => http_build_query($postData),
    CURLOPT_HTTPHEADER => array(
        'Content-Type: application/x-www-form-urlencoded',
        'Cookie: PHPSESSID=6i6633s3gknq1kvph6dtijoabu; USERTXNINFO=68ed4df291d9b7.27710642'
    )
));

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if (curl_error($ch)) {
    echo 'Error: ' . curl_error($ch) . "\n";
} else {
    echo "Status Code: " . $httpCode . "\n";
    echo "Response: " . $response . "\n";
}

curl_close($ch);
?>
```
</Accordion>

<Accordion title="Sample response" icon="fa-info-circle">
  * Success response
    ```
    {
      "status": 1,
      "msg": "Transaction Fetched Successfully",
      "transaction_details": {
          "mihpayid": "Not Found",
          "status": "Not Found"
      }
    }
    ```
</Accordion>

## Request parameters

<Accordion title="Reference information for request parameters" icon="fa-book">
  <KeyHashForGeneralParametersDescription />
</Accordion>

**Sample values**

Use the following sample values while trying out the API:

* `var1` (your transaction ID/order ID): 403993715521889530
