---
title: Get On-Hold Transactions API - CB
deprecated: false
hidden: true
metadata:
  robots: index
---
Use this API to retrieve a list of on-hold transactions that require additional information or action.

***

**Endpoint**

| Environment | URL                                              | Method |
| :---------- | :----------------------------------------------- | :----- |
| Production  | `https://info.payu.in/opgsp/getOnHoldTxnDetails` | GET    |

***

## Request Headers

| Parameter                      | Description                                 | Example                                                             |
| :----------------------------- | :------------------------------------------ | :------------------------------------------------------------------ |
| mid<br />`mandatory`           | `String` - Merchant ID of the merchant      | 8763182                                                             |
| Authorization<br />`mandatory` | `String` - HMAC SHA512 authorization header | Refer to  [Authorization field format](#authorization-field-format) |
| Date<br />`mandatory`          | `String` - Current UTC date in HTTP format  | Wed, 28 Jun 2023 11:25:19 GMT                                       |

### Authorization field format

<Accordion title="Authorization field format" icon="fa-heading">
  The **Authorization** field format is similar to the following example:

  ```java
  hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4="
  ```

  Where, the fields in this example are:

  * **username**: The merchant key of the merchant.
  * **algorithm**: This must have the value as hmac-sha256 that is used for this API.
  * **headers**: This must have the value as date digest.
  * **signature**: This must contain the hmacsha256 of (signing\_string, merchant\_secret), where:
    * **signing\_string**: It must be in the following format. Here, the dateVale and digestValue is the same values in the fields listed in this table For example, "date: Thu, 17 Feb 2022 08:17:59 GMT\ndigest: vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0="

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
</Accordion>

## Request Parameters

| Parameter                  | Description                                                                         | Example    |
| :------------------------- | :---------------------------------------------------------------------------------- | :--------- |
| startDate<br />`mandatory` | `String` - The start date from which you need to check the data. Format: YYYY-MM-DD | 2025-01-22 |
| endDate<br />`mandatory`   | `String` - The end date up to which you need the data. Format: YYYY-MM-DD           | 2025-01-25 |
| pageSize<br />`optional`   | `Integer` - Number of records per page. Default: 50                                 | 10         |
| pageOffset<br />`optional` | `Integer` - Page number for pagination. Default: 0                                  | 0          |
| orderBy<br />`optional`    | `String` - Field to order results by                                                | addedOn    |
| order<br />`optional`      | `String` - Sort order. Values: ASC, DESC                                            | ASC        |

***

## Sample Request

```bash
curl --location 'https://oneapi.payu.in/opgsp/getOnHoldTxnDetails?startDate=2025-01-22&endDate=2025-01-25&orderBy=addedOn&order=ASC&pageSize=10&pageOffset=0' \
--header 'mid: 8763182' \
--header 'Authorization: hmac username="<key>", algorithm="sha512", headers="date", signature="<hash>"' \
--header 'Date: Wed, 28 Jun 2023 11:25:19 GMT'
```
```python
import requests

url = "https://oneapi.payu.in/opgsp/getOnHoldTxnDetails"

params = {
    'startDate': '2025-01-22',
    'endDate': '2025-01-25',
    'orderBy': 'addedOn',
    'order': 'ASC',
    'pageSize': '10',
    'pageOffset': '0'
}

headers = {
    'mid': '8763182',
    'Authorization': 'hmac username="<key>", algorithm="sha512", headers="date", signature="<hash>"',
    'Date': 'Wed, 28 Jun 2023 11:25:19 GMT'
}

try:
    response = requests.get(url, headers=headers, params=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
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
            string baseUrl = "https://oneapi.payu.in/opgsp/getOnHoldTxnDetails";
            string queryParams = "?startDate=2025-01-22&endDate=2025-01-25&orderBy=addedOn&order=ASC&pageSize=10&pageOffset=0";
            string url = baseUrl + queryParams;

            client.DefaultRequestHeaders.Clear();
            client.DefaultRequestHeaders.Add("mid", "8763182");
            client.DefaultRequestHeaders.Add("Authorization", "hmac username=\"<key>\", algorithm=\"sha512\", headers=\"date\", signature=\"<hash>\"");
            client.DefaultRequestHeaders.Add("Date", "Wed, 28 Jun 2023 11:25:19 GMT");

            HttpResponseMessage response = await client.GetAsync(url);
            string responseContent = await response.Content.ReadAsStringAsync();

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
async function getOnHoldTransactions() {
    const baseUrl = 'https://oneapi.payu.in/opgsp/getOnHoldTxnDetails';
    const params = new URLSearchParams({
        startDate: '2025-01-22',
        endDate: '2025-01-25',
        orderBy: 'addedOn',
        order: 'ASC',
        pageSize: '10',
        pageOffset: '0'
    });

    const url = `${baseUrl}?${params.toString()}`;

    const requestOptions = {
        method: 'GET',
        headers: {
            'mid': '8763182',
            'Authorization': 'hmac username="<key>", algorithm="sha512", headers="date", signature="<hash>"',
            'Date': 'Wed, 28 Jun 2023 11:25:19 GMT'
        }
    };

    try {
        const response = await fetch(url, requestOptions);
        const responseJson = await response.json();

        console.log(`Status: ${response.status}`);
        console.log('Response:', responseJson);

        return responseJson;
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

getOnHoldTransactions()
    .then(result => console.log('Request complete'))
    .catch(error => console.error('Failed:', error));
```

```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class GetOnHoldTransactions {

    public static void main(String[] args) {
        try {
            String baseUrl = "https://oneapi.payu.in/opgsp/getOnHoldTxnDetails";
            String queryParams = "?startDate=2025-01-22&endDate=2025-01-25&orderBy=addedOn&order=ASC&pageSize=10&pageOffset=0";
            String url = baseUrl + queryParams;

            URL urlObj = new URL(url);
            HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();

            connection.setRequestMethod("GET");
            connection.setRequestProperty("mid", "8763182");
            connection.setRequestProperty("Authorization", "hmac username=\"<key>\", algorithm=\"sha512\", headers=\"date\", signature=\"<hash>\"");
            connection.setRequestProperty("Date", "Wed, 28 Jun 2023 11:25:19 GMT");

            int responseCode = connection.getResponseCode();
            System.out.println("Status Code: " + responseCode);

            try (BufferedReader br = new BufferedReader(new InputStreamReader(
                    connection.getInputStream(), StandardCharsets.UTF_8))) {

                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                System.out.println("Response: " + response.toString());
            }

            connection.disconnect();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```
```php
<?php

$baseUrl = 'https://oneapi.payu.in/opgsp/getOnHoldTxnDetails';
$params = http_build_query([
    'startDate' => '2025-01-22',
    'endDate' => '2025-01-25',
    'orderBy' => 'addedOn',
    'order' => 'ASC',
    'pageSize' => '10',
    'pageOffset' => '0'
]);

$url = $baseUrl . '?' . $params;

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'mid: 8763182',
    'Authorization: hmac username="<key>", algorithm="sha512", headers="date", signature="<hash>"',
    'Date: Wed, 28 Jun 2023 11:25:19 GMT'
));

$response = curl_exec($ch);

if (curl_errno($ch)) {
    echo 'cURL Error: ' . curl_error($ch);
} else {
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    echo "HTTP Status Code: " . $httpCode . "\n";
    echo "Response: " . $response . "\n";
}

curl_close($ch);

$responseData = json_decode($response, true);
if ($responseData !== null) {
    echo "Parsed Response:\n";
    print_r($responseData);
}
?>
```

***

## Response Parameters

| Parameter                   | Description                                              | Example   |
| :-------------------------- | :------------------------------------------------------- | :-------- |
| code<br />`mandatory`       | `String` - Response code. 2000 indicates success.        | 2000      |
| message<br />`mandatory`    | `String` - Response message                              | Success   |
| status<br />`mandatory`     | `Integer` - Status indicator. 0 indicates success.       | 0         |
| result<br />`mandatory`     | `Object` - Contains the result data with pagination info | See below |
| pageSize<br />`mandatory`   | `Integer` - Number of records per page                   | 10        |
| pages<br />`mandatory`      | `Integer` - Total number of pages                        | 1         |
| rows<br />`mandatory`       | `Integer` - Total number of records                      | 4         |
| pageOffset<br />`mandatory` | `Integer` - Current page offset                          | 0         |
| data<br />`mandatory`       | `Array` - Array of on-hold transaction objects           | See below |

### Transaction Object Parameters

| Parameter                                         | Description                                                                        | Example                                           |
| :------------------------------------------------ | :--------------------------------------------------------------------------------- | :------------------------------------------------ |
| requestId<br />`mandatory`                        | `String` - Unique request identifier for the on-hold transaction                   | 15908344641                                       |
| action<br />`mandatory`                           | `String` - Action type: capture or refund                                          | capture                                           |
| displayMessage<br />`mandatory`                   | `String` - Message describing the on-hold reason or required action                | Please provide additional customer information... |
| dueDate<br />`mandatory`                          | `String` - Due date by which response is required                                  | 2025-01-28 00:00:00                               |
| status<br />`mandatory`                           | `String` - Transaction status: needsResponse, rejected, dueDateExpired             | needsResponse                                     |
| keyMapping<br />`optional`                        | `String` - JSON string of required fields                                          | \{"invoice_id":""}                                |
| merchantTransactionId<br />`mandatory`            | `String` - Merchant's transaction ID                                               | 31011722620                                       |
| dateOfTransaction<br />`mandatory`                | `String` - Original transaction date                                               | 2025-01-20 11:52:27                               |
| dateOfFirstSettlementTransaction<br />`mandatory` | `String` - Date of first settlement attempt                                        | 2025-01-22 22:44:50                               |
| keyMappingList<br />`optional`                    | `Array` - List of required fields with validation rules                            | See below                                         |
| editable<br />`mandatory`                         | `Integer` - Whether the transaction can be updated. 1 = editable, 0 = not editable | 1                                                 |

### keyMappingList Object Parameters

| Parameter                        | Description                                      | Example          |
| :------------------------------- | :----------------------------------------------- | :--------------- |
| key<br />`mandatory`             | `String` - Field key name                        | zipcode          |
| displayName<br />`mandatory`     | `String` - Human-readable field name             | ZIP Code         |
| value<br />`optional`            | `String` - Current value (empty if not provided) |                  |
| order<br />`mandatory`           | `Integer` - Display order of the field           | 9                |
| validationRegex<br />`mandatory` | `String` - Regex pattern for validation          | ^[1-9][0-9]\{5}$ |

***

## Sample Responses

### 1. Rejected By Bank

```json
{
    "code": "2000",
    "message": "Success",
    "status": 0,
    "result": {
        "pageSize": 10,
        "pages": 1,
        "rows": 4,
        "pageOffset": 0,
        "data": [
            {
                "requestId": "15908344641",
                "action": "capture",
                "displayMessage": "The Bank authority has rejected this as non-individual transactions cannot be processed.",
                "dueDate": "2025-01-24 00:00:08",
                "status": "rejected",
                "keyMapping": "",
                "merchantTransactionId": "31011722620",
                "dateOfTransaction": "2025-01-20 11:52:27",
                "dateOfFirstSettlementTransaction": "2025-01-22 22:44:50",
                "keyMappingList": null,
                "editable": 0
            }
        ]
    }
}
```

### 2. Due Date Expired

```json
{
    "code": "2000",
    "message": "Success",
    "status": 0,
    "result": {
        "pageSize": 10,
        "pages": 1,
        "rows": 4,
        "pageOffset": 0,
        "data": [
            {
                "requestId": "15916911894",
                "action": "refund",
                "displayMessage": "amlockDueDateExpiredMsg",
                "dueDate": "2025-01-26 00:00:08",
                "status": "dueDateExpired",
                "keyMapping": "{\"invoice_id\":\"\"}",
                "merchantTransactionId": "31017154721",
                "dateOfTransaction": "2025-01-22 13:08:36",
                "dateOfFirstSettlementTransaction": "2025-01-23 17:17:40",
                "keyMappingList": null,
                "editable": 0
            }
        ]
    }
}
```

### 3. Needs Response

```json
{
    "code": "2000",
    "message": "Success",
    "status": 0,
    "result": {
        "pageSize": 10,
        "pages": 1,
        "rows": 4,
        "pageOffset": 0,
        "data": [
            {
                "requestId": "15916911884",
                "action": "capture",
                "displayMessage": "Please provide additional customer information to release settlement from on-hold by 2025-01-27 00:00:00 IST. Your prompt response is greatly appreciated.",
                "dueDate": "2025-01-27 00:00:00",
                "status": "needsResponse",
                "keyMapping": "{\"invoice_id\":\"\"}",
                "merchantTransactionId": "31017154721",
                "dateOfTransaction": "2025-01-21 13:15:27",
                "dateOfFirstSettlementTransaction": "2025-01-23 17:17:40",
                "keyMappingList": [
                    {
                        "key": "invoice_id",
                        "displayName": "Invoice ID",
                        "value": "",
                        "order": 5,
                        "validationRegex": "^[a-zA-Z0-9]*$"
                    }
                ],
                "editable": 1
            }
        ]
    }
}
```

### 4. Needs Response with Multiple Fields

```json
{
    "code": "2000",
    "message": "Success",
    "status": 0,
    "result": {
        "pageSize": 10,
        "pages": 1,
        "rows": 1,
        "pageOffset": 0,
        "data": [
            {
                "requestId": "15923771684",
                "action": "refund",
                "displayMessage": "Please provide additional customer information to release settlement from on-hold by 2025-01-28 00:00:00 IST. Your prompt response is greatly appreciated.",
                "dueDate": "2025-01-28 00:00:00",
                "status": "needsResponse",
                "keyMapping": "{\"address_line\":\"\",\"zipcode\":\"\",\"city\":\"\",\"state\":\"\",\"first_name\":\"\",\"last_name\":\"\"}",
                "merchantTransactionId": "31014100522",
                "dateOfTransaction": "2025-01-22 10:58:18",
                "dateOfFirstSettlementTransaction": "2025-01-24 16:13:24",
                "keyMappingList": [
                    {
                        "key": "first_name",
                        "displayName": "First name",
                        "value": "",
                        "order": 1,
                        "validationRegex": "^[A-Za-z]*$"
                    },
                    {
                        "key": "last_name",
                        "displayName": "Last name",
                        "value": "",
                        "order": 2,
                        "validationRegex": "^[A-Za-z]*$"
                    },
                    {
                        "key": "address_line",
                        "displayName": "Address",
                        "value": "",
                        "order": 6,
                        "validationRegex": "^[^<>%$]*$"
                    },
                    {
                        "key": "city",
                        "displayName": "City",
                        "value": "",
                        "order": 7,
                        "validationRegex": "^[a-zA-Z\\s]*$"
                    },
                    {
                        "key": "state",
                        "displayName": "State",
                        "value": "",
                        "order": 8,
                        "validationRegex": "^[a-zA-Z\\s]*$"
                    },
                    {
                        "key": "zipcode",
                        "displayName": "ZIP Code",
                        "value": "",
                        "order": 9,
                        "validationRegex": "^[1-9][0-9]{5}$"
                    }
                ],
                "editable": 1
            }
        ]
    }
}
```
