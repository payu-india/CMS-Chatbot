---
title: Integrate Payment Link TPV
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Integrate Payment Link TPV
deprecated: false
hidden: true
metadata:
  robots: index
---
This section describes the steps to integrate Payment Link <Glossary>TPV</Glossary> (Third Party Verification) - from payment link creation to payment processing.

### Prerequisites

To use the TPV flow for Payment Links, ensure the **enableTpvFlow** configuration is enabled for your merchant account: Contact your PayU Key Account Manager (KAM) or <Anchor label="PayU Support" target="_blank" href="https://help.payu.in">PayU Support</Anchor> to enable this configuration.

### Steps to integrate

<Cards columns={3}>
  <Card title="1. Create Payment Link" href="#step-1-create-payment-link">
    Create a payment link with beneficiary account details for TPV verification.
    <br />
  </Card>
  <Card title="2. Intermediate Page" href="#step-2-intermediate-page">
    Customer opens the payment link and fills relevant details.
    <br />
  </Card>
  <Card title="3. Check Response from PayU" href="#step-4-check-response-from-payu">
    Check and handle the response received from PayU after payment processing.
    <br />
  </Card>
  <Card title="4. Verify the Payment" href="#step-5-verify-the-payment">
    Verify the payment status using webhooks or Verify Payments API.
    <br />
  </Card>
</Cards>

***

## Step 1: Create Payment Link

Create a payment link with beneficiary account details using the Create Payment Link API.

<Accordion title="Environment" icon="fa-globe">
  | Environment | URL                                       |
  | ----------- | ----------------------------------------- |
  | Test        | `https://uatoneapi.payu.in/payment-links` |
  | Production  | `https://oneapi.payu.in/payment-links`    |

  **HTTP Method**: POST

  **<Glossary>Content-Type</Glossary>**: application/json
</Accordion>

<Tabs>
  <Tab title="Request Parameters">

<Accordion title="Request Headers" icon="fa-key">

**Mandatory Parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| Authorization | `String` <Glossary>Bearer Token</Glossary> for authentication. | `Bearer 03ddf1ee8d6daf811016c1cc9ce6a3de...` |
| mid | `String` Merchant ID (<Glossary>MID</Glossary>). | `8237350` |
| Content-Type | `String` Content type of the request. | `application/json` |

</Accordion>

**Mandatory Parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| subAmount | `Decimal` The payment amount. | `10.00` |
| description | `String` Purpose of payment. Max 250 characters. | `Payment for services` |
| source | `String` Source of the request. | `API` |
| maxPaymentsAllowed | `Integer` Must be `1` for TPV flow (single payment only). | `1` |
| beneficiarydetail | `Object` Object containing beneficiary account details for TPV. | See below |

**Optional Parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| invoiceNumber | `String` Unique invoice number for the payment link. | `INV123456789012` |
| customer | `Object` Customer details object. | See below |

<Accordion title="beneficiarydetail Object Parameters" icon="fa-code">

**Mandatory Parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| beneficiaryAccountNumber | `List<String>` Array of beneficiary account numbers. Maximum 4 accounts. Alphanumeric, max 50 characters each. | `["917732227242", "72522762"]` |
| ifscCode | `List<String>` Array of IFSC codes corresponding to each account number. Exactly 11 characters each: `[A-Z]{4}0[A-Z0-9]{6}` | `["SBIN0007001", "HDFC0001234"]` |
| beneficiaryName | `List<String>` Array of the beneficiary name. | `"Ashish","Harish"` |
| beneficiaryAccountType | `List<String>` Array of the beneficiary account type. It can be "SAVINGS" or "CURRENT". | `"SAVINGS","CURRENT"` |

</Accordion>

<Accordion title="customer Object Parameters" icon="fa-user">

**Optional Parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| email | `String` Customer's email address. | `john.doe@example.com` |
| phone | `String` Customer's phone number. | `9876543210` |
| name | `String` Customer's name. | `John Doe` |

</Accordion>

  </Tab>
  <Tab title="Sample Request">

```bash
curl --location 'https://uatoneapi.payu.in/payment-links' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <Bearer Token>' \
--header 'mid: 82**3*0' \
--data-raw '{
    "subAmount": 10,
    "maxPaymentsAllowed": 1,
    "invoiceNumber": "INV123456789012",
    "description": "Payment for services",
    "customer": {
        "email": "john.doe@example.com",
        "phone": "9876543210",
        "name": "John Doe"
    },
    "beneficiarydetail": {
      "beneficiaryAccountNumber": ["account1", "account2"],
      "ifscCode": ["IFSC1234567", "IFSC7654321"],
      "beneficiaryName": ["Beneficiary One", "Beneficiary Two"],
      "beneficiaryAccountType": ["SAVINGS", "CURRENT"]
    },
    "source": "API"
}'
```
```python
import requests
import json

url = "https://uatoneapi.payu.in/payment-links"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 03ddf1ee8d6daf811016c1cc9ce6a3de1771092b1eaeeb936764743888b9eb75",
    "mid": "8237350"
}
payload = {
    "subAmount": 10,
    "maxPaymentsAllowed": 1,
    "invoiceNumber": "INV123456789012",
    "description": "Payment for services",
    "customer": {
        "email": "john.doe@example.com",
        "phone": "9876543210",
        "name": "John Doe"
    },
    "beneficiarydetail": {
        "beneficiaryAccountNumber": ["account1", "account2"],
        "ifscCode": ["IFSC1234567", "IFSC7654321"],
        "beneficiaryName": ["Beneficiary One", "Beneficiary Two"],
        "beneficiaryAccountType": ["SAVINGS", "CURRENT"]
    },
    "source": "API"
}
try:
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://uatoneapi.payu.in/payment-links";
            client.DefaultRequestHeaders.Add("Authorization", "Bearer 03ddf1ee8d6daf811016c1cc9ce6a3de1771092b1eaeeb936764743888b9eb75");
            client.DefaultRequestHeaders.Add("mid", "8237350");
            string jsonPayload = @"{
                ""subAmount"": 10,
                ""maxPaymentsAllowed"": 1,
                ""invoiceNumber"": ""INV123456789012"",
                ""description"": ""Payment for services"",
                ""customer"": {
                    ""email"": ""john.doe@example.com"",
                    ""phone"": ""9876543210"",
                    ""name"": ""John Doe""
                },
                ""beneficiarydetail"": {
                    ""beneficiaryAccountNumber"": [""account1"", ""account2""],
                    ""ifscCode"": [""IFSC1234567"", ""IFSC7654321""],
                    ""beneficiaryName"": [""Beneficiary One"", ""Beneficiary Two""],
                    ""beneficiaryAccountType"": [""SAVINGS"", ""CURRENT""]
                },
                ""source"": ""API""
            }";
            var content = new StringContent(jsonPayload, Encoding.UTF8, "application/json");
            HttpResponseMessage response = await client.PostAsync(url, content);
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
async function makePaymentLinkRequest() {
    const url = "https://uatoneapi.payu.in/payment-links";
    const headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 03ddf1ee8d6daf811016c1cc9ce6a3de1771092b1eaeeb936764743888b9eb75",
        "mid": "8237350"
    };
    const payload = {
        subAmount: 10,
        maxPaymentsAllowed: 1,
        invoiceNumber: "INV123456789012",
        description: "Payment for services",
        customer: {
            email: "john.doe@example.com",
            phone: "9876543210",
            name: "John Doe"
        },
        beneficiarydetail: {
            beneficiaryAccountNumber: ["account1", "account2"],
            ifscCode: ["IFSC1234567", "IFSC7654321"],
            beneficiaryName: ["Beneficiary One", "Beneficiary Two"],
            beneficiaryAccountType: ["SAVINGS", "CURRENT"]
        },
        source: "API"
    };
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(payload)
        });
        const responseText = await response.text();
        console.log(`Status Code: ${response.status}`);
        console.log(`Response: ${responseText}`);
        return response;
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}
makePaymentLinkRequest();
```
```java
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

public class PaymentLinkRequest {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://uatoneapi.payu.in/payment-links");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Authorization", "Bearer 03ddf1ee8d6daf811016c1cc9ce6a3de1771092b1eaeeb936764743888b9eb75");
            connection.setRequestProperty("mid", "8237350");
            connection.setDoOutput(true);
            String jsonPayload = "{\"subAmount\": 10,\"maxPaymentsAllowed\": 1,\"invoiceNumber\": \"INV123456789012\",\"description\": \"Payment for services\",\"customer\": {\"email\": \"john.doe@example.com\",\"phone\": \"9876543210\",\"name\": \"John Doe\"},\"beneficiarydetail\": {\"beneficiaryAccountNumber\": [\"account1\", \"account2\"],\"ifscCode\": [\"IFSC1234567\", \"IFSC7654321\"],\"beneficiaryName\": [\"Beneficiary One\", \"Beneficiary Two\"],\"beneficiaryAccountType\": [\"SAVINGS\", \"CURRENT\"]},\"source\": \"API\"}";
            try (OutputStream outputStream = connection.getOutputStream()) {
                byte[] input = jsonPayload.getBytes(StandardCharsets.UTF_8);
                outputStream.write(input, 0, input.length);
            }
            int statusCode = connection.getResponseCode();
            BufferedReader reader = new BufferedReader(new InputStreamReader(
                statusCode >= 200 && statusCode < 300 ? connection.getInputStream() : connection.getErrorStream()
            ));
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
}
```
```php
<?php
$url = "https://uatoneapi.payu.in/payment-links";
$headers = [
    "Content-Type: application/json",
    "Authorization: Bearer 03ddf1ee8d6daf811016c1cc9ce6a3de1771092b1eaeeb936764743888b9eb75",
    "mid: 8237350"
];
$payload = [
    "subAmount" => 10,
    "maxPaymentsAllowed" => 1,
    "invoiceNumber" => "INV123456789012",
    "description" => "Payment for services",
    "customer" => [
        "email" => "john.doe@example.com",
        "phone" => "9876543210",
        "name" => "John Doe"
    ],
    "beneficiarydetail" => [
        "beneficiaryAccountNumber" => ["account1", "account2"],
        "ifscCode" => ["IFSC1234567", "IFSC7654321"],
        "beneficiaryName" => ["Beneficiary One", "Beneficiary Two"],
        "beneficiaryAccountType" => ["SAVINGS", "CURRENT"]
    ],
    "source" => "API"
];
$ch = curl_init();
curl_setopt_array($ch, [
    CURLOPT_URL => $url,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_HTTPHEADER => $headers,
    CURLOPT_POSTFIELDS => json_encode($payload)
]);
$response = curl_exec($ch);
$statusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
echo "Status Code: " . $statusCode . "\n";
echo "Response: " . $response . "\n";
?>
```

  </Tab>
</Tabs>

<Accordion title="Validation Rules" icon="fa-check-circle">
  | Validation               | Rule                                            |
  | ------------------------ | ----------------------------------------------- |
  | Max Payments             | `maxPaymentsAllowed = 1`                        |
  | Max Beneficiaries        | ≤ 4 beneficiaries                               |
  | Equal Count              | Account numbers count = IFSC codes count        |
  | Account Format           | Alphanumeric, max 50 characters                 |
  | IFSC Format              | Exactly 11 characters: `[A-Z]{4}0[A-Z0-9]{6}`   |
  | Beneficiary Name         | Alphabetic characters and spaces, max 100 chars |
  | Beneficiary Account Type | Enum values only: SAVINGS, CURRENT              |
</Accordion>

***

## Step 2: Intermediate Page

When the payment link is created, the API returns a short URL (e.g., `https://v.payu.in/PAYUMN/flashvrkWhFD`).

<Accordion title="Customer Flow" icon="fa-user">
  1. Customer receives the payment link via email, SMS, or other channels
  2. Customer opens the link in their browser
  3. Customer fills in relevant details on the intermediate page
  4. Customer clicks "Make Payment" to proceed to the checkout page
</Accordion>

***

<br />

When the customer initiates payment, the backend converts beneficiary details to pipe-separated format and posts to the `_payment` API.

<Accordion title="Environment" icon="fa-globe">
  | Environment | URL                               |
  | ----------- | --------------------------------- |
  | Test        | `https://test.payu.in/_payment`   |
  | Production  | `https://secure.payu.in/_payment` |
</Accordion>

<Tabs>
  <Tab title="Request Parameters">

**Mandatory Parameters**

<table>
  <thead>
    <tr>
      <th style="text-align:left">Parameter</th>
      <th style="text-align:left">Description</th>
      <th style="text-align:left">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><Glossary>key</Glossary></td>
      <td><code>String</code> Merchant key provided by PayU.</td>
      <td>JP***g</td>
    </tr>
    <tr>
      <td><Glossary>txnid</Glossary></td>
      <td><code>String</code> Unique transaction ID generated by you.</td>
      <td>TtEmKjWF2uGliF</td>
    </tr>
    <tr>
      <td>amount</td>
      <td><code>String</code> Payment amount.</td>
      <td>5000.00</td>
    </tr>
    <tr>
      <td><Glossary>productinfo</Glossary></td>
      <td><code>String</code> Brief description of the product or service.</td>
      <td>Payment for services</td>
    </tr>
    <tr>
      <td>firstname</td>
      <td><code>String</code> Customer's first name.</td>
      <td>John</td>
    </tr>
    <tr>
      <td>email</td>
      <td><code>String</code> Customer's email address.</td>
      <td>john.doe@example.com</td>
    </tr>
    <tr>
      <td>phone</td>
      <td><code>String</code> Customer's phone number.</td>
      <td>9876543210</td>
    </tr>
    <tr>
      <td><Glossary>surl</Glossary></td>
      <td><code>String</code> Success URL where PayU redirects after successful payment.</td>
      <td>https://yoursite.com/success</td>
    </tr>
    <tr>
      <td><Glossary>furl</Glossary></td>
      <td><code>String</code> Failure URL where PayU redirects after failed payment.</td>
      <td>https://yoursite.com/failure</td>
    </tr>
    <tr>
      <td>beneficiarydetail</td>
      <td><code>JSON String</code> JSON object with pipe-separated beneficiary account numbers and IFSC codes. Up to 4 accounts supported. Refer to beneficiarydetail JSON object fields section below.</td>
      <td></td>
    </tr>
    <tr>
      <td>api_version</td>
      <td><code>Integer</code> Must be set to 20 when beneficiary details are present.</td>
      <td>20</td>
    </tr>
    <tr>
      <td><Glossary>hash</Glossary></td>
      <td><code>String</code> <Glossary>SHA-512</Glossary> hash calculated using the checksum logic. Refer to Hash Generation below this table.</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Optional Parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| udf1 - udf5 | `String` User-defined fields for storing additional information. | |

<Accordion title="beneficiarydetail JSON object fields" icon="fa-code">
  It must contain the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to four account details in this parameter. For example:

  ```json
  {"beneficiaryAccountNumber":"002001600674|00000031957292212|00000035955239352|00000035955239352",
  "ifscCode":"KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"}
  ```
</Accordion>

<Accordion title="Hash Generation" icon="fa-lock">
  The hash is generated using the following format:

  ```
  key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|Salt
  ```

  Where `beneficiarydetail` is the JSON string representation with pipe-separated values:

  ```json
  {"beneficiaryAccountNumber":"917732227242|72522762","ifscCode":"SBIN0007001|HDFC0001234"}
  ```

  > **Note**: The `beneficiarydetail` parameter value will be the last value to be appended before SALT.
</Accordion>

  </Tab>
  <Tab title="Sample Request">

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
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
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

  </Tab>
</Tabs>

***

## Step 3: Check Response from PayU

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
  | Parameter          | Description                                                                                                                                | Example                                |
  | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------- |
  | <Glossary>mihpayid</Glossary>           | `String` Unique reference number created for each transaction at PayU's end. Store this for future actions like Inquiry or Refund.    | `403993715524308236`                   |
  | mode               | `String` The payment mode used by the customer.                                                                                       | `NB`                                   |
  | status             | `String` Status of the transaction. Possible values: `success`, `failure`, `pending`. Only `success` should be treated as successful. | `success`                              |
  | unmappedstatus     | `String` Detailed status of the transaction.                                                                                          | `captured`                             |
  | key                | `String` The merchant key used for the transaction.                                                                                   | `JP***g`                               |
  | txnid              | `String` The transaction ID posted by the merchant during the transaction request.                                                    | `TtEmKjWF2uGliF`                       |
  | amount             | `String` The transaction amount.                                                                                                      | `5000.00`                              |
  | discount           | `String` The discount amount given by bank on the transaction fee (if any).                                                           | `0.00`                                 |
  | net_amount_debit   | `String` The net amount debited from the customer's account.                                                                          | `5000`                                 |
  | addedon            | `String` The transaction timestamp.                                                                                                   | `2021-10-05 12:44:06`                  |
  | productinfo        | `String` Product information as sent in the request.                                                                                  | `Payment for services`                 |
  | firstname          | `String` Customer's first name.                                                                                                       | `John`                                 |
  | email              | `String` Customer's email address.                                                                                                    | `john.doe@example.com`                 |
  | phone              | `String` Customer's phone number.                                                                                                     | `9876543210`                           |
  | hash               | `String` Hash for response validation (reverse hash).                                                                                 | `<hash_value>`                         |
  | field9             | `String` Transaction message from the bank.                                                                                           | `Transaction Completed Successfully`   |
  | PG_TYPE            | `String` The payment gateway type used.                                                                                               | `NB-PG`                                |
  | bank_ref_num       | `String` Bank reference number for the transaction.                                                                                   | `30646df4-69b7-43f4-acdd-21e6a593c037` |
  | <Glossary>bankcode</Glossary>           | `String` Bank code used for the transaction.                                                                                          | `TESTPGNB`                             |
  | error              | `String` Error code. `E000` indicates no error.                                                                                       | `E000`                                 |
  | error_Message      | `String` Error message description.                                                                                                   | `No Error`                             |
  | udf1 - udf5        | `String` User-defined fields as sent in the request.                                                                                  | ` `                                    |
  | <Glossary>payment_source</Glossary>    | `String` Source of the payment.                                                                                                       | `payu`                                 |
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
      [email] => john.doe@example.com
      [phone] => 9876543210
      [hash] => 74d1039311528b4a7b699db7ce195d6a219d7442271dedb23e516e29490ec743a89c12448698178907e03d32fa05e8178694db8037bc0be53380099e47c3d63f
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

***

## Step 4: Verify the Payment

Upon receiving the response, PayU recommends performing a reconciliation step to validate all transaction details. You can verify your payments using either of the following methods:

<Verify_Payment_Tabs />

***

## Key Limitations

| Limitation        | Description                                    |
| ----------------- | ---------------------------------------------- |
| Max Beneficiaries | Maximum 4 beneficiaries per payment link       |
| Max Payments      | `maxPaymentsAllowed = 1` (single payment only) |
| Partial Payment   | Not supported with TPV flow                    |
| Merchant Config   | `enableTpvFlow` must be set to `"1"`           |

<br />
