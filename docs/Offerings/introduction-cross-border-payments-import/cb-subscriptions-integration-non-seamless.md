---
title: CB Subscriptions Integration - Non Seamless
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

| Parameter                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                   |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| key<br /><code>mandatory</code>                                        | <code>varchar</code> This parameter is the unique Merchant Key provided by PayU for your merchant account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Your Test Key                                                                                                                                                             |
| txnid<br /><code>mandatory</code>                                      | <code>varchar</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post a unique transaction ID for every new transaction. <code>Character limit</code>: 25<br /><strong>Note:</strong> Ensure this transaction ID hasn't been processed successfully before. | fd3e847h2                                                                                                                                                                 |
| amount<br /><code>mandatory</code>                                     | <code>float</code> This parameter should contain the payment amount for the specific transaction.<br /><strong>Note:</strong> Typecast the amount to a float type. The amount can vary based on use cases:<br />• For Net Banking, 0 INR<br />• For Cards & UPI, a minimum of 1 INR (penny transactions)                                                                                                                                                                                                                                                                               | 1000                                                                                                                                                                      |
| productinfo<br /><code>mandatory</code>                                | <code>varchar</code> A brief product description. Short information about the product/service. Character limit: 100                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Time Magazine Subscription                                                                                                                                                |
| firstname<br /><code>mandatory</code>                                  | <code>varchar</code> The customer's first name.<br />Character limit is 60.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Ashish                                                                                                                                                                    |
| email<br /><code>mandatory</code>                                      | <code>varchar</code> Contains the email of the customer; highly recommended accuracy as fraud detection relies on this. Character limit: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                           | [Ashish@test.com](mailto:Ashish@test.com)                                                                                                                                 |
| phone<br /><code>mandatory</code>                                      | <code>varchar</code> Customer phone number for fraud detection and user tracking. Character limit: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 9843176540                                                                                                                                                                |
| address1<br /><code>mandatory</code>                                   | <code>varchar</code> The customer's primary billing address line. This field is required for billing and fraud prevention purposes. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                              | 123 Main Street                                                                                                                                                           |
| city<br /><code>mandatory</code>                                       | <code>varchar</code> The customer's billing city. This field is required for billing and fraud prevention purposes. Character limit: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                               | New York                                                                                                                                                                  |
| state<br /><code>mandatory</code>                                      | <code>varchar</code> The customer's billing state or province. This field is required for billing and fraud prevention purposes. Character limit: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                  | NY                                                                                                                                                                        |
| country<br /><code>mandatory</code>                                    | <code>varchar</code> The customer's billing country code. This field is required for billing and fraud prevention purposes. Use ISO 3166-1 alpha-2 country codes. Character limit: 2.                                                                                                                                                                                                                                                                                                                                                                                                  | US                                                                                                                                                                        |
| zipcode<br /><code>mandatory</code>                                    | <code>varchar</code> The customer's billing postal/zip code. This field is required for billing and fraud prevention purposes. Character limit: 20.                                                                                                                                                                                                                                                                                                                                                                                                                                    | 10001                                                                                                                                                                     |
| surl<br /><code>mandatory</code>                                       | <code>URL</code> The success URL to which PayU redirects after a successful transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [https://example.com/success](https://example.com/success)                                                                                                                |
| furl<br /><code>mandatory</code>                                       | <code>URL</code> The failure URL to which PayU redirects after a failed transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | [https://example.com/failure](https://example.com/failure)                                                                                                                |
| api_version<br /><code>mandatory</code>                                | <code>int</code> Constant value to indicate the API version. Always pass as 7.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 7                                                                                                                                                                         |
| si<br /><code>mandatory</code>                                         | <code>int</code> Signifies user consent for subscriptions. Must be 1 for a valid subscription setup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1                                                                                                                                                                         |
| free_trial<br /><code>optional</code>                                  | <code>int</code> Enables free trials (adjusts transaction amount to INR 0.00 for Net Banking, INR 2.00 for others).                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 1                                                                                                                                                                         |
| si_details<br /><code>mandatory</code>                                 | <code>JSON</code> Details required for subscription registration as per RBI guidelines. Must include billingAmount, billingCurrency, billingCycle, billingInterval, paymentStartDate, and paymentEndDate.                                                                                                                                                                                                                                                                                                                                                                              | \{"billingAmount": "100.00", "billingCurrency": "INR", "billingCycle": "MONTHLY", "billingInterval": 1, "paymentStartDate": "2019-09-01", "paymentEndDate": "2019-12-01"} |
| udf1<br /><code>conditional</code>                                     | <code>String</code> If needed, contains the buyer's PAN. For UPI recurring, format is "Buyer's PAN\|\|Buyer's DOB". Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                              | AELPR1234E or AELPR1234E\|\|02-02-1980                                                                                                                                    |
| udf2<br /><code>optional</code>                                        | <code>String</code> User-defined field for storing transaction-specific data. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Additional transaction data                                                                                                                                               |
| udf3<br /><code>conditional</code>                                     | <code>String</code> Contains buyer's DOB (DD-MM-YYYY format). For UPI, format is "InvoiceID\|\|MerchantName". Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 02-02-1980 or INV-123_1231\|\|MerchantName                                                                                                                                |
| udf4<br /><code>mandatory<br /> for payment<br /> aggregators</code>   | <code>String</code> End merchant legal entity name. For UPI, this field should not be passed. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | XYZ Pvt. Ltd.                                                                                                                                                             |
| udf5<br /><code>mandatory<br /> for cross-border<br /> payments</code> | <code>String</code> Contains invoice ID for the merchant. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | INV123456                                                                                                                                                                 |
| hash<br /><code>mandatory</code>                                       | <code>String</code> Crucial security parameter using SHA512 hash encryption. Formula incorporates key, txnid, amount, productinfo, firstname, email, udf fields, si_details, and merchant salt.                                                                                                                                                                                                                                                                                                                                                                                        | \<Generated Hash>                                                                                                                                                         |

<HashingRequestParameters />

<Accordion title="My Accordion Title" icon="fa-info-circle">
  <HashingSample />
</Accordion>

### Sample request

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JPM7Fg&txnid=payuTestTxn12345&amount=100.00&productinfo=iPhone&firstname=Ashish&email=test@gmail.com&phone=9876543210&surl=https://example.com/success&furl=https://example.com/failure&pg=NB&bankcode=TESTPGNB&txn_s2s_flow=4&s2s_client_ip=10.200.12.12&s2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0&udf1=AELPR****E&udf3=02-02-1980&udf4=XYZ Pvt. Ltd.&udf5=098450845&buyer_type_business=1&udf_params={\"udf7\":\"<IE_CODE>\",\"udf8\":\"<AWB Num>\"}&hash=<generated_hash>"
```
```python
import requests

url = "https://test.payu.in/_payment"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "key": "JPM7Fg",
    "txnid": "payuTestTxn12345",
    "amount": "100.00",
    "productinfo": "iPhone",
    "firstname": "Ashish",
    "email": "test@gmail.com",
    "phone": "9876543210",
    "surl": "https://example.com/success",
    "furl": "https://example.com/failure",
    "pg": "NB",
    "bankcode": "TESTPGNB",
    "txn_s2s_flow": "4",
    "s2s_client_ip": "10.200.12.12",
    "s2s_device_info": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0",
    "udf1": "AELPR****E",
    "udf3": "02-02-1980",
    "udf4": "XYZ Pvt. Ltd.",
    "udf5": "098450845",
    "buyer_type_business": "1",
    "udf_params": '{"udf7":"<IE_CODE>","udf8":"<AWB Num>"}',
    "hash": "<generated_hash>"
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
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string url = "https://test.payu.in/_payment";
        
        var formData = new List<KeyValuePair<string, string>>
        {
            new KeyValuePair<string, string>("key", "JPM7Fg"),
            new KeyValuePair<string, string>("txnid", "payuTestTxn12345"),
            new KeyValuePair<string, string>("amount", "100.00"),
            new KeyValuePair<string, string>("productinfo", "iPhone"),
            new KeyValuePair<string, string>("firstname", "Ashish"),
            new KeyValuePair<string, string>("email", "test@gmail.com"),
            new KeyValuePair<string, string>("phone", "9876543210"),
            new KeyValuePair<string, string>("surl", "https://example.com/success"),
            new KeyValuePair<string, string>("furl", "https://example.com/failure"),
            new KeyValuePair<string, string>("pg", "NB"),
            new KeyValuePair<string, string>("bankcode", "TESTPGNB"),
            new KeyValuePair<string, string>("txn_s2s_flow", "4"),
            new KeyValuePair<string, string>("s2s_client_ip", "10.200.12.12"),
            new KeyValuePair<string, string>("s2s_device_info", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0"),
            new KeyValuePair<string, string>("udf1", "AELPR****E"),
            new KeyValuePair<string, string>("udf3", "02-02-1980"),
            new KeyValuePair<string, string>("udf4", "XYZ Pvt. Ltd."),
            new KeyValuePair<string, string>("udf5", "098450845"),
            new KeyValuePair<string, string>("buyer_type_business", "1"),
            new KeyValuePair<string, string>("udf_params", "{\"udf7\":\"<IE_CODE>\",\"udf8\":\"<AWB Num>\"}"),
            new KeyValuePair<string, string>("hash", "<generated_hash>")
        };

        using (HttpClient client = new HttpClient())
        {
            try
            {
                var content = new FormUrlEncodedContent(formData);
                content.Headers.ContentType.MediaType = "application/x-www-form-urlencoded";
                
                HttpResponseMessage response = await client.PostAsync(url, content);
                
                Console.WriteLine($"Status Code: {response.StatusCode}");
                string responseContent = await response.Content.ReadAsStringAsync();
                Console.WriteLine($"Response: {responseContent}");
            }
            catch (HttpRequestException e)
            {
                Console.WriteLine($"Error: {e.Message}");
            }
        }
    }
}
```
```javascript
async function makePayment() {
    const url = "https://test.payu.in/_payment";
    
    const formData = new URLSearchParams({
        "key": "JPM7Fg",
        "txnid": "payuTestTxn12345",
        "amount": "100.00",
        "productinfo": "iPhone",
        "firstname": "Ashish",
        "email": "test@gmail.com",
        "phone": "9876543210",
        "surl": "https://example.com/success",
        "furl": "https://example.com/failure",
        "pg": "NB",
        "bankcode": "TESTPGNB",
        "txn_s2s_flow": "4",
        "s2s_client_ip": "10.200.12.12",
        "s2s_device_info": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0",
        "udf1": "AELPR****E",
        "udf3": "02-02-1980",
        "udf4": "XYZ Pvt. Ltd.",
        "udf5": "098450845",
        "buyer_type_business": "1",
        "udf_params": '{"udf7":"<IE_CODE>","udf8":"<AWB Num>"}',
        "hash": "<generated_hash>"
    });

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: formData
        });

        console.log(`Status Code: ${response.status}`);
        const responseText = await response.text();
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.log(`Error: ${error.message}`);
    }
}

makePayment();
```
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.StringJoiner;

public class PayUPayment {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://test.payu.in/_payment");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            connection.setDoOutput(true);
            
            StringJoiner formData = new StringJoiner("&");
            formData.add("key=" + URLEncoder.encode("JPM7Fg", StandardCharsets.UTF_8));
            formData.add("txnid=" + URLEncoder.encode("payuTestTxn12345", StandardCharsets.UTF_8));
            formData.add("amount=" + URLEncoder.encode("100.00", StandardCharsets.UTF_8));
            formData.add("productinfo=" + URLEncoder.encode("iPhone", StandardCharsets.UTF_8));
            formData.add("firstname=" + URLEncoder.encode("Ashish", StandardCharsets.UTF_8));
            formData.add("email=" + URLEncoder.encode("test@gmail.com", StandardCharsets.UTF_8));
            formData.add("phone=" + URLEncoder.encode("9876543210", StandardCharsets.UTF_8));
            formData.add("surl=" + URLEncoder.encode("https://example.com/success", StandardCharsets.UTF_8));
            formData.add("furl=" + URLEncoder.encode("https://example.com/failure", StandardCharsets.UTF_8));
            formData.add("pg=" + URLEncoder.encode("NB", StandardCharsets.UTF_8));
            formData.add("bankcode=" + URLEncoder.encode("TESTPGNB", StandardCharsets.UTF_8));
            formData.add("txn_s2s_flow=" + URLEncoder.encode("4", StandardCharsets.UTF_8));
            formData.add("s2s_client_ip=" + URLEncoder.encode("10.200.12.12", StandardCharsets.UTF_8));
            formData.add("s2s_device_info=" + URLEncoder.encode("Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0", StandardCharsets.UTF_8));
            formData.add("udf1=" + URLEncoder.encode("AELPR****E", StandardCharsets.UTF_8));
            formData.add("udf3=" + URLEncoder.encode("02-02-1980", StandardCharsets.UTF_8));
            formData.add("udf4=" + URLEncoder.encode("XYZ Pvt. Ltd.", StandardCharsets.UTF_8));
            formData.add("udf5=" + URLEncoder.encode("098450845", StandardCharsets.UTF_8));
            formData.add("buyer_type_business=" + URLEncoder.encode("1", StandardCharsets.UTF_8));
            formData.add("udf_params=" + URLEncoder.encode("{\"udf7\":\"<IE_CODE>\",\"udf8\":\"<AWB Num>\"}", StandardCharsets.UTF_8));
            formData.add("hash=" + URLEncoder.encode("<generated_hash>", StandardCharsets.UTF_8));
            
            try (OutputStream outputStream = connection.getOutputStream()) {
                byte[] input = formData.toString().getBytes(StandardCharsets.UTF_8);
                outputStream.write(input, 0, input.length);
            }
            
            int responseCode = connection.getResponseCode();
            System.out.println("Status Code: " + responseCode);
            
            BufferedReader reader = new BufferedReader(new InputStreamReader(
                responseCode >= 200 && responseCode < 300 ? connection.getInputStream() : connection.getErrorStream()
            ));
            
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                response.append(line).append("\n");
            }
            reader.close();
            
            System.out.println("Response: " + response.toString());
            
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
$url = "https://test.payu.in/_payment";

$data = array(
    "key" => "JPM7Fg",
    "txnid" => "payuTestTxn12345",
    "amount" => "100.00",
    "productinfo" => "iPhone",
    "firstname" => "Ashish",
    "email" => "test@gmail.com",
    "phone" => "9876543210",
    "surl" => "https://example.com/success",
    "furl" => "https://example.com/failure",
    "pg" => "NB",
    "bankcode" => "TESTPGNB",
    "txn_s2s_flow" => "4",
    "s2s_client_ip" => "10.200.12.12",
    "s2s_device_info" => "Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0",
    "udf1" => "AELPR****E",
    "udf3" => "02-02-1980",
    "udf4" => "XYZ Pvt. Ltd.",
    "udf5" => "098450845",
    "buyer_type_business" => "1",
    "udf_params" => '{"udf7":"<IE_CODE>","udf8":"<AWB Num>"}',
    "hash" => "<generated_hash>"
);

$curl = curl_init();

curl_setopt_array($curl, array(
    CURLOPT_URL => $url,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => http_build_query($data),
    CURLOPT_HTTPHEADER => array(
        "Content-Type: application/x-www-form-urlencoded"
    ),
));

$response = curl_exec($curl);
$httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);

if (curl_errno($curl)) {
    echo "Error: " . curl_error($curl);
} else {
    echo "Status Code: " . $httpCode . "\n";
    echo "Response: " . $response;
}

curl_close($curl);
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

<br />

<br />

## Important Notes for Cross-Border Subscriptions

<Callout icon="📘" theme="info">
  **Notes**:

  * **buyer_type_business**: This parameter is used in _payment for Cross Border payment transactions to indicate the type of business of the buyer. After the payment is complete, you must use the [Invoice Upload API](ref:invoice_upload_api) to upload the invoices for banks processing.
  * **udf1**: This parameter must contain the buyer's PAN (Permanent Account Number). If the transaction is of UPI mandate or UPI recurring then udf1 should contain the "Buyer's PAN and date of birth in the following format (separated by two pipe characters): Buyer's PAN||Buyer's DOB.
  * **udf3**: This parameter must contain the buyer's DOB. If the transaction is of UPI mandate or UPI recurring then udf3 should contain the "invoice ID of the transaction (generated by the merchant) and merchant name in the following format (separated by two pipe characters): InvoiceID||MerchantName" (where, MerchantName is required for PA2PA integrations only).
  * **udf4**: This parameter must contain the "MerchantName" passed in udf3 in case of PA2PA integration, for UPI mandate consent and recurring transaction, this parameter value should not be passed.
  * **udf5**: This parameter must contain the "invoiceId" for every merchant, this field is mandatory during or after the transaction (using the udf_update API post successful transaction).
</Callout>
