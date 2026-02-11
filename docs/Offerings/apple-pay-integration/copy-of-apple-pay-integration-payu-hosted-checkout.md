---
title: Apple Pay Integration-PayU Hosted Checkout
deprecated: false
hidden: false
metadata:
  robots: index
---
This section describes step-by-step procedure to integrate Apple Pay as a payment method using PayU Hosted Checkout integration.

<Callout icon="📘" theme="info">
  **Before you begin**:   Ensure that you have completed the prerequisites before you start the integration. For more information, refer to [Prerequisites and Set up for Apple Pay Integration](doc:prerequisites-and-set-up-for-apple-pay-integration).
</Callout>

<Cards columns={3}>
  <Card title="1. Initiate the payment to PayU" href="https://docs.payu.in/docs/apple-pay-integration#step-1-initiate-the-payment-to-payu">
    Post the required parameters to PayU for Apple Pay integration

    <br />
  </Card>

  <Card title="2. Check response from PayU" href="https://docs.payu.in/docs/apple-pay-integration#step-2-check-response-from-payu">
    Check and handle the response received from PayU after posting parameters

    <br />
  </Card>

  <Card title="3. Verify the payment" href="https://docs.payu.in/docs/apple-pay-integration#step-3-verify-the-payment">
    Verify the payment status and ensure transaction completion
  </Card>
</Cards>

***

## Step 1: Initiate the payment to PayU

To initiate an Apple Pay payment, post the payment parameters to PayU's transaction endpoint.

| Environment | URL                               |
| :---------- | :-------------------------------- |
| Test        | `https://test.payu.in/_payment`   |
| Production  | `https://secure.payu.in/_payment` |

<Accordion title="Request parameters" icon="fa-table">
  | Parameter                    | Description                                                                                                                                                                     | Example                                                                                                                       |
  | :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------- |
  | key<br />`mandatory`         | `String` - This parameter contains the merchant key provided by PayU during onboarding.                                                                                         | JP\*\*\*g                                                                                                                     |
  | txnid<br />`mandatory`       | `String` - This parameter contains a unique transaction ID. You can generate this ID or use the PayU API to generate it. The maximum length of this parameter is 25 characters. | txn\_applepay\_001                                                                                                            |
  | amount<br />`mandatory`      | `String` - This parameter contains the payment amount.                                                                                                                          | 100.00                                                                                                                        |
  | productinfo<br />`mandatory` | `String` - This parameter contains a brief description of the product or service.                                                                                               | iPhone Case                                                                                                                   |
  | firstname<br />`mandatory`   | `String` - This parameter contains the first name of the customer.                                                                                                              | John                                                                                                                          |
  | email<br />`mandatory`       | `String` - This parameter contains the email address of the customer.                                                                                                           | [john@example.com](mailto:john@example.com)                                                                                   |
  | phone<br />`mandatory`       | `String` - This parameter contains the phone number of the customer.                                                                                                            | 9876543210                                                                                                                    |
  | surl<br />`mandatory`        | `String` - This parameter contains the Success URL. PayU will redirect the customer to this URL after a successful payment.                                                     | [https://yoursite.com/success](https://yoursite.com/success)                                                                  |
  | furl<br />`mandatory`        | `String` - This parameter contains the Failure URL. PayU will redirect the customer to this URL after a failed payment.                                                         | [https://yoursite.com/failure](https://yoursite.com/failure)                                                                  |
  | hash<br />`mandatory`        | `String` - This parameter contains the hash value calculated using SHA-512 algorithm. Hash logic ensures the integrity of the transaction data.                                 | Refer to [Hashing sample code](https://docs.payu.in/docs/apple-pay-integration-merchant-hosted-checkout#/hashing-sample-code) |
  | udf1<br />`optional`         | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                                                                                               |
  | udf2<br />`optional`         | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                                                                                               |
  | udf3<br />`optional`         | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                                                                                               |
  | udf4<br />`optional`         | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                                                                                               |
  | udf5<br />`optional`         | `String` - This parameter contains any additional information you want to pass. Maximum length is 255 characters.                                                               |                                                                                                                               |

  <br />

  <Accordion title="Understanding Hashing and sample code" icon="fa-code">
    <HashingRequestParameters />

    #### Hashing Sample Code

    <HashingSample />
  </Accordion>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl -X POST \
    'https://test.payu.in/_payment' \
    -H 'Accept: application/json' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'key=JP***g' \
    -d 'txnid=txn_applepay_001' \
    -d 'amount=100.00' \
    -d 'firstname=John' \
    -d 'email=john@example.com' \
    -d 'phone=9876543210' \
    -d 'productinfo=iPhone Case' \
    -d 'pg=APPLEPAY' \
    -d 'bankcode=APPLEPAY' \
    -d 'surl=https://yoursite.com/success' \
    -d 'furl=https://yoursite.com/failure' \
    -d 'hash=<generated_hash>'
  ```
  ```python
  import requests

  url = "https://test.payu.in/_payment"

  headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/x-www-form-urlencoded'
  }

  data = {
      'key': 'JP***g',
      'txnid': 'txn_applepay_001',
      'amount': '100.00',
      'firstname': 'John',
      'email': 'john@example.com',
      'phone': '9876543210',
      'productinfo': 'iPhone Case',
      'pg': 'APPLEPAY',
      'bankcode': 'APPLEPAY',
      'surl': 'https://yoursite.com/success',
      'furl': 'https://yoursite.com/failure',
      'hash': '<generated_hash>'
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
              string url = "https://test.payu.in/_payment";
              
              var formParams = new List<KeyValuePair<string, string>>
              {
                  new KeyValuePair<string, string>("key", "JP***g"),
                  new KeyValuePair<string, string>("txnid", "txn_applepay_001"),
                  new KeyValuePair<string, string>("amount", "100.00"),
                  new KeyValuePair<string, string>("firstname", "John"),
                  new KeyValuePair<string, string>("email", "john@example.com"),
                  new KeyValuePair<string, string>("phone", "9876543210"),
                  new KeyValuePair<string, string>("productinfo", "iPhone Case"),
                  new KeyValuePair<string, string>("pg", "APPLEPAY"),
                  new KeyValuePair<string, string>("bankcode", "APPLEPAY"),
                  new KeyValuePair<string, string>("surl", "https://yoursite.com/success"),
                  new KeyValuePair<string, string>("furl", "https://yoursite.com/failure"),
                  new KeyValuePair<string, string>("hash", "<generated_hash>")
              };

              var formContent = new FormUrlEncodedContent(formParams);
              client.DefaultRequestHeaders.Add("Accept", "application/json");

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
  async function initiateApplePayPayment() {
      const url = 'https://test.payu.in/_payment';
      
      const formData = new URLSearchParams();
      formData.append('key', 'JP***g');
      formData.append('txnid', 'txn_applepay_001');
      formData.append('amount', '100.00');
      formData.append('firstname', 'John');
      formData.append('email', 'john@example.com');
      formData.append('phone', '9876543210');
      formData.append('productinfo', 'iPhone Case');
      formData.append('pg', 'APPLEPAY');
      formData.append('bankcode', 'APPLEPAY');
      formData.append('surl', 'https://yoursite.com/success');
      formData.append('furl', 'https://yoursite.com/failure');
      formData.append('hash', '<generated_hash>');
      
      const requestOptions = {
          method: 'POST',
          headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/x-www-form-urlencoded'
          },
          body: formData
      };
      
      try {
          const response = await fetch(url, requestOptions);
          const responseText = await response.text();
          
          console.log(`Status: ${response.status}`);
          console.log(`Response: ${responseText}`);
          
          return responseText;
      } catch (error) {
          console.error('Error:', error);
          throw error;
      }
  }

  initiateApplePayPayment()
      .then(result => console.log('Payment initiated'))
      .catch(error => console.error('Failed:', error));
  ```
  ```java
  import java.io.BufferedReader;
  import java.io.DataOutputStream;
  import java.io.InputStreamReader;
  import java.net.HttpURLConnection;
  import java.net.URL;
  import java.net.URLEncoder;
  import java.nio.charset.StandardCharsets;
  import java.util.HashMap;
  import java.util.Map;
  import java.util.StringJoiner;

  public class InitiateApplePayPayment {

      public static void main(String[] args) {
          try {
              String url = "https://test.payu.in/_payment";

              Map<String, String> params = new HashMap<>();
              params.put("key", "JP***g");
              params.put("txnid", "txn_applepay_001");
              params.put("amount", "100.00");
              params.put("firstname", "John");
              params.put("email", "john@example.com");
              params.put("phone", "9876543210");
              params.put("productinfo", "iPhone Case");
              params.put("pg", "APPLEPAY");
              params.put("bankcode", "APPLEPAY");
              params.put("surl", "https://yoursite.com/success");
              params.put("furl", "https://yoursite.com/failure");
              params.put("hash", "<generated_hash>");

              StringJoiner sj = new StringJoiner("&");
              for (Map.Entry<String, String> entry : params.entrySet()) {
                  sj.add(URLEncoder.encode(entry.getKey(), "UTF-8") + "="
                       + URLEncoder.encode(entry.getValue(), "UTF-8"));
              }
              byte[] postData = sj.toString().getBytes(StandardCharsets.UTF_8);

              URL apiUrl = new URL(url);
              HttpURLConnection conn = (HttpURLConnection) apiUrl.openConnection();
              conn.setRequestMethod("POST");
              conn.setRequestProperty("Accept", "application/json");
              conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
              conn.setRequestProperty("Content-Length", String.valueOf(postData.length));
              conn.setDoOutput(true);

              try (DataOutputStream dos = new DataOutputStream(conn.getOutputStream())) {
                  dos.write(postData);
              }

              int responseCode = conn.getResponseCode();
              try (BufferedReader br = new BufferedReader(
                      new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
                  StringBuilder response = new StringBuilder();
                  String responseLine;
                  while ((responseLine = br.readLine()) != null) {
                      response.append(responseLine.trim());
                  }

                  System.out.println("Status Code: " + responseCode);
                  System.out.println("Response: " + response.toString());
              }

          } catch (Exception e) {
              e.printStackTrace();
          }
      }
  }
  ```
  ```php
  <?php

  $url = 'https://test.payu.in/_payment';

  $postData = array(
      'key' => 'JP***g',
      'txnid' => 'txn_applepay_001',
      'amount' => '100.00',
      'firstname' => 'John',
      'email' => 'john@example.com',
      'phone' => '9876543210',
      'productinfo' => 'iPhone Case',
      'pg' => 'APPLEPAY',
      'bankcode' => 'APPLEPAY',
      'surl' => 'https://yoursite.com/success',
      'furl' => 'https://yoursite.com/failure',
      'hash' => '<generated_hash>'
  );

  $ch = curl_init();

  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'Accept: application/json',
      'Content-Type: application/x-www-form-urlencoded'
  ));

  $response = curl_exec($ch);

  if (curl_errno($ch)) {
      echo 'cURL Error: ' . curl_error($ch);
  } else {
      $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
      echo "HTTP Status Code: " . $httpCode . "\n";
      echo "Response: " . $response . "\n";
  }

  curl_close($ch);

  $responseData = json_decode($response, true);
  if ($responseData !== null) {
      echo "Parsed Response:\n";
      print_r($responseData);
  }
  ?>
  ```

  <br />
</Accordion>

## Step 2: Check response from PayU

<Accordion title="Hash validation logic for payment response (Reverse Hashing)" icon="fa-shield">
  While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure. This is to make sure the transaction has not been tampered with in the response.

  The order of the parameters is similar to the following:

  ```
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```
</Accordion>

<Accordion title="Sample response (parsed)" icon="fa-file-code">
  ```php
  Array
  (
      [mihpayid] => 403993715524045752
      [mode] => APPLEPAY
      [status] => success
      [unmappedstatus] => captured
      [key] => JP***g
      [txnid] => txn_applepay_001
      [amount] => 100.00
      [discount] => 0.00
      [net_amount_debit] => 100
      [addedon] => 2024-01-15 10:30:00
      [productinfo] => iPhone Case
      [firstname] => John
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => john@example.com
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
      [hash] => 1be7e6e97ab1ea9034b9a107e7cf9718308aa9637b4dbbd1a3343c91b0da02b34a40d00ac7267ebe81c20ea1129b931371c555d565bc6e11f470c3d2cf69b5a3
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
      [PG_TYPE] => APPLEPAY-PG
      [bank_ref_num] => 87d3b2a1-5a60-4169-8692-649f61923b3d
      [bankcode] => APPLEPAY
      [error] => E000
      [error_Message] => No Error
  )
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-table">
  | Parameter                           | Description                                                                                                                                | Example                                     |
  | :---------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------ |
  | mihpayid<br />`mandatory`           | `String` - This parameter contains the unique payment ID generated by PayU for this transaction.                                           | 403993715524045752                          |
  | mode<br />`mandatory`               | `String` - This parameter contains the payment mode used for the transaction. For Apple Pay, this value is `APPLEPAY`.                     | APPLEPAY                                    |
  | status<br />`mandatory`             | `String` - This parameter contains the status of the transaction. Possible values: `success`, `failure`, `pending`.                        | success                                     |
  | unmappedstatus<br />`mandatory`     | `String` - This parameter contains the detailed status of the transaction. Possible values: `captured`, `auth`, `bounced`, `dropped`, etc. | captured                                    |
  | key<br />`mandatory`                | `String` - This parameter contains the merchant key.                                                                                       | JP\*\*\*g                                   |
  | txnid<br />`mandatory`              | `String` - This parameter contains the transaction ID that was sent in the request.                                                        | txn\_applepay\_001                          |
  | amount<br />`mandatory`             | `String` - This parameter contains the transaction amount.                                                                                 | 100.00                                      |
  | discount<br />`optional`            | `String` - This parameter contains the discount amount applied to the transaction.                                                         | 0.00                                        |
  | net\_amount\_debit<br />`mandatory` | `String` - This parameter contains the net amount debited from the customer.                                                               | 100                                         |
  | addedon<br />`mandatory`            | `String` - This parameter contains the date and time when the transaction was added.                                                       | 2024-01-15 10:30:00                         |
  | productinfo<br />`mandatory`        | `String` - This parameter contains the product information sent in the request.                                                            | iPhone Case                                 |
  | firstname<br />`mandatory`          | `String` - This parameter contains the first name of the customer.                                                                         | John                                        |
  | email<br />`mandatory`              | `String` - This parameter contains the email address of the customer.                                                                      | [john@example.com](mailto:john@example.com) |
  | phone<br />`mandatory`              | `String` - This parameter contains the phone number of the customer.                                                                       | 9876543210                                  |
  | hash<br />`mandatory`               | `String` - This parameter contains the hash value returned by PayU. You must validate this hash to ensure the response integrity.          | 1be7e6e97...                                |
  | field9<br />`optional`              | `String` - This parameter contains additional information or error description returned by the bank or payment gateway.                    | Transaction Completed Successfully          |
  | payment\_source<br />`mandatory`    | `String` - This parameter contains the source of the payment.                                                                              | payu                                        |
  | PG\_TYPE<br />`mandatory`           | `String` - This parameter contains the type of payment gateway used. For Apple Pay, this value is `APPLEPAY-PG`.                           | APPLEPAY-PG                                 |
  | bank\_ref\_num<br />`mandatory`     | `String` - This parameter contains the reference number returned by the bank for this transaction.                                         | 87d3b2a1-5a60...                            |
  | bankcode<br />`mandatory`           | `String` - This parameter contains the bank code used for the transaction. For Apple Pay, this value is `APPLEPAY`.                        | APPLEPAY                                    |
  | error<br />`mandatory`              | `String` - This parameter contains the error code. `E000` indicates no error.                                                              | E000                                        |
  | error\_Message<br />`mandatory`     | `String` - This parameter contains the description of the error.                                                                           | No Error                                    |
</Accordion>

***

## Step 3: Verify the payment

<Verify_Payment_Tabs />
