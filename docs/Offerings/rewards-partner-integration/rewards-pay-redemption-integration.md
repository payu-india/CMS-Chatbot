---
title: Rewards Pay Redemption Integration
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
---
title: Rewards Pay Redemption Integration
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
---
title: Twid Seamless Card Transaction Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  robots: index
---

Integrate TWID or Zillion rewards  to enable customers to redeem their TWID or Zillon loyalty points during checkout. Follow these sequential steps to implement a complete TWID or Zillion rewards integration.

This section describes the complete integration workflow for TWID Rewards Seamless Transactions. This integration involves the following steps:

<Cards columns={3}>
  <Card title="1. Fetch All Balance" href="#step-1-fetch-all-balance">
    Call loyalty-service to get usable reward balances for the customer before initiating payment
  </Card>

  <Card title="2. Initiate Payment with PayU" href="#step-2-initiate-payment-with-payu">
    Prepare PayU payment POST with SPLITPAY, TWIDX, splitInfo parameters and generate the required hash
  </Card>

  <Card title="3. Redirect the Customer" href="#step-3-redirect-the-customer">
    Use acsTemplate to post authentication response to merchant termUrl with bankData fields
  </Card>

  <Card title="4. Authorize (charge) the payment" href="#step-4-authorize-charge-the-payment">
    Make merchant S2S POST of authentication\_info to PayU AuthorizeTransaction endpoint
  </Card>

  <Card title="5. Check Response from PayU" href="#step-5-check-response-from-payu">
    Parse postback response and validate reverse hash from PayU
  </Card>

  <Card title="6. Verify the Payment" href="#step-6-verify-the-payment">
    Perform final verification step to confirm transaction completion
  </Card>
</Cards>

## Step 1: Fetch All Balance

Use the Fetch All Balance API to retrieve reward point balances from multiple specified loyalty providers and determine how much users can save using their points.
Use the Fetch All Balance API to retrieve reward point balances from multiple specified loyalty providers and determine how much users can save using their points.

<Accordion title="Request parameters" icon="fa-table">
  <HTMLBlock>{`
                                <style>
                                /* Target only the second column in the table */
                                .markdown-body table td:nth-child(2) {
                                  word-break: break-word !important;
                                }

                                /* Keep the first column from breaking unnecessarily */
                                .markdown-body table td:nth-child(1) {
                                  word-break: normal;
                                  white-space: nowrap;
                                }
                                </style>
                                <Table align={["left","left","left"]}>
                                  <thead>
                                    <tr>
                                      <th style={{ textAlign: "left" }}>
                                        Parameter
                                      </th>
                                      <th style={{ textAlign: "left" }}>
                                        Description
                                      </th>
                                      <th style={{ textAlign: "left" }}>
                                        Example
                                      </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    <tr>
                                      <td style={{ textAlign: "left" }}>
                                        loyaltyProviders <br/>
                                        <code>mandatory</code>
                                      </td>
                                      <td style={{ textAlign: "left" }}>
                                        <code>Array</code> Array of loyalty provider names to fetch rewards from
                                      </td>
                                      <td style={{ textAlign: "left" }}>
                                        ["TWID", "ZILLION"]
                                      </td>
                                    </tr>
                                    <tr>
                                      <td style={{ textAlign: "left" }}>
                                        mobileNumber <br/>
                                        <code>mandatory</code>
                                      </td>
                                      <td style={{ textAlign: "left" }}>
                                        <code>Number</code> User's mobile number (masked for privacy)
                                      </td>
                                      <td style={{ textAlign: "left" }}>
                                        88001085**
                                      </td>
                                    </tr>
                                    <tr>
                                      <td style={{ textAlign: "left" }}>
                                        orderAmount <br/>
                                        <code>mandatory</code>
                                      </td>
                                      <td style={{ textAlign: "left" }}>
                                        <code>Number</code> Order amount for which reward points are applicable
                                      </td>
                                      <td style={{ textAlign: "left" }}>
                                        1000
                                      </td>
                                    </tr>
                                    <tr>
                                      <td style={{ textAlign: "left" }}>
                                        merchantTxnId <br/>
                                        <code>optional</code>
                                      </td>
                                      <td style={{ textAlign: "left" }}>
                                        <code>String</code> Merchant-generated transaction reference identifier for tracking the balance lookup against the order.
                                      </td>
                                      <td style={{ textAlign: "left" }}>
                                        123merchantTxnId
                                      </td>
                                    </tr>
                                    <tr>
                                      <td style={{ textAlign: "left" }}>
                                        fetchRevisedEarn <br/>
                                        <code>optional</code>
                                      </td>
                                      <td style={{ textAlign: "left" }}>
                                        <code>Boolean</code> When set to <code>true</code>, the response includes the revised earn configuration (<code>revisedEarnConfig</code>) for each reward.
                                      </td>
                                      <td style={{ textAlign: "left" }}>
                                        true
                                      </td>
                                    </tr>
                                  </tbody>
                                </Table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
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

<Accordion title="Sample response" icon="fa-file-code">
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

## Step 2: Initiate Payment with PayU

<Accordion title="Request parameters" icon="fa-table">
  | Parameter                             | Description                                                                                                                                                                                                                                                                                        | Example                                                                                            |   |
  | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | - |
  | key<br />`mandatory`                  | `String` Merchant key provided by PayU during onboarding.                                                                                                                                                                                                                                          |                                                                                                    |   |
  | txnid<br />`mandatory`                | `String` The transaction ID is a reference number for a specific order that is generated by the merchant.                                                                                                                                                                                          |                                                                                                    |   |
  | amount<br />`mandatory`               | `String` The payment amount for the transaction.                                                                                                                                                                                                                                                   |                                                                                                    |   |
  | productinfo<br />`mandatory`          | `String` A brief description of the product.                                                                                                                                                                                                                                                       |                                                                                                    |   |
  | firstname<br />`mandatory`            | `String` The first name of the customer.                                                                                                                                                                                                                                                           | Ashish                                                                                             |   |
  | email<br />`mandatory`                | `String` The email address of the customer.                                                                                                                                                                                                                                                        |                                                                                                    |   |
  | phone<br />`mandatory`                | `String` The phone number of the customer.                                                                                                                                                                                                                                                         |                                                                                                    |   |
  | pg<br />`mandatory`                   | `String` The pg parameter must contain `SPLITPAY` for Rewards transactions.                                                                                                                                                                                                                        | SPLITPAY                                                                                           |   |
  | bankcode<br />`mandatory`             | `String` The bankcode parameter identifies the reward provider used at the parent transaction level. Use `TWIDX` for **TWID** Rewards or `ZRD` for **Zillion** Rewards. For more information, refer to [Reward Provider Codes](#reward-provider-codes).                                            | TWIDX                                                                                              |   |
  | splitInfo                             | `JSON` This parameter must contain the TWID split information. For more information, refer to [splitInfo JSON Object Fields Description](#splitinfo-json-object-fields-description). The sample JSON for Spend/Burn or Earn Points with payment methods: <br />-[Cards](#cards) <br />-[UPI](#upi) | Refer to to [splitInfo JSON Object Fields Description](#splitinfo-json-object-fields-description). |   |
  | furl<br />`mandatory`                 | `String` The success URL, which is the page PayU will redirect to if the transaction is successful.                                                                                                                                                                                                |                                                                                                    |   |
  | surl<br />`mandatory`                 | `String` The Failure URL, which is the page PayU will redirect to if the transaction is failed.                                                                                                                                                                                                    |                                                                                                    |   |
  | hash<br />`mandatory`                 | `String` It is the hash calculated by the merchant. The hash calculation logic is: \`sha512(key\\\|txnid\\\|amount\\\|productinfo\\\|firstname\\\|email\\\|udf1\\\|udf2\\\|udf3\\\|udf4\\\|udf5\\\|\\\|\\\|\\\|\\\|                                                                                | SALT)\`                                                                                            |   |
  | txn\_s2s\_flow<br />`mandatory`       | `String` This parameter must be passed with the value as **4** for Legacy Decoupled flow.                                                                                                                                                                                                          | 4                                                                                                  |   |
  | auth\_only<br />`mandatory`           | `String` This parameter must be passed with the value as **1** for this parameter.                                                                                                                                                                                                                 | 1                                                                                                  |   |
  | termUrl<br />`mandatory`              | `String` This parameter must contain the URL which will receive the authentication response from ACS.                                                                                                                                                                                              |                                                                                                    |   |
  | authentication\_flow<br />`mandatory` | `String` This parameter must be passed with value as REDIRECT.                                                                                                                                                                                                                                     | REDIRECT                                                                                           |   |
  | s2s\_client\_ip<br />`mandatory`      | `String` This parameter must have the source IP of the customer.                                                                                                                                                                                                                                   |                                                                                                    |   |
  | s2s\_device\_info<br />`mandatory`    | `String` This parameter must have the customer agent's device.                                                                                                                                                                                                                                     |                                                                                                    |   |
  | notifyurl<br />`optional`             | `String` It is used to send response regarding current transaction to notify about the current transaction done in merchant site.                                                                                                                                                                  |                                                                                                    |   |
  | address1<br />`optional`              | `String` The first line of the billing address. **For Fraud Detection**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.                                                                     |                                                                                                    |   |
  | address2<br />`optional`              | `String` The second line of the billing address.                                                                                                                                                                                                                                                   |                                                                                                    |   |
  | city<br />`optional`                  | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                      |                                                                                                    |   |
  | state<br />`optional`                 | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                     |                                                                                                    |   |
  | country<br />`optional`               | `String` The country where your customer resides.                                                                                                                                                                                                                                                  |                                                                                                    |   |
  | zipcode<br />`optional`               | `String` Billing address zip code is mandatory for the cardless EMI option. `Character Limit`-20                                                                                                                                                                                                   |                                                                                                    |   |
  | udf1<br />`optional`                  | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.                                                                                                |                                                                                                    |   |
  | udf2<br />`optional`                  | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.                                                                                                |                                                                                                    |   |
  | udf3<br />`optional`                  | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.                                                                                                                                                                                    |                                                                                                    |   |
  | udf4<br />`optional`                  | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.                                                                                                                                                                                    |                                                                                                    |   |
  | udf5<br />`optional`                  | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.                                                                                                                                                                                    |                                                                                                    |   |

  <Accordion title="Understanding Hashing and sample code" icon="fa-code">
    <HashingRequestParameters />

    #### Hashing Sample Code

    <HashingSample />
  </Accordion>
</Accordion>

### Reward Provider Codes

Use the following bankcode values to identify the reward provider in both the top-level `_payment` request and inside the `splitInfo.childPaymentInstruments` / `earnPaymentInstruments` arrays:

| Reward Provider | Top-level `bankcode` (parent) | Reward instrument `bankCode` (child, RD) |
| --------------- | ----------------------------- | ---------------------------------------- |
| **TWID**        | `TWIDX`                       | `TWIDLS`                                 |
| **Zillion**     | `ZRD`                         | `ZLS`                                    |

> 📘 Note:
>
> The `bankcode` (parent) signals the reward provider being used for the transaction, while the `bankCode` inside the `RD` instrument inside `splitInfo` is the child code that PayU uses to settle the reward leg of the split payment.

### splitInfo JSON Object Fields Description

> 📘 Important:
>
> A complete payment cannot be settled by Rewards (TWID or Zillion) alone — Rewards must always be combined with a **Card** or **UPI** instrument inside `childPaymentInstruments`. The sum of `transactionAmount` across all child instruments must equal the order `amount`.
>
> **Earn** is supported for both **TWID and Zillion**. Pass the reward instrument inside `earnPaymentInstruments` (with `transactionAmount: "0"`) when the customer is paying via Card/UPI and accruing reward points on that transaction.

#### Cards

<Accordion title="Sample request for Burn Points with Card (Zillion)" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -d '{
      "key": "KOEfPI",
      "txnid": "ram1234",
      "productinfo": "Product Info",
      "amount": "100",
      "email": "test@example.com",
      "firstname": "Payu-Admin",
      "lastname": "",
      "phone": "880**08522",
      "surl": "https://pp56admin.payu.in/test_response",
      "furl": "https://pp56admin.payu.in/test_response",
      "pg": "SPLITPAY",
      "bankcode": "ZRD",
      "txn_s2s_flow": "4",
      "splitInfo": {
        "childPaymentInstruments": [
          {
            "name": "CC",
            "bankCode": "CC",
            "cardNumber": "5123456789012346",
            "cvv": "345",
            "validThrough": "07/25",
            "ownerName": "Payu",
            "transactionAmount": "99"
          },
          {
            "name": "RD",
            "bankCode": "ZLS",
            "transactionAmount": "1"
          }
        ]
      },
      "hash": "3842a54c294792e9c8c37c7eba8d9693a85517cb7a47aea33a0368a8f6b337e8343f5ef4f726af206ef68549b542ff75dc66fb3b8e8fd5786733131a74cbe741"
    }'
  ```
</Accordion>

<Accordion title="Sample request for Burn Points with Card (TWID)" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -d '{
      "key": "KOEfPI",
      "txnid": "ram1234",
      "productinfo": "Product Info",
      "amount": "100",
      "email": "test@example.com",
      "firstname": "Payu-Admin",
      "lastname": "",
      "phone": "880**08522",
      "surl": "https://pp56admin.payu.in/test_response",
      "furl": "https://pp56admin.payu.in/test_response",
      "pg": "SPLITPAY",
      "bankcode": "TWIDX",
      "txn_s2s_flow": "4",
      "splitInfo": {
        "childPaymentInstruments": [
          {
            "name": "CC",
            "bankCode": "CC",
            "cardNumber": "5123456789012346",
            "cvv": "345",
            "validThrough": "07/25",
            "ownerName": "Payu",
            "transactionAmount": "412"
          },
          {
            "name": "RD",
            "bankCode": "TWIDLS",
            "transactionAmount": "100",
            "rewardId": 269434,
            "cardBin": "512345",
            "cardLastFour": "2346"
          }
        ]
      },
      "hash": "3842a54c294792e9c8c37c7eba8d9693a85517cb7a47aea33a0368a8f6b337e8343f5ef4f726af206ef68549b542ff75dc66fb3b8e8fd5786733131a74cbe741"
    }'
  ```
</Accordion>

<Accordion title="Sample request for Earn Points with Card (TWID)" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -d '{
      "key": "KOEfPI",
      "txnid": "ram1234",
      "productinfo": "Product Info",
      "amount": "1000",
      "email": "test@example.com",
      "firstname": "Payu-Admin",
      "lastname": "",
      "phone": "9304204920",
      "surl": "https://pp1admin.payu.in/test_response",
      "furl": "https://pp1admin.payu.in/test_response",
      "pg": "SPLITPAY",
      "bankcode": "TWIDX",
      "txn_s2s_flow": "4",
      "splitInfo": {
        "childPaymentInstruments": [
          {
            "bankCode": "CC",
            "name": "CC",
            "cardNumber": "5123456789012346",
            "cvv": "345",
            "validThrough": "12/26",
            "ownerName": "Payu",
            "transactionAmount": "1000.00"
          }
        ],
        "earnPaymentInstruments": [
          {
            "name": "RD",
            "bankCode": "TWIDLS",
            "transactionAmount": "0",
            "rewardId": 270940,
            "rewardName": "Woodland",
            "cardBin": "524216",
            "cardLastFour": "0009"
          }
        ],
        "totalAmount": "1000.00",
        "consent": false
      },
      "hash": "e0241876845d20e42336426cf135651d5241503b51e525dffd17f88d1e694f7718a89e33cec6f21971097faad7dca5442910498c298de249b23ea3b12a75ed0c"
    }'
  ```
</Accordion>

<Accordion title="Sample request for Earn Points with Card (Zillion)" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -d '{
      "key": "KOEfPI",
      "txnid": "ram1234",
      "productinfo": "Product Info",
      "amount": "1000",
      "email": "test@example.com",
      "firstname": "Payu-Admin",
      "lastname": "",
      "phone": "9304204920",
      "surl": "https://pp1admin.payu.in/test_response",
      "furl": "https://pp1admin.payu.in/test_response",
      "pg": "SPLITPAY",
      "bankcode": "ZRD",
      "txn_s2s_flow": "4",
      "splitInfo": {
        "childPaymentInstruments": [
          {
            "bankCode": "CC",
            "name": "CC",
            "cardNumber": "5123456789012346",
            "cvv": "345",
            "validThrough": "12/26",
            "ownerName": "Payu",
            "transactionAmount": "1000.00"
          }
        ],
        "earnPaymentInstruments": [
          {
            "name": "RD",
            "bankCode": "ZLS",
            "transactionAmount": "0",
            "rewardId": 270940
          }
        ],
        "totalAmount": "1000.00",
        "consent": false
      },
      "hash": "e0241876845d20e42336426cf135651d5241503b51e525dffd17f88d1e694f7718a89e33cec6f21971097faad7dca5442910498c298de249b23ea3b12a75ed0c"
    }'
  ```
</Accordion>

<Accordion title="Sample JSON for Spend Points along with Card (Partly)" icon="fa-code">
  ```JSON
  "splitInfo": {
  "childPaymentInstruments": [
    {
      "name": "CC",
      "bankCode": "CC",
      "cardNumber": "4808550000000000",
      "cvv": "855",
      "validThrough": "05/26",
      "ownerName": "Payu",
      "transactionAmount": "992"
    },
    {
      "name": "RD",
      "bankCode": "TWIDLS",
      "transactionAmount": "8",
      "rewardId": 271508,
      "rewardName": "Zillion",
      "cardBin": "000000",
      "cardLastFour": "0000"
    }
  ],
  "earnPaymentInstruments": [],
  "totalAmount": "1000.00",
  "consent": false
  }
  ```
</Accordion>

<Accordion title="Sample JSON for Earn Points with Card" icon="fa-code">
  ```json
  {
      "childPaymentInstruments": [
          {
              "bankCode": "CC",
              "name": "CC",
              "cardNumber": "5123456789012346",
              "cvv": "345",
              "validThrough": "12/26",
              "ownerName": "Payu",
              "transactionAmount": "1000.00"
          }
      ],
      "earnPaymentInstruments": [
          {
              "name": "RD",
              "bankCode": "TWIDLS",
              "transactionAmount": "0",
              "rewardId": 270940,
              "rewardName": "Woodland",
              "cardBin": "524216",
              "cardLastFour": "0009"
          }
      ],
      "totalAmount": "1000.00",
      "consent": false
  }
  ```
</Accordion>

#### UPI

<Accordion title="Sample request for Burn Points with UPI (Zillion)" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -d '{
      "key": "KOEfPI",
      "txnid": "ram1234",
      "productinfo": "Product Info",
      "amount": "100",
      "email": "test@example.com",
      "firstname": "Payu-Admin",
      "lastname": "",
      "phone": "9999999999",
      "surl": "https://pp56admin.payu.in/test_response",
      "furl": "https://pp56admin.payu.in/test_response",
      "pg": "SPLITPAY",
      "bankcode": "ZRD",
      "txn_s2s_flow": "4",
      "splitInfo": {
        "childPaymentInstruments": [
          {
            "name": "UPI",
            "bankCode": "UPI",
            "vpa": "kk@okaxis",
            "transactionAmount": "99"
          },
          {
            "name": "RD",
            "bankCode": "ZLS",
            "transactionAmount": "1"
          }
        ]
      },
      "hash": "3842a54c294792e9c8c37c7eba8d9693a85517cb7a47aea33a0368a8f6b337e8343f5ef4f726af206ef68549b542ff75dc66fb3b8e8fd5786733131a74cbe741"
    }'
  ```
</Accordion>

<Accordion title="Sample request for Burn Points with UPI (TWID)" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -d '{
      "key": "KOEfPI",
      "txnid": "ram1234",
      "productinfo": "Product Info",
      "amount": "100",
      "email": "test@example.com",
      "firstname": "Payu-Admin",
      "lastname": "",
      "phone": "9999999999",
      "surl": "https://pp56admin.payu.in/test_response",
      "furl": "https://pp56admin.payu.in/test_response",
      "pg": "SPLITPAY",
      "bankcode": "TWIDX",
      "txn_s2s_flow": "4",
      "splitInfo": {
        "childPaymentInstruments": [
          {
            "name": "UPI",
            "bankCode": "UPI",
            "vpa": "kk@okaxis",
            "transactionAmount": "412"
          },
          {
            "name": "RD",
            "bankCode": "TWIDLS",
            "transactionAmount": "100",
            "rewardId": 269434,
            "cardBin": "512345",
            "cardLastFour": "2346"
          }
        ]
      },
      "hash": "3842a54c294792e9c8c37c7eba8d9693a85517cb7a47aea33a0368a8f6b337e8343f5ef4f726af206ef68549b542ff75dc66fb3b8e8fd5786733131a74cbe741"
    }'
  ```
</Accordion>

<Accordion title="Sample request for Earn Points with UPI (TWID)" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -d '{
      "key": "KOEfPI",
      "txnid": "ram1234",
      "productinfo": "Product Info",
      "amount": "1000",
      "email": "test@example.com",
      "firstname": "Payu-Admin",
      "lastname": "",
      "phone": "9304204920",
      "surl": "https://pp1admin.payu.in/test_response",
      "furl": "https://pp1admin.payu.in/test_response",
      "pg": "SPLITPAY",
      "bankcode": "TWIDX",
      "txn_s2s_flow": "4",
      "splitInfo": {
        "childPaymentInstruments": [
          {
            "name": "UPI",
            "bankCode": "UPI",
            "vpa": "kk@okaxis",
            "transactionAmount": "1000"
          }
        ],
        "earnPaymentInstruments": [
          {
            "name": "RD",
            "bankCode": "TWIDLS",
            "transactionAmount": "0",
            "rewardId": 270940,
            "rewardName": "Woodland"
          }
        ],
        "totalAmount": "1000.00",
        "consent": false
      },
      "hash": "f158a418e38993aa4d1d72d056ebf08047d77a8a14f219ef619f6612e9a6ff8f6147ad035c97c012b74f15ebd08eaea423dd7438654f91d7aca1f10d4f406800"
    }'
  ```
</Accordion>

<Accordion title="Sample request for Earn Points with UPI (Zillion)" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -d '{
      "key": "KOEfPI",
      "txnid": "ram1234",
      "productinfo": "Product Info",
      "amount": "1000",
      "email": "test@example.com",
      "firstname": "Payu-Admin",
      "lastname": "",
      "phone": "9304204920",
      "surl": "https://pp1admin.payu.in/test_response",
      "furl": "https://pp1admin.payu.in/test_response",
      "pg": "SPLITPAY",
      "bankcode": "ZRD",
      "txn_s2s_flow": "4",
      "splitInfo": {
        "childPaymentInstruments": [
          {
            "name": "UPI",
            "bankCode": "UPI",
            "vpa": "kk@okaxis",
            "transactionAmount": "1000"
          }
        ],
        "earnPaymentInstruments": [
          {
            "name": "RD",
            "bankCode": "ZLS",
            "transactionAmount": "0",
            "rewardId": 270940
          }
        ],
        "totalAmount": "1000.00",
        "consent": false
      },
      "hash": "f158a418e38993aa4d1d72d056ebf08047d77a8a14f219ef619f6612e9a6ff8f6147ad035c97c012b74f15ebd08eaea423dd7438654f91d7aca1f10d4f406800"
    }'
  ```
</Accordion>

<Accordion title="Sample JSON for Spend Points along with UPI" icon="fa-code">
  ```json
  {
    "childPaymentInstruments": [
      {
        "name": "UPI",
        "bankCode": "UPI",
        "vpa": "kk@okaxis",
        "transactionAmount": "995"
      },
      {
        "name": "RD",
        "bankCode": "TWIDLS",
        "rewardId": 271508,
        "rewardName": "Zillion",
        "transactionAmount": "5"
      }
    ],
    "earnPaymentInstruments": [],
    "totalAmount": "1000.00",
    "consent": false
  }
  ```
</Accordion>

<Accordion title="Sample JSON for Earn Points with UPI (Partly)" icon="fa-code">
  ```json
  {
    "childPaymentInstruments": [
      {
        "name": "UPI",
        "bankCode": "UPI",
        "vpa": "kk@okaxis",
        "transactionAmount": "1000"
      }
    ],
    "earnPaymentInstruments": [
      {
        "name": "RD",
        "bankCode": "TWIDLS",
        "transactionAmount": "0",
        "rewardId": 270940,
        "rewardName": "Woodland"
      }
    ],
    "totalAmount": "1000.00",
    "consent": false
  }
  ```
</Accordion>

#### Field Descriptions

<Accordion title="Field Descriptions in childPaymentInstruments" icon="fa-table">
  | Field                                    | Description                                                                                                                                                                                                                | Example          |
  | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
  | name                                     | The name of the payment method. Use any of the following as required:<br />**CC** for Cards<br />**RD** for Rewards (TWID or Zillion)<br />**UPI** for UPI                                                                 | CC               |
  | bankCode                                 | The bank code identifier for the payment instrument. Use `CC` for Cards, `UPI` for UPI, `TWIDLS` for **TWID** Rewards or `ZLS` for **Zillion** Rewards.                                                                    | CC               |
  | cardNumber<br /> `mandatory for cards`   | The credit/debit card number for the transaction.                                                                                                                                                                          | 5123456789012346 |
  | cvv<br /> `mandatory for cards`          | The Card Verification Value (CVV) for card validation.                                                                                                                                                                     | 345              |
  | validThrough<br /> `mandatory for cards` | The card expiry date in MM/YY format.                                                                                                                                                                                      | 07/25            |
  | ownerName                                | The name of the card holder or account owner.                                                                                                                                                                              | Payu             |
  | vpa<br /> `mandatory for UPI`            | The Virtual Payment Address (VPA) used for the UPI transaction.                                                                                                                                                            | kk@okaxis        |
  | rewardId<br /> `mandatory for TWID`      | The unique reward identifier returned in the `rewardId` field of the Fetch Balance response.                                                                                                                               | 271508           |
  | rewardName<br /> `mandatory for TWID`    | `String` Brand name of the reward program. Pass the value received as `issuerDetailDTO.brandName` in the Fetch Balance response (for example, `Woodland`, `HDFC Bank`). **Mandatory for TWID, not applicable for Zillion.** | Woodland         |
  | cardBin<br /> `mandatory for TWID`       | The TWID Rewards card BIN (first 6 digits of the underlying card).                                                                                                                                                         | 524216           |
  | cardLastFour<br /> `mandatory for TWID`  | The last four digits of the TWID Rewards card.                                                                                                                                                                             | 0009             |
  | transactionAmount                        | The amount to be processed in the transaction for the given payment instrument.                                                                                                                                            | 512              |
</Accordion>

<Accordion title="Field Descriptions in earnPaymentInstruments" icon="fa-table">
  Use the `earnPaymentInstruments` array when the customer is paying via Card or UPI and accruing reward points on the same transaction. Earn is supported for both **TWID** and **Zillion**.

  | Field                                   | Description                                                                                                                                                                                                                | Example  |
  | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
  | name                                    | The name of the payment instrument. Use **RD** for the reward instrument.                                                                                                                                                  | RD       |
  | bankCode                                | The bank code identifier for the reward instrument. Use `TWIDLS` for **TWID** Rewards or `ZLS` for **Zillion** Rewards.                                                                                                    | TWIDLS   |
  | transactionAmount                       | The amount processed against the reward instrument. For Earn requests this is typically `"0"`, since reward points are accrued (not redeemed).                                                                             | 0        |
  | rewardId<br /> `mandatory for TWID`     | The unique reward identifier returned in the `rewardId` field of the Fetch Balance response.                                                                                                                               | 270940   |
  | rewardName<br /> `mandatory for TWID`   | `String` Brand name of the reward program. Pass the value received as `issuerDetailDTO.brandName` in the Fetch Balance response (for example, `Woodland`, `HDFC Bank`). **Mandatory for TWID, not applicable for Zillion.** | Woodland |
  | cardBin<br /> `mandatory for TWID`      | The TWID Rewards card BIN (first 6 digits of the underlying card).                                                                                                                                                         | 524216   |
  | cardLastFour<br /> `mandatory for TWID` | The last four digits of the TWID Rewards card.                                                                                                                                                                             | 0009     |
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment" \
    -H "Content-Type: application/json" \
    -d '{
      "key": "KOEfPI",
      "txnid": "ram1234",
      "productinfo": "Product Info",
      "amount": "100",
      "email": "test@example.com",
      "firstname": "Payu-Admin",
      "lastname": "",
      "phone": "880**08522",
      "surl": "https://pp56admin.payu.in/test_response",
      "furl": "https://pp56admin.payu.in/test_response",
      "pg": "SPLITPAY",
      "bankcode": "TWIDX",
      "txn_s2s_flow": "4",
      "splitInfo": {
          "childPaymentInstruments": [
              {
                  "name": "CC",
                  "bankCode": "CC",
                  "cardNumber": "5123456789012346",
                  "cvv": "345",
                  "validThrough": "07/25",
                  "ownerName": "Payu",
                  "transactionAmount": "512"
              }
          ],
          "earnPaymentInstruments": [
              {
                  "name": "RD",
                  "bankCode": "TWIDLS",
                  "transactionAmount": "0",
                  "rewardId": 269431,
                  "cardBin": "480855",
                  "cardLastFour": "0000"
              }
          ]
      },
      "hash": "3842a54c294792e9c8c37c7eba8d9693a85517cb7a47aea33a0368a8f6b337e8343f5ef4f726af206ef68549b542ff75dc66fb3b8e8fd5786733131a74cbe741"
  }'
  ```
  ```python
  import requests
  import json

  url = "https://test.payu.in/_payment"

  data = {
      "key": "KOEfPI",
      "txnid": "ram1234",
      "productinfo": "Product Info",
      "amount": "100",
      "email": "test@example.com",
      "firstname": "Payu-Admin",
      "lastname": "",
      "phone": "880**08522",
      "surl": "https://pp56admin.payu.in/test_response",
      "furl": "https://pp56admin.payu.in/test_response",
      "pg": "SPLITPAY",
      "bankcode": "TWIDX",
      "txn_s2s_flow": "4",
      "splitInfo": {
          "childPaymentInstruments": [
              {
                  "name": "CC",
                  "bankCode": "CC",
                  "cardNumber": "5123456789012346",
                  "cvv": "345",
                  "validThrough": "07/25",
                  "ownerName": "Payu",
                  "transactionAmount": "512"
              }
          ],
          "earnPaymentInstruments": [
              {
                  "name": "RD",
                  "bankCode": "TWIDLS",
                  "transactionAmount": "0",
                  "rewardId": 269431,
                  "cardBin": "480855",
                  "cardLastFour": "0000"
              }
          ]
      },
      "hash": "3842a54c294792e9c8c37c7eba8d9693a85517cb7a47aea33a0368a8f6b337e8343f5ef4f726af206ef68549b542ff75dc66fb3b8e8fd5786733131a74cbe741"
  }

  headers = {
      "Content-Type": "application/json"
  }

  try:
      response = requests.post(url, headers=headers, json=data)
      print(f"Status Code: {response.status_code}")
      print(f"Response: {response.text}")
  except requests.exceptions.RequestException as e:
      print(f"Error: {e}")
  ```
  ```csharp
  using System;
  using System.Net.Http;
  using System.Text;
  using System.Threading.Tasks;
  using Newtonsoft.Json;

  class Program
  {
      static async Task Main(string[] args)
      {
          string url = "https://test.payu.in/_payment";
          
          var data = new
          {
              key = "KOEfPI",
              txnid = "ram1234",
              productinfo = "Product Info",
              amount = "100",
              email = "test@example.com",
              firstname = "Payu-Admin",
              lastname = "",
              phone = "880**08522",
              surl = "https://pp56admin.payu.in/test_response",
              furl = "https://pp56admin.payu.in/test_response",
              pg = "SPLITPAY",
              bankcode = "TWIDX",
              txn_s2s_flow = "4",
              splitInfo = new
              {
                  childPaymentInstruments = new[]
                  {
                      new
                      {
                          name = "CC",
                          bankCode = "CC",
                          cardNumber = "5123456789012346",
                          cvv = "345",
                          validThrough = "07/25",
                          ownerName = "Payu",
                          transactionAmount = "512"
                      }
                  },
                  earnPaymentInstruments = new[]
                  {
                      new
                      {
                          name = "RD",
                          bankCode = "TWIDLS",
                          transactionAmount = "0",
                          rewardId = 269431,
                          cardBin = "480855",
                          cardLastFour = "0000"
                      }
                  }
              },
              hash = "3842a54c294792e9c8c37c7eba8d9693a85517cb7a47aea33a0368a8f6b337e8343f5ef4f726af206ef68549b542ff75dc66fb3b8e8fd5786733131a74cbe741"
          };

          using (var client = new HttpClient())
          {
              try
              {
                  string jsonData = JsonConvert.SerializeObject(data);
                  var content = new StringContent(jsonData, Encoding.UTF8, "application/json");
                  
                  HttpResponseMessage response = await client.PostAsync(url, content);
                  string responseContent = await response.Content.ReadAsStringAsync();
                  
                  Console.WriteLine($"Status Code: {response.StatusCode}");
                  Console.WriteLine($"Response: {responseContent}");
              }
              catch (Exception ex)
              {
                  Console.WriteLine($"Error: {ex.Message}");
              }
          }
      }
  }
  ```

  ```javascript
  async function makePayment() {
      const url = "https://test.payu.in/_payment";
      
      const data = {
          key: "KOEfPI",
          txnid: "ram1234",
          productinfo: "Product Info",
          amount: "100",
          email: "test@example.com",
          firstname: "Payu-Admin",
          lastname: "",
          phone: "880**08522",
          surl: "https://pp56admin.payu.in/test_response",
          furl: "https://pp56admin.payu.in/test_response",
          pg: "SPLITPAY",
          bankcode: "TWIDX",
          txn_s2s_flow: "4",
          splitInfo: {
              childPaymentInstruments: [
                  {
                      name: "CC",
                      bankCode: "CC",
                      cardNumber: "5123456789012346",
                      cvv: "345",
                      validThrough: "07/25",
                      ownerName: "Payu",
                      transactionAmount: "512"
                  }
              ],
              earnPaymentInstruments: [
                  {
                      name: "RD",
                      bankCode: "TWIDLS",
                      transactionAmount: "0",
                      rewardId: 269431,
                      cardBin: "480855",
                      cardLastFour: "0000"
                  }
              ]
          },
          hash: "3842a54c294792e9c8c37c7eba8d9693a85517cb7a47aea33a0368a8f6b337e8343f5ef4f726af206ef68549b542ff75dc66fb3b8e8fd5786733131a74cbe741"
      };

      try {
          const response = await fetch(url, {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json'
              },
              body: JSON.stringify(data)
          });
          
          const responseText = await response.text();
          console.log(`Status Code: ${response.status}`);
          console.log(`Response: ${responseText}`);
      } catch (error) {
          console.log(`Error: ${error.message}`);
      }
  }

  makePayment();
  ```
  ```java
  import java.io.IOException;
  import java.net.URI;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;
  import com.google.gson.Gson;
  import com.google.gson.GsonBuilder;
  import java.util.HashMap;
  import java.util.Map;
  import java.util.List;
  import java.util.Arrays;

  public class PaymentRequest {
      public static void main(String[] args) {
          String url = "https://test.payu.in/_payment";
          
          Map<String, Object> childInstrument = new HashMap<>();
          childInstrument.put("name", "CC");
          childInstrument.put("bankCode", "CC");
          childInstrument.put("cardNumber", "5123456789012346");
          childInstrument.put("cvv", "345");
          childInstrument.put("validThrough", "07/25");
          childInstrument.put("ownerName", "Payu");
          childInstrument.put("transactionAmount", "512");
          
          Map<String, Object> earnInstrument = new HashMap<>();
          earnInstrument.put("name", "RD");
          earnInstrument.put("bankCode", "TWIDLS");
          earnInstrument.put("transactionAmount", "0");
          earnInstrument.put("rewardId", 269431);
          earnInstrument.put("cardBin", "480855");
          earnInstrument.put("cardLastFour", "0000");
          
          Map<String, Object> splitInfo = new HashMap<>();
          splitInfo.put("childPaymentInstruments", Arrays.asList(childInstrument));
          splitInfo.put("earnPaymentInstruments", Arrays.asList(earnInstrument));
          
          Map<String, Object> data = new HashMap<>();
          data.put("key", "KOEfPI");
          data.put("txnid", "ram1234");
          data.put("productinfo", "Product Info");
          data.put("amount", "100");
          data.put("email", "test@example.com");
          data.put("firstname", "Payu-Admin");
          data.put("lastname", "");
          data.put("phone", "880**08522");
          data.put("surl", "https://pp56admin.payu.in/test_response");
          data.put("furl", "https://pp56admin.payu.in/test_response");
          data.put("pg", "SPLITPAY");
          data.put("bankcode", "TWIDX");
          data.put("txn_s2s_flow", "4");
          data.put("splitInfo", splitInfo);
          data.put("hash", "3842a54c294792e9c8c37c7eba8d9693a85517cb7a47aea33a0368a8f6b337e8343f5ef4f726af206ef68549b542ff75dc66fb3b8e8fd5786733131a74cbe741");
          
          Gson gson = new GsonBuilder().create();
          String jsonData = gson.toJson(data);
          
          HttpClient client = HttpClient.newHttpClient();
          HttpRequest request = HttpRequest.newBuilder()
                  .uri(URI.create(url))
                  .header("Content-Type", "application/json")
                  .POST(HttpRequest.BodyPublishers.ofString(jsonData))
                  .build();
          
          try {
              HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
              System.out.println("Status Code: " + response.statusCode());
              System.out.println("Response: " + response.body());
          } catch (IOException | InterruptedException e) {
              System.out.println("Error: " + e.getMessage());
          }
      }
  }
  ```
  ```php
  <?php
  $url = "https://test.payu.in/_payment";

  $data = array(
      "key" => "KOEfPI",
      "txnid" => "ram1234",
      "productinfo" => "Product Info",
      "amount" => "100",
      "email" => "test@example.com",
      "firstname" => "Payu-Admin",
      "lastname" => "",
      "phone" => "880**08522",
      "surl" => "https://pp56admin.payu.in/test_response",
      "furl" => "https://pp56admin.payu.in/test_response",
      "pg" => "SPLITPAY",
      "bankcode" => "TWIDX",
      "txn_s2s_flow" => "4",
      "splitInfo" => array(
          "childPaymentInstruments" => array(
              array(
                  "name" => "CC",
                  "bankCode" => "CC",
                  "cardNumber" => "5123456789012346",
                  "cvv" => "345",
                  "validThrough" => "07/25",
                  "ownerName" => "Payu",
                  "transactionAmount" => "512"
              )
          ),
          "earnPaymentInstruments" => array(
              array(
                  "name" => "RD",
                  "bankCode" => "TWIDLS",
                  "transactionAmount" => "0",
                  "rewardId" => 269431,
                  "cardBin" => "480855",
                  "cardLastFour" => "0000"
              )
          )
      ),
      "hash" => "3842a54c294792e9c8c37c7eba8d9693a85517cb7a47aea33a0368a8f6b337e8343f5ef4f726af206ef68549b542ff75dc66fb3b8e8fd5786733131a74cbe741"
  );

  $options = array(
      'http' => array(
          'header' => "Content-Type: application/json\r\n",
          'method' => 'POST',
          'content' => json_encode($data)
      )
  );

  $context = stream_context_create($options);

  try {
      $result = file_get_contents($url, false, $context);
      if ($result === FALSE) {
          echo "Error: Failed to make request\n";
      } else {
          $http_response_header_status = $http_response_header[0];
          echo "Status: " . $http_response_header_status . "\n";
          echo "Response: " . $result . "\n";
      }
  } catch (Exception $e) {
      echo "Error: " . $e->getMessage() . "\n";
  }
  ?>
  ```
</Accordion>

## Step 3: Redirect the customer

Basis a successful response of the authentication API, you need to redirect the user to the bank page using **acsTemplate**.  This API specifies the response that is posted to `termUrl` after the authentication for the transaction has been processed.

> 📘 Notes:
>
> * All callbacks POST form data on the merchant's `termUrl` that is passed in Initiate Transaction API.
> * Validation of the response happens on the basis of the hash value being returned in the hash value of the response.

<Accordion title="Request parameters" icon="fa-code">
  <HTMLBlock>{`
                                             <style>
                                             /* Target only the second column in the table */
                                             .markdown-body table td:nth-child(2) {
                                               word-break: break-word !important;
                                             }
                                             
                                             /* Keep the first column from breaking unnecessarily */
                                             .markdown-body table td:nth-child(1) {
                                               word-break: normal;
                                               white-space: nowrap;
                                             }
                                             </style>
                                             <table style="width: 100%; border-collapse: collapse;">
                                             <thead>
                                             <tr>
                                               <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
                                               <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
                                             </tr>
                                             </thead>
                                             <tbody>
                                             <tr>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>rawBankData<br><code>mandatory</code></p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter contains the raw response that is received from bank after authentication. The response is urlencoded and in query string format.</p>
                                             </td>
                                             </tr>
                                             <tr>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>referenceId<br><code>mandatory</code></p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter contains the reference id being returned for the transaction</p>
                                             </td>
                                             </tr>
                                             <tr>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>bankData<br><code>mandatory</code></p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON</code> This parameter contains the JSON string that is to be used for authorization call.This parameter is received in case of successful OTP submission of decoupled transactions. The postToBank contains messageDigest and pares that is to be posted back for authorization. For more information on the fields in this JSON, refer to bankData <a href="#bankdata-json-fields-description">JSON Fields Description</a>.</p>
                                             </td>
                                             </tr>
                                             <tr>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>authenticationStatus<br><code>mandatory</code></p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter contains the authentication status of the transaction</p>
                                             </td>
                                             </tr>
                                             <tr>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>hash<br><code>mandatory</code></p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter contains the calculated hash of the data that is posted to the merchant. For security purpose it is recommended to validate the hash value before consuming the response. The hash calculation logic is:<br><code>sha512(authenticationStatus\|bankData\|rawBankData\|referenceId\|salt)</code></p>
                                             </td>
                                             </tr>
                                             </tbody>
                                             </table>
  `}</HTMLBlock>

  #### bankData JSON fields description

  <HTMLBlock>{`
                                             <table style="width: 100%; border-collapse: collapse;">
                                             <thead>
                                             <tr>
                                               <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
                                               <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
                                               <th style="border: 1px solid #ddd; padding: 8px;"><strong>Applicable for EMV 3DS</strong></th>
                                             </tr>
                                             </thead>
                                             <tbody>
                                             <tr>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>cres<br><code>mandatory</code></p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field contains the Base64 encoded value received from ACS as part of the authentication response.</p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>Yes</p>
                                             </td>
                                             </tr>
                                             <tr>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>referenceId<br><code>mandatory</code></p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field is returned in case of decoupled flow. This field contains the reference id for the transaction</p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
                                             </td>
                                             </tr>
                                             <tr>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>messageDigest<br><code>mandatory</code></p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field is returned in case of decoupled flow. This field contains the MD value being returned by the bank.</p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
                                             </td>
                                             </tr>
                                             <tr>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>pares<br><code>mandatory</code></p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field is returned in case of decoupled flow. This field contains the pares being returned by the bank</p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
                                             </td>
                                             </tr>
                                             <tr>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalInfo<br><code>mandatory</code></p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field is returned in case of decoupled flow. This field contains the data that is being used for the gateways that do not return pares.</p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
                                             </td>
                                             </tr>
                                             <tr>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>authorizationUrl<br><code>mandatory</code></p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This integration document assumes that you have opt-ed out for the particular configuration.<br>The authorization URL in legacy integrations are present basis the config at PayU. Please reach out to <a href="mailto:integration@payu.in">integration@payu.in</a> to know more about.</p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"></td>
                                             </tr>
                                             </tbody>
                                             </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  ```plaintext
  { 
      "rawBankData" : ""  
      "referenceId":  "00c44a4c8306f9cbe5ecf6133afe08a7" 
      "bankData" : { 
      "referenceId": "00c44a4c8306f9cbe5ecf6133afe08a7", 
      "messageDigest": "c2e9e456037f033e5cc3d7b6e556189adf41eeabf706844dff70aac91f6b8e73bb1846286c8f99ea768cf38f7c12369c|523727493647950f32684bd6f1ab07aa6474016f", 
      "pares": "eNrVmdeS47i2pl+lo8+loje968jOCHojGtGLvKM3opHoyacfZmZVde06PWfOzMXEjCIUgkBiYRHAWv8H4s0phyzj7CyZh+z9TcvGMSqy36r0r99jFAfhGIT/gLE8/QNNM/IPEiGoP5CUgGEwAjGCSH9/f7vRVjZ+NvgsnTVLNoxV371D/wL/Bb8B3/+exoekjLrp/S1KXoysv6MkQhHYG/Dt71ubDTL3DkMwhZIgRoIIAoL4G/BV/Qb83f42f5TG0+GtSt9Dp5gMTkMMGzxCLtm1mik1zkV02PzrDfi44y2NpuwdBuHTNgj9BiF/IsSfyOnbZ/3b88Mc3fbzaRuCwDfg54q3c2SGrEv2dwQ7nfnx7y3bnn2XnXecdn6U34C/fXtG3Tv40wcFQeK0fda+Off3t6lqf/YJ/RMi/4ShN+Cz/m2comme34M34FvpLYmW5Z2maYYVTJqWzadhJqu+0t8/57N+3vKWJdU7eA7rx+9nK7op+qGayvbD1X+veAM+XAE+p+79za6K7uxsyH7b2qYb//q9nKbnnwCwruu/VuRf/VAA8PkgAEgB5w3pWBX/8ftXqyyVu7z/32rGRl3fVUnUVEc0nQtEy6ayT3/74ds/mXGsD0sQYPHsH6epPxII7f74qAERCDttAv9s9Kcn++/08quzwxj9MZYR9NHBL4be36wszz5WRPaba8l//f4f36OAq4psnP5Puvve1c8WvtvzombO3mc3DXRwZEp92R+80+1LH1P8RNQ4/9f3dl93vgE//Pvm/NdM/TQiXzc6RMf6GG04qXdxrxgV1PAQ4FJa38tkuNT", 
      "additionalInfo": 
      { 
          "authUdf1": "", 
          "authUdf2": "", 
          "authUdf3": "", 
          "authUdf4": "", 
          "authUdf5": "", 
          "authUdf6": "", 
          "authUdf7": "", 
          "authUdf8": "", 
          "authUdf9": "", 
          "authUdf10": "" 
      } 
  }, 
      "authenticationStatus"  :  "success", 
      "hash" : "664b8ddd1b5b2d1b68abb7eee5ea6e001a02773499ddcd86956ba0833315e7d4e69c641d7b0b3e7590532e21e71936da173f4eda716fc09f83cd1117f0d0c37c"} 
  ```
</Accordion>

## Step 4: Authorize (charge) the payment

The authorization request is the final step of transaction processing. This again needs to be an S2S call from the merchant's server to PayU server.

<Accordion title="Request parameters" icon="fa-code">
  **Post URL**: The data to be posted has to be exactly the same as the JSON response received in the authentication response in [Step 2](#step-2-redirect-the-customer). The data must include the following parameters.

  #### Environment

  |            |                                                                                                    |
  | ---------- | -------------------------------------------------------------------------------------------------- |
  | Test       | [https://test.payu.in/AuthorizeTransaction.php](https://test.payu.in/AuthorizeTransaction.php)     |
  | Production | [https://secure.payu.in/AuthorizeTransaction.php](https://secure.payu.in/AuthorizeTransaction.php) |

  <HTMLBlock>{`
                                             <style>
                                             /* Target only the second column in the table */
                                             .markdown-body table td:nth-child(2) {
                                               word-break: break-word !important;
                                             }
                                             
                                             /* Keep the first column from breaking unnecessarily */
                                             .markdown-body table td:nth-child(1) {
                                               word-break: normal;
                                               white-space: nowrap;
                                             }
                                             </style>
                                             <table style="width: 100%; border-collapse: collapse;">
                                             <thead>
                                             <tr>
                                               <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
                                               <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
                                             </tr>
                                             </thead>
                                             <tbody>
                                             <tr>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>key<br><code>mandatory</code></p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The merchant key is provided by PayU and acts as a unique identifier for a specific merchant account in PayU's database.</p>
                                             </td>
                                             </tr>
                                             <tr>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>txnid<br><code>mandatory</code></p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The transaction ID is the order reference number generated by the merchant to track a particular order. It can be used only once and PayU's system does not accept a duplicate Transaction ID.</p>
                                             </td>
                                             </tr>
                                             <tr>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>amount<br><code>mandatory</code></p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> It should contain the payment amount of the particular transaction. The amount must be greater than Rs. 8000 for the cardless EMI option.</p>
                                             </td>
                                             </tr>
                                             <tr>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>hash<br><code>mandatory</code></p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> It is used to avoid the possibility of transaction tampering. The hash must in the following structure:<br> <code>valueOf(key)\| valueOf(txnid) \| valueOf(amount) \|valueOf(authentication_info) \| valueOf(salt)</code></p>
                                             </td>
                                             </tr>
                                             <tr>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p>authentication_info<br><code>mandatory</code></p>
                                             </td>
                                               <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON</code> The JSON value received in the bankData on the Term URL or pass the fields as in the <a href="#example-for-authentication_info-json">JSON example</a>.</p>
                                             </td>
                                             </tr>
                                             </tbody>
                                             </table>
  `}</HTMLBlock>

  #### Example for authentication\_info JSON

  ```plaintext
  {
     "referenceId": "00c44a4c8306f9cbe5ecf6133afe08a7",
     "cres": "eyJhY3NUcmFuc0lEIjoiODc3OTFjZWUtMjUxNC00MzZjLWJlZDgtYTYzYTg3YmJkZjAxIiwiY2hhbGxlbmdlQ29tcGxldGlvbkluZCI6IlkiLCJtZXNzYWdlVHlwZSI6IkNSZXMiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMS4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiJkNDFmNjIwMC0wNDM1LTQ5ZWUtYWExMS1mMzY2ZjA2NjFjNmYiLCJ0cmFuc1N0YXR1cyI6IlkifQ==",
     "messageDigest": "",
     "pares": "",
     "additionalInfo": {
        "authUdf1": "",
        "authUdf2": "",
        "authUdf3": "",
        "authUdf4": "",
        "authUdf5": "",
        "authUdf6": "",
        "authUdf7": "",
        "authUdf8": "",
        "authUdf9": "",
        "authUdf10": ""
     }
  }
  ```

  #### authentication\_info JSON Fields Description

  | **Field**      | **Description**                                                                                        | **Applicable to EMV 3DS** |
  | -------------- | ------------------------------------------------------------------------------------------------------ | ------------------------- |
  | cres           | This field contains the Base 64 encoded value received from ACS as part of the authentication response | Yes                       |
  | referenceId    | This field contains the same referenceId which sent in response of the first call                      |                           |
  | additionalInfo | This field can be used in the case of schemes where different parameters may need from merchant side.  |                           |
  | messageDigest  | This field includes the Base 64 encoding of (sha56 hash of the JSON data (post to server).             |                           |
  | pares          | This parameter contains the pares being returned by the bank.                                          |                           |
</Accordion>

## Step 5: Check response from PayU

<ReverseHashing />

<Accordion title="Sample response (parsed)" icon="fa-code">
  * Success scenario (Zillion + UPI)

  ```
  {
  "mihpayid": "999091000010475",
  "mode": "SPLITPAY",
  "status": "success",
  "unmappedstatus": "success",
  "key": "KOEfPI",
  "txnid": " ram12345",
  "amount": "100",
  "discount": "0.00",
  "net_amount_debit": "100",
  "addedon": "2025-01-10 14:56:13",
  "productinfo": "Product Info",
  "firstname": "Payu-Admin",
  "lastname": "",
  "address1": "",
  "address2": "",
  "city": "",
  "state": "",
  "country": "",
  "zipcode": "",
  "email": "test@example.com",
  "phone": "8800**8522",
  "udf1": "",
  "udf2": "",
  "udf3": "",
  "udf4": "",
  "udf5": "",
  "udf6": "",
  "udf7": "",
  "udf8": "",
  "udf9": "",
  "udf10": "",
  "hash": "29efcd4f7a8a9a60a61481d70e21baf5ba6e7a472716d9b99bd911ef5390240411107b959e5bc8cdabc31463d150d4e02578349afa20529b18e271f60dd6db59",
  "field1": "",
  "field2": "",
  "field3": "",
  "field4": "",
  "field5": "",
  "field6": "",
  "field7": "",
  "field8": "",
  "field9": "",
  "payment_source": "payuS2S",
  "PG_TYPE": "SPLITPAY-PG",
  "bank_ref_num": "1254",
  "error": "E000",
  "bankcode": "ZRD",
  "error_Message": "No Error",
  "splitPayInfo": {
    "upi": {
      "name": "UPI",
      "bankCode": "UPI",
      "vpa": "kk@okaxis",
      "transactionAmount": "99"
    },
    "rd": {
      "name": "RD",
      "bankCode": "ZLS",
      "transactionAmount": "1"
    }
  }
  }
  ```

  * Success scenario (Zillion + Cards)

  ```
  {
  "mihpayid": "999091000010471",
  "mode": "SPLITPAY",
  "status": "success",
  "unmappedstatus": "success",
  "key": "KOEfPI",
  "txnid": " ram1234",
  "amount": "100",
  "discount": "0.00",
  "net_amount_debit": "100",
  "addedon": "2025-01-10 14:54:13",
  "productinfo": "Product Info",
  "firstname": "Payu-Admin",
  "lastname": "",
  "address1": "",
  "address2": "",
  "city": "",
  "state": "",
  "country": "",
  "zipcode": "",
  "email": "test@example.com",
  "phone": "8800108522",
  "udf1": "",
  "udf2": "",
  "udf3": "",
  "udf4": "",
  "udf5": "",
  "udf6": "",
  "udf7": "",
  "udf8": "",
  "udf9": "",
  "udf10": "",
  "hash": "29efcd4f7a8a9a60a61481d70e21baf5ba6e7a472716d9b99bd911ef5390240411107b959e5bc8cdabc31463d150d4e02578349afa20529b18e271f60dd6db59",
  "field1": "",
  "field2": "",
  "field3": "",
  "field4": "",
  "field5": "",
  "field6": "",
  "field7": "",
  "field8": "",
  "field9": "",
  "payment_source": "payuS2S",
  "PG_TYPE": "SPLITPAY-PG",
  "bank_ref_num": "1254",
  "error": "E000",
  "bankcode": "ZRD",
  "error_Message": "No Error",
  "splitPayInfo": {
    "cc": {
      "name": "CC",
      "bankCode": "CC",
      "transactionAmount": "99"
    },
    "rd": {
      "name": "RD",
      "bankCode": "ZLS",
      "transactionAmount": "1"
    }
  }
  }
  ```

  * Success scenario (TWID + Cards)

  ```
  {
  "mihpayid": "999091000010480",
  "mode": "SPLITPAY",
  "status": "success",
  "unmappedstatus": "success",
  "key": "KOEfPI",
  "txnid": "ram1234",
  "amount": "512",
  "discount": "0.00",
  "net_amount_debit": "512",
  "addedon": "2025-01-10 15:00:00",
  "productinfo": "Product Info",
  "firstname": "Payu-Admin",
  "lastname": "",
  "address1": "",
  "address2": "",
  "city": "",
  "state": "",
  "country": "",
  "zipcode": "",
  "email": "test@example.com",
  "phone": "8800108522",
  "udf1": "",
  "udf2": "",
  "udf3": "",
  "udf4": "",
  "udf5": "",
  "udf6": "",
  "udf7": "",
  "udf8": "",
  "udf9": "",
  "udf10": "",
  "hash": "29efcd4f7a8a9a60a61481d70e21baf5ba6e7a472716d9b99bd911ef5390240411107b959e5bc8cdabc31463d150d4e02578349afa20529b18e271f60dd6db59",
  "field1": "",
  "field2": "",
  "field3": "",
  "field4": "",
  "field5": "",
  "field6": "",
  "field7": "",
  "field8": "",
  "field9": "",
  "payment_source": "payuS2S",
  "PG_TYPE": "SPLITPAY-PG",
  "bank_ref_num": "1255",
  "error": "E000",
  "bankcode": "TWIDX",
  "error_Message": "No Error",
  "splitPayInfo": {
    "cc": {
      "name": "CC",
      "bankCode": "CC",
      "transactionAmount": "412"
    },
    "rd": {
      "name": "RD",
      "bankCode": "TWIDLS",
      "transactionAmount": "100"
    }
  }
  }
  ```

  * Success scenario (TWID + UPI)

  ```
  {
  "mihpayid": "999091000010482",
  "mode": "SPLITPAY",
  "status": "success",
  "unmappedstatus": "success",
  "key": "KOEfPI",
  "txnid": "ram1234",
  "amount": "512",
  "discount": "0.00",
  "net_amount_debit": "512",
  "addedon": "2025-01-10 15:10:00",
  "productinfo": "Product Info",
  "firstname": "Payu-Admin",
  "lastname": "",
  "address1": "",
  "address2": "",
  "city": "",
  "state": "",
  "country": "",
  "zipcode": "",
  "email": "test@example.com",
  "phone": "8800108522",
  "udf1": "",
  "udf2": "",
  "udf3": "",
  "udf4": "",
  "udf5": "",
  "udf6": "",
  "udf7": "",
  "udf8": "",
  "udf9": "",
  "udf10": "",
  "hash": "29efcd4f7a8a9a60a61481d70e21baf5ba6e7a472716d9b99bd911ef5390240411107b959e5bc8cdabc31463d150d4e02578349afa20529b18e271f60dd6db59",
  "field1": "",
  "field2": "",
  "field3": "",
  "field4": "",
  "field5": "",
  "field6": "",
  "field7": "",
  "field8": "",
  "field9": "",
  "payment_source": "payuS2S",
  "PG_TYPE": "SPLITPAY-PG",
  "bank_ref_num": "1256",
  "error": "E000",
  "bankcode": "TWIDX",
  "error_Message": "No Error",
  "splitPayInfo": {
    "upi": {
      "name": "UPI",
      "bankCode": "UPI",
      "vpa": "kk@okaxis",
      "transactionAmount": "412"
    },
    "rd": {
      "name": "RD",
      "bankCode": "TWIDLS",
      "transactionAmount": "100"
    }
  }
  }
  ```

  * Failure scenario

  ```
  Array
  (
      [mihpayid] => 20869277619
      [mode] => CC
      [status] => failure
      [unmappedstatus] => failed
      [key] => L43t1c
      [txnid] => 26ba7cd6a67b0a010542
      [amount] => 1.00
      [cardCategory] => domestic
      [discount] => 0.00
      [net_amount_debit] => 0.00
      [addedon] => 2024-09-05 17:46:10
      [productinfo] => Product Info
      [firstname] => Payu-Admin
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => test@example.com
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
      [hash] => ac7720e4bc33e5494bec6d37302e522171175a987f9d47286bfd29e8a7fc794f56433fcacf0bc120db781c4dc1d05a4857d71e83f00f6ed6aa9c97a1938b9467
      [field1] => 
      [field2] => 
      [field3] => 
      [field4] => 
      [field5] => 05
      [field6] => 
      [field7] => AUTHNEGATIVE
      [field8] => 
      [field9] => Authorization failed at Bank
      [payment_source] => payu
      [pa_name] => PayU
      [PG_TYPE] => CC-PG
      [bank_ref_num] => 2409052690
      [bankcode] => AMEX
      [error] => E1903
      [error_Message] => Authorization failed at Bank
      [cardnum] => XXXXXXXXXXXX2003
      [cardhash] => This field is no longer supported in postback params.
  )
  ```

  <br />
</Accordion>

<Accordion title="Raw _payment API response (Card / UPI)" icon="fa-code">
  In the **decoupled (txn\_s2s\_flow = 4)** integration, the immediate response from the `_payment` endpoint is a JSON payload containing a `referenceId`, `metaData`, optional `binData`, and a base64-encoded `result.acsTemplate`. The merchant must base64-decode the `acsTemplate` to obtain an HTML form that auto-submits to the bank/UPI redirect page where the customer completes authentication. The `parsed` postback shown above is what PayU posts back to your `surl` / `furl` after the customer finishes the authentication step.

  * Raw `_payment` response (Card)

  ```json
  {
    "referenceId": "29b2d115825c53d10a56d64fd359c816",
    "order": 1,
    "metaData": {
      "referenceId": "29b2d115825c53d10a56d64fd359c816",
      "txnId": "6e5cc585-6d9f-47e5-909c-78268bafec7b",
      "txnStatus": "Enrolled",
      "unmappedStatus": "pending",
      "type": "otp",
      "expiryTimeout": 180,
      "cancelUrl": "https://pp1api.payu.in/split-payment/transaction/v1/af6221f5e6baa4cae60c86eff057b234/cancel/29b2d115825c53d10a56d64fd359c816",
      "isSplitTransaction": true
    },
    "binData": {
      "pureS2SSupported": false,
      "issuingBank": "ICICI",
      "category": "creditcard",
      "cardType": "VISA",
      "isDomestic": true
    },
    "result": {
      "otpPostUrl": "",
      "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vcHAxc2VjdXJlLnBheXUuaW4vLi4uLi9DcmVxIiBtZXRob2Q9InBvc3QiPjwvZm9ybT4="
    },
    "mode": "CC"
  }
  ```

  * Raw `_payment` response (UPI)

  ```json
  {
    "referenceId": "3d6cd50a233c2016644af4a0be40fa12",
    "order": 1,
    "metaData": {
      "referenceId": "3d6cd50a233c2016644af4a0be40fa12",
      "txnId": "6e557dba-955d-4ee9-b49e-7b5b186e71e5",
      "txnStatus": "pending",
      "unmappedStatus": "pending",
      "type": "otp",
      "expiryTimeout": 180,
      "cancelUrl": "https://pp1api.payu.in/split-payment/transaction/v1/9c5c73a100f323c2c2b5a3568cd3176f/cancel/3d6cd50a233c2016644af4a0be40fa12",
      "isSplitTransaction": true
    },
    "result": {
      "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vcHAxYXBpLnBheXUuaW4vcHVibGljLy8vM2Q2Y2Q1MGEyMzNjMjAxNjY0NGFmNGEwYmU0MGZhMTIvdXBpTG9hZGVyIiBtZXRob2Q9ImdldCI+PC9mb3JtPg=="
    },
    "mode": "UPI"
  }
  ```

  #### Raw response field reference

  | Field                       | Description                                                                                                              | Example                            |
  | --------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- |
  | referenceId                 | `String` Unique reference for this leg of the split transaction.                                                         | 29b2d115825c53d10a56d64fd359c816   |
  | order                       | `Number` Sequence of the leg within the split transaction.                                                               | 1                                  |
  | metaData.txnId              | `String` PayU internal transaction id.                                                                                   | 6e5cc585-6d9f-47e5-909c-78268bafec7b |
  | metaData.txnStatus          | `String` Status of the leg (e.g. `Enrolled`, `pending`).                                                                 | Enrolled                           |
  | metaData.unmappedStatus     | `String` Unmapped (raw) status of the leg.                                                                               | pending                            |
  | metaData.type               | `String` Type of authentication challenge (e.g. `otp`).                                                                  | otp                                |
  | metaData.expiryTimeout      | `Number` Expiry, in seconds, for the authentication step.                                                                | 180                                |
  | metaData.cancelUrl          | `String` URL the merchant can call to cancel the split-payment leg before the customer completes authentication.         | https://...                        |
  | metaData.isSplitTransaction | `Boolean` Always `true` for `SPLITPAY` flows.                                                                            | true                               |
  | binData.issuingBank         | `String` Issuing bank for the card (Card flow only).                                                                     | ICICI                              |
  | binData.category            | `String` Card category (Card flow only).                                                                                 | creditcard                         |
  | binData.cardType            | `String` Card network (Card flow only).                                                                                  | VISA                               |
  | binData.isDomestic          | `Boolean` Whether the card is domestic (Card flow only).                                                                 | true                               |
  | result.acsTemplate          | `String (Base64)` Base64-encoded HTML form. Decode and render in the browser to redirect the customer for authentication. | PGh0bWw+PGJvZHk+...                |
  | result.otpPostUrl           | `String` URL to which the OTP must be POSTed (when applicable).                                                          |                                    |
  | mode                        | `String` Payment instrument used for this leg: `CC` for Card, `UPI` for UPI.                                             | CC                                 |
</Accordion>

## Step 6: Verify the Payment

<Verify_Payment_Tabs />