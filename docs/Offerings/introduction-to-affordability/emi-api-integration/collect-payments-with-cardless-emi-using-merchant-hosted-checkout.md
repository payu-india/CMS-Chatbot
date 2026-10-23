---
title: Cardless EMI - Merchant Hosted Checkout Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Integrate with Cardless EMI - Merchant Hosted Checkout
  description: ''
  robots: index
next:
  description: ''
---
---
title: Cardless EMI - Merchant Hosted Checkout Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Integrate with Cardless EMI - Merchant Hosted Checkout
  description: ''
  robots: index
next:
  description: ''
---
When your customer wants to opt for the Cardless EMI option, you can use the EMI APIs to check the customer’s eligibility and get the EMI amount, interest, processing fee, or No-Cost EMI and tenure. If the customer is eligible, you can post the Cardless EMI transaction.

<Callout icon="📘" theme="info">
  **Handle Guest Checkout Transaction**: You can handle Guest Checkout transactions for EMI integration. For more information, refer to [Cards Integration > Handling Guest Checkout Transactions](doc:collect-payments-with-cards-seamless#handling-guest-checkout-transactions).
</Callout>

**Steps to integrate**

<Cards columns={2}>
  <Card title="1. Check the Cardless EMI Eligibility" href="#step-1-check-the-cardless-emi-eligibility">
    Check whether the customer is eligible for cardless EMI. For New to Bank (NTB) customers, also check main eligibility with the customer's details.

    <br />
  </Card>

  <Card title="2. Initiate the Payment" href="#step-2-initiate-the-payment">
    Post the Cardless EMI payment request to PayU using the Collect Payment API

    <br />
  </Card>

  <Card title="3. Check the Response from PayU" href="#step-3-check-the-response-from-payu">
    Handle and process the response received from PayU after payment initiation
  </Card>

  <Card title="4. Verify Payment" href="#step-4-verify-payment">
    Confirm the payment status and ensure successful transaction completion

    <br />
  </Card>
</Cards>

## Step 1: Check the cardless EMI eligibility

### Step 1a: Check customer eligibility

After collecting the customer’s mobile number and the amount to be paid, check the Cardless EMI eligibility based on the customer’s mobile using the **Get Checkout Details API** (get_checkout_details) API. For more information, refer to [Get Checkout Details API](ref:get_checkout_details#check-customer-eligibility)

To find out whether the customer is New to Bank (NTB) for a cardless EMI lender, set `useCase.checkNTBCustomerEligibility` to `true` in the `var1` JSON along with `useCase.checkCustomerEligibility`.

<Callout icon="📘" theme="info">
  The NTB journey must be enabled for your PayU account. Contact your PayU Key Account Manager (KAM) to enable it.
</Callout>

| Environment | URL                                                |
| :---------- | :------------------------------------------------- |
| Production  | `https://info.payu.in/merchant/postservice?form=2` |
| Test        | `https://test.payu.in/merchant/postservice?form=2` |

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location 'https://test.payu.in/merchant/postservice?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'command=get_checkout_details' \
  --data-urlencode 'var1={"requestId":"9078698a15d746feadcffbdaf979a198","transactionDetails":{"amount":10000},"customerDetails":{"mobile":"9876543210"},"filters":{"paymentOptions":{"emi":{"cardless":"all"}}},"useCase":{"checkCustomerEligibility":true,"checkNTBCustomerEligibility":true}}' \
  --data-urlencode 'hash={{hash}}'
  ```
  ```python
  import requests

  url = "https://test.payu.in/merchant/postservice?form=2"

  headers = {
      "Content-Type": "application/x-www-form-urlencoded"
  }

  data = {
      "key": "JP***g",
      "command": "get_checkout_details",
      "var1": '{"requestId":"9078698a15d746feadcffbdaf979a198","transactionDetails":{"amount":10000},"customerDetails":{"mobile":"9876543210"},"filters":{"paymentOptions":{"emi":{"cardless":"all"}}},"useCase":{"checkCustomerEligibility":true,"checkNTBCustomerEligibility":true}}',
      "hash": "{{hash}}"  # sha512(key|command|var1|SALT)
  }

  try:
      response = requests.post(url, headers=headers, data=data)
      print("Status Code:", response.status_code)
      print("Response:", response.text)
  except requests.exceptions.RequestException as e:
      print("Error:", e)
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
          var client = new HttpClient();

          var formData = new List<KeyValuePair<string, string>>
          {
              new KeyValuePair<string, string>("key", "JP***g"),
              new KeyValuePair<string, string>("command", "get_checkout_details"),
              new KeyValuePair<string, string>("var1", "{\"requestId\":\"9078698a15d746feadcffbdaf979a198\",\"transactionDetails\":{\"amount\":10000},\"customerDetails\":{\"mobile\":\"9876543210\"},\"filters\":{\"paymentOptions\":{\"emi\":{\"cardless\":\"all\"}}},\"useCase\":{\"checkCustomerEligibility\":true,\"checkNTBCustomerEligibility\":true}}"),
              new KeyValuePair<string, string>("hash", "{{hash}}") // sha512(key|command|var1|SALT)
          };

          var content = new FormUrlEncodedContent(formData);

          try
          {
              var response = await client.PostAsync("https://test.payu.in/merchant/postservice?form=2", content);
              string responseBody = await response.Content.ReadAsStringAsync();
              Console.WriteLine("Status Code: " + response.StatusCode);
              Console.WriteLine("Response: " + responseBody);
          }
          catch (HttpRequestException e)
          {
              Console.WriteLine("Error: " + e.Message);
          }
      }
  }
  ```
  ```javascript
  async function getCheckoutDetails() {
      const url = "https://test.payu.in/merchant/postservice?form=2";

      const formData = new URLSearchParams();
      formData.append("key", "JP***g");
      formData.append("command", "get_checkout_details");
      formData.append("var1", JSON.stringify({
          requestId: "9078698a15d746feadcffbdaf979a198",
          transactionDetails: { amount: 10000 },
          customerDetails: { mobile: "9876543210" },
          filters: { paymentOptions: { emi: { cardless: "all" } } },
          useCase: {
              checkCustomerEligibility: true,
              checkNTBCustomerEligibility: true
          }
      }));
      formData.append("hash", "{{hash}}"); // sha512(key|command|var1|SALT)

      try {
          const response = await fetch(url, {
              method: "POST",
              headers: { "Content-Type": "application/x-www-form-urlencoded" },
              body: formData.toString()
          });

          const data = await response.text();
          console.log("Status Code:", response.status);
          console.log("Response:", data);
      } catch (error) {
          console.error("Error:", error);
      }
  }

  getCheckoutDetails();
  ```
  ```java
  import java.io.*;
  import java.net.*;
  import java.nio.charset.StandardCharsets;

  public class GetCheckoutDetails {
      public static void main(String[] args) {
          try {
              URL url = new URL("https://test.payu.in/merchant/postservice?form=2");
              HttpURLConnection conn = (HttpURLConnection) url.openConnection();
              conn.setRequestMethod("POST");
              conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
              conn.setDoOutput(true);

              String var1 = "{\"requestId\":\"9078698a15d746feadcffbdaf979a198\","
                  + "\"transactionDetails\":{\"amount\":10000},"
                  + "\"customerDetails\":{\"mobile\":\"9876543210\"},"
                  + "\"filters\":{\"paymentOptions\":{\"emi\":{\"cardless\":\"all\"}}},"
                  + "\"useCase\":{\"checkCustomerEligibility\":true,\"checkNTBCustomerEligibility\":true}}";

              String formData = "key=" + URLEncoder.encode("JP***g", "UTF-8")
                  + "&command=" + URLEncoder.encode("get_checkout_details", "UTF-8")
                  + "&var1=" + URLEncoder.encode(var1, "UTF-8")
                  + "&hash=" + URLEncoder.encode("{{hash}}", "UTF-8"); // sha512(key|command|var1|SALT)

              try (OutputStream os = conn.getOutputStream()) {
                  os.write(formData.getBytes(StandardCharsets.UTF_8));
              }

              System.out.println("Status Code: " + conn.getResponseCode());

              BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8));
              StringBuilder response = new StringBuilder();
              String line;
              while ((line = reader.readLine()) != null) {
                  response.append(line);
              }
              reader.close();

              System.out.println("Response: " + response);
          } catch (Exception e) {
              System.out.println("Error: " + e.getMessage());
          }
      }
  }
  ```
  ```php
  <?php

  $url = "https://test.payu.in/merchant/postservice?form=2";

  $postFields = http_build_query([
      "key"     => "JP***g",
      "command" => "get_checkout_details",
      "var1"    => json_encode([
          "requestId"          => "9078698a15d746feadcffbdaf979a198",
          "transactionDetails" => ["amount" => 10000],
          "customerDetails"    => ["mobile" => "9876543210"],
          "filters"            => [
              "paymentOptions" => [
                  "emi" => ["cardless" => "all"]
              ]
          ],
          "useCase" => [
              "checkCustomerEligibility"    => true,
              "checkNTBCustomerEligibility" => true
          ]
      ]),
      "hash" => "{{hash}}" // sha512(key|command|var1|SALT)
  ]);

  $ch = curl_init();

  curl_setopt_array($ch, [
      CURLOPT_URL            => $url,
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_POST           => true,
      CURLOPT_POSTFIELDS     => $postFields,
      CURLOPT_HTTPHEADER     => ["Content-Type: application/x-www-form-urlencoded"]
  ]);

  $response = curl_exec($ch);

  if (curl_error($ch)) {
      echo "Error: " . curl_error($ch);
  } else {
      echo "Status Code: " . curl_getinfo($ch, CURLINFO_HTTP_CODE) . "\n";
      echo "Response: " . $response . "\n";
  }

  curl_close($ch);
  ?>
  ```
</Accordion>

#### Sample response

<Callout icon="✅" theme="okay">
  The response shows the cardless EMI lenders and tenures the customer is eligible for. Show only the eligible tenures (`eligibility.status: true`) to your customer.
</Callout>

**How to read the response**

| Customer type | What the response contains | What to do next |
| :--- | :--- | :--- |
| ETB (pre-approved) | The lender (for example, `LPEMI`) appears under `emi.all.cardless.all` with `tenureOptions`, and the eligible tenures have `eligibility.status: true`. | Show the eligible tenures and go to [Step 2](#step-2-initiate-the-payment). |
| NTB | The lender appears under `emi.ntb.cardless.all` with `eligibility.status: true`, but without `tenureOptions`. | Collect the customer's details and go to [Step 1b](#step-1b-check-main-eligibility-for-ntb-customer). |
| Not eligible | The lender has `eligibility.status: false` with a `reason`. | Don't show this lender. Offer the customer another payment option. |

<Accordion title="GCD response — customer is ETB" icon="fa-info-circle">
  ```json
  {
    "httpCode": "200",
    "message": "",
    "status": 1,
    "data": {
      "details": {
        "paymentOption": {
          "emi": {
            "all": {
              "cardless": {
                "all": {
                  "BIMAPAY": {
                    "tenureOptions": {
                      "BIMAP03": { "tenure": 3, "maximumAmount": null, "eligibility": { "status": true } },
                      "BIMAP06": { "tenure": 6, "maximumAmount": null, "eligibility": { "status": true } },
                      "BIMAPAY": { "tenure": 0, "maximumAmount": null, "eligibility": { "status": true } },
                      "BIMAP09": { "tenure": 9, "maximumAmount": null, "eligibility": { "status": true } },
                      "BIMAP12": { "tenure": 12, "maximumAmount": null, "eligibility": { "status": true } }
                    },
                    "maximumAmount": null,
                    "eligibility": { "status": true }
                  },
                  "SMPI3": {
                    "tenureOptions": {
                      "SMPI03": { "tenure": 3, "maximumAmount": null, "eligibility": { "status": true } }
                    },
                    "maximumAmount": null,
                    "eligibility": { "status": true }
                  },
                  "ICICI_CL": {
                    "tenureOptions": {
                      "ICICIC12": { "tenure": 12, "maximumAmount": null, "eligibility": { "status": true } },
                      "ICICIC03": { "tenure": 3, "maximumAmount": null, "eligibility": { "status": true } },
                      "ICICIC09": { "tenure": 9, "maximumAmount": null, "eligibility": { "status": true } },
                      "ICICIC06": { "tenure": 6, "maximumAmount": null, "eligibility": { "status": true } }
                    },
                    "maximumAmount": null,
                    "eligibility": { "status": true }
                  },
                  "LPEMI": {
                    "tenureOptions": {
                      "LPEMI12": { "tenure": 12, "maximumAmount": null, "eligibility": { "status": true } },
                      "LPEMI": { "tenure": 0, "maximumAmount": null, "eligibility": { "status": true } },
                      "LPEMI09": { "tenure": 9, "maximumAmount": null, "eligibility": { "status": true } },
                      "LPEMI03": { "tenure": 3, "maximumAmount": null, "eligibility": { "status": true } },
                      "LPEMI06": { "tenure": 6, "maximumAmount": null, "eligibility": { "status": true } }
                    },
                    "maximumAmount": null,
                    "eligibility": { "status": true }
                  },
                  "HDFC_CL": {
                    "tenureOptions": {
                      "HDFCCL09": { "tenure": 9, "maximumAmount": null, "eligibility": { "status": true } },
                      "HDFCCL18": { "tenure": 18, "maximumAmount": null, "eligibility": { "status": true } },
                      "HDFCCL06": { "tenure": 6, "maximumAmount": null, "eligibility": { "status": true } },
                      "HDFCCL03": { "tenure": 3, "maximumAmount": null, "eligibility": { "status": true } },
                      "HDFCCL12": { "tenure": 12, "maximumAmount": null, "eligibility": { "status": true } }
                    },
                    "maximumAmount": null,
                    "eligibility": { "status": true }
                  }
                },
                "hasEligible": true
              }
            }
          }
        }
      }
    }
  }
  ```
</Accordion>

<Accordion title="GCD response — customer is NTB" icon="fa-info-circle">
  **Scenario:** The customer is NTB for LazyPay EMI (`LPEMI`). `LPEMI` appears under `emi.ntb.cardless.all` without tenures. Check main eligibility in [Step 1b](#step-1b-check-main-eligibility-for-ntb-customer).

  ```json
  {
    "httpCode": "200",
    "message": "",
    "status": 1,
    "data": {
      "details": {
        "paymentOption": {
          "emi": {
            "all": {
              "cardless": {
                "all": {
                  "BIMAPAY": {
                    "tenureOptions": {
                      "BIMAP03": { "tenure": 3, "maximumAmount": null, "eligibility": { "status": true } },
                      "BIMAP06": { "tenure": 6, "maximumAmount": null, "eligibility": { "status": true } },
                      "BIMAPAY": {
                        "tenure": 0,
                        "maximumAmount": null,
                        "eligibility": {
                          "status": false,
                          "reason": "This mobile number is not eligible. Please change the mobile number."
                        }
                      },
                      "BIMAP09": { "tenure": 9, "maximumAmount": null, "eligibility": { "status": true } },
                      "BIMAP12": { "tenure": 12, "maximumAmount": null, "eligibility": { "status": true } }
                    },
                    "maximumAmount": null,
                    "eligibility": { "status": true }
                  },
                  "SMPI3": {
                    "tenureOptions": {
                      "SMPI03": { "tenure": 3, "maximumAmount": null, "eligibility": { "status": true } }
                    },
                    "maximumAmount": null,
                    "eligibility": { "status": true }
                  },
                  "ICICI_CL": {
                    "tenureOptions": {
                      "ICICIC12": { "tenure": 12, "maximumAmount": null, "eligibility": { "status": true } },
                      "ICICIC03": { "tenure": 3, "maximumAmount": null, "eligibility": { "status": true } },
                      "ICICIC09": { "tenure": 9, "maximumAmount": null, "eligibility": { "status": true } },
                      "ICICIC06": { "tenure": 6, "maximumAmount": null, "eligibility": { "status": true } }
                    },
                    "maximumAmount": null,
                    "eligibility": { "status": true }
                  },
                  "HDFC_CL": {
                    "tenureOptions": {
                      "HDFCCL09": { "tenure": 9, "maximumAmount": null, "eligibility": { "status": true } },
                      "HDFCCL18": { "tenure": 18, "maximumAmount": null, "eligibility": { "status": true } },
                      "HDFCCL06": { "tenure": 6, "maximumAmount": null, "eligibility": { "status": true } },
                      "HDFCCL03": { "tenure": 3, "maximumAmount": null, "eligibility": { "status": true } },
                      "HDFCCL12": { "tenure": 12, "maximumAmount": null, "eligibility": { "status": true } }
                    },
                    "maximumAmount": null,
                    "eligibility": { "status": true }
                  }
                },
                "hasEligible": true
              }
            },
            "ntb": {
              "cardless": {
                "all": {
                  "LPEMI": {
                    "maximumAmount": null,
                    "eligibility": { "status": true }
                  }
                },
                "hasEligible": true
              }
            }
          }
        }
      }
    }
  }
  ```
</Accordion>

<Accordion title="GCD response — customer is not eligible" icon="fa-info-circle">
  **Scenario:** The customer is not eligible for LazyPay EMI (`LPEMI`). Every `LPEMI` tenure has `eligibility.status: false`.

  ```json
  {
    "httpCode": "200",
    "message": "",
    "status": 1,
    "data": {
      "details": {
        "paymentOption": {
          "emi": {
            "all": {
              "cardless": {
                "all": {
                  "SMPI3": {
                    "tenureOptions": {
                      "SMPI03": { "tenure": 3, "maximumAmount": null, "eligibility": { "status": true } }
                    },
                    "maximumAmount": null,
                    "eligibility": { "status": true }
                  },
                  "LPEMI": {
                    "tenureOptions": {
                      "LPEMI12": { "tenure": 12, "maximumAmount": null, "eligibility": { "status": false, "reason": "User is not eligible for cof product" } },
                      "LPEMI": { "tenure": 0, "maximumAmount": null, "eligibility": { "status": false, "reason": "User is not eligible for cof product" } },
                      "LPEMI09": { "tenure": 9, "maximumAmount": null, "eligibility": { "status": false, "reason": "User is not eligible for cof product" } },
                      "LPEMI03": { "tenure": 3, "maximumAmount": null, "eligibility": { "status": false, "reason": "User is not eligible for cof product" } },
                      "LPEMI06": { "tenure": 6, "maximumAmount": null, "eligibility": { "status": false, "reason": "User is not eligible for cof product" } }
                    },
                    "maximumAmount": null,
                    "eligibility": {
                      "status": false,
                      "reason": "Customer not eligible for EMI"
                    }
                  },
                  "HDFC_CL": {
                    "tenureOptions": {
                      "HDFCCL09": { "tenure": 9, "maximumAmount": null, "eligibility": { "status": true } },
                      "HDFCCL18": { "tenure": 18, "maximumAmount": null, "eligibility": { "status": true } },
                      "HDFCCL06": { "tenure": 6, "maximumAmount": null, "eligibility": { "status": true } },
                      "HDFCCL03": { "tenure": 3, "maximumAmount": null, "eligibility": { "status": true } },
                      "HDFCCL12": { "tenure": 12, "maximumAmount": null, "eligibility": { "status": true } }
                    },
                    "maximumAmount": null,
                    "eligibility": { "status": true }
                  }
                },
                "hasEligible": true
              }
            }
          }
        }
      }
    }
  }
  ```
</Accordion>

### Step 1b: Check Main Eligibility for NTB Customer

If **Get Checkout Details** shows the customer is New to the Bank (**NTB**) for LazyPay, you must obtain full eligibility using **Get EMI Checkout Details** (GECD). Collect the required personal information (PI) from the customer and include it in the GECD request to check main eligibility. When the customer is eligible, the response includes the down payment, and any applicable fees (similar to the pre-approved path).

{/* REVIEW: Pending engineering confirmation. The sample response below returns tenureOptions and maximumAmount only, not the down payment or fees. */}

| Environment | URL |
| :---------- | :-- |
| Production  | `https://info.payu.in/info/linkAndPay/get_emi_checkout_details` |
| Test        | `https://test.payu.in/info/linkAndPay/get_emi_checkout_details` |

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location 'https://test.payu.in/info/linkAndPay/get_emi_checkout_details' \
  --header 'x-credential-username: JP***g' \
  --header 'Content-Type: application/json' \
  --header 'authorization: hmac username="JP***g", algorithm="sha512", headers="date", signature="{{signature}}"' \
  --header 'date: Wed, 21 Oct 2026 09:39:46 GMT' \
  --data '{
      "bankCode": "LPEMI",
      "phone": "9876543210",
      "amount": "10000.00",
      "pg": "EMI",
      "checkCustomerEligibilityWithDetails": true,
      "customerDetails": {
          "panNumber": "ABCDE1234F",
          "dob": "01-01-1990",
          "zipcode": "560001",
          "firstName": "Ashish",
          "lastName": "Kumar",
          "bureauPullConsent": "false",
          "gender": "Male",
          "income": "100000",
          "employeeType": "Salaried"
      }
  }'
  ```
  ```python
  import requests
  import json

  url = "https://test.payu.in/info/linkAndPay/get_emi_checkout_details"

  headers = {
      "x-credential-username": "JP***g",
      "Content-Type": "application/json",
      "authorization": 'hmac username="JP***g", algorithm="sha512", headers="date", signature="{{signature}}"',
      "date": "Wed, 21 Oct 2026 09:39:46 GMT"
  }

  payload = {
      "bankCode": "LPEMI",
      "phone": "9876543210",
      "amount": "10000.00",
      "pg": "EMI",
      "checkCustomerEligibilityWithDetails": True,
      "customerDetails": {
          "panNumber": "ABCDE1234F",
          "dob": "01-01-1990",
          "zipcode": "560001",
          "firstName": "Ashish",
          "lastName": "Kumar",
          "bureauPullConsent": "false",
          "gender": "Male",
          "income": "100000",
          "employeeType": "Salaried"
      }
  }

  try:
      response = requests.post(url, headers=headers, data=json.dumps(payload))
      print("Status Code:", response.status_code)
      print("Response:", response.text)
  except requests.exceptions.RequestException as e:
      print("Error:", e)
  ```
  ```csharp
  using System;
  using System.Net.Http;
  using System.Text;
  using System.Threading.Tasks;

  class Program
  {
      static async Task Main(string[] args)
      {
          var client = new HttpClient();

          client.DefaultRequestHeaders.Add("x-credential-username", "JP***g");
          client.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "hmac username=\"JP***g\", algorithm=\"sha512\", headers=\"date\", signature=\"{{signature}}\"");
          client.DefaultRequestHeaders.TryAddWithoutValidation("date", "Wed, 21 Oct 2026 09:39:46 GMT");

          var jsonBody = @"{
              ""bankCode"": ""LPEMI"",
              ""phone"": ""9876543210"",
              ""amount"": ""10000.00"",
              ""pg"": ""EMI"",
              ""checkCustomerEligibilityWithDetails"": true,
              ""customerDetails"": {
                  ""panNumber"": ""ABCDE1234F"",
                  ""dob"": ""01-01-1990"",
                  ""zipcode"": ""560001"",
                  ""firstName"": ""Ashish"",
                  ""lastName"": ""Kumar"",
                  ""bureauPullConsent"": ""false"",
                  ""gender"": ""Male"",
                  ""income"": ""100000"",
                  ""employeeType"": ""Salaried""
              }
          }";

          var content = new StringContent(jsonBody, Encoding.UTF8, "application/json");

          try
          {
              var response = await client.PostAsync("https://test.payu.in/info/linkAndPay/get_emi_checkout_details", content);
              string responseBody = await response.Content.ReadAsStringAsync();
              Console.WriteLine("Status Code: " + response.StatusCode);
              Console.WriteLine("Response: " + responseBody);
          }
          catch (HttpRequestException e)
          {
              Console.WriteLine("Error: " + e.Message);
          }
      }
  }
  ```
  ```javascript
  async function getEmiCheckoutDetails() {
      const url = "https://test.payu.in/info/linkAndPay/get_emi_checkout_details";

      const payload = {
          bankCode: "LPEMI",
          phone: "9876543210",
          amount: "10000.00",
          pg: "EMI",
          checkCustomerEligibilityWithDetails: true,
          customerDetails: {
              panNumber: "ABCDE1234F",
              dob: "01-01-1990",
              zipcode: "560001",
              firstName: "Ashish",
              lastName: "Kumar",
              bureauPullConsent: "false",
              gender: "Male",
              income: "100000",
              employeeType: "Salaried"
          }
      };

      try {
          const response = await fetch(url, {
              method: "POST",
              headers: {
                  "x-credential-username": "JP***g",
                  "Content-Type": "application/json",
                  "authorization": 'hmac username="JP***g", algorithm="sha512", headers="date", signature="{{signature}}"',
                  "date": "Wed, 21 Oct 2026 09:39:46 GMT"
              },
              body: JSON.stringify(payload)
          });

          const data = await response.text();
          console.log("Status Code:", response.status);
          console.log("Response:", data);
      } catch (error) {
          console.error("Error:", error);
      }
  }

  getEmiCheckoutDetails();
  ```
  ```java
  import java.io.*;
  import java.net.*;
  import java.nio.charset.StandardCharsets;

  public class GetEmiCheckoutDetails {
      public static void main(String[] args) {
          try {
              URL url = new URL("https://test.payu.in/info/linkAndPay/get_emi_checkout_details");
              HttpURLConnection conn = (HttpURLConnection) url.openConnection();
              conn.setRequestMethod("POST");
              conn.setRequestProperty("x-credential-username", "JP***g");
              conn.setRequestProperty("Content-Type", "application/json");
              conn.setRequestProperty("authorization", "hmac username=\"JP***g\", algorithm=\"sha512\", headers=\"date\", signature=\"{{signature}}\"");
              conn.setRequestProperty("date", "Wed, 21 Oct 2026 09:39:46 GMT");
              conn.setDoOutput(true);

              String jsonBody = "{"
                  + "\"bankCode\":\"LPEMI\","
                  + "\"phone\":\"9876543210\","
                  + "\"amount\":\"10000.00\","
                  + "\"pg\":\"EMI\","
                  + "\"checkCustomerEligibilityWithDetails\":true,"
                  + "\"customerDetails\":{"
                  +     "\"panNumber\":\"ABCDE1234F\","
                  +     "\"dob\":\"01-01-1990\","
                  +     "\"zipcode\":\"560001\","
                  +     "\"firstName\":\"Ashish\","
                  +     "\"lastName\":\"Kumar\","
                  +     "\"bureauPullConsent\":\"false\","
                  +     "\"gender\":\"Male\","
                  +     "\"income\":\"100000\","
                  +     "\"employeeType\":\"Salaried\""
                  + "}"
                  + "}";

              try (OutputStream os = conn.getOutputStream()) {
                  os.write(jsonBody.getBytes(StandardCharsets.UTF_8));
              }

              System.out.println("Status Code: " + conn.getResponseCode());

              BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8));
              StringBuilder response = new StringBuilder();
              String line;
              while ((line = reader.readLine()) != null) {
                  response.append(line);
              }
              reader.close();

              System.out.println("Response: " + response);
          } catch (Exception e) {
              System.out.println("Error: " + e.getMessage());
          }
      }
  }
  ```
  ```php
  <?php

  $url = "https://test.payu.in/info/linkAndPay/get_emi_checkout_details";

  $payload = json_encode([
      "bankCode"                            => "LPEMI",
      "phone"                               => "9876543210",
      "amount"                              => "10000.00",
      "pg"                                  => "EMI",
      "checkCustomerEligibilityWithDetails" => true,
      "customerDetails"                     => [
          "panNumber"         => "ABCDE1234F",
          "dob"               => "01-01-1990",
          "zipcode"           => "560001",
          "firstName"         => "Ashish",
          "lastName"          => "Kumar",
          "bureauPullConsent" => "false",
          "gender"            => "Male",
          "income"            => "100000",
          "employeeType"      => "Salaried"
      ]
  ]);

  $ch = curl_init();

  curl_setopt_array($ch, [
      CURLOPT_URL            => $url,
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_POST           => true,
      CURLOPT_POSTFIELDS     => $payload,
      CURLOPT_HTTPHEADER     => [
          "x-credential-username: JP***g",
          "Content-Type: application/json",
          'authorization: hmac username="JP***g", algorithm="sha512", headers="date", signature="{{signature}}"',
          "date: Wed, 21 Oct 2026 09:39:46 GMT"
      ]
  ]);

  $response = curl_exec($ch);

  if (curl_error($ch)) {
      echo "Error: " . curl_error($ch);
  } else {
      echo "Status Code: " . curl_getinfo($ch, CURLINFO_HTTP_CODE) . "\n";
      echo "Response: " . $response . "\n";
  }

  curl_close($ch);
  ?>
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  #### Success scenario

  Response when registration got success

  ```json
  {
    "httpCode": "200",
    "message": "",
    "status": 1,
    "data": {
      "emi": {
        "ntb": {
          "cardless": {
            "all": {
              "LPEMI": {
                "tenureOptions": {
                  "LPEMI12": {
                    "tenure": 12,
                    "maximumAmount": 100000.0,
                    "eligibility": {
                      "status": false,
                      "reason": "Tenure not available"
                    }
                  },
                  "LPEMI03": {
                    "tenure": 3,
                    "maximumAmount": 60000.0,
                    "eligibility": {
                      "status": true
                    }
                  },
                  "LPEMI09": {
                    "tenure": 9,
                    "maximumAmount": 100000.0,
                    "eligibility": {
                      "status": false,
                      "reason": "Tenure not available"
                    }
                  },
                  "LPEMI06": {
                    "tenure": 6,
                    "maximumAmount": 100000.0,
                    "eligibility": {
                      "status": true
                    }
                  },
                  "LPEMI": {
                    "tenure": 0,
                    "maximumAmount": 100000.0,
                    "eligibility": {
                      "status": false,
                      "reason": "Tenure not available"
                    }
                  }
                },
                "eligibility": {
                  "status": true
                }
              }
            },
            "hasEligible": true
          }
        }
      }
    }
  }
  ```
</Accordion>

## Step 2: Initiate the payment

Post the following additional parameters for using the Cardless EMI. Check the response when you try enter the values in API Reference. For complete list of parameters, refer to [Collect Payment API - EMI](ref:_payment_merchant_hosted_emi) for the complete list parameters with **Try It** experience.

### Request Parameters


<Tabs>
  <Tab title="Request Parameters">

**Mandatory Parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| key | `String` Merchant key provided by PayU during onboarding. | JP\*\*\*\*g |
| txnid | `String` The transaction ID is a reference number for a specific order that is generated by the merchant. | |
| amount | `String` The payment amount for the transaction. | |
| productinfo | `String` A brief description of the product. | |
| firstname | `String` The first name of the customer. | Ashish |
| email | `String` The email address of the customer. | abc@payu.in |
| phone | `String` The phone number of the customer. | |
| pg | `String` It defines the payment category. In this integration, "EMI" must be specified. | EMI |
| bankcode | `String` Post this parameter to identify payment options with unique bank codes and use getEmiAmountAccordingToInterest API to check for EMI code for corresponding tenure. For the list of EMI codes, refer to EMI Codes. | HDFCCL06 |
| panNumber *(mandatory for ICICI, HDFC Bank, and Homecredit Cardless EMI; not mandatory for other banks)* | `String` <Glossary>PAN</Glossary> number of the customer. | ABCTY1234D |
| ccnum *(mandatory only for Bajaj Finserv)* | `String` Use 13-19 digit card number for credit/debit cards and validate with LUHN algorithm. | 5123456789012346 |
| surl | `String` The success URL, which is the page PayU will redirect to if the transaction is successful. | |
| furl | `String` The Failure URL, which is the page PayU will redirect to if the transaction is failed. | |
| hash | `String` It is the hash calculated by the merchant. The hash calculation logic is: SHA-512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt) | |

**Optional Parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| ccname | `String` This parameter must contain the name on card – as entered by the customer for the transaction. | Ashish Kumar |
| ccvv | `String` Use 3-digit CVV number for credit/debit cards and 4-digit security code (4DBC/CID) for AMEX cards. Validate with BIN API. | 123 |
| ccexpmon | `String` This parameter must contain the card's expiry month in MM format. For months 1-9, prepend 0. For months 10-12, use as-is. | 10 |
| ccexpyr | `String` This parameter must contain the card's expiry year in four digits. | 2021 |
| address1 | `String` The first line of the billing address. For Fraud Detection: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information. | |
| address2 | `String` The second line of the billing address. | |
| city | `String` The city where your customer resides as part of the billing address. | |
| state | `String` The state where your customer resides as part of the billing address. | |
| country | `String` The country where your customer resides. | |
| zipcode | `String` Billing address zip code is mandatory for the cardless EMI option. `Character Limit`-20 | |
| udf1 | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. | |
| udf2 | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. | |
| udf3 | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. | |
| udf4 | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. | |
| udf5 | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. | |

  </Tab>

  <Tab title="Sample Request">

  ```curl
  curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=JP***g&txnid=EaE4ZO3vU4iPsp&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=EMI&bankcode=EMI03&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=1234&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=undefined&store_card_token=1234 4567 2456 3566&storecard_token_type=1&additional_info={“last4Digits”: “1234”, “tavv”: “ABCDEFGH”,”trid”:”1234567890”, “tokenRefNo”:”abcde123456”}&hash=fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"
  ```
  ```javascript
  /**
   * PayU Cardless EMI Payment Integration using Fetch API
   * 
   * IMPORTANT: This should only be executed server-side (e.g., in Node.js), never in the browser,
   * as it contains sensitive payment information.
   */

  // Payment endpoint
  const url = 'https://test.payu.in/_payment';

  // Additional info as a JSON object
  const additionalInfo = {
    "last4Digits": "1234",
    "tavv": "ABCDEFGH",
    "trid": "1234567890",
    "tokenRefNo": "abcde123456"
  };

  // Form data parameters
  const formData = new URLSearchParams();
  formData.append('key', 'JP***g');                  // Your merchant key
  formData.append('txnid', 'EaE4ZO3vU4iPsp');       // Unique transaction ID
  formData.append('amount', '10.00');               // Payment amount
  formData.append('firstname', 'Ashish');           // Customer's name
  formData.append('email', 'test@gmail.com');       // Customer's email
  formData.append('phone', '9876543210');           // Customer's phone
  formData.append('productinfo', 'iPhone');         // Product information
  formData.append('pg', 'EMI');                     // Payment gateway (EMI)
  formData.append('bankcode', 'EMI03');             // Bank code (Cardless EMI provider)
  formData.append('surl', 'https://apiplayground-response.herokuapp.com'); // Success URL
  formData.append('furl', 'https://apiplayground-response.herokuapp.com'); // Failure URL
  // Token and card details
  formData.append('ccnum', '1234');                 // Limited card details for verification
  formData.append('ccexpmon', '05');                // Expiry month
  formData.append('ccexpyr', '2022');               // Expiry year 
  formData.append('ccvv', '123');                   // CVV
  formData.append('ccname', 'undefined');           // Cardholder name
  formData.append('store_card_token', '1234 4567 2456 3566'); // Tokenized card
  formData.append('storecard_token_type', '1');     // Token type
  formData.append('additional_info', JSON.stringify(additionalInfo)); // Tokenization details
  // Security hash
  formData.append('hash', 'fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304');

  // Request options
  const requestOptions = {
    method: 'POST',
    headers: {
      'accept': 'application/json',
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: formData
  };

  // Execute the request
  fetch(url, requestOptions)
    .then(response => {
      console.log('Status Code:', response.status);
      return response.text(); // or response.json() if you're sure it returns JSON
    })
    .then(data => {
      console.log('Response:', data);
      // Process payment response here
    })
    .catch(error => {
      console.error('Error:', error);
    });

  ```
  ```python
  import urllib.request
  import urllib.parse
  import json
  from typing import Dict, Any

  def process_cardless_emi_payment() -> Dict[str, Any]:
      """
      Process cardless EMI payment using PayU's Merchant Hosted Checkout
      
      IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
      
      Returns:
          Dictionary with response from PayU API
      """
      # API endpoint
      url = "https://test.payu.in/_payment"
      
      # Additional info as a dictionary
      additional_info = {
          "last4Digits": "1234",
          "tavv": "ABCDEFGH",
          "trid": "1234567890",
          "tokenRefNo": "abcde123456"
      }
      
      # Prepare the form data
      payload = {
          "key": "JP***g",                     # Your merchant key
          "txnid": "EaE4ZO3vU4iPsp",           # Unique transaction ID
          "amount": "10.00",                   # Payment amount
          "firstname": "Ashish",               # Customer's name
          "email": "test@gmail.com",           # Customer's email
          "phone": "9876543210",               # Customer's phone
          "productinfo": "iPhone",             # Product information
          "pg": "EMI",                         # Payment gateway (EMI)
          "bankcode": "EMI03",                 # Bank code (Cardless EMI provider)
          "surl": "https://apiplayground-response.herokuapp.com", # Success URL
          "furl": "https://apiplayground-response.herokuapp.com", # Failure URL
          # Token and card details
          "ccnum": "1234",                     # Limited card details for verification
          "ccexpmon": "05",                    # Expiry month
          "ccexpyr": "2022",                   # Expiry year
          "ccvv": "123",                       # CVV
          "ccname": "undefined",               # Cardholder name
          "store_card_token": "1234 4567 2456 3566", # Tokenized card
          "storecard_token_type": "1",         # Token type
          "additional_info": json.dumps(additional_info), # Tokenization details
          # Security hash
          "hash": "fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"
      }
      
      # Convert dictionary to URL-encoded form data
      data = urllib.parse.urlencode(payload).encode('utf-8')
      
      # Set headers
      headers = {
          "accept": "application/json",
          "Content-Type": "application/x-www-form-urlencoded"
      }
      
      # Create a request object
      req = urllib.request.Request(url, data=data, headers=headers, method="POST")
      
      try:
          # Send the request and get the response
          with urllib.request.urlopen(req) as response:
              response_data = response.read().decode('utf-8')
              
              # Process and return response
              return {
                  "status_code": response.getcode(),
                  "response": response_data
              }
              
      except urllib.error.HTTPError as e:
          # Handle HTTP errors
          error_data = e.read().decode('utf-8')
          return {
              "status_code": e.code,
              "error": e.reason,
              "response": error_data
          }
          
      except Exception as e:
          # Handle other exceptions
          return {
              "status_code": 500,
              "error": str(e),
              "response": "An error occurred during payment processing"
          }

  # Example usage
  if __name__ == "__main__":
      result = process_cardless_emi_payment()
      print(f"Status Code: {result['status_code']}")
      if 'error' in result:
          print(f"Error: {result['error']}")
      print(f"Response: {result['response']}")

  ```
  ```php
  <?php
  /**
   * Process cardless EMI payment using PayU's Merchant Hosted Checkout
   * 
   * IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
   * 
   * @return array Response from PayU API
   */
  function processCardlessEmiPayment() {
      // API endpoint
      $url = "https://test.payu.in/_payment";
      
      // Additional info as an array
      $additionalInfo = [
          "last4Digits" => "1234",
          "tavv" => "ABCDEFGH",
          "trid" => "1234567890",
          "tokenRefNo" => "abcde123456"
      ];
      
      // Prepare the form data
      $payload = [
          "key" => "JP***g",                      // Your merchant key
          "txnid" => "EaE4ZO3vU4iPsp",            // Unique transaction ID
          "amount" => "10.00",                    // Payment amount
          "firstname" => "Ashish",                // Customer's name
          "email" => "test@gmail.com",            // Customer's email
          "phone" => "9876543210",                // Customer's phone
          "productinfo" => "iPhone",              // Product information
          "pg" => "EMI",                          // Payment gateway (EMI)
          "bankcode" => "EMI03",                  // Bank code (Cardless EMI provider)
          "surl" => "https://apiplayground-response.herokuapp.com", // Success URL
          "furl" => "https://apiplayground-response.herokuapp.com", // Failure URL
          // Token and card details
          "ccnum" => "1234",                      // Limited card details for verification
          "ccexpmon" => "05",                     // Expiry month
          "ccexpyr" => "2022",                    // Expiry year
          "ccvv" => "123",                        // CVV
          "ccname" => "undefined",                // Cardholder name
          "store_card_token" => "1234 4567 2456 3566", // Tokenized card
          "storecard_token_type" => "1",          // Token type
          "additional_info" => json_encode($additionalInfo), // Tokenization details
          // Security hash
          "hash" => "fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"
      ];
      
      // Initialize cURL session
      $ch = curl_init($url);
      
      // Set cURL options
      curl_setopt($ch, CURLOPT_POST, true);
      curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
      curl_setopt($ch, CURLOPT_HTTPHEADER, [
          "accept: application/json",
          "Content-Type: application/x-www-form-urlencoded"
      ]);
      
      // For additional security in production
      curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);
      curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
      
      // Execute the request
      $response = curl_exec($ch);
      $statusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
      $error = curl_error($ch);
      $errno = curl_errno($ch);
      
      // Close cURL session
      curl_close($ch);
      
      // Handle response
      if ($errno) {
          return [
              "status_code" => 500,
              "error" => $error,
              "response" => "cURL Error: " . $error
          ];
      }
      
      return [
          "status_code" => $statusCode,
          "response" => $response
      ];
  }

  // Example usage
  $result = processCardlessEmiPayment();
  echo "Status Code: " . $result["status_code"] . "\n";
  if (isset($result["error"])) {
      echo "Error: " . $result["error"] . "\n";
  }
  echo "Response: " . $result["response"] . "\n";
  ?>

  ```
  ```java
  import java.io.BufferedReader;
  import java.io.DataOutputStream;
  import java.io.IOException;
  import java.io.InputStreamReader;
  import java.net.HttpURLConnection;
  import java.net.URL;
  import java.net.URLEncoder;
  import java.nio.charset.StandardCharsets;
  import java.util.HashMap;
  import java.util.Map;
  import java.util.StringJoiner;

  /**
   * PayU Cardless EMI Payment Processor for Merchant Hosted Checkout
   * 
   * IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
   */
  public class PayUCardlessEmiPaymentProcessor {
      
      // API endpoint
      private static final String PAYU_TEST_URL = "https://test.payu.in/_payment";
      
      /**
       * Process cardless EMI payment through PayU
       * @return PaymentResponse containing status and response data
       */
      public PaymentResponse processCardlessEmiPayment() {
          try {
              // Initialize URL
              URL url = new URL(PAYU_TEST_URL);
              
              // Additional info JSON
              String additionalInfo = "{"
                  + "\"last4Digits\": \"1234\","
                  + "\"tavv\": \"ABCDEFGH\","
                  + "\"trid\": \"1234567890\","
                  + "\"tokenRefNo\": \"abcde123456\""
                  + "}";
              
              // Prepare form parameters
              Map<String, String> params = new HashMap<>();
              params.put("key", "JP***g");                      // Your merchant key
              params.put("txnid", "EaE4ZO3vU4iPsp");            // Unique transaction ID
              params.put("amount", "10.00");                    // Payment amount
              params.put("firstname", "Ashish");                // Customer's name
              params.put("email", "test@gmail.com");            // Customer's email
              params.put("phone", "9876543210");                // Customer's phone
              params.put("productinfo", "iPhone");              // Product information
              params.put("pg", "EMI");                          // Payment gateway (EMI)
              params.put("bankcode", "EMI03");                  // Bank code (Cardless EMI provider)
              params.put("surl", "https://apiplayground-response.herokuapp.com"); // Success URL
              params.put("furl", "https://apiplayground-response.herokuapp.com"); // Failure URL
              // Token and card details
              params.put("ccnum", "1234");                      // Limited card details for verification
              params.put("ccexpmon", "05");                     // Expiry month
              params.put("ccexpyr", "2022");                    // Expiry year
              params.put("ccvv", "123");                        // CVV
              params.put("ccname", "undefined");                // Cardholder name
              params.put("store_card_token", "1234 4567 2456 3566"); // Tokenized card
              params.put("storecard_token_type", "1");          // Token type
              params.put("additional_info", additionalInfo);    // Tokenization details
              // Security hash
              params.put("hash", "fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304");
              
              // Convert parameters to URL-encoded form data
              StringJoiner formData = new StringJoiner("&");
              for (Map.Entry<String, String> entry : params.entrySet()) {
                  formData.add(URLEncoder.encode(entry.getKey(), "UTF-8") + "=" + 
                               URLEncoder.encode(entry.getValue(), "UTF-8"));
              }
              byte[] postData = formData.toString().getBytes(StandardCharsets.UTF_8);
              
              // Configure connection
              HttpURLConnection conn = (HttpURLConnection) url.openConnection();
              conn.setRequestMethod("POST");
              conn.setRequestProperty("accept", "application/json");
              conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
              conn.setRequestProperty("Content-Length", String.valueOf(postData.length));
              conn.setDoOutput(true);
              conn.setConnectTimeout(5000);
              conn.setReadTimeout(15000);
              
              // Send request
              try (DataOutputStream dos = new DataOutputStream(conn.getOutputStream())) {
                  dos.write(postData);
                  dos.flush();
              }
              
              // Get response
              int responseCode = conn.getResponseCode();
              
              // Read response data
              StringBuilder response = new StringBuilder();
              try (BufferedReader reader = new BufferedReader(
                      new InputStreamReader(
                          responseCode >= 400 ? conn.getErrorStream() : conn.getInputStream(), 
                          StandardCharsets.UTF_8))) {
                          
                  String line;
                  while ((line = reader.readLine()) != null) {
                      response.append(line);
                  }
              }
              
              return new PaymentResponse(responseCode, response.toString(), null);
              
          } catch (IOException e) {
              // Handle exception
              return new PaymentResponse(500, null, "Error: " + e.getMessage());
          }
      }
      
      /**
       * Payment response wrapper class
       */
      public static class PaymentResponse {
          private final int statusCode;
          private final String response;
          private final String error;
          
          public PaymentResponse(int statusCode, String response, String error) {
              this.statusCode = statusCode;
              this.response = response;
              this.error = error;
          }
          
          public int getStatusCode() {
              return statusCode;
          }
          
          public String getResponse() {
              return response;
          }
          
          public String getError() {
              return error;
          }
          
          public boolean isSuccess() {
              return statusCode >= 200 && statusCode < 300;
          }
      }
      
      // Example usage
      public static void main(String[] args) {
          PayUCardlessEmiPaymentProcessor processor = new PayUCardlessEmiPaymentProcessor();
          PaymentResponse result = processor.processCardlessEmiPayment();
          
          System.out.println("Status Code: " + result.getStatusCode());
          if (result.isSuccess()) {
              System.out.println("Response: " + result.getResponse());
          } else {
              System.out.println("Error: " + result.getError());
          }
      }
  }

  ```
  ```csharp
  using System;
  using System.Collections.Generic;
  using System.Net.Http;
  using System.Threading.Tasks;
  using System.Text;
  using System.Text.Json;

  namespace PayUCardlessEmiIntegration
  {
      /// <summary>
      /// PayU Cardless EMI Payment Processor for Merchant Hosted Checkout
      /// 
      /// IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
      /// </summary>
      public class PayUCardlessEmiPaymentProcessor
      {
          // API endpoint
          private const string PayuTestUrl = "https://test.payu.in/_payment";
          
          /// <summary>
          /// Process cardless EMI payment through PayU
          /// </summary>
          /// <returns>PaymentResponse containing status and response data</returns>
          public async Task<PaymentResponse> ProcessCardlessEmiPaymentAsync()
          {
              try
              {
                  // Create additional info object
                  var additionalInfo = new
                  {
                      last4Digits = "1234",
                      tavv = "ABCDEFGH",
                      trid = "1234567890",
                      tokenRefNo = "abcde123456"
                  };
                  
                  // Serialize additional info to JSON
                  string additionalInfoJson = JsonSerializer.Serialize(additionalInfo);
                  
                  // Prepare form parameters
                  var formData = new Dictionary<string, string>
                  {
                      { "key", "JP***g" },                       // Your merchant key
                      { "txnid", "EaE4ZO3vU4iPsp" },             // Unique transaction ID
                      { "amount", "10.00" },                     // Payment amount
                      { "firstname", "Ashish" },                 // Customer's name
                      { "email", "test@gmail.com" },             // Customer's email
                      { "phone", "9876543210" },                 // Customer's phone
                      { "productinfo", "iPhone" },               // Product information
                      { "pg", "EMI" },                           // Payment gateway (EMI)
                      { "bankcode", "EMI03" },                   // Bank code (Cardless EMI provider)
                      { "surl", "https://apiplayground-response.herokuapp.com" }, // Success URL
                      { "furl", "https://apiplayground-response.herokuapp.com" }, // Failure URL
                      // Token and card details
                      { "ccnum", "1234" },                       // Limited card details for verification
                      { "ccexpmon", "05" },                      // Expiry month
                      { "ccexpyr", "2022" },                     // Expiry year
                      { "ccvv", "123" },                         // CVV
                      { "ccname", "undefined" },                 // Cardholder name
                      { "store_card_token", "1234 4567 2456 3566" }, // Tokenized card
                      { "storecard_token_type", "1" },           // Token type
                      { "additional_info", additionalInfoJson }, // Tokenization details
                      // Security hash
                      { "hash", "fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304" }
                  };
                  
                  // Create HttpClient with timeout
                  using (var httpClient = new HttpClient())
                  {
                      httpClient.Timeout = TimeSpan.FromSeconds(30);
                      
                      // Convert form data to content
                      var content = new FormUrlEncodedContent(formData);
                      
                      // Add headers
                      content.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue("application/x-www-form-urlencoded");
                      httpClient.DefaultRequestHeaders.Add("accept", "application/json");
                      
                      // Send POST request
                      var response = await httpClient.PostAsync(PayuTestUrl, content);
                      
                      // Get response content
                      var responseContent = await response.Content.ReadAsStringAsync();
                      
                      return new PaymentResponse(
                          (int)response.StatusCode,
                          responseContent,
                          null
                      );
                  }
              }
              catch (Exception ex)
              {
                  // Handle exception
                  return new PaymentResponse(
                      500,
                      null,
                      $"Error: {ex.Message}"
                  );
              }
          }
          
          /// <summary>
          /// Payment response wrapper class
          /// </summary>
          public class PaymentResponse
          {
              public int StatusCode { get; }
              public string Response { get; }
              public string Error { get; }
              
              public PaymentResponse(int statusCode, string response, string error)
              {
                  StatusCode = statusCode;
                  Response = response;
                  Error = error;
              }
              
              public bool IsSuccess => StatusCode >= 200 && StatusCode < 300;
          }
      }
      
      // Example usage
      class Program
      {
          static async Task Main(string[] args)
          {
              var processor = new PayUCardlessEmiPaymentProcessor();
              var result = await processor.ProcessCardlessEmiPaymentAsync();
              
              Console.WriteLine($"Status Code: {result.StatusCode}");
              if (result.IsSuccess)
              {
                  Console.WriteLine($"Response: {result.Response}");
              }
              else
              {
                  Console.WriteLine($"Error: {result.Error}");
              }
          }
      }
  }

  ```

  </Tab>
</Tabs>


<HashingRequestParameters />

## Step 3: Check the response from PayU

<Accordion title="Sample response" icon="fa-info-circle">
  ```
  Array
  (
      [mihpayid] => 403993715523602563
      [status] => success
      [unmappedstatus] => captured
      [key] => smsplus
      [txnid] => v2tWbbdUOuacK9
      [amount] => 20000.00
      [discount] => 0.00
      [net_amount_debit] => 20000.00
      [addedon] => 2021-07-27 11:14:44
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
      [hash] => 10f8ead10cdf5f9b7bf9046987de046d63d62d6679dded9d5da8145f459066943570eec4aa184494ae77f99a8bcd55452af3c4eff0d7a7d3ba809c97b7c73045
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
      [PG_TYPE] => EMI-PG
      [bank_ref_num] => 3d7cc4a4-00c8-4705-a0e7-5708d2c2bb75
      [bankcode]=> EMIA3
      [error] => E000
      [error_Message] => No Error
      [name_on_card] => payu
      [cardnum] =>XXXXXXXXXXXX1234
  )
  ```
</Accordion>

## Step 4: Verify Payment

<Verify_Payment_Tabs />

## Refund Processing

Refund processing is asynchronous in nature: the create-refund response is an acknowledgement/initial outcome, while the merchant must track the refund to a final state using the applicable PayU refund-status operation or configured notification mechanism. 

<Callout icon="📘" theme="warn">
  ### Reference

  For cancelling or refunding a successful payment transaction, refer to [Refunds.](https://docs.payu.in/docs/introduction-refunds) 
</Callout>

<br />

<br />
