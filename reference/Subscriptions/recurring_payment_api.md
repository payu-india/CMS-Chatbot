---
title: Recurring Payment Transaction API
api:
  file: test_si_collection-6.json
  operationId: RecurringPaymentAPI
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  title: Recurring Payment Transaction API
  description: >-
    Learn how to set up and make Recurring Payment Transaction using PayU's API.
    This API documentation provides specification for collecting recurring
    payments for Net Banking, Cards, and UPI, enabling seamless and automated
    billing for your customers
  keywords:
    - UPI Recurring Payment
    - ' UPI Mandate'
    - ' Card Recurring Payment'
    - ' Subscription using Card'
    - ' Recurring Payment using Card'
    - ' recurring status description'
    - ' Collect Recurring Payment using Card'
    - ' Collect Recurring Payment using UPI'
  robots: index
next:
  pages:
    - slug: using-api-integration-recurring-payments
      title: Using API Integration
      type: basic
    - slug: customer-experience-and-workflow-recurring-payments
      title: Customer Experience and Workflow
      type: basic
---
All successful registration transactions are charged over the recurring interface with server-to-server API without any additional 2FA or the customers’ involvement. This section describes how to achieve the Recurring Transaction for Net Banking, Cards, and UPI through the common platform.

<Callout icon="📘" theme="info">
  **Notes**:

  * Banks do not support refunds for Net Banking Recurring Payment transactions (or e-NACH transaction) so you will get an error message, “Refund not accepted for txn” or Error 232. For the list of banks supporting e-NACH, refer to Recurring Payments Bank Codes.
  * Check the mandate status, call the **Pre-Debit Notification** API before calling the **Recurring Payment Transaction** API to make a recurring payment transaction.
</Callout>

<Callout icon="🚧" theme="warn">
  **Assumptions**: If the merchant has already performed a successful registration transaction with Net Banking/UPI/Card and mihpayid is received in response to the registration transaction captured successfully and mapped to the customer at the merchant’s end.
</Callout>

### Environment

|                        |                                                                      |
| :--------------------- | :------------------------------------------------------------------- |
| Production Environment | \<[https://info.payu.in/merchant/>](https://info.payu.in/merchant/>) |
| Test Environment       | \<[https://test.payu.in/merchant/>](https://test.payu.in/merchant/>) |

<Accordion title="Sample request" icon="fa-code">
  ```curl
    curl -X POST "https://test.payu.in/merchant/postservice?form=2" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&command=si_transaction&var1={\"authpayuid\": \"6611192557\",\"invoiceDisplayNumber\":\"12345678910\",\"amount\": 3,\"txnid\": \"REC15113506209\",\"phone\": \"9999999999\",\"email\": \"chota.bheem@gmail.com\",\"udf2\": \"\",\"udf3\": \"\",\"udf4\": \"\",\"udf5\": \"\"}&hash=jbUS07Og8BToVZ"
  ```
  ```python
  import requests
  import urllib.parse

  # PayU API endpoint
  url = "https://test.payu.in/merchant/postservice?form=2"

  # Headers
  headers = {
      "accept": "application/json",
      "Content-Type": "application/x-www-form-urlencoded"
  }

  # Form data
  form_data = {
      "key": "JP***g",
      "command": "si_transaction",
      "var1": '{"authpayuid": "6611192557","invoiceDisplayNumber":"12345678910","amount": 3,"txnid": "REC15113506209","phone": "9999999999","email": "chota.bheem@gmail.com","udf2": "","udf3": "","udf4": "","udf5": ""}',
      "hash": "jbUS07Og8BToVZ"
  }

  # Make the POST request
  try:
      response = requests.post(url, headers=headers, data=form_data)
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
          string url = "https://test.payu.in/merchant/postservice?form=2";
          
          // Set headers
          client.DefaultRequestHeaders.Add("accept", "application/json");
          
          // Prepare form data
          var formData = new List<KeyValuePair<string, string>>
          {
              new KeyValuePair<string, string>("key", "JP***g"),
              new KeyValuePair<string, string>("command", "si_transaction"),
              new KeyValuePair<string, string>("var1", "{\"authpayuid\": \"6611192557\",\"invoiceDisplayNumber\":\"12345678910\",\"amount\": 3,\"txnid\": \"REC15113506209\",\"phone\": \"9999999999\",\"email\": \"chota.bheem@gmail.com\",\"udf2\": \"\",\"udf3\": \"\",\"udf4\": \"\",\"udf5\": \"\"}"),
              new KeyValuePair<string, string>("hash", "jbUS07Og8BToVZ")
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
  // PayU API call using modern Async/Await Fetch
  async function makePayURequest() {
      const url = "https://test.payu.in/merchant/postservice?form=2";
      
      // Headers
      const headers = {
          "accept": "application/json",
          "Content-Type": "application/x-www-form-urlencoded"
      };
      
      // Form data
      const formData = new URLSearchParams({
          "key": "JP***g",
          "command": "si_transaction",
          "var1": '{"authpayuid": "6611192557","invoiceDisplayNumber":"12345678910","amount": 3,"txnid": "REC15113506209","phone": "9999999999","email": "chota.bheem@gmail.com","udf2": "","udf3": "","udf4": "","udf5": ""}',
          "hash": "jbUS07Og8BToVZ"
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
          
          return {
              status: response.status,
              data: responseText
          };
          
      } catch (error) {
          console.error("Error:", error);
          throw error;
      }
  }

  // Call the function
  makePayURequest()
      .then(result => console.log("Success:", result))
      .catch(error => console.error("Failed:", error));
  ```
  ```java
  import java.io.IOException;
  import java.net.URI;
  import java.net.URLEncoder;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;
  import java.nio.charset.StandardCharsets;
  import java.time.Duration;
  import java.util.HashMap;
  import java.util.Map;
  import java.util.stream.Collectors;

  public class PayUApiClient {
      
      private static final HttpClient client = HttpClient.newBuilder()
              .connectTimeout(Duration.ofSeconds(30))
              .build();
      
      public static void main(String[] args) {
          try {
              makePayURequest();
          } catch (Exception e) {
              System.err.println("Error: " + e.getMessage());
          }
      }
      
      public static void makePayURequest() throws IOException, InterruptedException {
          String url = "https://test.payu.in/merchant/postservice?form=2";
          
          // Prepare form data
          Map<String, String> formData = new HashMap<>();
          formData.put("key", "JP***g");
          formData.put("command", "si_transaction");
          formData.put("var1", "{\"authpayuid\": \"6611192557\",\"invoiceDisplayNumber\":\"12345678910\",\"amount\": 3,\"txnid\": \"REC15113506209\",\"phone\": \"9999999999\",\"email\": \"chota.bheem@gmail.com\",\"udf2\": \"\",\"udf3\": \"\",\"udf4\": \"\",\"udf5\": \"\"}");
          formData.put("hash", "jbUS07Og8BToVZ");
          
          // Convert to URL encoded string
          String formBody = formData.entrySet().stream()
                  .map(entry -> URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8) + 
                               "=" + URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8))
                  .collect(Collectors.joining("&"));
          
          // Build request
          HttpRequest request = HttpRequest.newBuilder()
                  .uri(URI.create(url))
                  .header("accept", "application/json")
                  .header("Content-Type", "application/x-www-form-urlencoded")
                  .POST(HttpRequest.BodyPublishers.ofString(formBody))
                  .build();
          
          // Send request
          HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
          
          System.out.println("Status Code: " + response.statusCode());
          System.out.println("Response: " + response.body());
      }
  }
  ```
  ```php
  // PayU API endpoint
  $url = "https://test.payu.in/merchant/postservice?form=2";

  // Form data
  $postData = [
      'key' => 'JP***g',
      'command' => 'si_transaction',
      'var1' => '{"authpayuid": "6611192557","invoiceDisplayNumber":"12345678910","amount": 3,"txnid": "REC15113506209","phone": "9999999999","email": "chota.bheem@gmail.com","udf2": "","udf3": "","udf4": "","udf5": ""}',
      'hash' => 'jbUS07Og8BToVZ'
  ];

  // Initialize cURL
  $ch = curl_init();

  // Set cURL options
  curl_setopt_array($ch, [
      CURLOPT_URL => $url,
      CURLOPT_POST => true,
      CURLOPT_POSTFIELDS => http_build_query($postData),
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_HTTPHEADER => [
          'accept: application/json',
          'Content-Type: application/x-www-form-urlencoded'
      ],
      CURLOPT_TIMEOUT => 30,
      CURLOPT_FOLLOWLOCATION => true,
      CURLOPT_SSL_VERIFYPEER => false, // Only for testing
  ]);

  // Execute request
  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  $error = curl_error($ch);

  // Close cURL
  curl_close($ch);

  // Handle response
  if ($error) {
      echo "cURL Error: " . $error . PHP_EOL;
  } else {
      echo "Status Code: " . $httpCode . PHP_EOL;
      echo "Response: " . $response . PHP_EOL;
  }
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  **Success scenario**

  Here is a sample response object returned against recurring payment API when the transaction is successfully charged.

  ```json
  {
    "status": 1,
    "message": "Transaction Processed successfully",
    "details": {
        "REC15113506209": {
            "authpayuid": "25600342065",
            "transactionid": "REC15113506209",
            "amount": "1.00",
            "user_credentials": "",
            "card_token": "",
            "payuid": "",
            "status": "captured",
            "udf1": "",
            "field9": "Transaction Completed Successfully",
            "udf2": "",
            "udf3": "",
            "udf4": "",
            "udf5": "",
            "phone": "9999999999",
            "email": "chota.bheem@gmail.com"
        }
    }
  }
  ```

  **Failure scenarios**

  * Invalid hash

  ```json
  {
      "status": 0,
      "msg": "Invalid Hash."
  }
  ```

  * Basic authentication check failed

  ```json
  {
      "status": 1,
      "message": "Transaction Processed successfully",
      "details": {
          "REC9812123123": {
              "authpayuid": "6611192559",
              "transactionid": "REC9812123123",
              "amount": "1",
              "user_credentials": " ",
              "card_token": " ",
              "payuid": "",
              "status": "failed",
              "field9": "Basic authentication check failed",
              "phone": "",
              "email": ""
          }
      }
  }
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  **JSON fields description of the Details parameter**

  | JSON Field    | Description                                                                                                                                                                       |
  | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | transactionid | This field contains the value of transaction ID parameter which is echoed back in the response. This is unique transaction ID generated by merchant during calling recurring API. |
  | amount        | This field contains the requested transaction amount is echoed back in the payment response.                                                                                      |
  | payuid        | This field contains the PayU’s transaction ID for processed recurring transaction. Merchant can use this field for reference point in the settlement report.                      |
  | status        | This field gives the status of the transaction. Hence, the value of this field depends on whether the transaction was successful or not.                                          |
  | field9        | This field returns the description of transaction status which can help the merchant in providing better customer communication.                                                  |
  | phone         | The mobile number of the customer echoed back.                                                                                                                                    |
  | email         | Email ID of the customer echoed back.                                                                                                                                             |
  | udf1          | Extra information received in the request echoed back.                                                                                                                            |
  | udf2          | Extra information received in the request echoed back.                                                                                                                            |
  | udf3          | Extra information received in the request echoed back.                                                                                                                            |
  | udf4          | Extra information received in the request echoed back.                                                                                                                            |
  | udf5          | Extra information received in the request echoed back.                                                                                                                            |

  ### status field description

  This field gives the status of the transaction. Hence, the value of this field depends on whether the transaction was successful or not.\
  You must map the order status using this parameter only. The possible values of this parameter are:

  * **captured**: If the transaction is successful, the value will be captured. In some cases, the response of Net banking recurring can be captured over real-time basis (ICICI bank in the specific scenario).
  * **pending**: This is common with most Net Banking (except ICICI in the specific scenario) or UPI recurring transaction. In that case, the merchant should consider this as successful initiation of payment with bank / NPCI. The status will be notified back to the merchant over payment processing with individual bank gets completed.\
    For UPI, “pending” transactions get usually get converted into captured or failed within 10 mins from the time of initiation. The Query API can be called post 10 mins from initiation, whereas for Net Banking, it can be called up to T+2 once a day. For more information, refer to [Capture response of Recurring Transaction](#capture-response-of-recurring-transaction-for-net-banking-and-upi).\
    For Net Banking, “pending” transaction gets converted into “captured” or “failed” from the same day till T+2 anytime, depending upon the bank account used by the customer in setting up registration.
  * **failed**: The value of the status as “failed” or blank must be treated as a failed transaction only.
  * **in-progress**: The status of transaction is in progress.

  To capture the final status of “pending” transaction to either “captured” or “failed”, PayU recommends merchants to either implement Webhook URL or call **verify\_payment** API after regular intervals. For more information on:

  * Webhook: Refer to [Webhooks](doc:webhooks)
  * **verify\_payment** API: Refer to [Verify Payment API](ref:verify_payment_api)

  > 📘 Note:
  >
  > For UPI, call the **verify\_settlement** API after 10 mins from time of initiation whereas for Net Banking it can be called up to T+2 once in a day.
</Accordion>

## Request parameters

<Accordion title="Reference information" icon="fa-flask">
  <HTMLBlock>{`
                  <table style="width: 100%; border-collapse: collapse;">
                  <thead>
                  <tr>
                    <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
                    <th style="border: 1px solid #ddd; padding: 8px;">Reference</th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr>
                    <td style="border: 1px solid #ddd; padding: 8px;"><p>&lt;&lt;glossary:key&gt;&gt;</p>
                  </td>
                    <td style="border: 1px solid #ddd; padding: 8px;"><p>For more information on how to generate the Key and Salt, refer to any of the following:  </p>
                  <ul>
                  <li><strong>Production</strong>: <a href="http://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard">Generate Merchant Key and Salt</a></li>
                  <li><strong>Test</strong>: <a href="http://docs.payu.in/docs/generate-test-merchant-key-and-salt">Generate Test Merchant Key and Salt</a></li>
                  </ul>
                  </td>
                  </tr>
                  <tr>
                    <td style="border: 1px solid #ddd; padding: 8px;"><p>&lt;&lt;glossary:hash&gt;&gt;</p>
                  </td>
                    <td style="border: 1px solid #ddd; padding: 8px;"><p>Hash logic for this API is:<br>sha512(key|command|var1|salt)sha512</p>
                  </td>
                  </tr>
                  <tr>
                    <td style="border: 1px solid #ddd; padding: 8px;"><p>var1</p>
                  </td>
                    <td style="border: 1px solid #ddd; padding: 8px;"><p>For JSON fields description, refer to <a href="http://docs.payu.in/reference/addl_info-payment-apis#/">Additional Info. Payment APIs</a></p>
                  </td>
                  </tr>
                  </tbody>
                  </table>
  `}</HTMLBlock>
</Accordion>
