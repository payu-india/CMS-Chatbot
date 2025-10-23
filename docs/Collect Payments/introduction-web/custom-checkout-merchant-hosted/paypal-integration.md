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
Integrate PayU with PayPal wallets to facilitate international payments. PayPal can be seamlessly integrated with your PayU Hosted or Merchant Hosted Checkout integration. Customers have the option to utilize PayPal Currency Conversion to convert international payments from INR (or other currencies) to their chosen currency. This ensures businesses can continue accepting payments via PayPal. Payments made through PayPal are directly transferred to your PayPal wallet, with settlements processed in INR.

You can accept payments within the transaction limits of your PayU account. Discover more about alternative payment methods and their respective transaction limits. This section describes the following:

* [Customer journey](https://docs.payu.in/docs/paypal-integration#customer-journey)
* [Benefits](https://docs.payu.in/docs/paypal-integration#benefits)
* [Steps to Integrate](https://docs.payu.in/docs/paypal-integration#steps-to-integrate)

## Customer journey

1. Customer is redirected to PayU Payment page.
2. Customer selects the **Wallets** option.

<Image align="center" border={true} src="https://files.readme.io/429e564-payu_payment_pagE_wallets_list.png" className="border" />

3. Customer selects the **Paypal** option.

<Image align="center" border={true} src="https://files.readme.io/44bffcc-payu_payment_paypal_page.png" className="border" />

4. Customer selects the preferred currency and clicks **PayPal**.

   The success or failure response is sent back to you by PayU after vaerfication.

## Benefits

Incorporating PayU into your Checkout system offers several benefits:

* Improved Success Rates: Experience success rates up to 20% higher.
* Accelerated Settlement: Receive payments on a T+1 settlement schedule.
* Extensive User Base: Access over 30 Crore PayPal users worldwide.
* No Extra Charges: Transaction rates are determined by PayPal.
* Currency Conversion: Facilitate currency conversions from INR to your customers' preferred currencies.

## Steps to Integrate

<Cards columns={3}>
  <Card title="1. Initiate the Payment to PayU" href="#step-1-initiate-the-payment-to-payu" target="_blank">
    Initiate the payment to PayU with pg=PAYPAL and bankcode=PAYPAL

    <br />
  </Card>

  <Card title="2. Check response from PayU" href="#step-2-check-response-from-payu">
    Check the response from PayU

    <br />
  </Card>

  <Card title="3. Verify the payment" href="#step-3-verify-the-payment">
    Verify the payment using verify\_payment and monitor using webhooks
  </Card>

  <br />
</Cards>

### Step 1: Initiate the payment to PayU

You need use **bankcode** as PAYPAL with the **pg** as PAYPAL.

<Callout icon="📘" theme="info">
  **Reference**: For the **Try It** experience ), refer to <a href="https://docs.payu.in/reference/_payment_merchant_hosted_wallets" target="_blank">Collect Payments API</a> under API Reference.
</Callout>

<Accordion title="Request parameters" icon="fa-code">
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
  | pg <br /> `mandatory`          | string - It defines the payment category using the Merchant Hosted Checkout integration. For a Wallet payment, "**PAYPAL**" must be specified in the **pg** parameter.                                                                                                                                                                                                                                                                                      | PAYPAL                                                                                         |
  | bankcode <br /> `mandatory`    | string - The merchant must post  **PAYPAL** as the value for this parameter.                                                                                                                                                                                                                                                                                                                                                                                | PAYPAL                                                                                         |
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
<br/>
<Accordion title="Understanding Hashing and sample code" icon="fa-code">
  <HashingRequestParameters />

  #### Hashing Sample Code

  <HashingSample />
</Accordion>

</Accordion>

<Accordion title="Sample request" icon="fa-code">
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
                  new KeyValuePair<string, string>("pg", "PAYPAL"),
                  new KeyValuePair<string, string>("bankcode", "PAYPAL"),
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
  async function makePayPalPayment() {
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
          "pg": "PAYPAL",
          "bankcode": "PAYPAL",
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
          formData.put("key", "J****g");
          formData.put("txnid", "aI1UM19ONxLgPz");
          formData.put("amount", "10.00");
          formData.put("firstname", "Ashish");
          formData.put("email", "test@gmail.com");
          formData.put("phone", "9876543210");
          formData.put("productinfo", "iPhone");
          formData.put("pg", "PAYPAL");
          formData.put("bankcode", "PAYPAL");
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
      'pg' => 'PAYPAL',
      'bankcode' => 'PAYPAL',
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

> 📘 Note:
>
> Ensure your PayPal account maintains sufficient funds before initiating a refund. Refunds can be initiated either through the PayU Dashboard or the **Refund Transasction** API. Refunded amounts are deducted from your PayPal account and credited to your customer's PayPal account. For more information, refer to:
>
> * <Anchor label="Refunds Dashboard" target="_blank" href="https://docs.payu.in/docs/refunds-dashboard">Refunds Dashboard</Anchor>.
> * <Anchor label="Refunds Transaction API" target="_blank" href="https://docs.payu.in/reference/refund_transaction_api">Refunds Transaction API</Anchor>.

### Step 2: Check the response from PayU

<Accordion title="Sample response" icon="fa-code">
  You must look for the following:

  * PG\_TYPE:  PAYPAL-PG
  * bankcode: PAYPAL
  * field4: Amount collected in the foreign currency
  * field5: Foreign currency used
  * net\_amount\_debit: Amount debited in INR

  ```
  Array
  (
      [mihpayid] => 403993715527518775
      [mode] => PAYPAL
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
      [country] => US
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
      [field3] => MCP8405944934679133147
      [field4] => 0.12
      [field5] => USD
      [field6] => 
      [field7] => 
      [field8] => 
      [field9] => Transaction Completed Successfully
      [payment_source] => payu
      [PG_TYPE] => PAYPAL-PG
      [bank_ref_num] => 540898ed-72e7-40a8-a96e-f17de621cbb4
      [bankcode] => PAYPAL
      [error] => E000
      [error_Message] => No Error
      [splitInfo] => {"splitStatus":"splitNotReceived","splitSegments":[]}
  )
  ```
</Accordion>

### Step 3: Verify the payment

<Verify_Payment_Tabs />
