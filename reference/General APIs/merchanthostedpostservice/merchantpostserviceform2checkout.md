---
api:
  file: merchant-hosted-checkout-postservice.openapi.yaml
  operationId: merchantPostserviceForm2Checkout
hidden: true
---
---
title: Merchant Hosted Checkout — Cards postservice commands
excerpt: >-
  API reference for card-related `postservice?form=2` commands used with Merchant
  Hosted Checkout: getBinInfo, check_isDomestic, and verify_payment.
deprecated: false
hidden: false
metadata:
  title: Merchant Hosted Checkout — Cards postservice commands
  description: >-
    Reference for PayU Merchant Hosted card flows that call
    POST /merchant/postservice?form=2 for BIN lookup, domestic check, and
    payment verification.
  keywords:
    - getBinInfo
    - check_isDomestic
    - verify_payment
    - postservice form=2
    - merchant hosted cards
  robots: index
---

This page documents the following commands with **`postservice`**  commonly used for **Cards** in Merchant Hosted Checkout. For full parameter tables and hashing rules, refer the Request Parameter sub-section below.

* <Accordion title="getBinInfo" icon="fa-info-circle">
  Retrieves issuing bank, card type, category, domestic or international flag, ATM PIN and OTP-on-the-fly support, and optional zero-redirect or SI flags for a **single BIN**, **feature-filtered lists**, or **paginated bulk** BIN data. Use a **9-digit BIN** where possible for accuracy.
</Accordion>

* <Accordion title="check_isDomestic" icon="fa-info-circle">
  Determines whether a **BIN** (first six digits of the card) is **domestic or international**, and returns issuing bank, card type, and credit or debit category.
</Accordion>

* <Accordion title="verify_payment" icon="fa-info-circle">
  Returns the **status and details** of a transaction for a given **merchant transaction ID** (`var1`). Use it to **reconcile** with PayU after you receive the payment response.
</Accordion>


<GENERALAPIsEnvironment />

<Accordion title="Get Bin Info" icon="fa-credit-card">

## Sample request and response

### Sample request
#### For Single Card

  The following values are specified in the var1, var2, and var5 for this scenario:

  * var1 = 1
  * var2 = 512345
  * var5 = 1

  ```bash
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&command=getBinInfo&var1=2&var2=512345&var3=&var4=&var5=1&hash=df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2"
  ```

  #### For Multiple Cards

  ```bash
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&command=getBinInfo&var1=3&var2=&var3=1&var4=5&var5=&hash=df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2"
  ```

  > 📘 **Note**
  >
  > When querying multiple cards, make sure to set the appropriate values for var3 (start index) and var4 (offset).

### Sample response

* Success Scenario

  **For single card:**

  ```php
  Array
  (
      [status] => 1
      [data] => Array
          (
              [bins_data] => Array
                  (
                      [issuing_bank] => HDFC
                      [bin] => 512345
                      [category] => creditcard
                      [card_type] => MAST
                      [is_domestic] => 1
                      [is_atmpin_card] => 1
                      [is_otp_on_the_fly] => 1
                      [is_zero_redirect_supported] => 1
                      [is_si_supported] => 0
                  )
          )
  )
  ```

  > 📘 **Note**
  >
  > Ensure that the value of the **is\_otp\_on\_the\_fly** parameter is 1. Only if the value is 1, you can fetch the card details with the Native OTP support.

  **For multiple cards:**

  ```php
  Array
  (
      [status] => 1
      [data] => Array
          (
              [total_count] => 2580
              [last] => 0
              [bins_data] => Array
                  (
                      [37100] => Array
                          (
                              [issuing_bank] => AMEX
                              [bin] => 37100
                              [category] => UNKNOWN
                              [card_type] => AMEX
                              [is_domestic] => 1
                              [is_atmpin_card] => 1
                              [is_otp_on_the_fly] => 1
                          )
                      [37200] => Array
                          (
                              [issuing_bank] => AMEX
                              [bin] => 37200
                              [category] => UNKNOWN
                              [card_type] => AMEX
                              [is_domestic] => 1
                              [is_atmpin_card] => 1
                              [is_otp_on_the_fly] => 1
                          )
                      [37443] => Array
                          (
                              [issuing_bank] => AMEX
                              [bin] => 37443
                              [category] => UNKNOWN
                              [card_type] => AMEX
                              [is_domestic] => 1
                              [is_atmpin_card] => 1
                              [is_otp_on_the_fly] => 1
                          )
                      [37653] => Array
                          (
                              [issuing_bank] => AMEX
                              [bin] => 37653
                              [category] => UNKNOWN
                              [card_type] => AMEX
                              [is_domestic] => 1
                              [is_atmpin_card] => 1
                              [is_otp_on_the_fly] => 1
                          )
                      [37700] => Array
                          (
                              [issuing_bank] => AMEX
                              [bin] => 37700
                              [category] => UNKNOWN
                              [card_type] => AMEX
                              [is_domestic] => 1
                              [is_atmpin_card] => 1
                              [is_otp_on_the_fly] => 1
                          )
                  )
              [nextStart] => 6
          )
  )
  ```

* Failure Scenarios

  **If BIN is not passed with var2 when requesting for single BIN details (var1=1):**

  ```php
  Array
  (
      [status] => 0
      [data] => Invalid bin passed in var2
  )
  ```

  **If BIN is passed with var2 when multiple card details are request (var1=2):**

  ```php
  Array
  (
      [status] => 0
      [data] => Invalid var2, it should be either 1 or 2 according to feature
  )
  ```

  **If BIN is passed with var2 and multiple card details are requested (var1=3):**

  ```php
  Array
  (
      [status] => 0
      [data] => Invalid var2, it should be empty as var1 is 3
  )
  ```

</Accordion>

<Accordion title="Check if it is a Domestic Card" icon="fa-credit-card">

### Sample request

```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&command=check_isDomestic&var1=462273&hash=df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2"
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
    "command": "check_isDomestic",
    "var1": "462273",
    "hash": "df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2"
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
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        try
        {
            string url = "https://test.payu.in/merchant/postservice?form=2";
            
            client.DefaultRequestHeaders.Add("accept", "application/json");

            var formData = new List<KeyValuePair<string, string>>
            {
                new KeyValuePair<string, string>("key", "JP***g"),
                new KeyValuePair<string, string>("command", "check_isDomestic"),
                new KeyValuePair<string, string>("var1", "462273"),
                new KeyValuePair<string, string>("hash", "df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2")
            };

            var formContent = new FormUrlEncodedContent(formData);
            HttpResponseMessage response = await client.PostAsync(url, formContent);
            string responseBody = await response.Content.ReadAsStringAsync();
            
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {responseBody}");
        }
        catch (HttpRequestException ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
```
```javascript
async function makeRequest() {
    const url = "https://test.payu.in/merchant/postservice?form=2";
    
    const headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    };

    const formData = new URLSearchParams({
        "key": "JP***g",
        "command": "check_isDomestic",
        "var1": "462273",
        "hash": "df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2"
    });

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: headers,
            body: formData
        });
        
        const responseText = await response.text();
        console.log(`Status Code: ${response.status}`);
        console.log(`Response: ${responseText}`);
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

makeRequest();
```
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;

public class ApiRequest {
    public static void main(String[] args) {
        try {
            String url = "https://test.payu.in/merchant/postservice?form=2";
            
            String formData = "key=JP***g&command=check_isDomestic&var1=462273&hash=df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2";
            
            HttpClient client = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(10))
                .build();

            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formData))
                .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            
            System.out.println("Status Code: " + response.statusCode());
            System.out.println("Response: " + response.body());
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
$url = "https://test.payu.in/merchant/postservice?form=2";

$headers = [
    "accept: application/json",
    "Content-Type: application/x-www-form-urlencoded"
];

$postData = [
    "key" => "JP***g",
    "command" => "check_isDomestic",
    "var1" => "462273",
    "hash" => "df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2"
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if (curl_errno($ch)) {
    echo "Error: " . curl_error($ch) . "\n";
} else {
    echo "Status Code: " . $httpCode . "\n";
    echo "Response: " . $response . "\n";
}

curl_close($ch);
?>
```

  **Example Values:**

  * `var1` (first six digit of the card): 512345

### Sample response

## If the card is domestic

  ```json
  {
    "isDomestic": "Y",
    "issuingBank": "SCB",
    "cardType": "VISA",
    "cardCategory": "CC"
  }
  ```

  ## If the card is international

  ```json
  {
    "isDomestic": "N",
    "issuingBank": "UNKNOWN",
    "cardType": "Unknown",
    "cardCategory": "CC"
  }
  ```

</Accordion>

<Accordion title="Verify Payment" icon="fa-credit-card">

### Sample request

```bash
  curl --request POST   --url 'https://test.payu.in/merchant/postservice?form=2'   --header 'Content-Type: application/x-www-form-urlencoded'   --data key=JPM7Fg   --data command=verify_payment   --data var1=IhfgcZnXR4o4nB   --data hash=a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9
  ```
  ```python
  import requests

  try:
      url = "https://test.payu.in/merchant/postservice?form=2"
      headers = {
          'Content-Type': 'application/x-www-form-urlencoded'
      }
      data = {
          'key': 'JPM7Fg',
          'command': 'verify_payment',
          'var1': 'IhfgcZnXR4o4nB',
          'hash': 'a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9'
      }
      
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
  using System.Threading.Tasks;

  class Program
  {
      static async Task Main(string[] args)
      {
          try
          {
              using var client = new HttpClient();
              var url = "https://test.payu.in/merchant/postservice?form=2";
              
              var postData = new List<KeyValuePair<string, string>>
              {
                  new("key", "JPM7Fg"),
                  new("command", "verify_payment"),
                  new("var1", "IhfgcZnXR4o4nB"),
                  new("hash", "a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9")
              };
              
              var content = new FormUrlEncodedContent(postData);
              content.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue("application/x-www-form-urlencoded");
              
              var response = await client.PostAsync(url, content);
              var responseContent = await response.Content.ReadAsStringAsync();
              
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
  async function makeRequest() {
      try {
          const url = 'https://test.payu.in/merchant/postservice?form=2';
          
          const postData = new URLSearchParams({
              'key': 'JPM7Fg',
              'command': 'verify_payment',
              'var1': 'IhfgcZnXR4o4nB',
              'hash': 'a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9'
          });
          
          const response = await fetch(url, {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/x-www-form-urlencoded'
              },
              body: postData
          });
          
          const responseText = await response.text();
          
          console.log(`Status Code: ${response.status}`);
          console.log(`Response: ${responseText}`);
          
      } catch (error) {
          console.error('Error:', error);
      }
  }

  makeRequest();
  ```
  ```java
  import java.io.*;
  import java.net.*;
  import java.nio.charset.StandardCharsets;

  public class PaymentVerification {
      public static void main(String[] args) {
          try {
              URL url = new URL("https://test.payu.in/merchant/postservice?form=2");
              HttpURLConnection connection = (HttpURLConnection) url.openConnection();
              
              connection.setRequestMethod("POST");
              connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
              connection.setDoOutput(true);
              
              String postData = "key=" + URLEncoder.encode("JPM7Fg", StandardCharsets.UTF_8) +
                              "&command=" + URLEncoder.encode("verify_payment", StandardCharsets.UTF_8) +
                              "&var1=" + URLEncoder.encode("IhfgcZnXR4o4nB", StandardCharsets.UTF_8) +
                              "&hash=" + URLEncoder.encode("a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9", StandardCharsets.UTF_8);
              
              try (OutputStream os = connection.getOutputStream()) {
                  byte[] input = postData.getBytes(StandardCharsets.UTF_8);
                  os.write(input, 0, input.length);
              }
              
              int statusCode = connection.getResponseCode();
              System.out.println("Status Code: " + statusCode);
              
              BufferedReader reader;
              if (statusCode >= 200 && statusCode < 300) {
                  reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
              } else {
                  reader = new BufferedReader(new InputStreamReader(connection.getErrorStream()));
              }
              
              StringBuilder response = new StringBuilder();
              String line;
              while ((line = reader.readLine()) != null) {
                  response.append(line);
              }
              reader.close();
              
              System.out.println("Response: " + response.toString());
              
          } catch (Exception e) {
              System.err.println("Error: " + e.getMessage());
          }
      }
  }
  ```
  ```php
  <?php
  $url = 'https://test.payu.in/merchant/postservice?form=2';

  $postData = array(
      'key' => 'JPM7Fg',
      'command' => 'verify_payment',
      'var1' => 'IhfgcZnXR4o4nB',
      'hash' => 'a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9'
  );

  $ch = curl_init();

  curl_setopt_array($ch, array(
      CURLOPT_URL => $url,
      CURLOPT_POST => true,
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_POSTFIELDS => http_build_query($postData),
      CURLOPT_HTTPHEADER => array(
          'Content-Type: application/x-www-form-urlencoded'
      )
  ));

  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

  if (curl_error($ch)) {
      echo 'Error: ' . curl_error($ch) . "\n";
  } else {
      echo "Status Code: " . $httpCode . "\n";
      echo "Response: " . $response . "\n";
  }

  curl_close($ch);
  ?>
  ```

### Sample response

* If credit card payment is made, the response is similar to the following:

  ```plaintext
  {
  "status":0,
  "msg":"0 out of 1 Transactions Fetched Successfully",
  "transaction_details":
  {
    "IhfgcZnXR4o4nB":
    {
      "mihpayid":"Not Found",
      "status":"Not Found"
    }
  }
  }
  ```

  * Offer availed on cart level

  ```
  {
      "status": 1,
      "msg": "1 out of 1 Transactions Fetched Successfully",
      "transaction_details": {
          "1036-f0cf85f2": {
              "mihpayid": "21564143078",
              "request_id": "",
              "bank_ref_num": "431998369241",
              "amt": "2.00",
              "transaction_amount": "2.00",
              "txnid": "1036-f0cf85f2",
              "additional_charges": "0.00",
              "productinfo": "EXPRESS",
              "firstname": "guest",
              "bankcode": "TEZOMNI",
              "udf1": "Magento2",
              "udf2": "",
              "udf3": "",
              "udf4": "",
              "udf5": "qs8rbc1ng2hmqtakk381en6j2p",
              "field2": "114390824407",
              "field9": "SUCCESS|Completed Using Callback",
              "error_code": "E000",
              "addedon": "2024-11-14 16:06:40",
              "payment_source": "express",
              "card_type": null,
              "error_Message": "NO ERROR",
              "net_amount_debit": 2.00,
              "disc": "0.00",
              "mode": "UPI",
              "PG_TYPE": "UPI-PG",
              "card_no": "",
              "status": "success",
              "unmappedstatus": "captured",
              "Merchant_UTR": null,
              "Settled_At": "0000-00-00 00:00:00",
              "App_Name": "GooglePay",
              "card_token": null,
              "field4": null,
              "offerAvailed": null,
              "cart_details": {
                  "id": "2446425",
                  "payu_id": "21564143078",
                  "total_items": "1",
                  "total_cart_amount": "2.00",
                  "offer_applied": null,
                  "offer_availed": null,
                  "offer_auto_apply": "0",
                  "instant_discount": "0.00",
                  "cashback_discount": "0.00",
                  "total_discount": "0.00",
                  "net_cart_amount": "2.00",
                  "created_at": "2024-11-14 16:06:40",
                  "updated_at": "2024-11-14 16:06:40",
                  "sku_details": [
                      {
                          "id": "3468748",
                          "cart_id": "2446425",
                          "payu_id": "21564143078",
                          "mid": "2",
                          "sku_id": "Sample Sofa Design-Red",
                          "sku_name": "Sample Sofa Designtest?=!name",
                          "amount_per_sku": "2.00",
                          "quantity": "1",
                          "amount_before_discount": "2.00",
                          "discount": "0.00",
                          "amount_after_discount": "2.00",
                          "offer_applied": null,
                          "offer_availed": null,
                          "offer_status": null,
                          "offer_type": null,
                          "offer_auto_apply": "0",
                          "is_nce": "0",
                          "failure_reason": null,
                          "created_at": "2024-11-14 16:06:40",
                          "updated_at": "2024-11-14 16:06:40",
                          "offer_title": null,
                          "offer_description": null,
                          "instant_discount": null,
                          "cashback_discount": null,
                          "offers_raw_response": null,
                          "raw_response": null
                      }
                  ]
              }
          }
      }
  }
  ```

  * Offer availed at Transaction level

  ```
  {
      "status": 1,
      "msg": "1 out of 1 Transactions Fetched Successfully",
      "transaction_details": {
          "1725950872187": {
              "mihpayid": "20911942990",
              "request_id": null,
              "bank_ref_num": null,
              "amt": "9900.00",
              "transaction_amount": "10000.00",
              "txnid": "1725950872187",
              "additional_charges": "0.00",
              "productinfo": "Macbook Pro",
              "firstname": "Abc",
              "bankcode": "MAST",
              "udf1": "udf1",
              "udf2": "udf2",
              "udf3": "udf3",
              "udf4": "udf4",
              "udf5": "udf5",
              "field2": null,
              "field9": "You have reached credit card load limit. Please use other payment options to continue.",
              "error_code": "E4936",
              "addedon": "2024-09-10 12:18:20",
              "payment_source": "payu",
              "card_type": "MAST",
              "error_Message": "Bank was unable to authenticate.",
              "net_amount_debit": "0.00",
              "disc": "100.00",
              "mode": "DC",
              "PG_TYPE": "DC-PG",
              "card_no": "XXXXXXXXXXXX9528",
              "status": "failure",
              "unmappedstatus": "failed",
              "Merchant_UTR": null,
              "Settled_At": null,
              "cardhash": "31056eb2112b68cdc90896f1953ca26605bb525249096172c178881bcd45ac93",
              "name_on_card": null,
              "card_token": null,
              "field4": null,
              "offerApplied": "LoadTest1@m3phN7YptAA6",
              "offerAvailed": "LoadTest1@m3phN7YptAA6",
              "transactionOffer": "{"offer_data":[{"offer_key":"LoadTest1@m3phN7YptAA6","discount":100,"offer_type":"INSTANT","isNoCost":false,"flag_to_fail":false,"status":"SUCCESS","failure_code":null,"failure_reason":"Offer Applied Successfully","offer_description":"Load Test 1","offer_title":"Load Test 1","record_type":"OFFER","parent_offer_key":null,"offer_category":null,"isDpEmi":false}],"discount_data":{"total_discount":100,"cashback_discount":0,"instant_discount":100,"total_nce_discount":0,"instant_nce_discount":0,"cashback_nce_discount":0,"gstSubventedViaOffer":false,"downPaymentAmount":0}}",
              "offerType": "instant",
              "offerLevel": "TRANSACTION_LEVEL"
          }
      }
  }
  ```

  #### Failure Responses

  * If txnID is not found, the response is similar to the following:

  ```plaintext
  {
  "status":0,"msg":"0 out of 1 Transactions Fetched

  Successfully","transaction_details":{"IhfgcZnXR4o4nB":{"mihpayid":"Not Found","status":"Not Found"}}
  }
  ```

</Accordion>

<Callout icon="📘" theme="info">
  For request parameters, response fields, and error semantics, refer to the canonical references: [Get BIN Info API](ref:get_bin_info_api), [Check is Domestic API](ref:check_is_domestic_api), and [Verify Payment API](ref:verify_payment_api).
</Callout>
## Request Parameters