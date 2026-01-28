---
title: TWID Seamless Card Transaction Integration
deprecated: false
hidden: true
metadata:
  title: TWID Seamless Card Transaction Integration
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

This section describes the complete integration workflow for Twid Seamless Card Transactions. The workflow involves fetching balances from multiple loyalty providers, holding the points for a card transaction, and then redeeming them.

<Cards columns={3}>
  <Card title="1. Fetch All Balance" href="#step-1-fetch-all-balance">
    Fetch reward point balances from multiple loyalty providers

    <br />
  </Card>

  <Card title="2. Hold TWID Points" href="#step-2-hold-twid-points">
    Hold (reserve) reward points for the card transaction

    <br />
  </Card>

  <Card title="3. Redeem TWID Points" href="#step-3-redeem-twid-points">
    Redeem the held points to complete the transaction
  </Card>
</Cards>

## Step 1: Fetch All Balance

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

<br />
## Step 2: Initiate the payment to PayU

<Accordion title="Post Request Syntax & Composition" icon="fa-code">
  Post Request Syntax & Composition for Cards

  ```html
  <body>
  <form action='https://test.payu.in/_payment' method='post'>
  <input type="hidden" name="key" value="JP***g" />
  <input type="hidden" name="txnid" value="t6svtqtjRdl34W" />
  <input type="hidden" name="productinfo" value="iPhone" />
  <input type="hidden" name="amount" value="10" />
  <input type="hidden" name="email" value="test@gmail.com" />
  <input type="hidden" name="firstname" value="Ashish" />
  <input type="hidden" name="lastname" value="Kumar" />
  <input type="hidden" name="pg" value="CC" />
  <input type="hidden" name="bankcode" value="MAST" />
  <input type="hidden" name="ccnum" value="5123456789012346" />
  <input type="hidden" name="ccname" value="Ashish Kumar" />
  <input type="hidden" name="ccvv" value="123" />
  <input type="hidden" name="ccexpmon" value="12" />
  <input type="hidden" name="ccexpyr" value="2021" />
  <input type="hidden" name="surl" value="your own success url" />
  <input type="hidden" name="furl" value="your own failure url" />
  <input type="hidden" name="phone" value="9988776655" />
  <input type="hidden" name="hash" value="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />
  <input type="submit" value="submit"> </form>
  </body>
  </html>
  ```

  <Callout icon="📘" theme="info">
    **Note**: The above code block is for Merchant Checkout integration on the credit card call for the test environment.
  </Callout>
</Accordion>

<Accordion title="Request Parameters" icon="fa-table">
  Post the following parameters for the card payment to PayU using the Merchant Hosted integration.

  **Environment**

  |                            |                                                                         |
  | :------------------------- | :---------------------------------------------------------------------- |
  | **Test Environment**       | \<[https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
  | **Production Environment** | \<[https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

  <Callout icon="📘" theme="info">
    **Reference**: For the **Try It** experience and response, refer to <Anchor label="Collect Payment API - Merchant Hosted Checkout" target="_blank" href="https://docs.payu.in/reference/_payment_merchant_hosted">Collect Payment API - Merchant Hosted Checkout</Anchor> under API Reference.
  </Callout>
| Parameter | Description | Example |
| --- | --- | --- |
| key<br/>`mandatory` | `String` Merchant key provided by PayU during onboarding. | JP***g |
| txnid<br/>`mandatory` | `String` The transaction ID is a reference number for a specific order that is generated by the merchant. | ashdfu72634 |
| amount<br/>`mandatory` | `String` The payment amount for the transaction. |  |
| productinfo<br/>`mandatory` | `String` A brief description of the product. |  |
| firstname<br/>`mandatory` | `String` The first name of the customer. | Ashish |
| email<br/>`mandatory` | `String` The email address of the customer. |  |
| phone<br/>`mandatory` | `String` The phone number of the customer. |  |
| pg<br/>`mandatory` | `String` The pg parameter determines which payment tabs will be displayed on the PayU page. For card payments, 'CC' will be the value. | CC |
| bankcode<br/>`mandatory` | `String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For more information, refer to Card Type Codes and Supported Banks for Cards. | AMEX |
| ccnum<br/>`mandatory` | `String` Use 13-19 digit card number for credit/debit cards (15 digits for AMEX, 13-19 for Maestro) and validate with LUHN algorithm. Refer to Card Number Formats and display error message on invalid input. | 5123456789012346 |
| ccname<br/>`mandatory` | `String` This parameter must contain the name on card – as entered by the customer for the transaction. | Ashish Kumar |
| ccvv<br/>`mandatory` | `String` Use 3-digit CVV number for credit/debit cards and 4-digit security code (4DBC/CID) for AMEX cards. Validate with BIN API. | 123 |
| ccexpmon<br/>`mandatory` | `String` This parameter must contain the card's expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format. For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively. | 10 |
| ccexpyr<br/>`mandatory` | `String` This parameter must contain the card's expiry year – as entered by the customer for the transaction. It must be of four digits. | 2021 |
| furl<br/>`mandatory` | `String` The failure URL, which is the page PayU will redirect to if the transaction is failure. |  |
| surl<br/>`mandatory` | `String` The success URL, which is the page PayU will redirect to if the transaction is successful. |  |
| splitInfo<br/>`mandatory for TWID` | `String` This must include the payment details containing card and TWID rewards part of the payment. For more information, refer to [splitInfo JSON Object Fields Description](#splitInfo-json-object-fields-description) | Refer to [splitInfo JSON Object Fields Description](#splitInfo-json-object-fields-description) |
| hash<br/>`mandatory` | `String` It is the hash calculated by the merchant. The hash calculation logic is: `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)` |  |
| address1<br/>`optional` | `String` The first line of the billing address. • **For Fraud Detection**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information. |  |
| address2<br/>`optional` | `String` The second line of the billing address. |  |
| city<br/>`optional` | `String` The city where your customer resides as part of the billing address. |  |
| state<br/>`optional` | `String` The state where your customer resides as part of the billing address. |  |
| country<br/>`optional` | `String` The country where your customer resides. |  |
| zipcode<br/>`optional` | `String` Billing address zip code is mandatory for the cardless EMI option. Character Limit: 20 |  |
| udf1<br/>`optional` | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. |  |
| udf2<br/>`optional` | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. |  |
| udf3<br/>`optional` | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. |  |
| udf4<br/>`optional` | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. |  |
| udf5<br/>`optional` | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. |  |

  <Accordion title="Understanding Hashing and sample code" icon="fa-code">
    <HashingRequestParameters />

    #### Hashing Sample Code

    <HashingSample />
  </Accordion>
</Accordion>
###splitInfo JSON Object Fields Description
<Accordion title="Sample JSON" icon="fa-code">
```JSON
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
    } 
``` 
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  # IMPORTANT: This is a server-side call, never execute this client-side
  # Replace placeholders with actual values
  # In production: Use environment variables for sensitive values

  curl -X POST "https://test.payu.in/_payment" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=YOUR_MERCHANT_KEY" \
    -d "txnid=TXN_12345" \
    -d "amount=1000.00" \
    -d "productinfo=Product+Description" \
    -d "firstname=Customer+Name" \
    -d "email=customer@example.com" \
    -d "phone=9988776655" \
    -d "pg=CC" \
    -d "bankcode=CC" \
    -d "ccnum=CARD_NUMBER" \
    -d "ccexpmon=MM" \
    -d "ccexpyr=YY" \
    -d "ccvv=CVV" \
    -d "ccname=NAME_ON_CARD" \
    -d "surl=https://yourwebsite.com/success" \
    -d "furl=https://yourwebsite.com/failure" \
    -d "hash=HASH_GENERATED_ON_SERVER"
  ```
  ```python
  import urllib.request
  import urllib.parse
  import json
  import os
  from typing import Dict, Any

  def process_payment(payment_data: Dict[str, Any]) -> Dict[str, Any]:
      """
      Process payment using PayU's Merchant Hosted Checkout
      
      IMPORTANT: This is a server-side function. Never expose card details to client-side code.
      This handles sensitive card data and requires PCI DSS compliance.
      
      Args:
          payment_data: Dictionary containing payment information
          
      Returns:
          Dictionary with response from PayU API
      """
      # API endpoint - Use different URLs for test/production environments
      url = "https://test.payu.in/_payment"  # Test URL
      # url = "https://secure.payu.in/_payment"  # Production URL
      
      # Prepare the form data with proper URL encoding
      # In production: Get merchant_key and hash from secure environment variables
      payload = {
          "key": "YOUR_MERCHANT_KEY",           # Replace with actual merchant key
          "txnid": "TXN_12345",                 # Generate unique transaction ID
          "amount": "1000.00",                  # Amount to be charged
          "productinfo": "Product Description", # Description of product/service
          "firstname": "Customer Name",         # Customer's first name
          "email": "customer@example.com",      # Customer's email
          "phone": "9988776655",                # Customer's phone number
          "pg": "CC",                           # Payment gateway (CC for credit card)
          "bankcode": "CC",                     # Bank code (CC for credit card)
          
          # SENSITIVE DATA - Handle with care according to PCI DSS requirements
          "ccnum": "CARD_NUMBER",               # Credit card number
          "ccexpmon": "MM",                     # Expiry month (2 digits)
          "ccexpyr": "YY",                      # Expiry year (2 digits)
          "ccvv": "CVV",                        # Card verification value
          "ccname": "NAME_ON_CARD",             # Name on the card
          
          # Success and failure URLs
          "surl": "https://yourwebsite.com/success",  # Success callback URL
          "furl": "https://yourwebsite.com/failure",  # Failure callback URL
          
          # Hash is generated on server using specific algorithm provided by PayU
          # See PayU documentation for the exact hash generation logic
          "hash": "HASH_GENERATED_ON_SERVER",   # Security hash
      }
      
      # Convert dictionary to URL-encoded form data
      data = urllib.parse.urlencode(payload).encode('utf-8')
      
      # Set headers
      headers = {
          "Content-Type": "application/x-www-form-urlencoded"
      }
      
      # Create a request object
      req = urllib.request.Request(url, data=data, headers=headers, method="POST")
      
      try:
          # Send the request and get the response
          with urllib.request.urlopen(req) as response:
              response_data = response.read().decode('utf-8')
              
              # In production, implement proper response handling and logging
              # (but never log full card details)
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
              "response": "An error occurred during the payment process"
          }

  # Example usage:
  # payment_result = process_payment(payment_data)
  # print(f"Status: {payment_result['status_code']}")
  # Process the response appropriately

  ```
  ```php
  <?php
  /**
   * Process payment using PayU's Merchant Hosted Checkout
   * 
   * IMPORTANT: This is a server-side function. Never expose card details to client-side code.
   * This handles sensitive card data and requires PCI DSS compliance.
   * 
   * @param array $paymentData Payment information
   * @return array Response from PayU API
   */
  function processPayment($paymentData = []) {
      // API endpoint - Use different URLs for test/production environments
      $url = "https://test.payu.in/_payment"; // Test URL
      // $url = "https://secure.payu.in/_payment"; // Production URL
      
      // Prepare the form data
      // In production: Get merchant_key and hash from secure environment variables
      $payload = [
          "key" => "YOUR_MERCHANT_KEY",           // Replace with actual merchant key
          "txnid" => "TXN_12345",                 // Generate unique transaction ID
          "amount" => "1000.00",                  // Amount to be charged
          "productinfo" => "Product Description", // Description of product/service
          "firstname" => "Customer Name",         // Customer's first name
          "email" => "customer@example.com",      // Customer's email
          "phone" => "9988776655",                // Customer's phone number
          "pg" => "CC",                           // Payment gateway (CC for credit card)
          "bankcode" => "CC",                     // Bank code (CC for credit card)
          
          // SENSITIVE DATA - Handle with care according to PCI DSS requirements
          "ccnum" => "CARD_NUMBER",               // Credit card number
          "ccexpmon" => "MM",                     // Expiry month (2 digits)
          "ccexpyr" => "YY",                      // Expiry year (2 digits)
          "ccvv" => "CVV",                        // Card verification value
          "ccname" => "NAME_ON_CARD",             // Name on the card
          
          // Success and failure URLs
          "surl" => "https://yourwebsite.com/success", // Success callback URL
          "furl" => "https://yourwebsite.com/failure", // Failure callback URL
          
          // Hash is generated on server using specific algorithm provided by PayU
          // See PayU documentation for the exact hash generation logic
          "hash" => "HASH_GENERATED_ON_SERVER",   // Security hash
      ];
      
      // Initialize cURL session
      $ch = curl_init($url);
      
      // Set cURL options
      curl_setopt($ch, CURLOPT_POST, true);
      curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
      curl_setopt($ch, CURLOPT_HTTPHEADER, [
          "Content-Type: application/x-www-form-urlencoded"
      ]);
      
      // For additional security in production
      curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);
      curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
      
      // Execute the request
      $response = curl_exec($ch);
      $status_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
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
      
      // In production, implement proper response handling and logging
      // (but never log full card details)
      return [
          "status_code" => $status_code,
          "response" => $response
      ];
  }

  // Example usage:
  // $paymentResult = processPayment($paymentData);
  // echo "Status: " . $paymentResult["status_code"];
  // Process the response appropriately
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
   * PayU Payment Processor for Merchant Hosted Checkout
   * 
   * IMPORTANT: This is a server-side implementation. Never expose card details to client-side code.
   * This handles sensitive card data and requires PCI DSS compliance.
   */
  public class PayUPaymentProcessor {
      
      // API endpoints - Use different URLs for test/production environments
      private static final String TEST_URL = "https://test.payu.in/_payment";
      private static final String PROD_URL = "https://secure.payu.in/_payment";
      
      /**
       * Process payment using PayU Merchant Hosted Checkout
       * 
       * @return PaymentResponse containing status and response data
       */
      public PaymentResponse processPayment() {
          try {
              // Use test URL (change to PROD_URL in production)
              URL url = new URL(TEST_URL);
              
              // Prepare form parameters
              // In production: Get merchant_key and hash from secure environment variables
              Map<String, String> params = new HashMap<>();
              params.put("key", "YOUR_MERCHANT_KEY");           // Replace with actual merchant key
              params.put("txnid", "TXN_12345");                 // Generate unique transaction ID
              params.put("amount", "1000.00");                  // Amount to be charged
              params.put("productinfo", "Product Description"); // Description of product/service
              params.put("firstname", "Customer Name");         // Customer's first name
              params.put("email", "customer@example.com");      // Customer's email
              params.put("phone", "9988776655");                // Customer's phone number
              params.put("pg", "CC");                           // Payment gateway (CC for credit card)
              params.put("bankcode", "CC");                     // Bank code (CC for credit card)
              
              // SENSITIVE DATA - Handle with care according to PCI DSS requirements
              params.put("ccnum", "CARD_NUMBER");               // Credit card number
              params.put("ccexpmon", "MM");                     // Expiry month (2 digits)
              params.put("ccexpyr", "YY");                      // Expiry year (2 digits)
              params.put("ccvv", "CVV");                        // Card verification value
              params.put("ccname", "NAME_ON_CARD");             // Name on the card
              
              // Success and failure URLs
              params.put("surl", "https://yourwebsite.com/success"); // Success callback URL
              params.put("furl", "https://yourwebsite.com/failure"); // Failure callback URL
              
              // Hash is generated on server using specific algorithm provided by PayU
              // See PayU documentation for the exact hash generation logic
              params.put("hash", "HASH_GENERATED_ON_SERVER");   // Security hash
              
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
              
              // In production, implement proper response handling and logging
              // (but never log full card details)
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
      
      // Example usage:
      public static void main(String[] args) {
          PayUPaymentProcessor processor = new PayUPaymentProcessor();
          PaymentResponse result = processor.processPayment();
          
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

  namespace PayUIntegration
  {
      /// <summary>
      /// PayU Payment Processor for Merchant Hosted Checkout
      /// 
      /// IMPORTANT: This is a server-side implementation. Never expose card details to client-side code.
      /// This handles sensitive card data and requires PCI DSS compliance.
      /// </summary>
      public class PayUPaymentProcessor
      {
          // API endpoints - Use different URLs for test/production environments
          private const string TestUrl = "https://test.payu.in/_payment";
          private const string ProdUrl = "https://secure.payu.in/_payment";
          
          /// <summary>
          /// Process payment using PayU Merchant Hosted Checkout
          /// </summary>
          /// <returns>PaymentResponse containing status and response data</returns>
          public async Task<PaymentResponse> ProcessPaymentAsync()
          {
              try
              {
                  // Use test URL (change to ProdUrl in production)
                  string url = TestUrl;
                  
                  // Prepare form parameters
                  // In production: Get merchant_key and hash from secure environment variables
                  var formData = new Dictionary<string, string>
                  {
                      { "key", "YOUR_MERCHANT_KEY" },           // Replace with actual merchant key
                      { "txnid", "TXN_12345" },                 // Generate unique transaction ID
                      { "amount", "1000.00" },                  // Amount to be charged
                      { "productinfo", "Product Description" }, // Description of product/service
                      { "firstname", "Customer Name" },         // Customer's first name
                      { "email", "customer@example.com" },      // Customer's email
                      { "phone", "9988776655" },                // Customer's phone number
                      { "pg", "CC" },                           // Payment gateway (CC for credit card)
                      { "bankcode", "CC" },                     // Bank code (CC for credit card)
                      
                      // SENSITIVE DATA - Handle with care according to PCI DSS requirements
                      { "ccnum", "CARD_NUMBER" },               // Credit card number
                      { "ccexpmon", "MM" },                     // Expiry month (2 digits)
                      { "ccexpyr", "YY" },                      // Expiry year (2 digits)
                      { "ccvv", "CVV" },                        // Card verification value
                      { "ccname", "NAME_ON_CARD" },             // Name on the card
                      
                      // Success and failure URLs
                      { "surl", "https://yourwebsite.com/success" }, // Success callback URL
                      { "furl", "https://yourwebsite.com/failure" }, // Failure callback URL
                      
                      // Hash is generated on server using specific algorithm provided by PayU
                      // See PayU documentation for the exact hash generation logic
                      { "hash", "HASH_GENERATED_ON_SERVER" }    // Security hash
                  };
                  
                  // Create HttpClient with timeout
                  using (var httpClient = new HttpClient())
                  {
                      httpClient.Timeout = TimeSpan.FromSeconds(30);
                      
                      // Convert form data to content
                      var content = new FormUrlEncodedContent(formData);
                      
                      // Send POST request
                      var response = await httpClient.PostAsync(url, content);
                      
                      // Get response content
                      var responseContent = await response.Content.ReadAsStringAsync();
                      
                      // In production, implement proper response handling and logging
                      // (but never log full card details)
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
      
      // Example usage:
      public class Program
      {
          public static async Task Main(string[] args)
          {
              var processor = new PayUPaymentProcessor();
              var result = await processor.ProcessPaymentAsync();
              
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
</Accordion>

<Accordion title="Sample request for saved card" icon="fa-code">
  <Accordion title="Request parameters" icon="fa-info-table">
    <HTMLBlock>{`
                                                                                                                                                      <Table>
                                                                                                                                                        <thead>
                                                                                                                                                          <tr>
                                                                                                                                                            <th>
                                                                                                                                                              Parameter
                                                                                                                                                            </th>

                                                                                                                                                            <th>
                                                                                                                                                              Description
                                                                                                                                                            </th>

                                                                                                                                                            <th>
                                                                                                                                                              Example
                                                                                                                                                            </th>
                                                                                                                                                          </tr>
                                                                                                                                                        </thead>

                                                                                                                                                        <tbody>
                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              key
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> The merchant key is a unique identifier for a merchant account in PayU's database.
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              Your Test Key
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              api_version
                                                                                                                                                              <br/><code>optional</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> The API version for this API.
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              1
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              txnid
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> The transaction ID is a reference number for a specific order that is generated by the merchant. It is used to track the order and must be unique. PayU's system will not accept duplicate transaction IDs.
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              s7hhDQVWvbhBdN
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              amount
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> This field should contain the payment amount for the transaction. If you want to use the cardless EMI option, the amount must be at least Rs. 8000
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              10.00
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              productinfo
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> It should be a string containing a brief description of the product.\`\`\`

                                                                                                                                                              Character Limit-100
                                                                                                                                                              \`\`\`
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              iPhone
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              firstname
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> The first name of the customer.\`\`\`

                                                                                                                                                              Character Limit-60
                                                                                                                                                              \`\`\`
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              Ashish
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              email
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> The email of the customer.\`\`\`

                                                                                                                                                              Character Limit-50
                                                                                                                                                              \`\`\`
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              [test@gmail.com](mailto:test@gmail.com)
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              phone
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> The phone number of the customer.  

                                                                                                                                                              * \*Note\*\*: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              9876543210
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              lastname
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> The last name of the customer.\`\`\`

                                                                                                                                                              Character Limit-60
                                                                                                                                                              \`\`\`
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              Verma
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              address1
                                                                                                                                                              <br/><code>optional</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> The first line of the billing address.\`\`\`

                                                                                                                                                              Character Limit-100
                                                                                                                                                              \`\`\`
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              address2
                                                                                                                                                              <br/><code>optional</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> The second line of the billing address.<code>Character Limit-100</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              34 Saikripa-Estate, Tilak Nagar
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              city
                                                                                                                                                              <br/><code>optional</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> The city where your customer resides as part of the billing address.
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              Mumbai
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              state
                                                                                                                                                              <br/><code>optional</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> The state where your customer resides as part of the billing address,
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              Maharashtra
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              country
                                                                                                                                                              <br/><code>optional</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> The country where your customer resides.<code>Character Limit-50</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              India
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              zipcode
                                                                                                                                                              <br/><code>optional</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> Billing address zip code is mandatory for the cardless EMI option.\`\`\`

                                                                                                                                                              Character Limit-20
                                                                                                                                                              \`\`\`
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              400004
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              surl
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              furl
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              hash
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> It is used to avoid the possibility of transaction tampering. For more information on hash generation process, refer to [Generate Hash](doc:generate-hash-merchant-hosted).
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>eabec285da28fd 0e3054d41a4d24fe 9f7599c9d0b6664 6f7a9984303fd612 4044b6206daf831 e9a8bda28a6200d 318293a13d6c193 109b60bd4b4f8b09 c90972</code>
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              <Glossary>pg</Glossary>
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> The pg parameter determines which payment tabs will be displayed. Here, use 'CC' as the value.
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              CC
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              <Glossary>bankcode</Glossary>
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. 
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              AMEX
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              udf1 - udf5
                                                                                                                                                              <br/><code>optional</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
                                                                                                                                                              <code>Character Limit-255</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              Payment Preference, Shipping Method, Shipping Address1, Shipping City, Shipping Zip Code, etc.
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              ccnum
                                                                                                                                                              <br/><code>optional</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>varchar</code> This parameter must contain the 13 to 19-digit card number for credit or debit cards in general. 
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              512***6789012346
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              ccname
                                                                                                                                                              <br/><code>optional</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>varchar</code> It is the customer's name on card.
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              Ashish
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              ccvv
                                                                                                                                                              <br/><code>optional</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>varchar</code> This parameter must contain the CVV number of the card – as entered by the customer for the transaction.
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              123
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              ccexpmon
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>integer</code> This parameter must contain the network token expiry month.
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              10
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              ccexpyr
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>integer</code> This parameter must contain the network token expiry year.
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              2022
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              store_card_token
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>varchar</code> This must include the Network token generated at your end.
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              1234 4567 2456 3566
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              storecard_token_type
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>integer</code> This parameter is used to specify the store card token type. For this scenario, you must include 1.
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              1
                                                                                                                                                            </td>
                                                                                                                                                          </tr>

                                                                                                                                                          <tr>
                                                                                                                                                            <td>
                                                                                                                                                              additional_info
                                                                                                                                                              <br/><code>mandatory</code>
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              <code>varchar</code> This parameter will contain the additional information in the following JSON format:
                                                                                                                                                              {"last4Digits": "1234", "<Glossary>TAVV</Glossary>": "ABCDEFGH","<Glossary>trid</Glossary>":"1234567890", "<Glossary>tokenRefNo</Glossary>":"abcde123456"}  
                                                                                                                                                            </td>

                                                                                                                                                            <td>
                                                                                                                                                              {"last4Digits": "1234", "tavv": "ABCDEFGH","trid":"1234567890", "tokenRefNo":"abcde123456"}
                                                                                                                                                            </td>
                                                                                                                                                          </tr>
                                                                                                                                                        </tbody>
                                                                                                                                                      </Table>
    `}</HTMLBlock>
  </Accordion>

  <Accordion title="Collect Payment with Saved Card" icon="fa-code">
    ```curl
    curl -X POST "https://test.payu.in/_payment" \
      -H "accept: application/json" \
      -H "Content-Type: application/x-www-form-urlencoded" \
      -d "key=YourMerchantKey" \
      -d "txnid=NT_TXN_1234567890" \
      -d "amount=250.00" \
      -d "productinfo=Premium Subscription Plan" \
      -d "firstname=John" \
      -d "lastname=Doe" \
      -d "email=john.doe@example.com" \
      -d "phone=9876543210" \
      -d "surl=https://yourwebsite.com/payment/success" \
      -d "furl=https://yourwebsite.com/payment/failure" \
      -d "pg=CC" \
      -d "bankcode=VISA" \
      -d "ccexpmon=12" \
      -d "ccexpyr=2025" \
      -d "ccname=John Doe" \
      -d "store_card_token=4111111111111111" \
      -d "storecard_token_type=1" \
      -d "additional_info={\"last4Digits\":\"1111\",\"TAVV\":\"ABCD1234EFGH5678\",\"trid\":\"987654321012345\",\"tokenRefNo\":\"TKN_REF_12345678\"}" \
      -d "api_version=1" \
      -d "address1=123 Business District" \
      -d "address2=Tech Park Avenue" \
      -d "city=Bangalore" \
      -d "state=Karnataka" \
      -d "country=India" \
      -d "zipcode=560001" \
      -d "udf1=Premium_Plan" \
      -d "udf2=Monthly_Billing" \
      -d "udf3=Customer_ID_789" \
      -d "udf4=" \
      -d "udf5=" \
      -d "hash=b5c6d8e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9"

    ```

    <br />
  </Accordion>
</Accordion>

## Step 3: Check response from PayU

<ReverseHashing />

<Accordion title="Sample response (parsed)" icon="fa-code">
  * Success scenario

  ```
  Array
  (
      [mihpayid] => 403993715524069222
      [mode] => CC
      [status] => success
      [unmappedstatus] => captured
      [key] => JF***g
      [txnid] => EaE4ZO3vU4iPsp
      [amount] => 10.00
      [cardCategory] => domestic
      [discount] => 0.00
      [net_amount_debit] => 10
      [addedon] => 2021-09-08 19:37:19
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
      [hash] => ed99957adb08fea56c907b88e8d158a79c3562c67f96c298461509826f77a7ae9e88b2a176b3234c25f50bcd451271728719656f3bb59c13a52bebabc468615a
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
      [PG_TYPE] => CC-PG
      [bank_ref_num] => 0608273386032718000015
      [bankcode] => CC
      [error] => E000
      [error_Message] => No Error
      [name_on_card] => payu
      [cardnum] => 512345XXXXXX2346
  )
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
