---
title: UPI Collect Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collect Payments with UPI - Merchant Hosted Checkout
  description: >-
    Learn how to seamlessly collect payments through UPI transactions using
    PayU's Merchant Hosted Checkout integration. Discover the steps to validate
    the customer's Virtual Payment Address (VPA), initiate payments, and verify
    the payment status.
  robots: index
next:
  description: ''
---
---
title: UPI Collect Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collect Payments with UPI - Merchant Hosted Checkout
  description: >-
    Learn how to seamlessly collect payments through UPI transactions using
    PayU\'s Merchant Hosted Checkout integration.
  robots: index
next:
  description: ''
---
<NPCI_Mandate />

This section describes how UPI Collect should be integrated on your checkout. **As per NPCI\'s guidelines, UPI Collect payments are allowed only on MCC 6012 and 6211.**

<Callout icon="👍" theme="okay">
  ###

  Experience the end-to-end **Merchant Hosted Checkout** > **UPI** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

  <HTMLBlock>{`
                      <button onclick="window.open(\'https://payu.in/integrationlab/seamless/sm-upiflow\', \'_blank\')" class="tooltip-btn">
                          Experience the flow and get the code
                      </button>
  `}</HTMLBlock>
</Callout>

**Steps to Integrate:**

<Cards>
  <Card title="1. Validate the UPI handle" href="https://docs.payu.in/docs/collect-payments-with-upi-seamless#step-1-validate-the-upi-handle">
    Validate the card type using the Validate VPA API.
  </Card>
  <Card title="2. Initiate the Payment to PayU" href="https://docs.payu.in/docs/collect-payments-with-upi-seamless#step-2-initiate-the-payment-to-payu">
    Initiate the payment to PayU with pg=UPI and bankcode=UPI
  </Card>
  <Card title="3. Check response from PayU" href="https://docs.payu.in/docs/collect-payments-with-upi-seamless#step-3-check-response-from-payu">
    Check the response from PayU
  </Card>
  <Card title="4. Verify the payment" href="#step-4-verify-the-payment">
    Verify the payment using verify\_payment and monitor using webhooks
  </Card>
</Cards>

<RegisterMerchantPrerequiste />

<Callout icon="📮" theme="default">
  ###

  **Postman Collection**: Access the **Merchant Hosted Checkout > UPI APIs Postman Collection** from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/394lrbp/upi-integration](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/394lrbp/upi-integration)
</Callout>

<Callout icon="⚠️" theme="warning">
  ###

  **Important UPI Integration Changes as per NPCI Mandate on UPI Collect Disablement**:

  - **Seamless Form Post Users**: Merchants using Seamless Form Post flow must migrate to `txn_s2s_flow` (UPI Intent S2S). For migration guidance, refer to [UPI Intent S2S Integration](doc:upi-intent-server-to-server).
  - **For Android Apps**: Merchants must implement the Smart Intent implementation. Refer to [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow).
  - **For iOS Apps**: Merchants can implement the specific deeplink and continue using the UPI Collect flow as is.
  - **For Web**: Merchants must use the deeplink created via [UPI Intent S2S Integration](doc:upi-intent-server-to-server) to generate a QR code.
</Callout>

## Step 1: Validate the UPI handle

You can validate your customer\'s Virtual Payment Address (VPA) using the <Anchor target="_blank" href="https://docs.payu.in/reference/validate_vpa_api">Validate VPA Handle</Anchor> API before initiating the transaction.

<GENERALAPIsEnvironment />

<Accordion title="Sample request" icon="fa-code">
  <Validate_VPA />
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  **Success scenario**

  ```plaintext
  {
     "status":"SUCCESS",
     "vpa":"9999999999@upi",
     "isVPAValid":1,
     "isAutoPayVPAValid":1,
     "payerAccountName":"ABC"
  }
  ```

  **Failure scenarios**

  ```plaintext
  {"status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"payerAccountName":"NA"}
  ```
</Accordion>

<Accordion title="Sample VPA validation code" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
       -H "Content-Type: application/x-www-form-urlencoded" \
       -d "key=YOUR_MERCHANT_KEY" \
       -d "command=validateVPA" \
       -d "var1=customer@upi" \
       -d "hash=$HASH"
  ```
</Accordion>

## Step 2: Initiate the payment to PayU

<Accordion title="Post request syntax & composition" icon="fa-code">
  Post Request Syntax & Composition for UPI

  ```html
  <body>
  <form action=\'https://test.payu.in/_payment\' method=\'post\'>
  <input type="hidden" name="key" value="JP***g" />
  <input type="hidden" name="txnid" value="t6svtqtjRdl34W" />
  <input type="hidden" name="productinfo" value="iPhone" />
  <input type="hidden" name="amount" value="10" />
  <input type="hidden" name="email" value="test@gmail.com" />
  <input type="hidden" name="firstname" value="Ashish" />
  <input type="hidden" name="pg" value="UPI" />
  <input type="hidden" name="bankcode" value="UPI" />
  <input type="hidden" name="vpa" value="test123@okhdfcbank" />
  <input type="hidden" name="surl" value="your own success url" />
  <input type="hidden" name="furl" value="your own failure url" />
  <input type="hidden" name="phone" value="9988776655" />
  <input type="hidden" name="hash" value="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />
  <input type="submit" value="submit"> </form>
  </body>
  ```
</Accordion>

**Environment**

|                            |                                                                         |
| :------------------------- | :---------------------------------------------------------------------- |
| **Test Environment**       | \<[https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | \<[https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

> 📘 Reference:
>
> For the **Try It** experience and response, refer to [Collect Payment API - Merchant Hosted Checkout](https://docs.payu.in/reference/_payment_merchant_hosted) under API Reference.

<Tabs>
  <Tab title="Request Parameters">

**Mandatory Parameters**

<table>
<thead>
<tr><th>Parameter</th><th>Description</th><th>Example</th></tr>
</thead>
<tbody>
<tr><td>key</td><td><code>String</code> Merchant key provided by PayU during onboarding.</td><td>JPg***r</td></tr>
<tr><td>txnid</td><td><code>String</code> The transaction ID is a reference number for a specific order that is generated by the merchant.</td><td>ypl938459435</td></tr>
<tr><td>amount</td><td><code>String</code> The payment amount for the transaction.</td><td>10.00</td></tr>
<tr><td>productinfo</td><td><code>String</code> A brief description of the product.</td><td>iPhone</td></tr>
<tr><td>firstname</td><td><code>String</code> The first name of the customer.</td><td>Ashish</td></tr>
<tr><td>email</td><td><code>String</code> The email address of the customer.</td><td>abc@payu.in</td></tr>
<tr><td>phone</td><td><code>String</code> The phone number of the customer.</td><td>9988776655</td></tr>
<tr><td>pg</td><td><code>String</code> It defines the payment category on the PayU payment page. Must contain "<Glossary>UPI</Glossary>" for UPI transactions.</td><td>UPI</td></tr>
<tr><td>bankcode</td><td><code>String</code> Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option\'s bank code value.</td><td>UPI</td></tr>
<tr><td><Glossary>vpa</Glossary></td><td><code>String</code> The VPA of the customer. For the list of bank name part of the handles, refer to <a href="https://docs.payu.in/docs/upi-handles">UPI Handles</a>. For test UPI IDs, refer to <a href="https://docs.payu.in/docs/test-cards-upi-id-and-wallets">Test Cards, UPI ID and Wallets</a>.</td><td>test123@okhdfcbank</td></tr>
<tr><td>furl</td><td><code>String</code> The failure URL, which is the page PayU will redirect to if the transaction is failure.</td><td>https://example.com/success</td></tr>
<tr><td>surl</td><td><code>String</code> The success URL, which is the page PayU will redirect to if the transaction is success.</td><td>https://example.com/failure</td></tr>
<tr><td>hash</td><td><code>String</code> It is the hash calculated by the merchant. SHA-512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)</td><td>eabec285da28fd...</td></tr>
</tbody>
</table>

**Optional Parameters**

<table>
<thead>
<tr><th>Parameter</th><th>Description</th><th>Example</th></tr>
</thead>
<tbody>
<tr><td>address1</td><td><code>String</code> The first line of the billing address. For Fraud Detection: helpful when it comes to fraud detection and chargebacks.</td><td>123 Main Street</td></tr>
<tr><td>address2</td><td><code>String</code> The second line of the billing address.</td><td>Apt 4B</td></tr>
<tr><td>city</td><td><code>String</code> The city where your customer resides as part of the billing address.</td><td>New Delhi</td></tr>
<tr><td>state</td><td><code>String</code> The state where your customer resides as part of the billing address.</td><td>Delhi</td></tr>
<tr><td>country</td><td><code>String</code> The country where your customer resides.</td><td>India</td></tr>
<tr><td>zipcode</td><td><code>String</code> Billing address zip code is mandatory for the cardless EMI option. <code>Character Limit</code>: 20</td><td>110001</td></tr>
<tr><td>udf1</td><td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</td><td>Custom Data 1</td></tr>
<tr><td>udf2</td><td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</td><td>Custom Data 2</td></tr>
<tr><td>udf3</td><td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td><td>Custom Data 3</td></tr>
<tr><td>udf4</td><td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td><td>Custom Data 4</td></tr>
<tr><td>udf5</td><td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td><td>Custom Data 5</td></tr>
</tbody>
</table>

  <Accordion title="Understanding Hashing and sample code" icon="fa-code">
    <HashingRequestParameters />

    #### Hashing Sample Code

    <HashingSample />
  </Accordion>

  </Tab>

  <Tab title="Sample Request">

```curl
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&txnid=xdB9G7qYpfqszo&amount=10&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=UPI&bankcode=UPI&vpa=VPA-anything@payu&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb"
```
```python
import requests

url = "https://test.payu.in/_payment"
headers = {
  "accept": "application/json",
  "Content-Type": "application/x-www-form-urlencoded"
}
data = {
  "key": "JP***g",
  "txnid": "xdB9G7qYpfqszo",
  "amount": "10",
  "firstname": "PayU User",
  "email": "test@gmail.com",
  "phone": "9876543210",
  "productinfo": "iPhone",
  "pg": "UPI",
  "bankcode": "UPI",
  "vpa": "VPA-anything@payu",
  "surl": "https://apiplayground-response.herokuapp.com/",
  "furl": "https://apiplayground-response.herokuapp.com/",
  "hash": "649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb"
}
response = requests.post(url, headers=headers, data=data)
print(response.status_code)
print(response.text)
```
```perl
use strict;
use warnings;
use LWP::UserAgent;
use HTTP::Request::Common qw(POST);
my $url = "https://test.payu.in/_payment";
my $ua = LWP::UserAgent->new();
my $response = $ua->request(POST $url,
    'Accept' => 'application/json',
    'Content-Type' => 'application/x-www-form-urlencoded',
    Content => [
        key => 'JP***g', txnid => 'xdB9G7qYpfqszo', amount => '10',
        firstname => 'PayU User', email => 'test@gmail.com', phone => '9876543210',
        productinfo => 'iPhone', pg => 'UPI', bankcode => 'UPI',
        vpa => 'VPA-anything@payu',
        surl => 'https://apiplayground-response.herokuapp.com/',
        furl => 'https://apiplayground-response.herokuapp.com/',
        hash => '649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb'
    ]
);
print "Status: " . $response->code . "\n";
print "Response: " . $response->content . "\n";
```
```php
<?php
$url = "https://test.payu.in/_payment";
$data = http_build_query([
    "key"         => "JP***g",
    "txnid"       => "xdB9G7qYpfqszo",
    "amount"      => "10",
    "firstname"   => "PayU User",
    "email"       => "test@gmail.com",
    "phone"       => "9876543210",
    "productinfo" => "iPhone",
    "pg"          => "UPI",
    "bankcode"    => "UPI",
    "vpa"         => "VPA-anything@payu",
    "surl"        => "https://apiplayground-response.herokuapp.com/",
    "furl"        => "https://apiplayground-response.herokuapp.com/",
    "hash"        => "649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb"
]);
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "accept: application/json",
    "Content-Type: application/x-www-form-urlencoded"
]);
$response = curl_exec($ch);
if (curl_errno($ch)) {
    echo "cURL Error: " . curl_error($ch);
} else {
    echo "Response: " . $response;
}
curl_close($ch);
?>
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
        var client = new HttpClient();
        var url = "https://test.payu.in/_payment";
        var formData = new FormUrlEncodedContent(new[]
        {
            new KeyValuePair<string, string>("key",         "JP***g"),
            new KeyValuePair<string, string>("txnid",       "xdB9G7qYpfqszo"),
            new KeyValuePair<string, string>("amount",      "10"),
            new KeyValuePair<string, string>("firstname",   "PayU User"),
            new KeyValuePair<string, string>("email",       "test@gmail.com"),
            new KeyValuePair<string, string>("phone",       "9876543210"),
            new KeyValuePair<string, string>("productinfo", "iPhone"),
            new KeyValuePair<string, string>("pg",          "UPI"),
            new KeyValuePair<string, string>("bankcode",    "UPI"),
            new KeyValuePair<string, string>("vpa",         "VPA-anything@payu"),
            new KeyValuePair<string, string>("surl",        "https://apiplayground-response.herokuapp.com/"),
            new KeyValuePair<string, string>("furl",        "https://apiplayground-response.herokuapp.com/"),
            new KeyValuePair<string, string>("hash",        "649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb")
        });
        client.DefaultRequestHeaders.Add("accept", "application/json");
        var response = await client.PostAsync(url, formData);
        string responseBody = await response.Content.ReadAsStringAsync();
        Console.WriteLine("Status Code: " + response.StatusCode);
        Console.WriteLine("Response: " + responseBody);
    }
}
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
public class PayURequest {
    public static void main(String[] args) throws IOException, InterruptedException {
        String url = "https://test.payu.in/_payment";
        Map<String, String> parameters = new HashMap<>();
        parameters.put("key","JP***g"); parameters.put("txnid","xdB9G7qYpfqszo"); parameters.put("amount","10");
        parameters.put("firstname","PayU User"); parameters.put("email","test@gmail.com"); parameters.put("phone","9876543210");
        parameters.put("productinfo","iPhone"); parameters.put("pg","UPI"); parameters.put("bankcode","UPI");
        parameters.put("vpa","VPA-anything@payu");
        parameters.put("surl","https://apiplayground-response.herokuapp.com/");
        parameters.put("furl","https://apiplayground-response.herokuapp.com/");
        parameters.put("hash","649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb");
        String formData = parameters.entrySet().stream()
            .map(e -> URLEncoder.encode(e.getKey(),StandardCharsets.UTF_8)+"="+URLEncoder.encode(e.getValue(),StandardCharsets.UTF_8))
            .collect(Collectors.joining("&"));
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder().uri(URI.create(url))
            .header("Accept","application/json").header("Content-Type","application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formData)).build();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```

  </Tab>
</Tabs>

## Step 3: Check response from PayU

<ReverseHashing />

### Hash validation logic for payment response (Reverse Hashing)

The order of the parameters for reverse hashing:

```
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

<Accordion title="Sample Response" icon="fa-code">
  ```
  Array
  (
      [mihpayid] => 403993715523409521
      [mode] => UPI
      [status] => success
      [unmappedstatus] => captured
      [key] => JPM7Fg
      [txnid] => 5jJ9xRceXX1ydT
      [amount] => 10.00
      [PG_TYPE] => UPI-PG
      [bank_ref_num] => 5jJ9xRceXX1ydT
      [bankcode] => UPI
      [error] => E000
      [error_Message] => No Error
  )
  ```
</Accordion>

## Step 4: Verify the payment

<Verify_Payment_Tabs />

## Recommended integrations for UPI

- **Recurring Payments**: Enable recurring payments or subscriptions. For more information, refer to [Recurring Payments Integration](https://docs.payu.in/docs/introduction-recurring-payments-integration).
- **Offers**: Configure offers for cards on Dashboard. For more information, refer to [Offers Dashboard](https://docs.payu.in/docs/offers-dashboard).

<br />
