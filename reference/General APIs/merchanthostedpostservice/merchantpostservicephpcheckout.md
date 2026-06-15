---
api:
  file: merchant-hosted-checkout-postservice.openapi.yaml
  operationId: merchantPostservicePhpCheckout
hidden: true
---
This page documents the following commands with `postservice` and `postservice.php` commonly used for **Net Banking** and custom checkout in Merchant Hosted Checkout. For full parameter tables and hashing rules, refer the Request Parameter sub-section below (at the end of this section).

- <Accordion title="getNetbankingStatus" icon="fa-info-circle">
  Checks whether a **specific Net Banking option** (by `ibibo_code` in `var1`) is **up or down**, or returns status for **all** options when `var1` is **`default`**. Use it to handle bank-side downtime in the UI.

</Accordion>

- <Accordion title="get_checkout_details" icon="fa-info-circle">
  Returns **extended checkout information** for custom checkout pages: payment option metadata, **additional charges**, eligibility, and **downtime** details, driven by the JSON payload in `var1`.

</Accordion>

- <Accordion title="verify_payment" icon="fa-info-circle">
  Returns the **status and details** of a transaction for a given **merchant transaction ID** (`var1`). Use it to reconcile PayU records for Net Banking and other modes after the payment response.

</Accordion>

> ⚠️ -

<Cards_PayU_Labs />

<br />

## Postman Collection

Accelerate your integration workflow with our Postman collection for PayU Hosted Checkout. Click the Download Postman Collection button below to download and get started.

<br />

<HTMLBlock>{`
                <style>
                .tooltip-btn {
                    position: relative;
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-weight: bold; /* Added this line */
                }
                .tooltip-btn:hover::after {
                    content: attr(data-tooltip);
                    position: absolute;
                    bottom: 125%;
                    left: 50%;
                    transform: translateX(-50%);
                    background-color: #333;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 4px;
                    white-space: nowrap;
                    font-size: 12px;
                    z-index: 1;
                }
                </style>

                <button onclick="window.open('https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/collection/ioepu0t/merchant-hosted-checkout?sideView=agentMode', '_blank')" 
                        class="tooltip-btn" 
                        data-tooltip="Click to download the Postman collection and explore APIs.">
                    Access Postman Collection
                </button>
`}</HTMLBlock>

<br />

<GENERALAPIsEnvironment />

<Accordion title="Get Net Banking Status" icon="fa-credit-card">

## Sample request and response

### Sample request

  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&command=getNetbankingStatus&var1=AXIB&hash=11f17a5b7b3a93bd0391a0447706ebebd37ab11d8ec8aff18e7d0ca6267f44d6b0b56c4bee6a8b8998acec1491be17047d43ad3ef1b4677bf2504f48d3e779ea"
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
      "command": "getNetbankingStatus",
      "var1": "AXIB",
      "hash": "11f17a5b7b3a93bd0391a0447706ebebd37ab11d8ec8aff18e7d0ca6267f44d6b0b56c4bee6a8b8998acec1491be17047d43ad3ef1b4677bf2504f48d3e779ea"
  }

  try:
      response = requests.post(url, headers=headers, data=data)
      print(f"Status Code: {response.status_code}")
      print(f"Response: {response.text}")
  except requests.exceptions.RequestException as e:
      print(f"Error: {e}")
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
          "command": "getNetbankingStatus",
          "var1": "AXIB",
          "hash": "11f17a5b7b3a93bd0391a0447706ebebd37ab11d8ec8aff18e7d0ca6267f44d6b0b56c4bee6a8b8998acec1491be17047d43ad3ef1b4677bf2504f48d3e779ea"
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
              
              String formData = "key=JP***g&command=getNetbankingStatus&var1=AXIB&hash=11f17a5b7b3a93bd0391a0447706ebebd37ab11d8ec8aff18e7d0ca6267f44d6b0b56c4bee6a8b8998acec1491be17047d43ad3ef1b4677bf2504f48d3e779ea";
              
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
                  new KeyValuePair<string, string>("command", "getNetbankingStatus"),
                  new KeyValuePair<string, string>("var1", "AXIB"),
                  new KeyValuePair<string, string>("hash", "11f17a5b7b3a93bd0391a0447706ebebd37ab11d8ec8aff18e7d0ca6267f44d6b0b56c4bee6a8b8998acec1491be17047d43ad3ef1b4677bf2504f48d3e779ea")
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
  ```php
  <?php
  $url = "https://test.payu.in/merchant/postservice?form=2";

  $headers = [
      "accept: application/json",
      "Content-Type: application/x-www-form-urlencoded"
  ];

  $postData = [
      "key" => "JP***g",
      "command" => "getNetbankingStatus",
      "var1" => "AXIB",
      "hash" => "11f17a5b7b3a93bd0391a0447706ebebd37ab11d8ec8aff18e7d0ca6267f44d6b0b56c4bee6a8b8998acec1491be17047d43ad3ef1b4677bf2504f48d3e779ea"
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

### Sample response

  ```json
  {
        "ibibo_code": "AXIB",
        "title": "AXIS Bank NetBanking",
        "up_status": 0,
        "mode": "NB"
  }
  ```

  To get the status of all Net Banking options pass (value “**default**” is passed in input):

  ```json
  {
        "AXIB": {
              "ibibo_code": "AXIB",
              "title": "AXIS Bank NetBanking",
              "up_status": 0,
              "mode": "NB"
        },
        "SBIB": {
              "ibibo_code": "SBIB",
              "title": "State Bank of India",
              "up_status": 1,
              "mode": "NB"
        },
        "TESTPGNB": {
              "ibibo_code": "TESTPGNB",
              "title": "Test Net Banking",
              "up_status": 1,
              "mode": "NB"
        },
        "UPI": {
              "ibibo_code": "UPI",
              "title": "Test UPI",
              "up_status": 1,
              "mode": "UPI"
        },
        "CASH": {
              "ibibo_code": "CASH",
              "title": "Test Wallet",
              "up_status": 1,
              "mode": "CASH"
        }
  }
  ```

</Accordion>

<Accordion title="Get Checkout Details" icon="fa-credit-card">

## Sample request and response

### Sample request

Use case: **Get extended payment details** (same samples as [Get Checkout Details API](ref:get_checkout_details)).

```curl
  curl --location 'https://info.payu.in/merchant/postservice.php?form=2' \
  --form 'key=0d5aDh' \
  --form 'command=get_checkout_details' \
  --form 'var1={"requestId":"9920371372_38","transactionDetails":{"amount":8000},"useCase":{"getExtendedPaymentDetails":true}}' \
  --form 'hash=5c4784472c10fab50be3730a923474925c477e0fdd9a4957d5b0e0469cca3144cb74670ddc5cbe0e3edcbcd04dae64792a93989e99fd17b1cb4ce561659ce24a'
  ```
  ```python
  import requests

  url = "https://info.payu.in/merchant/postservice.php?form=2"

  files = {
      'key': (None, '0d5aDh'),
      'command': (None, 'get_checkout_details'),
      'var1': (None, '{"requestId":"9920371372_38","transactionDetails":{"amount":8000},"useCase":{"getExtendedPaymentDetails":true}}'),
      'hash': (None, '5c4784472c10fab50be3730a923474925c477e0fdd9a4957d5b0e0469cca3144cb74670ddc5cbe0e3edcbcd04dae64792a93989e99fd17b1cb4ce561659ce24a')
  }

  try:
      response = requests.post(url, files=files)
      print(f"Status Code: {response.status_code}")
      print(f"Response: {response.text}")
  except requests.exceptions.RequestException as e:
      print(f"Error: {e}")
  ```
  ```javascript
  async function makeRequest() {
      const url = "https://info.payu.in/merchant/postservice.php?form=2";
      
      const formData = new FormData();
      formData.append('key', '0d5aDh');
      formData.append('command', 'get_checkout_details');
      formData.append('var1', '{"requestId":"9920371372_38","transactionDetails":{"amount":8000},"useCase":{"getExtendedPaymentDetails":true}}');
      formData.append('hash', '5c4784472c10fab50be3730a923474925c477e0fdd9a4957d5b0e0469cca3144cb74670ddc5cbe0e3edcbcd04dae64792a93989e99fd17b1cb4ce561659ce24a');

      try {
          const response = await fetch(url, {
              method: "POST",
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
  import java.util.HashMap;
  import java.util.Map;

  public class ApiRequest {
      public static void main(String[] args) {
          try {
              String url = "https://info.payu.in/merchant/postservice.php?form=2";
              String boundary = "----boundary" + System.currentTimeMillis();
              
              Map<String, String> formData = new HashMap<>();
              formData.put("key", "0d5aDh");
              formData.put("command", "get_checkout_details");
              formData.put("var1", "{\"requestId\":\"9920371372_38\",\"transactionDetails\":{\"amount\":8000},\"useCase\":{\"getExtendedPaymentDetails\":true}}");
              formData.put("hash", "5c4784472c10fab50be3730a923474925c477e0fdd9a4957d5b0e0469cca3144cb74670ddc5cbe0e3edcbcd04dae64792a93989e99fd17b1cb4ce561659ce24a");
              
              StringBuilder body = new StringBuilder();
              for (Map.Entry<String, String> entry : formData.entrySet()) {
                  body.append("--").append(boundary).append("\r\n");
                  body.append("Content-Disposition: form-data; name=\"").append(entry.getKey()).append("\"\r\n\r\n");
                  body.append(entry.getValue()).append("\r\n");
              }
              body.append("--").append(boundary).append("--\r\n");
              
              HttpClient client = HttpClient.newBuilder()
                  .connectTimeout(Duration.ofSeconds(10))
                  .build();

              HttpRequest request = HttpRequest.newBuilder()
                  .uri(URI.create(url))
                  .header("Content-Type", "multipart/form-data; boundary=" + boundary)
                  .POST(HttpRequest.BodyPublishers.ofString(body.toString()))
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
  ```csharp
  using System;
  using System.Net.Http;
  using System.Threading.Tasks;

  class Program
  {
      private static readonly HttpClient client = new HttpClient();

      static async Task Main(string[] args)
      {
          try
          {
              string url = "https://info.payu.in/merchant/postservice.php?form=2";
              
              var formContent = new MultipartFormDataContent();
              formContent.Add(new StringContent("0d5aDh"), "key");
              formContent.Add(new StringContent("get_checkout_details"), "command");
              formContent.Add(new StringContent("{\"requestId\":\"9920371372_38\",\"transactionDetails\":{\"amount\":8000},\"useCase\":{\"getExtendedPaymentDetails\":true}}"), "var1");
              formContent.Add(new StringContent("5c4784472c10fab50be3730a923474925c477e0fdd9a4957d5b0e0469cca3144cb74670ddc5cbe0e3edcbcd04dae64792a93989e99fd17b1cb4ce561659ce24a"), "hash");

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
  ```php
  <?php
  $url = "https://info.payu.in/merchant/postservice.php?form=2";

  $postData = [
      "key" => "0d5aDh",
      "command" => "get_checkout_details",
      "var1" => '{"requestId":"9920371372_38","transactionDetails":{"amount":8000},"useCase":{"getExtendedPaymentDetails":true}}',
      "hash" => "5c4784472c10fab50be3730a923474925c477e0fdd9a4957d5b0e0469cca3144cb74670ddc5cbe0e3edcbcd04dae64792a93989e99fd17b1cb4ce561659ce24a"
  ];

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, $postData);
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

### Sample response

```json
  {
    "status": 1,
    "details": {
      "paymentOptions": {
        "emi": {
          "all": {
            "dc": {
              "hasEligible": true,
              "all": {
                // Key is the 4 letter IFSC initials of the banks.
                "UTIB": {
                  "title": "Axis Bank",
                  "shortName": "Axis",
                  // Minimum amount for this bank.
                  "minimumAmount": 1000,
                  // Maximum amount for this bank, null means no-limit.
                  "maximumAmount": null,
                  "eligibility": {"status": true},
                  "tenureOptions": {
                    // Key name is the value of bankcode accepted by PayU.
                    "AXISD03": {
                      "tenure": 3,
                      "interestRate": 10.5,
                      "interestCharged": 200.45,
                      "monthlyEmi": 400.5,
                      "minimumAmount": 1000,
                      "maximumAmount": null,
                      "eligibility": {"status": true},
                    },
                    "AXISD...": { "...": "..." }
                  }
                },
                "HDFC": { "...": "..." }
              },
              // Least amount limit of any dc emi.
              "minimumAmount": 1000,
              // Highest amount limit of any dc emi, null means no limit.
              "maximumAmount": null
            },
            "cc": { "...": "..." },
            "others": { "...": "..." },
            "cardless": {
              "hasEligible": true,
              "all": {
                "ZESTMON": {
                  "title": "Zest Money",
                  "shortName": "ZestMoney",
                  "minimumAmount": 1000,
                  "maximumAmount": null,
                  "tenureOptions": {
                    "ZESTMON": {
                      // Tenure field will be all in case tenures of an option
                      // not managed on PayU end.
                      "tenure": null,
                      "minimumAmount": 1000,
                      "maximumAmount": null,
                      "eligibility": {"status": true},
                      // interestRate, interestCharged, monthlyEmi, etc may/may
                      // not be present depending whether these are maintained
                      // at payu's end or not. Eg ZESTMON's tenures are maintained
                      // on the bank end only and are returned once the customer
                      // proceeds with this option and submits the OTP.
                    }
                  }
                },
                "...": { "...": "..." }
              }
            }
          }
        },
        "nb": {
          "all": {
            // Key name is the value of bankcode accepted by PayU.
            "SBIB": {
              "title": "State Bank of India"
            },
            "ADBB": {
              "title": "Andhra Bank"
            },
            "AXIB": {
              "title": "AXIS Bank NetBanking"
            },
            "AXNBTPV": {
              "title": "Axis NB TPV"
            },
            "...": { "...": "..." }
          }
        },
        "si": {
          "all": {
            "ANDBENCR": {
              "title": "Andhra Bank Recurring"
            },
            "AUBLENCR": {
              "title": "AU Small Finance Bank Ltd Recurring"
            },
            "UTIBENCR": {
              "title": "AXIS BANK Recurring"
            },
            "BARBENCR": {
              "title": "BARB ENACH Recurring"
            },
            "...": { "...": "..." }
          }
        },
        "dc": {
          "all": {
            "MAST": {
              "title": "MasterCard Debit Cards"
            },
            "MASTTPV": {
              "title": "MasterCard TPV Debit Cards"
            },
            "SMAE": {
              "title": "State Bank Maestro Cards"
            },
            "MAES": {
              "title": "Other Maestro Cards"
            },
            "RUPAY": {
              "title": "Rupay Debit Card"
            },
            "...": { "...": "..." }
          }
        },
        "cc": {
          "all": {
            "CC": {
              "title": "Credit Card"
            },
            "DINR": {
              "title": "Diners"
            },
            "RUPAYCC": {
              "title": "Rupay Credit Card"
            },
            "...": { "...": "..." }
          }
        },
        "lazypay": {
          "all": {
            "LAZYPAY": {
              "title": "LazyPay"
            }
          }
        },
        "lp-emi": {
          "all": {
            "LP-EMI": {
              "title": "LAZYPAYEMI"
            }
          }
        },
        "cash": {
          "all": {
            "PAYTM": {
              "title": "Paytm"
            },
            "...": { "...": "..." }
          }
        },
        // Similarly all the modes & payment options that are available for
        // the merchant.
        "...": { "...": "..." }
      }
    }
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

> 📘
>
> For request parameters, response fields, and error semantics, refer to the canonical references: [Get Net Banking Status API](ref:get_net_banking_status_api), [Get Checkout Details API](ref:get_checkout_details), and [Verify Payment API](ref:verify_payment_api).

## Request Parameters

<br />
