---
title: Apple Pay
deprecated: false
hidden: true
metadata:
  robots: index
---
Use the Collect Payment (**_payment**) API to initiate an Apple Pay payment transaction. This is the primary endpoint to collect payments using Apple Pay.

**Endpoint**

| Environment | URL                               |
| :---------- | :-------------------------------- |
| Test        | `https://test.payu.in/_payment`   |
| Production  | `https://secure.payu.in/_payment` |

HTTP Method: **POST**

## Request Parameters

| Parameter                    | Description                                                                                                                                                                     | Example                                                      |
| :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------- |
| key<br />`mandatory`         | `String` - This parameter contains the merchant key provided by PayU during onboarding.                                                                                         | JP***g                                                       |
| txnid<br />`mandatory`       | `String` - This parameter contains a unique transaction ID. You can generate this ID or use the PayU API to generate it. The maximum length of this parameter is 25 characters. | txn_applepay_001                                             |
| amount<br />`mandatory`      | `String` - This parameter contains the payment amount.                                                                                                                          | 100.00                                                       |
| productinfo<br />`mandatory` | `String` - This parameter contains a brief description of the product or service.                                                                                               | iPhone Case                                                  |
| firstname<br />`mandatory`   | `String` - This parameter contains the first name of the customer.                                                                                                              | John                                                         |
| email<br />`mandatory`       | `String` - This parameter contains the email address of the customer.                                                                                                           | [john@example.com](mailto:john@example.com)                  |
| phone<br />`mandatory`       | `String` - This parameter contains the phone number of the customer.                                                                                                            | 9876543210                                                   |
| pg<br />`mandatory`          | `String` - This parameter specifies the payment category. For Apple Pay integration, the value must be `APPLEPAY`.                                                              | APPLEPAY                                                     |
| bankcode<br />`mandatory`    | `String` - This parameter specifies the payment option. For Apple Pay integration, the value must be `APPLEPAY`.                                                                | APPLEPAY                                                     |
| surl<br />`mandatory`        | `String` - This parameter contains the Success URL. PayU will redirect the customer to this URL after a successful payment.                                                     | [https://yoursite.com/success](https://yoursite.com/success) |
| furl<br />`mandatory`        | `String` - This parameter contains the Failure URL. PayU will redirect the customer to this URL after a failed payment.                                                         | [https://yoursite.com/failure](https://yoursite.com/failure) |
| hash<br />`mandatory`        | `String` - This parameter contains the hash value calculated using SHA-512 algorithm. Hash logic ensures the integrity of the transaction data.                                 | See hash generation                                          |
| lastname<br />`optional`     | `String` - This parameter contains the last name of the customer.                                                                                                               | Doe                                                          |
| address1<br />`optional`     | `String` - This parameter contains the first line of the billing address.                                                                                                       | 123 Main St                                                  |
| address2<br />`optional`     | `String` - This parameter contains the second line of the billing address.                                                                                                      | Apt 4B                                                       |
| city<br />`optional`         | `String` - This parameter contains the city of the billing address.                                                                                                             | Mumbai                                                       |
| state<br />`optional`        | `String` - This parameter contains the state of the billing address.                                                                                                            | Maharashtra                                                  |
| country<br />`optional`      | `String` - This parameter contains the country of the billing address.                                                                                                          | India                                                        |
| zipcode<br />`optional`      | `String` - This parameter contains the ZIP/postal code of the billing address.                                                                                                  | 400001                                                       |
| udf1<br />`optional`         | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                              |
| udf2<br />`optional`         | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                              |
| udf3<br />`optional`         | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                              |
| udf4<br />`optional`         | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                              |
| udf5<br />`optional`         | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                              |


## Hash Generation

Generate the hash using the following formula:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

## Sample Request

```bash
curl -X POST \
  'https://test.payu.in/_payment' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'key=JP***g' \
  -d 'txnid=txn_applepay_001' \
  -d 'amount=100.00' \
  -d 'firstname=John' \
  -d 'email=john@example.com' \
  -d 'phone=9876543210' \
  -d 'productinfo=iPhone Case' \
  -d 'pg=APPLEPAY' \
  -d 'bankcode=APPLEPAY' \
  -d 'surl=https://yoursite.com/success' \
  -d 'furl=https://yoursite.com/failure' \
  -d 'hash=<generated_hash>'
```
```python
import requests

url = "https://test.payu.in/_payment"

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'key': 'JP***g',
    'txnid': 'txn_applepay_001',
    'amount': '100.00',
    'firstname': 'John',
    'email': 'john@example.com',
    'phone': '9876543210',
    'productinfo': 'iPhone Case',
    'pg': 'APPLEPAY',
    'bankcode': 'APPLEPAY',
    'surl': 'https://yoursite.com/success',
    'furl': 'https://yoursite.com/failure',
    'hash': '<generated_hash>'
}

try:
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
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://test.payu.in/_payment";
            
            var formParams = new List<KeyValuePair<string, string>>
            {
                new KeyValuePair<string, string>("key", "JP***g"),
                new KeyValuePair<string, string>("txnid", "txn_applepay_001"),
                new KeyValuePair<string, string>("amount", "100.00"),
                new KeyValuePair<string, string>("firstname", "John"),
                new KeyValuePair<string, string>("email", "john@example.com"),
                new KeyValuePair<string, string>("phone", "9876543210"),
                new KeyValuePair<string, string>("productinfo", "iPhone Case"),
                new KeyValuePair<string, string>("pg", "APPLEPAY"),
                new KeyValuePair<string, string>("bankcode", "APPLEPAY"),
                new KeyValuePair<string, string>("surl", "https://yoursite.com/success"),
                new KeyValuePair<string, string>("furl", "https://yoursite.com/failure"),
                new KeyValuePair<string, string>("hash", "<generated_hash>")
            };

            var formContent = new FormUrlEncodedContent(formParams);
            client.DefaultRequestHeaders.Add("Accept", "application/json");

            HttpResponseMessage response = await client.PostAsync(url, formContent);
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
async function initiateApplePayPayment() {
    const url = 'https://test.payu.in/_payment';
    
    const formData = new URLSearchParams();
    formData.append('key', 'JP***g');
    formData.append('txnid', 'txn_applepay_001');
    formData.append('amount', '100.00');
    formData.append('firstname', 'John');
    formData.append('email', 'john@example.com');
    formData.append('phone', '9876543210');
    formData.append('productinfo', 'iPhone Case');
    formData.append('pg', 'APPLEPAY');
    formData.append('bankcode', 'APPLEPAY');
    formData.append('surl', 'https://yoursite.com/success');
    formData.append('furl', 'https://yoursite.com/failure');
    formData.append('hash', '<generated_hash>');
    
    const requestOptions = {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData
    };
    
    try {
        const response = await fetch(url, requestOptions);
        const responseText = await response.text();
        
        console.log(`Status: ${response.status}`);
        console.log(`Response: ${responseText}`);
        
        return responseText;
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

initiateApplePayPayment()
    .then(result => console.log('Payment initiated'))
    .catch(error => console.error('Failed:', error));
```
```java
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.StringJoiner;

public class InitiateApplePayPayment {

    public static void main(String[] args) {
        try {
            String url = "https://test.payu.in/_payment";

            Map<String, String> params = new HashMap<>();
            params.put("key", "JP***g");
            params.put("txnid", "txn_applepay_001");
            params.put("amount", "100.00");
            params.put("firstname", "John");
            params.put("email", "john@example.com");
            params.put("phone", "9876543210");
            params.put("productinfo", "iPhone Case");
            params.put("pg", "APPLEPAY");
            params.put("bankcode", "APPLEPAY");
            params.put("surl", "https://yoursite.com/success");
            params.put("furl", "https://yoursite.com/failure");
            params.put("hash", "<generated_hash>");

            StringJoiner sj = new StringJoiner("&");
            for (Map.Entry<String, String> entry : params.entrySet()) {
                sj.add(URLEncoder.encode(entry.getKey(), "UTF-8") + "="
                     + URLEncoder.encode(entry.getValue(), "UTF-8"));
            }
            byte[] postData = sj.toString().getBytes(StandardCharsets.UTF_8);

            URL apiUrl = new URL(url);
            HttpURLConnection conn = (HttpURLConnection) apiUrl.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Accept", "application/json");
            conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            conn.setRequestProperty("Content-Length", String.valueOf(postData.length));
            conn.setDoOutput(true);

            try (DataOutputStream dos = new DataOutputStream(conn.getOutputStream())) {
                dos.write(postData);
            }

            int responseCode = conn.getResponseCode();
            try (BufferedReader br = new BufferedReader(
                    new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }

                System.out.println("Status Code: " + responseCode);
                System.out.println("Response: " + response.toString());
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```
```php
<?php

$url = 'https://test.payu.in/_payment';

$postData = array(
    'key' => 'JP***g',
    'txnid' => 'txn_applepay_001',
    'amount' => '100.00',
    'firstname' => 'John',
    'email' => 'john@example.com',
    'phone' => '9876543210',
    'productinfo' => 'iPhone Case',
    'pg' => 'APPLEPAY',
    'bankcode' => 'APPLEPAY',
    'surl' => 'https://yoursite.com/success',
    'furl' => 'https://yoursite.com/failure',
    'hash' => '<generated_hash>'
);

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'Accept: application/json',
    'Content-Type: application/x-www-form-urlencoded'
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

| Parameter                         | Description                                                                                                                                | Example                                     |
| :-------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------ |
| mihpayid<br />`mandatory`         | `String` - This parameter contains the unique payment ID generated by PayU for this transaction.                                           | 403993715524045752                          |
| mode<br />`mandatory`             | `String` - This parameter contains the payment mode used for the transaction. For Apple Pay, this value is `APPLEPAY`.                     | APPLEPAY                                    |
| status<br />`mandatory`           | `String` - This parameter contains the status of the transaction. Possible values: `success`, `failure`, `pending`.                        | success                                     |
| unmappedstatus<br />`mandatory`   | `String` - This parameter contains the detailed status of the transaction. Possible values: `captured`, `auth`, `bounced`, `dropped`, etc. | captured                                    |
| key<br />`mandatory`              | `String` - This parameter contains the merchant key.                                                                                       | JP***g                                      |
| txnid<br />`mandatory`            | `String` - This parameter contains the transaction ID that was sent in the request.                                                        | txn_applepay_001                            |
| amount<br />`mandatory`           | `String` - This parameter contains the transaction amount.                                                                                 | 100.00                                      |
| discount<br />`optional`          | `String` - This parameter contains the discount amount applied to the transaction.                                                         | 0.00                                        |
| net_amount_debit<br />`mandatory` | `String` - This parameter contains the net amount debited from the customer.                                                               | 100                                         |
| addedon<br />`mandatory`          | `String` - This parameter contains the date and time when the transaction was added.                                                       | 2024-01-15 10:30:00                         |
| productinfo<br />`mandatory`      | `String` - This parameter contains the product information sent in the request.                                                            | iPhone Case                                 |
| firstname<br />`mandatory`        | `String` - This parameter contains the first name of the customer.                                                                         | John                                        |
| email<br />`mandatory`            | `String` - This parameter contains the email address of the customer.                                                                      | [john@example.com](mailto:john@example.com) |
| phone<br />`mandatory`            | `String` - This parameter contains the phone number of the customer.                                                                       | 9876543210                                  |
| hash<br />`mandatory`             | `String` - This parameter contains the hash value returned by PayU. You must validate this hash to ensure the response integrity.          | 1be7e6e97...                                |
| field9<br />`optional`            | `String` - This parameter contains additional information or error description returned by the bank or payment gateway.                    | Transaction Completed Successfully          |
| payment_source<br />`mandatory`   | `String` - This parameter contains the source of the payment.                                                                              | payu                                        |
| PG_TYPE<br />`mandatory`          | `String` - This parameter contains the type of payment gateway used. For Apple Pay, this value is `APPLEPAY-PG`.                           | APPLEPAY-PG                                 |
| bank_ref_num<br />`mandatory`     | `String` - This parameter contains the reference number returned by the bank for this transaction.                                         | 87d3b2a1-5a60...                            |
| bankcode<br />`mandatory`         | `String` - This parameter contains the bank code used for the transaction. For Apple Pay, this value is `APPLEPAY`.                        | APPLEPAY                                    |
| error<br />`mandatory`            | `String` - This parameter contains the error code. `E000` indicates no error.                                                              | E000                                        |
| error_Message<br />`mandatory`    | `String` - This parameter contains the description of the error.                                                                           | No Error                                    |

## Sample Response

```json
Array
(
    [mihpayid] => 403993715524045752
    [mode] => APPLEPAY
    [status] => success
    [unmappedstatus] => captured
    [key] => JP***g
    [txnid] => txn_applepay_001
    [amount] => 100.00
    [discount] => 0.00
    [net_amount_debit] => 100
    [addedon] => 2024-01-15 10:30:00
    [productinfo] => iPhone Case
    [firstname] => John
    [lastname] => 
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => 
    [zipcode] => 
    [email] => john@example.com
    [phone] => 9876543210
    [udf1] => 
    [udf2] => 
    [udf3] => 
    [udf4] => 
    [udf5] => 
    [udf6] => 
    [udf7] => 
    [udf8] => 
    [udf9] => 
    [udf10] => 
    [hash] => 1be7e6e97ab1ea9034b9a107e7cf9718308aa9637b4dbbd1a3343c91b0da02b34a40d00ac7267ebe81c20ea1129b931371c555d565bc6e11f470c3d2cf69b5a3
    [field1] => 
    [field2] => 
    [field3] => 
    [field4] => 
    [field5] => 
    [field6] => 
    [field7] => 
    [field8] => 
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [PG_TYPE] => APPLEPAY-PG
    [bank_ref_num] => 87d3b2a1-5a60-4169-8692-649f61923b3d
    [bankcode] => APPLEPAY
    [error] => E000
    [error_Message] => No Error
)
```