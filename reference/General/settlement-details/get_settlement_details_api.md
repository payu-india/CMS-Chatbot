---
title: '[Backup]Get Settlement Details API'
api:
  file: updated_settlement_devguide_api_postman_collection_v1.json
  operationId: get_treasury-int-payu-settlement-settlementdetails
hidden: true
---
You can use the **Get Settlement Details** API to retrieve settlement details which the bank has to settle for you. The input is the date for which settlement details are required, where the var1 parameter is the date you want to know the settlement status or UTR (Unique Transaction Reference number). This API can be posted with version (1 or 2) in the var5 parameter.

<Callout icon="📮" theme="default">
  **Postman Collection**: Access the **Get Settlement Details API Postman Collection** from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/bbccd36/getsettlementdetailsapi](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/bbccd36/getsettlementdetailsapi)
</Callout>

**Environment**

| Environment            | URL                                                                                                                                        |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/treasury/int/payu/settlement/settlementDetails](https://test.payu.in/treasury/int/payu/settlement/settlementDetails) |
| Production Environment | [https://info.payu.in/treasury/settlement/settlementDetails](https://info.payu.in/treasury/settlement/settlementDetails)                   |

## Request Parameters

### Authentication Header

<HeaderAuthentication />

### Query Parameters

| Parameter                    | Description                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------- |
| settledOn  <br/> `mandatory` | `String` This parameter must contain the settlement date (required if utr not provided).                |
| utr<br/> `mandatory`         | `String` This parameter must contain the  Unique Transaction Reference (UTR, alternative to settledOn). |
| page<br/> `mandatory`        | `Integer` This parameter must contain the page number for pagination                                    |
| pageSize<br/> `mandatory`    | `Integer` This parameter must contain the records per page (2000-50000)                                 |
| type<br/> `optional`         | `String` This parameter must contain the Settlement type ('G' or blank).                                |
| isVersion<br/> `optional`    | `Integer` This parameter must contain the API version and it can be 1 or 2.                             |

## Sample Request

```curl
curl -X GET \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"YOUR_SIGNATURE_HASH\"" \
  -H "Date: Wed, 28 Jun 2023 11:25:19 GMT" \
  -H "mid: 135670" \
  "https://test.payu.in/treasury/int/payu/settlement/settlementDetails?settledOn=2023-06-28&page=1&pageSize=2000&type=G&isVersion=1"
```
```python
import requests
import hashlib
import hmac
import base64
from datetime import datetime

url = "https://info.payu.in/treasury/settlement/settlementDetails"
merchant_key = "<your_merchant_key>"
merchant_secret = "<your_merchant_secret>"
date_string = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

# Create HMAC SHA512 signature
message = f"date: {date_string}"
signature = hmac.new(
    merchant_secret.encode(), 
    message.encode(), 
    hashlib.sha512
).hexdigest()

headers = {
    'Authorization': f'hmac username="{merchant_key}", algorithm="sha512", headers="date", signature="{signature}"',
    'Date': date_string,
    'mid': '<your_merchant_id>'
}

params = {
    'settledOn': '2023-06-28',
    'page': 1,
    'pageSize': 5000,
    'type': '',
    'isVersion': 1
}

try:
    response = requests.get(url, headers=headers, params=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
```csharp
using System;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        var client = new HttpClient();
        var url = "https://info.payu.in/treasury/settlement/settlementDetails?settledOn=2023-06-28&page=1&pageSize=5000&type=&isVersion=1";
        var merchantKey = "<your_merchant_key>";
        var merchantSecret = "<your_merchant_secret>";
        var dateString = DateTime.UtcNow.ToString("ddd, dd MMM yyyy HH:mm:ss 'GMT'");
        
        var message = $"date: {dateString}";
        var signature = CreateHmacSha512(message, merchantSecret);
        
        client.DefaultRequestHeaders.Add("Authorization", $"hmac username=\"{merchantKey}\", algorithm=\"sha512\", headers=\"date\", signature=\"{signature}\"");
        client.DefaultRequestHeaders.Add("Date", dateString);
        client.DefaultRequestHeaders.Add("mid", "<your_merchant_id>");
        
        try
        {
            var response = await client.GetAsync(url);
            var content = await response.Content.ReadAsStringAsync();
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {content}");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
    
    static string CreateHmacSha512(string message, string secret)
    {
        var encoding = new UTF8Encoding();
        var keyByte = encoding.GetBytes(secret);
        var messageBytes = encoding.GetBytes(message);
        using (var hmac = new HMACSHA512(keyByte))
        {
            var hashmessage = hmac.ComputeHash(messageBytes);
            return BitConverter.ToString(hashmessage).Replace("-", "").ToLower();
        }
    }
}
```
```javascript
async function getSettlementDetails() {
    const crypto = require('crypto');
    const url = "https://info.payu.in/treasury/settlement/settlementDetails?settledOn=2023-06-28&page=1&pageSize=5000&type=&isVersion=1";
    const merchantKey = "<your_merchant_key>";
    const merchantSecret = "<your_merchant_secret>";
    const dateString = new Date().toUTCString();
    
    const message = `date: ${dateString}`;
    const signature = crypto.createHmac('sha512', merchantSecret).update(message).digest('hex');
    
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Authorization': `hmac username="${merchantKey}", algorithm="sha512", headers="date", signature="${signature}"`,
                'Date': dateString,
                'mid': '<your_merchant_id>'
            }
        });
        
        const data = await response.text();
        console.log(`Status: ${response.status}`);
        console.log(`Response: ${data}`);
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

getSettlementDetails();
```
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.security.MessageDigest;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.TimeZone;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

public class SettlementDetailsAPI {
    public static void main(String[] args) {
        try {
            String urlString = "https://info.payu.in/treasury/settlement/settlementDetails?settledOn=2023-06-28&page=1&pageSize=5000&type=&isVersion=1";
            String merchantKey = "<your_merchant_key>";
            String merchantSecret = "<your_merchant_secret>";
            
            SimpleDateFormat sdf = new SimpleDateFormat("EEE, dd MMM yyyy HH:mm:ss 'GMT'", Locale.US);
            sdf.setTimeZone(TimeZone.getTimeZone("GMT"));
            String dateString = sdf.format(new Date());
            
            String message = "date: " + dateString;
            String signature = createHmacSha512(message, merchantSecret);
            
            URL url = new URL(urlString);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "hmac username=\"" + merchantKey + "\", algorithm=\"sha512\", headers=\"date\", signature=\"" + signature + "\"");
            connection.setRequestProperty("Date", dateString);
            connection.setRequestProperty("mid", "<your_merchant_id>");
            
            int statusCode = connection.getResponseCode();
            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder response = new StringBuilder();
            String line;
            
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
            reader.close();
            
            System.out.println("Status Code: " + statusCode);
            System.out.println("Response: " + response.toString());
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
    
    private static String createHmacSha512(String message, String secret) throws Exception {
        Mac sha512Hmac = Mac.getInstance("HmacSHA512");
        SecretKeySpec secretKey = new SecretKeySpec(secret.getBytes(), "HmacSHA512");
        sha512Hmac.init(secretKey);
        byte[] hashBytes = sha512Hmac.doFinal(message.getBytes());
        
        StringBuilder result = new StringBuilder();
        for (byte b : hashBytes) {
            result.append(String.format("%02x", b));
        }
        return result.toString();
    }
}
```
```php
<?php
$url = "https://info.payu.in/treasury/settlement/settlementDetails?settledOn=2023-06-28&page=1&pageSize=5000&type=&isVersion=1";
$merchantKey = "<your_merchant_key>";
$merchantSecret = "<your_merchant_secret>";
$dateString = gmdate('D, d M Y H:i:s T');

$message = "date: " . $dateString;
$signature = hash_hmac('sha512', $message, $merchantSecret);

$headers = [
    'Authorization: hmac username="' . $merchantKey . '", algorithm="sha512", headers="date", signature="' . $signature . '"',
    'Date: ' . $dateString,
    'mid: <your_merchant_id>'
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if (curl_errno($ch)) {
    echo 'Error: ' . curl_error($ch);
} else {
    echo "Status Code: " . $httpCode . "\n";
    echo "Response: " . $response;
}

curl_close($ch);
?>
```

**Sample Response**

```json
{
    "status": 1,
    "msg": "Settlement details retrieved successfully",
    "result": {
        "settlementData": [
            {
                "settlementId": "SETT123456",
                "utr": "UTR123456789",
                "settlementAmount": "9800.00",
                "settlementDate": "2023-06-28",
                "transactionCount": 10,
                "totalAmount": "10000.00",
                "totalFees": "200.00",
                "totalTax": "36.00",
                "totalAdjustments": "0.00",
                "bankName": "HDFC Bank",
                "accountNumber": "XXXX5678",
                "transactions": [
                    {
                        "transactionId": "TXN001",
                        "payuId": "403993715525901741",
                        "amount": "1000.00",
                        "fees": "20.00",
                        "tax": "3.60",
                        "netAmount": "976.40",
                        "status": "settled"
                    }
                ]
            }
        ],
        "totalRecords": 1,
        "page": 1,
        "pageSize": 5000,
        "totalPages": 1
    }
}
```

## Response Parameters

| Parameter | Description                                                                                                                                       |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| status    | Response status (1 = success, 0 = failure)                                                                                                        |
| msg       | Response message                                                                                                                                  |
| result    | Main response data container in a JSON format. For more information, refer to [result JSON Fields Descriptions](#result-json-fields-descriptions) |

### result JSON Fields Descriptions

| Parameter      | Description                                                                                                                                                         |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| settlementData | Array of settlement records in a JSON format.   For more information, refer to  [settlementData JSON Fields Descriptions](#settlementdata-json-fields-descriptions) |
| totalRecords   | Total number of settlement records found                                                                                                                            |
| page           | Current page number                                                                                                                                                 |
| pageSize       | Number of records per page                                                                                                                                          |
| totalPages     | Total number of pages available                                                                                                                                     |

#### settlementData JSON Fields Descriptions

| Parameter        | Description                                                                                                                                                                  |
| :--------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| settlementId     | Unique settlement identifier                                                                                                                                                 |
| utr              | Unique Transaction Reference from bank                                                                                                                                       |
| settlementAmount | Net amount settled to merchant account                                                                                                                                       |
| settlementDate   | Date when settlement was processed (YYYY-MM-DD)                                                                                                                              |
| transactionCount | Number of transactions in this settlement                                                                                                                                    |
| totalAmount      | Total gross transaction amount                                                                                                                                               |
| totalFees        | Total processing fees deducted                                                                                                                                               |
| totalTax         | Total tax on fees                                                                                                                                                            |
| totalAdjustments | Any adjustments applied to settlement                                                                                                                                        |
| bankName         | Merchant's settlement bank name                                                                                                                                              |
| accountNumber    | Masked bank account number                                                                                                                                                   |
| transactions     | Individual transaction details (if requested) in a JSON format. For more information, refer to [transactions JSON Fields description][#transactions-json-fields-description] |

#### transactions JSON Fields description

| Parameter     | Description                      |
| :------------ | :------------------------------- |
| transactionId | Merchant transaction identifier  |
| payuId        | PayU internal transaction ID     |
| amount        | Transaction amount               |
| fees          | Fees for this transaction        |
| tax           | Tax on fees for this transaction |
| netAmount     | Net amount after fees and tax    |
| status        | Transaction settlement status    |