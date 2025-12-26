---
title: PayU Hosted Integration -Cross-Border Payments
deprecated: false
hidden: true
metadata:
  title: >-
    PayU Hosted Integration -Subscriptions Integration with Cross-Border
    Payments
  robots: index
---
---
title: PayU Hosted Integration -Cross-Border Payments
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: CB Subscriptions Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: CB Subscriptions Integration
  description: >-
    Learn how to integrate Cross-Border Subscriptions using PayU Hosted Checkout.
    This guide covers Payment Consent Transaction with Cross-Border specific UDF
    parameters and payment verification.
  keywords:
    - CB Subscriptions Integration
    - Cross-Border Subscriptions
    - Payment Consent Transaction CB
    - Verify Payment CB
  robots: index
next:
  description: ''
---

This section describes how to set up a Payment Consent or Registration transaction for Cross-Border Subscriptions using PayU Hosted Checkout integration with **_payment** API.

## Step 1: Payment Consent Transaction using PayU Hosted Checkout

For detailed information about the Payment Consent Transaction using PayU Hosted Checkout, refer to [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted).

<Callout icon="📘" theme="info">
  **Note**: For Cross-Border Payments, the UDF parameters (udf1, udf2, udf3, udf4, and udf5) have specific requirements as described in the Request parameters table below.
</Callout>

## Request parameters

In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

| Parameter                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                   |
| :--------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| key<br /><code>mandatory</code>                                                          | <code>varchar</code> This parameter is the unique Merchant Key provided by PayU for your merchant account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Your Test Key                                                                                                                                                             |
| txnid<br /><code>mandatory</code>                                                        | <code>varchar</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post a unique transaction ID for every new transaction. <code>Character limit</code>: 25<br /><strong>Note:</strong> Ensure this transaction ID hasn't been processed successfully before. | fd3e847h2                                                                                                                                                                 |
| amount<br /><code>mandatory</code>                                                       | <code>float</code> This parameter should contain the payment amount for the specific transaction.<br /><strong>Note:</strong> Typecast the amount to a float type. The amount can vary based on use cases:<br />• For Net Banking, 0 INR<br />• For Cards & UPI, a minimum of 1 INR (penny transactions)                                                                                                                                                                                                                                                                               | 1000                                                                                                                                                                      |
| productinfo<br /><code>mandatory</code>                                                  | <code>varchar</code> A brief product description. Short information about the product/service. Character limit: 100                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Time Magazine Subscription                                                                                                                                                |
| firstname<br /><code>mandatory</code>                                                    | <code>varchar</code> The customer's first name.<br />Character limit is 60.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Ashish                                                                                                                                                                    |
| lastname<br /><code>mandatory</code>                                                     | <code>varchar</code> The customer's last name.<br />Character limit is 60.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Kumar                                                                                                                                                                     |
| email<br /><code>mandatory</code>                                                        | <code>varchar</code> Contains the email of the customer; highly recommended accuracy as fraud detection relies on this. Character limit: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                           | [Ashish@test.com](mailto:Ashish@test.com)                                                                                                                                 |
| phone<br /><code>mandatory</code>                                                        | <code>varchar</code> Customer phone number for fraud detection and user tracking. Character limit: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 9843176540                                                                                                                                                                |
| address1<br /><code>mandatory</code>                                                     | <code>varchar</code> The customer's primary billing address line. This field is required for billing and fraud prevention purposes. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                              | 123 Main Street                                                                                                                                                           |
| city<br /><code>mandatory</code>                                                         | <code>varchar</code> The customer's billing city. This field is required for billing and fraud prevention purposes. Character limit: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                               | New York                                                                                                                                                                  |
| state<br /><code>mandatory</code>                                                        | <code>varchar</code> The customer's billing state or province. This field is required for billing and fraud prevention purposes. Character limit: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                  | NY                                                                                                                                                                        |
| country<br /><code>mandatory</code>                                                      | <code>varchar</code> The customer's billing country code. This field is required for billing and fraud prevention purposes. Use ISO 3166-1 alpha-2 country codes. Character limit: 2.                                                                                                                                                                                                                                                                                                                                                                                                  | US                                                                                                                                                                        |
| zipcode<br /><code>mandatory</code>                                                      | <code>varchar</code> The customer's billing postal/zip code. This field is required for billing and fraud prevention purposes. Character limit: 20.                                                                                                                                                                                                                                                                                                                                                                                                                                    | 10001                                                                                                                                                                     |
| surl<br /><code>mandatory</code>                                                         | <code>URL</code> The success URL to which PayU redirects after a successful transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [https://example.com/success](https://example.com/success)                                                                                                                |
| furl<br /><code>mandatory</code>                                                         | <code>URL</code> The failure URL to which PayU redirects after a failed transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | [https://example.com/failure](https://example.com/failure)                                                                                                                |
| api_version<br /><code>mandatory</code>                                                  | <code>int</code> Constant value to indicate the API version. Always pass as 7.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 7                                                                                                                                                                         |
| si<br /><code>mandatory</code>                                                           | <code>int</code> Signifies user consent for subscriptions. Must be 1 for a valid subscription setup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1                                                                                                                                                                         |
| free_trial<br /><code>optional</code>                                                    | <code>int</code> Enables free trials (adjusts transaction amount to INR 0.00 for Net Banking, INR 2.00 for others).                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 1                                                                                                                                                                         |
| si_details<br /><code>mandatory</code>                                                   | <code>JSON</code> Details required for subscription registration as per RBI guidelines. Must include billingAmount, billingCurrency, billingCycle, billingInterval, paymentStartDate, and paymentEndDate.                                                                                                                                                                                                                                                                                                                                                                              | \{"billingAmount": "100.00", "billingCurrency": "INR", "billingCycle": "MONTHLY", "billingInterval": 1, "paymentStartDate": "2019-09-01", "paymentEndDate": "2019-12-01"} |
| udf1<br /><code>conditional</code>                                                       | <code>String</code> If needed, contains the buyer's PAN. For UPI recurring, format is "Buyer's PAN\|\|Buyer's DOB". Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                              | AELPR1234E or AELPR1234E\|\|02-02-1980                                                                                                                                    |
| udf2<br /><code>optional</code>                                                          | <code>String</code> User-defined field for storing transaction-specific data. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Additional transaction data                                                                                                                                               |
| udf3<br />`optional but recommended for higher approval rate`                            | `String` Date of Birth (DOB) of buyer in DD-MM-YYYY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 02-02-1980                                                                                                                                                                |
| udf4<br />`mandatory for payment aggregators`                                            | `String` End merchant legal entity name. For UPI, this field should not be passed. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | XYZ Pvt. Ltd.                                                                                                                                                             |
| udf5<br />`mandatory for cross-border payments`                                          | `String` Contains invoice ID for the merchant. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | INV123456                                                                                                                                                                 |
| buyer_type_business<br />`optional in case of B2B transaction for cross-border payments` | `Binary` To be sent as "1" in case the buyer is a business. In case of individual buyers, it can be skipped. Default is "0".<br />**Note**: This will be included in hash if posted (covered in next section).                                                                                                                                                                                                                                                                                                                                                                         | 1                                                                                                                                                                         |
| udf_params<br />`optional`                                                               | `String JSON`<br /><br />UDF7 value to capture "Import or Export Code" of the buyer<br /><br />UDF8 value to capture Airway Bill Number / Consignment Number (in case of goods imports)                                                                                                                                                                                                                                                                                                                                                                                                | \{"udf7":"0100000029",<br />"udf8":"99953729071"}                                                                                                                         |
| hash<br />`mandatory`                                                                    | `String` Crucial security parameter using SHA512 hash encryption. Formula incorporates key, txnid, amount, productinfo, firstname, email, udf fields, si_details, and merchant salt.                                                                                                                                                                                                                                                                                                                                                                                                   | \<Generated Hash>                                                                                                                                                         |

<Accordion title="Hash Logic" icon="fa-info-circle">
  <PACB_Hashing />
</Accordion>

### Sample request

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&txnid=fM3O2HnkpJ8XEC&amount=100.00&firstname=PayU User&lastname=Kumar&email=test@gmail.com&phone=9876543210&productinfo=iPhone Subscription&address1=123 Main Street&city=New Delhi&state=Delhi&country=India&si=1&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&udf1=AELPR1234E&udf3=02-02-1980&udf4=XYZ Pvt. Ltd.&udf5=INV123456&buyer_type_business=1&udf_params={\"udf7\":\"0100000029\",\"udf8\":\"99953729071\"}&si_details={\"billingAmount\": \"100.00\",\"billingCurrency\": \"INR\",\"billingCycle\": \"MONTHLY\",\"billingInterval\": 1,\"paymentStartDate\": \"2022-09-01\",\"paymentEndDate\": \"2022-12-01\"}&hash=2ad878f64de47c7c1149ff554cd00ee44555a8512a1d2cff9690d6ea3c9d9de0bc44b0e77c61dd60a3c64ef970612a9b71761559aa202d2a278d29dc87b998c5"
```
```python
import requests

def payu_payment():
    url = "https://test.payu.in/_payment"
    
    form_data = {
        'key': 'JP***g',
        'txnid': 'fM3O2HnkpJ8XEC',
        'amount': '100.00',
        'firstname': 'PayU User',
        'lastname': 'Kumar',
        'email': 'test@gmail.com',
        'phone': '9876543210',
        'productinfo': 'iPhone Subscription',
        'address1': '123 Main Street',
        'city': 'New Delhi',
        'state': 'Delhi',
        'country': 'India',
        'si': '1',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'udf1': 'AELPR1234E',
        'udf3': '02-02-1980',
        'udf4': 'XYZ Pvt. Ltd.',
        'udf5': 'INV123456',
        'buyer_type_business': '1',
        'udf_params': '{"udf7":"0100000029","udf8":"99953729071"}',
        'si_details': '{"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2022-09-01","paymentEndDate": "2022-12-01"}',
        'hash': '2ad878f64de47c7c1149ff554cd00ee44555a8512a1d2cff9690d6ea3c9d9de0bc44b0e77c61dd60a3c64ef970612a9b71761559aa202d2a278d29dc87b998c5'
    }
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    try:
        response = requests.post(url, data=form_data, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

payu_payment()
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

public class PayUPayment
{
    private static readonly HttpClient client = new HttpClient();

    public static async Task Main(string[] args)
    {
        await ProcessPayment();
    }

    public static async Task ProcessPayment()
    {
        try
        {
            string url = "https://test.payu.in/_payment";
            
            var formParams = new List<KeyValuePair<string, string>>()
            {
                new KeyValuePair<string, string>("key", "JP***g"),
                new KeyValuePair<string, string>("txnid", "fM3O2HnkpJ8XEC"),
                new KeyValuePair<string, string>("amount", "100.00"),
                new KeyValuePair<string, string>("firstname", "PayU User"),
                new KeyValuePair<string, string>("lastname", "Kumar"),
                new KeyValuePair<string, string>("email", "test@gmail.com"),
                new KeyValuePair<string, string>("phone", "9876543210"),
                new KeyValuePair<string, string>("productinfo", "iPhone Subscription"),
                new KeyValuePair<string, string>("address1", "123 Main Street"),
                new KeyValuePair<string, string>("city", "New Delhi"),
                new KeyValuePair<string, string>("state", "Delhi"),
                new KeyValuePair<string, string>("country", "India"),
                new KeyValuePair<string, string>("si", "1"),
                new KeyValuePair<string, string>("surl", "https://apiplayground-response.herokuapp.com/"),
                new KeyValuePair<string, string>("furl", "https://apiplayground-response.herokuapp.com/"),
                new KeyValuePair<string, string>("udf1", "AELPR1234E"),
                new KeyValuePair<string, string>("udf3", "02-02-1980"),
                new KeyValuePair<string, string>("udf4", "XYZ Pvt. Ltd."),
                new KeyValuePair<string, string>("udf5", "INV123456"),
                new KeyValuePair<string, string>("buyer_type_business", "1"),
                new KeyValuePair<string, string>("udf_params", "{\"udf7\":\"0100000029\",\"udf8\":\"99953729071\"}"),
                new KeyValuePair<string, string>("si_details", "{\"billingAmount\": \"100.00\",\"billingCurrency\": \"INR\",\"billingCycle\": \"MONTHLY\",\"billingInterval\": 1,\"paymentStartDate\": \"2022-09-01\",\"paymentEndDate\": \"2022-12-01\"}"),
                new KeyValuePair<string, string>("hash", "2ad878f64de47c7c1149ff554cd00ee44555a8512a1d2cff9690d6ea3c9d9de0bc44b0e77c61dd60a3c64ef970612a9b71761559aa202d2a278d29dc87b998c5")
            };

            HttpContent formContent = new FormUrlEncodedContent(formParams);
            formContent.Headers.ContentType.MediaType = "application/x-www-form-urlencoded";

            HttpResponseMessage response = await client.PostAsync(url, formContent);
            string responseContent = await response.Content.ReadAsStringAsync();

            Console.WriteLine($"Status Code: {(int)response.StatusCode}");
            Console.WriteLine($"Response: {responseContent}");
        }
        catch (HttpRequestException ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
```
```javascript
async function processPayment() {
    const url = "https://test.payu.in/_payment";
    
    const formData = new URLSearchParams();
    formData.append('key', 'JP***g');
    formData.append('txnid', 'fM3O2HnkpJ8XEC');
    formData.append('amount', '100.00');
    formData.append('firstname', 'PayU User');
    formData.append('lastname', 'Kumar');
    formData.append('email', 'test@gmail.com');
    formData.append('phone', '9876543210');
    formData.append('productinfo', 'iPhone Subscription');
    formData.append('address1', '123 Main Street');
    formData.append('city', 'New Delhi');
    formData.append('state', 'Delhi');
    formData.append('country', 'India');
    formData.append('si', '1');
    formData.append('surl', 'https://apiplayground-response.herokuapp.com/');
    formData.append('furl', 'https://apiplayground-response.herokuapp.com/');
    formData.append('udf1', 'AELPR1234E');
    formData.append('udf3', '02-02-1980');
    formData.append('udf4', 'XYZ Pvt. Ltd.');
    formData.append('udf5', 'INV123456');
    formData.append('buyer_type_business', '1');
    formData.append('udf_params', '{"udf7":"0100000029","udf8":"99953729071"}');
    formData.append('si_details', '{"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2022-09-01","paymentEndDate": "2022-12-01"}');
    formData.append('hash', '2ad878f64de47c7c1149ff554cd00ee44555a8512a1d2cff9690d6ea3c9d9de0bc44b0e77c61dd60a3c64ef970612a9b71761559aa202d2a278d29dc87b998c5');

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: formData
        });

        const responseText = await response.text();
        console.log(`Status Code: ${response.status}`);
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

processPayment();
```
```java
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

public class PayUPayment {
    public static void main(String[] args) {
        processPayment();
    }

    public static void processPayment() {
        try {
            String apiUrl = "https://test.payu.in/_payment";
            URL url = new URL(apiUrl);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();

            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            connection.setDoOutput(true);

            Map<String, String> parameters = new HashMap<>();
            parameters.put("key", "JP***g");
            parameters.put("txnid", "fM3O2HnkpJ8XEC");
            parameters.put("amount", "100.00");
            parameters.put("firstname", "PayU User");
            parameters.put("lastname", "Kumar");
            parameters.put("email", "test@gmail.com");
            parameters.put("phone", "9876543210");
            parameters.put("productinfo", "iPhone Subscription");
            parameters.put("address1", "123 Main Street");
            parameters.put("city", "New Delhi");
            parameters.put("state", "Delhi");
            parameters.put("country", "India");
            parameters.put("si", "1");
            parameters.put("surl", "https://apiplayground-response.herokuapp.com/");
            parameters.put("furl", "https://apiplayground-response.herokuapp.com/");
            parameters.put("udf1", "AELPR1234E");
            parameters.put("udf3", "02-02-1980");
            parameters.put("udf4", "XYZ Pvt. Ltd.");
            parameters.put("udf5", "INV123456");
            parameters.put("buyer_type_business", "1");
            parameters.put("udf_params", "{\"udf7\":\"0100000029\",\"udf8\":\"99953729071\"}");
            parameters.put("si_details", "{\"billingAmount\": \"100.00\",\"billingCurrency\": \"INR\",\"billingCycle\": \"MONTHLY\",\"billingInterval\": 1,\"paymentStartDate\": \"2022-09-01\",\"paymentEndDate\": \"2022-12-01\"}");
            parameters.put("hash", "2ad878f64de47c7c1149ff554cd00ee44555a8512a1d2cff9690d6ea3c9d9de0bc44b0e77c61dd60a3c64ef970612a9b71761559aa202d2a278d29dc87b998c5");

            StringBuilder postData = new StringBuilder();
            for (Map.Entry<String, String> param : parameters.entrySet()) {
                if (postData.length() != 0) {
                    postData.append('&');
                }
                postData.append(URLEncoder.encode(param.getKey(), StandardCharsets.UTF_8));
                postData.append('=');
                postData.append(URLEncoder.encode(String.valueOf(param.getValue()), StandardCharsets.UTF_8));
            }

            byte[] postDataBytes = postData.toString().getBytes(StandardCharsets.UTF_8);
            connection.setRequestProperty("Content-Length", String.valueOf(postDataBytes.length));

            try (DataOutputStream wr = new DataOutputStream(connection.getOutputStream())) {
                wr.write(postDataBytes);
            }

            int responseCode = connection.getResponseCode();
            System.out.println("Status Code: " + responseCode);

            BufferedReader in = new BufferedReader(new InputStreamReader(
                responseCode >= 200 && responseCode < 300 ? 
                connection.getInputStream() : connection.getErrorStream()
            ));
            
            String inputLine;
            StringBuilder response = new StringBuilder();
            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();

            System.out.println("Response: " + response.toString());

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
function processPayment() {
    $url = "https://test.payu.in/_payment";
    
    $postData = array(
        'key' => 'JP***g',
        'txnid' => 'fM3O2HnkpJ8XEC',
        'amount' => '100.00',
        'firstname' => 'PayU User',
        'lastname' => 'Kumar',
        'email' => 'test@gmail.com',
        'phone' => '9876543210',
        'productinfo' => 'iPhone Subscription',
        'address1' => '123 Main Street',
        'city' => 'New Delhi',
        'state' => 'Delhi',
        'country' => 'India',
        'si' => '1',
        'surl' => 'https://apiplayground-response.herokuapp.com/',
        'furl' => 'https://apiplayground-response.herokuapp.com/',
        'udf1' => 'AELPR1234E',
        'udf3' => '02-02-1980',
        'udf4' => 'XYZ Pvt. Ltd.',
        'udf5' => 'INV123456',
        'buyer_type_business' => '1',
        'udf_params' => '{"udf7":"0100000029","udf8":"99953729071"}',
        'si_details' => '{"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2022-09-01","paymentEndDate": "2022-12-01"}',
        'hash' => '2ad878f64de47c7c1149ff554cd00ee44555a8512a1d2cff9690d6ea3c9d9de0bc44b0e77c61dd60a3c64ef970612a9b71761559aa202d2a278d29dc87b998c5'
    );

    $options = array(
        CURLOPT_URL => $url,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => http_build_query($postData),
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER => array(
            'Content-Type: application/x-www-form-urlencoded'
        ),
        CURLOPT_SSL_VERIFYPEER => false,
        CURLOPT_SSL_VERIFYHOST => false
    );

    $ch = curl_init();
    curl_setopt_array($ch, $options);

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    
    if ($response === false) {
        echo "Error: " . curl_error($ch) . "\n";
    } else {
        echo "Status Code: " . $httpCode . "\n";
        echo "Response: " . $response . "\n";
    }
    
    curl_close($ch);
}

processPayment();
?>
```

### Sample Response

The response URL returned from PayU is in the form URL format (application/x-www-form-urlencoded).

#### Parsed response

```
Array
(
    [mihpayid] => 403993715525331373
    [mode] => ENACH
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => oRWSUMU4XSQBZn
    [amount] => 100.00
    [discount] => 0.00
    [net_amount_debit] => 0
    [addedon] => 2022-02-03 19:06:55
    [productinfo] => iPhone Subscription
    [firstname] => PayU User
    [lastname] => 
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => 
    [zipcode] => 
    [email] => test@gmail.com
    [phone] => 9876543210
    [udf1] => AELPR1234E
    [udf2] => 
    [udf3] => 02-02-1980
    [udf4] => XYZ Pvt. Ltd.
    [udf5] => INV123456
    [hash] => f3f8e4088231b190930fc4b87d3f39397d1a1d02622ef4683a983244e1cd5158f39adbb67c3d87dcb4da25ae4a941ebbf55918e4575fa1c39677a774d02c0d2d
    [field1] => ENACH285259747472911093
    [field2] => 337026657857179355
    [field9] => Mandate successfully scheduled at bank end: Your payment is scheduled successfully
    [payment_source] => sist
    [PG_TYPE] => ENACH-PG
    [bank_ref_num] => 450699821592111537
    [bankcode] => ICICENCC
    [error] => E000
    [error_Message] => No Error
)
```

## Step 2: Verify the Payment

Upon receiving the response, PayU recommends performing a reconciliation step to validate all transaction details. You can verify your payments using either of the following methods:

<Verify_Payment_Tabs />

## Step 3: Recurring Payment Transaction

Use the **Recurring Payment Transaction** API to execute recurring payment transactions for customers who have already completed a successful mandate/registration transaction with Net Banking, UPI, or Cards. For detailed API reference, refer to [Recurring Payment Transaction API - PACB](ref:recurring-payment-transaction-api-pacb).

| Environment | URL                                                |
| :---------- | :------------------------------------------------- |
| Production  | `https://info.payu.in/merchant/postservice?form=2` |
| Test        | `https://test.payu.in/merchant/postservice?form=2` |

### Request Parameters

| Parameter                             | Description                                                                                  | Example                           |
| :------------------------------------ | :------------------------------------------------------------------------------------------- | :-------------------------------- |
| key <br /> <code>mandatory</code>     | <code>String</code> Merchant Key provided by PayU                                            | JPM7Fg                            |
| command <br /> <code>mandatory</code> | <code>String</code> API command. Must be `si_transaction`                                    | si_transaction                    |
| var1 <br /> <code>mandatory</code>    | <code>JSON Object</code> Transaction details object containing mandatory and optional fields | Refer to var1 Object Fields below |
| hash <br /> <code>mandatory</code>    | <code>String</code> SHA512 hash: `sha512(key\|command\|var1\|salt)`                          | 9f5faabedb...                     |

### var1 Object Fields

| Parameter                                                       | Description                                                                                                                                                               | Example                                             |
| :-------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------- |
| authpayuid <br /> <code>mandatory</code>                        | <code>String</code> The mihpayid returned in the payment response of the Registration/Consent transaction when transaction is successfully completed.                     | 6611192557                                          |
| amount <br /> <code>mandatory</code>                            | <code>String</code> The transaction amount which will be deducted from the customer's payment instrument.                                                                 | 10.00                                               |
| txnid <br /> <code>mandatory</code>                             | <code>String</code> Unique Transaction ID (Order ID) generated by the merchant for this recurring transaction.                                                            | REC15113506209                                      |
| firstname <br /> <code>mandatory</code>                         | <code>String</code> First name of the buyer/customer.                                                                                                                     | John                                                |
| lastname <br /> <code>mandatory</code>                          | <code>String</code> Last name of the buyer/customer.                                                                                                                      | Doe                                                 |
| address1 <br /> <code>mandatory</code>                          | <code>String</code> Address line 1 of the buyer.                                                                                                                          | 123 Main Street                                     |
| city <br /> <code>mandatory</code>                              | <code>String</code> City of the buyer.                                                                                                                                    | Mumbai                                              |
| state <br /> <code>mandatory</code>                             | <code>String</code> State of the buyer.                                                                                                                                   | Maharashtra                                         |
| country <br /> <code>mandatory</code>                           | <code>String</code> Country of the buyer. Allowed values: `IN` or `India` only.                                                                                           | IN                                                  |
| zipcode <br /> <code>mandatory</code>                           | <code>String</code> ZIP/PIN code of the buyer. Must be a valid 6-digit Indian PIN code.                                                                                   | 400001                                              |
| phone <br /> <code>optional</code>                              | <code>String</code> The phone number of the customer.                                                                                                                     | 9999999999                                          |
| email <br /> <code>optional</code>                              | <code>String</code> The email address of the customer.                                                                                                                    | [customer@example.com](mailto:customer@example.com) |
| invoiceDisplayNumber <br /> <code>mandatory for Cards SI</code> | <code>String</code> A unique display number by merchant for every subsequent invoice/recurring charge. This must be the same value passed during `pre_debit_si` API call. | 12345678910                                         |
| udf5 <br /> <code>mandatory</code>                              | <code>String</code> Invoice ID for every merchant. This field is mandatory during or after the transaction.                                                               | INV789012                                           |

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JPM7Fg&command=si_transaction&var1={
    \"authpayuid\": \"6611192557\",
    \"amount\": \"100.00\",
    \"txnid\": \"REC15113506209\",
    \"phone\": \"9999999999\",
    \"email\": \"customer@example.com\",
    \"firstname\": \"John\",
    \"lastname\": \"Doe\",
    \"address1\": \"123 Main Street\",
    \"city\": \"Mumbai\",
    \"state\": \"Maharashtra\",
    \"country\": \"IN\",
    \"zipcode\": \"400001\",
    \"invoiceDisplayNumber\": \"12345678910\",
    \"udf1\": \"ABCDE1234F\",
    \"udf2\": \"\",
    \"udf3\": \"15-08-1990\",
    \"udf4\": \"\",
    \"udf5\": \"INV789012\"
  }&hash=jbUS07Og8BToVZ..."
  ```
  ```python
  import requests

  url = "https://test.payu.in/merchant/postservice?form=2"

  payload = {
      "key": "JPM7Fg",
      "command": "si_transaction",
      "var1": '{"authpayuid":"6611192557","amount":"100.00","txnid":"REC15113506209","phone":"9999999999","email":"customer@example.com","firstname":"John","lastname":"Doe","address1":"123 Main Street","city":"Mumbai","state":"Maharashtra","country":"IN","zipcode":"400001","invoiceDisplayNumber":"12345678910","udf1":"ABCDE1234F","udf2":"","udf3":"15-08-1990","udf4":"","udf5":"INV789012"}',
      "hash": "jbUS07Og8BToVZ..."
  }

  headers = {
      "accept": "application/json",
      "Content-Type": "application/x-www-form-urlencoded"
  }

  response = requests.post(url, data=payload, headers=headers)
  print(response.json())
  ```
  ```csharp
  using System;
  using System.Net.Http;
  using System.Collections.Generic;
  using System.Threading.Tasks;

  class Program
  {
      static async Task Main()
      {
          using var client = new HttpClient();
          
          var content = new FormUrlEncodedContent(new[]
          {
              new KeyValuePair<string, string>("key", "JPM7Fg"),
              new KeyValuePair<string, string>("command", "si_transaction"),
              new KeyValuePair<string, string>("var1", "{\"authpayuid\":\"6611192557\",\"amount\":\"100.00\",\"txnid\":\"REC15113506209\",\"phone\":\"9999999999\",\"email\":\"customer@example.com\",\"firstname\":\"John\",\"lastname\":\"Doe\",\"address1\":\"123 Main Street\",\"city\":\"Mumbai\",\"state\":\"Maharashtra\",\"country\":\"IN\",\"zipcode\":\"400001\",\"invoiceDisplayNumber\":\"12345678910\",\"udf1\":\"ABCDE1234F\",\"udf2\":\"\",\"udf3\":\"15-08-1990\",\"udf4\":\"\",\"udf5\":\"INV789012\"}"),
              new KeyValuePair<string, string>("hash", "jbUS07Og8BToVZ...")
          });
          
          var response = await client.PostAsync("https://test.payu.in/merchant/postservice?form=2", content);
          var result = await response.Content.ReadAsStringAsync();
          Console.WriteLine(result);
      }
  }
  ```
  ```javascript
  const executeRecurringPayment = async () => {
      const url = "https://test.payu.in/merchant/postservice?form=2";
      
      const params = new URLSearchParams();
      params.append("key", "JPM7Fg");
      params.append("command", "si_transaction");
      params.append("var1", JSON.stringify({
          authpayuid: "6611192557",
          amount: "100.00",
          txnid: "REC15113506209",
          phone: "9999999999",
          email: "customer@example.com",
          firstname: "John",
          lastname: "Doe",
          address1: "123 Main Street",
          city: "Mumbai",
          state: "Maharashtra",
          country: "IN",
          zipcode: "400001",
          invoiceDisplayNumber: "12345678910",
          udf1: "ABCDE1234F",
          udf2: "",
          udf3: "15-08-1990",
          udf4: "",
          udf5: "INV789012"
      }));
      params.append("hash", "jbUS07Og8BToVZ...");
      
      const response = await fetch(url, {
          method: "POST",
          headers: {
              "accept": "application/json",
              "Content-Type": "application/x-www-form-urlencoded"
          },
          body: params
      });
      
      const data = await response.json();
      console.log(data);
  };

  executeRecurringPayment();
  ```
  ```java
  import java.io.*;
  import java.net.*;
  import java.nio.charset.StandardCharsets;

  public class RecurringPaymentTransaction {
      public static void main(String[] args) throws Exception {
          String url = "https://test.payu.in/merchant/postservice?form=2";
          
          String params = "key=JPM7Fg" +
              "&command=si_transaction" +
              "&var1=" + URLEncoder.encode("{\"authpayuid\":\"6611192557\",\"amount\":\"100.00\",\"txnid\":\"REC15113506209\",\"phone\":\"9999999999\",\"email\":\"customer@example.com\",\"firstname\":\"John\",\"lastname\":\"Doe\",\"address1\":\"123 Main Street\",\"city\":\"Mumbai\",\"state\":\"Maharashtra\",\"country\":\"IN\",\"zipcode\":\"400001\",\"invoiceDisplayNumber\":\"12345678910\",\"udf1\":\"ABCDE1234F\",\"udf2\":\"\",\"udf3\":\"15-08-1990\",\"udf4\":\"\",\"udf5\":\"INV789012\"}", StandardCharsets.UTF_8) +
              "&hash=jbUS07Og8BToVZ...";
          
          HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
          conn.setRequestMethod("POST");
          conn.setRequestProperty("accept", "application/json");
          conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
          conn.setDoOutput(true);
          
          try (OutputStream os = conn.getOutputStream()) {
              os.write(params.getBytes(StandardCharsets.UTF_8));
          }
          
          try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()))) {
              String line;
              while ((line = br.readLine()) != null) {
                  System.out.println(line);
              }
          }
      }
  }
  ```
  ```php
  <?php
  $url = "https://test.payu.in/merchant/postservice?form=2";

  $data = array(
      "key" => "JPM7Fg",
      "command" => "si_transaction",
      "var1" => json_encode(array(
          "authpayuid" => "6611192557",
          "amount" => "100.00",
          "txnid" => "REC15113506209",
          "phone" => "9999999999",
          "email" => "customer@example.com",
          "firstname" => "John",
          "lastname" => "Doe",
          "address1" => "123 Main Street",
          "city" => "Mumbai",
          "state" => "Maharashtra",
          "country" => "IN",
          "zipcode" => "400001",
          "invoiceDisplayNumber" => "12345678910",
          "udf1" => "ABCDE1234F",
          "udf2" => "",
          "udf3" => "15-08-1990",
          "udf4" => "",
          "udf5" => "INV789012"
      )),
      "hash" => "jbUS07Og8BToVZ..."
  );

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      "accept: application/json",
      "Content-Type: application/x-www-form-urlencoded"
  ));

  $response = curl_exec($ch);
  curl_close($ch);

  echo $response;
  ?>
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-check">
  **Success Response**

  ```json
  {
    "status": 1,
    "message": "Transaction Processed successfully",
    "details": {
      "REC15113506209": {
        "transactionid": "REC15113506209",
        "amount": "100.00",
        "payuid": "6611427463",
        "status": "captured",
        "field9": "Transaction Completed Successfully",
        "phone": "9999999999",
        "email": "customer@example.com",
        "udf1": "ABCDE1234F",
        "udf2": "",
        "udf3": "15-08-1990",
        "udf4": "",
        "udf5": "INV789012"
      }
    }
  }
  ```

  **Failure Responses**

  | Scenario                    | Response                                                                                                                                                            |
  | :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | Invalid Hash                | `{"status": 0, "msg": "Invalid Hash."}`                                                                                                                             |
  | Basic Authentication Failed | `{"status": 1, "message": "Transaction Processed successfully", "details": {"REC9812123123": {"status": "failed", "field9": "Basic authentication check failed"}}}` |
  | Invalid Country             | `{"status": 0, "message": "Invalid country. Only 'IN' or 'India' is allowed."}`                                                                                     |
  | Missing Mandatory Fields    | `{"status": 0, "message": "Missing mandatory field: firstname/lastname/address1/city/state/country/zipcode"}`                                                       |
</Accordion>

<Callout icon="📘" theme="info">
  **Transaction Status Values**

  | Status      | Description                                                                  |
  | :---------- | :--------------------------------------------------------------------------- |
  | captured    | Transaction successful                                                       |
  | pending     | Payment initiated with bank/NPCI. Final status will be notified via webhook. |
  | failed      | Transaction failed                                                           |
  | in-progress | Transaction is being processed                                               |
</Callout>

***

## Step 4: Pre-Debit SI Notification

Use the **Pre-Debit SI** API to send pre-debit notifications for upcoming recurring debits with parallel sequencing support. This notification must be sent before executing the recurring transaction for Cards SI. For detailed API reference, refer to [Pre-Debit SI API](ref:pre-debit-si-api-parallel-sequencing).

| Environment | URL                                                         |
| :---------- | :---------------------------------------------------------- |
| Test        | `https://test.info.payu.in/merchant/postservice.php?form=2` |
| Production  | `https://info.payu.in/merchant/postservice.php?form=2`      |

### Request Parameters

| Parameter                             | Description                                                            | Example               |
| :------------------------------------ | :--------------------------------------------------------------------- | :-------------------- |
| key <br /> <code>mandatory</code>     | <code>String</code> Your merchant key provided by PayU.                | JP***g                |
| command <br /> <code>mandatory</code> | <code>String</code> The API command name.                              | pre_debit_SI          |
| hash <br /> <code>mandatory</code>    | <code>String</code> The hash value generated using the hash logic.     | abc0ada2e12           |
| var1 <br /> <code>mandatory</code>    | <code>JSON String</code> JSON object containing the pre-debit details. | See var1 Object below |

### var1 Object Parameters

| Parameter                                         | Description                                                                            | Example         |
| :------------------------------------------------ | :------------------------------------------------------------------------------------- | :-------------- |
| authpayuid <br /> <code>mandatory</code>          | <code>String</code> The authorization PayU ID received during mandate creation.        | 999000000000826 |
| requestid <br /> <code>mandatory</code>           | <code>String</code> Unique request ID for tracking the pre-debit request.              | RCS0123459PD    |
| debitdate <br /> <code>mandatory</code>           | <code>String</code> The date when the debit will occur in YYYY-MM-DD format.           | 2024-11-22      |
| amount <br /> <code>mandatory</code>              | <code>String</code> The amount to be debited.                                          | 125             |
| invoiceDisplayNumber <br /> <code>optional</code> | <code>String</code> Invoice number to display to the customer.                         | 12345678910     |
| mandateSeqNo <br /> <code>optional</code>         | <code>Integer</code> Sequence number for parallel processing. Valid range: 2 to 11000. | 2               |

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl --location 'https://test.info.payu.in/merchant/postservice.php?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'command=pre_debit_SI' \
  --data-urlencode 'var1={"authpayuid":"999000000000826","requestid":"RCS0123459PD","debitdate":"2024-11-22","amount":"125","invoiceDisplayNumber":"12345678910","mandateSeqNo":2}' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'hash=abc0ada2e12'
  ```
  ```python
  import requests

  url = "https://test.info.payu.in/merchant/postservice.php?form=2"

  payload = {
      "command": "pre_debit_SI",
      "var1": '{"authpayuid":"999000000000826","requestid":"RCS0123459PD","debitdate":"2024-11-22","amount":"125","invoiceDisplayNumber":"12345678910","mandateSeqNo":2}',
      "key": "JP***g",
      "hash": "abc0ada2e12"
  }

  headers = {
      "Content-Type": "application/x-www-form-urlencoded"
  }

  response = requests.post(url, data=payload, headers=headers)
  print(response.json())
  ```
  ```csharp
  using System;
  using System.Net.Http;
  using System.Collections.Generic;
  using System.Threading.Tasks;

  class Program
  {
      static async Task Main()
      {
          using var client = new HttpClient();
          
          var content = new FormUrlEncodedContent(new[]
          {
              new KeyValuePair<string, string>("command", "pre_debit_SI"),
              new KeyValuePair<string, string>("var1", "{\"authpayuid\":\"999000000000826\",\"requestid\":\"RCS0123459PD\",\"debitdate\":\"2024-11-22\",\"amount\":\"125\",\"invoiceDisplayNumber\":\"12345678910\",\"mandateSeqNo\":2}"),
              new KeyValuePair<string, string>("key", "JP***g"),
              new KeyValuePair<string, string>("hash", "abc0ada2e12")
          });
          
          var response = await client.PostAsync("https://test.info.payu.in/merchant/postservice.php?form=2", content);
          var result = await response.Content.ReadAsStringAsync();
          Console.WriteLine(result);
      }
  }
  ```
  ```javascript
  const sendPreDebitRequest = async () => {
      const url = "https://test.info.payu.in/merchant/postservice.php?form=2";
      
      const params = new URLSearchParams();
      params.append("command", "pre_debit_SI");
      params.append("var1", JSON.stringify({
          authpayuid: "999000000000826",
          requestid: "RCS0123459PD",
          debitdate: "2024-11-22",
          amount: "125",
          invoiceDisplayNumber: "12345678910",
          mandateSeqNo: 2
      }));
      params.append("key", "JP***g");
      params.append("hash", "abc0ada2e12");
      
      const response = await fetch(url, {
          method: "POST",
          headers: {
              "Content-Type": "application/x-www-form-urlencoded"
          },
          body: params
      });
      
      const data = await response.json();
      console.log(data);
  };

  sendPreDebitRequest();
  ```
  ```java
  import java.io.*;
  import java.net.*;
  import java.nio.charset.StandardCharsets;

  public class PreDebitSI {
      public static void main(String[] args) throws Exception {
          String url = "https://test.info.payu.in/merchant/postservice.php?form=2";
          
          String params = "command=pre_debit_SI" +
              "&var1=" + URLEncoder.encode("{\"authpayuid\":\"999000000000826\",\"requestid\":\"RCS0123459PD\",\"debitdate\":\"2024-11-22\",\"amount\":\"125\",\"invoiceDisplayNumber\":\"12345678910\",\"mandateSeqNo\":2}", StandardCharsets.UTF_8) +
              "&key=JP***g" +
              "&hash=abc0ada2e12";
          
          HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
          conn.setRequestMethod("POST");
          conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
          conn.setDoOutput(true);
          
          try (OutputStream os = conn.getOutputStream()) {
              os.write(params.getBytes(StandardCharsets.UTF_8));
          }
          
          try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()))) {
              String line;
              while ((line = br.readLine()) != null) {
                  System.out.println(line);
              }
          }
      }
  }
  ```
  ```php
  <?php
  $url = "https://test.info.payu.in/merchant/postservice.php?form=2";

  $data = array(
      "command" => "pre_debit_SI",
      "var1" => json_encode(array(
          "authpayuid" => "999000000000826",
          "requestid" => "RCS0123459PD",
          "debitdate" => "2024-11-22",
          "amount" => "125",
          "invoiceDisplayNumber" => "12345678910",
          "mandateSeqNo" => 2
      )),
      "key" => "JP***g",
      "hash" => "abc0ada2e12"
  );

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array("Content-Type: application/x-www-form-urlencoded"));

  $response = curl_exec($ch);
  curl_close($ch);

  echo $response;
  ?>
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-check">
  **Success Response**

  ```json
  {
      "status": "1",
      "action": "MANDATE_PRE_DEBIT",
      "message": "Request Processed Successfully"
  }
  ```

  **Error Responses**

  | Scenario                              | Response                                                                                                                               |
  | :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------- |
  | Invalid mandateSeqNo                  | `{"status":"0","message":"Invalid value for mandateSeqNo","action":"MANDATE_PRE_DEBIT"}`                                               |
  | Pre-debit already sent for sequence   | `{"status":"E9254","action":"MANDATE_PRE_DEBIT","message":"Predebit notification already sent for the mandate sequence no. 2"}`        |
  | Execution already exists for sequence | `{"status":"E9256","action":"MANDATE_PRE_DEBIT","message":"Execution already sent for the mandate sequence no.:2"}`                    |
  | Debit date exceeds 30 days            | `{"status":"E9260","action":"MANDATE_PRE_DEBIT","message":"Predebit notification can only be sent for a maximum 30 days in advance."}` |
  | Pre-debit sent for past sequence      | `{"status":"E9263","action":"MANDATE_PRE_DEBIT","message":"Predebit for calculated sequence sent during incorrect period"}`            |
</Accordion>

### Response Parameters

| Parameter | Description                                                                                            | Example                        |
| :-------- | :----------------------------------------------------------------------------------------------------- | :----------------------------- |
| status    | <code>String</code> Status of the request. `1` indicates success, `0` or error code indicates failure. | 1                              |
| action    | <code>String</code> The action performed.                                                              | MANDATE_PRE_DEBIT              |
| message   | <code>String</code> Description of the response status.                                                | Request Processed Successfully |

## Step 5: Update Invoice ID [Conditional]

If the Invoice ID value was unavailable when posting the transaction at [Step 1](#step-1-make-payment-using-web-checkout-integration), it can be updated using the **UDF Update** API by posting it in the UDF5 parameter.

<GENERALAPIsEnvironment />

<Accordion title="Sample request other then UPI AutoPay" icon="fa-code">
  ```
    curl --location --globoff 'https://test.payu.in/merchant/postservice.php?form=2' \
    --form 'key="PRiQvJ"' \
    --form 'command="udf_update"' \
    --form 'var1="my_order_642"' \
    --form 'var2="AAAPZ1234C"' \
    --form 'var4="22/08/1972"' \
    --form 'var5="SellerName"' \
    --form 'var6="INV000000005"' \
    --form 'hash="{{hash}}"'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ### Success Scenario

  * If successfully updated for cards

  ```JSON
  {
      "status": "UDF values updated",
      "transaction_id": "my_order_64240",
      "udf1": "AAAPZ1234C",
      "udf2": "",
      "udf3": "22/08/1972",
      "udf4": "SellerName",
      "udf5": "INV000000005"
  }
  ```

  * If successfully updated for UPI autopay:

  ```JSON
  {
      "status": "UDF values updated",
      "transaction_id": "my_order_64240",
      "udf1": "AAAPZ1234C",
      "udf2": "",
      "udf3": "22/08/1972",
      "udf4": "SellerName",
      "udf5": "INV000000005"
  }
  ```

  ### Failure Scenarios

  * If the transaction ID is empty

  ```JSON
  ( 
  [status] => 0 
  [msg] => Parameter missing 
  ) 
  ```

  * If the transaction ID is invalid

  ```JSON
  ( 
  [status] => 0 
  [msg] => Invalid TXN ID 
  ) 
  ```

  * If Hash is invalid:

  ```JSON
  {
      "status": 0,
      "msg": "Invalid Hash."
  }
  ```

  * If the merchant is not enabled for UDF updates:

  ```JSON
  {
    "status": "0",
    "msg": "Update not allowed on provided Field"
  }
  ```

  * If no data found in the transaction ID:

  ```JSON
  {
    "status": "0",
    "msg": "No Data Found for txnid: 3424"
  }
  ```

  * If the merchant is inactive:

  ```JSON
  {
    "msg": "Merchant is not authorized to use PayU API",
    "status": 0
  }
  ```
</Accordion>

## Important Notes for Cross-Border Subscriptions

<Callout icon="📘" theme="info">
  **Notes**:

  * **buyer_type_business**: This parameter is used in _payment for Cross Border payment transactions to indicate the type of business of the buyer. After the payment is complete, you must use the [Invoice Upload API](ref:invoice_upload_api) to upload the invoices for banks processing.
  * **udf1**: This parameter must contain the buyer's PAN (Permanent Account Number). If the transaction is of UPI mandate or UPI recurring then udf1 should contain the "Buyer's PAN and date of birth in the following format (separated by two pipe characters): Buyer's PAN||Buyer's DOB.
  * **udf3**: This parameter must contain the buyer's DOB. If the transaction is of UPI mandate or UPI recurring then udf3 should contain the "invoice ID of the transaction (generated by the merchant) and merchant name in the following format (separated by two pipe characters): InvoiceID||MerchantName" (where, MerchantName is required for PA2PA integrations only).
  * **udf4**: This parameter must contain the "MerchantName" passed in udf3 in case of PA2PA integration, for UPI mandate consent and recurring transaction, this parameter value should not be passed.
  * **udf5**: This parameter must contain the "invoiceId" for every merchant, this field is mandatory during or after the transaction (using the udf_update API post successful transaction).
</Callout>
