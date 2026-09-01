---
title: Cards Integration
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
title: Cards Integration
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
PayU supports the following debit cards and credit cards:

- American Express (AMEX)
- Visa
- Mastercard
- Diners
- Rupay

<Callout icon="📘" theme="info">
  ###

  **Notes**:

  - PayU accepts domestic and international transactions, but international transactions need to be enabled by writing to PayU Integration Team (<Anchor target="_blank" href="mailto:integration@pay.in">integration@pay.in</Anchor>).
  - If you are storing or transmitting cardholder data, you must fill the "<Anchor target="_blank" href="https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf">Self-Assessment Questionnaire A-EP and Attestation of Compliance</Anchor>" form. For more information on Save Cards API integration, refer to PayU Save Cards API Integration docs.
</Callout>

<br />

<Cards_PayU_Labs />

<br />

<RegisterMerchantPrerequiste />

## Steps to Integrate

<Cards>
  <Card title="1. Validate the card type" href="https://docs.payu.in/docs/collect-payments-with-cards-seamless#step-1-validate-the-card-type">
    Validate the card type using the card BIN API>
  </Card>

  <Card title="2. Initiate the Payment to PayU" href="https://docs.payu.in/docs/collect-payments-with-cards-seamless#step-2-initiate-the-payment-to-payu">
    Initiate the payment to PayU with pg=CC and bankcode=CC
  </Card>

  <Card title="3. Check response from PayU" href="https://docs.payu.in/docs/collect-payments-with-cards-seamless#step-3-check-response-from-payu">
    Check the response from PayU
  </Card>

  <Card title="4. Verify the payment" href="https://docs.payu.in/docs/collect-payments-with-cards-seamless#step-4-verify-the-payment">
    Verify the payment using verify\_payment and monitor using webhooks
  </Card>
</Cards>

### Handling Transactions

<Cards>
  <Card title="Guest Checkout Transactions" href="#handling-guest-checkout-transactions" target="_blank">
    For handling Guest Checkout transaction, you need to include additional parameter based on the Guest Checkout flow.
  </Card>

  <Card title="3DS Secure 2.0 Transactions" href="#handling-3ds-secure-20-transaction" target="_blank">
    For handling 3DS Secure 2.0 transaction, you need to include threeDS2RequestData as an additional parameter to \_payment.
  </Card>
</Cards>

<Callout icon="📘" theme="info">
  ###

  **Postman Collection**

  <Postman_collection />
</Callout>

## Step 1: Validate the card type

When customers use debit cards or credit cards on your website, you can validate the card type with the first six digits. Use the **getBinInfo** API (known as BIN API) to validate the type of card. For more information, refer to  <Anchor target="_blank" href="https://docs.payu.in/reference/get_bin_info_api">BIN APIs</Anchor>.

| Environment            | URL                                                                                                  |
| :--------------------- | :--------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/merchant/postservice?form=2](https://test.payu.in/merchant/postservice?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice?form=2](https://info.payu.in/merchant/postservice?form=2) |

<Accordion title="Sample request" icon="fa-code">
  ## For Single Card

  The following values are specified in the var1, var2, and var5 for this scenario:

  * var1 = 1
  * var2 = 512345
  * var5 = 1

<Tabs>
  <Tab title="Request Parameters">

  No dedicated request parameter table for this step — refer to the BIN API documentation linked above.

  ### Hashing Logic

  <KeyHashForGeneralParametersDescription />

  </Tab>

  <Tab title="Sample Request">

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
-H "accept: application/json" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "key=JP***g" \
-d "command=getBinInfo" \
-d "var1=2" \
-d "var2=512345" \
-d "var3=" \
-d "var4=" \
-d "var5=1" \
-d "hash={{hash_value}}"
```
```python
import requests

url = "https://test.payu.in/merchant/postservice?form=2"
headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "key": "JP***g",
    "command": "getBinInfo",
    "var1": "2",
    "var2": "512345",
    "var3": "",
    "var4": "",
    "var5": "1",
    "hash": "{{hash_value}}"
}
response = requests.post(url, headers=headers, data=data)
print("Status Code:", response.status_code)
print("Response:", response.text)
```
```php
<?php
$url = "https://test.payu.in/merchant/postservice?form=2";
$data = http_build_query([
    "key"     => "JP***g",
    "command" => "getBinInfo",
    "var1"    => "2",
    "var2"    => "512345",
    "var3"    => "",
    "var4"    => "",
    "var5"    => "1",
    "hash"    => "{{hash_value}}"
]);
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "accept: application/json",
    "Content-Type: application/x-www-form-urlencoded"
]);
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
public class BinApiRequest {
    public static void main(String[] args) throws Exception {
        String url = "https://test.payu.in/merchant/postservice?form=2";
        String formData = "key=JP***g"
                + "&command=getBinInfo"
                + "&var1=2"
                + "&var2=512345"
                + "&var3="
                + "&var4="
                + "&var5=1"
                + "&hash={{hash_value}}";
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
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;
class BinApiRequest {
    static async Task Main(string[] args) {
        using var client = new HttpClient();
        client.DefaultRequestHeaders.Add("accept", "application/json");
        var formData = new FormUrlEncodedContent(new[] {
            new KeyValuePair<string, string>("key",     "JP***g"),
            new KeyValuePair<string, string>("command", "getBinInfo"),
            new KeyValuePair<string, string>("var1",    "2"),
            new KeyValuePair<string, string>("var2",    "512345"),
            new KeyValuePair<string, string>("var3",    ""),
            new KeyValuePair<string, string>("var4",    ""),
            new KeyValuePair<string, string>("var5",    "1"),
            new KeyValuePair<string, string>("hash",    "{{hash_value}}")
        });
        var response = await client.PostAsync(
            "https://test.payu.in/merchant/postservice?form=2", formData);
        string responseBody = await response.Content.ReadAsStringAsync();
        Console.WriteLine("Status Code: " + (int)response.StatusCode);
        Console.WriteLine("Response: " + responseBody);
    }
}
```

  </Tab>
</Tabs>
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ### Success Scenario

  ```php
  $response = array(
    'status' => 1,
    'data'   => array(
        'bins_data' => array(
            'issuing_bank' => 'HDFC',
            'bin'           => '512345',
            'category'      => 'creditcard',
            'card_type'     => 'MAST',
            'is_domestic'   => 1,
        ),
    ),
  );
  ```
</Accordion>

## Step 2: Initiate the payment to PayU

<Accordion title="Post Request Syntax & Composition" icon="fa-code">
  Post Request Syntax & Composition for Cards

  ```html
  <body>
  <form action='https://test.payu.in/_payment' method='post'>
  <input type="hidden" name="key" value="JP***g" />
  <input type="hidden" name="txnid" value="t6svtqtjRdl34W" />
  <input type="hidden" name="productinfo" value="iPhone" />
  <input type="hidden" name="amount" value="10" />
  <input type="hidden" name="email" value="test@gmail.com" />
  <input type="hidden" name="firstname" value="Ashish" />
  <input type="hidden" name="lastname" value="Kumar" />
  <input type="hidden" name="pg" value="CC" />
  <input type="hidden" name="bankcode" value="MAST" />
  <input type="hidden" name="ccnum" value="5123456789012346" />
  <input type="hidden" name="ccname" value="Ashish Kumar" />
  <input type="hidden" name="ccvv" value="123" />
  <input type="hidden" name="ccexpmon" value="12" />
  <input type="hidden" name="ccexpyr" value="2021" />
  <input type="hidden" name="surl" value="your own success url" />
  <input type="hidden" name="furl" value="your own failure url" />
  <input type="hidden" name="phone" value="9988776655" />
  <input type="hidden" name="hash" value="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />
  <input type="submit" value="submit"> </form>
  </body>
  </html>
  ```

  <Callout icon="📘" theme="info">
    **Note**: The above code block is for Merchant Checkout integration on the credit card call for the test environment.
  </Callout>
</Accordion>

**Environment**

|                            |                                                                         |
| :------------------------- | :---------------------------------------------------------------------- |
| **Test Environment**       | \<[https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | \<[https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

<Callout icon="📘" theme="info">
  **Reference**: For the **Try It** experience and response, refer to <Anchor label="Collect Payment API - Merchant Hosted Checkout" target="_blank" href="https://docs.payu.in/reference/_payment_merchant_hosted">Collect Payment API - Merchant Hosted Checkout</Anchor> under API Reference.
</Callout>

<Tabs>
  <Tab title="Request Parameters">

**Mandatory Parameters**

| Parameter | Description | Example |
|:----------|:------------|:--------|
| key | The <Glossary>key</Glossary> is the unique merchant key provided by PayU at the time of registration. | JP***g |
| txnid | The <Glossary>txnid</Glossary> is a unique reference ID for the transaction, generated by the merchant. | ashdfu72634 |
| amount | The payment amount for the transaction. | 1000.00 |
| productinfo | The <Glossary>productinfo</Glossary> is a brief description or name of the product being purchased. | iPhone |
| firstname | The first name of the customer. | Ashish |
| email | The email address of the customer. | test@gmail.com |
| phone | The phone number of the customer. | 9988776655 |
| pg | The <Glossary>pg</Glossary> parameter specifies the payment gateway. For card payments, use CC. | CC |
| bankcode | The <Glossary>bankcode</Glossary> is the bank or card network code derived from the card's <Glossary>BIN</Glossary> (e.g., MAST for Mastercard, VISA for Visa). | AMEX |
| ccnum | The 13-19 digit card number (15 digits for AMEX, 13-19 for Maestro). Must be handled in accordance with <Glossary>PCI DSS</Glossary> compliance standards. Validate with the LUHN algorithm. | 5123456789012346 |
| ccname | The name on card as entered by the customer. | Ashish Kumar |
| ccvv | The <Glossary>CVV</Glossary> of the card (3 digits for credit/debit cards, 4 digits for AMEX). Used for <Glossary>Fraud Detection</Glossary>. | 123 |
| ccexpmon | The card expiry month in MM format. For months 1–9, prepend 0 (e.g., 01, 02…09). | 10 |
| ccexpyr | The card expiry year in four digits as entered by the customer. | 2026 |
| furl | The <Glossary>furl</Glossary> is the failure URL to which PayU redirects the customer if the transaction fails. | https://yourwebsite.com/failure |
| surl | The <Glossary>surl</Glossary> is the success URL to which PayU redirects the customer after a successful transaction. | https://yourwebsite.com/success |
| hash | The <Glossary>hash</Glossary> is a security parameter computed using <Glossary>SHA-512</Glossary> encryption to prevent tampering. Formula: `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|`<Glossary>Salt</Glossary>`)` | |

**Optional Parameters**

| Parameter | Description | Example |
|:----------|:------------|:--------|
| address1 | The first line of the billing address. For <Glossary>Fraud Detection</Glossary>: This information is helpful for fraud detection and chargebacks. Provide correct information. | 123 Main St |
| address2 | The second line of the billing address. | Apt 4B |
| city | The city where the customer resides as part of the billing address. | Mumbai |
| state | The state where the customer resides as part of the billing address. | Maharashtra |
| country | The country where the customer resides. | India |
| zipcode | Billing address zip code. Mandatory for cardless <Glossary>EMI</Glossary> option. `Character Limit` - 20 | 400001 |
| udf1 | <Glossary>User Defined Field</Glossary> 1 used to store any information corresponding to a particular transaction. Up to five udfs can be used (udf1–udf5). | custom_value_1 |
| udf2 | User Defined Field 2 used to store any information corresponding to a particular transaction. | custom_value_2 |
| udf3 | User Defined Field 3 used to store any information corresponding to a particular transaction. | custom_value_3 |
| udf4 | User Defined Field 4 used to store any information corresponding to a particular transaction. | custom_value_4 |
| udf5 | User Defined Field 5 used to store any information corresponding to a particular transaction. | custom_value_5 |

  <Accordion title="Understanding Hashing and sample code" icon="fa-code">
    <HashingRequestParameters />

    #### Hashing Sample Code

    <HashingSample />
  </Accordion>

  </Tab>

  <Tab title="Sample Request">

```curl
# IMPORTANT: This is a server-side call, never execute this client-side
# Replace placeholders with actual values
# In production: Use environment variables for sensitive values

curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=YOUR_MERCHANT_KEY" \
  -d "txnid=TXN_12345" \
  -d "amount=1000.00" \
  -d "productinfo=Product+Description" \
  -d "firstname=Customer+Name" \
  -d "email=customer@example.com" \
  -d "phone=9988776655" \
  -d "pg=CC" \
  -d "bankcode=CC" \
  -d "ccnum=CARD_NUMBER" \
  -d "ccexpmon=MM" \
  -d "ccexpyr=YY" \
  -d "ccvv=CVV" \
  -d "ccname=NAME_ON_CARD" \
  -d "surl=https://yourwebsite.com/success" \
  -d "furl=https://yourwebsite.com/failure" \
  -d "hash=HASH_GENERATED_ON_SERVER"
```
```python
import urllib.request
import urllib.parse

url = "https://test.payu.in/_payment"
payload = {
    "key": "YOUR_MERCHANT_KEY",
    "txnid": "TXN_12345",
    "amount": "1000.00",
    "productinfo": "Product Description",
    "firstname": "Customer Name",
    "email": "customer@example.com",
    "phone": "9988776655",
    "pg": "CC",
    "bankcode": "CC",
    "ccnum": "CARD_NUMBER",
    "ccexpmon": "MM",
    "ccexpyr": "YY",
    "ccvv": "CVV",
    "ccname": "NAME_ON_CARD",
    "surl": "https://yourwebsite.com/success",
    "furl": "https://yourwebsite.com/failure",
    "hash": "HASH_GENERATED_ON_SERVER",
}
data = urllib.parse.urlencode(payload).encode("utf-8")
req = urllib.request.Request(url, data=data,
      headers={"Content-Type": "application/x-www-form-urlencoded"}, method="POST")
with urllib.request.urlopen(req) as response:
    print(response.read().decode("utf-8"))
```
```php
<?php
$url = "https://test.payu.in/_payment";
$payload = [
    "key"         => "YOUR_MERCHANT_KEY",
    "txnid"       => "TXN_12345",
    "amount"      => "1000.00",
    "productinfo" => "Product Description",
    "firstname"   => "Customer Name",
    "email"       => "customer@example.com",
    "phone"       => "9988776655",
    "pg"          => "CC",
    "bankcode"    => "CC",
    "ccnum"       => "CARD_NUMBER",
    "ccexpmon"    => "MM",
    "ccexpyr"     => "YY",
    "ccvv"        => "CVV",
    "ccname"      => "NAME_ON_CARD",
    "surl"        => "https://yourwebsite.com/success",
    "furl"        => "https://yourwebsite.com/failure",
    "hash"        => "HASH_GENERATED_ON_SERVER",
];
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ["Content-Type: application/x-www-form-urlencoded"]);
$response = curl_exec($ch);
curl_close($ch);
echo $response;
?>
```
```java
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.StringJoiner;
public class PayUPaymentProcessor {
    public static void main(String[] args) throws Exception {
        String url = "https://test.payu.in/_payment";
        Map<String, String> params = new LinkedHashMap<>();
        params.put("key", "YOUR_MERCHANT_KEY");
        params.put("txnid", "TXN_12345");
        params.put("amount", "1000.00");
        params.put("productinfo", "Product Description");
        params.put("firstname", "Customer Name");
        params.put("email", "customer@example.com");
        params.put("phone", "9988776655");
        params.put("pg", "CC");
        params.put("bankcode", "CC");
        params.put("ccnum", "CARD_NUMBER");
        params.put("ccexpmon", "MM");
        params.put("ccexpyr", "YY");
        params.put("ccvv", "CVV");
        params.put("ccname", "NAME_ON_CARD");
        params.put("surl", "https://yourwebsite.com/success");
        params.put("furl", "https://yourwebsite.com/failure");
        params.put("hash", "HASH_GENERATED_ON_SERVER");
        StringJoiner formData = new StringJoiner("&");
        for (Map.Entry<String, String> e : params.entrySet())
            formData.add(URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "=" + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8));
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData.toString()))
                .build();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
    }
}
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;
class PayUPaymentProcessor {
    static async Task Main(string[] args) {
        using var client = new HttpClient();
        var formData = new FormUrlEncodedContent(new[] {
            new KeyValuePair<string, string>("key",         "YOUR_MERCHANT_KEY"),
            new KeyValuePair<string, string>("txnid",       "TXN_12345"),
            new KeyValuePair<string, string>("amount",      "1000.00"),
            new KeyValuePair<string, string>("productinfo", "Product Description"),
            new KeyValuePair<string, string>("firstname",   "Customer Name"),
            new KeyValuePair<string, string>("email",       "customer@example.com"),
            new KeyValuePair<string, string>("phone",       "9988776655"),
            new KeyValuePair<string, string>("pg",          "CC"),
            new KeyValuePair<string, string>("bankcode",    "CC"),
            new KeyValuePair<string, string>("ccnum",       "CARD_NUMBER"),
            new KeyValuePair<string, string>("ccexpmon",    "MM"),
            new KeyValuePair<string, string>("ccexpyr",     "YY"),
            new KeyValuePair<string, string>("ccvv",        "CVV"),
            new KeyValuePair<string, string>("ccname",      "NAME_ON_CARD"),
            new KeyValuePair<string, string>("surl",        "https://yourwebsite.com/success"),
            new KeyValuePair<string, string>("furl",        "https://yourwebsite.com/failure"),
            new KeyValuePair<string, string>("hash",        "HASH_GENERATED_ON_SERVER")
        });
        var response = await client.PostAsync("https://test.payu.in/_payment", formData);
        Console.WriteLine(await response.Content.ReadAsStringAsync());
    }
}
```

  </Tab>
</Tabs>

#### Sample request for saved card

<Accordion title="Sample request for saved card" icon="fa-code">

<Tabs>
  <Tab title="Request Parameters">

**Mandatory Parameters**

| Parameter | Description | Example |
|:----------|:------------|:--------|
| key | The unique merchant key provided by PayU at the time of registration. | Your Test Key |
| txnid | A unique reference ID for the transaction, generated by the merchant. It must be unique — PayU's system will not accept duplicate transaction IDs. | s7hhDQVWvbhBdN |
| amount | The payment amount for the transaction. For the cardless EMI option, the amount must be at least Rs. 8000. | 10.00 |
| productinfo | A brief description of the product. `Character Limit` - 100 | iPhone |
| firstname | The first name of the customer. `Character Limit` - 60 | Ashish |
| email | The email of the customer. `Character Limit` - 50 | test@gmail.com |
| phone | The phone number of the customer. **Note**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information. | 9876543210 |
| lastname | The last name of the customer. `Character Limit` - 60 | Verma |
| surl | The success URL — the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there. | https://apiplayground-response.herokuapp.com/ |
| furl | The failure URL — the page PayU will redirect to if the transaction fails. The merchant can handle the response at this URL after the customer is redirected there. | https://apiplayground-response.herokuapp.com/ |
| hash | The security hash used to avoid the possibility of transaction tampering. For more information on hash generation, refer to [Generate Hash](doc:generate-hash-merchant-hosted). | eabec285da28fd... |
| pg | The payment gateway type. Use 'CC' for card payments. | CC |
| bankcode | Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value. | AMEX |
| ccexpmon | The network token expiry month. | 10 |
| ccexpyr | The network token expiry year. | 2022 |
| store_card_token | The <Glossary>Saved Card</Glossary> network token generated at your end. | 1234 4567 2456 3566 |
| storecard_token_type | The store card token type. For this scenario, include 1. | 1 |
| additional_info | Additional information required for processing the saved card transaction, in JSON format: `{"last4Digits": "1234", "<Glossary>TAVV</Glossary>": "ABCDEFGH", "<Glossary>trid</Glossary>": "1234567890", "<Glossary>tokenRefNo</Glossary>": "abcde123456"}`. The <Glossary>last4Digits</Glossary> field contains the last four digits of the tokenized card. | `{"last4Digits": "1234", "TAVV": "ABCDEFGH", "trid": "1234567890", "tokenRefNo": "abcde123456"}` |

**Optional Parameters**

| Parameter | Description | Example |
|:----------|:------------|:--------|
| api_version | The API version for this API. | 1 |
| address1 | The first line of the billing address. `Character Limit` - 100 | H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai |
| address2 | The second line of the billing address. `Character Limit` - 100 | 34 Saikripa-Estate, Tilak Nagar |
| city | The city where the customer resides as part of the billing address. | Mumbai |
| state | The state where the customer resides as part of the billing address. | Maharashtra |
| country | The country where the customer resides. `Character Limit` - 50 | India |
| zipcode | Billing address zip code. Mandatory for the cardless EMI option. `Character Limit` - 20 | 400004 |
| udf1 | User Defined Field 1 used to store any information corresponding to a particular transaction. Up to five udfs can be used (udf1–udf5). `Character Limit` - 255 | Payment Preference |
| udf2 | User Defined Field 2 used to store any information corresponding to a particular transaction. `Character Limit` - 255 | Shipping Method |
| udf3 | User Defined Field 3 used to store any information corresponding to a particular transaction. `Character Limit` - 255 | Shipping Address |
| udf4 | User Defined Field 4 used to store any information corresponding to a particular transaction. `Character Limit` - 255 | Shipping City |
| udf5 | User Defined Field 5 used to store any information corresponding to a particular transaction. `Character Limit` - 255 | Shipping Zip Code |
| ccnum | The 13 to 19-digit card number for credit or debit cards. | 512***6789012346 |
| ccname | The customer's name on card. | Ashish |
| ccvv | The CVV number of the card as entered by the customer. | 123 |

  </Tab>

  <Tab title="Sample Request">

```curl
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=YourMerchantKey" \
  -d "txnid=NT_TXN_1234567890" \
  -d "amount=250.00" \
  -d "productinfo=Premium Subscription Plan" \
  -d "firstname=John" \
  -d "lastname=Doe" \
  -d "email=john.doe@example.com" \
  -d "phone=9876543210" \
  -d "surl=https://yourwebsite.com/payment/success" \
  -d "furl=https://yourwebsite.com/payment/failure" \
  -d "pg=CC" \
  -d "bankcode=VISA" \
  -d "ccexpmon=12" \
  -d "ccexpyr=2025" \
  -d "ccname=John Doe" \
  -d "store_card_token=4111111111111111" \
  -d "storecard_token_type=1" \
  -d "additional_info={\"last4Digits\":\"1111\",\"TAVV\":\"ABCD1234EFGH5678\",\"trid\":\"987654321012345\",\"tokenRefNo\":\"TKN_REF_12345678\"}" \
  -d "api_version=1" \
  -d "address1=123 Business District" \
  -d "address2=Tech Park Avenue" \
  -d "city=Bangalore" \
  -d "state=Karnataka" \
  -d "country=India" \
  -d "zipcode=560001" \
  -d "udf1=Premium_Plan" \
  -d "udf2=Monthly_Billing" \
  -d "udf3=Customer_ID_789" \
  -d "udf4=" \
  -d "udf5=" \
  -d "hash=b5c6d8e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9"
```
```python
import requests

url = "https://test.payu.in/_payment"
headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "key":                  "YourMerchantKey",
    "txnid":                "NT_TXN_1234567890",
    "amount":               "250.00",
    "productinfo":          "Premium Subscription Plan",
    "firstname":            "John",
    "lastname":             "Doe",
    "email":                "john.doe@example.com",
    "phone":                "9876543210",
    "surl":                 "https://yourwebsite.com/payment/success",
    "furl":                 "https://yourwebsite.com/payment/failure",
    "pg":                   "CC",
    "bankcode":             "VISA",
    "ccexpmon":             "12",
    "ccexpyr":              "2025",
    "ccname":               "John Doe",
    "store_card_token":     "4111111111111111",
    "storecard_token_type": "1",
    "additional_info":      '{"last4Digits":"1111","TAVV":"ABCD1234EFGH5678","trid":"987654321012345","tokenRefNo":"TKN_REF_12345678"}',
    "api_version":          "1",
    "address1":             "123 Business District",
    "address2":             "Tech Park Avenue",
    "city":                 "Bangalore",
    "state":                "Karnataka",
    "country":              "India",
    "zipcode":              "560001",
    "udf1":                 "Premium_Plan",
    "udf2":                 "Monthly_Billing",
    "udf3":                 "Customer_ID_789",
    "udf4":                 "",
    "udf5":                 "",
    "hash":                 "b5c6d8e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9"
}
response = requests.post(url, headers=headers, data=data)
print("Status Code:", response.status_code)
print("Response:", response.text)
```
```php
<?php
$url = "https://test.payu.in/_payment";
$data = http_build_query([
    "key"                  => "YourMerchantKey",
    "txnid"                => "NT_TXN_1234567890",
    "amount"               => "250.00",
    "productinfo"          => "Premium Subscription Plan",
    "firstname"            => "John",
    "lastname"             => "Doe",
    "email"                => "john.doe@example.com",
    "phone"                => "9876543210",
    "surl"                 => "https://yourwebsite.com/payment/success",
    "furl"                 => "https://yourwebsite.com/payment/failure",
    "pg"                   => "CC",
    "bankcode"             => "VISA",
    "ccexpmon"             => "12",
    "ccexpyr"              => "2025",
    "ccname"               => "John Doe",
    "store_card_token"     => "4111111111111111",
    "storecard_token_type" => "1",
    "additional_info"      => '{"last4Digits":"1111","TAVV":"ABCD1234EFGH5678","trid":"987654321012345","tokenRefNo":"TKN_REF_12345678"}',
    "api_version"          => "1",
    "address1"             => "123 Business District",
    "address2"             => "Tech Park Avenue",
    "city"                 => "Bangalore",
    "state"                => "Karnataka",
    "country"              => "India",
    "zipcode"              => "560001",
    "udf1"                 => "Premium_Plan",
    "udf2"                 => "Monthly_Billing",
    "udf3"                 => "Customer_ID_789",
    "udf4"                 => "",
    "udf5"                 => "",
    "hash"                 => "b5c6d8e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9"
]);
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "accept: application/json",
    "Content-Type: application/x-www-form-urlencoded"
]);
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```
```java
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.StringJoiner;
public class SavedCardRequest {
    public static void main(String[] args) throws Exception {
        String url = "https://test.payu.in/_payment";
        Map<String, String> params = new LinkedHashMap<>();
        params.put("key",                  "YourMerchantKey");
        params.put("txnid",                "NT_TXN_1234567890");
        params.put("amount",               "250.00");
        params.put("productinfo",          "Premium Subscription Plan");
        params.put("firstname",            "John");
        params.put("lastname",             "Doe");
        params.put("email",                "john.doe@example.com");
        params.put("phone",                "9876543210");
        params.put("surl",                 "https://yourwebsite.com/payment/success");
        params.put("furl",                 "https://yourwebsite.com/payment/failure");
        params.put("pg",                   "CC");
        params.put("bankcode",             "VISA");
        params.put("ccexpmon",             "12");
        params.put("ccexpyr",              "2025");
        params.put("ccname",               "John Doe");
        params.put("store_card_token",     "4111111111111111");
        params.put("storecard_token_type", "1");
        params.put("additional_info",      "{\"last4Digits\":\"1111\",\"TAVV\":\"ABCD1234EFGH5678\",\"trid\":\"987654321012345\",\"tokenRefNo\":\"TKN_REF_12345678\"}");
        params.put("api_version",          "1");
        params.put("address1",             "123 Business District");
        params.put("address2",             "Tech Park Avenue");
        params.put("city",                 "Bangalore");
        params.put("state",                "Karnataka");
        params.put("country",              "India");
        params.put("zipcode",              "560001");
        params.put("udf1",                 "Premium_Plan");
        params.put("udf2",                 "Monthly_Billing");
        params.put("udf3",                 "Customer_ID_789");
        params.put("udf4",                 "");
        params.put("udf5",                 "");
        params.put("hash",                 "b5c6d8e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9");
        StringJoiner formData = new StringJoiner("&");
        for (Map.Entry<String, String> entry : params.entrySet())
            formData.add(URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8) + "=" + URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8));
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData.toString()))
                .build();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;
class SavedCardRequest {
    static async Task Main(string[] args) {
        using var client = new HttpClient();
        client.DefaultRequestHeaders.Add("accept", "application/json");
        var formData = new FormUrlEncodedContent(new[] {
            new KeyValuePair<string, string>("key",                  "YourMerchantKey"),
            new KeyValuePair<string, string>("txnid",                "NT_TXN_1234567890"),
            new KeyValuePair<string, string>("amount",               "250.00"),
            new KeyValuePair<string, string>("productinfo",          "Premium Subscription Plan"),
            new KeyValuePair<string, string>("firstname",            "John"),
            new KeyValuePair<string, string>("lastname",             "Doe"),
            new KeyValuePair<string, string>("email",                "john.doe@example.com"),
            new KeyValuePair<string, string>("phone",                "9876543210"),
            new KeyValuePair<string, string>("surl",                 "https://yourwebsite.com/payment/success"),
            new KeyValuePair<string, string>("furl",                 "https://yourwebsite.com/payment/failure"),
            new KeyValuePair<string, string>("pg",                   "CC"),
            new KeyValuePair<string, string>("bankcode",             "VISA"),
            new KeyValuePair<string, string>("ccexpmon",             "12"),
            new KeyValuePair<string, string>("ccexpyr",              "2025"),
            new KeyValuePair<string, string>("ccname",               "John Doe"),
            new KeyValuePair<string, string>("store_card_token",     "4111111111111111"),
            new KeyValuePair<string, string>("storecard_token_type", "1"),
            new KeyValuePair<string, string>("additional_info",      "{\"last4Digits\":\"1111\",\"TAVV\":\"ABCD1234EFGH5678\",\"trid\":\"987654321012345\",\"tokenRefNo\":\"TKN_REF_12345678\"}"),
            new KeyValuePair<string, string>("api_version",          "1"),
            new KeyValuePair<string, string>("address1",             "123 Business District"),
            new KeyValuePair<string, string>("address2",             "Tech Park Avenue"),
            new KeyValuePair<string, string>("city",                 "Bangalore"),
            new KeyValuePair<string, string>("state",                "Karnataka"),
            new KeyValuePair<string, string>("country",              "India"),
            new KeyValuePair<string, string>("zipcode",              "560001"),
            new KeyValuePair<string, string>("udf1",                 "Premium_Plan"),
            new KeyValuePair<string, string>("udf2",                 "Monthly_Billing"),
            new KeyValuePair<string, string>("udf3",                 "Customer_ID_789"),
            new KeyValuePair<string, string>("udf4",                 ""),
            new KeyValuePair<string, string>("udf5",                 ""),
            new KeyValuePair<string, string>("hash",                 "b5c6d8e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9")
        });
        var response = await client.PostAsync("https://test.payu.in/_payment", formData);
        string responseBody = await response.Content.ReadAsStringAsync();
        Console.WriteLine("Status Code: " + (int)response.StatusCode);
        Console.WriteLine("Response: " + responseBody);
    }
}
```

  </Tab>
</Tabs>

</Accordion>

## Step 3: Check response from PayU

<ReverseHashing />

<Accordion title="Sample response (parsed)" icon="fa-code">
  * Success scenario

  ```
  Array
  (
      [mihpayid] => 403993715524069222
      [mode] => CC
      [status] => success
      [unmappedstatus] => captured
      [key] => JF***g
      [txnid] => EaE4ZO3vU4iPsp
      [amount] => 10.00
      [cardCategory] => domestic
      [discount] => 0.00
      [net_amount_debit] => 10
      [addedon] => 2021-09-08 19:37:19
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
      [hash] => ed99957adb08fea56c907b88e8d158a79c3562c67f96c298461509826f77a7ae9e88b2a176b3234c25f50bcd451271728719656f3bb59c13a52bebabc468615a
      [field1] => 0608273386032718000015
      [field2] => 986987
      [field3] => 10.00
      [field4] => 403993715524069222
      [field5] => 100
      [field6] => 02
      [field7] => AUTHPOSITIVE
      [field8] => 
      [field9] => Transaction is Successful
      [payment_source] => payu
      [PG_TYPE] => CC-PG
      [bank_ref_num] => 0608273386032718000015
      [bankcode] => CC
      [error] => E000
      [error_Message] => No Error
      [name_on_card] => payu
      [cardnum] => 512345XXXXXX2346
  )
  ```

  * Failure scenario

  ```
  Array
  (
      [mihpayid] => 20869277619
      [mode] => CC
      [status] => failure
      [unmappedstatus] => failed
      [key] => L43t1c
      [txnid] => 26ba7cd6a67b0a010542
      [amount] => 1.00
      [cardCategory] => domestic
      [discount] => 0.00
      [net_amount_debit] => 0.00
      [addedon] => 2024-09-05 17:46:10
      [productinfo] => Product Info
      [firstname] => Payu-Admin
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => test@example.com
      [phone] => 1234567890
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
      [hash] => ac7720e4bc33e5494bec6d37302e522171175a987f9d47286bfd29e8a7fc794f56433fcacf0bc120db781c4dc1d05a4857d71e83f00f6ed6aa9c97a1938b9467
      [field1] => 
      [field2] => 
      [field3] => 
      [field4] => 
      [field5] => 05
      [field6] => 
      [field7] => AUTHNEGATIVE
      [field8] => 
      [field9] => Authorization failed at Bank
      [payment_source] => payu
      [pa_name] => PayU
      [PG_TYPE] => CC-PG
      [bank_ref_num] => 2409052690
      [bankcode] => AMEX
      [error] => E1903
      [error_Message] => Authorization failed at Bank
      [cardnum] => XXXXXXXXXXXX2003
      [cardhash] => This field is no longer supported in postback params.
  )
  ```

  <br />
</Accordion>

## Step 4: Verify the Payment

<Verify_Payment_Tabs />

## Handling Guest Checkout Transactions

Guest Checkout is a valuable feature that can provided be enabled for your e-commerce websites. It allows your customers to make purchases without the need to sign in or create a user account. This streamlined process benefits one-time or occasional shoppers, as it eliminates the registration step, leading to faster transactions and enhanced customer satisfaction.

<Callout icon="📘" theme="info">
  ###

  **Enable Guest Checkout**: To enable this feature, contact your PayU Key Account Manager or PayU Integration Support.
</Callout>

As per RBI compliances, acquirers are also not allowed to store card details after a stipulated timeline. As per recommendations from RBI end, Guest checkout transactions won't be allowed post 31st Oct. 2023. Guest checkout PAN should be replaced with some alternative number for transaction processing. As per the new regulations on guest checkout, where we have to tokenise plain card numbers. This token is called Alternative ID or Alt ID.

There are three scenarios with Alternative ID:

<Image src="https://files.readme.io/f84108124634526cf547dac1d59ff3272600f8cfd26f486baba8425033ddf5c8-Guest-checkout-alt-id-implementation-methods.png" align="center" width="900px" />

<Accordion title="Scenario 1: Provision & processes guest transaction with PayU" icon="fa-code">
  No changes required in the **\_payment** request used to collect payments.
</Accordion>

<Accordion title="Scenario 2: Provision Alt ID outside PayU and use PayU to Process Transaction" icon="fa-code">
  #### Request parameters

  Along with the parameters listed in the <Anchor label="Collect Payment API - Cards (Merchant Hosted Checkout)" target="_blank" href="https://docs.payu.in/reference/_payment_merchant_hosted_cards">Collect Payment API - Cards (Merchant Hosted Checkout)</Anchor>, you have to pass alt ID as a variable and pass TAVV (Cryptogram), last four digits and **par** parameter as part of **additional\_info** JSON. There is no change in the response and it remains the same.

  <Callout icon="📘" theme="info">
    **Note**: The **par** parameter is optional as part of **additional\_info** JSON.
  </Callout>

<Tabs>
  <Tab title="Request Parameters">

**Mandatory Parameters**

| Parameter | Description | Example |
|:----------|:------------|:--------|
| key | The unique merchant key provided by PayU at the time of registration. | JP***g |
| txnid | A unique reference ID for the transaction, generated by the merchant. | ashdfu72634 |
| amount | The payment amount for the transaction. | |
| productinfo | A brief description of the product. | |
| firstname | The first name of the customer. | Ashish |
| email | The email address of the customer. | |
| phone | The phone number of the customer. | |
| pg | The payment gateway type. For cards, use 'CC'. | CC |
| bankcode | Each payment option is identified with a unique bank code at PayU. The merchant must post the corresponding bank code value. For more information, refer to Card Type Codes and Supported Banks for Cards. | AMEX |
| ccname | The name on card as entered by the customer. | Ashish Kumar |
| ccvv | The CVV of the card (3 digits for credit/debit cards, 4 digits for AMEX). Validate with BIN API. | 123 |
| ccexpmon | The card's expiry month or Alt ID expiry month for <Glossary>Guest Checkout</Glossary>. Must be in MM format. For months 1–9, prepend 0 (e.g., 01, 02…09). For VISA cards, the plain card's expiry month must be posted. | 10 |
| ccexpyr | The card's expiry year or Alt ID expiry year for Guest Checkout. Must be four digits. For VISA cards, the plain card's expiry year must be posted. | 2021 |
| alt_id | The Alt ID for the guest checkout transaction. | |
| furl | The failure URL — the page PayU will redirect to if the transaction fails. | |
| surl | The success URL — the page PayU will redirect to if the transaction is successful. | |
| hash | The security hash. Formula: `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | |
| additional_info | Additional information in JSON format containing TAVV (Cryptogram), last four digits, and par. For more information, refer to [additional_info JSON sample and field description](#additional_info-json-sample-and-field-description). | |

**Optional Parameters**

| Parameter | Description | Example |
|:----------|:------------|:--------|
| address1 | The first line of the billing address. For Fraud Detection: This information is helpful for fraud detection and chargebacks. Provide correct information. | |
| address2 | The second line of the billing address. | |
| city | The city where the customer resides as part of the billing address. | |
| state | The state where the customer resides as part of the billing address. | |
| country | The country where the customer resides. | |
| zipcode | Billing address zip code. Mandatory for the cardless EMI option. Character Limit - 20 | |
| udf1 | User Defined Field 1 used to store any information corresponding to a particular transaction. Up to five udfs can be used (udf1–udf5). | |
| udf2 | User Defined Field 2 used to store any information corresponding to a particular transaction. | |
| udf3 | User Defined Field 3 used to store any information corresponding to a particular transaction. | |
| udf4 | User Defined Field 4 used to store any information corresponding to a particular transaction. | |
| udf5 | User Defined Field 5 used to store any information corresponding to a particular transaction. | |

  <Callout icon="📘" theme="info">
    **Note**: **tokenReferenceid** field is required in the additional\_info parameter if you are provisioning Alt ID outside PayU for Diners card.
  </Callout>

  #### additional\_info JSON sample and field description

  ```
  {  
  "tavv":"AKF/FaM3BPWoAAEWYTiQAAADFA==",  
  "last4Digits":"2346",  
  "par":"799F3ED865F5965CC760A32682BA8A80F19E99ECB3F7F03574C14F5B6C3EB2C1",  
  "tokenReferenceId":"3acdd709-3c4b-4280-a6db-3f02271d09a3"  
  }
  ```

  The description of the fields in the additional\_info JSON.

  | Field            | Description                                                                                                                                                                   |
  | :--------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | trid             | trid is the acronym for Token Requestor ID and it is the identity given by the networks for creating the tokens. You should be able to get the same from your token provider. |
  | tokenReferenceID | The Token Reference ID is generated along with the network token. You should be able to get the same from your token provider.                                                |
  | TAVV             | It is a token authentication verification value given by schemes or interchange. Also, known as cryptogram.                                                                   |

  </Tab>

  <Tab title="Sample Request">

```curl
curl --location 'http://local.secure.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=smsplus' \
--data-urlencode 'firstname={{firstname}}' \
--data-urlencode 'email={{email}}' \
--data-urlencode 'amount={{amount}}' \
--data-urlencode 'phone=9999999999' \
--data-urlencode 'productinfo={{productinfo}}' \
--data-urlencode 'surl=your own success url' \
--data-urlencode 'furl=your own failure url' \
--data-urlencode 'pg=CC' \
--data-urlencode 'bankcode=MASTERCARD' \
--data-urlencode 'alt_id=5123456789012346' \
--data-urlencode 'additional_info={"tavv":"AKF/FaM3BPWoAAEWYTiQAAADFA==","last4Digits":"2346","par":"799F3ED865F5965CC760A32682BA8A80F19E99ECB3F7F03574C14F5B6C3EB2C1","tokenReferenceId":"3acdd709-3c4b-4280-a6db-3f02271d09a3"}' \
--data-urlencode 'ccname=Flipkart' \
--data-urlencode 'ccvv=126' \
--data-urlencode 'ccexpmon=05' \
--data-urlencode 'ccexpyr=2024' \
--data-urlencode 'txnid={{txnid}}' \
--data-urlencode 'hash={{hash}}'
```
```python
import requests

url = "http://local.secure.payu.in/_payment"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = {
    "key":             "smsplus",
    "firstname":       "{{firstname}}",
    "email":           "{{email}}",
    "amount":          "{{amount}}",
    "phone":           "9999999999",
    "productinfo":     "{{productinfo}}",
    "surl":            "your own success url",
    "furl":            "your own failure url",
    "pg":              "CC",
    "bankcode":        "MASTERCARD",
    "alt_id":          "5123456789012346",
    "additional_info": '{"tavv":"AKF/FaM3BPWoAAEWYTiQAAADFA==","last4Digits":"2346","par":"799F3ED865F5965CC760A32682BA8A80F19E99ECB3F7F03574C14F5B6C3EB2C1","tokenReferenceId":"3acdd709-3c4b-4280-a6db-3f02271d09a3"}',
    "ccname":          "Flipkart",
    "ccvv":            "126",
    "ccexpmon":        "05",
    "ccexpyr":         "2024",
    "txnid":           "{{txnid}}",
    "hash":            "{{hash}}"
}
response = requests.post(url, headers=headers, data=data)
print("Status Code:", response.status_code)
print("Response:", response.text)
```
```php
<?php
$url = "http://local.secure.payu.in/_payment";
$data = http_build_query([
    "key"             => "smsplus",
    "firstname"       => "{{firstname}}",
    "email"           => "{{email}}",
    "amount"          => "{{amount}}",
    "phone"           => "9999999999",
    "productinfo"     => "{{productinfo}}",
    "surl"            => "your own success url",
    "furl"            => "your own failure url",
    "pg"              => "CC",
    "bankcode"        => "MASTERCARD",
    "alt_id"          => "5123456789012346",
    "additional_info" => '{"tavv":"AKF/FaM3BPWoAAEWYTiQAAADFA==","last4Digits":"2346","par":"799F3ED865F5965CC760A32682BA8A80F19E99ECB3F7F03574C14F5B6C3EB2C1","tokenReferenceId":"3acdd709-3c4b-4280-a6db-3f02271d09a3"}',
    "ccname"          => "Flipkart",
    "ccvv"            => "126",
    "ccexpmon"        => "05",
    "ccexpyr"         => "2024",
    "txnid"           => "{{txnid}}",
    "hash"            => "{{hash}}"
]);
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_HTTPHEADER, ["Content-Type: application/x-www-form-urlencoded"]);
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```
```java
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.StringJoiner;
public class GuestCheckoutRequest {
    public static void main(String[] args) throws Exception {
        String url = "http://local.secure.payu.in/_payment";
        Map<String, String> params = new LinkedHashMap<>();
        params.put("key",             "smsplus");
        params.put("firstname",       "{{firstname}}");
        params.put("email",           "{{email}}");
        params.put("amount",          "{{amount}}");
        params.put("phone",           "9999999999");
        params.put("productinfo",     "{{productinfo}}");
        params.put("surl",            "your own success url");
        params.put("furl",            "your own failure url");
        params.put("pg",              "CC");
        params.put("bankcode",        "MASTERCARD");
        params.put("alt_id",          "5123456789012346");
        params.put("additional_info", "{\"tavv\":\"AKF/FaM3BPWoAAEWYTiQAAADFA==\",\"last4Digits\":\"2346\",\"par\":\"799F3ED865F5965CC760A32682BA8A80F19E99ECB3F7F03574C14F5B6C3EB2C1\",\"tokenReferenceId\":\"3acdd709-3c4b-4280-a6db-3f02271d09a3\"}");
        params.put("ccname",          "Flipkart");
        params.put("ccvv",            "126");
        params.put("ccexpmon",        "05");
        params.put("ccexpyr",         "2024");
        params.put("txnid",           "{{txnid}}");
        params.put("hash",            "{{hash}}");
        StringJoiner formData = new StringJoiner("&");
        for (Map.Entry<String, String> entry : params.entrySet())
            formData.add(URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8) + "=" + URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8));
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData.toString()))
                .build();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;
class GuestCheckoutRequest {
    static async Task Main(string[] args) {
        using var client = new HttpClient();
        var formData = new FormUrlEncodedContent(new[] {
            new KeyValuePair<string, string>("key",             "smsplus"),
            new KeyValuePair<string, string>("firstname",       "{{firstname}}"),
            new KeyValuePair<string, string>("email",           "{{email}}"),
            new KeyValuePair<string, string>("amount",          "{{amount}}"),
            new KeyValuePair<string, string>("phone",           "9999999999"),
            new KeyValuePair<string, string>("productinfo",     "{{productinfo}}"),
            new KeyValuePair<string, string>("surl",            "your own success url"),
            new KeyValuePair<string, string>("furl",            "your own failure url"),
            new KeyValuePair<string, string>("pg",              "CC"),
            new KeyValuePair<string, string>("bankcode",        "MASTERCARD"),
            new KeyValuePair<string, string>("alt_id",          "5123456789012346"),
            new KeyValuePair<string, string>("additional_info", "{\"tavv\":\"AKF/FaM3BPWoAAEWYTiQAAADFA==\",\"last4Digits\":\"2346\",\"par\":\"799F3ED865F5965CC760A32682BA8A80F19E99ECB3F7F03574C14F5B6C3EB2C1\",\"tokenReferenceId\":\"3acdd709-3c4b-4280-a6db-3f02271d09a3\"}"),
            new KeyValuePair<string, string>("ccname",          "Flipkart"),
            new KeyValuePair<string, string>("ccvv",            "126"),
            new KeyValuePair<string, string>("ccexpmon",        "05"),
            new KeyValuePair<string, string>("ccexpyr",         "2024"),
            new KeyValuePair<string, string>("txnid",           "{{txnid}}"),
            new KeyValuePair<string, string>("hash",            "{{hash}}")
        });
        var response = await client.PostAsync("http://local.secure.payu.in/_payment", formData);
        string responseBody = await response.Content.ReadAsStringAsync();
        Console.WriteLine("Status Code: " + (int)response.StatusCode);
        Console.WriteLine("Response: " + responseBody);
    }
}
```

  </Tab>
</Tabs>

</Accordion>

<Accordion title="Sample response" icon="fa-code">
  > 📘 Notes:
  >
  > The **authRefNo** response parameter contains:
  >
  > * <Glossary>AEVV</Glossary> number for an AMEX card transaction. This is mandatory for AMEX for compliance for token (<Glossary>CoFT</Glossary>) provisioning.
  > * rupayAuthRefId for a Rupay card transaction
  >
  > To enable the  **authRefNo** response parameter in response, contact your PayU Key Account Manager or [PayU Support](https://help.payu.in).

  ```json
  Array
  (
      [mihpayid] => 20869277619
      [mode] => CC
      [status] => failure
      [unmappedstatus] => failed
      [key] => L43t1c
      [txnid] => 26ba7cd6a67b0a010542
      [amount] => 1.00
      [authRefNo] => AAAXXXlxAAICQkXXXEAEAAXXXX=
      [corporate_card] => 0
      [cobranded_card] => AMEX_CONSUMER
  )
  ```

  <br />
</Accordion>

<Accordion title="Scenario 3: Provision Alt ID from PayU" icon="fa-code">
  The Provision Alt ID API is used to provision Alt ID from PayU, but process transaction outside PayU. For more information, refer to <Anchor label="Provision Alt ID API" target="_blank" href="https://docs.payu.in/reference/provision-alt-id-api">Provision Alt ID API</Anchor>.
</Accordion>

## Handling 3DS Secure 2.0 Transaction

PayU supports 3DS Secure 2.0 transaction with Merchant Hosted Checkout integration. This section provides the information relevant to 3DS Secure 2.0 transaction.

You must include the `threeDS2RequestData` parameter along with the regular Collect Payment API for cards.

<Callout icon="📘" theme="info">
  **Reference**: For the **Try It** experience, refer to  [Collect Payment API - Cards (Merchant Hosted Checkout)](https://docs.payu.in/reference/_payment_merchant_hosted_cards),
</Callout>

<Tabs>
  <Tab title="Request Parameters">

**Mandatory Parameters**

| Parameter | Description | Example |
|:----------|:------------|:--------|
| key | The unique merchant key provided by PayU at the time of registration. | JF****g |
| txnid | A unique reference ID for the transaction, generated by the merchant. | jYhbOYH9o4 |
| amount | The payment amount for the transaction. | 10 |
| productinfo | A brief description of the product. | Product_info |
| firstname | The first name of the customer. | Ashish |
| email | The email address of the customer. | test@example.com |
| phone | The phone number of the customer. | 9876543210 |
| pg | The payment gateway type. For cards, use 'CC'. | CC |
| bankcode | Each payment option is identified with a unique bank code at PayU. The merchant must post the corresponding bank code value. | CC |
| ccnum | The 13-19 digit card number (15 digits for AMEX, 13-19 for Maestro). Validate with the LUHN algorithm. | 4012000000002004 |
| ccname | The name on card as entered by the customer. | Test User |
| ccvv | The CVV of the card (3 digits for credit/debit cards, 4 digits for AMEX). Validate with BIN API. | 123 |
| ccexpmon | The card's expiry month in MM format. For months 1–9, prepend 0 (e.g., 01, 02…09). | 06 |
| ccexpyr | The card's expiry year in four digits. | 2024 |
| surl | The success URL — the page PayU will redirect to if the transaction is successful. | http://pp30admin.payu.in/test_response |
| furl | The failure URL — the page PayU will redirect to if the transaction fails. | http://pp30admin.payu.in/test_response |
| hash | The security hash. Formula: `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | e5b286a9... |

**Optional Parameters**

| Parameter | Description | Example |
|:----------|:------------|:--------|
| lastname | The last name of the customer. | Test |
| txn_s2s_flow | The <Glossary>txn_s2s_flow</Glossary> parameter specifies the server-to-server flow type for the transaction. | 4 |
| threeDS2RequestData | The <Glossary>threeDS2RequestData</Glossary> contains additional authentication data required for 3DS Secure 2.0 compliance, including browser information, user agent, screen dimensions, and timezone. | Refer to threeDS2RequestData JSON format below |

  #### threeDS2RequestData JSON format

  The following JSON format is used for 3DS Secure 2.0 support for cards:

  ```json
  "browserInfo": {
      "userAgent": "Mozilla\/5.0 (X11 Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) HeadlessChrome\/93.0.4577.0 Safari\/537.36",
      "acceptHeader": "*\/*",
      "language": "en-US",
      "colorDepth": "24",
      "screenHeight": "600",
      "screenWidth": "800",
      "timeZone": "-300",
      "javaEnabled": true,
      "ip": "10.248.2.71"
  }
  ```

  #### 3DS Secure 2.0 browserDetails JSON Fields Description

  | **Field**    | **Description**                                                                             | **Example**      |
  | ------------ | ------------------------------------------------------------------------------------------- | ---------------- |
  | userAgent    | This field must include user agent of the device browser.                                   |                  |
  | acceptHeader | This field contains the format of the header.                                               | application/json |
  | language     | This field contains the language for the 3D Secure Challenge.                               | en-US            |
  | colorDepth   | This field contains the color depth of the screen.                                          | 24               |
  | screenHeight | This field contains the screen height of the device displaying the 3D Secure Challenge.     | 640              |
  | screenWidth  | This field contains the screen width of the device displaying the 3D Secure Challenge.      | 480              |
  | javaEnabled  | This field contains whether Java is enabled for the device.                                 | true             |
  | timeZone     | This field contains the time zone code where the payment is accepted.                       | 273              |
  | ip           | This should include the IP address of the device from which the browser is accessed.        | 10.248.2.71      |

  </Tab>

  <Tab title="Sample Request">

```curl
curl --location 'https://test.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e' \
--data-urlencode 'key=JF****g' \
--data-urlencode 'firstname=Ashish' \
--data-urlencode 'email=test@example.com' \
--data-urlencode 'amount=10' \
--data-urlencode 'phone= 9876543210' \
--data-urlencode 'productinfo=Product_info' \
--data-urlencode 'surl=http://pp30admin.payu.in/test_response' \
--data-urlencode 'furl=http://pp30admin.payu.in/test_response' \
--data-urlencode 'pg=CC' \
--data-urlencode 'bankcode=CC' \
--data-urlencode 'lastname=Test' \
--data-urlencode 'ccname=Test User' \
--data-urlencode 'ccvv=123' \
--data-urlencode 'ccexpmon=06' \
--data-urlencode 'ccexpyr=2024' \
--data-urlencode 'txnid=jYhbOYH9o4' \
--data-urlencode 'hash=e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184' \
--data-urlencode 'ccnum=4012000000002004' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 'threeDS2RequestData={"browserInfo":{"userAgent":"Mozilla\/5.0","acceptHeader":"*\/*","language":"en-US","colorDepth":"24","screenHeight":"600","screenWidth":"800","timeZone":"-300","javaEnabled":true,"ip":"10.248.2.71"}}'
```
```python
import requests

url = "https://test.payu.in/_payment"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e"
}
data = {
    "key":                  "JF****g",
    "firstname":            "Ashish",
    "email":                "test@example.com",
    "amount":               "10",
    "phone":                " 9876543210",
    "productinfo":          "Product_info",
    "surl":                 "http://pp30admin.payu.in/test_response",
    "furl":                 "http://pp30admin.payu.in/test_response",
    "pg":                   "CC",
    "bankcode":             "CC",
    "lastname":             "Test",
    "ccname":               "Test User",
    "ccvv":                 "123",
    "ccexpmon":             "06",
    "ccexpyr":              "2024",
    "txnid":                "jYhbOYH9o4",
    "hash":                 "e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184",
    "ccnum":                "4012000000002004",
    "txn_s2s_flow":         "4",
    "threeDS2RequestData":  '{"browserInfo":{"userAgent":"Mozilla/5.0","acceptHeader":"*/*","language":"en-US","colorDepth":"24","screenHeight":"600","screenWidth":"800","timeZone":"-300","javaEnabled":true,"ip":"10.248.2.71"}}'
}
response = requests.post(url, headers=headers, data=data)
print("Status Code:", response.status_code)
print("Response:", response.text)
```
```php
<?php
$url = "https://test.payu.in/_payment";
$data = http_build_query([
    "key"                 => "JF****g",
    "firstname"           => "Ashish",
    "email"               => "test@example.com",
    "amount"              => "10",
    "phone"               => " 9876543210",
    "productinfo"         => "Product_info",
    "surl"                => "http://pp30admin.payu.in/test_response",
    "furl"                => "http://pp30admin.payu.in/test_response",
    "pg"                  => "CC",
    "bankcode"            => "CC",
    "lastname"            => "Test",
    "ccname"              => "Test User",
    "ccvv"                => "123",
    "ccexpmon"            => "06",
    "ccexpyr"             => "2024",
    "txnid"               => "jYhbOYH9o4",
    "hash"                => "e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184",
    "ccnum"               => "4012000000002004",
    "txn_s2s_flow"        => "4",
    "threeDS2RequestData" => '{"browserInfo":{"userAgent":"Mozilla/5.0","acceptHeader":"*/*","language":"en-US","colorDepth":"24","screenHeight":"600","screenWidth":"800","timeZone":"-300","javaEnabled":true,"ip":"10.248.2.71"}}'
]);
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/x-www-form-urlencoded",
    "Cookie: PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e"
]);
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```
```java
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.StringJoiner;
public class ThreeDSRequest {
    public static void main(String[] args) throws Exception {
        String url = "https://test.payu.in/_payment";
        Map<String, String> params = new LinkedHashMap<>();
        params.put("key",                 "JF****g");
        params.put("firstname",           "Ashish");
        params.put("email",               "test@example.com");
        params.put("amount",              "10");
        params.put("phone",               " 9876543210");
        params.put("productinfo",         "Product_info");
        params.put("surl",                "http://pp30admin.payu.in/test_response");
        params.put("furl",                "http://pp30admin.payu.in/test_response");
        params.put("pg",                  "CC");
        params.put("bankcode",            "CC");
        params.put("lastname",            "Test");
        params.put("ccname",              "Test User");
        params.put("ccvv",                "123");
        params.put("ccexpmon",            "06");
        params.put("ccexpyr",             "2024");
        params.put("txnid",               "jYhbOYH9o4");
        params.put("hash",                "e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184");
        params.put("ccnum",               "4012000000002004");
        params.put("txn_s2s_flow",        "4");
        params.put("threeDS2RequestData", "{\"browserInfo\":{\"userAgent\":\"Mozilla/5.0\",\"acceptHeader\":\"*/*\",\"language\":\"en-US\",\"colorDepth\":\"24\",\"screenHeight\":\"600\",\"screenWidth\":\"800\",\"timeZone\":\"-300\",\"javaEnabled\":true,\"ip\":\"10.248.2.71\"}}");
        StringJoiner formData = new StringJoiner("&");
        for (Map.Entry<String, String> entry : params.entrySet())
            formData.add(URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8) + "=" + URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8));
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .header("Cookie", "PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e")
                .POST(HttpRequest.BodyPublishers.ofString(formData.toString()))
                .build();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;
class ThreeDSRequest {
    static async Task Main(string[] args) {
        using var client = new HttpClient();
        client.DefaultRequestHeaders.Add("Cookie",
            "PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e");
        var formData = new FormUrlEncodedContent(new[] {
            new KeyValuePair<string, string>("key",                 "JF****g"),
            new KeyValuePair<string, string>("firstname",           "Ashish"),
            new KeyValuePair<string, string>("email",               "test@example.com"),
            new KeyValuePair<string, string>("amount",              "10"),
            new KeyValuePair<string, string>("phone",               " 9876543210"),
            new KeyValuePair<string, string>("productinfo",         "Product_info"),
            new KeyValuePair<string, string>("surl",                "http://pp30admin.payu.in/test_response"),
            new KeyValuePair<string, string>("furl",                "http://pp30admin.payu.in/test_response"),
            new KeyValuePair<string, string>("pg",                  "CC"),
            new KeyValuePair<string, string>("bankcode",            "CC"),
            new KeyValuePair<string, string>("lastname",            "Test"),
            new KeyValuePair<string, string>("ccname",              "Test User"),
            new KeyValuePair<string, string>("ccvv",                "123"),
            new KeyValuePair<string, string>("ccexpmon",            "06"),
            new KeyValuePair<string, string>("ccexpyr",             "2024"),
            new KeyValuePair<string, string>("txnid",               "jYhbOYH9o4"),
            new KeyValuePair<string, string>("hash",                "e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184"),
            new KeyValuePair<string, string>("ccnum",               "4012000000002004"),
            new KeyValuePair<string, string>("txn_s2s_flow",        "4"),
            new KeyValuePair<string, string>("threeDS2RequestData", "{\"browserInfo\":{\"userAgent\":\"Mozilla/5.0\",\"acceptHeader\":\"*/*\",\"language\":\"en-US\",\"colorDepth\":\"24\",\"screenHeight\":\"600\",\"screenWidth\":\"800\",\"timeZone\":\"-300\",\"javaEnabled\":true,\"ip\":\"10.248.2.71\"}}")
        });
        var response = await client.PostAsync("https://test.payu.in/_payment", formData);
        string responseBody = await response.Content.ReadAsStringAsync();
        Console.WriteLine("Status Code: " + (int)response.StatusCode);
        Console.WriteLine("Response: " + responseBody);
    }
}
```

  </Tab>
</Tabs>

<br />
