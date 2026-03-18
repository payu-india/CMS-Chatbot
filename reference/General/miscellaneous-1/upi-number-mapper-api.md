---
title: UPI Number Mapper API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: UPI Number Mapper API
  description: >-
    This document explains how to use the UPI Number API command to fetch the
    VPA associated with a mobile number. It provides details on the request
    parameters, authorization field format, sample requests for UPI Collect and
    UPI Autopay, and the response parameters for success and failure scenarios.
  keywords:
    - VPA for given number API
    - VPA checker API
    - UPI Number Mapper API
  robots: index
next:
  description: ''
---
UPI Number is an 8-11 digit number that can be registered from any PSP App on NPCI. Along with this number, the Default VPA of this PSP App gets registered at the NPCI end.

The UPI Number API command is used to fetch the VPA from the NPCI database. After the customer enters the UPI Number on your website, you need to initiate this API to check whether the UPI number is registered. If the UPI number is registered it will return the VPA associated with that Mobile Number.

HTTP Method: **GET**

## Environment

| Environment    | URL                                                                                          |
| -------------- | -------------------------------------------------------------------------------------------- |
| **Production** | [https://info.payu.in/payment-mode/v1/upi/vpa](https://info.payu.in/payment-mode/v1/upi/vpa) |

## Request parameters

<Callout icon="📘" theme="info">
  **Note**: The request parameters must be passed in headers.
</Callout>

| **Field**                                 | **Description**                                                                                                                                                                                  | **Example**                                               |
| :---------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| Date<br /><code>mandatory</code>          | <code>String</code> The date and time should be in the GMT time conversion(not the IST). For example, current time in India is 18:00:00 IST, the time in the date header should be 12:30:00 GMT. | Thu, 17 Feb 2022 08:17:59 GMT                             |
| Digest<br /><code>mandatory</code>        | <code>String</code> Base 64 encode of (sha256 hash of the JSON data (post to server).                                                                                                            | <code>vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=</code> |
| Authorization<br /><code>mandatory</code> | <code>String</code> This field is in the String format. For more information, refer to [Authorization field format](#authorization-field-format).                                                |                                                           |

### Authorization field format

The **Authorization** field format is similar to the following example:

```java
hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4="
```

Where, the fields in this example are:

* **username**: The merchant key of the merchant.
* **algorithm**: This must have the value as hmac-sha256 that is used for this API.
* **headers**: This must have the value as date digest.
* **signature**: This must contain the hmacsha256 of (signing_string, merchant_secret), where:
  * **signing_string**: It must be in the following format. Here, the dateVale and digestValue is the same values in the fields listed in this table For example, "date: Thu, 17 Feb 2022 08:17:59 GMT\ndigest: vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0="

```
"date: {dateValue}"+"\\n"+"digest: {digestValue}"
  - **merchant_secret**: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to Generate Merchant Key and Salt.
```

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

The sample header is similar to the following:

> 📘 **Note:**
>
> You need to include the current date and time in the **Date** field of the header.

```java
'Date: Tue, 09 Aug 2022 12:14:51 GMT'
'Digest: vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0= '
'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI=""'
```

## Sample Request

### For UPI Collect

```curl
curl --location --request GET 'https://info.payu.in/payment-mode/v1/upi/vpa?upiNumber=9123412345' \
--header 'Content-Type: application/json' \
--header 'Date: Thu, 09 Feb 2023 10:13:28 GMT' \
--header 'Digest: 47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="T4FRZcZ3AUYNCMnpZOePT6EKwhiGwCPgglp0RLyYN6Q="'
```
```python
import requests

url = "https://info.payu.in/payment-mode/v1/upi/vpa?upiNumber=9123412345"

headers = {
    "Content-Type": "application/json",
    "Date": "Thu, 09 Feb 2023 10:13:28 GMT",
    "Digest": "47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=",
    "Authorization": 'hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="T4FRZcZ3AUYNCMnpZOePT6EKwhiGwCPgglp0RLyYN6Q="'
}

try:
    response = requests.get(url, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
```javascript
async function makeRequest() {
    const url = "https://info.payu.in/payment-mode/v1/upi/vpa?upiNumber=9123412345";
    
    const headers = {
        "Content-Type": "application/json",
        "Date": "Thu, 09 Feb 2023 10:13:28 GMT",
        "Digest": "47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=",
        "Authorization": 'hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="T4FRZcZ3AUYNCMnpZOePT6EKwhiGwCPgglp0RLyYN6Q="'
    };

    try {
        const response = await fetch(url, {
            method: "GET",
            headers: headers
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
            String url = "https://info.payu.in/payment-mode/v1/upi/vpa?upiNumber=9123412345";
            
            HttpClient client = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(10))
                .build();

            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Content-Type", "application/json")
                .header("Date", "Thu, 09 Feb 2023 10:13:28 GMT")
                .header("Digest", "47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=")
                .header("Authorization", "hmac username=\"smsplus\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"T4FRZcZ3AUYNCMnpZOePT6EKwhiGwCPgglp0RLyYN6Q=\"")
                .GET()
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
            string url = "https://info.payu.in/payment-mode/v1/upi/vpa?upiNumber=9123412345";
            
            client.DefaultRequestHeaders.Add("Content-Type", "application/json");
            client.DefaultRequestHeaders.Add("Date", "Thu, 09 Feb 2023 10:13:28 GMT");
            client.DefaultRequestHeaders.Add("Digest", "47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=");
            client.DefaultRequestHeaders.Add("Authorization", "hmac username=\"smsplus\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"T4FRZcZ3AUYNCMnpZOePT6EKwhiGwCPgglp0RLyYN6Q=\"");

            HttpResponseMessage response = await client.GetAsync(url);
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
$url = "https://info.payu.in/payment-mode/v1/upi/vpa?upiNumber=9123412345";

$headers = [
    "Content-Type: application/json",
    "Date: Thu, 09 Feb 2023 10:13:28 GMT",
    "Digest: 47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=",
    "Authorization: hmac username=\"smsplus\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"T4FRZcZ3AUYNCMnpZOePT6EKwhiGwCPgglp0RLyYN6Q=\""
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
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

### For UPI Autopay

```curl
curl --location --request GET 'https://info.payu.in/payment-mode/v1/upi/vpa?isAutoVPAValid=true&upiNumber=9123412345' \
--header 'Content-Type: application/json' \
--header 'Date: Thu, 09 Feb 2023 10:13:28 GMT' \
--header 'Digest: 47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="T4FRZcZ3AUYNCMnpZOePT6EKwhiGwCPgglp0RLyYN6Q="'
```
```python
import requests

url = "https://info.payu.in/payment-mode/v1/upi/vpa?isAutoVPAValid=true&upiNumber=9123412345"

headers = {
    "Content-Type": "application/json",
    "Date": "Thu, 09 Feb 2023 10:13:28 GMT",
    "Digest": "47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=",
    "Authorization": 'hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="T4FRZcZ3AUYNCMnpZOePT6EKwhiGwCPgglp0RLyYN6Q="'
}

try:
    response = requests.get(url, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
```javascript
async function makeRequest() {
    const url = "https://info.payu.in/payment-mode/v1/upi/vpa?isAutoVPAValid=true&upiNumber=9123412345";
    
    const headers = {
        "Content-Type": "application/json",
        "Date": "Thu, 09 Feb 2023 10:13:28 GMT",
        "Digest": "47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=",
        "Authorization": 'hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="T4FRZcZ3AUYNCMnpZOePT6EKwhiGwCPgglp0RLyYN6Q="'
    };

    try {
        const response = await fetch(url, {
            method: "GET",
            headers: headers
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
            String url = "https://info.payu.in/payment-mode/v1/upi/vpa?isAutoVPAValid=true&upiNumber=9123412345";
            
            HttpClient client = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(10))
                .build();

            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Content-Type", "application/json")
                .header("Date", "Thu, 09 Feb 2023 10:13:28 GMT")
                .header("Digest", "47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=")
                .header("Authorization", "hmac username=\"smsplus\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"T4FRZcZ3AUYNCMnpZOePT6EKwhiGwCPgglp0RLyYN6Q=\"")
                .GET()
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
            string url = "https://info.payu.in/payment-mode/v1/upi/vpa?isAutoVPAValid=true&upiNumber=9123412345";
            
            client.DefaultRequestHeaders.Add("Content-Type", "application/json");
            client.DefaultRequestHeaders.Add("Date", "Thu, 09 Feb 2023 10:13:28 GMT");
            client.DefaultRequestHeaders.Add("Digest", "47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=");
            client.DefaultRequestHeaders.Add("Authorization", "hmac username=\"smsplus\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"T4FRZcZ3AUYNCMnpZOePT6EKwhiGwCPgglp0RLyYN6Q=\"");

            HttpResponseMessage response = await client.GetAsync(url);
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
$url = "https://info.payu.in/payment-mode/v1/upi/vpa?isAutoVPAValid=true&upiNumber=9123412345";

$headers = [
    "Content-Type: application/json",
    "Date: Thu, 09 Feb 2023 10:13:28 GMT",
    "Digest: 47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=",
    "Authorization: hmac username=\"smsplus\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"T4FRZcZ3AUYNCMnpZOePT6EKwhiGwCPgglp0RLyYN6Q=\""
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
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

| **Field** | **Description**                                                                                                                                                                                                                                                           | **Example**                   |
| :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------- |
| message   | <code>String</code> This parameter returns whether the API call is success or not                                                                                                                                                                                         | Success                       |
| status    | <code>String</code> This parameter returns the any of the following status of web service call:                                                                                                                                                                           | 1                             |
| result    | <code>JSON Object</code> This field contains the result of the API query including Payer VPA and Payer Name in a JSON format. For more information on fields in the JSON, refer to <a href="#description-of-fields-in-the-result-json">Description of Fields in JSON</a>. | Refer to the subsection below |

### Description of fields in the Result JSON

| **Field**         | **Description**                                                                                                                             | **Example**           |
| :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------- |
| isValidVpa        | Whether the UPI Number is Valid or not                                                                                                      | true                  |
| payerAccountName  | If UPI Number is valid, Name associated with the VPA                                                                                        | Abc                   |
| vpa               | VPA associated with the UPI Number                                                                                                          | 9123412345@okhdfcbank |
| isAutoPayVPAValid | Whether the VPA is UPI Autopay supported or not.Note: This will only be included if **isAutoVPAValid**=true is sent as part of the request. | true                  |

## Sample Response

### Success Scenarios

* For UPI Collect

```json
{ 
    "message": "Success", 
    "status": 1, 
    "result": { 
        "isValidVpa": true, 
        "payerAccountName": "Abc", 
        "vpa": "9123412345@okhdfcbank" 
    } 
}
```

* For UPI Autopay

```json
{ 
    "message": "Success", 
    "status": 1, 
    "result": { 
        "isValidVpa": true, 
        "payerAccountName": "Abc", 
        "vpa": "9123412345@okhdfcbank", 
        "isAutoPayVPAValid": true 
    } 
}
```

### Failure Scenario

```json
{ 
    "message": "Success", 
    "status": 1, 
    "result": { 
        "isValidVpa": false, 
        "payerAccountName": "NA", 
        "vpa": null 
    } 
}
```