---
title: Provision Alt ID API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Provision Alt ID API
  description: >-
    The document provides information on the Provision Alt ID API used to
    provision Alt ID from PayU for transactions outside PayU, including request
    parameters, sample request and response, and Java code for encryption.
  keywords:
    - Provision Alt ID API
    - ' Alt ID Provisioning API'
  robots: index
next:
  description: ''
---
The **Provision Alt ID API** is used to provision Alt ID from PayU, but process transaction outside PayU. This section describes the request parameters with sample request and response.

HTTP Method: **POST**

## Environment

| Environment | URL                                                                      |
| ----------- | ------------------------------------------------------------------------ |
| Test        | [https://apitest.payu.in/card/altid](https://apitest.payu.in/card/altid) |
| Production  | [https://api.payu.in/card/altid](https://api.payu.in/card/altid)         |

## Request Headers

The request header contains the following fields:

<br />

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
        Date<br /><code>mandatory</code>
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
        Digest<br /><code>mandatory</code>
      </td>

      <td>
        Base 64 encode of (sha256 hash of the JSON data (post to server).
      </td>

      <td>
        <code>vpGay5D/dmfoDupA
        LPplYGucJAln9gS2
        9g5Orn+8TC0=</code>
      </td>
    </tr>

    <tr>
      <td>
        Authorization<br /><code>mandatory</code>
      </td>

      <td>
        This field is in the format described in [Authorization format](#Authorization-format).
      </td>

      <td>
        hmac username="smsplus",
        algorithm="hmac-sha256",
        headers="date digest", signature="zGmP5Zeqm1pxNa
        +d68DWfQFXhxoqf3st353SkYvX8HI="
      </td>
    </tr>

    <tr>
      <td>
        platformId<br /><code>mandatory</code>
      </td>

      <td>
        This field contains the platform ID and include the value as **1**.
      </td>

      <td>
        1
      </td>
    </tr>
  </tbody>
</Table>

##### Authorization format

<code>hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4="</code>
Where the above format includes the following:

* **username**: The merchant key of the merchant.
* **algorithm**: This must have the value as **hmac-sha256** that is used for this API
* **headers**: This must have the value as **date digest**
* **signature**: This must contain the hmacsha256 of (signing_string, merchant_secret), where:
  * **signing_string**: This is in the "**Date**"+"\n"+"**Digest**" format. Here, the Date and Digest is the same values in the fields listed in this table For example, "Thu, 17 Feb 2022 08:17:59 GMT""\n"+"vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0="
  * **merchant_secret**: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard)

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

## Request parameters

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
        clientReferenceId<br /><code>optional</code>
      </td>

      <td>
        The alphanumeric value to track the request.
      </td>

      <td>
        DKSAI80033U2BRRE90FD0SDJAOSA
      </td>
    </tr>

    <tr>
      <td>
        cardNumber<br /><code>mandatory</code>
      </td>

      <td>
        The card number entered by the customer.
      </td>

      <td>
        XXXXXXXXXXXX3669
      </td>
    </tr>

    <tr>
      <td>
        nameOnCard<br /><code>optional</code>
      </td>

      <td>
        The name on card entered by the customer.
      </td>

      <td>
        Ashish K
      </td>
    </tr>

    <tr>
      <td>
        cardType<br /><code>optional</code>
      </td>

      <td>
        The type card used by the customer.
      </td>

      <td>
        AMEX
      </td>
    </tr>

    <tr>
      <td>
        expiryMonth<br /><code>mandatory</code>
      </td>

      <td>
        The expiry date of card entered by the customer.
      </td>

      <td>
        12
      </td>
    </tr>

    <tr>
      <td>
        expiryYear<br /><code>mandatory</code>
      </td>

      <td>
        The expiry year of the card entered by the customer.
      </td>

      <td>
        26
      </td>
    </tr>

    <tr>
      <td>
        cvv<br /> <code>mandatory</code>
      </td>

      <td>
        The CVV or secret code found behind the cardentered by the customer.
      </td>

      <td>
        000
      </td>
    </tr>

    <tr>
      <td>
        mail<br /> <code>optional</code>
      </td>

      <td>
        The mail ID of the customer.
      </td>

      <td>
        [testmail@test.com](mailto:testmail@test.com)
      </td>
    </tr>

    <tr>
      <td>
        amount<br /><code>mandatory</code>
      </td>

      <td>
        The amount of the transaction.
      </td>

      <td>
        100
      </td>
    </tr>

    <tr>
      <td>
        authenticationCode<br /><code>conditional</code>
      </td>

      <td>
        The authentication code for the transaction.
        **Note**: This parameter is required for RUPAY cards.
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl --location --request POST 'https://apitest.payu.in/card/altid' \
--header 'Content-Type: application/json' \
--header 'date: Fri, 12 Jan 2024 10:13:08 GMT' \
--header 'digest: n6XDOH1fAUrD+WC47SFsa+mNxmm1+yTrUAupmxbYMoc=' \
--header 'authorization: hmac username="DGy1hY", algorithm="hmac-sha256", headers="date digest", signature="FBp5QsOIxBzxyDnRXPCt76htkdm5ijc4nm/Hvyvaw/s="' \
--data-raw '{
    "clientReferenceId": null,
    "cardNumber": "5299920970259709",
    "nameOnCard": "Jagadesh Reddy",
    "cardType": "MAST",
    "expiryMonth": "06",
    "expiryYear": "2024",
    "cvv": "000",
    "mail": "jagadesh@reddy.com",
    "amount": "100",
    "authenticationCode": null
}'
```
```python
import requests
import json

url = "https://apitest.payu.in/card/altid"

headers = {
    "Content-Type": "application/json",
    "date": "Fri, 12 Jan 2024 10:13:08 GMT",
    "digest": "n6XDOH1fAUrD+WC47SFsa+mNxmm1+yTrUAupmxbYMoc=",
    "authorization": 'hmac username="DGy1hY", algorithm="hmac-sha256", headers="date digest", signature="FBp5QsOIxBzxyDnRXPCt76htkdm5ijc4nm/Hvyvaw/s="'
}

data = {
    "clientReferenceId": None,
    "cardNumber": "5299920970259709",
    "nameOnCard": "Jagadesh Reddy",
    "cardType": "MAST",
    "expiryMonth": "06",
    "expiryYear": "2024",
    "cvv": "000",
    "mail": "jagadesh@reddy.com",
    "amount": "100",
    "authenticationCode": None
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
    const url = "https://apitest.payu.in/card/altid";
    
    const headers = {
        "Content-Type": "application/json",
        "date": "Fri, 12 Jan 2024 10:13:08 GMT",
        "digest": "n6XDOH1fAUrD+WC47SFsa+mNxmm1+yTrUAupmxbYMoc=",
        "authorization": 'hmac username="DGy1hY", algorithm="hmac-sha256", headers="date digest", signature="FBp5QsOIxBzxyDnRXPCt76htkdm5ijc4nm/Hvyvaw/s="'
    };

    const requestData = {
        "clientReferenceId": null,
        "cardNumber": "5299920970259709",
        "nameOnCard": "Jagadesh Reddy",
        "cardType": "MAST",
        "expiryMonth": "06",
        "expiryYear": "2024",
        "cvv": "000",
        "mail": "jagadesh@reddy.com",
        "amount": "100",
        "authenticationCode": null
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
            String url = "https://apitest.payu.in/card/altid";
            
            String jsonData = "{\"clientReferenceId\":null,\"cardNumber\":\"5299920970259709\",\"nameOnCard\":\"Jagadesh Reddy\",\"cardType\":\"MAST\",\"expiryMonth\":\"06\",\"expiryYear\":\"2024\",\"cvv\":\"000\",\"mail\":\"jagadesh@reddy.com\",\"amount\":\"100\",\"authenticationCode\":null}";
            
            HttpClient client = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(10))
                .build();

            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Content-Type", "application/json")
                .header("date", "Fri, 12 Jan 2024 10:13:08 GMT")
                .header("digest", "n6XDOH1fAUrD+WC47SFsa+mNxmm1+yTrUAupmxbYMoc=")
                .header("authorization", "hmac username=\"DGy1hY\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"FBp5QsOIxBzxyDnRXPCt76htkdm5ijc4nm/Hvyvaw/s=\"")
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
            string url = "https://apitest.payu.in/card/altid";
            
            client.DefaultRequestHeaders.Add("date", "Fri, 12 Jan 2024 10:13:08 GMT");
            client.DefaultRequestHeaders.Add("digest", "n6XDOH1fAUrD+WC47SFsa+mNxmm1+yTrUAupmxbYMoc=");
            client.DefaultRequestHeaders.Add("authorization", "hmac username=\"DGy1hY\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"FBp5QsOIxBzxyDnRXPCt76htkdm5ijc4nm/Hvyvaw/s=\"");

            var requestData = new
            {
                clientReferenceId = (string)null,
                cardNumber = "5299920970259709",
                nameOnCard = "Jagadesh Reddy",
                cardType = "MAST",
                expiryMonth = "06",
                expiryYear = "2024",
                cvv = "000",
                mail = "jagadesh@reddy.com",
                amount = "100",
                authenticationCode = (string)null
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
$url = "https://apitest.payu.in/card/altid";

$headers = [
    "Content-Type: application/json",
    "date: Fri, 12 Jan 2024 10:13:08 GMT",
    "digest: n6XDOH1fAUrD+WC47SFsa+mNxmm1+yTrUAupmxbYMoc=",
    "authorization: hmac username=\"DGy1hY\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"FBp5QsOIxBzxyDnRXPCt76htkdm5ijc4nm/Hvyvaw/s=\""
];

$requestData = [
    "clientReferenceId" => null,
    "cardNumber" => "5299920970259709",
    "nameOnCard" => "Jagadesh Reddy",
    "cardType" => "MAST",
    "expiryMonth" => "06",
    "expiryYear" => "2024",
    "cvv" => "000",
    "mail" => "jagadesh@reddy.com",
    "amount" => "100",
    "authenticationCode" => null
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
## Response Parameters

| Parameter           | Value                                            |
| ------------------- | ------------------------------------------------ |
| statusCode          | TK0000, INV001, ONB001, TK0002                   |
| status              | 0(failure), 1(success)                           |
| clientReferenceId   | Same id sent in request                          |
| cryptogram          | Cryptogram details                               |
| altIdToken          | ALT ID                                           |
| expiryMonth         | Expiry month of AltId Token                      |
| expiryYear          | Expiry year of AltId Token                       |
| las4                | Last 4 digits of the card                        |
| par                 | Payment Account Reference(Unique Id of the card) |
| msg                 | Success or failure message                       |
| errorDesc           | Error description                                |
| errorMsgFromNetwork | Message received from the network                |

## Sample response

### Success scenario

```json
{
    "statusCode": "EA01",
    "status": 1,
    "clientReferenceId": "339c6c458ac3161da90839",
    "tokenReferenceId": "018b90aa-b9c5-41c0-8528-71dd22b6b65e",
    "cryptogram": "IjDso7oA5xFBdiOd/m035meW5UpImrSRAXWMe7406m0=",
    "altInfo": {
        "altIdToken": "3612143521818338",
        "expiryMonth": "09",
        "expiryYear": "2026",
        "last4": "6622"
    },
    "msg": "AltID created successful",
    "par": "799F3ED865F5965CC760A32682BA8A80F19E99ECB3F7F03574C14F5B6C3EB2C1"
}
```

### Failure Ssenarios

* Invalid card number

```json
{
    "statusCode": "EA02",
    "errorDesc": "CardNo is Invalid. Please check and initiate again",
    "status": 0
}
```

* Invalid expiry month of card

```json
{
    "statusCode": "EA02",
    "errorDesc": "Expiry year is Invalid. Please check and initiate again",
    "status": 0
}
```

* Invalid CVV specified for card

```json
{
    "statusCode": "EA02",
    "errorDesc": "CVV is Invalid. Please check and initiate again",
    "status": 0
}
```

* Internal error

```json
{
    "statusCode": "EA03",
    "errorDesc": "Technical error. Please try again",
    "status": 0,
    "clientReferenceId": "6751c7ca1365415b6b0a"
}
```

* Invalid Acquired Merchant ID

```json
{
    "statusCode": "EA04",
    "errorDesc": "Invalid merchant ID configuration. Please reachout to PayU support team",
    "status": 0,
    "clientReferenceId": "6b831fb451717be74130"
}
```

* Card Network Failure

```json
{
    "statusCode": "EA05",
    "errorDesc": "Card network seems to be down. Please retry after some time",
    "status": 0,
    "clientReferenceId": "6700ac2393ec5091af75"
}
```

* Invalid Authentication Code (RUPAY)

```json
{
    "statusCode": "EA06",
    "errorDesc": "Invalid auth code configuration. Please raise this to PayU support team",
    "status": 0,
    "clientReferenceId": "6bf002e42595130f3b5d"
}
```

* Invalid AcquirerInstance id Code (MASTER)

```json
{
    "statusCode": "EA07",
    "errorDesc": "Invalid Acq ID Code configuration. Please raise this to PayU support team",
    "status": 0,
    "clientReferenceId": "6c3d6d35a5982a3d9637"
}
```

* Merchant Not Onboarded(AMEX)

```json
{
    "statusCode": "EA09",
    "errorDesc": "Invalid merchant ID configuration. Please reach out to PayU support team",
    "status": 0,
    "clientReferenceId": "85096f63e4366f9d199"
}
```

* Merchant Invalid Or Merchant AltId is InActive

```json
{
    "statusCode": "EA10",
    "errorDesc": "The MID is not active. Please raise this to PayU support team",
    "status": 0
}
```

* Mastercard DPA creation in progress

```json
{
    "statusCode": "EA082",
    "errorDesc": "Mastercard DPA creation in progress. Please retry after 15 mins.",
    "status": 0,
    "clientReferenceId": "befd87386aebf388206",
    "errorMsgFromNetwork": "DPA entity data not found for the given clientId or dpaId in getDpaEntityData request."
}
```

* Invalid Acquired Merchant ID Code configuration

```json
{
    "statusCode": "EA07",
    "errorDesc": "Invalid Acq ID Code configuration. Please raise this to PayU support team",
    "status": 0,
    "clientReferenceId": "bf117fe66fa5148e4e5d"
}
```

* Invalid expiry month

```json
 
{
    "statusCode": "EA025",
    "errorDesc": "Expiry month is Invalid. Please check and initiate again..",
    "status": 0
}
```
