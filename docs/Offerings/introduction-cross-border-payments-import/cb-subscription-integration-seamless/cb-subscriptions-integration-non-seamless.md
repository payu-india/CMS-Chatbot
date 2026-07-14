---
title: '[Redirect] Subscriptions on PayU Hosted Page - Cross-Border'
deprecated: false
hidden: false
metadata:
  title: >-
    PayU Hosted Integration -Subscriptions Integration with Cross-Border
    Payments
  robots: index
---
This section describes how to set up a Payment Consent or Registration transaction for Cross-Border Subscriptions using PayU Hosted Checkout integration with **_payment** API.

**Payment Consent Flow**

<Cards columns={2}>
  <Card title="1. Payment Consent Transaction using PayU Hosted Chackout" href="#step-1-payment-consent-transaction-using-payu-hosted-checkout">
    Send the ENACH consent transaction request with S2S parameters.
  </Card>

  <Card title="2. Verify the Mandate" href="#step-2-verify-the-mandate">
    Send the ENACH consent transaction request with S2S parameters.
  </Card>

  <Card title="3. Verify Payment" href="#step-3-verify_the_payment">
    Handle the response for Net Banking flow.
  </Card>
</Cards>

**Recurring Payments Flow**

<Cards columns={2}>
  <Card title="1. Pre-Debit SI Notification" href="#step-1-pre-debit-si-notification">
    Send pre-debit notifications for upcoming recurring debits.
  </Card>

  <Card title="2. Recurring Payment Transaction" href="#step-2-recurring-payment-transaction">
    Execute recurring payment transactions using the registered mandate.
  </Card>
</Cards>

## Payment Consent Transaction Flow

### Step 1: Payment Consent Transaction using PayU Hosted Checkout

For detailed information about the Payment Consent Transaction using PayU Hosted Checkout, refer to [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted).

<Callout icon="📘" theme="info">
  **Note**: For Cross-Border Payments, the UDF parameters (udf1, udf2, udf3, udf4, and udf5) have specific requirements as described in the Request parameters table below.
</Callout>

<Accordion title="Request parameters" icon="fa-info-circle">
  In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

  | Parameter                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                   |
  | :----------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | key<br /><code>mandatory</code>                                                            | <code>varchar</code> This parameter is the unique Merchant Key provided by PayU for your merchant account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Your Test Key                                                                                                                                                             |
  | txnid<br /><code>mandatory</code>                                                          | <code>varchar</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post a unique transaction ID for every new transaction. <code>Character limit</code>: 25<br /><strong>Note:</strong> Ensure this transaction ID hasn't been processed successfully before. | fd3e847h2                                                                                                                                                                 |
  | amount<br /><code>mandatory</code>                                                         | <code>float</code> This parameter should contain the payment amount for the specific transaction.<br /><strong>Note:</strong> Typecast the amount to a float type. The amount can vary based on use cases:<br />• For Net Banking, 0 INR<br />• For Cards & UPI, a minimum of 1 INR (penny transactions)                                                                                                                                                                                                                                                                               | 1000                                                                                                                                                                      |
  | productinfo<br /><code>mandatory</code>                                                    | <code>varchar</code> A brief product description. Short information about the product/service. Character limit: 100                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Time Magazine Subscription                                                                                                                                                |
  | firstname<br /><code>mandatory</code>                                                      | <code>varchar</code> The customer's first name.<br />Character limit is 60.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Ashish                                                                                                                                                                    |
  | lastname<br /><code>mandatory</code>                                                       | <code>varchar</code> The customer's last name.<br />Character limit is 60.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Kumar                                                                                                                                                                     |
  | email<br /><code>mandatory</code>                                                          | <code>varchar</code> Contains the email of the customer; highly recommended accuracy as fraud detection relies on this. Character limit: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                           | [Ashish@test.com](mailto:Ashish@test.com)                                                                                                                                 |
  | phone<br /><code>mandatory</code>                                                          | <code>varchar</code> Customer phone number for fraud detection and user tracking. Character limit: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 9843176540                                                                                                                                                                |
  | address1<br /><code>optional but recommended for higher approval rate</code>               | <code>varchar</code> The customer's primary billing address line. This field is required for billing and fraud prevention purposes. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                              | 123 Main Street                                                                                                                                                           |
  | address2<br /><code>optional</code>               | <code>varchar</code> The customer's secondary billing address line. This field is required for billing and fraud prevention purposes. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                              | Anytown                                                                                                                                                           |
  | city<br /><code>optional but recommended for higher approval rate</code>                   | <code>varchar</code> The customer's billing city. This field is required for billing and fraud prevention purposes. Character limit: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                               | New York                                                                                                                                                                  |
  | state<br /><code>optional but recommended for higher approval rate</code>                  | <code>varchar</code> The customer's billing state or province. This field is required for billing and fraud prevention purposes. Character limit: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                  | NY                                                                                                                                                                        |
  | country<br /><code>optional but recommended for higher approval rate</code>                | <code>varchar</code> The customer's billing country code. This field is required for billing and fraud prevention purposes. Use ISO 3166-1 alpha-2 country codes. Character limit: 2.                                                                                                                                                                                                                                                                                                                                                                                                  | US                                                                                                                                                                        |
  | zipcode<br /><code>mandatory</code>                                                        | <code>varchar</code> The customer's billing postal/zip code. This field is required for billing and fraud prevention purposes. Character limit: 20.                                                                                                                                                                                                                                                                                                                                                                                                                                    | 10001                                                                                                                                                                     |
  | surl<br /><code>mandatory</code>                                                           | <code>URL</code> The success URL to which PayU redirects after a successful transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [https://example.com/success](https://example.com/success)                                                                                                                |
  | furl<br /><code>mandatory</code>                                                           | <code>URL</code> The failure URL to which PayU redirects after a failed transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | [https://example.com/failure](https://example.com/failure)                                                                                                                |
  | api\_version<br /><code>mandatory</code>                                                   | <code>int</code> Constant value to indicate the API version. Always pass as 7.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 7                                                                                                                                                                         |
  | si<br /><code>mandatory</code>                                                             | <code>int</code> Signifies user consent for subscriptions. Must be 1 for a valid subscription setup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1                                                                                                                                                                         |
  | free\_trial<br /><code>optional</code>                                                     | <code>int</code> Enables free trials (adjusts transaction amount to INR 0.00 for Net Banking, INR 2.00 for others).                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 1                                                                                                                                                                         |
  | si\_details<br /><code>mandatory</code>                                                    | <code>JSON</code> Details required for subscription registration as per RBI guidelines. Must include billingAmount, billingCurrency, billingCycle, billingInterval, paymentStartDate, and paymentEndDate.                                                                                                                                                                                                                                                                                                                                                                              | \{"billingAmount": "100.00", "billingCurrency": "INR", "billingCycle": "MONTHLY", "billingInterval": 1, "paymentStartDate": "2019-09-01", "paymentEndDate": "2019-12-01"} |
  | udf1<br /><code>optional but recommended for higher approval rate</code>                   | <code>String</code> If needed, contains the buyer's PAN. For UPI recurring, format is "Buyer's PAN\\\|\\\|Buyer's DOB". Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                          | AELPR1234E or AELPR1234E\\\|\\\|02-02-1980                                                                                                                                |
  | udf2<br /><code>optional</code>                                                            | <code>String</code> User-defined field for storing transaction-specific data. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Additional transaction data                                                                                                                                               |
  | udf3<br />`optional but recommended for higher approval rate`                              | `String` Date of Birth (DOB) of buyer in DD-MM-YYYY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 02-02-1980                                                                                                                                                                |
  | udf4<br />`mandatory for payment aggregators`                                              | `String` End merchant legal entity name. For UPI, this field should not be passed. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | XYZ Pvt. Ltd.                                                                                                                                                             |
  | udf5<br />`mandatory for cross-border payments`                                            | `String` Contains invoice ID for the merchant. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | INV123456                                                                                                                                                                 |
  | buyer\_type\_business<br />`optional in case of B2B transaction for cross-border payments` | `Binary` To be sent as "1" in case the buyer is a business. In case of individual buyers, it can be skipped. Default is "0".<br />**Note**: This will be included in hash if posted (covered in next section).                                                                                                                                                                                                                                                                                                                                                                         | 1                                                                                                                                                                         |
  | udf\_params<br />`optional`                                                                | `String JSON`<br /><br />UDF7 value to capture "Import or Export Code" of the buyer<br /><br />UDF8 value to capture Airway Bill Number / Consignment Number (in case of goods imports)                                                                                                                                                                                                                                                                                                                                                                                                | \{"udf7":"0100000029",<br />"udf8":"99953729071"}                                                                                                                         |
  | hash<br />`mandatory`                                                                      | `String` Crucial security parameter using SHA512 hash encryption. Formula incorporates key, txnid, amount, productinfo, firstname, email, udf fields, si\_details, and merchant salt.                                                                                                                                                                                                                                                                                                                                                                                                  | \<Generated Hash>                                                                                                                                                         |
</Accordion>

<Accordion title="Hash Logic" icon="fa-info-circle">
  <PACB_Hashing />
</Accordion>

#### Sample request

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

### Step 2: Verify the Mandate

<Accordion title="Verify Netbanking Mandate" icon="fa-info-circle">
  The API returns response structure for Net Banking flow.

  <Accordion title="Net Banking Response" icon="fa-check">
    For Net Banking, the response is returned in URL-encoded format (application/x-www-form-urlencoded):

    ```json
    {
        "metaData": {
            "message": null,
            "referenceId": "cf0f49bb21893055c5ad7182642fc4cf3e1135385b9e55d0b6b0f5e45a19ee74",
            "statusCode": null,
            "txnId": "my_order_2542",
            "txnStatus": "pending",
            "unmappedStatus": "pending"
        },
        "result": {
            "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vcGdzaW0wMS5wYXl1LmluL2luaXRpYXRlIiBtZXRob2Q9InBvc3QiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9Im1lcmNoYW50TmFtZSIgdmFsdWU9IlBBWVUiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9Im1lcmNoYW50Q29kZSIgdmFsdWU9IlNsRXNjdUpBOTgiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9Im1lck5hbWUiIHZhbHVlPSJTdWRoYW5zaHUiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InR4bkFtb3VudCIgdmFsdWU9IjIuMDAiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InR4bkRhdGUiIHZhbHVlPSIyMDI1LTEyLTI2Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJ0eG5DdXJyZW5jeSIgdmFsdWU9IklOUiI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iY3VzdE5hbWUiIHZhbHVlPSJzdWRoYW5zaHUiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9ImN1c3RFbWFpbCIgdmFsdWU9InRlc3RAdGVzdC5jb20iPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9ImN1c3RNb2JpbGUiIHZhbHVlPSI5OTk5OTk5OTk5Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJ0eG5SZWZJZCIgdmFsdWU9Im15X29yZGVyXzI1NDIiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9ImxpdmVtb2RlIiB2YWx1ZT0iZmFsc2UiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InNvdXJjZSIgdmFsdWU9IiI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iUlUiIHZhbHVlPSJodHRwczovL3Rlc3QucGF5dS5pbi9jZjBmNDliYjIxODkzMDU1YzVhZDcxODI2NDJmYzRjZjMyYTNkNjQ3YWUwODA5ZDJhMDM0MzJmOTIxOTg4NzIxL1Rlc3RQZ19yZXNwb25zZS5waHAiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9Im1vZGUiIHZhbHVlPSJUa0k9Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJ0eG5EZXNjcmlwdGlvbiIgdmFsdWU9IlRlc3QgTmV0IEJhbmtpbmcgUGF5bWVudCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iaWJpYm9fY29kZSIgdmFsdWU9IkFYSUIiPjwvZm9ybT48c2NyaXB0IHR5cGU9J3RleHQvamF2YXNjcmlwdCc+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB3aW5kb3cub25sb2FkPWZ1bmN0aW9uKCl7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZG9jdW1lbnQuZm9ybXNbJ3BheW1lbnRfcG9zdCddLnN1Ym1pdCgpOwogICAgICAgICAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgICAgICAgICA8L3NjcmlwdD48L2JvZHk+PC9odG1sPg==",
            "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
        }
    }
    ```
  </Accordion>

  <Accordion title="Response Handling Logic" icon="fa-info-circle">
    ### Expected Values for Successful Registration

    | Response Parameter | Expected Value | Description                                                                       |
    | ------------------ | -------------- | --------------------------------------------------------------------------------- |
    | status             | `success`      | Indicates that the transaction is successful with the Net Banking provider        |
    | payment\_source    | `sist`         | Indicates Net Banking details have been marked correctly for Standing Instruction |
    | mihpayid           | `<mihpayid>`   | PayU's transaction acknowledgment for a Consent transaction                       |
  </Accordion>
</Accordion>

<Accordion title="Verify Mandate for Cards" icon="fa-info-circle">
  After successful registration, verify the mandate status:

  1. **Check Response Parameters**:

  | **Response Parameter** | **Expected Value**              | **Description**                                                                         |
  | ---------------------- | ------------------------------- | --------------------------------------------------------------------------------------- |
  | status                 | success                         | Indicates that the transaction is successful with the UPI provider                      |
  | payment\_source        | SIST                            | Indicates that UPI details have been marked correctly for Standing Instruction          |
  | mihpayid               | \<mihpayid number> sent by PayU | Indicates PayU’s transaction acknowledgment for a Consent transaction                   |
  | cardToken              | Alphanumeric string             | Mandatory to be validated if mode is CC or DC returned in response. Should not be empty |

  2. **Store Mandate Details**:
     * Save `mihpayid` for future recurring payments
     * Store `cardToken` if tokenization is enabled
     * Save mandate expiry dates from `si_details`

  3. **Test Recurring Payment**:
     * Use the stored `mihpayid` to initiate a recurring payment
     * Verify the payment processes successfully
</Accordion>

<Accordion title="Verify UPI Mandate" icon="fa-check-circle">
  1. **Check Response Parameters**:
     * `status` should be `success`
     * `payment_source` should be `sist`
     * `mihpayid` should not be null

  2. **Store Mandate Details**:
     * Save `mihpayid` for future recurring payments
     * Save mandate expiry dates from `si_details`
     * Store customer's VPA for reference

  3. **Test Subsequent Payment**:
     * Use the stored mandate details to initiate a subsequent recurring payment
     * Verify the payment processes successfully
</Accordion>

### Step 3: Verify the Payment

Upon receiving the response, PayU recommends performing a reconciliation step to validate all transaction details. You can verify your payments using either of the following methods:

<Verify_Payment_Tabs />

### Step 4: Update Invoice ID [Optional]

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

<PACB_Recurring_Payments_Flow />

## Important Notes for Cross-Border Subscriptions

<Callout icon="📘" theme="info">
  **Notes**:

  * **buyer_type_business**: This parameter is used in _payment for Cross Border payment transactions to indicate the type of business of the buyer. After the payment is complete, you must use the [Invoice Upload API](ref:invoice_upload_api) to upload the invoices for banks processing.
  * **udf1**: This parameter may contain the buyer's PAN (Permanent Account Number). If the transaction is of UPI mandate or UPI recurring then udf1 should contain the "Buyer's PAN and date of birth in the following format (separated by two pipe characters): Buyer's PAN||Buyer's DOB.
  * **udf3**: This parameter may contain the buyer's DOB. If the transaction is of UPI mandate or UPI recurring then udf3 should contain the "invoice ID of the transaction (generated by the merchant) and merchant name in the following format (separated by two pipe characters): InvoiceID||MerchantName" (where, MerchantName is required for PA2PA integrations only).
  * **udf4**: This parameter must contain the "MerchantName" passed in udf3 in case of PA2PA integration, for UPI mandate consent and recurring transaction, this parameter value should not be passed.
  * **udf5**: This parameter must contain the "invoiceId" for every merchant, this field is mandatory during or after the transaction (using the udf_update API post successful transaction).
</Callout>