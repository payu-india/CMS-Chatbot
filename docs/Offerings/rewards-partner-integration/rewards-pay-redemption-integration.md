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

Integrate TWID pay to enable customers to redeem their TWID loyalty points during checkout. Follow these sequential steps to implement a complete TWID pay solution.

This section describes the complete integration workflow for TWID Rewards Seamless Transactions. This integration involves the following steps:

<Cards columns={3}>
  <Card title="1. Fetch All Balance" href="#step-1-fetch-all-balance">
    Call loyalty-service to get usable reward balances for the customer before initiating payment
  </Card>

  <Card title="2. Initiate Payment with PayU" href="#step-2-initiate-payment-with-payu">
    Prepare PayU payment POST with SPLITPAY, TWIDX, splitInfo parameters and generate the required hash
  </Card>

  <Card title="3. Check Response from PayU" href="#step-3-check-response-from-payu">
    Parse postback response and validate reverse hash from PayU
  </Card>

  <Card title="4. Verify the Payment" href="#step-4-verify-the-payment">
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
                                          <code>String</code> User's mobile number (masked for privacy)
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
                                    </tbody>
                                  </Table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "{{loyalty-service-url}}/v1/balance/all" \
    -H "Content-Type: application/json" \
    -H "mid: YOUR_MERCHANT_ID" \
    -d '{
      "loyaltyProviders": ["TWID", "ZILLION"],
      "mobileNumber": "88001085**",
      "orderAmount": 1000
    }'
  ```
  ```python
  import requests
  import json

  url = "{{loyalty-service-url}}/v1/balance/all"

  headers = {
    "Content-Type": "application/json",
    "mid": "YOUR_MERCHANT_ID"
  }

  payload = {
    "loyaltyProviders": ["TWID", "ZILLION"],
    "mobileNumber": "88001085**",
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
          var url = "{{loyalty-service-url}}/v1/balance/all";
          
          client.DefaultRequestHeaders.Add("Content-Type", "application/json");
          client.DefaultRequestHeaders.Add("mid", "YOUR_MERCHANT_ID");

          var json = new
          {
              loyaltyProviders = new[] { "TWID", "ZILLION" },
              mobileNumber = "88001085**",
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
  const url = "{{loyalty-service-url}}/v1/balance/all";

  const headers = {
    "Content-Type": "application/json",
    "mid": "YOUR_MERCHANT_ID"
  };

  const payload = {
    "loyaltyProviders": ["TWID", "ZILLION"],
    "mobileNumber": "88001085**",
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
          URL url = new URL("{{loyalty-service-url}}/v1/balance/all");
          HttpURLConnection conn = (HttpURLConnection) url.openConnection();
          conn.setRequestMethod("POST");
          conn.setDoOutput(true);
          
          conn.setRequestProperty("Content-Type", "application/json");
          conn.setRequestProperty("mid", "YOUR_MERCHANT_ID");

          Gson gson = new Gson();
          String jsonInputString = "{\"loyaltyProviders\":[\"TWID\",\"ZILLION\"],\"mobileNumber\":\"88001085**\",\"orderAmount\":1000}";
          
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

  $url = "{{loyalty-service-url}}/v1/balance/all";

  $headers = [
    "Content-Type" => "application/json",
    "mid" => "YOUR_MERCHANT_ID"
  ];

  $payload = [
    "loyaltyProviders" => ["TWID", "ZILLION"],
    "mobileNumber" => "88001085**",
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
        "title": "Save Rs 500 using 500 TWID Cash Points",
        "earnConfig": { 
          "points": 0, 
          "amount": null, 
          "title": null 
        },
        "issuerDetailDTO": {
          "brandName": "TWID Cash",
          "logo": "https://cdn.twidpay.com/brand_image.png",
          "issuerType": "brand"
        },
        "holdApplicable": false
      },
      {
        "loyaltyProvider": "ZILLION",
        "customErrorMessage": "Unable to process request for provider",
        "usableAmount": null,
        "usablePoints": null
      }
    ]
  }
  ```
</Accordion>

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
  | pg<br />`mandatory`                   | `String` The pg parameter must contain `SPLITPAY` for TWID Rewards.                                                                                                                                                                                                                                | SPLITPAY                                                                                           |   |
  | bankcode<br />`mandatory`             | `String` The bankcode parameter must contain any of the following based on the Reward partner: <ul><li>TWIDX for TWID Rewards</li><li>ZRD for Zillon </li></ul>-                                                                                                                                   | TWIDX                                                                                              |   |
  | splitInfo                             | `JSON` This parameter must contain the TWID split information. For more information, refer to [splitInfo JSON Object Fields Description](#splitinfo-json-object-fields-description). The sample JSON for Spend/Burn or Earn Points with payment methods: <br />-[Cards](#cards) <br />-[UPI](#upi) | Refer to to [splitInfo JSON Object Fields Description](#splitinfo-json-object-fields-description). |   |
  | furl<br />`mandatory`                 | `String` The success URL, which is the page PayU will redirect to if the transaction is successful.                                                                                                                                                                                                |                                                                                                    |   |
  | surl<br />`mandatory`                 | `String` The Failure URL, which is the page PayU will redirect to if the transaction is failed.                                                                                                                                                                                                    |                                                                                                    |   |
  | hash<br />`mandatory`                 | `String` It is the hash calculated by the merchant. The hash calculation logic is: \`sha512(key\\\|txnid\\\|amount\\\|productinfo\\\|firstname\\\|email\\\|udf1\\\|udf2\\\|udf3\\\|udf4\\\|udf5\\\|\\\|\\\|\\\|\\\|                                                                                | SALT)\`                                                                                            |   |
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

### splitInfo JSON Object Fields Description

#### Cards

<Accordion title="Sample request for Spend Points with Card (Zillion)" icon="fa-code">
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

<Accordion title="Sample request for Spend Points with Card (TWID)" icon="fa-code">
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

<Accordion title="Sample request for Spend Points with UPI (Zillion)" icon="fa-code">
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

<Accordion title="Sample request for Spend Points with UPI (TWID)" icon="fa-code">
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
  | Field                                    | Description                                                                                                                           | Example          |
  | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
  | name                                     | The name of the payment method. Use any of the following as required:<br />**CC** for Cards<br />**RD** for TWID<br />**UPI** for UPI | CC               |
  | bankCode                                 | The bank code identifier for the payment method. Use `TWIDLS` for TWID Rewards                                                        | CC               |
  | cardNumber<br /> `mandatory for cards`   | The credit/debit card number for the transaction.                                                                                     | 5123456789012346 |
  | cvv<br /> `mandatory for cards`          | The Card Verification Value (CVV) for card validation.                                                                                | 345              |
  | validThrough<br /> `mandatory for cards` | The card expiry date in MM/YY format.                                                                                                 | 07/25            |
  | ownerName                                | The name of the card holder or account owner.                                                                                         | Ashish           |
  | rewardId<br /> `mandatory for TWID`      | The TWID Rewards card holder ID.                                                                                                      | 345              |
  | rewardName<br /> `mandatory for TWID`    | The TWID Rewards card holder name.                                                                                                    | 345              |
  | cardBin<br /> `mandatory for cards`      | The TWID Rewards card BIN.                                                                                                            | 345456           |
  | cardLastFour<br /> `mandatory for cards` | The TWID Rewards card last four digits.                                                                                               | 3455             |
  | transactionAmount                        | The amount to be processed in the transaction for the given payment instrument.                                                       | 512              |
</Accordion>

<Accordion title="Field Descriptions in earnPaymentInstruments" icon="fa-table">
  | Field    | Description                                                                                                                           | Example |
  | -------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------- |
  | name     | The name of the payment method. Use any of the following as required:<br />**CC** for Cards<br />**RD** for TWID<br />**UPI** for UPI | CC      |
  | bankCode | The bank code identifier for the payment method. Use `TWIDLS` for TWID Rewards                                                        |         |

  CC               |
  \| transactionAmount                        | The amount to be processed in the transaction for the given payment instrument.                                                       | 512              |
  \| rewardId<br /> `mandatory for TWID`      | The TWID Rewards card holder ID.                                                                                                      | 345              |
  \| rewardName<br /> `mandatory for TWID`      | The TWID Rewards Program Name.                                                                                                      | 345              |
  \| cardBin<br /> `mandatory for cards`      | The TWID Rewards card BIN.                                                                                                            | 345456           |
  \| cardLastFour<br /> `mandatory for cards` | The TWID Rewards card last four digits.                                                                                               | 3455             |
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


## Step 3: Check response from PayU

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

## Step 4: Verify the Payment

<Verify_Payment_Tabs />
