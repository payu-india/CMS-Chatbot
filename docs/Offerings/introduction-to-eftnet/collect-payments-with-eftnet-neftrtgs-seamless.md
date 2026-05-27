---
title: Merchant Hosted Checkout Integration - EFTNET
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collect Payments with EFTNET (NEFT/RTGS) - Merchant Hosted Checkout
  description: >-
    Learn how to efficiently collect payments through EFTNET (NEFT/RTGS)
    transactions using PayU's Merchant Hosted Checkout integration. This guide
    outlines the process of initiating payments and verifying payment status for
    secure and seamless transactions.
  keywords:
    - EFTNET integration
    - EFT integration
    - NEFT integration
    - RTGS integration
    - bank transfer
  robots: index
next:
  description: ''
---
---
title: Merchant Hosted Checkout Integration - EFTNET
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collect Payments with EFTNET (NEFT/RTGS) - Merchant Hosted Checkout
  description: >-
    Learn how to efficiently collect payments through EFTNET (NEFT/RTGS)
    transactions using PayU's Merchant Hosted Checkout integration. This guide
    outlines the process of initiating payments and verifying payment status for
    secure and seamless transactions.
  keywords:
    - EFTNET integration
    - EFT integration
    - NEFT integration
    - RTGS integration
    - bank transfer
    - EFTNET integration seamless
    - EFT integration seamless
    - NEFT integration seamless
    - RTGS integration seamless
    - bank transfer seamless 
    - EFTNET integration merchant hosted
    - EFT integration merchant hosted
    - NEFT integration merchant hosted
    - RTGS integration merchant hosted
    - bank transfer merchant hosted
  robots: index
next:
  description: ''
---
Collect payments using EFTNET (NEFT/RTGS) with Merchant Hosted Checkout integration as described in this section. After collecting the details from the customer, make the transaction request with the payment details to PayU.

To integrate with EFTNET:

**Steps to Integrate**

<Cards columns={3}>
  <Card title="1. Initiate the Payment to PayU" href="#step-1-initiate-the-payment-to-payu">
    Initiate the payment to PayU with pg= NEFTRTGS and bankcode= \<based on the bank>
  </Card>

  <Card title="2. Check response from PayU" href="#step-2-check-response-from-payu">
    Check the response from PayU
  </Card>

  <Card title="3. Verify the payment" href="#step-3-verify-the-payment">
    Verify the payment using verify\_payment and monitor using webhooks
  </Card>
</Cards>

<RegisterMerchantPrerequiste />

## Step 1: Initiate the payment to PayU

<Accordion title="Post request syntax & composition" icon="fa-code">
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
  <input type="hidden" name="pg" value="NEFTRTGS" />
  <input type="hidden" name="bankcode" value="EFTAXIS" />
  <input type="hidden" name="surl" value="your own success url" />
  <input type="hidden" name="furl" value="your own failure url" />
  <input type="hidden" name="phone" value="9988776655" />
  <input type="hidden" name="hash" value="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />
  <input type="submit" value="submit"> </form>
  </body>

  </html>
  ```

  <Callout icon="📘" theme="info">
    **Note**: The sample HTML code mentioned above is for Merchant Checkout integration with the NEFT/RTGS payment method call for the test environment.
  </Callout>
</Accordion>

<Accordion title="Optional configuration for challan" icon="fa-code">
  PayU provides an optional **Back to Merchant** button on the payment challan of a NEFT/RTGS payment. This button enables your customer to go back to the merchant portal once the transaction is done.

  In this scenario, if a customer clicks on **Back to Merchant** button the merchant will receive the response on the furl shared in the <Anchor label="Collect Payment API - Merchant Hosted Checkout" target="_blank" href="https://docs.payu.in/reference/_payment_merchant_hosted">Collect Payment API - Merchant Hosted Checkout</Anchor>.

  *Sample challan of a NEFT/RTGS transaction*

  <img
    src="https://files.readme.io/4f959a8-neftrtgs_challan.jpeg"
    alt=""
    style={{
    display: "block",
    margin: "0 auto",
    width: "400px"
  }}
  />
</Accordion>

<Accordion title="Request parameters" icon="fa-table">
  The following parameters vary for the EFTNEFT payment mode in the **Collect Payment**API (**\_payment** API).

  **Environment**

  |                            |                                                                     |
  | :------------------------- | :------------------------------------------------------------------ |
  | **Test Environment**       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
  | **Production Environment** | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

  | Parameter                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Example                                                                                        |
  | :----------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------- |
  | key <br /> `mandatory`         | String - This parameter is the unique merchant key provided by PayU for your merchant account. For more information, refer to Generate Merchant Key and Salt.                                                                                                                                                                                                                                                                                               | 8488225                                                                                        |
  | txnid <br /> `mandatory`       | varchar - This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant's) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction. | fd3e847h2                                                                                      |
  | amount <br /> `mandatory`      | float - This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type                                                                                                                                                                                                                                                                                                                            | 10                                                                                             |
  | productinfo <br /> `mandatory` | varchar - This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice).                                                                                                                                                                                                                                                                                           | T-shirt                                                                                        |
  | firstname <br /> `mandatory`   | varchar - This parameter must contain the first name of the customer.                                                                                                                                                                                                                                                                                                                                                                                       | Ankit                                                                                          |
  | email <br /> `mandatory`       | varchar - This parameter must contain the email of the customer                                                                                                                                                                                                                                                                                                                                                                                             | [test@gmail.com](mailto:test@gmail.com)                                                        |
  | phone `mandatory`              | integer - Merchant needs to take the customer's GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request.                                                                                                                                                                                                                                                           | 9876543210                                                                                     |
  | pg <br /> `mandatory`          | string - The payment gateway is specified in this parameter. For EFTNET, specify NEFTRTGS.                                                                                                                                                                                                                                                                                                                                                                  | NEFTRTGS                                                                                       |
  | bankcode <br /> `mandatory`    | string - Each payment option is identified with a unique bank code at PayU.                                                                                                                                                                                                                                                                                                                                                                                 | EFTAXIS                                                                                        |
  | surl <br /> `mandatory`        | The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                     | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/) |
  | furl <br /> `mandatory`        | The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                         | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/) |
  | hash <br /> `mandatory`        | string - The hash calculated by the merchant using the key and salt provided by PayU. The format for calculating the hash: sha512(key\\\|txnid\\\|amount\\\|productinfo\\\|firstname\\\|email\\\|udf1\\\|udf2\\\|udf3\\\|udf4\\\|udf5\\\|\\\|\\\|\\\|\\\|SALT) For more information, refer to Generate Hash.                                                                                                                                                | calculated\_hash\_value                                                                        |
  | lastname <br /> `optional`     | string - The last name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                     | Kumar                                                                                          |
  | address1 <br /> `optional`     | string - The first line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                             | 123 Main St                                                                                    |
  | address2 <br /> `optional`     | string - The second line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                            | Apt 4B                                                                                         |
  | city <br /> `optional`         | string - The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                               | Mumbai                                                                                         |
  | state <br /> `optional`        | string - The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                              | Maharashtra                                                                                    |
  | country <br /> `optional`      | string - The country where your customer resides.                                                                                                                                                                                                                                                                                                                                                                                                           | India                                                                                          |
  | zipcode <br /> `optional`      | string - Billing address zip code is mandatory for the cardless EMI option.                                                                                                                                                                                                                                                                                                                                                                                 | 400001                                                                                         |
  | udf1 <br /> `optional`         | string - This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                     | custom\_data\_1                                                                                |
  | udf2 <br /> `optional`         | string - This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                     | custom\_data\_2                                                                                |
  | udf3 <br /> `optional`         | string - This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                     | custom\_data\_3                                                                                |
  | udf4 <br /> `optional`         | string - This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                     | custom\_data\_4                                                                                |
  | udf5 <br /> `optional`         | string - This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                     | custom\_data\_5                                                                                |

  <Accordion title="Understanding Hashing and sample code" icon="fa-code">
    <HashingRequestParameters />

    #### Hashing Sample Code

    <HashingSample />
  </Accordion>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment"  -H "accept: application/json"  -H "Content-Type: application/x-www-form-urlencoded"  -d "key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=NEFTRTGS&bankcode=EFTAXIS&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
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
      "pg": "NEFTRTGS",
      "bankcode": "EFTAXIS",
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
              var url = "https://test.payu.in/_payment";
              
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
                  new KeyValuePair<string, string>("pg", "NEFTRTGS"),
                  new KeyValuePair<string, string>("bankcode", "EFTAXIS"),
                  new KeyValuePair<string, string>("surl", "https://apiplayground-response.herokuapp.com/"),
                  new KeyValuePair<string, string>("furl", "https://apiplayground-response.herokuapp.com/"),
                  new KeyValuePair<string, string>("hash", "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa")
              };
              
              var formContent = new FormUrlEncodedContent(formData);
              
              var response = await client.PostAsync(url, formContent);
              var responseBody = await response.Content.ReadAsStringAsync();
              
              Console.WriteLine($"Status: {response.StatusCode}");
              Console.WriteLine($"Response: {responseBody}");
          }
      }
  }
  ```
  ```javascript
  async function makeBankTransferPayment() {
      const url = "https://test.payu.in/_payment";
      
      const headers = {
          "accept": "application/json",
          "Content-Type": "application/x-www-form-urlencoded"
      };
      
      const formData = new URLSearchParams({
          "key": "J****g",
          "txnid": "aI1UM19ONxLgPz",
          "amount": "10.00",
          "firstname": "Ashish",
          "email": "test@gmail.com",
          "phone": "9876543210",
          "productinfo": "iPhone",
          "pg": "NEFTRTGS",
          "bankcode": "EFTAXIS",
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
          
          const data = await response.text();
          console.log("Status:", response.status);
          console.log("Response:", data);
          
          return data;
      } catch (error) {
          console.error("Error:", error);
          throw error;
      }
  }

  // Call the function
  makeBankTransferPayment();
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

  public class BankTransferPayment {
      public static void main(String[] args) throws IOException, InterruptedException {
          String url = "https://test.payu.in/_payment";
          
          Map<String, String> formData = new HashMap<>();
          formData.put("key", "J****g");
          formData.put("txnid", "aI1UM19ONxLgPz");
          formData.put("amount", "10.00");
          formData.put("firstname", "Ashish");
          formData.put("email", "test@gmail.com");
          formData.put("phone", "9876543210");
          formData.put("productinfo", "iPhone");
          formData.put("pg", "NEFTRTGS");
          formData.put("bankcode", "EFTAXIS");
          formData.put("surl", "https://apiplayground-response.herokuapp.com/");
          formData.put("furl", "https://apiplayground-response.herokuapp.com/");
          formData.put("hash", "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa");
          
          String formBody = formData.entrySet()
              .stream()
              .map(entry -> entry.getKey() + "=" + entry.getValue())
              .collect(Collectors.joining("&"));
          
          HttpClient client = HttpClient.newHttpClient();
          
          HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create(url))
              .header("accept", "application/json")
              .header("Content-Type", "application/x-www-form-urlencoded")
              .POST(HttpRequest.BodyPublishers.ofString(formBody))
              .build();
          
          HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
          
          System.out.println("Status Code: " + response.statusCode());
          System.out.println("Response Body: " + response.body());
      }
  }
  ```
  ```php

  $url = "https://test.payu.in/_payment";

  $data = array(
      'key' => 'J****g',
      'txnid' => 'aI1UM19ONxLgPz',
      'amount' => '10.00',
      'firstname' => 'Ashish',
      'email' => 'test@gmail.com',
      'phone' => '9876543210',
      'productinfo' => 'iPhone',
      'pg' => 'NEFTRTGS',
      'bankcode' => 'EFTAXIS',
      'surl' => 'https://apiplayground-response.herokuapp.com/',
      'furl' => 'https://apiplayground-response.herokuapp.com/',
      'hash' => '6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa'
  );

  $options = array(
      'http' => array(
          'header' => "accept: application/json\r\n" .
                     "Content-Type: application/x-www-form-urlencoded\r\n",
          'method' => 'POST',
          'content' => http_build_query($data)
      )
  );

  $context = stream_context_create($options);
  $response = file_get_contents($url, false, $context);

  if ($response === FALSE) {
      echo "Error occurred";
  } else {
      echo "Response: " . $response;
  }

  // Alternative using cURL
  /*
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

  echo "HTTP Code: " . $httpCode . "\n";
  echo "Response: " . $response;
  */

  ```
</Accordion>

## Step 2: Check response from PayU

<ReverseHashing />

> 📘
>
> **Note on Response**: For security reasons, the sample response or URL is not included here.

## Step 3: Verify the payment

<Verify_Payment_Tabs />

<br />
