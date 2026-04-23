---
name: Rewards_Fetch_All_Balance
---
## Step 1: Fetch All Balance

Use the Fetch All Balance API to retrieve reward point balances from multiple specified loyalty providers and determine how much users can save using their points.
Use the Fetch All Balance API to retrieve reward point balances from multiple specified loyalty providers and determine how much users can save using their points.

<Accordion title="Request parameters" icon="fa-table">
  # Loyalty API Parameters

  | Parameter                         | Description                                                                                                               | Example              |
  | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------- |
  | loyaltyProviders<br />`mandatory` | `Array` Array of loyalty provider names to fetch rewards from                                                             | \["TWID", "ZILLION"] |
  | mobileNumber<br />`mandatory`     | `Number` User's mobile number (masked for privacy)                                                                        | 88001085\*\*         |
  | orderAmount<br />`mandatory`      | `Number` Order amount for which reward points are applicable                                                              | 1000                 |
  | merchantTxnId<br />`optional`     | `String` Merchant-generated transaction reference identifier for tracking the balance lookup against the order.           | 123merchantTxnId     |
  | fetchRevisedEarn<br />`optional`  | `Boolean` When set to `true`, the response includes the revised earn configuration (`revisedEarnConfig`) for each reward. | true                 |
</Accordion>

<Accordion title="Sample request for combined for both TWID & Zillion" icon="fa-code">
  ```curl
  curl -X POST "https://apitest.payu.in/loyalty-points/v1/balance/all" \
    -H "Content-Type: application/json" \
    -H "mid: YOUR_MERCHANT_ID" \
    -d '{
      "loyaltyProviders": ["TWID", "ZILLION"],
      "merchantTxnId": "123merchantTxnId",
      "mobileNumber": 8800108522,
      "fetchRevisedEarn": true,
      "orderAmount": 1000
    }'
  ```
  ```python
  import requests
  import json

  url = "https://apitest.payu.in/loyalty-points/v1/balance/all"

  headers = {
    "Content-Type": "application/json",
    "mid": "YOUR_MERCHANT_ID"
  }

  payload = {
    "loyaltyProviders": ["TWID", "ZILLION"],
    "merchantTxnId": "123merchantTxnId",
    "mobileNumber": 8800108522,
    "fetchRevisedEarn": True,
    "orderAmount": 1000
  }

  response = requests.post(url, headers=headers, json=payload)
  print("Status Code:", response.status_code)
  print("Response:", response.text)
  ```
  ```csharp
  using System;
  using System.Net.Http;
  using System.Text;
  using System.Text.Json;
  using System.Threading.Tasks;

  class Program
  {
      static async Task Main(string[] args)
      {
          var client = new HttpClient();
          var url = "https://apitest.payu.in/loyalty-points/v1/balance/all";
          
          client.DefaultRequestHeaders.Add("Content-Type", "application/json");
          client.DefaultRequestHeaders.Add("mid", "YOUR_MERCHANT_ID");

          var json = new
          {
              loyaltyProviders = new[] { "TWID", "ZILLION" },
              merchantTxnId = "123merchantTxnId",
              mobileNumber = 8800108522L,
              fetchRevisedEarn = true,
              orderAmount = 1000
          };
          var jsonString = JsonSerializer.Serialize(json);
          var content = new StringContent(jsonString, Encoding.UTF8, "application/json");
          
          var response = await client.PostAsync(url, content);
          var responseBody = await response.Content.ReadAsStringAsync();
          
          Console.WriteLine($"Status Code: {(int)response.StatusCode}");
          Console.WriteLine($"Response: {responseBody}");
      }
  }
  ```
  ```javascript
  const url = "https://apitest.payu.in/loyalty-points/v1/balance/all";

  const headers = {
    "Content-Type": "application/json",
    "mid": "YOUR_MERCHANT_ID"
  };

  const payload = {
    "loyaltyProviders": ["TWID", "ZILLION"],
    "merchantTxnId": "123merchantTxnId",
    "mobileNumber": 8800108522,
    "fetchRevisedEarn": true,
    "orderAmount": 1000
  };

  async function makeRequest() {
      try {
          const response = await fetch(url, {
              method: "POST",
              headers: headers,
              body: JSON.stringify(payload)
          });
          
          const data = await response.text();
          console.log("Status Code:", response.status);
          console.log("Response:", data);
      } catch (error) {
          console.error("Error:", error);
      }
  }

  makeRequest();
  ```
  ```java
  import java.io.*;
  import java.net.HttpURLConnection;
  import java.net.URL;
  import java.nio.charset.StandardCharsets;
  import com.google.gson.Gson;
  import java.util.Arrays;
  import java.util.List;

  public class ApiRequest {
      public static void main(String[] args) throws Exception {
          URL url = new URL("https://apitest.payu.in/loyalty-points/v1/balance/all");
          HttpURLConnection conn = (HttpURLConnection) url.openConnection();
          conn.setRequestMethod("POST");
          conn.setDoOutput(true);
          
          conn.setRequestProperty("Content-Type", "application/json");
          conn.setRequestProperty("mid", "YOUR_MERCHANT_ID");

          Gson gson = new Gson();
          String jsonInputString = "{\"loyaltyProviders\":[\"TWID\",\"ZILLION\"],\"merchantTxnId\":\"123merchantTxnId\",\"mobileNumber\":8800108522,\"fetchRevisedEarn\":true,\"orderAmount\":1000}";
          
          try (OutputStream os = conn.getOutputStream()) {
              byte[] input = jsonInputString.getBytes(StandardCharsets.UTF_8);
              os.write(input, 0, input.length);
          }
          
          int responseCode = conn.getResponseCode();
          System.out.println("Status Code: " + responseCode);
          
          try (BufferedReader br = new BufferedReader(
                  new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
              StringBuilder response = new StringBuilder();
              String responseLine;
              while ((responseLine = br.readLine()) != null) {
                  response.append(responseLine.trim());
              }
              System.out.println("Response: " + response.toString());
          }
      }
  }
  ```
  ```php
  <?php

  $url = "https://apitest.payu.in/loyalty-points/v1/balance/all";

  $headers = [
    "Content-Type" => "application/json",
    "mid" => "YOUR_MERCHANT_ID"
  ];

  $payload = [
    "loyaltyProviders" => ["TWID", "ZILLION"],
    "merchantTxnId" => "123merchantTxnId",
    "mobileNumber" => 8800108522,
    "fetchRevisedEarn" => true,
    "orderAmount" => 1000
  ];

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
  curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
  curl_setopt($ch, CURLOPT_HTTPHEADER, array_map(function($key, $value) {
      return "$key: $value";
  }, array_keys($headers), $headers));

  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  curl_close($ch);

  echo "Status Code: " . $httpCode . "\n";
  echo "Response: " . $response . "\n";
  ?>
  ```
</Accordion>

<Accordion title="Sample response for combined" icon="fa-file-code">
  ```json
  {
    "data": [
      {
        "loyaltyProvider": "TWID",
        "usableAmount": 500.0,
        "usablePoints": 500,
        "userStatus": null,
        "title": "Save Rs 500 using 500 twid Cash Points",
        "availablePoints": null,
        "earnConfig": {
          "points": 0,
          "amount": null,
          "title": null
        },
        "revisedEarnConfig": null,
        "rewardId": 270943,
        "issuerDetailDTO": {
          "brandName": "twid Cash",
          "logo": "https://cdn.twidpay.com/co/brand_images/brand_image_14b20_1651155946.png",
          "issuerType": "brand"
        },
        "holdApplicable": false,
        "rewards": [
          {
            "loyaltyProvider": "TWID",
            "usableAmount": 250.0,
            "usablePoints": 1000,
            "userStatus": null,
            "title": "Save Rs 250 using 1000 Woodland Points",
            "availablePoints": null,
            "earnConfig": {
              "points": 50,
              "amount": null,
              "title": "Earn 50 Woodland Points"
            },
            "revisedEarnConfig": null,
            "rewardId": 270940,
            "issuerDetailDTO": {
              "brandName": "Woodland",
              "logo": "https://cdn.twidpay.com/co/s2s_issuer_images/Woodland.jpg",
              "issuerType": "brand"
            },
            "holdApplicable": false,
            "rewards": null
          },
          {
            "loyaltyProvider": "TWID",
            "usableAmount": 125.0,
            "usablePoints": 125,
            "userStatus": null,
            "title": "Save Rs 125 using 125 HDFC Bank Points",
            "availablePoints": null,
            "earnConfig": {
              "points": 0,
              "amount": null,
              "title": null
            },
            "revisedEarnConfig": null,
            "rewardId": 270942,
            "issuerDetailDTO": {
              "brandName": "HDFC Bank",
              "logo": "https://cdn.twidpay.com/co/s2s_issuer_images/hdfc_square.svg",
              "issuerType": "bank"
            },
            "holdApplicable": false,
            "rewards": null,
            "applicableBinList": [
              "531849",
              "536303",
              "524167"
            ]
          }
        ]
      },
      {
        "customErrorMessage": "Unable to process request for provider",
        "loyaltyProvider": "ZILLION",
        "usableAmount": null,
        "usablePoints": null,
        "userStatus": null
      }
    ]
  }
  ```
</Accordion>




> 📘 Note:
>
> The `issuerDetailDTO.brandName` returned in the Fetch Balance response (for example, `"Woodland"`, `"HDFC Bank"`) is the value you must pass as `rewardName` in the `childPaymentInstruments` / `earnPaymentInstruments` array of the `_payment` request when the reward provider is **TWID**. The `rewardName` field is **not applicable for Zillion**.
