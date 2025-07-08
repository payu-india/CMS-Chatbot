---
title: API Integration for Split During Transaction
deprecated: false
hidden: true
metadata:
  robots: index
---
\_payment API allows you to split a payment among multiple merchants or entities during the transaction process that is split during transaction. This is ideal for marketplace platforms where payment distribution needs to happen at the time of transaction with fixed, predetermined amounts.

## Prerequisites

Before integrating Absolute Split During Transaction, ensure you have:

1. **PayU Merchant Account**: An active PayU merchant account set up as an aggregator/marketplace
2. **Child Merchants Onboarded**: Child merchants must be registered and approved in the PayU system
3. **API Credentials**: Your merchant `key` and `salt` values from the PayU dashboard
4. **Transaction Logic**: A system to calculate the exact split amounts for each transaction

### Getting Your API Credentials

1. Log into your [PayU Dashboard](https://test.payu.in/merchant/dashboard).
2. Navigate to **Developer** → **API Keys**.
3. Copy your **key** and **Salt** values.
4. Note your Merchant ID for reference.

## Step 1: Prepare the Split Request

Create a JSON structure that defines how the transaction amount should be split among different merchants:

```json
{
  "type": "absolute",
  "splitInfo": {
    "MERCHANT_KEY_1": {
      "aggregatorSubTxnId": "SUB_TXN_ID_1",
      "aggregatorSubAmt": "600",
      "aggregatorCharges": "50"
    },
    "MERCHANT_KEY_2": {
      "aggregatorSubTxnId": "SUB_TXN_ID_2",
      "aggregatorSubAmt": "400"
    }
  }
}
```

**Parameters Explained**:

* `type`: Must be set to "absolute" for Absolute Split During Transaction
* `splitInfo`: Contains the split details for each merchant
  * `MERCHANT_KEY_x`: The merchant key of the child merchant
  * `aggregatorSubTxnId`: A unique ID for this sub-transaction
  * `aggregatorSubAmt`: The exact amount to be settled to this merchant
  * `aggregatorCharges`: (Optional) Platform fees or service charges

> 📘 Split calculation:
>
> The sum of all `aggregatorSubAmt` values plus any `aggregatorCharges` must equal the total transaction amount.

## Step 2: Generate the Payment Request

Create a payment request that includes the split information:

**Sample request**

```curl
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=Ax4j7J" \
  -d "txnid=payment-txnid-1" \
  -d "amount=10" \
  -d "productinfo=Product Info" \
  -d "firstname=Payu-Admin" \
  -d "email=test@example.com" \
  -d "phone=1234567890" \
  -d "pg=CC" \
  -d "bankcode=VISA" \
  -d "ccnum=4111111111111111" \
  -d "ccname=Test User" \
  -d "ccvv=123" \
  -d "ccexpmon=12" \
  -d "ccexpyr=2028" \
  -d "surl=https://example.com/success" \
  -d "furl=https://example.com/failure" \
  -d 'splitRequest={"type":"absolute","splitInfo":{"P41sCY":{"aggregatorSubTxnId":"0e7411799c9f0e96620c11","aggregatorSubAmt":"3","aggregatorCharges":"2"},"P41sCK":{"aggregatorSubTxnId":"0e7411799c9f0e96620c22","aggregatorSubAmt":"5"}}}' \
  -d "hash=6e700275583072c0361bac771a4166a4be5334112d59e40181c5668895c477a047c7be250068186fd26ca72928d7e168f92bb96003a7fffbf4933bb818f4c48a"

```
```php
$key = "Ax4j7J";
$salt = "t5atu4TyCvrJDPxAYrmfJfzd90kbXMfL";
$txnid = "payment-txnid-1";
$amount = "10";
$productinfo = "Product Info";
$firstname = "Payu-Admin";
$email = "test@example.com";
$phone = "1234567890";
$pg = "CC";
$bankcode = "VISA";
$ccnum = "4111111111111111";
$ccname = "Test User";
$ccvv = "123";
$ccexpmon = "12";
$ccexpyr = "2028";
$surl = "https://example.com/success";
$furl = "https://example.com/failure";

// Split request JSON
$splitRequest = json_encode([
    'type' => 'absolute',
    'splitInfo' => [
        'P41sCY' => [
            'aggregatorSubTxnId' => '0e7411799c9f0e96620c11',
            'aggregatorSubAmt' => '3',
            'aggregatorCharges' => '2'
        ],
        'P41sCK' => [
            'aggregatorSubTxnId' => '0e7411799c9f0e96620c22',
            'aggregatorSubAmt' => '5'
        ]
    ]
], JSON_UNESCAPED_SLASHES);

// Generate hash
$hashString = "{$key}|{$txnid}|{$amount}|{$productinfo}|{$firstname}|{$email}|||||||||||{$salt}|{$splitRequest}";
$hash = hash("sha512", $hashString);

// Create form data
$postData = [
    'key' => $key,
    'txnid' => $txnid,
    'amount' => $amount,
    'productinfo' => $productinfo,
    'firstname' => $firstname,
    'email' => $email,
    'phone' => $phone,
    'pg' => $pg,
    'bankcode' => $bankcode,
    'ccnum' => $ccnum,
    'ccname' => $ccname,
    'ccvv' => $ccvv,
    'ccexpmon' => $ccexpmon,
    'ccexpyr' => $ccexpyr,
    'surl' => $surl,
    'furl' => $furl,
    'splitRequest' => $splitRequest,
    'hash' => $hash
];

// Initialize cURL session
$ch = curl_init("https://test.payu.in/_payment");
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/x-www-form-urlencoded'
]);

// Execute request and get response
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

// Display response
echo "HTTP Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";


```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using System.Web;

class PayUAbsoluteSplitExample
{
    static async Task Main(string[] args)
    {
        // Merchant details
        string key = "Ax4j7J";
        string salt = "t5atu4TyCvrJDPxAYrmfJfzd90kbXMfL";
        string txnid = "payment-txnid-1";
        string amount = "10";
        string productinfo = "Product Info";
        string firstname = "Payu-Admin";
        string email = "test@example.com";
        string phone = "1234567890";
        string pg = "CC";
        string bankcode = "VISA";
        string ccnum = "4111111111111111";
        string ccname = "Test User";
        string ccvv = "123";
        string ccexpmon = "12";
        string ccexpyr = "2028";
        string surl = "https://example.com/success";
        string furl = "https://example.com/failure";

        // Create split request object
        var splitRequestObj = new
        {
            type = "absolute",
            splitInfo = new
            {
                P41sCY = new
                {
                    aggregatorSubTxnId = "0e7411799c9f0e96620c11",
                    aggregatorSubAmt = "3",
                    aggregatorCharges = "2"
                },
                P41sCK = new
                {
                    aggregatorSubTxnId = "0e7411799c9f0e96620c22",
                    aggregatorSubAmt = "5"
                }
            }
        };

        // Convert to JSON
        string splitRequest = JsonSerializer.Serialize(splitRequestObj, new JsonSerializerOptions
        {
            WriteIndented = false
        });

        // Generate hash
        string hashString = $"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|||||||||||{salt}|{splitRequest}";
        string hash = ComputeSHA512Hash(hashString);

        // Create form data
        var formData = new Dictionary<string, string>
        {
            ["key"] = key,
            ["txnid"] = txnid,
            ["amount"] = amount,
            ["productinfo"] = productinfo,
            ["firstname"] = firstname,
            ["email"] = email,
            ["phone"] = phone,
            ["pg"] = pg,
            ["bankcode"] = bankcode,
            ["ccnum"] = ccnum,
            ["ccname"] = ccname,
            ["ccvv"] = ccvv,
            ["ccexpmon"] = ccexpmon,
            ["ccexpyr"] = ccexpyr,
            ["surl"] = surl,
            ["furl"] = furl,
            ["splitRequest"] = splitRequest,
            ["hash"] = hash
        };

        await SendPaymentRequest(formData);
    }

    static string ComputeSHA512Hash(string input)
    {
        using (SHA512 sha512 = SHA512.Create())
        {
            byte[] inputBytes = Encoding.UTF8.GetBytes(input);
            byte[] hashBytes = sha512.ComputeHash(inputBytes);

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < hashBytes.Length; i++)
            {
                sb.Append(hashBytes[i].ToString("x2"));
            }
            return sb.ToString();
        }
    }

    static async Task SendPaymentRequest(Dictionary<string, string> formData)
    {
        try
        {
            using (HttpClient client = new HttpClient())
            {
                // Create form URL encoded content
                var content = new FormUrlEncodedContent(formData);

                // Send request
                HttpResponseMessage response = await client.PostAsync("https://test.payu.in/_payment", content);
                
                // Get response
                string responseContent = await response.Content.ReadAsStringAsync();
                
                Console.WriteLine($"Status Code: {response.StatusCode}");
                Console.WriteLine($"Response: {responseContent}");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }

    static string GeneratePaymentForm(Dictionary<string, string> formData)
    {
        // For server-side rendering of the payment form
        StringBuilder formHtml = new StringBuilder();
        formHtml.AppendLine("<!DOCTYPE html>");
        formHtml.AppendLine("<html>");
        formHtml.AppendLine("<head>");
        formHtml.AppendLine("    <title>PayU Payment with Split</title>");
        formHtml.AppendLine("</head>");
        formHtml.AppendLine("<body>");
        formHtml.AppendLine("    <form action=\"https://test.payu.in/_payment\" method=\"post\" id=\"payuForm\" name=\"payuForm\">");
        
        foreach (var item in formData)
        {
            formHtml.AppendLine($"        <input type=\"hidden\" name=\"{HttpUtility.HtmlEncode(item.Key)}\" value=\"{HttpUtility.HtmlEncode(item.Value)}\">");
        }
        
        formHtml.AppendLine("        <input type=\"submit\" value=\"Proceed to Payment\">");
        formHtml.AppendLine("    </form>");
        formHtml.AppendLine("    <script>");
        formHtml.AppendLine("        // Uncomment to auto-submit form");
        formHtml.AppendLine("        // document.getElementById(\"payuForm\").submit();");
        formHtml.AppendLine("    </script>");
        formHtml.AppendLine("</body>");
        formHtml.AppendLine("</html>");
        
        return formHtml.ToString();
    }
}

```
```javascript
const crypto = require('crypto');
const axios = require('axios');
const querystring = require('querystring');

// Merchant details
const key = "Ax4j7J";
const salt = "t5atu4TyCvrJDPxAYrmfJfzd90kbXMfL";
const txnid = "payment-txnid-1";
const amount = "10";
const productinfo = "Product Info";
const firstname = "Payu-Admin";
const email = "test@example.com";
const phone = "1234567890";
const pg = "CC";
const bankcode = "VISA";
const ccnum = "4111111111111111";
const ccname = "Test User";
const ccvv = "123";
const ccexpmon = "12";
const ccexpyr = "2028";
const surl = "https://example.com/success";
const furl = "https://example.com/failure";

// Split request JSON
const splitRequestObj = {
  type: "absolute",
  splitInfo: {
    P41sCY: {
      aggregatorSubTxnId: "0e7411799c9f0e96620c11",
      aggregatorSubAmt: "3",
      aggregatorCharges: "2"
    },
    P41sCK: {
      aggregatorSubTxnId: "0e7411799c9f0e96620c22",
      aggregatorSubAmt: "5"
    }
  }
};

const splitRequest = JSON.stringify(splitRequestObj);

// Generate hash
const hashString = `${key}|${txnid}|${amount}|${productinfo}|${firstname}|${email}|||||||||||${salt}|${splitRequest}`;
const hash = crypto.createHash('sha512').update(hashString).digest('hex');

// Create form data
const formData = {
  key,
  txnid,
  amount,
  productinfo,
  firstname,
  email,
  phone,
  pg,
  bankcode,
  ccnum,
  ccname,
  ccvv,
  ccexpmon,
  ccexpyr,
  surl,
  furl,
  splitRequest,
  hash
};

// Make the API request
async function makePaymentRequest() {
  try {
    const response = await axios.post(
      'https://test.payu.in/_payment',
      querystring.stringify(formData),
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }
    );
    
    console.log('Status Code:', response.status);
    console.log('Response:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error making request:', error.message);
    if (error.response) {
      console.error('Response status:', error.response.status);
      console.error('Response data:', error.response.data);
    }
    throw error;
  }
}

// Frontend form generation example
function generatePaymentForm() {
  let formHtml = `
  <!DOCTYPE html>
  <html>
  <head>
      <title>PayU Payment with Split</title>
  </head>
  <body>
      <form action="https://test.payu.in/_payment" method="post" name="payuForm" id="payuForm">
  `;
  
  // Add all form fields
  Object.entries(formData).forEach(([key, value]) => {
    formHtml += `        <input type="hidden" name="${key}" value="${value}">\n`;
  });
  
  formHtml += `
        <input type="submit" value="Proceed to Payment">
      </form>
      <script>
        // Uncomment to auto-submit form
        // document.getElementById("payuForm").submit();
      </script>
  </body>
  </html>
  `;
  
  return formHtml;
}

// Execute the payment request
makePaymentRequest()
  .then(data => console.log('Payment request successful'))
  .catch(err => console.error('Payment request failed'));

// To generate HTML form instead
// console.log(generatePaymentForm());

```
```java
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class PayUAbsoluteSplitRequest {
    public static void main(String[] args) throws Exception {
        // Merchant details
        String key = "Ax4j7J";
        String salt = "t5atu4TyCvrJDPxAYrmfJfzd90kbXMfL";
        String txnid = "payment-txnid-1";
        String amount = "10";
        String productinfo = "Product Info";
        String firstname = "Payu-Admin";
        String email = "test@example.com";
        String phone = "1234567890";
        String pg = "CC";
        String bankcode = "VISA";
        String ccnum = "4111111111111111";
        String ccname = "Test User";
        String ccvv = "123";
        String ccexpmon = "12";
        String ccexpyr = "2028";
        String surl = "https://example.com/success";
        String furl = "https://example.com/failure";

        // Split request JSON
        String splitRequest = "{"
            + "\"type\":\"absolute\","
            + "\"splitInfo\":{"
            + "\"P41sCY\":{"
            + "\"aggregatorSubTxnId\":\"0e7411799c9f0e96620c11\","
            + "\"aggregatorSubAmt\":\"3\","
            + "\"aggregatorCharges\":\"2\""
            + "},"
            + "\"P41sCK\":{"
            + "\"aggregatorSubTxnId\":\"0e7411799c9f0e96620c22\","
            + "\"aggregatorSubAmt\":\"5\""
            + "}"
            + "}"
            + "}";

        // Generate hash
        String hashString = key + "|" + txnid + "|" + amount + "|" + productinfo + "|" +
                           firstname + "|" + email + "|||||||||||" + salt + "|" + splitRequest;
        
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] digest = md.digest(hashString.getBytes(StandardCharsets.UTF_8));
        
        StringBuilder hexString = new StringBuilder();
        for (byte b : digest) {
            String hex = Integer.toHexString(0xff & b);
            if (hex.length() == 1) hexString.append('0');
            hexString.append(hex);
        }
        String hash = hexString.toString();

        // Create form parameters
        Map<String, String> formParams = new HashMap<>();
        formParams.put("key", key);
        formParams.put("txnid", txnid);
        formParams.put("amount", amount);
        formParams.put("productinfo", productinfo);
        formParams.put("firstname", firstname);
        formParams.put("email", email);
        formParams.put("phone", phone);
        formParams.put("pg", pg);
        formParams.put("bankcode", bankcode);
        formParams.put("ccnum", ccnum);
        formParams.put("ccname", ccname);
        formParams.put("ccvv", ccvv);
        formParams.put("ccexpmon", ccexpmon);
        formParams.put("ccexpyr", ccexpyr);
        formParams.put("surl", surl);
        formParams.put("furl", furl);
        formParams.put("splitRequest", splitRequest);
        formParams.put("hash", hash);

        // Convert parameters to form-urlencoded format
        String formData = formParams.entrySet()
            .stream()
            .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "=" + 
                     URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
            .collect(Collectors.joining("&"));

        // Create HTTP client and request
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://test.payu.in/_payment"))
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formData))
            .build();

        // Send request and get response
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Response Status: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}

```

## Step 3: Handle the Response

After payment completion, PayU redirects to your success or failure URL with transaction details:

**Response Parameters**:

| Parameter                 | Description                                |
| ------------------------- | ------------------------------------------ |
| `status`                  | Payment status (success, failure, pending) |
| `txnid`                   | Transaction ID sent in the request         |
| `amount`                  | Transaction amount                         |
| `mihpayid`                | PayU payment ID                            |
| `splitInfo.splitStatus`   | Status of the split operation              |
| `splitInfo.splitSegments` | Array of split details                     |

**Example Response**:

```json
{
  "status": "success",
  "txnid": "payment-txnid-1",
  "amount": "10.00",
  "mihpayid": "403993715519672950",
  "error_code": "E000",
  "splitInfo": {
    "splitStatus": "success",
    "splitSegments": [
      {
        "merchantKey": "P41sCY",
        "amount": 3,
        "txnId": "0e7411799c9f0e96620c11"
      },
      {
        "merchantKey": "P41sCK",
        "amount": 5,
        "txnId": "0e7411799c9f0e96620c22"
      }
    ]
  }
}

```

## Step 4: Check the Transaction Info

Always verify the transaction info using the Get Aggregator/Parent Transaction Info API to ensure data integrity. For more information, refer to [Get Aggregator/Parent Transaction Info API](ref:get_aggregator_parent_transaction_info_api).

**Sample request**

```curl
curl -X POST "https://info.payu.in/merchant/postservice?form=2" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=Ax4j7J" \
  -d "command=get_aggregator_transactions" \
  -d "var1=2024-01-15 10:00" \
  -d "var2=2024-01-15 23:59" \
  -d "var3=1" \
  -d "var4=100" \
  -d "var5=1" \
  -d "hash=586e3379b3d9f90682329cf7efd27273aeb290936d9edf98686370bc59fdc67b8c0a15c9b6d5c48a24f66a8834b4b75e7e1a9c8d2e3f4a5b6c7d8e9f0a1b2c3d4e5"

```
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.security.MessageDigest;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;
import java.net.URLEncoder;

public class PayUGetAggregatorTransactionInfo {
    public static void main(String[] args) throws Exception {
        // API parameters
        String key = "Ax4j7J";
        String salt = "t5atu4TyCvrJDPxAYrmfJfzd90kbXMfL";
        String command = "get_aggregator_transactions";
        String startDate = "2024-01-15 10:00"; // var1
        String endDate = "2024-01-15 23:59";   // var2
        String pageNumber = "1";               // var3
        String pageLimit = "100";              // var4
        String splitFlag = "1";                // var5 (1 = split created, 0 = split not created)

        // Generate hash: sha512(key|command|var1|salt)
        String hashString = key + "|" + command + "|" + startDate + "|" + salt;
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] digest = md.digest(hashString.getBytes(StandardCharsets.UTF_8));
        
        StringBuilder hexString = new StringBuilder();
        for (byte b : digest) {
            String hex = Integer.toHexString(0xff & b);
            if (hex.length() == 1) hexString.append('0');
            hexString.append(hex);
        }
        String hash = hexString.toString();

        // Create form parameters
        Map<String, String> formParams = new HashMap<>();
        formParams.put("key", key);
        formParams.put("command", command);
        formParams.put("var1", startDate);
        formParams.put("var2", endDate);
        formParams.put("var3", pageNumber);
        formParams.put("var4", pageLimit);
        formParams.put("var5", splitFlag);
        formParams.put("hash", hash);

        // Convert to form-urlencoded format
        String formData = formParams.entrySet()
            .stream()
            .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "=" + 
                     URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
            .collect(Collectors.joining("&"));

        // Create HTTP client and request
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://info.payu.in/merchant/postservice?form=2"))
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formData))
            .build();

        // Send request and get response
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Response Status: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}

```
```php
<?php
// API parameters
$key = "Ax4j7J";
$salt = "t5atu4TyCvrJDPxAYrmfJfzd90kbXMfL";
$command = "get_aggregator_transactions";
$startDate = "2024-01-15 10:00"; // var1
$endDate = "2024-01-15 23:59";   // var2
$pageNumber = "1";               // var3
$pageLimit = "100";              // var4
$splitFlag = "1";                // var5 (1 = split created, 0 = split not created)

// Generate hash: sha512(key|command|var1|salt)
$hashString = "{$key}|{$command}|{$startDate}|{$salt}";
$hash = hash("sha512", $hashString);

// Create form data
$postData = [
    'key' => $key,
    'command' => $command,
    'var1' => $startDate,
    'var2' => $endDate,
    'var3' => $pageNumber,
    'var4' => $pageLimit,
    'var5' => $splitFlag,
    'hash' => $hash
];

// Initialize cURL session
$ch = curl_init("https://info.payu.in/merchant/postservice?form=2");
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/x-www-form-urlencoded'
]);

// Execute request and get response
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

// Parse and display response
echo "HTTP Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";

// Parse JSON response
$responseData = json_decode($response, true);
if ($responseData && $responseData['status'] == 1) {
    echo "Transaction fetch successful!\n";
    echo "Total transactions: " . count($responseData['Transaction_details']) . "\n";
} else {
    echo "Error: " . ($responseData['msg'] ?? 'Unknown error') . "\n";
}
?>

```
```javascript
const crypto = require('crypto');
const axios = require('axios');
const querystring = require('querystring');

// API parameters
const key = "Ax4j7J";
const salt = "t5atu4TyCvrJDPxAYrmfJfzd90kbXMfL";
const command = "get_aggregator_transactions";
const startDate = "2024-01-15 10:00"; // var1
const endDate = "2024-01-15 23:59";   // var2
const pageNumber = "1";               // var3
const pageLimit = "100";              // var4
const splitFlag = "1";                // var5 (1 = split created, 0 = split not created)

// Generate hash: sha512(key|command|var1|salt)
const hashString = `${key}|${command}|${startDate}|${salt}`;
const hash = crypto.createHash('sha512').update(hashString).digest('hex');

// Create form data
const formData = {
  key,
  command,
  var1: startDate,
  var2: endDate,
  var3: pageNumber,
  var4: pageLimit,
  var5: splitFlag,
  hash
};

// Make the API request
async function getAggregatorTransactionInfo() {
  try {
    const response = await axios.post(
      'https://info.payu.in/merchant/postservice?form=2',
      querystring.stringify(formData),
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }
    );
    
    console.log('Status Code:', response.status);
    console.log('Response:', JSON.stringify(response.data, null, 2));
    
    if (response.data.status === 1) {
      console.log('Transaction fetch successful!');
      console.log('Total transactions:', response.data.Transaction_details.length);
      
      // Display transaction details
      response.data.Transaction_details.forEach((transaction, index) => {
        console.log(`\nTransaction ${index + 1}:`);
        console.log(`  ID: ${transaction.id}`);
        console.log(`  Status: ${transaction.status}`);
        console.log(`  Amount: ${transaction.amount}`);
        console.log(`  TxnID: ${transaction.txnid}`);
        console.log(`  Is Parent: ${transaction.is_parent_transaction}`);
        
        if (transaction.splitInfo && transaction.splitInfo.length > 0) {
          console.log(`  Split Info:`);
          transaction.splitInfo.forEach((split, splitIndex) => {
            console.log(`    Split ${splitIndex + 1}: ${split.amount} to ${split.key}`);
          });
        }
      });
    } else {
      console.log('Error:', response.data.msg);
    }
    
    return response.data;
  } catch (error) {
    console.error('Error making request:', error.message);
    if (error.response) {
      console.error('Response status:', error.response.status);
      console.error('Response data:', error.response.data);
    }
    throw error;
  }
}

// Execute the request
getAggregatorTransactionInfo()
  .then(data => console.log('API call successful'))
  .catch(err => console.error('API call failed'));

```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class PayUGetAggregatorTransactionInfo
{
    static async Task Main(string[] args)
    {
        // API parameters
        string key = "Ax4j7J";
        string salt = "t5atu4TyCvrJDPxAYrmfJfzd90kbXMfL";
        string command = "get_aggregator_transactions";
        string startDate = "2024-01-15 10:00"; // var1
        string endDate = "2024-01-15 23:59";   // var2
        string pageNumber = "1";               // var3
        string pageLimit = "100";              // var4
        string splitFlag = "1";                // var5 (1 = split created, 0 = split not created)

        // Generate hash: sha512(key|command|var1|salt)
        string hashString = $"{key}|{command}|{startDate}|{salt}";
        string hash = ComputeSHA512Hash(hashString);

        // Create form data
        var formData = new Dictionary<string, string>
        {
            ["key"] = key,
            ["command"] = command,
            ["var1"] = startDate,
            ["var2"] = endDate,
            ["var3"] = pageNumber,
            ["var4"] = pageLimit,
            ["var5"] = splitFlag,
            ["hash"] = hash
        };

        await SendRequest(formData);
    }

    static string ComputeSHA512Hash(string input)
    {
        using (SHA512 sha512 = SHA512.Create())
        {
            byte[] inputBytes = Encoding.UTF8.GetBytes(input);
            byte[] hashBytes = sha512.ComputeHash(inputBytes);

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < hashBytes.Length; i++)
            {
                sb.Append(hashBytes[i].ToString("x2"));
            }
            return sb.ToString();
        }
    }

    static async Task SendRequest(Dictionary<string, string> formData)
    {
        try
        {
            using (HttpClient client = new HttpClient())
            {
                var content = new FormUrlEncodedContent(formData);

                HttpResponseMessage response = await client.PostAsync(
                    "https://info.payu.in/merchant/postservice?form=2", 
                    content
                );
                
                string responseContent = await response.Content.ReadAsStringAsync();
                
                Console.WriteLine($"Status Code: {response.StatusCode}");
                Console.WriteLine($"Response: {responseContent}");

                // Parse JSON response
                try
                {
                    var jsonDoc = JsonDocument.Parse(responseContent);
                    var root = jsonDoc.RootElement;
                    
                    if (root.TryGetProperty("status", out var status) && status.GetInt32() == 1)
                    {
                        Console.WriteLine("Transaction fetch successful!");
                        
                        if (root.TryGetProperty("Transaction_details", out var transactions))
                        {
                            Console.WriteLine($"Total transactions: {transactions.GetArrayLength()}");
                        }
                    }
                    else
                    {
                        if (root.TryGetProperty("msg", out var msg))
                        {
                            Console.WriteLine($"Error: {msg.GetString()}");
                        }
                    }
                }
                catch (JsonException ex)
                {
                    Console.WriteLine($"JSON parsing error: {ex.Message}");
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

**Sample response**

```
{
  "status": 1,
  "msg": "Transaction Fetched Successfully",
  "Transaction_details": [
    {
      "id": "412345678912384148",
      "status": "captured",
      "key": "Ax4j7J",
      "merchantname": "Aggregator-Parent",
      "txnid": "payment-txnid-1",
      "base_id": null,
      "firstname": "Payu-Admin",
      "lastname": "",
      "addedon": "2024-01-15 10:11:08",
      "bank_name": "Credit Cards",
      "payment_gateway": "AxisCYBER",
      "phone": "1234567890",
      "email": "test@example.com",
      "transaction_fee": "10.00",
      "amount": "10.00",
      "discount": "0.00",
      "additional_charges": "0.00",
      "productinfo": "Product Info",
      "error_code": "E000",
      "bank_ref_no": "5192296867061049177385",
      "ibibo_code": "CC",
      "mode": "CC",
      "is_parent_transaction": true,
      "splitInfo": [
        {
          "id": "412345678912384152",
          "status": "captured",
          "merchantId": "39032915",
          "key": "P41sCY",
          "txnid": "0e7411799c9f0e96620c11",
          "transaction_fee": "3.00",
          "amount": "3.00",
          "aggregatorCharges": "2.00"
        },
        {
          "id": "412345678912384153",
          "status": "captured",
          "merchantId": "39032916",
          "key": "P41sCK",
          "txnid": "0e7411799c9f0e96620c22",
          "transaction_fee": "5.00",
          "amount": "5.00"
        }
      ]
    }
  ]
}

```

## Security Considerations

### Hash Validation

Always validate the hash received in the response to ensure data integrity:

```php
<?php
$key = $_POST['key'];
$txnid = $_POST['txnid'];
$amount = $_POST['amount'];
$productinfo = $_POST['productinfo'];
$firstname = $_POST['firstname'];
$email = $_POST['email'];
$salt = "YOUR_MERCHANT_SALT";
$status = $_POST['status'];
$resphash = $_POST['hash'];

// Calculate hash
$hashString = "$salt|$status|||||||||$email|$firstname|$productinfo|$amount|$txnid|$key";
$calculatedHash = hash("sha512", $hashString);

if ($calculatedHash == $resphash) {
    // Hash is valid, proceed with order processing
    if ($status == "success") {
        // Payment successful
        // Update order status and process splits
    } else {
        // Payment failed
        // Handle failure
    }
} else {
    // Hash validation failed
    // Possible tampering detected
}
?>
```

### Split Amount Validation

Always ensure that the sum of all split amounts equals the total transaction amount:

```javascript
function validateSplitAmounts(splitInfo, totalAmount) {
    let sum = 0;
    
    // Calculate total from split amounts
    for (const merchantKey in splitInfo) {
        const merchantInfo = splitInfo[merchantKey];
        sum += parseFloat(merchantInfo.aggregatorSubAmt);
        
        if (merchantInfo.aggregatorCharges) {
            sum += parseFloat(merchantInfo.aggregatorCharges);
        }
    }
    
    // Compare with total amount
    return Math.abs(sum - parseFloat(totalAmount)) < 0.01;
}
```

## Error Handling

### Common Error Codes

| Error Code | Description                 | Resolution                            |
| ---------- | --------------------------- | ------------------------------------- |
| `E000`     | No Error                    | Transaction successful                |
| `E1001`    | Invalid hash                | Check hash calculation                |
| `E1002`    | Invalid parameters          | Verify all required parameters        |
| `E1003`    | Invalid merchant            | Verify merchant key                   |
| `E1004`    | Transaction not found       | Verify transaction ID                 |
| `E1007`    | Invalid split configuration | Check split amounts and merchant keys |

### Handling Split Failures

Even if the main payment succeeds, the split operation might fail. Always check the `splitInfo.splitStatus` field in the response:

```javascript
function handleResponse(response) {
    if (response.status === "success") {
        if (response.splitInfo && response.splitInfo.splitStatus === "success") {
            // Both payment and split successful
            console.log("Payment and split successful");
        } else {
            // Payment successful but split failed
            console.log("Payment successful but split failed");
            // Log split failure details
            console.log("Split status:", response.splitInfo?.splitStatus);
            console.log("Split errors:", response.splitInfo?.errors);
        }
    } else {
        // Payment failed
        console.log("Payment failed:", response.error_Message);
    }
}
```

## Additional Resources

* [PayU Developer Documentation](https://docs.payu.in/)
* [Split Settlements API Reference](https://docs.payu.in/docs/api-integration-for-split-settlements)
* [Absolute Split During Transaction](https://docs.payu.in/reference/absolute-split-during-transaction/)
* [Payment Verification API](https://docs.payu.in/reference/get-transaction-details-api)
* [Error Codes Reference](https://docs.payu.in/docs/error-codes)

## Support

For technical support and integration assistance:

* **Email**: [integration@payu.in](mailto:integration@payu.in)
* **Documentation**: [docs.payu.in](https://docs.payu.in)
* **Developer Community**: [PayU Developer Forum](https://community.payu.in)

***

**Note**: This integration guide provides a comprehensive overview of implementing Absolute Split During Transaction with PayU. Always refer to the latest API documentation for the most up-to-date information and endpoints.