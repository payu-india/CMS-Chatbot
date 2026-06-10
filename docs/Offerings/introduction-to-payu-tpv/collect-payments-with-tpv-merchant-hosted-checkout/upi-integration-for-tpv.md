---
title: UPI Integration - TPV
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  title: UPI TPV Integration - Merchant Hosted Checkout
  description: >-
    Discover how to integrate UPI with Third Party Validation (TPV) using PayU's
    detailed guide. This documentation offers step-by-step instructions, API
    specifications, and best practices for efficient and secure payment
    processing. Streamline your online payment solutions with seamless UPI
    integration.
  keywords:
    - UPI Integration for TPV
    - ' Third Party Validation UPI Integration'
    - API Integration for UPI TPV
    - ' PayU UPI TPV Integration'
    - TPV UPI Setup Guide
  robots: index
---
Integrate TPV through UPI using the procedure described in this section.

## Prerequisites

Merchant Hosted or S2S (Seamless) integration has to be done as per the standard kit. For more information, refer to  [UPI Integration](doc:collect-payments-with-upi-seamless).

## Step 1: Validate VPA

When your customer makes payment through UPI, you can validate the customer’s Virtual Payment Address (VPA) and then initiate payment. The **validateVpa** API is used to validate the UPI handle. Validate the VPA (UPI handle) using the **validateVpa** API. For Try-It experience, refer to [Validate VPA Handle API](ref:validate_vpa_api).

<Accordion title="Sample request" icon="fa-code">
  **Validate VPA**

  <Validate_VPA />

  **Validate VPA for Recurring Payment**
```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g" \
  -d "command=validateVPA" \
  -d "var1=9999999999@upi" \
  -d "var2={\"validateAutoPayVPA\":\"1\"}" \
  -d "hash=75uy573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472poy9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e"
```
```python
import requests
import json

url = "https://test.payu.in/merchant/postservice"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

var2_json = json.dumps({"validateAutoPayVPA": "1"})

data = {
    "key": "JP***g",
    "command": "validateVPA",
    "var1": "9999999999@upi",
    "var2": var2_json,
    "hash": "75uy573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472poy9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e"
}

response = requests.post(url, headers=headers, data=data, params={"form": "2"})

print("Status Code:", response.status_code)
print("Response:", response.json())
```
```java
import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class ValidateAutoPayVPA {
    public static void main(String[] args) throws IOException, InterruptedException {
        String url = "https://test.payu.in/merchant/postservice?form=2";
        
        String var2Json = "{\"validateAutoPayVPA\":\"1\"}";
        
        Map<String, String> params = new HashMap<>();
        params.put("key", "JP***g");
        params.put("command", "validateVPA");
        params.put("var1", "9999999999@upi");
        params.put("var2", var2Json);
        params.put("hash", "75uy573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472poy9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e");
        
        String formData = params.entrySet().stream()
            .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "=" 
                    + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
            .collect(Collectors.joining("&"));
        
        HttpClient client = HttpClient.newHttpClient();
        
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("accept", "application/json")
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formData))
            .build();
        
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```
```javascript
const axios = require('axios');
const qs = require('qs');

const url = 'https://test.payu.in/merchant/postservice?form=2';

const var2Json = JSON.stringify({ validateAutoPayVPA: '1' });

const data = {
    key: 'JP***g',
    command: 'validateVPA',
    var1: '9999999999@upi',
    var2: var2Json,
    hash: '75uy573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472poy9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e'
};

const config = {
    headers: {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
};

axios.post(url, qs.stringify(data), config)
    .then(response => {
        console.log('Status Code:', response.status);
        console.log('Response:', response.data);
    })
    .catch(error => {
        console.error('Error:', error.response ? error.response.data : error.message);
    });
```
```php
<?php

$url = "https://test.payu.in/merchant/postservice?form=2";

$var2Json = json_encode(array('validateAutoPayVPA' => '1'));

$data = array(
    'key' => 'JP***g',
    'command' => 'validateVPA',
    'var1' => '9999999999@upi',
    'var2' => $var2Json,
    'hash' => '75uy573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472poy9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e'
);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'accept: application/json',
    'Content-Type: application/x-www-form-urlencoded'
));

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";

$jsonResponse = json_decode($response, true);
print_r($jsonResponse);
?>
```
```perl
#!/usr/bin/perl
use strict;
use warnings;
use LWP::UserAgent;
use HTTP::Request::Common;
use JSON;

my $url = "https://test.payu.in/merchant/postservice?form=2";

my $var2_json = encode_json({ validateAutoPayVPA => '1' });

my %data = (
    key     => 'JP***g',
    command => 'validateVPA',
    var1    => '9999999999@upi',
    var2    => $var2_json,
    hash    => '75uy573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472poy9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e'
);

my $ua = LWP::UserAgent->new;
$ua->timeout(30);

my $response = $ua->post($url, 
    Content_Type => 'application/x-www-form-urlencoded',
    Content => \%data
);

if ($response->is_success) {
    print "Status Code: " . $response->code . "\n";
    print "Response: " . $response->decoded_content . "\n";
} else {
    print "Error: " . $response->status_line . "\n";
}
```

</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  **Success scenario**

  if successfully validated:

  ```plaintext
  {
     "status":"SUCCESS",
     "vpa":"9999999999@upi",
     "isVPAValid":1,
     "isAutoPayVPAValid":1,
     "isAutoPayBankValid":"NA",
     "payerAccountName":"ABC"
  }
  ```

  > 📘 Notes:
  >
  > * The **payerAccountName** parameter can be empty or NA or will have a payer name based on the value given by the bank.
  > * If both **isVPAValid** and **isAutoPayVPAValid** is 1, you must initiate payment for Recurring Payments.
  > * Ignore the **isAutoPayBankValid** parameter in the response.

  **Failure scenarios**

  * If invalid VPA, the response is similar to the following:

  ```plaintext
  {
   "status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"payerAccountName":"NA"
  }  
  ```

  * Invalid VPA but handle supporting SI (Autopay):

  ```plaintext
  {
   "status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"isAutoPayVPAValid":1,"isAutoPayBankValid":"NA","payerAccountName":"NA"
  }
  ```

  * Customer valid but handle not supporting SI (Autopay):

  ```plaintext
  {
    "status":"SUCCESS","vpa":"xyz@freecharge","isVPAValid":1,"isAutoPayVPAValid":0,"isAutoPayBankValid":"NA","payerAccountName":"XYZ"
  }
  ```

  * Neither customer valid nor handle supporting Autopay:

  ```plaintext
  {
    "status":"SUCCESS","vpa":"xyz@freecharge","isVPAValid":0,"isAutoPayVPAValid":0,"isAutoPayBankValid":"NA","payerAccountName":"NA"
  }
  ```
</Accordion>

## Step 2: Post the request to PayU

With the following parameters, make the transaction request with the customer’s bank account number to the PayU using the Collect Payment (**_payment**) API.

**Environment**

|                            |                                                                        |
| -------------------------- | ---------------------------------------------------------------------- |
| **Test Environment**       | [https://test.payu.in/_payment>](https://test.payu.in/_payment%3E)     |
| **Production Environment** | [https://secure.payu.in/_payment>](https://secure.payu.in/_payment%3E) |

<Accordion title="Request parameters" icon="fa-table">
  <HTMLBlock>{`
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
                  </thead>

                  <tbody>
                      <td>
                        key<br/>
                        <code>mandatory</code>
                      </td>

                      <td>
                        <code>String</code> Merchant key provided by PayU during onboarding.
                      </td>

                      <td>
                        JPg***r
                      </td>
                    </tr>
                    
                    <tr>
                      <td>
                        txnid<br/>
                        <code>mandatory</code>
                      </td>

                      <td>
                        <code>String</code> The transaction ID is a reference number for a specific order that is generated by the merchant.
                      </td>

                      <td>
                        ypl938459435
                      </td>
                    </tr>
                    <tr>
                      <td>
                        amount<br/>
                        <code>mandatory</code>
                      </td>

                      <td>
                        <code>String</code> The payment amount for the transaction.
                      </td>

                      <td>
                        10.00
                      </td>
                    </tr>

                    <tr>
                      <td>
                        productinfo<br/>
                        <code>mandatory</code>
                      </td>

                      <td>
                        <code>String</code> A brief description of the product.
                      </td>

                      <td>
                        iPhone
                      </td>
                    </tr>

                    <tr>
                      <td>
                        firstname<br/>
                        <code>mandatory</code>
                      </td>

                      <td>
                        <code>String</code> The first name of the customer.
                      </td>

                      <td>
                        Ashish
                      </td>
                    </tr>

                    <tr>
                      <td>
                        email<br/>
                        <code>mandatory</code>
                      </td>

                      <td>
                        <code>String</code> The email address of the customer.
                      </td>

                      <td>
                        [abc@payu.in](mailto:abc@payu.in)
                      </td>
                    </tr>

                    <tr>
                      <td>
                        phone<br/>
                        <code>mandatory</code>
                      </td>

                      <td>
                        <code>String</code> The phone number of the customer.
                      </td>

                      <td>

                      </td>
                    </tr>

                    <tr>
                      <td>
                        <Glossary>pg</Glossary><br/>
                        <code>mandatory</code>
                      </td>

                      <td>
                        <code>String</code> It defines the payment category for which you wish to perform TPV. For Net Banking, pg= 'UPI'.
                      </td>

                      <td>
                        UPI
                      </td>
                    </tr>

                    <tr>
                      <td>
                        <Glossary>bankcode</Glossary><br/>
                        <code>mandatory</code>
                      </td>

                      <td>
                       <code>String</code> It defines the bank with which you wish to perform TPV using the bank code. The values can be any one of the following values:
                  <ul>
                    <li><strong>UPITPV</strong>: Used for UPI Collect</li>
                    <li><strong>INTTPV</strong>: Used for UPI Intent</li>
                    <li><strong>TEJTPV</strong>: Used for Google Pay in app transactions only</li>
                        </ul>
                      </td>

                      <td>
                        UPI
                      </td>
                    </tr>

                    <tr>
                      <td>
                        vpa<br/>
                        <code>mandatory</code>
                      </td>

                      <td>
                        <code>String</code> The VPA or UPI handle of the customer.
                      </td>

                      <td>

                      </td>
                    </tr>

                    <tr>
                      <td>
                        beneficiarydetail<br/>
                        <code>mandatory</code>
                      </td>

                      <td>
                <code>JSON</code> This is a JSON format text and there should be key named **beneficiaryAccountNumber** with the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter.
                      </td>

                      <td>
                        Refer to beneficiarydetail JSON object fields section below the table</a>
                      </td>
                    </tr>

                    <tr>
                      <td>
                        api_version
                      </td>

                      <td>
                        <code>String</code> The api_version "6" must be passed fro this parameter.
                      </td>

                      <td>

                      </td>
                    </tr>

                    <tr>
                      <td>
                        furl<br/>
                        <code>mandatory</code>
                      </td>

                      <td>
                        <code>String</code> The success URL, which is the page PayU will redirect to if the transaction is successful.
                      </td>

                      <td>

                      </td>
                    </tr>

                    <tr>
                      <td>
                        surl<br/>
                        <code>mandatory</code>
                      </td>

                      <td>
                        <code>String</code> The Failure URL, which is the page PayU will redirect to if the transaction is failed.
                      </td>

                      <td>

                      </td>
                    </tr>

                    <tr>
                      <td>
                        hash<br/>
                        <code>mandatory</code>
                      </td>

                      <td>
                        <code>String</code> It is the hash calculated by the merchant. The hash calculation logic is:<br/>
                        <code>sha512(key|txnid|amount|productinfo|<br/>firstname|email|udf1|udf2|udf3|udf4|<br/>udf5|||||SALT)</code>
                      </td>

                      <td>

                      </td>
                    </tr>

                    <tr>
                      <td>
                        address1<br/>
                        <code>optional</code>
                      </td>

                      <td>
                        <code>String</code> The first line of the billing address.

                        * *For Fraud Detection*\*: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is required to provide the correct information.
                      </td>

                      <td>

                      </td>
                    </tr>

                    <tr>
                      <td>
                        address2<br/>
                        <code>optional</code>
                      </td>

                      <td>
                        <code>String</code> The second line of the billing address.
                      </td>

                      <td>

                      </td>
                    </tr>

                    <tr>
                      <td>
                        city<br/>
                        <code>optional</code>
                      </td>

                      <td>
                        <code>String</code> The city where your customer resides as part of the billing address.
                      </td>

                      <td>

                      </td>
                    </tr>

                    <tr>
                      <td>
                        state<br/>
                        <code>optional</code>
                      </td>

                      <td>
                        <code>String</code> The state where your customer resides as part of the billing address,
                      </td>

                      <td>

                      </td>
                    </tr>

                    <tr>
                      <td>
                        country<br/>
                        <code>optional</code>
                      </td>

                      <td>
                        <code>String</code> The country where your customer resides.
                      </td>

                      <td>

                      </td>
                    </tr>

                    <tr>
                      <td>
                        zipcode<br/>
                        <code>optional</code>
                      </td>

                      <td>
                        <code>String</code> Billing address zip code is mandatory for the cardless EMI option.<br/>
                        <code>Character Limit</code>-20
                      </td>

                      <td>

                      </td>
                    </tr>

                    <tr>
                      <td>
                        udf1<br/>
                        <code>optional</code>
                      </td>

                      <td>
                        <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
                      </td>

                      <td>

                      </td>
                    </tr>

                    <tr>
                      <td>
                        udf2<br/>
                        <code>optional</code>
                      </td>

                      <td>
                        <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
                      </td>

                      <td>

                      </td>
                    </tr>

                    <tr>
                      <td>
                        udf3<br/>
                        <code>optional</code>
                      </td>

                      <td>
                        <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.
                      </td>

                      <td>

                      </td>
                    </tr>

                    <tr>
                      <td>
                        udf4<br/>
                        <code>optional</code>
                      </td>

                      <td>
                        <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.
                      </td>

                      <td>

                      </td>
                    </tr>

                    <tr>
                      <td>
                        udf5<br/>
                        <code>optional</code>
                      </td>

                      <td>
                        <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.
                      </td>

                      <td>

                      </td>
                    </tr>
                  </tbody>
                </Table>
  `}</HTMLBlock>

  <Accordion title="beneficiarydetail JSON object fields" icon="fa-code">
    It must contain the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter. For example:

    ```
    {"beneficiaryAccountNumber":"002001600674|00000031957292212|00000035955239352|00000035955239352",  
    "ifscCode":"KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"}
    ```
  </Accordion>

  <Accordion title="Checksum Logic for Hash" icon="fa-code">
    The following hash logic must be used for the parameters posted:

    > 📘 beneficiarydetail parameter in Hashing:
    >
    > The **beneficiarydetail** parameter value will be at last or the last value to be appended.
    >
    > ```plaintext
    > key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3
    > |udf4|udf5||||||beneficiarydetail|SALT
    > ```
  </Accordion>
</Accordion>

## Step 3: Check the response from PayU

<Accordion title="Hash Validation Logic for Payment Response (Reverse Hashing)" icon="fa-code">
  While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure. This is to make sure the transaction has not tampered within the response.

  The order of the parameters is similar to the following code block:

  ```
  sha512(SALT|beneficiarydetail|status||||||udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```
</Accordion>

> 📘 Store the mihpayid and txnid parameter values in response:
>
> PayU recommends you to make provisions to store the **mihpayid** and **txnid** parameter values (in the response) in your server as proof that TPV has been completed for a customer.

<Accordion title="Sample response" icon="fa-code">
  The formatted response from PayU:

  ```
  Array
  (
      [mihpayid] => 403993715524308315
      [mode] => UPI
      [status] => success
      [unmappedstatus] => captured
      [key] => JP***g
      [txnid] => Job7NydtwPVAmy
      [amount] => 10.00
      [discount] => 0.00
      [net_amount_debit] => 10
      [addedon] => 2021-10-05 12:51:20
      [productinfo] => iPhone
      [firstname] => Ashish
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => test@gmail.com
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
      [hash] => de4f82af65458c84080d6515c1a80d42af703be390346ef020974e520efeb4ab9ebe4752e63e70d6f00dedd671c663dfdb22d0f0c818c52790e911e8babd3f6e
      [field1] => anything@payu
      [field2] => Job7NydtwPVAmy
      [field3] => 
      [field4] => Ashish
      [field5] => AXImAH1BxekGdTLY7qgjMXffAAjJj5Q75mY
      [field6] => 
      [field7] => Transaction completed successfully
      [field8] => 
      [field9] => Transaction completed successfully
      [payment_source] => payu
      [PG_TYPE] => UPI-PG
      [bank_ref_num] => Job7NydtwPVAmy
      [bankcode] => UPI
      [error] => E000
      [error_Message] => No Error
  )

  ```
</Accordion>

## Step 4. Verify the payment

<Verify_Payment_Tabs />