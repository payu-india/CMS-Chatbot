---
title: Refund Transaction API
api:
  file: refund_apis.json
  operationId: refundTransaction
hidden: false
link:
  new_tab: false
metadata:
  title: Refund Transaction API
  description: >-
    The Refund Transaction API allows users to cancel or refund transactions in
    different states, with specific parameters required for each action. Sample
    requests and responses are provided for successful and failed scenarios.
  keywords:
    - cancel_refund_transaction command
    - Refund Transaction API
    - Cancel a Refund API
    - API for Refund Transaction
---
The Refund Transaction API (**cancel_refund_transaction**) can be used for the following purposes:

* **Cancel** a transaction that is in '`auth`' state at the moment
* **Refund** a transaction that is in a '`captured`' state at the moment

To learn more about different payment states, refer to [Payment States Explanations](https://docs.payu.in/reference/payment-state-explanations).

In this API:

* **var1** is the Payu ID (mihpayid) of the transaction
* **var2** should contain the Token ID (unique token from the merchant)
* **var3** parameter should contain the amount that needs to be refunded

<Callout icon="📮" theme="default">
  **Postman Collection**: Access the **Refund Transaction API Postman Collection** from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/w4v94j2/refund-transaction-api](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/w4v94j2/refund-transaction-api)
</Callout>

<GENERALAPIsEnvironment />

<Accordion title="Simple Sample Request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&command=cancel_refund_transaction&var1=403993715521937565&var2=20201105secrettokenaturend&hash=10"
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
      "command": "cancel_refund_transaction",
      "var1": "403993715521937565",
      "var2": "20201105secrettokenaturend",
      "hash": "10"
  }

  response = requests.post(url, headers=headers, data=data)
  print(response.json())
  ```
  ```javascript
  fetch("https://test.payu.in/merchant/postservice?form=2", {
      method: "POST",
      headers: {
          "accept": "application/json",
          "Content-Type": "application/x-www-form-urlencoded"
      },
      body: new URLSearchParams({
          "key": "JP***g",
          "command": "cancel_refund_transaction",
          "var1": "403993715521937565",
          "var2": "20201105secrettokenaturend",
          "hash": "10"
      })
  })
  .then(response => response.json())
  .then(data => console.log(data));
  ```
  ```java
  import java.net.URI;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;

  String url = "https://test.payu.in/merchant/postservice?form=2";
  String formData = "key=JP***g&command=cancel_refund_transaction&var1=403993715521937565&var2=20201105secrettokenaturend&hash=10";

  HttpClient client = HttpClient.newHttpClient();
  HttpRequest request = HttpRequest.newBuilder()
      .uri(URI.create(url))
      .header("accept", "application/json")
      .header("Content-Type", "application/x-www-form-urlencoded")
      .POST(HttpRequest.BodyPublishers.ofString(formData))
      .build();

  HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
  System.out.println(response.body());
  ```
  ```php
  <?php
  $url = "https://test.payu.in/merchant/postservice?form=2";
  $data = array(
      "key" => "JP***g",
      "command" => "cancel_refund_transaction",
      "var1" => "403993715521937565",
      "var2" => "20201105secrettokenaturend",
      "hash" => "10"
  );

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      "accept: application/json",
      "Content-Type: application/x-www-form-urlencoded"
  ));

  $response = curl_exec($ch);
  curl_close($ch);

  $result = json_decode($response, true);
  print_r($result);
  ?>
  ```
</Accordion>

<Accordion title="Sample request for split settlements" icon="fa-code">
  ```curl
  curl --location 'https://info.payu.in/merchant/postservice.php?form=2' \
  --header 'Cookie: PHPSESSID=7nv3d144qeh7g102p3uau1o6pm' \
  --form 'key="smsplus"' \
  --form 'command="cancel_refund_transaction"' \
  --form 'var1="24523622342"' \
  --form 'var2="test15"' \
  --form 'var3="0.10"' \
  --form 'hash=""' \
  --form 'var8="{\"amount\": 100,\"aggregatorRefundAmount\": 40 }"
  ```
  ```python
  import requests

  url = "https://info.payu.in/merchant/postservice.php?form=2"

  headers = {
      'Cookie': 'PHPSESSID=7nv3d144qeh7g102p3uau1o6pm'
  }

  data = {
      'key': 'smsplus',
      'command': 'cancel_refund_transaction',
      'var1': '24523622342',
      'var2': 'test15',
      'var3': '0.10',
      'hash': '',
      'var8': '{"amount": 100,"aggregatorRefundAmount": 40 }'
  }

  response = requests.post(url, headers=headers, data=data)
  print(response.text)
  ```

  ```javascript
  const axios = require('axios');
  const FormData = require('form-data');

  const form = new FormData();
  form.append('key', 'smsplus');
  form.append('command', 'cancel_refund_transaction');
  form.append('var1', '24523622342');
  form.append('var2', 'test15');
  form.append('var3', '0.10');
  form.append('hash', '');
  form.append('var8', '{"amount": 100,"aggregatorRefundAmount": 40 }');

  axios.post('https://info.payu.in/merchant/postservice.php?form=2', form, {
    headers: {
      ...form.getHeaders(),
      'Cookie': 'PHPSESSID=7nv3d144qeh7g102p3uau1o6pm'
    }
  })
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
  ```

  ```php
  <?php
  $curl = curl_init();

  curl_setopt_array($curl, array(
    CURLOPT_URL => 'https://info.payu.in/merchant/postservice.php?form=2',
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => array(
      'Cookie: PHPSESSID=7nv3d144qeh7g102p3uau1o6pm'
    ),
    CURLOPT_POSTFIELDS => array(
      'key' => 'smsplus',
      'command' => 'cancel_refund_transaction',
      'var1' => '24523622342',
      'var2' => 'test15',
      'var3' => '0.10',
      'hash' => '',
      'var8' => '{"amount": 100,"aggregatorRefundAmount": 40 }'
    )
  ));

  $response = curl_exec($curl);
  curl_close($curl);
  echo $response;
  ?>
  ```

  ```java
  import java.io.*;
  import java.net.http.*;
  import java.net.*;

  public class PayURequest {
      public static void main(String[] args) throws Exception {
          HttpClient client = HttpClient.newHttpClient();
          
          String boundary = "----Boundary" + System.currentTimeMillis();
          String formData = "--" + boundary + "\r\n" +
              "Content-Disposition: form-data; name=\"key\"\r\n\r\nsmsplus\r\n" +
              "--" + boundary + "\r\n" +
              "Content-Disposition: form-data; name=\"command\"\r\n\r\ncancel_refund_transaction\r\n" +
              "--" + boundary + "\r\n" +
              "Content-Disposition: form-data; name=\"var1\"\r\n\r\n24523622342\r\n" +
              "--" + boundary + "\r\n" +
              "Content-Disposition: form-data; name=\"var2\"\r\n\r\ntest15\r\n" +
              "--" + boundary + "\r\n" +
              "Content-Disposition: form-data; name=\"var3\"\r\n\r\n0.10\r\n" +
              "--" + boundary + "\r\n" +
              "Content-Disposition: form-data; name=\"hash\"\r\n\r\n\r\n" +
              "--" + boundary + "\r\n" +
              "Content-Disposition: form-data; name=\"var8\"\r\n\r\n{\"amount\": 100,\"aggregatorRefundAmount\": 40 }\r\n" +
              "--" + boundary + "--\r\n";
          
          HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create("https://info.payu.in/merchant/postservice.php?form=2"))
              .header("Content-Type", "multipart/form-data; boundary=" + boundary)
              .header("Cookie", "PHPSESSID=7nv3d144qeh7g102p3uau1o6pm")
              .POST(HttpRequest.BodyPublishers.ofString(formData))
              .build();
          
          HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
          System.out.println(response.body());
      }
  }
  ```

  ```ruby
  require 'net/http'
  require 'uri'

  uri = URI.parse("https://info.payu.in/merchant/postservice.php?form=2")
  request = Net::HTTP::Post.new(uri)
  request["Cookie"] = "PHPSESSID=7nv3d144qeh7g102p3uau1o6pm"

  request.set_form({
    "key" => "smsplus",
    "command" => "cancel_refund_transaction",
    "var1" => "24523622342",
    "var2" => "test15",
    "var3" => "0.10",
    "hash" => "",
    "var8" => '{"amount": 100,"aggregatorRefundAmount": 40 }'
  }, 'multipart/form-data')

  response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
    http.request(request)
  end

  puts response.body
  ```

  ```go
  package main

  import (
      "bytes"
      "fmt"
      "io"
      "mime/multipart"
      "net/http"
  )

  func main() {
      url := "https://info.payu.in/merchant/postservice.php?form=2"
      
      body := &bytes.Buffer{}
      writer := multipart.NewWriter(body)
      
      writer.WriteField("key", "smsplus")
      writer.WriteField("command", "cancel_refund_transaction")
      writer.WriteField("var1", "24523622342")
      writer.WriteField("var2", "test15")
      writer.WriteField("var3", "0.10")
      writer.WriteField("hash", "")
      writer.WriteField("var8", `{"amount": 100,"aggregatorRefundAmount": 40 }`)
      writer.Close()
      
      req, _ := http.NewRequest("POST", url, body)
      req.Header.Set("Content-Type", writer.FormDataContentType())
      req.Header.Set("Cookie", "PHPSESSID=7nv3d144qeh7g102p3uau1o6pm")
      
      client := &http.Client{}
      resp, _ := client.Do(req)
      defer resp.Body.Close()
      
      responseBody, _ := io.ReadAll(resp.Body)
      fmt.Println(string(responseBody))
  }
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
          var client = new HttpClient();
          var content = new MultipartFormDataContent();
          
          content.Add(new StringContent("smsplus"), "key");
          content.Add(new StringContent("cancel_refund_transaction"), "command");
          content.Add(new StringContent("24523622342"), "var1");
          content.Add(new StringContent("test15"), "var2");
          content.Add(new StringContent("0.10"), "var3");
          content.Add(new StringContent(""), "hash");
          content.Add(new StringContent("{\"amount\": 100,\"aggregatorRefundAmount\": 40 }"), "var8");
          
          client.DefaultRequestHeaders.Add("Cookie", "PHPSESSID=7nv3d144qeh7g102p3uau1o6pm");
          
          var response = await client.PostAsync("https://info.payu.in/merchant/postservice.php?form=2", content);
          var result = await response.Content.ReadAsStringAsync();
          
          Console.WriteLine(result);
      }
  }
  ```

  Each example replicates the same multipart form-data POST request with the split information JSON in the `var8` field 🚀
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ### Success Scenarios

  **1. On successful processing from PayU:**

  ```json
  Array 
  (
        [status] => 1
        [msg] => Cancel Request Queued 
        [txn_update_id] => <Request ID> 
        [bank_ref_num] => <Bank Reference Number> 
        [mihpayid] => <PayU Transaction ID>
  )
  ```

  **2. On successful processing for captured transactions:**

  ```json
  Array 
  (
       [status] => 1
       [msg] => Refund Request Queued 
       [request_id] => Request ID 
       [bank_ref_num] => <Bank Reference Number> 
       [mihpayid] => <PayU Transaction ID>
  )
  ```

  **3. On successful processing for auth transactions:**

  ```json
  Array 
  (
      [status] => 1
      [msg] => Cancel Request Queued 
      [txn_update_id] => <Request ID> 
      [bank_ref_num] => <Bank Reference Number>
  )
  ```

  ### Failure Scenarios

  **1. If token is missing:**

  ```json
  {
        "status": 0,
        "msg": "token is empty",
        "mihpayid": "403993715521937565"
  }
  ```

  **2. If amount is missing:**

  ```json
  Array 
  (
      [status] => 0
      [msg] => amount is empty 
  )
  ```

  **3. If the transaction is not found:**

  ```json
  Array 
  (
      [status] => 0
      [msg] => transaction not exists 
  )
  ```

  **4. If failed to refund:**

  ```json
  Array 
  (
      [status] => 0
      [msg] => Refund request failed
  )
  ```

  **5. If capture is done on the same day:**

  ```json
  Array 
  (
      [status] => 1
      [msg] => Capture is done today, please check for refund status tomorrow 
      [request_id] => Request ID
      [bank_ref_num] => Bank Reference Number
      [mihpayid] => PayU ID
  )
  ```

  **6. If the token is invalid:**

  ```json
  Array
  (
      [status] => 0
      [msg] => token already used or request pending 
  )
  ```

  **7. If failed to cancel a transaction:**

  ```json
  Array 
  (
      [status] => 0
      [msg] => Cancel request failed
  )
  ```

  > **Important:** The error\_code value 102 should be treated as success; the rest are failures. For the list of error codes, refer to [Error Codes for Refund Initiation](ref:error-codes-for-refund-initiation).
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  | Parameter          | Description                                                                                                                 | Sample Value          |
  | :----------------- | :-------------------------------------------------------------------------------------------------------------------------- | :-------------------- |
  | **status**         | The status can be any of the following:• **1** if API call is a success • **0** if the API has failed                       | 1                     |
  | **msg**            | This parameter contains a response message description                                                                      | Refund Request Queued |
  | **request\_id**    | This parameter contains a unique refund ID generated by PayU                                                                | 6582898821            |
  | **bank\_ref\_num** | This parameter contains a bank reference number returned from bank                                                          | IRN6601148            |
  | **mihpayid**       | This parameter contains a unique transaction ID generated by PayU during sale                                               | 7043873219            |
  | **error\_code**    | This parameter contains the code for response. For a list of error codes and their description, refer to Refund Error Codes | 102                   |

  > 📘 **Note on Error Codes**
  >
  > The error\_code value **102** should be treated as success; the rest are failures. To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).
</Accordion>

## Request Parameters

<Accordion title="Request Parameters Reference" icon="fa-book">
  ### Key Request Parameters

  | Parameter                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
  | :------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | **var2** <br /> `mandatory`           | This parameter must contain the Token ID (unique token from the merchant) for the refund request.• Token ID has to be generated at your end for each new refund request • It is an identifier for each new refund request which can be used for tracking it • It must be unique for every new refund request generated – otherwise the refund request would not be generated successfully • Token ID length should not be greater than 23 characters                                                                                                                          |
  | **var3** <br /> `mandatory`           | **For captured transaction:** This parameter must contain the amount which needs to be refunded. Both partial and full refunds are allowed. • **For a full refund:** The var3 value would be equal to the amount with which the transaction was made • **For a partial refund:** This var3 value would be less than the amount with which the transaction was made **For pre-auth transaction:** If the transaction is in a pre-auth state currently, the full cancellation is allowed. The amount must be the same as the auth amount. A partial amount would not be allowed |
  | **var5** <br /> `mandatory`           | This parameter must contain the refund webhook/callback URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
  | **var8** <br /> `mandatory for split` | Refund split information provided by merchant in a JSON format. This is applicable only with the Split transactions. The JSON format is described in the table below                                                                                                                                                                                                                                                                                                                                                                                                          |

  ### Split Transaction Parameters (var8)

  The **var8** parameter is in JSON format that contains the following fields:

  | Field               | Description                                                                                                                                                                                                                                | Example                                                                  |
  | :------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------- |
  | **Split 1 Details** | The child merchant key, amount and aggregator refund amount is specified in the following format: `child_merchant_key_1": { "amount": 100, "aggregatorRefundAmount": 40 }`**Note:** The aggregator refund amount is optional in this field | `child_merchant_key_1": { "amount": 100, "aggregatorRefundAmount": 40 }` |
  | **Split 2 Details** | The child merchant key, amount and aggregator refund amount is specified similar to Split 1 details                                                                                                                                        | `child_merchant_key_2": {"amount": 20, "aggregatorRefundAmount": 0 }`    |

  #### Sample JSON for var8

  ```json
  {
    "child_merchant_key_1": { 
      "amount": 100, 
      "aggregatorRefundAmount": 40 
    }, 
    "child_merchant_key_2": {
      "amount": 20, 
      "aggregatorRefundAmount": 0 
    }
  }
  ```

  > 📘 **Reference**
  >
  > var5 and var8 are optional parameters and not included in the following **Try It** experience. For more information on description with examples, refer to the [Other request parameters](#key-request-parameters) subsection.
</Accordion>

<Accordion title="Example Values for Testing" icon="fa-flask">
  Use the following sample values while trying out the API:

  * `var1` (mihpayid): **403993715521937565**
  * `var2` (reference number for a refund provided by merchant): **20201105secrettokenaturend**
</Accordion>
