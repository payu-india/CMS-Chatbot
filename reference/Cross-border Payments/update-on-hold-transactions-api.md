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

| Parameter                      | Description                                | Example                                                             |
| :----------------------------- | :----------------------------------------- | :------------------------------------------------------------------ |
| mid<br />`mandatory`           | `String` - Merchant ID of the merchant     | 8763182                                                             |
| Authorization<br />`mandatory` | `String` - SHA512 authorization header     | Refer to  [Authorization field format](#authorization-field-format) |
| Date<br />`mandatory`          | `String` - Current UTC date in HTTP format | Wed, 28 Jun 2023 11:25:19 GMT                                       |

### Authorization field format

<Accordion title="Authorization field format" icon="fa-heading">
  The **Authorization** field format is similar to the following example:

  ```
  hmac username="smsplus", algorithm="sha512", headers="date", signature="8a913dab44bdd4721857728ecf19e52bb3b57cd1a77dd92c32829e4a4612eb2445e3bdc84b74dd259b92d53bd6d8ebd75853643de5edd1cfda326e13d87d212d"
  ```

  Where, the fields in this example are:

  * **username**: The merchant key of the merchant.
  * **algorithm**: This must have the value `sha512` for this API.
  * **headers**: This must have the value `date`.
  * **signature**: SHA512 hex hash of the hash string `{request_body}|{date}|{merchant_secret}`, where:
    * **request_body**: The raw JSON request body. Use an empty string if the body is empty.
    * **date**: The same value sent in the **Date** request header (for example, `Wed, 28 Jun 2023 11:25:19 GMT`).
    * **merchant_secret**: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to Generate Merchant Key and Salt.

  > 📘 **Note:**
  >
  > You need to include the current date and time in the **Date** field of the header.
</Accordion>

## Request Parameters

The request body is an array of transaction update objects.

| Parameter                                   | Description                                                       | Example   |
| :------------------------------------------ | :---------------------------------------------------------------- | :-------- |
| transactionId<br />`mandatory`              | `String` - The PayU transaction ID                                | 12345     |
| amlockTxnRequestMappingDto<br />`mandatory` | `Array` - Array of key-value pairs containing the required fields | See below |

### amlockTxnRequestMappingDto Object

| Parameter              | Description                                                         | Example |
| :--------------------- | :------------------------------------------------------------------ | :------ |
| key<br />`mandatory`   | `String` - Field key name (from keyMappingList in GET API response) | city    |
| value<br />`mandatory` | `String` - Value for the field                                      | Mumbai  |

### Common Field Keys

| Key           | Display Name  | Validation Regex  |
| :------------ | :------------ | :---------------- |
| first\_name   | First name    | ^\[A-Za-z]\*$     |
| last\_name    | Last name     | ^\[A-Za-z]\*$     |
| address\_line | Address       | ^\[^\<>%$]\*$     |
| city          | City          | ^\[a-zA-Z\s]\*$   |
| state         | State         | ^\[a-zA-Z\s]\*$   |
| zipcode       | ZIP Code      | ^\[1-9]\[0-9]{5}$ |
| invoice\_id   | Invoice ID    | ^\[a-zA-Z0-9]\*$  |
| dob           | Date of Birth | -                 |

## Sample Request

```bash
curl --location 'https://info.payu.in/opgsp/updateOnHoldTxnDetails' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'mid: 2' \
--header 'Authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="8a913dab44bdd4721857728ecf19e52bb3b57cd1a77dd92c32829e4a4612eb2445e3bdc84b74dd259b92d53bd6d8ebd75853643de5edd1cfda326e13d87d212d"' \
--header 'Date: Wed, 03 Jun 2026 12:45:54 GMT' \
--data '[
    {
        "transactionId": "28349973129",
        "amlockTxnRequestMappingDto": [
            {
                "key": "invoice_id",
                "value": "8c7e492c0278496ba0c7cd862d94dcce"
            }
        ]
    }
]'
```
```python
import requests
import json

url = "https://info.payu.in/opgsp/updateOnHoldTxnDetails"

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
            string url = "https://info.payu.in/opgsp/updateOnHoldTxnDetails";

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
    const url = 'https://info.payu.in/opgsp/updateOnHoldTxnDetails';

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
            String url = "https://info.payu.in/opgsp/updateOnHoldTxnDetails";

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

$url = 'https://info.payu.in/opgsp/updateOnHoldTxnDetails';

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

## Sample Script to Generate Header

Use this pre-request script to generate the **Date** and **Authorization** headers. Set `merchantKey` and `merchantSalt` before sending the request. You may use them in Postman as prerequisite in this regard.

```javascript
function encode_base64(value) {
    return CryptoJS.enc.Base64.stringify(value);
}
// date
var date = new Date();
//var date = "Thu, 25 Apr 2019 10:59:33 GMT";
date = date.toUTCString();
console.log("date " + date);
// digest
console.log("request "  + request['data']);
// console.log("sha256.  " + CryptoJS.SHA256(isEmpty(request['data'])));
var digest = encode_base64(CryptoJS.SHA256(isEmpty(request['data'])?"":request['data']));
console.log("Digest " + digest);
// authorization
var authorization = getAuthHeader(date, digest);
postman.setEnvironmentVariable('date', date);
postman.setEnvironmentVariable('digest', digest);
postman.setEnvironmentVariable('authorization', authorization);
console.log("Authorization " + authorization);

var merchant_key = pm.variables.get("merchantKey");
var merchant_secret = pm.variables.get("merchantSalt");

// date
var date = new Date();
// var date = "Wed, 28 Jun 2023 11:25:19 GMT";
date = date.toUTCString();

// authorization
var authorization = getAuthHeader(date);
console.log(authorization);

function getAuthHeader(date) {
var AUTH_TYPE = 'sha512';
var data = isEmpty(request['data'])?"":request['data'];
var hash_string = data + '|' + date + '|' + merchant_secret;
console.log("Hash String is ", hash_string);
var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
var authHeader = 'hmac username="' + merchant_key + '", ' + 'algorithm="' + AUTH_TYPE + '", headers="date", signature="' + hash + '"'
return authHeader;
}

pm.environment.set('date', date);
pm.environment.set('authorization', authorization);
pm.environment.set('merchant_key',merchant_key);
pm.environment.set('merchant_secret',merchant_secret);

function isEmpty(obj) {
for(var key in obj) {
if(obj.hasOwnProperty(key))
return false;
}
return true;
}
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

- Simple transaction

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

- Multiple transactions

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

- Invalid Merchant ID

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

- RequestId Not in Need Response State

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

- No Data Found

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
| -2    | Failed to call PayU API opgsp\_update\_transaction             | Retry the request or contact support                                  |
| -3    | Exception occurred in updateFieldsForAmlockTxnRetry            | Contact support with traceId                                          |

<br />
