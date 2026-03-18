---
title: Save Card BIN Info API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Save Card BIN Info API
  description: >-
    The Save Card BIN API helps determine whether CVV needs to be collected for
    saved card transactions. It provides request headers, parameters, and sample
    code for encryption.
  keywords:
    - Card BIN Info API
    - Save Card BIN Info API
    - Save BIN Info API
    - Card BIN information API
    - Store BIN info API
    - Card BIN information API
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: collect-payments-using-a-saved-card
      title: Collect Payments using a Saved Card
    - type: endpoint
      slug: collect-payments-save-card
      title: Collect Payments - Save Card
---
---
title: Save Card BIN Info API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Save Card BIN Info API
  description: >-
    The Save Card BIN API helps determine whether CVV needs to be collected for
    saved card transactions. It provides request headers, parameters, and sample
    code for encryption.
  keywords:
    - Card BIN Info API
    - Save Card BIN Info API
    - Save BIN Info API
    - Card BIN information API
    - Store BIN info API
    - Card BIN information API
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: collect-payments-using-a-saved-card
      title: Collect Payments using a Saved Card
    - type: endpoint
      slug: collect-payments-save-card
      title: Collect Payments - Save Card
---
The **Save Card BIN** API helps you determine whether CVV needs to be collected from your customers and validated or not be collected for saved card transactions.

HTTP Method: **POST**

<GENERALAPIsEnvironment />

<Accordion title="Request headers" icon="fa-table">

<span id="request-headers" />

The request header contains the following fields:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Field**
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
        Date
        `mandatory`
      </td>

      <td>
        The date and time should be in the GMT time conversion(not the IST). For example, current time in India is 18:00:00 IST, the time in the date header should be 12:30:00 GMT.
      </td>

      <td>
        Thu, 17 Feb 2022 08:17:59 GMT
      </td>
    </tr>

    <tr>
      <td>
        Digest
        `mandatory`
      </td>

      <td>
        Base 64 encode of (sha256 hash of the JSON data (post to server).
      </td>

      <td>
        `vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=`
      </td>
    </tr>

    <tr>
      <td>
        Authorization
        `mandatory`
      </td>

      <td>
        This field is in the following format:
        `hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4="\`
        Where the above format includes the following:

        * **username**: The merchant key of the merchant.
        * **algorithm**: This must have the value as **hmac-sha256** that is used for this API
        * **headers**: This must have the value as **date digest**
        * **signature**: This must contain the hmacsha256 of (signing_string, merchant_secret), where:
          * **signing_string**: This is in the "**Date**"+"\n"+"**Digest**" format. Here, the Date and Digest is the same values in the fields listed in this table For example, "Thu, 17 Feb 2022 08:17:59 GMT""\n"+"vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0="
          * **merchant_secret**: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard)  | hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI=" |
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

The following sample Java code contains the logic used to encrypt as described in the above table:

```java
import com.google.gson.Gson;
import com.google.gson.JsonObject;
import org.apache.commons.codec.binary.Base64;
import org.joda.time.DateTime;
import org.joda.time.format.DateTimeFormat;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.security.InvalidKeyException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class HmacAuth {

    public static String getSha256(String input) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] digest = md.digest(input.getBytes());
            return Base64.encodeBase64String(digest);
        } catch (NoSuchAlgorithmException ignored) {}
        return null;
    }

    public static JsonObject getRequestBody(){
        JsonObject requestJson = new JsonObject();
        requestJson.addProperty("firstname","John");
        requestJson.addProperty("lastname","Doe");
        return requestJson;
    }

    public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeyException {
        String key = "smsplus";
        String secret = "admin";
        Gson gson = new Gson();
        String date = DateTimeFormat.forPattern("EEE, dd MMM yyyy HH:mm:ss 'GMT'").withZoneUTC().print(new DateTime());
        System.out.println(date);
        JsonObject requestJson = getRequestBody();
        String digest = getSha256(gson.toJson(requestJson));
        System.out.println(digest);
        String signingString = new StringBuilder()
            .append("date: " + date)
            .append("\ndigest: " + digest).toString();
        Mac sha256_HMAC = Mac.getInstance("HmacSHA256");
        SecretKeySpec secret_key = new SecretKeySpec(secret.getBytes(), "HmacSHA256");
        sha256_HMAC.init(secret_key);
        String signature = Base64.encodeBase64String(sha256_HMAC.doFinal(signingString.getBytes()));
        String authorization = new StringBuilder()
            .append("hmac username=\"")
            .append(key)
            .append("\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"")
            .append(signature)
            .append("\"").toString();
        System.out.println(authorization);
    }
}
```

</Accordion>

<Accordion title="Request parameters" icon="fa-list">

In addition to the [Request Headers](#request-headers) listed above, the **data** parameter is posted with the following fields are posted in an array:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        bin
      </td>

      <td>
        `String` The Network Token BIN or the first 9-digits of the network token is posted in this parameter.
      </td>
    </tr>

    <tr>
      <td>
        checkCVVRequired
      </td>

      <td>
        `Boolean` This parameter may contain any of the following:

        * **True**: Request the API to check if card CVV must be checked for the saved card transaction so that merchant need to validate the CVV accordingly.
        * **False**: Request the API not to check if card CVV need to be checked for the saved card transaction
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

<Accordion title="Sample request" icon="fa-code">

```curl
curl --location 'https://info.payu.in/issuing-bank/v1/bin' \
--header 'Content-Type: application/json' \
--header 'Date: Thu, 01 Jun 2023 06:59:03 GMT' \
--header 'Digest: sYxiEFksDG+h+sB11nonf9ry31aKynEJ/Hmxwc6M3pM=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="F8D2PW2/Q2VF7FZKiY3RKJ6+1HU5OH8/HkxvitghvP4="' \
--header 'Cookie: PHPSESSID=lf33il1bio9scn7cars1hqsf05; PHPSESSID=o7bbf6gbociqmroctldtslkc21' \
--header 'mid: 2' \
--data '{
    "bin": "512345789",
    "checkCVVRequired": true
}'
```
```python
import requests
import json

url = "https://info.payu.in/issuing-bank/v1/bin"

headers = {
    "Content-Type": "application/json",
    "Date": "Thu, 01 Jun 2023 06:59:03 GMT",
    "Digest": "sYxiEFksDG+h+sB11nonf9ry31aKynEJ/Hmxwc6M3pM=",
    "Authorization": 'hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="F8D2PW2/Q2VF7FZKiY3RKJ6+1HU5OH8/HkxvitghvP4="',
    "Cookie": "PHPSESSID=lf33il1bio9scn7cars1hqsf05; PHPSESSID=o7bbf6gbociqmroctldtslkc21",
    "mid": "2"
}

data = {
    "bin": "512345789",
    "checkCVVRequired": True
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
    const url = "https://info.payu.in/issuing-bank/v1/bin";
    
    const headers = {
        "Content-Type": "application/json",
        "Date": "Thu, 01 Jun 2023 06:59:03 GMT",
        "Digest": "sYxiEFksDG+h+sB11nonf9ry31aKynEJ/Hmxwc6M3pM=",
        "Authorization": 'hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="F8D2PW2/Q2VF7FZKiY3RKJ6+1HU5OH8/HkxvitghvP4="',
        "Cookie": "PHPSESSID=lf33il1bio9scn7cars1hqsf05; PHPSESSID=o7bbf6gbociqmroctldtslkc21",
        "mid": "2"
    };

    const requestData = {
        "bin": "512345789",
        "checkCVVRequired": true
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
            String url = "https://info.payu.in/issuing-bank/v1/bin";
            
            String jsonData = "{\"bin\":\"512345789\",\"checkCVVRequired\":true}";
            
            HttpClient client = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(10))
                .build();

            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Content-Type", "application/json")
                .header("Date", "Thu, 01 Jun 2023 06:59:03 GMT")
                .header("Digest", "sYxiEFksDG+h+sB11nonf9ry31aKynEJ/Hmxwc6M3pM=")
                .header("Authorization", "hmac username=\"smsplus\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"F8D2PW2/Q2VF7FZKiY3RKJ6+1HU5OH8/HkxvitghvP4=\"")
                .header("Cookie", "PHPSESSID=lf33il1bio9scn7cars1hqsf05; PHPSESSID=o7bbf6gbociqmroctldtslkc21")
                .header("mid", "2")
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
            string url = "https://info.payu.in/issuing-bank/v1/bin";
            
            client.DefaultRequestHeaders.Add("Date", "Thu, 01 Jun 2023 06:59:03 GMT");
            client.DefaultRequestHeaders.Add("Digest", "sYxiEFksDG+h+sB11nonf9ry31aKynEJ/Hmxwc6M3pM=");
            client.DefaultRequestHeaders.Add("Authorization", "hmac username=\"smsplus\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"F8D2PW2/Q2VF7FZKiY3RKJ6+1HU5OH8/HkxvitghvP4=\"");
            client.DefaultRequestHeaders.Add("Cookie", "PHPSESSID=lf33il1bio9scn7cars1hqsf05; PHPSESSID=o7bbf6gbociqmroctldtslkc21");
            client.DefaultRequestHeaders.Add("mid", "2");

            var requestData = new
            {
                bin = "512345789",
                checkCVVRequired = true
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
$url = "https://info.payu.in/issuing-bank/v1/bin";

$headers = [
    "Content-Type: application/json",
    "Date: Thu, 01 Jun 2023 06:59:03 GMT",
    "Digest: sYxiEFksDG+h+sB11nonf9ry31aKynEJ/Hmxwc6M3pM=",
    "Authorization: hmac username=\"smsplus\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"F8D2PW2/Q2VF7FZKiY3RKJ6+1HU5OH8/HkxvitghvP4=\"",
    "Cookie: PHPSESSID=lf33il1bio9scn7cars1hqsf05; PHPSESSID=o7bbf6gbociqmroctldtslkc21",
    "mid: 2"
];

$requestData = [
    "bin" => "512345789",
    "checkCVVRequired" => true
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
</Accordion>

<Accordion title="Response parameters" icon="fa-table">

The response involves the following parameters and the **result** parameter contains the offer results:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
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
        code
      </td>

      <td>
        This parameter returns the status of web service call. The status can be any of the following:

        * **0**: If web service call failed.
        * **1** : If web service call succeeded.
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        result
      </td>

      <td>
        `JSON Object` This parameter gives the information about the result of the API response in a JSON format. For more information, refer to the [result Field JSON Details](#result-parameter-json-details) subsection.
      </td>

      <td>
        Refer to the [result Field JSON Details](#result-parameter-json-details) subsection.
      </td>
    </tr>
  </tbody>
</Table>

<span id="result-parameter-json-details" />

### result parameter JSON details

The **result** parameter contains the result in a JSON format and the fields in the JSON are described in the following table:

</Accordion>

<Accordion title="Sample response" icon="fa-file-code">

<span id="sample-response" />

### Success scenario

```json
{    
 "message": "Success",    
 "status": 1,    
 "result": 
 {        
   "status": 0,      
   "category": "debitcard",        
   "bin": "401151",        
   "cvvLessSupported": false,        
   "is_domestic": true,        
   "card_type": "VISA",        
   "issuing_bank": "HDFC",        
   "otp_on_fly": true,        
   "is_atmpin_card": 1    
  }
}
```

</Accordion>