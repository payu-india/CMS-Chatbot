---
title: Wallets Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collect Payments with Wallets - Merchant Hosted Checkout
  description: >-
    Discover how to efficiently collect payments from customers using wallets
    through PayU's Merchant Hosted Checkout integration. This guide outlines the
    process of initiating payments and verifying payment status, ensuring a
    smooth transaction experience.
  robots: index
next:
  description: ''
---
---
title: Wallets Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collect Payments with Wallets - Merchant Hosted Checkout
  description: >-
    Merchant-hosted wallet seamless integration: Paytm, PhonePe, Amazon Pay wallets, wallet codes, hash, and wallet payments on your checkout.
  keywords:
    - payu merchant hosted wallet seamless integration web india
    - payment gateway wallet payment integration merchant hosted payu
    - integrate wallet payments website custom checkout payu guide
    - payu wallet seamless api integration steps merchant hosted
    - website wallet payment integration paytm phonepe payu checkout
    - merchant hosted wallet payment gateway integration payu web
    - payu collect payments wallet seamless custom checkout integration
    - server side wallet payment integration payu website checkout
    - payu wallet hash wallet code seamless integration developer
    - payment gateway india wallet integration merchant hosted payu
    - payu custom checkout wallet api integration web guide
    - merchant hosted wallet payment integration payu website india
  robots: index

next:
  description: ''
---
You can collect payments from customers with leading wallets using the Merchant Hosted integration. You need to ensure that **CASH** for the **pg** parameter and wallet code based on the desired wallet for the **bankcode** parameter is posted as mentioned in <Anchor label="Collect Payment API - Merchant Hosted Checkout" target="_blank" href="https://docs.payu.in/reference/_payment_merchant_hosted">Collect Payment API - Merchant Hosted Checkout</Anchor>.

**Steps to Integrate**

<Cards columns={3}>
  <Card title="1. Initiate the Payment to PayU" href="https://docs.payu.in/docs/collect-payments-with-wallets-seamless#step-1-initiate-the-payment-to-payu" target="_blank">
    Initiate the payment to PayU with pg=CASH and bankcode=\<based on wallet provider>

    <br />
  </Card>

  <Card title="2. Check response from PayU" href="https://docs.payu.in/docs/collect-payments-with-wallets-seamless#step-2-check-response-from-payu">
    Check the response from PayU

    <br />
  </Card>

  <Card title="3. Verify the payment" href="https://docs.payu.in/docs/collect-payments-with-wallets-seamless#step-3-verify-the-payment">
    Verify the payment using verify\_payment and monitor using webhooks
  </Card>

  <br />
</Cards>

<RegisterMerchantPrerequiste />

<Callout icon="📮" theme="default">
  **Postman Collection**: Download the **Merchant Hosted Checkout > Wallets API Postman Collection** from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/iu0g7es/wallets-integration](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/iu0g7es/wallets-integration)
</Callout>

## Step 1: Initiate the payment to PayU

<Accordion title="Post Request Syntax & Composition" icon="fa-code">
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
  <input type="hidden" name="pg" value="CASH" />
  <input type="hidden" name="bankcode" value="PAYTM" />
  <input type="hidden" name="surl" value="your own success url" />
  <input type="hidden" name="furl" value="your own failure url" />
  <input type="hidden" name="phone" value="9988776655" />
  <input type="hidden" name="hash" value="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />
  <input type="submit" value="submit"> </form>
  </body>
  </html>
  ```

  > 📘 Note
  >
  > The above HTML code block is for Merchant Checkout integration on the Wallet call for the test environment.
</Accordion>

<Accordion title="Request parameters" icon="fa-table">
  The following parameters vary for the Wallet payment mode in the **Collect Payment** API (**\_payment** API).

  **Environment**

  |                            |                                                                     |
  | :------------------------- | :------------------------------------------------------------------ |
  | **Test Environment**       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
  | **Production Environment** | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

  <Callout icon="📘" theme="info">
    **Reference**: For the **Try It** experience and response, refer to [Collect Payment API - Merchant Hosted Checkout](doc:_payment_merchant_hosted) under API Reference.
  </Callout>

  | Parameter               | Description                                                                                                                                                                                                                                                                                  | Example                                                    |
  | :---------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------- |
  | key `mandatory`         | String - Merchant key provided by PayU during onboarding.                                                                                                                                                                                                                                    | JP\*\*\*g                                                  |
  | txnid `mandatory`       | String - The transaction ID is a reference number for a specific order that is generated by the merchant.                                                                                                                                                                                    | ypl938459435                                               |
  | amount `mandatory`      | String - The payment amount for the transaction.                                                                                                                                                                                                                                             | 10.00                                                      |
  | productinfo `mandatory` | String - A brief description of the product.                                                                                                                                                                                                                                                 | iPhone                                                     |
  | firstname `mandatory`   | String - The first name of the customer.                                                                                                                                                                                                                                                     | Ashish                                                     |
  | email `mandatory`       | String - The email address of the customer.                                                                                                                                                                                                                                                  | [abc@payu.in](mailto:abc@payu.in)                          |
  | phone `mandatory`       | String - The phone number of the customer.                                                                                                                                                                                                                                                   | 9876543210                                                 |
  | pg `mandatory`          | String - It defines the payment category using the Merchant Hosted Checkout integration. Use the following values accordingly: <br/> - Generally for all wallets: `CASH`</br>- For Advantage Club: `RD`                                                                                        | CASH (Only for Advantage Club use RD)  |
  | bankcode `mandatory`    | String - The merchant must post this parameter with the corresponding payment option's bank code value in it. For all the supported wallets, refer to [Wallet Codes](https://docs.payu.in/docs/wallet-codes/) to understand exact value which needs to be passed against bankcode parameter. | PAYTM                                                      |
  | furl `mandatory`        | String - The success URL, which is the page PayU will redirect to if the transaction is successful.                                                                                                                                                                                          | [https://example.com/success](https://example.com/success) |
  | surl `mandatory`        | String - The Failure URL, which is the page PayU will redirect to if the transaction is failed.                                                                                                                                                                                              | [https://example.com/failure](https://example.com/failure) |
  | hash `mandatory`        | String - It is the hash calculated by the merchant. The hash calculation logic is: sha512(key\\\|txnid\\\|amount\\\|productinfo\\\|firstname\\\|email\\\|udf1\\\|udf2\\\|udf3\\\|udf4\\\|udf5\\\|\\\|\\\|\\\|\\\|\\\|SALT)                                                                   | calculated\_hash\_value                                    |

  <Accordion title="Understanding Hashing and sample code" icon="fa-code">
    <HashingRequestParameters />

    #### Hashing Sample Code

    <HashingSample />
  </Accordion>
</Accordion>

<Accordion title="Sample request" icon="fa-table">
### PayTm
  ```curl
  curl -X POST "https://test.payu.in/_payment"  -H "accept: application/json"  -H "Content-Type: application/x-www-form-urlencoded"  -d "key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cash&bankcode=paytm&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
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
      "pg": "cash",
      "bankcode": "paytm",
      "surl": "https://apiplayground-response.herokuapp.com/",
      "furl": "https://apiplayground-response.herokuapp.com/",
      "hash": "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
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
      private static readonly HttpClient client = new HttpClient();

      static async Task Main(string[] args)
      {
          string url = "https://test.payu.in/_payment";
          
          // Set headers
          client.DefaultRequestHeaders.Add("accept", "application/json");
          
          // Prepare form data
          var formData = new List<KeyValuePair<string, string>>
          {
              new KeyValuePair<string, string>("key", "J****g"),
              new KeyValuePair<string, string>("txnid", "aI1UM19ONxLgPz"),
              new KeyValuePair<string, string>("amount", "10.00"),
              new KeyValuePair<string, string>("firstname", "Ashish"),
              new KeyValuePair<string, string>("email", "test@gmail.com"),
              new KeyValuePair<string, string>("phone", "9876543210"),
              new KeyValuePair<string, string>("productinfo", "iPhone"),
              new KeyValuePair<string, string>("pg", "cash"),
              new KeyValuePair<string, string>("bankcode", "paytm"),
              new KeyValuePair<string, string>("surl", "https://apiplayground-response.herokuapp.com/"),
              new KeyValuePair<string, string>("furl", "https://apiplayground-response.herokuapp.com/"),
              new KeyValuePair<string, string>("hash", "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa")
          };

          var formContent = new FormUrlEncodedContent(formData);

          try
          {
              HttpResponseMessage response = await client.PostAsync(url, formContent);
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
  async function makePaymentRequest() {
      const url = "https://test.payu.in/_payment";
      
      const headers = {
          "accept": "application/json",
          "Content-Type": "application/x-www-form-urlencoded"
      };
      
      // Prepare form data
      const formData = new URLSearchParams({
          "key": "J****g",
          "txnid": "aI1UM19ONxLgPz",
          "amount": "10.00",
          "firstname": "Ashish",
          "email": "test@gmail.com",
          "phone": "9876543210",
          "productinfo": "iPhone",
          "pg": "cash",
          "bankcode": "paytm",
          "surl": "https://apiplayground-response.herokuapp.com/",
          "furl": "https://apiplayground-response.herokuapp.com/",
          "hash": "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
      });
      
      try {
          const response = await fetch(url, {
              method: "POST",
              headers: headers,
              body: formData
          });
          
          const responseText = await response.text();
          
          console.log(`Status: ${response.status}`);
          console.log(`Response: ${responseText}`);
          
          return response;
      } catch (error) {
          console.error(`Error: ${error.message}`);
          throw error;
      }
  }

  // Call the function
  makePaymentRequest();
  ```
  ```java
  import java.io.*;
  import java.net.HttpURLConnection;
  import java.net.URL;
  import java.net.URLEncoder;
  import java.nio.charset.StandardCharsets;

  public class PaymentRequest {
      public static void main(String[] args) {
          try {
              String url = "https://test.payu.in/_payment";
              URL obj = new URL(url);
              HttpURLConnection connection = (HttpURLConnection) obj.openConnection();
              
              // Set request method and headers
              connection.setRequestMethod("POST");
              connection.setRequestProperty("accept", "application/json");
              connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
              connection.setDoOutput(true);
              
              // Prepare form data
              String formData = "key=" + URLEncoder.encode("J****g", StandardCharsets.UTF_8) +
                      "&txnid=" + URLEncoder.encode("aI1UM19ONxLgPz", StandardCharsets.UTF_8) +
                      "&amount=" + URLEncoder.encode("10.00", StandardCharsets.UTF_8) +
                      "&firstname=" + URLEncoder.encode("Ashish", StandardCharsets.UTF_8) +
                      "&email=" + URLEncoder.encode("test@gmail.com", StandardCharsets.UTF_8) +
                      "&phone=" + URLEncoder.encode("9876543210", StandardCharsets.UTF_8) +
                      "&productinfo=" + URLEncoder.encode("iPhone", StandardCharsets.UTF_8) +
                      "&pg=" + URLEncoder.encode("cash", StandardCharsets.UTF_8) +
                      "&bankcode=" + URLEncoder.encode("paytm", StandardCharsets.UTF_8) +
                      "&surl=" + URLEncoder.encode("https://apiplayground-response.herokuapp.com/", StandardCharsets.UTF_8) +
                      "&furl=" + URLEncoder.encode("https://apiplayground-response.herokuapp.com/", StandardCharsets.UTF_8) +
                      "&hash=" + URLEncoder.encode("6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa", StandardCharsets.UTF_8);
              
              // Send request
              try (OutputStream os = connection.getOutputStream()) {
                  byte[] input = formData.getBytes(StandardCharsets.UTF_8);
                  os.write(input, 0, input.length);
              }
              
              // Get response
              int responseCode = connection.getResponseCode();
              System.out.println("Response Code: " + responseCode);
              
              try (BufferedReader br = new BufferedReader(new InputStreamReader(
                      responseCode >= 200 && responseCode < 300 ? connection.getInputStream() : connection.getErrorStream(),
                      StandardCharsets.UTF_8))) {
                  StringBuilder response = new StringBuilder();
                  String responseLine;
                  while ((responseLine = br.readLine()) != null) {
                      response.append(responseLine.trim());
                  }
                  System.out.println("Response: " + response.toString());
              }
              
          } catch (Exception e) {
              System.err.println("Error: " + e.getMessage());
              e.printStackTrace();
          }
      }
  }
  ```
  ```php
  $url = "https://test.payu.in/_payment";

  $headers = [
      "accept: application/json",
      "Content-Type: application/x-www-form-urlencoded"
  ];

  $data = [
      "key" => "J****g",
      "txnid" => "aI1UM19ONxLgPz",
      "amount" => "10.00",
      "firstname" => "Ashish",
      "email" => "test@gmail.com",
      "phone" => "9876543210",
      "productinfo" => "iPhone",
      "pg" => "cash",
      "bankcode" => "paytm",
      "surl" => "https://apiplayground-response.herokuapp.com/",
      "furl" => "https://apiplayground-response.herokuapp.com/",
      "hash" => "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
  ];

  $ch = curl_init();

  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
  curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);

  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

  if (curl_errno($ch)) {
      echo 'Error: ' . curl_error($ch);
  } else {
      echo "Status Code: " . $httpCode . "\n";
      echo "Response: " . $response . "\n";
  }

  curl_close($ch);
  ?>
  ```

### Advantage Club
```curl
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=YOUR_MERCHANT_KEY" \
  -d "txnid=ADVCLUB_TXN_001" \
  -d "amount=10.00" \
  -d "productinfo=iPhone" \
  -d "firstname=Ashish" \
  -d "email=test@gmail.com" \
  -d "phone=9876543210" \
  -d "pg=RD" \
  -d "bankcode=ADVCLUB" \
  -d "surl=https://yourwebsite.com/success" \
  -d "furl=https://yourwebsite.com/failure" \
  -d "hash=YOUR_CALCULATED_HASH"
```
```python
import requests

url = "https://test.payu.in/_payment"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "key": "YOUR_MERCHANT_KEY",
    "txnid": "ADVCLUB_TXN_001",
    "amount": "10.00",
    "firstname": "Ashish",
    "email": "test@gmail.com",
    "phone": "9876543210",
    "productinfo": "iPhone",
    "pg": "RD",
    "bankcode": "ADVCLUB",
    "surl": "https://yourwebsite.com/success",
    "furl": "https://yourwebsite.com/failure",
    "hash": "YOUR_CALCULATED_HASH"
}

response = requests.post(url, headers=headers, data=data)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
```
```js 
async function payWithAdvantageClub() {
  const url = "https://test.payu.in/_payment";

  const formData = new URLSearchParams({
    key: "YOUR_MERCHANT_KEY",
    txnid: "ADVCLUB_TXN_001",
    amount: "10.00",
    firstname: "Ashish",
    email: "test@gmail.com",
    phone: "9876543210",
    productinfo: "iPhone",
    pg: "RD",
    bankcode: "ADVCLUB",
    surl: "https://yourwebsite.com/success",
    furl: "https://yourwebsite.com/failure",
    hash: "YOUR_CALCULATED_HASH"
  });

  const response = await fetch(url, {
    method: "POST",
    headers: {
      accept: "application/json",
      "Content-Type": "application/x-www-form-urlencoded"
    },
    body: formData
  });

  const responseText = await response.text();
  console.log(`Status: ${response.status}`);
  console.log(`Response: ${responseText}`);
}

payWithAdvantageClub();
```
```java
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

public class AdvantageClubPayment {
    public static void main(String[] args) throws Exception {
        String url = "https://test.payu.in/_payment";
        URL obj = new URL(url);
        HttpURLConnection conn = (HttpURLConnection) obj.openConnection();

        conn.setRequestMethod("POST");
        conn.setRequestProperty("accept", "application/json");
        conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
        conn.setDoOutput(true);

        String formData =
            "key=" + URLEncoder.encode("YOUR_MERCHANT_KEY", StandardCharsets.UTF_8) +
            "&txnid=" + URLEncoder.encode("ADVCLUB_TXN_001", StandardCharsets.UTF_8) +
            "&amount=" + URLEncoder.encode("10.00", StandardCharsets.UTF_8) +
            "&firstname=" + URLEncoder.encode("Ashish", StandardCharsets.UTF_8) +
            "&email=" + URLEncoder.encode("test@gmail.com", StandardCharsets.UTF_8) +
            "&phone=" + URLEncoder.encode("9876543210", StandardCharsets.UTF_8) +
            "&productinfo=" + URLEncoder.encode("iPhone", StandardCharsets.UTF_8) +
            "&pg=" + URLEncoder.encode("RD", StandardCharsets.UTF_8) +
            "&bankcode=" + URLEncoder.encode("ADVCLUB", StandardCharsets.UTF_8) +
            "&surl=" + URLEncoder.encode("https://yourwebsite.com/success", StandardCharsets.UTF_8) +
            "&furl=" + URLEncoder.encode("https://yourwebsite.com/failure", StandardCharsets.UTF_8) +
            "&hash=" + URLEncoder.encode("YOUR_CALCULATED_HASH", StandardCharsets.UTF_8);

        try (OutputStream os = conn.getOutputStream()) {
            os.write(formData.getBytes(StandardCharsets.UTF_8));
        }

        int code = conn.getResponseCode();
        System.out.println("Response Code: " + code);

        try (BufferedReader br = new BufferedReader(new InputStreamReader(
                code >= 200 && code < 300 ? conn.getInputStream() : conn.getErrorStream(),
                StandardCharsets.UTF_8))) {
            String line;
            StringBuilder response = new StringBuilder();
            while ((line = br.readLine()) != null) {
                response.append(line);
            }
            System.out.println("Response: " + response);
        }
    }
}
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

class AdvantageClubPayment
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main()
    {
        string url = "https://test.payu.in/_payment";

        client.DefaultRequestHeaders.Add("accept", "application/json");

        var formData = new List<KeyValuePair<string, string>>
        {
            new("key", "YOUR_MERCHANT_KEY"),
            new("txnid", "ADVCLUB_TXN_001"),
            new("amount", "10.00"),
            new("firstname", "Ashish"),
            new("email", "test@gmail.com"),
            new("phone", "9876543210"),
            new("productinfo", "iPhone"),
            new("pg", "RD"),
            new("bankcode", "ADVCLUB"),
            new("surl", "https://yourwebsite.com/success"),
            new("furl", "https://yourwebsite.com/failure"),
            new("hash", "YOUR_CALCULATED_HASH")
        };

        var content = new FormUrlEncodedContent(formData);
        HttpResponseMessage response = await client.PostAsync(url, content);
        string body = await response.Content.ReadAsStringAsync();

        Console.WriteLine($"Status Code: {response.StatusCode}");
        Console.WriteLine($"Response: {body}");
    }
}
```
```php
<?php
$url = "https://test.payu.in/_payment";

$headers = [
    "accept: application/json",
    "Content-Type: application/x-www-form-urlencoded"
];

$data = [
    "key" => "YOUR_MERCHANT_KEY",
    "txnid" => "ADVCLUB_TXN_001",
    "amount" => "10.00",
    "firstname" => "Ashish",
    "email" => "test@gmail.com",
    "phone" => "9876543210",
    "productinfo" => "iPhone",
    "pg" => "RD",
    "bankcode" => "ADVCLUB",
    "surl" => "https://yourwebsite.com/success",
    "furl" => "https://yourwebsite.com/failure",
    "hash" => "YOUR_CALCULATED_HASH"
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: $httpCode\n";
echo "Response: $response\n";
?>
```
</Accordion>

## Step 2: Check response from PayU

<ReverseHashing />

<Accordion title="Sample response" icon="fa-table">
  ```
  Array
  (
      [mihpayid] => 403993715527518775
      [mode] => CASH
      [status] => success
      [unmappedstatus] => captured
      [key] => J*****g
      [txnid] => HC13glcAkssIkl
      [amount] => 10.00
      [discount] => 0.00
      [net_amount_debit] => 10
      [addedon] => 2022-10-21 17:45:24
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
      [hash] => 007435a716982c7f5eec5cff95701f65eb1bdbff8f852e461224e3b5e17126ad26bb3a3ffdb95cded6a87d3515fe86fc58925cad024595a4a6825adfed2dc436
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
      [PG_TYPE] => CASH-PG
      [bank_ref_num] => 540898ed-72e7-40a8-a96e-f17de621cbb4
      [bankcode] => CASH
      [error] => E000
      [error_Message] => No Error
      [splitInfo] => {"splitStatus":"splitNotReceived","splitSegments":[]}
  )
  ```
</Accordion>

## Step 3: Verify the payment

<Verify_Payment_Tabs />

## Recommended integrations for Wallets

* **Recurring Payments**: Enable recurring payments or subscriptions for wallets. For more information, refer to [Recurring Payments Integration](doc:introduction-recurring-payments-integration).
* **Offers**: Configure offers for cards on Dashboard and then collect payments with offers. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer) and [Offers](doc:offers-integration).