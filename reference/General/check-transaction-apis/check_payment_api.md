---
api:
  file: check_transaction_api.json
  operationId: CheckPaymentAPI
hidden: false
metadata:
  title: Check Payment API
  description: >-
    The Check Payment API is similar to the Verify Payment API but uses PayUID
    or mihpayuID as input instead of TxnID, and it returns all transaction
    parameters.
  keywords:
    - check_payment API Command
    - Check Payment Status API
    - Payment Checking API
    - Check Payment Status using PayU ID
    - PayU ID payment status
---
The Check Payment (**check\_payment**) API functions similar to the [Verify Payment API](ref:verify_payment_api). However, the input parameter in this API is the PayUID or mihpayuID generated at PayU's Server unlike **verify\_payment** API where the input parameter is the TxnID (Transaction ID generated at merchant's server). It returns all the parameters for a given transaction.

<GENERALAPIsEnvironment />

<Accordion title="Sample request" icon="fa-code">
```curl
curl --request POST \
  --url 'https://test.payu.in/merchant/postservice?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data key=JPM7Fg \
  --data command=check_payment \
  --data var1=25779819010 \
  --data hash=9ba8c5c14b1d8643053b121ce7beb556b1e81fe7f4685048008bcc9f81a35f2b03f879704c10e0999e84923701219fc507c53a57c5ea8ff033ccd4148fb3366c
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
          'command': 'check_payment',
          'var1': '25779819010',
          'hash': '9ba8c5c14b1d8643053b121ce7beb556b1e81fe7f4685048008bcc9f81a35f2b03f879704c10e0999e84923701219fc507c53a57c5ea8ff033ccd4148fb3366c'
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
                  new("command", "check_payment"),
                  new("var1", "25779819010"),
                  new("hash", "9ba8c5c14b1d8643053b121ce7beb556b1e81fe7f4685048008bcc9f81a35f2b03f879704c10e0999e84923701219fc507c53a57c5ea8ff033ccd4148fb3366c")
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
              'command': 'check_payment',
              'var1': '25779819010',
              'hash': '9ba8c5c14b1d8643053b121ce7beb556b1e81fe7f4685048008bcc9f81a35f2b03f879704c10e0999e84923701219fc507c53a57c5ea8ff033ccd4148fb3366c'
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

  public class PaymentCheck {
      public static void main(String[] args) {
          try {
              URL url = new URL("https://test.payu.in/merchant/postservice?form=2");
              HttpURLConnection connection = (HttpURLConnection) url.openConnection();
              
              connection.setRequestMethod("POST");
              connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
              connection.setDoOutput(true);
              
              String postData = "key=" + URLEncoder.encode("JPM7Fg", StandardCharsets.UTF_8) +
                              "&command=" + URLEncoder.encode("check_payment", StandardCharsets.UTF_8) +
                              "&var1=" + URLEncoder.encode("25779819010", StandardCharsets.UTF_8) +
                              "&hash=" + URLEncoder.encode("9ba8c5c14b1d8643053b121ce7beb556b1e81fe7f4685048008bcc9f81a35f2b03f879704c10e0999e84923701219fc507c53a57c5ea8ff033ccd4148fb3366c", StandardCharsets.UTF_8);
              
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
      'command' => 'check_payment',
      'var1' => '25779819010',
      'hash' => '9ba8c5c14b1d8643053b121ce7beb556b1e81fe7f4685048008bcc9f81a35f2b03f879704c10e0999e84923701219fc507c53a57c5ea8ff033ccd4148fb3366c'
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
</Accordion>

<Accordion title="Sample response" icon="fa-info-circle">
  * Success response
    ```
    {
      "status": 1,
      "msg": "Transaction Fetched Successfully",
      "transaction_details": {
          "mihpayid": "Not Found",
          "status": "Not Found"
      }
    }
    ```
</Accordion>

## Request parameters

<Accordion title="Reference information for request parameters" icon="fa-book">
  <KeyHashForGeneralParametersDescription />
</Accordion>

**Sample values**

Use the following sample values while trying out the API:

- `var1` (your transaction ID/order ID): 403993715521889530

<br />
