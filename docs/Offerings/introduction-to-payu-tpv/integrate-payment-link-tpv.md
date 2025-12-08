---
title: Integrate Payment Link TPV
deprecated: false
hidden: true
metadata:
  robots: index
---
This section describes the steps to integrate Payment Link TPV (Third Party Verification) - from payment link creation to payment processing.

> **Note**: Ensure your merchant account has `enableTpvFlow = "1"` enabled. Contact your PayU account manager if this configuration is not active.

<Cards columns={3}>
  <Card title="1. Create Payment Link" href="#step-1-create-payment-link">
    Create a payment link with beneficiary account details for TPV verification.
    <br />
  </Card>
  <Card title="2. Intermediate Page" href="#step-2-intermediate-page">
    Backend sends beneficiary details to prepayment page for customer visibility.
    <br />
  </Card>
  <Card title="3. Post Parameters to PayU" href="#step-3-post-parameters-to-payu">
    Backend converts data and posts to _payment API with api_version 20.
    <br />
  </Card>
  <Card title="4. Check Response from PayU" href="#step-4-check-response-from-payu">
    Check and handle the response received from PayU after payment processing.
    <br />
  </Card>
  <Card title="5. Verify the Payment" href="#step-5-verify-the-payment">
    Verify the payment status using webhooks or Verify Payments API.
    <br />
  </Card>
</Cards>


## Step 1: Create Payment Link

Create a payment link with beneficiary account details using the Create Payment Link API.

<Accordion title="Environment" icon="fa-globe">

| Environment | URL |
|-------------|-----|
| Test | `https://test.payu.in/paymentlink/create` |
| Production | `https://info.payu.in/paymentlink/create` |

</Accordion>

<Accordion title="Request Parameters" icon="fa-table">

| Parameter | Description | Example |
|-----------|-------------|---------|
| amount<br/>`mandatory` | `Decimal`<br/>The payment amount. | `5000.00` |
| maxPaymentsAllowed<br/>`mandatory` | `Integer`<br/>Must be 1 for TPV flow (single payment only). | `1` |
| invoiceNumber<br/>`mandatory` | `String`<br/>Unique invoice number for the payment link. | `INV123456789012` |
| description<br/>`optional` | `String`<br/>Description of the payment. | `Payment for services` |
| customerName<br/>`optional` | `String`<br/>Customer's name. | `John Doe` |
| customerEmail<br/>`optional` | `String`<br/>Customer's email address. | `john.doe@example.com` |
| customerPhone<br/>`optional` | `String`<br/>Customer's phone number. | `9876543210` |
| beneficiarydetail<br/>`optional` | `Object`<br/>Object containing beneficiary account details for TPV. | See below |
| source<br/>`optional` | `String`<br/>Source of the payment link creation. | `API` |

<Accordion title="beneficiarydetail Object Parameters" icon="fa-code">

| Parameter | Description | Example |
|-----------|-------------|---------|
| beneficiaryAccountNumber<br/>`mandatory` | `List<String>`<br/>Array of beneficiary account numbers. Maximum 4 accounts. | `["917732227242", "72522762"]` |
| ifscCode<br/>`mandatory` | `List<String>`<br/>Array of IFSC codes corresponding to each account number. | `["SBIN0007001", "HDFC0001234"]` |

</Accordion>

</Accordion>

<Accordion title="Sample Request" icon="fa-code">

```bash
curl --location 'https://test.payu.in/paymentlink/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access_token>' \
--data '{
    "amount": 5000.00,
    "maxPaymentsAllowed": 1,
    "invoiceNumber": "INV123456789012",
    "description": "Payment for services",
    "customerName": "John Doe",
    "customerEmail": "john.doe@example.com",
    "customerPhone": "9876543210",
    "beneficiarydetail": {
        "beneficiaryAccountNumber": ["917732227242", "72522762"],
        "ifscCode": ["SBIN0007001", "HDFC0001234"]
    },
    "source": "API"
}'
```
```python
import requests
import json

url = "https://test.payu.in/paymentlink/create"

payload = {
    "amount": 5000.00,
    "maxPaymentsAllowed": 1,
    "invoiceNumber": "INV123456789012",
    "description": "Payment for services",
    "customerName": "John Doe",
    "customerEmail": "john.doe@example.com",
    "customerPhone": "9876543210",
    "beneficiarydetail": {
        "beneficiaryAccountNumber": ["917732227242", "72522762"],
        "ifscCode": ["SBIN0007001", "HDFC0001234"]
    },
    "source": "API"
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <access_token>"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        using var client = new HttpClient();
        
        var payload = @"{
            ""amount"": 5000.00,
            ""maxPaymentsAllowed"": 1,
            ""invoiceNumber"": ""INV123456789012"",
            ""description"": ""Payment for services"",
            ""customerName"": ""John Doe"",
            ""customerEmail"": ""john.doe@example.com"",
            ""customerPhone"": ""9876543210"",
            ""beneficiarydetail"": {
                ""beneficiaryAccountNumber"": [""917732227242"", ""72522762""],
                ""ifscCode"": [""SBIN0007001"", ""HDFC0001234""]
            },
            ""source"": ""API""
        }";
        
        var content = new StringContent(payload, Encoding.UTF8, "application/json");
        client.DefaultRequestHeaders.Add("Authorization", "Bearer <access_token>");
        
        var response = await client.PostAsync("https://test.payu.in/paymentlink/create", content);
        var result = await response.Content.ReadAsStringAsync();
        Console.WriteLine(result);
    }
}
```
```javascript
const createPaymentLinkTPV = async () => {
    const url = "https://test.payu.in/paymentlink/create";
    
    const payload = {
        amount: 5000.00,
        maxPaymentsAllowed: 1,
        invoiceNumber: "INV123456789012",
        description: "Payment for services",
        customerName: "John Doe",
        customerEmail: "john.doe@example.com",
        customerPhone: "9876543210",
        beneficiarydetail: {
            beneficiaryAccountNumber: ["917732227242", "72522762"],
            ifscCode: ["SBIN0007001", "HDFC0001234"]
        },
        source: "API"
    };
    
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer <access_token>"
        },
        body: JSON.stringify(payload)
    });
    
    const data = await response.json();
    console.log(data);
};

createPaymentLinkTPV();
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class CreatePaymentLinkTPV {
    public static void main(String[] args) throws Exception {
        String url = "https://test.payu.in/paymentlink/create";
        
        String payload = "{"
            + "\"amount\": 5000.00,"
            + "\"maxPaymentsAllowed\": 1,"
            + "\"invoiceNumber\": \"INV123456789012\","
            + "\"description\": \"Payment for services\","
            + "\"customerName\": \"John Doe\","
            + "\"customerEmail\": \"john.doe@example.com\","
            + "\"customerPhone\": \"9876543210\","
            + "\"beneficiarydetail\": {"
            + "\"beneficiaryAccountNumber\": [\"917732227242\", \"72522762\"],"
            + "\"ifscCode\": [\"SBIN0007001\", \"HDFC0001234\"]"
            + "},"
            + "\"source\": \"API\""
            + "}";
        
        HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("Authorization", "Bearer <access_token>");
        conn.setDoOutput(true);
        
        try (OutputStream os = conn.getOutputStream()) {
            os.write(payload.getBytes(StandardCharsets.UTF_8));
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
$url = "https://test.payu.in/paymentlink/create";

$payload = array(
    "amount" => 5000.00,
    "maxPaymentsAllowed" => 1,
    "invoiceNumber" => "INV123456789012",
    "description" => "Payment for services",
    "customerName" => "John Doe",
    "customerEmail" => "john.doe@example.com",
    "customerPhone" => "9876543210",
    "beneficiarydetail" => array(
        "beneficiaryAccountNumber" => array("917732227242", "72522762"),
        "ifscCode" => array("SBIN0007001", "HDFC0001234")
    ),
    "source" => "API"
);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    "Content-Type: application/json",
    "Authorization: Bearer <access_token>"
));

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```

</Accordion>

<Accordion title="Sample Response" icon="fa-check">

```json
{
    "status": "SUCCESS",
    "data": {
        "invoiceNumber": "INV123456789012",
        "amount": 5000.00,
        "beneficiarydetail": {
            "beneficiaryAccountNumber": ["917732227242", "72522762"],
            "ifscCode": ["SBIN0007001", "HDFC0001234"]
        }
    }
}
```

</Accordion>

---

## Step 2: Intermediate Page

When the customer accesses the payment link, the backend sends beneficiary details to the prepayment page.

<Accordion title="Endpoint" icon="fa-globe">

**Endpoint**: `GET /pay/{id}/intermediate`

The backend retrieves the payment link details including beneficiary information and sends it to the prepayment/checkout page.

</Accordion>

<Accordion title="Data Format" icon="fa-code">

The beneficiary details are sent in **list format** (same as the create payment link format):

```json
{
    "beneficiarydetail": {
        "beneficiaryAccountNumber": ["917732227242", "72522762", "283228235"],
        "ifscCode": ["SBIN0007001", "HDFC0001234", "ICIC0002522"]
    }
}
```

> **Note**: The frontend displays these beneficiary accounts on the checkout page for customer visibility.

</Accordion>

<Accordion title="Sample Response" icon="fa-check">

```json
{
    "status": "SUCCESS",
    "data": {
        "invoiceNumber": "INV123456789012",
        "amount": 5000.00,
        "beneficiarydetail": {
            "beneficiaryAccountNumber": ["917732227242", "72522762"],
            "ifscCode": ["SBIN0007001", "HDFC0001234"]
        }
    }
}
```

</Accordion>

---

## Step 3: Post Parameters to PayU

When the customer initiates payment, the backend converts beneficiary details to pipe-separated format and posts to the `_payment` API.

<Accordion title="Environment" icon="fa-globe">

| Environment | URL |
|-------------|-----|
| Test | `https://test.payu.in/_payment` |
| Production | `https://secure.payu.in/_payment` |

</Accordion>

<Accordion title="Data Conversion" icon="fa-exchange">

**Conversion Logic:**

| Stage | Format |
|-------|--------|
| Input | Lists from database (same format as create payment link) |
| Processing | Join each list with pipe separator (`\|`) |
| Output | Pipe-separated strings in JSON object |

**Before Conversion (List Format):**

```json
{
    "beneficiarydetail": {
        "beneficiaryAccountNumber": ["917732227242", "72522762"],
        "ifscCode": ["SBIN0007001", "HDFC0001234"]
    }
}
```

**After Conversion (Pipe-Separated Format):**

```json
{
    "beneficiarydetail": {
        "beneficiaryAccountNumber": "917732227242|72522762",
        "ifscCode": "SBIN0007001|HDFC0001234"
    },
    "api_version": 20
}
```

</Accordion>

<Accordion title="Request Parameters" icon="fa-table">

| Parameter | Description | Example |
|-----------|-------------|---------|
| key<br/>`mandatory` | `String`<br/>Merchant key provided by PayU. | `JP***g` |
| txnid<br/>`mandatory` | `String`<br/>Unique transaction ID generated by you. | `TtEmKjWF2uGliF` |
| amount<br/>`mandatory` | `String`<br/>Payment amount. | `5000.00` |
| productinfo<br/>`mandatory` | `String`<br/>Brief description of the product or service. | `Payment for services` |
| firstname<br/>`mandatory` | `String`<br/>Customer's first name. | `John` |
| email<br/>`mandatory` | `String`<br/>Customer's email address. | `john.doe@example.com` |
| phone<br/>`mandatory` | `String`<br/>Customer's phone number. | `9876543210` |
| surl<br/>`mandatory` | `String`<br/>Success URL where PayU redirects after successful payment. | `https://yoursite.com/success` |
| furl<br/>`mandatory` | `String`<br/>Failure URL where PayU redirects after failed payment. | `https://yoursite.com/failure` |
| beneficiarydetail<br/>`mandatory` | `JSON String`<br/>JSON object with pipe-separated beneficiary account numbers and IFSC codes. Up to 4 accounts supported. | `{"beneficiaryAccountNumber":"917732227242\|72522762","ifscCode":"SBIN0007001\|HDFC0001234"}` |
| api_version<br/>`mandatory` | `Integer`<br/>Must be set to 20 when beneficiary details are present. | `20` |
| hash<br/>`mandatory` | `String`<br/>Hash calculated using the checksum logic. | `<generated_hash>` |
| udf1 - udf5<br/>`optional` | `String`<br/>User-defined fields for storing additional information. | ` ` |

</Accordion>

<Accordion title="Hash Generation" icon="fa-lock">

The hash is generated using the following format:

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT
```

Where `beneficiarydetail` is the JSON string representation with pipe-separated values:

```json
{"beneficiaryAccountNumber":"917732227242|72522762","ifscCode":"SBIN0007001|HDFC0001234"}
```

> **Note**: The `beneficiarydetail` parameter value will be the last value to be appended before SALT.

</Accordion>

<Accordion title="Sample Request" icon="fa-code">

```bash
curl --location 'https://test.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=JP***g' \
--data-urlencode 'txnid=TtEmKjWF2uGliF' \
--data-urlencode 'amount=5000.00' \
--data-urlencode 'productinfo=Payment for services' \
--data-urlencode 'firstname=John' \
--data-urlencode 'email=john.doe@example.com' \
--data-urlencode 'phone=9876543210' \
--data-urlencode 'surl=https://yoursite.com/success' \
--data-urlencode 'furl=https://yoursite.com/failure' \
--data-urlencode 'beneficiarydetail={"beneficiaryAccountNumber":"917732227242|72522762","ifscCode":"SBIN0007001|HDFC0001234"}' \
--data-urlencode 'api_version=20' \
--data-urlencode 'hash=<generated_hash>'
```

```python
import requests

url = "https://test.payu.in/_payment"

payload = {
    "key": "JP***g",
    "txnid": "TtEmKjWF2uGliF",
    "amount": "5000.00",
    "productinfo": "Payment for services",
    "firstname": "John",
    "email": "john.doe@example.com",
    "phone": "9876543210",
    "surl": "https://yoursite.com/success",
    "furl": "https://yoursite.com/failure",
    "beneficiarydetail": '{"beneficiaryAccountNumber":"917732227242|72522762","ifscCode":"SBIN0007001|HDFC0001234"}',
    "api_version": "20",
    "hash": "<generated_hash>"
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(url, data=payload, headers=headers)
print(response.text)
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
            new KeyValuePair<string, string>("key", "JP***g"),
            new KeyValuePair<string, string>("txnid", "TtEmKjWF2uGliF"),
            new KeyValuePair<string, string>("amount", "5000.00"),
            new KeyValuePair<string, string>("productinfo", "Payment for services"),
            new KeyValuePair<string, string>("firstname", "John"),
            new KeyValuePair<string, string>("email", "john.doe@example.com"),
            new KeyValuePair<string, string>("phone", "9876543210"),
            new KeyValuePair<string, string>("surl", "https://yoursite.com/success"),
            new KeyValuePair<string, string>("furl", "https://yoursite.com/failure"),
            new KeyValuePair<string, string>("beneficiarydetail", "{\"beneficiaryAccountNumber\":\"917732227242|72522762\",\"ifscCode\":\"SBIN0007001|HDFC0001234\"}"),
            new KeyValuePair<string, string>("api_version", "20"),
            new KeyValuePair<string, string>("hash", "<generated_hash>")
        });
        
        var response = await client.PostAsync("https://test.payu.in/_payment", content);
        var result = await response.Content.ReadAsStringAsync();
        Console.WriteLine(result);
    }
}
```

```javascript
const postPaymentTPV = async () => {
    const url = "https://test.payu.in/_payment";
    
    const params = new URLSearchParams();
    params.append("key", "JP***g");
    params.append("txnid", "TtEmKjWF2uGliF");
    params.append("amount", "5000.00");
    params.append("productinfo", "Payment for services");
    params.append("firstname", "John");
    params.append("email", "john.doe@example.com");
    params.append("phone", "9876543210");
    params.append("surl", "https://yoursite.com/success");
    params.append("furl", "https://yoursite.com/failure");
    params.append("beneficiarydetail", JSON.stringify({
        beneficiaryAccountNumber: "917732227242|72522762",
        ifscCode: "SBIN0007001|HDFC0001234"
    }));
    params.append("api_version", "20");
    params.append("hash", "<generated_hash>");
    
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: params
    });
    
    const data = await response.text();
    console.log(data);
};

postPaymentTPV();
```

```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class PaymentLinkTPV {
    public static void main(String[] args) throws Exception {
        String url = "https://test.payu.in/_payment";
        
        String beneficiarydetail = URLEncoder.encode("{\"beneficiaryAccountNumber\":\"917732227242|72522762\",\"ifscCode\":\"SBIN0007001|HDFC0001234\"}", StandardCharsets.UTF_8);
        
        String params = "key=JP***g"
            + "&txnid=TtEmKjWF2uGliF"
            + "&amount=5000.00"
            + "&productinfo=Payment+for+services"
            + "&firstname=John"
            + "&email=john.doe@example.com"
            + "&phone=9876543210"
            + "&surl=https://yoursite.com/success"
            + "&furl=https://yoursite.com/failure"
            + "&beneficiarydetail=" + beneficiarydetail
            + "&api_version=20"
            + "&hash=<generated_hash>";
        
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
$url = "https://test.payu.in/_payment";

$data = array(
    "key" => "JP***g",
    "txnid" => "TtEmKjWF2uGliF",
    "amount" => "5000.00",
    "productinfo" => "Payment for services",
    "firstname" => "John",
    "email" => "john.doe@example.com",
    "phone" => "9876543210",
    "surl" => "https://yoursite.com/success",
    "furl" => "https://yoursite.com/failure",
    "beneficiarydetail" => json_encode(array(
        "beneficiaryAccountNumber" => "917732227242|72522762",
        "ifscCode" => "SBIN0007001|HDFC0001234"
    )),
    "api_version" => "20",
    "hash" => "<generated_hash>"
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

---

## Step 4: Check Response from PayU

After the payment is processed, PayU sends a response to your success or failure URL. You must validate the hash and handle the response accordingly.

<Accordion title="Hash Validation (Reverse Hashing)" icon="fa-lock">

While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure.

The order of the parameters for reverse hashing:

```
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

> **Important**: The `beneficiarydetail` parameter should **NOT** be present in reverse hashing.

</Accordion>

<Accordion title="Response Parameters" icon="fa-table">

| Parameter | Description | Example |
|-----------|-------------|---------|
| mihpayid | `String`<br/>Unique reference number created for each transaction at PayU's end. Store this for future actions like Inquiry or Refund. | `403993715524308236` |
| mode | `String`<br/>The payment mode used by the customer. | `NB` |
| status | `String`<br/>Status of the transaction. Possible values: `success`, `failure`, `pending`. Only `success` should be treated as successful. | `success` |
| unmappedstatus | `String`<br/>Detailed status of the transaction. | `captured` |
| key | `String`<br/>The merchant key used for the transaction. | `JP***g` |
| txnid | `String`<br/>The transaction ID posted by the merchant during the transaction request. | `TtEmKjWF2uGliF` |
| amount | `String`<br/>The transaction amount. | `5000.00` |
| discount | `String`<br/>The discount amount given by bank on the transaction fee (if any). | `0.00` |
| net_amount_debit | `String`<br/>The net amount debited from the customer's account. | `5000` |
| addedon | `String`<br/>The transaction timestamp. | `2021-10-05 12:44:06` |
| productinfo | `String`<br/>Product information as sent in the request. | `Payment for services` |
| firstname | `String`<br/>Customer's first name. | `John` |
| email | `String`<br/>Customer's email address. | `john.doe@example.com` |
| phone | `String`<br/>Customer's phone number. | `9876543210` |
| hash | `String`<br/>Hash for response validation (reverse hash). | `<hash_value>` |
| field9 | `String`<br/>Transaction message from the bank. | `Transaction Completed Successfully` |
| PG_TYPE | `String`<br/>The payment gateway type used. | `NB-PG` |
| bank_ref_num | `String`<br/>Bank reference number for the transaction. | `30646df4-69b7-43f4-acdd-21e6a593c037` |
| bankcode | `String`<br/>Bank code used for the transaction. | `TESTPGNB` |
| error | `String`<br/>Error code. `E000` indicates no error. | `E000` |
| error_Message | `String`<br/>Error message description. | `No Error` |
| udf1 - udf5 | `String`<br/>User-defined fields as sent in the request. | ` ` |

</Accordion>

<Accordion title="Sample Response" icon="fa-check">

```php
Array
(
    [mihpayid] => 403993715524308236
    [mode] => NB
    [status] => success
    [unmappedstatus] => captured
    [key] => JP***g
    [txnid] => TtEmKjWF2uGliF
    [amount] => 5000.00
    [discount] => 0.00
    [net_amount_debit] => 5000
    [addedon] => 2021-10-05 12:44:06
    [productinfo] => Payment for services
    [firstname] => John
    [lastname] => Doe
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => 
    [zipcode] => 
    [email] => john.doe@example.com
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
    [hash] => 74d1039311528b4a7b699db7ce195d6a219d7442271dedb23e516e29490ec743a89c12448698178907e03d32fa05e8178694db8037bc0be53380099e47c3d63f
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
    [PG_TYPE] => NB-PG
    [bank_ref_num] => 30646df4-69b7-43f4-acdd-21e6a593c037
    [bankcode] => TESTPGNB
    [error] => E000
    [error_Message] => No Error
)
```

> **Important**: Store the `mihpayid` and `txnid` parameter values in your server as proof that TPV has been completed for a customer.

</Accordion>

---

## Step 5: Verify the Payment

Upon receiving the response, PayU recommends performing a reconciliation step to validate all transaction details. You can verify your payments using either of the following methods:

<Accordion title="Verify using Webhooks" icon="fa-bell">

Configure webhooks to monitor the status of payments. Webhooks enable a server to communicate with another server by sending an HTTP callback or message. These callbacks are triggered by specific events and operate at the server-to-server (S2S) level.

**Benefits of using Webhooks:**
- Real-time notification of payment status changes
- Server-to-server communication (more reliable than browser redirects)
- Automatic retry mechanism for failed deliveries

👉 For more details, refer to [Webhooks for Payments](https://docs.payu.in/docs/webhooks-for-payments).

</Accordion>

<Accordion title="Verify using Verify Payments API" icon="fa-check-circle">

Use the Verify Payments API to check the status of a transaction programmatically.

**Sample Request:**

```bash
curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=JP***g' \
--data-urlencode 'command=verify_payment' \
--data-urlencode 'var1=TtEmKjWF2uGliF' \
--data-urlencode 'hash=<generated_hash>'
```

**Hash Generation for Verify Payment:**

```
sha512(key|command|var1|SALT)
```

👉 For more details, refer to [Verify Payments API](https://docs.payu.in/reference/verify-payment-api).

</Accordion>

---

## Validation Rules

| Validation | Rule | Error Code |
|------------|------|------------|
| Merchant TPV Enabled | enableTpvFlow = "1" | 427 |
| Max Payments | maxPaymentsAllowed = 1 | 400 |
| Max Beneficiaries | ≤ 4 beneficiaries | 400 |
| Equal Count | Account numbers = IFSC codes count | 400 |
| Account Format | Alphanumeric, max 50 chars | 400 |
| IFSC Format | Exactly 11 chars: `[A-Z]{4}0[A-Z0-9]{6}` | 400 |

