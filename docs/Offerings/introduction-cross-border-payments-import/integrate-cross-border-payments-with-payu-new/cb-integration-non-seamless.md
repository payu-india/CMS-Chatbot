---
title: '[Redirect] PayU Hosted Payment Integration - Cross Border Outward'
deprecated: false
hidden: true
metadata:
  robots: index
---
This section describes how to integrate Cross-Border Subscriptions with PayU Hosted Checkout integration using **_payment** API.

## Step 1: Post the Payment Request with PayU

For detailed information about the Payment Consent Transaction using PayU Hosted Checkout, refer to [PayU Hosted Checkout - CB](ref:_payment_cross-border_payu_hosted_checkout)

<Callout icon="📘" theme="info">
  **Note**: For Cross-Border Payments, the UDF parameters (udf1, udf2, udf3, udf4, and udf5) have specific requirements as described in the Request parameters table below.
</Callout>

## Request parameters

In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

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
        key<br /><code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> This parameter is the unique Merchant Key provided by PayU for your merchant account.
      </td>

      <td>
        Your Test Key
      </td>
    </tr>

    <tr>
      <td>
        txnid<br /><code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post a unique transaction ID for every new transaction. <code>Character limit</code>: 25<br /><strong>Note:</strong> Ensure this transaction ID hasn't been processed successfully before.
      </td>

      <td>
        fd3e847h2
      </td>
    </tr>

    <tr>
      <td>
        amount<br /><code>mandatory</code>
      </td>

      <td>
        <code>float</code> This parameter should contain the payment amount for the specific transaction.<br /><strong>Note:</strong> Typecast the amount to a float type. The amount can vary based on use cases:<br />• For Net Banking, 0 INR<br />• For Cards & UPI, a minimum of 1 INR (penny transactions)
      </td>

      <td>
        1000
      </td>
    </tr>

    <tr>
      <td>
        productinfo<br /><code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> A brief product description. Short information about the product/service. Character limit: 100
      </td>

      <td>
        Time Magazine Subscription
      </td>
    </tr>

    <tr>
      <td>
        email<br /><code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> Contains the email of the customer; highly recommended accuracy as fraud detection relies on this. Character limit: 50.
      </td>

      <td>
        [Ashish@test.com](mailto:Ashish@test.com)
      </td>
    </tr>

    <tr>
      <td>
        firstname<br /><code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> The customer's first name.<br />Character limit is 60.
      </td>

      <td>
        John
      </td>
    </tr>

    <tr>
      <td>
        lastname<br /><code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> The customer's middle & last name (wherever applicable).<br />Character limit is 60.
      </td>

      <td>
        Doe
      </td>
    </tr>

    <tr>
      <td>
        phone<br /><code>optional</code>
      </td>

      <td>
        <code>varchar</code> Customer phone number for fraud detection and user tracking. Character limit: 50.
      </td>

      <td>
        9843176540
      </td>
    </tr>

    <tr>
      <td>
        address1<br /><code>optional but recommended for higher approval rate</code>
      </td>

      <td>
        <code>varchar</code> The customer's primary billing address line. This field is required for billing and fraud prevention purposes. Character limit: 255.
      </td>

      <td>
        123 Main Street
      </td>
    </tr>

    <tr>
      <td>
        city<br /><code>optional but recommended for higher approval rate</code>
      </td>

      <td>
        <code>varchar</code> The customer's billing city. This field is required for billing and fraud prevention purposes. Character limit: 50.
      </td>

      <td>
        New Delhi
      </td>
    </tr>

    <tr>
      <td>
        state<br /><code>optional but recommended for higher approval rate</code>
      </td>

      <td>
        <code>varchar</code> The customer's billing state or province. This field is required for billing and fraud prevention purposes. Character limit: 50.
      </td>

      <td>
        Delhi
      </td>
    </tr>

    <tr>
      <td>
        country<br /><code>optional but recommended for higher approval rate</code>
      </td>

      <td>
        <code>varchar</code> The customer's billing country code. This field is required for billing and fraud prevention purposes. Use ISO 3166-1 alpha-2 country codes. Character limit: 2.
      </td>

      <td>
        India
      </td>
    </tr>

    <tr>
      <td>
        zipcode<br /><code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> The customer's billing postal/zip code. This field is required for billing and fraud prevention purposes. Character limit: 6 digit (India Zipcode)
      </td>

      <td>
        110075
      </td>
    </tr>

    <tr>
      <td>
        surl<br /><code>mandatory</code>
      </td>

      <td>
        <code>URL</code> The success URL to which PayU redirects after a successful transaction.
      </td>

      <td>
        [https://example.com/success](https://example.com/success)
      </td>
    </tr>

    <tr>
      <td>
        furl<br /><code>mandatory</code>
      </td>

      <td>
        <code>URL</code> The failure URL to which PayU redirects after a failed transaction.
      </td>

      <td>
        [https://example.com/failure](https://example.com/failure)
      </td>
    </tr>

    <tr>
      <td>
        udf1<br /><code>optional but recommended for higher approval rate</code>
      </td>

      <td>
        <code>String</code> The Permanent Account Number (PAN primary taxation ID in India) of the buyer must be collected in this field.

        Character limit: 10 character alphanumeric
      </td>

      <td>
        ABCDE1234K
      </td>
    </tr>

    <tr>
      <td>
        udf2<br /><code>optional</code>
      </td>

      <td>
        <code>String</code> User-defined field for storing transaction-specific data. Character limit: 255.
      </td>

      <td>
        Additional transaction data
      </td>
    </tr>

    <tr>
      <td>
        udf3<br /><code>optional but recommended for higher approval rate</code>
      </td>

      <td>
        <code>String</code> Date of Birth (DOB) of buyer in DD-MM-YYYY
      </td>

      <td>
        02-02-1980
      </td>
    </tr>

    <tr>
      <td>
        udf4<br /><code>mandatory<br /> for payment<br /> aggregators</code>
      </td>

      <td>
        <code>String</code> End merchant legal entity name. For UPI, this field should not be passed. Character limit: 255.
      </td>

      <td>
        XYZ Pvt. Ltd.
      </td>
    </tr>

    <tr>
      <td>
        udf5<br /><code>mandatory<br /> for cross-border<br /> payments</code>
      </td>

      <td>
        <code>String</code> Contains invoice ID for the merchant. Character limit: 255.
      </td>

      <td>
        INV123456
      </td>
    </tr>

    <tr>
      <td>
        buyer_type_business<br /><code>optional in case of B2B transaction<br /> for cross-border<br /> payments</code>
      </td>

      <td>
        <code>Binary</code> To be sent as "1" in case the buyer is a business. In case of individual buyers, it can be skipped. Default is "0".

        _Note: This will be included in hash if posted (covered in next section)_
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        udf_params<br /><code>optional</code>
      </td>

      <td>
        <code>String JSON</code>

        UDF7 value to capture "Import /Export Code" of the buyer

        UDF8 value to capture Airway Bill Number / Consignment Number (in case of goods imports)
      </td>

      <td>
        \{"udf7":"0100000029","udf8":"99953729071"}
      </td>
    </tr>

    <tr>
      <td>
        hash<br /><code>mandatory</code>
      </td>

      <td>
        <code>String</code> Crucial security parameter using SHA512 hash encryption. Formula incorporates key, txnid, amount, productinfo, firstname, email, udf fields, si_details, and merchant salt.
      </td>

      <td>
        \<Generated Hash>
      </td>
    </tr>
  </tbody>
</Table>

### Hashing

You must hash the request parameters using the following hash logic:

Parameters in the below sequence needs to be checked before generating the hash, if these params are being posted, it needs to be added in the hash calculation:
|additional_charges|miles|base_payuid|base_merchantid|paisa_mecode|subvention_amount|subvention_eligibility|merchant_data|payoutdetails|loan_id|twid_customer_hash|splitrequest|percentage_additional_charges|force_pa|udf_params|buyer_type_business

* **Case1 example**: Simple Hashing, if the merchant is not sending the api_version in the payment request, then it will be treated as hash sequence version 1.

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt
```

* **Case2 example**:  if the merchant is passing the additional_charges in the payment request then they have to append the additional_charges value in the raw hash sequence as below.

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt|additional_charges
```

**Case3 example**: If the merchant wants to pass additional_charges, buyer_type_business in the payment request, then hash formula for payment request will be:

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt|additional_charges|buyer_type_business
```

* **Case4 example**: if the merchant wants to pass the api_version = 7 and buyer_type_business, udf_params in the payment request.

```
* key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|si_details|salt|udf_params|buyer_type_business
```

For more information, refer to  <a href="generate-hash-merchant-hosted" target="_blank"> Generate Hash</a>.

<Accordion title="My Accordion Title" icon="fa-info-circle">
  <HashingSample />
</Accordion>

## Sample request

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


## Step 2: Check Response from PayU

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
