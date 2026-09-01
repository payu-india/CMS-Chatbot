---
title: PayPal Integration
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
---
title: PayPal Integration
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
Integrate PayU with PayPal wallets to facilitate international payments. PayPal can be seamlessly integrated with your PayU Hosted or Merchant Hosted Checkout integration. Customers have the option to utilize PayPal Currency Conversion to convert international payments from INR (or other currencies) to their chosen currency. Payments made through PayPal are directly transferred to your PayPal wallet, with settlements processed in INR.

This section describes the following:

- [Customer journey](https://docs.payu.in/docs/paypal-integration#customer-journey)
- [Benefits](https://docs.payu.in/docs/paypal-integration#benefits)
- [Steps to Integrate](https://docs.payu.in/docs/paypal-integration#steps-to-integrate)

## Customer journey

1. Customer is redirected to PayU Payment page.
2. Customer selects the **Wallets** option.

<Image src="https://files.readme.io/429e564-payu_payment_pagE_wallets_list.png" align="center" border={true} />

3. Customer selects the **Paypal** option.

<Image src="https://files.readme.io/44bffcc-payu_payment_paypal_page.png" align="center" border={true} />

4. Customer selects the preferred currency and clicks **PayPal**. The success or failure response is sent back to you by PayU after verification.

## Benefits

- Improved Success Rates: Experience success rates up to 20% higher.
- Accelerated Settlement: Receive payments on a T+1 settlement schedule.
- Extensive User Base: Access over 30 Crore PayPal users worldwide.
- No Extra Charges: Transaction rates are determined by PayPal.
- Currency Conversion: Facilitate currency conversions from INR to your customers\' preferred currencies.

## Steps to Integrate

<Cards columns={3}>
  <Card title="1. Initiate the Payment to PayU" href="#step-1-initiate-the-payment-to-payu" target="_blank">
    Initiate the payment to PayU with pg=PAYPAL and bankcode=PAYPAL
  </Card>
  <Card title="2. Check response from PayU" href="#step-2-check-response-from-payu">
    Check the response from PayU
  </Card>
  <Card title="3. Verify the payment" href="#step-3-verify-the-payment">
    Verify the payment using verify\_payment and monitor using webhooks
  </Card>
</Cards>

### Step 1: Initiate the payment to PayU

You need to use **bankcode** as PAYPAL with the **pg** as PAYPAL.

<Callout icon="📘" theme="info">
  ###

  **Reference**: For the **Try It** experience, refer to <a href="https://docs.payu.in/reference/_payment_merchant_hosted_wallets" target="_blank">Collect Payments API</a> under API Reference.
</Callout>

**Environment**

|                            |                                                                     |
| :------------------------- | :------------------------------------------------------------------ |
| **Test Environment**       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
| **Production Environment** | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

<Tabs>
  <Tab title="Request Parameters">

**Mandatory Parameters**

<table>
<thead>
<tr><th>Parameter</th><th>Description</th><th>Example</th></tr>
</thead>
<tbody>
<tr><td>key</td><td><code>String</code> The unique merchant key provided by PayU for your merchant account.</td><td>8488225</td></tr>
<tr><td>txnid</td><td><code>varchar</code> The Transaction ID (or OrderID). Order reference number generated at merchant\'s end. Must be unique for every new transaction.</td><td>fd3e847h2</td></tr>
<tr><td>amount</td><td><code>float</code> The payment amount of the particular transaction. Type-cast to float type.</td><td>10</td></tr>
<tr><td>productinfo</td><td><code>varchar</code> A brief product description.</td><td>T-shirt</td></tr>
<tr><td>firstname</td><td><code>varchar</code> The first name of the customer.</td><td>Ankit</td></tr>
<tr><td>email</td><td><code>varchar</code> The email of the customer.</td><td>test@gmail.com</td></tr>
<tr><td>phone</td><td><code>integer</code> The customer\'s phone number.</td><td>9876543210</td></tr>
<tr><td>pg</td><td><code>String</code> It defines the payment category using Merchant Hosted Checkout integration. For Wallet payment, "PAYPAL" must be specified.</td><td>PAYPAL</td></tr>
<tr><td>bankcode</td><td><code>String</code> The merchant must post PAYPAL as the value for this parameter.</td><td>PAYPAL</td></tr>
<tr><td>surl</td><td>The success URL — the page PayU will redirect to if the transaction is successful.</td><td>https://apiplayground-response.herokuapp.com/</td></tr>
<tr><td>furl</td><td>The failure URL — the page PayU will redirect to if the transaction fails.</td><td>https://apiplayground-response.herokuapp.com/</td></tr>
<tr><td>hash</td><td><code>String</code> The hash calculated by the merchant using key and salt. SHA-512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)</td><td>calculated_hash_value</td></tr>
</tbody>
</table>

**Optional Parameters**

<table>
<thead>
<tr><th>Parameter</th><th>Description</th><th>Example</th></tr>
</thead>
<tbody>
<tr><td>lastname</td><td><code>String</code> The last name of the customer.</td><td>Kumar</td></tr>
<tr><td>address1</td><td><code>String</code> The first line of the billing address.</td><td>123 Main St</td></tr>
<tr><td>address2</td><td><code>String</code> The second line of the billing address.</td><td>Apt 4B</td></tr>
<tr><td>city</td><td><code>String</code> The city where your customer resides as part of the billing address.</td><td>Mumbai</td></tr>
<tr><td>state</td><td><code>String</code> The state where your customer resides as part of the billing address.</td><td>Maharashtra</td></tr>
<tr><td>country</td><td><code>String</code> The country where your customer resides.</td><td>India</td></tr>
<tr><td>zipcode</td><td><code>String</code> Billing address zip code is mandatory for the cardless EMI option.</td><td>400001</td></tr>
<tr><td>udf1</td><td><code>String</code> This parameter has been made for you to keep any information corresponding to the transaction.</td><td>custom_data_1</td></tr>
<tr><td>udf2</td><td><code>String</code> This parameter has been made for you to keep any information corresponding to the transaction.</td><td>custom_data_2</td></tr>
<tr><td>udf3</td><td><code>String</code> This parameter has been made for you to keep any information corresponding to the transaction.</td><td>custom_data_3</td></tr>
<tr><td>udf4</td><td><code>String</code> This parameter has been made for you to keep any information corresponding to the transaction.</td><td>custom_data_4</td></tr>
<tr><td>udf5</td><td><code>String</code> This parameter has been made for you to keep any information corresponding to the transaction.</td><td>custom_data_5</td></tr>
</tbody>
</table>

  <Accordion title="Understanding Hashing and sample code" icon="fa-code">
    <HashingRequestParameters />

    #### Hashing Sample Code

    <HashingSample />
  </Accordion>

  </Tab>

  <Tab title="Sample Request">

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=PAYPAL&bankcode=PAYPAL&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
```
```python
import requests

url = "https://test.payu.in/_payment"
headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "key": "J****g",
    "txnid": "aI1UM19ONxLgPz",
    "amount": "10.00",
    "firstname": "Ashish",
    "email": "test@gmail.com",
    "phone": "9876543210",
    "productinfo": "iPhone",
    "pg": "PAYPAL",
    "bankcode": "PAYPAL",
    "surl": "https://apiplayground-response.herokuapp.com/",
    "furl": "https://apiplayground-response.herokuapp.com/",
    "hash": "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
}
response = requests.post(url, headers=headers, data=data)
print(response.status_code)
print(response.text)
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;
class Program
{
    static async Task Main(string[] args)
    {
        using (var client = new HttpClient())
        {
            client.DefaultRequestHeaders.Add("accept", "application/json");
            var formData = new List<KeyValuePair<string, string>>
            {
                new KeyValuePair<string, string>("key", "J****g"),
                new KeyValuePair<string, string>("txnid", "aI1UM19ONxLgPz"),
                new KeyValuePair<string, string>("amount", "10.00"),
                new KeyValuePair<string, string>("firstname", "Ashish"),
                new KeyValuePair<string, string>("email", "test@gmail.com"),
                new KeyValuePair<string, string>("phone", "9876543210"),
                new KeyValuePair<string, string>("productinfo", "iPhone"),
                new KeyValuePair<string, string>("pg", "PAYPAL"),
                new KeyValuePair<string, string>("bankcode", "PAYPAL"),
                new KeyValuePair<string, string>("surl", "https://apiplayground-response.herokuapp.com/"),
                new KeyValuePair<string, string>("furl", "https://apiplayground-response.herokuapp.com/"),
                new KeyValuePair<string, string>("hash", "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa")
            };
            var response = await client.PostAsync("https://test.payu.in/_payment", new FormUrlEncodedContent(formData));
            Console.WriteLine($"Status: {response.StatusCode}");
            Console.WriteLine($"Response: {await response.Content.ReadAsStringAsync()}");
        }
    }
}
```
```javascript
async function makePayPalPayment() {
    const url = "https://test.payu.in/_payment";
    const formData = new URLSearchParams({
        "key": "J****g", "txnid": "aI1UM19ONxLgPz", "amount": "10.00",
        "firstname": "Ashish", "email": "test@gmail.com", "phone": "9876543210",
        "productinfo": "iPhone", "pg": "PAYPAL", "bankcode": "PAYPAL",
        "surl": "https://apiplayground-response.herokuapp.com/",
        "furl": "https://apiplayground-response.herokuapp.com/",
        "hash": "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
    });
    const response = await fetch(url, { method: "POST", headers: { "accept": "application/json", "Content-Type": "application/x-www-form-urlencoded" }, body: formData });
    console.log("Status:", response.status);
    console.log("Response:", await response.text());
}
makePayPalPayment();
```
```java
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;
public class PayPalPayment {
    public static void main(String[] args) throws IOException, InterruptedException {
        String url = "https://test.payu.in/_payment";
        Map<String, String> formData = new HashMap<>();
        formData.put("key","J****g"); formData.put("txnid","aI1UM19ONxLgPz"); formData.put("amount","10.00");
        formData.put("firstname","Ashish"); formData.put("email","test@gmail.com"); formData.put("phone","9876543210");
        formData.put("productinfo","iPhone"); formData.put("pg","PAYPAL"); formData.put("bankcode","PAYPAL");
        formData.put("surl","https://apiplayground-response.herokuapp.com/");
        formData.put("furl","https://apiplayground-response.herokuapp.com/");
        formData.put("hash","6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa");
        String formBody = formData.entrySet().stream().map(e -> e.getKey()+"="+e.getValue()).collect(Collectors.joining("&"));
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder().uri(URI.create(url))
            .header("accept","application/json").header("Content-Type","application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formBody)).build();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
```php
<?php
$url = "https://test.payu.in/_payment";
$data = array(
    'key' => 'J****g', 'txnid' => 'aI1UM19ONxLgPz', 'amount' => '10.00',
    'firstname' => 'Ashish', 'email' => 'test@gmail.com', 'phone' => '9876543210',
    'productinfo' => 'iPhone', 'pg' => 'PAYPAL', 'bankcode' => 'PAYPAL',
    'surl' => 'https://apiplayground-response.herokuapp.com/',
    'furl' => 'https://apiplayground-response.herokuapp.com/',
    'hash' => '6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa'
);
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('accept: application/json', 'Content-Type: application/x-www-form-urlencoded'));
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
echo "HTTP Code: " . $httpCode . "\n";
echo "Response: " . $response;
?>
```

  </Tab>
</Tabs>

<Callout icon="📘" theme="info">
  ### Note:

  Ensure your PayPal account maintains sufficient funds before initiating a refund. Refunds can be initiated either through the PayU Dashboard or the **Refund Transaction** API. For more information, refer to:

  - <Anchor target="_blank" href="https://docs.payu.in/docs/refunds-dashboard">Refunds Dashboard</Anchor>.
  - <Anchor target="_blank" href="https://docs.payu.in/reference/refund_transaction_api">Refunds Transaction API</Anchor>.
</Callout>

### Step 2: Check the response from PayU

<Accordion title="Sample response" icon="fa-code">
  ```
  Array
  (
      [mihpayid] => 403993715527518775
      [mode] => PAYPAL
      [status] => success
      [PG_TYPE] => PAYPAL-PG
      [bank_ref_num] => 540898ed-72e7-40a8-a96e-f17de621cbb4
      [bankcode] => PAYPAL
      [field4] => 0.12
      [field5] => USD
      [error] => E000
      [error_Message] => No Error
  )
  ```
</Accordion>

### Step 3: Verify the payment

<Verify_Payment_Tabs />

<br />
