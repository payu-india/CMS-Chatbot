---
excerpt: ''
api:
  file: payment-link-4.json
  operationId: SharePaymentLinkAPI
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to share a payment link with a list of email IDs and/or phone numbers.

**Environment**

|                        |                                                         |
| :--------------------- | :------------------------------------------------------ |
| Test Environment       | `<redacted URL>`    |
| Production Environment | `<redacted URL>`       |

<Callout icon="📘" theme="info">
  **Note**: The access token with the scope as **read_payment_links** is required on the header. For more information on getting the access token, refer to [Get Access Token](ref:get-token-api-for-payment-links).
</Callout>

<Callout icon="🚧" theme="warn">
  **Important**: The `channelList` must be passed as a **query parameter** in the request URL, not in the request body. Separate multiple email IDs and phone numbers with a comma (`,`) and URL-encode the value (for example, `@` becomes `%40` and `,` becomes `%2C`). This request does not require a request body.
</Callout>
## Sample Requests
<Accordion title="Basic Sample request" icon="fa-code">
   ```curl
   curl --location --request POST '<redacted URL>' \
     --header 'merchantId: 8235900' \
     --header 'Authorization: Bearer <access_token>'
   ```
   ```python
   import requests

   url = "<redacted URL>"
   headers = {
       "merchantId": "8235900",
       "Authorization": "Bearer <access_token>"
   }
   # requests URL-encodes the query parameter value automatically
   params = {
       "channelList": "abc.example@payu.in,9876543210"
   }
   response = requests.post(url, headers=headers, params=params)
   print(response.json())
   ```
   ```php
   <?php
   $baseUrl = "<redacted URL>";
   // http_build_query URL-encodes the query parameter value
   $query = http_build_query([
       "channelList" => "abc.example@payu.in,9876543210"
   ]);
   $url = $baseUrl . "?" . $query;
   $headers = [
       "merchantId: 8235900",
       "Authorization: Bearer <access_token>"
   ];
   $ch = curl_init($url);
   curl_setopt($ch, CURLOPT_POST, true);
   curl_setopt($ch, CURLOPT_POSTFIELDS, "");
   curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
   curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
   $response = curl_exec($ch);
   curl_close($ch);
   echo $response;
   ?>
   ```
   ```javascript
   const fetch = require('node-fetch');

   const baseUrl = '<redacted URL>';
   // URLSearchParams URL-encodes the query parameter value
   const query = new URLSearchParams({
       channelList: 'abc.example@payu.in,9876543210'
   });
   const url = `${baseUrl}?${query.toString()}`;
   const headers = {
       'merchantId': '8235900',
       'Authorization': 'Bearer <access_token>'
   };

   fetch(url, {
       method: 'POST',
       headers: headers
   })
   .then(response => response.json())
   .then(data => console.log(data))
   .catch(error => console.error('Error:', error));
   ```
   ```java
   import java.net.HttpURLConnection;
   import java.net.URL;
   import java.net.URLEncoder;
   import java.nio.charset.StandardCharsets;
   import java.io.BufferedReader;
   import java.io.InputStreamReader;

   public class SharePaymentLink {
       public static void main(String[] args) throws Exception {
           String baseUrl = "<redacted URL>";
           String channelList = URLEncoder.encode("abc.example@payu.in,9876543210", StandardCharsets.UTF_8.toString());
           URL url = new URL(baseUrl + "?channelList=" + channelList);

           HttpURLConnection conn = (HttpURLConnection) url.openConnection();
           conn.setRequestMethod("POST");
           conn.setRequestProperty("merchantId", "8235900");
           conn.setRequestProperty("Authorization", "Bearer <access_token>");
           conn.setDoOutput(true);
           conn.setFixedLengthStreamingMode(0); // No request body

           try (BufferedReader br = new BufferedReader(
                   new InputStreamReader(conn.getInputStream(), "utf-8"))) {
               StringBuilder response = new StringBuilder();
               String responseLine;
               while ((responseLine = br.readLine()) != null) {
                   response.append(responseLine.trim());
               }
               System.out.println(response.toString());
           }
       }
   }
   ```
</Accordion>
<Accordion title="Sample Request to share using a plaform" icon="fa-code">
```curl
curl --location --request POST 'https://oneapi.payu.in/payment-links/INV797179197263280201/share?channelList=abc.example%40payu.… \
--header 'accept: application/json' \
--header 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' \
--header 'authorization: Bearer 14cc7e78d0a9748607c2bb833d91a5ad7a03c4ccc6f3ab88a7f85b74b47bb9d1' \
--header 'content-length: 0' \
--header 'mid: 8235900' \
--header 'origin: PayU - Best Digital Payment Solutions for Businesses | 150+ Payment Methods ' \
--header 'priority: u=1, i' \
--header 'product: PAYUBIZ' \
--header 'referer: https://payu.in/' \
--header 'sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"' \
--header 'sec-ch-ua-mobile: ?0' \
--header 'sec-ch-ua-platform: "macOS"' \
--header 'sec-fetch-dest: empty' \
--header 'sec-fetch-mode: cors' \
--header 'sec-fetch-site: same-site' \
--header 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
--header 'Cookie: USERTXNINFO=69f1ec146b4ec8.61066366'
```
```python
import requests

url = "https://oneapi.payu.in/payment-links/INV797179197263280201/share?channelList=abc.example%40payu.…"

headers = {
    "accept": "application/json",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "authorization": "Bearer 14cc7e78d0a9748607c2bb833d91a5ad7a03c4ccc6f3ab88a7f85b74b47bb9d1",
    "content-length": "0",
    "mid": "8235900",
    "origin": "PayU - Best Digital Payment Solutions for Businesses | 150+ Payment Methods",
    "priority": "u=1, i",
    "product": "PAYUBIZ",
    "referer": "https://payu.in/",
    "sec-ch-ua": '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    "Cookie": "USERTXNINFO=69f1ec146b4ec8.61066366"
}

response = requests.post(url, headers=headers, allow_redirects=True)

print(response.status_code)
print(response.text)
```
```csharp
using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var handler = new HttpClientHandler { AllowAutoRedirect = true };
        using var client = new HttpClient(handler);

        var request = new HttpRequestMessage(
            HttpMethod.Post,
            "https://oneapi.payu.in/payment-links/INV797179197263280201/share?channelList=abc.example%40payu.…"
        );

        request.Headers.TryAddWithoutValidation("accept", "application/json");
        request.Headers.TryAddWithoutValidation("accept-language", "en-GB,en-US;q=0.9,en;q=0.8");
        request.Headers.TryAddWithoutValidation("authorization", "Bearer 14cc7e78d0a9748607c2bb833d91a5ad7a03c4ccc6f3ab88a7f85b74b47bb9d1");
        request.Headers.TryAddWithoutValidation("mid", "8235900");
        request.Headers.TryAddWithoutValidation("origin", "PayU - Best Digital Payment Solutions for Businesses | 150+ Payment Methods");
        request.Headers.TryAddWithoutValidation("priority", "u=1, i");
        request.Headers.TryAddWithoutValidation("product", "PAYUBIZ");
        request.Headers.TryAddWithoutValidation("referer", "https://payu.in/");
        request.Headers.TryAddWithoutValidation("sec-ch-ua", "\"Not:A-Brand\";v=\"99\", \"Google Chrome\";v=\"145\", \"Chromium\";v=\"145\"");
        request.Headers.TryAddWithoutValidation("sec-ch-ua-mobile", "?0");
        request.Headers.TryAddWithoutValidation("sec-ch-ua-platform", "\"macOS\"");
        request.Headers.TryAddWithoutValidation("sec-fetch-dest", "empty");
        request.Headers.TryAddWithoutValidation("sec-fetch-mode", "cors");
        request.Headers.TryAddWithoutValidation("sec-fetch-site", "same-site");
        request.Headers.TryAddWithoutValidation("user-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36");
        request.Headers.TryAddWithoutValidation("Cookie", "USERTXNINFO=69f1ec146b4ec8.61066366");

        request.Content = new ByteArrayContent(Array.Empty<byte>());
        request.Content.Headers.ContentLength = 0;

        var response = await client.SendAsync(request);

        Console.WriteLine((int)response.StatusCode);
        Console.WriteLine(await response.Content.ReadAsStringAsync());
    }
}
```
```javascript
async function sharePaymentLink() {
    const url = "https://oneapi.payu.in/payment-links/INV797179197263280201/share?channelList=abc.example%40payu.…";

    const headers = {
        "accept": "application/json",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "authorization": "Bearer 14cc7e78d0a9748607c2bb833d91a5ad7a03c4ccc6f3ab88a7f85b74b47bb9d1",
        "content-length": "0",
        "mid": "8235900",
        "origin": "PayU - Best Digital Payment Solutions for Businesses | 150+ Payment Methods",
        "priority": "u=1, i",
        "product": "PAYUBIZ",
        "referer": "https://payu.in/",
        "sec-ch-ua": '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
        "cookie": "USERTXNINFO=69f1ec146b4ec8.61066366"
    };

    const response = await fetch(url, {
        method: "POST",
        headers: headers,
        redirect: "follow"
    });

    console.log(response.status);
    const text = await response.text();
    console.log(text);
}

sharePaymentLink();
```
```java
import okhttp3.*;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        OkHttpClient client = new OkHttpClient.Builder()
                .followRedirects(true)
                .build();

        RequestBody body = RequestBody.create(new byte[0], null);

        Request request = new Request.Builder()
                .url("https://oneapi.payu.in/payment-links/INV797179197263280201/share?channelList=abc.example%40payu.…")
                .post(body)
                .addHeader("accept", "application/json")
                .addHeader("accept-language", "en-GB,en-US;q=0.9,en;q=0.8")
                .addHeader("authorization", "Bearer 14cc7e78d0a9748607c2bb833d91a5ad7a03c4ccc6f3ab88a7f85b74b47bb9d1")
                .addHeader("mid", "8235900")
                .addHeader("origin", "PayU - Best Digital Payment Solutions for Businesses | 150+ Payment Methods")
                .addHeader("priority", "u=1, i")
                .addHeader("product", "PAYUBIZ")
                .addHeader("referer", "https://payu.in/")
                .addHeader("sec-ch-ua", "\"Not:A-Brand\";v=\"99\", \"Google Chrome\";v=\"145\", \"Chromium\";v=\"145\"")
                .addHeader("sec-ch-ua-mobile", "?0")
                .addHeader("sec-ch-ua-platform", "\"macOS\"")
                .addHeader("sec-fetch-dest", "empty")
                .addHeader("sec-fetch-mode", "cors")
                .addHeader("sec-fetch-site", "same-site")
                .addHeader("user-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36")
                .addHeader("Cookie", "USERTXNINFO=69f1ec146b4ec8.61066366")
                .build();

        try (Response response = client.newCall(request).execute()) {
            System.out.println(response.code());
            if (response.body() != null) {
                System.out.println(response.body().string());
            }
        }
    }
}
```
```php
<?php

$url = "https://oneapi.payu.in/payment-links/INV797179197263280201/share?channelList=abc.example%40payu.…";

$headers = [
    "accept: application/json",
    "accept-language: en-GB,en-US;q=0.9,en;q=0.8",
    "authorization: Bearer 14cc7e78d0a9748607c2bb833d91a5ad7a03c4ccc6f3ab88a7f85b74b47bb9d1",
    "content-length: 0",
    "mid: 8235900",
    "origin: PayU - Best Digital Payment Solutions for Businesses | 150+ Payment Methods",
    "priority: u=1, i",
    "product: PAYUBIZ",
    "referer: https://payu.in/",
    'sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    "sec-ch-ua-mobile: ?0",
    'sec-ch-ua-platform: "macOS"',
    "sec-fetch-dest: empty",
    "sec-fetch-mode: cors",
    "sec-fetch-site: same-site",
    "user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    "Cookie: USERTXNINFO=69f1ec146b4ec8.61066366"
];

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, "");
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if (curl_errno($ch)) {
    echo "cURL Error: " . curl_error($ch) . "\n";
}

curl_close($ch);

echo $httpCode . "\n";
echo $response . "\n";
```
</Accordion>
<Accordion title="Sample response" icon="fa-reply">
  ```json
    {
      "status": 0,
      "message": "string",
      "result": {},
      "errorCode": 170,
      "guid": "f529e375-739f-4c8a-b5f5-0e67fa3f533f"
    }
  ```
</Accordion>

<Accordion title="Request headers" icon="fa-flask">
  <HTMLBlock>{`
            <table style="width: 100%; border-collapse: collapse;">
            <thead>
            <tr>
              <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
              <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td style="border: 1px solid #ddd; padding: 8px;"><p>merchantId<br><strong>mandatory</strong></p>
            </td>
              <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This contains the merchant identifier (MID). For example, 8235900.</p>
            </td>
            </tr>
            <tr>
              <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization<br><strong>mandatory</strong></p>
            </td>
              <td style="border: 1px solid #ddd; padding: 8px;"><p>Bearer <code>String</code> This contains the access token in the <code>Bearer &lt;access_token&gt;</code> format. For getting a token, refer to <a href="http://docs.payu.in/reference/get_token_api">Get Token API</a>.</p>
            </td>
            </tr>
            </tbody>
            </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Path parameters" icon="fa-flask">
  <HTMLBlock>{`
            <table style="width: 100%; border-collapse: collapse;">
            <thead>
            <tr>
              <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameters</strong></th>
              <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
              <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td style="border: 1px solid #ddd; padding: 8px;"><p>id<br><strong>mandatory</strong></p>
            </td>
              <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the payment link invoice number.</p>
            </td>
              <td style="border: 1px solid #ddd; padding: 8px;"><p>INV7444229847726</p>
            </td>
            </tr>
            </tbody>
            </table>
  `}</HTMLBlock>
</Accordion>

## Query parameters

<Accordion title="Reference info for query parameters" icon="fa-flask">
  | Parameter                        | Description                                                                                                                                                                                                                                  | Example                                        |
  | :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------- |
  | channelList<br>**mandatory**     | `String` This parameter must contain the email IDs and/or phone numbers to which the payment link needs to be shared. Pass it as a query parameter in the URL, separate multiple values with a comma (`,`), and URL-encode the value. | `abc.example%40payu.in%2C9876543210`           |
</Accordion>