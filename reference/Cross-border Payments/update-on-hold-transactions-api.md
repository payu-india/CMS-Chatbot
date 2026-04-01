---
title: Update On-Hold Transactions API - CB
deprecated: false
hidden: true
metadata:
  robots: index
---
Use this API to submit additional customer information required to release on-hold settlements. After successful submission, the API updates the transaction fields and triggers a settlement fallback process.

**Endpoint**

| Environment | URL                                                 | Method |
| :---------- | :-------------------------------------------------- | :----- |
| Production  | `https://info.payu.in/opgsp/updateOnHoldTxnDetails` | POST   |

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

The request body is an array of transaction update objects.

| Parameter                                   | Description                                                          | Example   |
| :------------------------------------------ | :------------------------------------------------------------------- | :-------- |
| transactionId<br />`mandatory`              | `String` - The PayU transaction ID (requestId from GET API response) | 12345     |
| amlockTxnRequestMappingDto<br />`mandatory` | `Array` - Array of key-value pairs containing the required fields    | See below |

### amlockTxnRequestMappingDto Object

| Parameter              | Description                                                         | Example |
| :--------------------- | :------------------------------------------------------------------ | :------ |
| key<br />`mandatory`   | `String` - Field key name (from keyMappingList in GET API response) | city    |
| value<br />`mandatory` | `String` - Value for the field                                      | Mumbai  |

### Common Field Keys

| Key          | Display Name  | Validation Regex |
| :----------- | :------------ | :--------------- |
| first_name   | First name    | ^[A-Za-z]*$      |
| last_name    | Last name     | ^[A-Za-z]*$      |
| address_line | Address       | ^[^\<>%$]*$      |
| city         | City          | ^[a-zA-Z\s]*$    |
| state        | State         | ^[a-zA-Z\s]*$    |
| zipcode      | ZIP Code      | ^[1-9][0-9]{5}$  |
| invoice_id   | Invoice ID    | ^[a-zA-Z0-9]*$   |
| dob          | Date of Birth | -                |

## Sample Request

```bash
curl --location 'https://oneapi.payu.in/opgsp/updateOnHoldTxnDetails' \
--header 'accept: application/json' \
--header 'mid: 180012' \
--header 'Content-Type: application/json' \
--header 'Authorization: hmac username="<key>", algorithm="sha512", headers="date", signature="<hash>"' \
--header 'Date: Wed, 28 Jun 2023 11:25:19 GMT' \
--data '[
    {
        "transactionId": "12345",
        "amlockTxnRequestMappingDto": [
            {
                "key": "city",
                "value": "Mumbai"
            },
            {
                "key": "zipcode",
                "value": "400001"
            }
        ]
    },
    {
        "transactionId": "67890",
        "amlockTxnRequestMappingDto": [
            {
                "key": "first_name",
                "value": "John"
            },
            {
                "key": "last_name",
                "value": "Doe"
            },
            {
                "key": "address_line",
                "value": "123 Main Street"
            }
        ]
    }
]'
```
```python
import requests
import json

url = "https://oneapi.payu.in/opgsp/updateOnHoldTxnDetails"

headers = {
    'accept': 'application/json',
    'mid': '180012',
    'Content-Type': 'application/json',
    'Authorization': 'hmac username="<key>", algorithm="sha512", headers="date", signature="<hash>"',
    'Date': 'Wed, 28 Jun 2023 11:25:19 GMT'
}

data = [
    {
        "transactionId": "12345",
        "amlockTxnRequestMappingDto": [
            {
                "key": "city",
                "value": "Mumbai"
            },
            {
                "key": "zipcode",
                "value": "400001"
            }
        ]
    },
    {
        "transactionId": "67890",
        "amlockTxnRequestMappingDto": [
            {
                "key": "first_name",
                "value": "John"
            },
            {
                "key": "last_name",
                "value": "Doe"
            },
            {
                "key": "address_line",
                "value": "123 Main Street"
            }
        ]
    }
]

try:
    response = requests.post(url, headers=headers, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://oneapi.payu.in/opgsp/updateOnHoldTxnDetails";

            string jsonData = @"[
                {
                    ""transactionId"": ""12345"",
                    ""amlockTxnRequestMappingDto"": [
                        {
                            ""key"": ""city"",
                            ""value"": ""Mumbai""
                        },
                        {
                            ""key"": ""zipcode"",
                            ""value"": ""400001""
                        }
                    ]
                },
                {
                    ""transactionId"": ""67890"",
                    ""amlockTxnRequestMappingDto"": [
                        {
                            ""key"": ""first_name"",
                            ""value"": ""John""
                        },
                        {
                            ""key"": ""last_name"",
                            ""value"": ""Doe""
                        },
                        {
                            ""key"": ""address_line"",
                            ""value"": ""123 Main Street""
                        }
                    ]
                }
            ]";

            var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

            client.DefaultRequestHeaders.Clear();
            client.DefaultRequestHeaders.Add("accept", "application/json");
            client.DefaultRequestHeaders.Add("mid", "180012");
            client.DefaultRequestHeaders.Add("Authorization", "hmac username=\"<key>\", algorithm=\"sha512\", headers=\"date\", signature=\"<hash>\"");
            client.DefaultRequestHeaders.Add("Date", "Wed, 28 Jun 2023 11:25:19 GMT");

            HttpResponseMessage response = await client.PostAsync(url, content);
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
async function updateOnHoldTransactions() {
    const url = 'https://oneapi.payu.in/opgsp/updateOnHoldTxnDetails';

    const data = [
        {
            transactionId: "12345",
            amlockTxnRequestMappingDto: [
                {
                    key: "city",
                    value: "Mumbai"
                },
                {
                    key: "zipcode",
                    value: "400001"
                }
            ]
        },
        {
            transactionId: "67890",
            amlockTxnRequestMappingDto: [
                {
                    key: "first_name",
                    value: "John"
                },
                {
                    key: "last_name",
                    value: "Doe"
                },
                {
                    key: "address_line",
                    value: "123 Main Street"
                }
            ]
        }
    ];

    const requestOptions = {
        method: 'POST',
        headers: {
            'accept': 'application/json',
            'mid': '180012',
            'Content-Type': 'application/json',
            'Authorization': 'hmac username="<key>", algorithm="sha512", headers="date", signature="<hash>"',
            'Date': 'Wed, 28 Jun 2023 11:25:19 GMT'
        },
        body: JSON.stringify(data)
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

updateOnHoldTransactions()
    .then(result => console.log('Update complete'))
    .catch(error => console.error('Failed:', error));
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class UpdateOnHoldTransactions {

    public static void main(String[] args) {
        try {
            String url = "https://oneapi.payu.in/opgsp/updateOnHoldTxnDetails";

            String jsonData = "[\n" +
                "    {\n" +
                "        \"transactionId\": \"12345\",\n" +
                "        \"amlockTxnRequestMappingDto\": [\n" +
                "            {\n" +
                "                \"key\": \"city\",\n" +
                "                \"value\": \"Mumbai\"\n" +
                "            },\n" +
                "            {\n" +
                "                \"key\": \"zipcode\",\n" +
                "                \"value\": \"400001\"\n" +
                "            }\n" +
                "        ]\n" +
                "    },\n" +
                "    {\n" +
                "        \"transactionId\": \"67890\",\n" +
                "        \"amlockTxnRequestMappingDto\": [\n" +
                "            {\n" +
                "                \"key\": \"first_name\",\n" +
                "                \"value\": \"John\"\n" +
                "            },\n" +
                "            {\n" +
                "                \"key\": \"last_name\",\n" +
                "                \"value\": \"Doe\"\n" +
                "            },\n" +
                "            {\n" +
                "                \"key\": \"address_line\",\n" +
                "                \"value\": \"123 Main Street\"\n" +
                "            }\n" +
                "        ]\n" +
                "    }\n" +
                "]";

            URL urlObj = new URL(url);
            HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();

            connection.setRequestMethod("POST");
            connection.setRequestProperty("accept", "application/json");
            connection.setRequestProperty("mid", "180012");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Authorization", "hmac username=\"<key>\", algorithm=\"sha512\", headers=\"date\", signature=\"<hash>\"");
            connection.setRequestProperty("Date", "Wed, 28 Jun 2023 11:25:19 GMT");
            connection.setDoOutput(true);

            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = jsonData.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }

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

$url = 'https://oneapi.payu.in/opgsp/updateOnHoldTxnDetails';

$data = [
    [
        "transactionId" => "12345",
        "amlockTxnRequestMappingDto" => [
            [
                "key" => "city",
                "value" => "Mumbai"
            ],
            [
                "key" => "zipcode",
                "value" => "400001"
            ]
        ]
    ],
    [
        "transactionId" => "67890",
        "amlockTxnRequestMappingDto" => [
            [
                "key" => "first_name",
                "value" => "John"
            ],
            [
                "key" => "last_name",
                "value" => "Doe"
            ],
            [
                "key" => "address_line",
                "value" => "123 Main Street"
            ]
        ]
    ]
];

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'accept: application/json',
    'mid: 180012',
    'Content-Type: application/json',
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

## Response Parameters

| Parameter                      | Description                                      | Example     |
| :----------------------------- | :----------------------------------------------- | :---------- |
| transactionId<br />`mandatory` | `String` - The transaction ID that was submitted | 22224815621 |
| action<br />`optional`         | `String` - Action type: capture or refund        | capture     |
| responseDTO<br />`mandatory`   | `Object` - Response details object               | See below   |

### responseDTO Object

| Parameter                | Description                                         | Example                                                        |
| :----------------------- | :-------------------------------------------------- | :------------------------------------------------------------- |
| code<br />`optional`     | `String` - Response code. 2000 indicates success.   | 2000                                                           |
| message<br />`mandatory` | `String` - Response message                         | Success                                                        |
| status<br />`mandatory`  | `Integer` - Status indicator. 0 indicates success.  | 0                                                              |
| result<br />`optional`   | `String` - Result message for successful operations | Successfully update the fields and run the settlement fallback |
| traceId<br />`optional`  | `String` - Trace ID for debugging failed requests   | 24916044faeafc41f750c7fe63939e47                               |

## Sample Response

### Success Scenario

* Simple transaction

```json
{
    "transactionId": "22224815621",
    "action": "capture",
    "responseDTO": {
        "code": "2000",
        "message": "Success",
        "status": 0,
        "result": "Successfully update the fields and run the settlement fallback"
    }
}
```

* Multiple transactions

```json
[
    {
        "transactionId": "22224815621",
        "action": "capture",
        "responseDTO": {
            "code": "2000",
            "message": "Success",
            "status": 0,
            "result": "Successfully update the fields and run the settlement fallback"
        }
    },
    {
        "transactionId": "22224815621",
        "action": "",
        "responseDTO": {
            "message": "Invalid Merchant Id",
            "status": 1,
            "traceId": "64482922ff4453a763f5ef9f192585fc"
        }
    },
    {
        "transactionId": "22214595898",
        "action": null,
        "responseDTO": {
            "code": "4000",
            "message": "No data found for given payuId",
            "status": 1,
            "traceId": "64482922ff4453a763f5ef9f192585fc"
        }
    }
]
```

### Failure scenarios

* Invalid Merchant ID

```json
{
    "transactionId": "12345",
    "action": "capture",
    "responseDTO": {
        "message": "Invalid Merchant Id",
        "status": 1,
        "traceId": "24916044faeafc41f750c7fe63939e47"
    }
}
```

* RequestId Not in Need Response State

```json
{
    "transactionId": "22214595898",
    "action": null,
    "responseDTO": {
        "message": "RequestId not in need response state",
        "status": 1,
        "traceId": "9a45e0d772976cedc97789c8c1dd6b19"
    }
}
```

* No Data Found

```json
{
    "transactionId": "22214595898",
    "action": null,
    "responseDTO": {
        "code": "4000",
        "message": "No data found for given payuId",
        "status": 1,
        "traceId": "21df514339749b538e91102982073f0a"
    }
}
```

## Response Status Codes

| Value | Meaning                                                        | Action to Take                                                        |
| :---- | :------------------------------------------------------------- | :-------------------------------------------------------------------- |
| 0     | Response not received yet / Fields updated successfully        | Wait for processing or proceed                                        |
| 1     | Successfully update the fields and run the settlement fallback | No action required - success                                          |
| -1    | Invalid key value pair passed                                  | Verify the key names and values match the keyMappingList from GET API |
| -2    | Failed to call PayU API opgsp_update_transaction               | Retry the request or contact support                                  |
| -3    | Exception occurred in updateFieldsForAmlockTxnRetry            | Contact support with traceId                                          |
