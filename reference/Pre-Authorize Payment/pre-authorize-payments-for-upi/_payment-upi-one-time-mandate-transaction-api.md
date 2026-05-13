---
title: UPI One-Time Mandate API - Merchant Hosted
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This section describes the request and response parameters with sample request and response for UPI One-Time mandate Intent and Collect flow. For more information on integration, refer to [Merchant Hosted Integration - UPI OTM](doc:merchant-hosted-integration-upi-otm).

<Callout icon="📘" theme="info">
  **Note**: Currently, PayU supports UPI One-Time Mandate only for the Seamless integration.
</Callout>

<br />

<Callout icon="👍" theme="okay">
  Experience the end-to-end **Merchant Hosted Checkout**> **UPI** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

  <HTMLBlock>{`
                          <style>
                          .tooltip-btn {
                              position: relative;
                              background-color: #4CAF50;
                              color: white;
                              padding: 10px 20px;
                              border: none;
                              border-radius: 5px;
                              cursor: pointer;
                              font-weight: bold; /* Added this line */
                          }
                          .tooltip-btn:hover::after {
                              content: attr(data-tooltip);
                              position: absolute;
                              bottom: 125%;
                              left: 50%;
                              transform: translateX(-50%);
                              background-color: #333;
                              color: white;
                              padding: 5px 10px;
                              border-radius: 4px;
                              white-space: nowrap;
                              font-size: 12px;
                              z-index: 1;
                          }
                          </style>

                          <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-otm', '_blank')" 
                                  class="tooltip-btn" 
                                  data-tooltip="Click here to see the Merchant Hosted Checkout > UPI end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
                              Experience the flow and get the code
                          </button>
  `}</HTMLBlock>
</Callout>

## Request Parameters

<PaymentAPIEnvironment />

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key `mandatory`
      </td>

      <td>
        `varchar` This parameter is the unique Merchant Key provided by PayU for your merchant account.
      </td>

      <td>
        Your Test Key
      </td>
    </tr>

    <tr>
      <td>
        txnid `mandatory`
      </td>

      <td>
        `varchar` This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant’s) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction. `Character limit`: 25

        * _Note_*: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of ‘duplicate Order ID.’
      </td>

      <td>
        fd3e847h2
      </td>
    </tr>

    <tr>
      <td>
        amount `mandatory`
      </td>

      <td>
        `float` This parameter should contain the payment amount of the particular transaction.

        * _Note_*: Type-cast the amount to float type
      </td>

      <td>
        1000
      </td>
    </tr>

    <tr>
      <td>
        productinfo `mandatory`
      </td>

      <td>
        `varchar` This parameter should contain a brief product description. It should be a string describing the product. `Character limit`: 100
      </td>

      <td>
        Time Magazine Subscription
      </td>
    </tr>

    <tr>
      <td>
        firstname `mandatory`
      </td>

      <td>
        `varchar` Must contain the first name of the customer. `Character limit`: 60
      </td>

      <td>
        Ashish
      </td>
    </tr>

    <tr>
      <td>
        email `mandatory`
      </td>

      <td>
        `varchar` Must contain the email of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information. Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions. Character limit: 50
      </td>

      <td>
        [Ashish@test.com](mailto:Ashish@test.com)
      </td>
    </tr>

    <tr>
      <td>
        phone `mandatory`
      </td>

      <td>
        `varchar` Must contain the phone number of the customer.

        This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions. Character limit: 50
      </td>

      <td>
        9843176540
      </td>
    </tr>

    <tr>
      <td>
        surl `mandatory`
      </td>

      <td>
        surL is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        furl `mandatory`
      </td>

      <td>
        furl is the acronym for for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        pg `mandatory`
      </td>

      <td>
        It defines the payment category for which you wish to perform UPI One-Time Mandate. For UPI, **pg= UPI**
      </td>

      <td>
        UPI
      </td>
    </tr>

    <tr>
      <td>
        bankcode `mandatory`
      </td>

      <td>
        It defines the bank with which you wish to perform UPI using the bank code. Use **UPI** or **INTENT** according to the use case.
      </td>

      <td>
        * **UPI**: Used for UPI Collect
        * **INTENT**: Used for UPI Intent
      </td>
    </tr>

    <tr>
      <td>
        vpa `mandatory`
      </td>

      <td>
        This parameter contains the customer’s VPA handle. For the list UPI handles supported, refer to UPI Handles

        The merchant is advised to check the validity of the VPA through using the VPA Validation API. PayU extends support for the same if required. For more information on using VPA Validation API, refer to  [Validate VPA API](ref:validate_vpa_api).
      </td>

      <td>
        abc@payu
      </td>
    </tr>

    <tr>
      <td>
        txn_s2s_flow `mandatory`
      </td>

      <td>
        This parameter must be passed with the values as **4** for UPI Intent.
      </td>

      <td>
        4
      </td>
    </tr>

    <tr>
      <td>
        pre_authorize `mandatory for Pre-Auth`
      </td>

      <td>
        This parameter is set to**1** to pre-authorize payment.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        si_Details
      </td>

      <td>
        This parameter contains the following information in JSON format:

        * paymentStartDate
        * paymentEndDate
          * _Example_*:  \{"paymentStartDate":"2024-07-24","paymentEndDate":"2024-07-28"}
      </td>

      <td>
        \{"paymentStartDate":"2024-07-24","paymentEndDate":"2024-07-28"}
      </td>
    </tr>

    <tr>
      <td>
        hash `mandatory`
      </td>

      <td>
        Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU’s payment interface while registration transactions.

        It is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by merchant salt.

        In the case of registration transaction, the formula is used to calculate this hash is similar to the following: `HASH = SHA512(sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT))`
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

## Sample request

### Intent Flow

```curl
curl --request POST  

--url https://test.payu.in/_payment  
--header 'accept: text/plain'  
--header 'content-type: application/x-www-form-urlencoded'  
--data key=JPM7Fg  
--data pg=UPI  
--data bankcode=INTENT 
--data txn_s2s_flow=4  
--data txnid=aso6787  
--data siDetails="{"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}"  
--data pre_authorize=1 \ 
 --data amount=100.00  
--data productinfo=iPhone  
--data firstname=Ashish  
--data email=ashish@abc.com  
--data phone=9876543210  
--data surl=https://apiplayground-response.herokuapp.com/  
--data furl=https://apiplayground-response.herokuapp.com/  
--data hash=8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b 
```
```python
# Python implementation using requests library
import requests

# Define the URL and headers
url = "https://test.payu.in/_payment"
headers = {
    "accept": "text/plain",
    "content-type": "application/x-www-form-urlencoded"
}

# Define the form data
form_data = {
    "key": "JPM7Fg",
    "pg": "UPI",
    "bankcode": "INTENT",
    "txn_s2s_flow": "4",
    "txnid": "aso6787",
    "siDetails": "{\"paymentStartDate\": \"2019-09-01\",\"paymentEndDate\": \"2019-12-01\"}",
    "pre_authorize": "1",
    "amount": "100.00",
    "productinfo": "iPhone",
    "firstname": "Ashish",
    "email": "ashish@abc.com",
    "phone": "9876543210",
    "surl": "https://apiplayground-response.herokuapp.com/",
    "furl": "https://apiplayground-response.herokuapp.com/",
    "hash": "8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b"
}

# Make the POST request
try:
    response = requests.post(url, headers=headers, data=form_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

```
```java
// Java implementation using OkHttp library
import okhttp3.*;
import java.io.IOException;

public class PayUClient {
    private static final OkHttpClient client = new OkHttpClient();

    public static void main(String[] args) {
        // Define the URL
        String url = "https://test.payu.in/_payment";

        // Create form body
        RequestBody formBody = new FormBody.Builder()
            .add("key", "JPM7Fg")
            .add("pg", "UPI")
            .add("bankcode", "INTENT")
            .add("txn_s2s_flow", "4")
            .add("txnid", "aso6787")
            .add("siDetails", "{\"paymentStartDate\": \"2019-09-01\",\"paymentEndDate\": \"2019-12-01\"}")
            .add("pre_authorize", "1")
            .add("amount", "100.00")
            .add("productinfo", "iPhone")
            .add("firstname", "Ashish")
            .add("email", "ashish@abc.com")
            .add("phone", "9876543210")
            .add("surl", "https://apiplayground-response.herokuapp.com/")
            .add("furl", "https://apiplayground-response.herokuapp.com/")
            .add("hash", "8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b")
            .build();

        // Create request
        Request request = new Request.Builder()
            .url(url)
            .addHeader("accept", "text/plain")
            .addHeader("content-type", "application/x-www-form-urlencoded")
            .post(formBody)
            .build();

        try {
            // Execute the request
            Response response = client.newCall(request).execute();
            System.out.println("Status Code: " + response.code());
            System.out.println("Response: " + response.body().string());
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}

```
```php
// Define the URL
$url = "https://test.payu.in/_payment";

// Define the form data
$formData = array(
    'key' => 'JPM7Fg',
    'pg' => 'UPI',
    'bankcode' => 'INTENT',
    'txn_s2s_flow' => '4',
    'txnid' => 'aso6787',
    'siDetails' => '{"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}',
    'pre_authorize' => '1',
    'amount' => '100.00',
    'productinfo' => 'iPhone',
    'firstname' => 'Ashish',
    'email' => 'ashish@abc.com',
    'phone' => '9876543210',
    'surl' => 'https://apiplayground-response.herokuapp.com/',
    'furl' => 'https://apiplayground-response.herokuapp.com/',
    'hash' => '8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b'
);

// Initialize cURL
$ch = curl_init();

// Set cURL options
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($formData));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'accept: text/plain',
    'content-type: application/x-www-form-urlencoded'
));

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
    echo 'Error: ' . curl_error($ch);
} else {
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    echo "Status Code: " . $httpCode . "\n";
    echo "Response: " . $response . "\n";
}

// Close cURL handle
curl_close($ch);
?>

```
```csharp
// C# implementation using HttpClient
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

public class PayUClient
{
    private static readonly HttpClient client = new HttpClient();

    public static async Task Main(string[] args)
    {
        // Define the URL
        string url = "https://test.payu.in/_payment";

        // Set headers
        client.DefaultRequestHeaders.Add("accept", "text/plain");

        // Define the form data
        var formData = new FormUrlEncodedContent(new[]
        {
            new KeyValuePair<string, string>("key", "JPM7Fg"),
            new KeyValuePair<string, string>("pg", "UPI"),
            new KeyValuePair<string, string>("bankcode", "INTENT"),
            new KeyValuePair<string, string>("txn_s2s_flow", "4"),
            new KeyValuePair<string, string>("txnid", "aso6787"),
            new KeyValuePair<string, string>("siDetails", "{\"paymentStartDate\": \"2019-09-01\",\"paymentEndDate\": \"2019-12-01\"}"),
            new KeyValuePair<string, string>("pre_authorize", "1"),
            new KeyValuePair<string, string>("amount", "100.00"),
            new KeyValuePair<string, string>("productinfo", "iPhone"),
            new KeyValuePair<string, string>("firstname", "Ashish"),
            new KeyValuePair<string, string>("email", "ashish@abc.com"),
            new KeyValuePair<string, string>("phone", "9876543210"),
            new KeyValuePair<string, string>("surl", "https://apiplayground-response.herokuapp.com/"),
            new KeyValuePair<string, string>("furl", "https://apiplayground-response.herokuapp.com/"),
            new KeyValuePair<string, string>("hash", "8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b")
        });

        try
        {
            // Make the POST request
            HttpResponseMessage response = await client.PostAsync(url, formData);
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

### Collect Flow

```curl
curl --request POST  
--url https://test.payu.in/_payment  
--header 'accept: text/plain'  
--header 'content-type: application/x-www-form-urlencoded'  
--data key=JPM7Fg  
--data pg=UPI  
--data bankcode=UPI  
--data vpa=anything@payu  
--data txn_s2s_flow=4  
--data txnid=aso6787  
--data siDetails="{"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}"  
--data pre_authorize=1 \ 
 --data amount=100.00  
--data productinfo=iPhone  
--data firstname=Ashish  
--data email=ashish@abc.com  
--data phone=9876543210  
--data surl=https://apiplayground-response.herokuapp.com/  
--data furl=https://apiplayground-response.herokuapp.com/  
--data hash=8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b 
```
```python
<?php
// PHP implementation using cURL

// Define the URL
$url = "https://test.payu.in/_payment";

// Define the form data
$formData = array(
    'key' => 'JPM7Fg',
    'pg' => 'UPI',
    'bankcode' => 'UPI',
    'vpa' => 'anything@payu',
    'txn_s2s_flow' => '4',
    'txnid' => 'aso6787',
    'siDetails' => '{"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}',
    'pre_authorize' => '1',
    'amount' => '100.00',
    'productinfo' => 'iPhone',
    'firstname' => 'Ashish',
    'email' => 'ashish@abc.com',
    'phone' => '9876543210',
    'surl' => 'https://apiplayground-response.herokuapp.com/',
    'furl' => 'https://apiplayground-response.herokuapp.com/',
    'hash' => '8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b'
);

// Initialize cURL
$ch = curl_init();

// Set cURL options
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($formData));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'accept: text/plain',
    'content-type: application/x-www-form-urlencoded'
));

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
    echo 'Error: ' . curl_error($ch);
} else {
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    echo "Status Code: " . $httpCode . "\n";
    echo "Response: " . $response . "\n";
}

// Close cURL handle
curl_close($ch);
?>

```
```java
// Java implementation using OkHttp library
import okhttp3.*;
import java.io.IOException;

public class PayUClient {
    private static final OkHttpClient client = new OkHttpClient();

    public static void main(String[] args) {
        // Define the URL
        String url = "https://test.payu.in/_payment";

        // Create form body
        RequestBody formBody = new FormBody.Builder()
            .add("key", "JPM7Fg")
            .add("pg", "UPI")
            .add("bankcode", "UPI")
            .add("vpa", "anything@payu")
            .add("txn_s2s_flow", "4")
            .add("txnid", "aso6787")
            .add("siDetails", "{\"paymentStartDate\": \"2019-09-01\",\"paymentEndDate\": \"2019-12-01\"}")
            .add("pre_authorize", "1")
            .add("amount", "100.00")
            .add("productinfo", "iPhone")
            .add("firstname", "Ashish")
            .add("email", "ashish@abc.com")
            .add("phone", "9876543210")
            .add("surl", "https://apiplayground-response.herokuapp.com/")
            .add("furl", "https://apiplayground-response.herokuapp.com/")
            .add("hash", "8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b")
            .build();

        // Create request
        Request request = new Request.Builder()
            .url(url)
            .addHeader("accept", "text/plain")
            .addHeader("content-type", "application/x-www-form-urlencoded")
            .post(formBody)
            .build();

        try {
            // Execute the request
            Response response = client.newCall(request).execute();
            System.out.println("Status Code: " + response.code());
            System.out.println("Response: " + response.body().string());
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}

```
```csharp
// C# implementation using HttpClient
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

public class PayUClient
{
    private static readonly HttpClient client = new HttpClient();

    public static async Task Main(string[] args)
    {
        // Define the URL
        string url = "https://test.payu.in/_payment";

        // Set headers
        client.DefaultRequestHeaders.Add("accept", "text/plain");

        // Define the form data
        var formData = new FormUrlEncodedContent(new[]
        {
            new KeyValuePair<string, string>("key", "JPM7Fg"),
            new KeyValuePair<string, string>("pg", "UPI"),
            new KeyValuePair<string, string>("bankcode", "UPI"),
            new KeyValuePair<string, string>("vpa", "anything@payu"),
            new KeyValuePair<string, string>("txn_s2s_flow", "4"),
            new KeyValuePair<string, string>("txnid", "aso6787"),
            new KeyValuePair<string, string>("siDetails", "{\"paymentStartDate\": \"2019-09-01\",\"paymentEndDate\": \"2019-12-01\"}"),
            new KeyValuePair<string, string>("pre_authorize", "1"),
            new KeyValuePair<string, string>("amount", "100.00"),
            new KeyValuePair<string, string>("productinfo", "iPhone"),
            new KeyValuePair<string, string>("firstname", "Ashish"),
            new KeyValuePair<string, string>("email", "ashish@abc.com"),
            new KeyValuePair<string, string>("phone", "9876543210"),
            new KeyValuePair<string, string>("surl", "https://apiplayground-response.herokuapp.com/"),
            new KeyValuePair<string, string>("furl", "https://apiplayground-response.herokuapp.com/"),
            new KeyValuePair<string, string>("hash", "8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b")
        });

        try
        {
            // Make the POST request
            HttpResponseMessage response = await client.PostAsync(url, formData);
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
```php
# Python implementation using requests library
import requests

# Define the URL and headers
url = "https://test.payu.in/_payment"
headers = {
    "accept": "text/plain",
    "content-type": "application/x-www-form-urlencoded"
}

# Define the form data
form_data = {
    "key": "JPM7Fg",
    "pg": "UPI",
    "bankcode": "UPI",
    "vpa": "anything@payu",
    "txn_s2s_flow": "4",
    "txnid": "aso6787",
    "siDetails": "{\"paymentStartDate\": \"2019-09-01\",\"paymentEndDate\": \"2019-12-01\"}",
    "pre_authorize": "1",
    "amount": "100.00",
    "productinfo": "iPhone",
    "firstname": "Ashish",
    "email": "ashish@abc.com",
    "phone": "9876543210",
    "surl": "https://apiplayground-response.herokuapp.com/",
    "furl": "https://apiplayground-response.herokuapp.com/",
    "hash": "8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b"
}

# Make the POST request
try:
    response = requests.post(url, headers=headers, data=form_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

```

## Sample response

### Intent Flow

#### Success scenario

For Intent, as part of response, Intent URL is returned. Now, merchant needs to use data received in intentURIData parameter, JSON decode the response and use URL to invoke intent at their end

```json
{
  "metaData": {
    "message": null,
    "referenceId": "c5161bae370de1bd4fb886c6c66567a8",
    "statusCode": null,
    "txnId": "a7440cc636e747b635df",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  },
  "result": {
    "paymentId": "99900000000001875",
    "merchantName": "Name409208872",
    "merchantVpa": "paytmqr@icici",
    "amount": "10000.00",
    "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vcHA3OHNlY3VyZS5wYXl1LmluLzY1OWFjNWRhNWUyZjlmNzM1NzhkZWYwYzVjNDM2MWFmOWJhMGVkYmExYjk3NDg2Mjg3ZDI2MzBjZDg1YmU3NWEvaW50ZW50U2VhbWxlc3NIYW5kbGVyLnBocCIgbWV0aG9kPSJwb3N0Ij48aW5..."
    },
    "otpPostUrl": "https://pp78secure.payu.in/ResponseHandler.php"
  }
}

```

### Failure scenario

For Intent, as part of response, Intent URL is returned. Now merchant needs to use data received in intentURIData parameter, JSON decode the response and use URL to invoke intent at their end

After the transaction is authorised by the customer, PayU will receive confirmation. Same will be passed to the merchant as webhook

```json
{
  "metaData": {
    "message": "Transaction failed due to invalid params shared by the merchant",
    "referenceId": "dde7096af9db932a9fd09b9b4383d8be",
    "statusCode": "E1101",
    "txnId": "0c4931ddee7a4f69227f",
    "txnStatus": "failed",
    "intentURIData": "upi://mandate?pa=payu24@icici&pn=Payu&tr=EZM2024042211452400151942&am=10000.00&cu=INR&orgid=400011&mc=6012&purpose=01&tn=Upi%20Mandate&validitystart=22042024&validityend=21052024&amrule=MAX&Recur=ONETIME&Rev=N&Share=Y&Block=Y&txnType=CREATE&mode=13",
    "unmappedStatus": "failure"
  },
  "result": {}
}

```

### Collect Flow

#### Success scenario

```json
{ 
   "metaData":{ 
      "message":null, 
      ""referenceId":"c5161bae370de1bd4fb886c6c66567a8", 
      "statusCode":null, 
      ""txnId":"a7440cc636e747b635df", 
      ""txnStatus":"pending", 
      ""unmappedStatus":"pending" 
   }, 
   "result":{ 
      "postToBank":{ 
         "useMethodGet":true 
      }, 
      "issuerUrl":"https://api.payu.in/ public/#/c5161bae370de1bd4fb886c6c66567a8/upiLoader" 
   } 
} 
 
```

#### Failure scenarios

```json
{ 
   "metaData":{ 
      "message":"Transaction failed due to invalid params shared by the merchant", 
      "referenceId":"dde7096af9db932a9fd09b9b4383d8be", 
      "statusCode":"E1101", 
      "txnId":"0c4931ddee7a4f69227f", 
      "txnStatus":"failed", 
      "unmappedStatus":"failure" 
   }, 
   "result":{ 
       
   } 
} 
```

<br />
