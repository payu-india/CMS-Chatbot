---
title: Merchant Hosted Integration - COPY
deprecated: false
hidden: true
metadata:
  robots: index
---
# What you're building

A custom payment experience where you collect payment details on your own website and securely process them through PayU's APIs. Unlike the hosted solution, you have complete control over the UI/UX while PayU handles the secure payment processing. You pass order details, customer information, payment method-specific parameters (pg, bankcode), and a server-generated SHA-512 hash for integrity.

The PayU Merchant Hosted (Custom Checkout) integration involves the following steps:

<Cards columns={3}>
  <Card title="1. Start Integration" href="#step-1-start-integration" target="_blank" className="bg-blue text-white shadow-lg rounded-xl border-0">
    Build custom payment forms and integrate with PayU APIs
  </Card>

  <Card title="2. Test Integration" href="#step-2-test-integration" className="bg-teal text-white shadow-lg rounded-xl border-0">
    Test different payment modes with sandbox credentials
  </Card>

  <Card title="3. Go live Checklist" href="#step-3-going-live-your-final-checklist" className="bg-indigo text-white shadow-lg rounded-xl border-0">
    Complete security requirements and go live
  </Card>
</Cards>

<Callout icon="📘" theme="info">
  **Pre-requisites**

  * Merchant Key and Salt (test or production)
  * HTTPS success & failure URLs (surl, furl) reachable from the public internet
  * Ability to generate SHA-512 on the server (never in the browser)
  * Order ID generator for unique txnid
  * **PCI DSS compliance** if handling card data directly
  * SSL certificate for secure data transmission
</Callout>

<Callout icon="⚠️" theme="warning">
  **Security Requirements**

  * **PCI DSS Compliance**: Required when collecting card details on your website
  * **Never store sensitive payment data** like CVV, card numbers, or PINs
  * **Use HTTPS** for all payment-related communications
  * **Validate all inputs** on both client and server side
</Callout>

<Accordion title="Environment" icon="fa-globe">
  **Environment URLs**

  |                        |                                                                     |
  | :--------------------- | :------------------------------------------------------------------ |
  | Test Environment       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
  | Production Environment | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |
</Accordion>

## Step 1: Start Integration

Follow the below steps to complete the integration:

<Accordion title="Step 1.1: Validate Inputs" icon="fa-list-check">
<Tabs>
  <Tab title="💳 Cards">
    ## Check if Card is Domestic API
    Determines whether a card BIN (the first 6 digits of a card) corresponds to a domestic or international card, and provides additional information about the card including issuing bank, card type, and category.

    **Environment**  
    | Environment | URL |
    |-------------|-----|
    | Test | `https://test.payu.in/merchant/postservice.php?form=2` |
    | Production | `https://info.payu.in/merchant/postservice?form=2` |

    **Sample Request**  
    ```bash
    curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=&lt;Merchant_Key&gt;&command=check_isDomestic&var1=462273&hash=&lt;Generated_Hash&gt;"
    ```
    **Sample Response**  
    ```json
    {
      "isDomestic": "Y",
      "issuingBank": "SCB",
      "cardType": "VISA",
      "cardCategory": "CC"
    }
    ```
  </Tab>

  <Tab title="🏦 Net Banking">
    ## Get Net Banking Status API
    Provides detailed information about the availability (up or down status) of specific or all Net Banking options to help merchants handle bank downtime issues and ensure seamless user transactions.

    **Environment**  
    | Environment | URL |
    |-------------|-----|
    | Test | `https://test.payu.in/merchant/postservice.php?form=2` |
    | Production | `https://info.payu.in/merchant/postservice?form=2` |

    **Sample Request**  
    ```bash
    curl -X POST "https://test.payu.in/merchant/postservice.php?form=2" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JP***g&command=getNetbankingStatus&var1=AXIB&hash=&lt;Generated_Hash&gt;"
    ```

    **Sample Response**  
    ```json
    {
      "ibibo_code": "AXIB",
      "title": "AXIS Bank NetBanking",
      "up_status": 0,
      "mode": "NB"
    }
    ```
  </Tab>

  <Tab title="📱 UPI">
    ## Validate VPA API
    Validates Virtual Payment Address (VPA) to check if it's valid for transactions. Also checks eligibility for UPI recurring payments/autopay functionality.

    **Environment**  
    | Environment | URL |
    |-------------|-----|
    | Test | `https://test.payu.in/merchant/postservice.php?form=2` |

    **Sample Request**  
    ```bash
    curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JP***g&command=validateVPA&var1=9999999999@upi&hash=&lt;Generated_Hash&gt;"
    ```

    **Sample Response**  
    ```json
    {
      "status": "SUCCESS",
      "vpa": "9999999999@upi",
      "isVPAValid": 1,
      "isAutoPayVPAValid": 1,
      "isAutoPayBankValid": "NA",
      "payerAccountName": "ABC"
    }
    ```
  </Tab>

  <Tab title="💰 EMI">
    ## Eligible BINs for EMI API
    
    Determines the eligibility of a card BIN for EMI offers, provides issuing bank details, and retrieves minimum transaction amount required for EMI.

    **Environment**  
    HTTP POST request (specific URLs not explicitly mentioned in documentation)

    **Sample Request**  
    **Headers:**
    - `Date`: Current date/time in GMT format
    - `Digest`: Base64 encoded SHA-256 hash of request body
    - `Authorization`: HMAC authorization with merchant key
    - `platformId`: `1`

    **Request Body:**
    ```json
    {
      "bintype": "bin",
      "value": "4161041969147181",
      "amount": "10000",
      "bank": "ICICI"
    }
    ```

    **Sample Response**  
    ```json
    {
      "message": "Details fetched successfully",
      "status": 1,
      "result": [
        {
          "isEligible": 1,
          "bank": "ICICI",
          "minAmount": 1500.0
        }
      ]
    }
    ```
  </Tab>

  <Tab title="📅 BNPL">
    ## Get Checkout Details API
    Provides comprehensive checkout details including payment options, eligibility for BNPL, EMI options, additional charges, downtime information, and recommendations to create custom payment pages.

    **Environment**  
    | Environment | URL |
    |-------------|-----|
    | Test | `https://test.payu.in/merchant/postservice?form=2` |
    | Production | `https://info.payu.in/merchant/postservice?form=2` |

    **Sample Request**  
    ```bash
    curl --location 'https://info.payu.in/merchant/postservice.php?form=2' \
    --form 'key="merchant_key"' \
    --form 'command="get_checkout_details"' \
    --form 'var1="{\"requestId\":\"9920371372_38\",\"transactionDetails\":{\"amount\":8000},\"useCase\":{\"getExtendedPaymentDetails\":true}}"' \
    --form 'hash="&lt;Generated_Hash&gt;"'
    ```

    **Sample Response**  
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
                  "HDFC": {
                    "title": "HDFC Bank",
                    "minimumAmount": 1000,
                    "eligibility": { "status": true },
                    "tenureOptions": {
                      "HDFC12": { 
                        "tenure": 12, 
                        "interestRate": 10.5, 
                        "eligibility": { "status": true } 
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "downInfo": {
          "issuingBanks": [ "HDFC", "ICICI" ],
          "nb": ["SBIB", "ANDB"]
        },
        "config": {
          "taxSpecification": {
            "default": 18
          }
        }
      }
    }
    ```
  </Tab>
</Tabs>
</Accordion>

<Accordion title="Step 1.2: Prepare the request parameters" icon="fa-cogs">
  **Common Parameters (Required for all payment modes)**

  <HTMLBlock>{`
                                                  <div>
                                                    <table>
                                                      <thead>
                                                        <tr>
                                                          <th style="width: 10%;">Parameter</th>
                                                          <th style="width: 75%; white-space: normal; word-break: break-word;">Type & Description</th>
                                                          <th style="width: 15%;">Example</th>
                                                        </tr>
                                                      </thead>
                                                      <tbody>
                                                        <tr>
                                                          <td>
                                                            key<br>
                                                            <code>mandatory</code>
                                                          </td>
                                                          <td style="white-space: normal; word-break: break-word;">
                                                            <code>String</code> Merchant key provided by PayU during onboarding.
                                                          </td>
                                                          <td>JPG****.k</td>
                                                        </tr>
                                                        <tr>
                                                          <td>
                                                            txnid<br>
                                                            <code>mandatory</code>
                                                          </td>
                                                          <td style="white-space: normal; word-break: break-word;">
                                                            <code>String</code> The transaction ID is a reference number for a specific order generated by the merchant.
                                                          </td>
                                                          <td>ypl938459435</td>
                                                        </tr>
                                                        <tr>
                                                          <td>
                                                            amount<br>
                                                            <code>mandatory</code>
                                                          </td>
                                                          <td style="white-space: normal; word-break: break-word;">
                                                            <code>String</code> The payment amount for the transaction.
                                                          </td>
                                                          <td>10.00</td>
                                                        </tr>
                                                        <tr>
                                                          <td>
                                                            productinfo<br>
                                                            <code>mandatory</code>
                                                          </td>
                                                          <td style="white-space: normal; word-break: break-word;">
                                                            <code>String</code> A brief description of the product.
                                                          </td>
                                                          <td>iPhone</td>
                                                        </tr>
                                                        <tr>
                                                          <td>
                                                            firstname<br>
                                                            <code>mandatory</code>
                                                          </td>
                                                          <td style="white-space: normal; word-break: break-word;">
                                                            <code>String</code> The first name of the customer.
                                                          </td>
                                                          <td>Ashish</td>
                                                        </tr>
                                                        <tr>
                                                          <td>
                                                            email<br>
                                                            <code>mandatory</code>
                                                          </td>
                                                          <td style="white-space: normal; word-break: break-word;">
                                                            <code>String</code> The email address of the customer.
                                                          </td>
                                                          <td>test@payu.in</td>
                                                        </tr>
                                                        <tr>
                                                          <td>
                                                            phone<br>
                                                            <code>mandatory</code>
                                                          </td>
                                                          <td style="white-space: normal; word-break: break-word;">
                                                            <code>String</code> The phone number of the customer.
                                                          </td>
                                                          <td>9876543210</td>
                                                        </tr>
                                                        <tr>
                                                          <td>
                                                            pg<br>
                                                            <code>mandatory</code>
                                                          </td>
                                                          <td style="white-space: normal; word-break: break-word;">
                                                            <code>String</code> Payment gateway/method identifier. <strong>This is the key difference from hosted checkout.</strong>
                                                          </td>
                                                          <td>CC, NB, UPI, CASH</td>
                                                        </tr>
                                                        <tr>
                                                          <td>
                                                            bankcode<br>
                                                            <code>conditional</code>
                                                          </td>
                                                          <td style="white-space: normal; word-break: break-word;">
                                                            <code>String</code> Bank or payment provider specific code. Required for specific payment methods.
                                                          </td>
                                                          <td>HDFC, PAYTM, UPI</td>
                                                        </tr>
                                                        <tr>
                                                          <td>
                                                            surl<br>
                                                            <code>mandatory</code>
                                                          </td>
                                                          <td style="white-space: normal; word-break: break-word;">
                                                            <code>String</code> The success URL, which is the page PayU will redirect to if the transaction is successful.
                                                          </td>
                                                          <td>https://yoursite.com/success</td>
                                                        </tr>
                                                        <tr>
                                                          <td>
                                                            furl<br>
                                                            <code>mandatory</code>
                                                          </td>
                                                          <td style="white-space: normal; word-break: break-word;">
                                                            <code>String</code> The failure URL, which is the page PayU will redirect to if the transaction fails.
                                                          </td>
                                                          <td>https://yoursite.com/failure</td>
                                                        </tr>
                                                        <tr>
                                                          <td>
                                                            hash<br>
                                                            <code>mandatory</code>
                                                          </td>
                                                          <td style="white-space: normal; word-break: break-word;">
                                                            <code>String</code> It is the hash calculated by the merchant using SHA-512.
                                                          </td>
                                                          <td>[computed hash]</td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                  </div>
  `}</HTMLBlock>

  ## Payment Method Specific Parameters

  <Tabs>
    <Tab title="💳 Cards">
      **Additional Parameters for Card Payments**

      | Parameter | Type   | Description                    | Example                                   |
      | --------- | ------ | ------------------------------ | ----------------------------------------- |
      | pg        | String | Payment gateway (mandatory)    | `CC`                                      |
      | bankcode  | String | Card type identifier           | `VISA`, `MAST`, `AMEX`, `DINERS`, `RUPAY` |
      | ccnum     | String | 13-19 digit card number        | `4111111111111111`                        |
      | ccname    | String | Name on card                   | `John Doe`                                |
      | ccvv      | String | 3-digit CVV (4-digit for AMEX) | `123`                                     |
      | ccexpmon  | String | Card expiry month (MM)         | `12`                                      |
      | ccexpyr   | String | Card expiry year (YYYY)        | `2025`                                    |

      **Sample Card Payment Request**

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
              public async Task&lt;PaymentResponse&gt; ProcessPaymentAsync()
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

      **Important Security Notes:**

      * PCI DSS compliance mandatory
      * Use LUHN algorithm for card validation
      * 3D Secure authentication required
      * Never store card details on your server
    </Tab>

    <Tab title="🏦 Net Banking">
      **Additional Parameters for Net Banking**

      | Parameter | Type   | Description                 | Example                        |
      | --------- | ------ | --------------------------- | ------------------------------ |
      | pg        | String | Payment gateway (mandatory) | `NB`                           |
      | bankcode  | String | Bank identifier code        | `HDFC`, `ICICI`, `SBI`, `AXIS` |

      **Popular Bank Codes**

      | Bank Name            | Bank Code  |
      | -------------------- | ---------- |
      | HDFC Bank            | `HDFC`     |
      | ICICI Bank           | `ICICI`    |
      | State Bank of India  | `SBI`      |
      | Axis Bank            | `AXIS`     |
      | Punjab National Bank | `PNB`      |
      | Kotak Mahindra Bank  | `KOTAK`    |
      | Yes Bank             | `YES`      |
      | Test Environment     | `TESTPGNB` |

      **Sample Net Banking Request**

      ```curl
      curl -X \
       POST "https://test.payu.in/_payment" -H \
       "accept: application/json" -H \
       "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=ewP8oRopzdHEtC&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=TESTPG&bankcode=TESTPGNB&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
      ```
      ```javascript
      /**
       * PayU Payment Request using Fetch API
       * 
       * IMPORTANT: This should only be executed server-side, never in the browser,
       * as it contains sensitive payment information.
       */

      // Payment endpoint
      const url = 'https://test.payu.in/_payment';

      // Form data parameters
      const formData = new URLSearchParams();
      formData.append('key', 'JP***g');
      formData.append('txnid', 'ewP8oRopzdHEtC');
      formData.append('amount', '10.00');
      formData.append('firstname', 'Ashish');
      formData.append('email', 'test@gmail.com');
      formData.append('phone', '9876543210');
      formData.append('productinfo', 'iPhone');
      formData.append('pg', 'TESTPG');
      formData.append('bankcode', 'TESTPGNB');
      formData.append('surl', 'https://apiplayground-response.herokuapp.com/');
      formData.append('furl', 'https://apiplayground-response.herokuapp.com/');
      formData.append('hash', 'bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319');

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
        })
        .catch(error => {
          console.error('Error:', error);
        });

      ```
      ```python
      import urllib.request
      import urllib.parse

      url = "https://test.payu.in/_payment"

      headers = {
          "accept": "application/json",
          "Content-Type": "application/x-www-form-urlencoded"
      }

      payload = {
          "key": "JP***g",
          "txnid": "ewP8oRopzdHEtC",
          "amount": "10.00",
          "firstname": "Ashish",
          "email": "test@gmail.com",
          "phone": "9876543210",
          "productinfo": "iPhone",
          "pg": "TESTPG",
          "bankcode": "TESTPGNB",
          "surl": "https://apiplayground-response.herokuapp.com/",
          "furl": "https://apiplayground-response.herokuapp.com/",
          "hash": "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
      }

      data = urllib.parse.urlencode(payload).encode('utf-8')
      req = urllib.request.Request(url, data=data, headers=headers, method="POST")

      try:
          with urllib.request.urlopen(req) as response:
              response_body = response.read().decode('utf-8')
              print("Status Code:", response.getcode())
              print("Response:")
              print(response_body)
      except urllib.error.HTTPError as e:
          print("Error:", e.code, e.reason)
          print(e.read().decode('utf-8'))

      ```
      ```php
      <?php
      // PayU Payment Gateway API Request

      // Set the API endpoint
      $url = "https://test.payu.in/_payment";

      // Prepare the form data
      $postData = array(
          'key' => 'JP***g',
          'txnid' => 'ewP8oRopzdHEtC',
          'amount' => '10.00',
          'firstname' => 'Ashish',
          'email' => 'test@gmail.com',
          'phone' => '9876543210',
          'productinfo' => 'iPhone',
          'pg' => 'TESTPG',
          'bankcode' => 'TESTPGNB',
          'surl' => 'https://apiplayground-response.herokuapp.com/',
          'furl' => 'https://apiplayground-response.herokuapp.com/',
          'hash' => 'bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319'
      );

      // Initialize cURL session
      $ch = curl_init();

      // Set cURL options
      curl_setopt($ch, CURLOPT_URL, $url);
      curl_setopt($ch, CURLOPT_POST, true);
      curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
      curl_setopt($ch, CURLOPT_HTTPHEADER, array(
          'Accept: application/json',
          'Content-Type: application/x-www-form-urlencoded'
      ));

      // Optional: Disable SSL verification for testing (not recommended for production)
      // curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
      // curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);

      // Execute the request
      $response = curl_exec($ch);

      // Check for cURL errors
      if (curl_errno($ch)) {
          echo 'cURL Error: ' . curl_error($ch);
      } else {
          // Get HTTP status code
          $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
          echo "HTTP Status Code: " . $httpCode . "\n";
          echo "Response: " . $response . "\n";
      }

      // Close cURL session
      curl_close($ch);

      // Optional: Parse JSON response if needed
      $responseData = json_decode($response, true);
      if ($responseData !== null) {
          echo "Parsed Response:\n";
          print_r($responseData);
      }
      ?>

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

      public class PayUPaymentRequest {
          
          public static void main(String[] args) {
              try {
                  // API endpoint
                  String url = "https://test.payu.in/_payment";
                  
                  // Form parameters
                  Map<String, String> params = new HashMap<>();
                  params.put("key", "JP***g");
                  params.put("txnid", "ewP8oRopzdHEtC");
                  params.put("amount", "10.00");
                  params.put("firstname", "Ashish");
                  params.put("email", "test@gmail.com");
                  params.put("phone", "9876543210");
                  params.put("productinfo", "iPhone");
                  params.put("pg", "TESTPG");
                  params.put("bankcode", "TESTPGNB");
                  params.put("surl", "https://apiplayground-response.herokuapp.com/");
                  params.put("furl", "https://apiplayground-response.herokuapp.com/");
                  params.put("hash", "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319");
                  
                  // Convert parameters to URL encoded form data
                  StringJoiner sj = new StringJoiner("&");
                  for (Map.Entry<String, String> entry : params.entrySet()) {
                      sj.add(URLEncoder.encode(entry.getKey(), "UTF-8") + "="
                           + URLEncoder.encode(entry.getValue(), "UTF-8"));
                  }
                  byte[] postData = sj.toString().getBytes(StandardCharsets.UTF_8);
                  
                  // Create connection
                  URL apiUrl = new URL(url);
                  HttpURLConnection conn = (HttpURLConnection) apiUrl.openConnection();
                  conn.setRequestMethod("POST");
                  conn.setRequestProperty("accept", "application/json");
                  conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
                  conn.setRequestProperty("Content-Length", String.valueOf(postData.length));
                  conn.setDoOutput(true);
                  
                  // Send request
                  try (DataOutputStream dos = new DataOutputStream(conn.getOutputStream())) {
                      dos.write(postData);
                  }
                  
                  // Read response
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
    </Tab>

    <Tab title="📱 UPI">
      **Additional Parameters for UPI Payments**

      | Parameter | Type   | Description                 | Example          |
      | --------- | ------ | --------------------------- | ---------------- |
      | pg        | String | Payment gateway (mandatory) | `UPI`            |
      | bankcode  | String | UPI identifier              | `UPI`            |
      | vpa       | String | Virtual Payment Address     | `customer@paytm` |

      **UPI Flows Supported:**

      * Collect Flow (VPA-based)
      * Intent Flow (App-based)
      * Smart Intent Flow

      **Sample UPI Request**

      ```curl
      curl -X \
       POST "https://test.payu.in/_payment" -H \
       "accept: application/json" -H \
       "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=xdB9G7qYpfqszo&amount=10&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=UPI&bankcode=UPI&vpa=VPA-anything@payu&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb"
      ```
      ```javascript
      /**
       * PayU UPI Payment Integration using Fetch API
       * 
       * IMPORTANT: This should only be executed server-side (e.g., in Node.js), never in the browser,
       * as it contains sensitive payment information.
       */

      // Payment endpoint
      const url = 'https://test.payu.in/_payment';

      // Form data parameters
      const formData = new URLSearchParams();
      formData.append('key', 'JP***g');
      formData.append('txnid', 'xdB9G7qYpfqszo');
      formData.append('amount', '10');
      formData.append('firstname', 'PayU User');
      formData.append('email', 'test@gmail.com');
      formData.append('phone', '9876543210');
      formData.append('productinfo', 'iPhone');
      formData.append('pg', 'UPI');
      formData.append('bankcode', 'UPI');
      formData.append('vpa', 'VPA-anything@payu');
      formData.append('surl', 'https://apiplayground-response.herokuapp.com/');
      formData.append('furl', 'https://apiplayground-response.herokuapp.com/');
      formData.append('hash', '649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb');

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

      def process_upi_payment() -> Dict[str, Any]:
          """
          Process UPI payment using PayU's Merchant Hosted Checkout
          
          IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
          
          Returns:
              Dictionary with response from PayU API
          """
          # API endpoint
          url = "https://test.payu.in/_payment"
          
          # Prepare the form data
          payload = {
              "key": "JP***g",                   # Replace with actual merchant key
              "txnid": "xdB9G7qYpfqszo",         # Generate unique transaction ID
              "amount": "10",                    # Amount to be charged
              "firstname": "PayU User",          # Customer's name
              "email": "test@gmail.com",         # Customer's email
              "phone": "9876543210",             # Customer's phone number
              "productinfo": "iPhone",           # Description of product/service
              "pg": "UPI",                       # Payment gateway (UPI)
              "bankcode": "UPI",                 # Bank code (UPI)
              "vpa": "VPA-anything@payu",        # UPI Virtual Payment Address
              "surl": "https://apiplayground-response.herokuapp.com/", # Success callback URL
              "furl": "https://apiplayground-response.herokuapp.com/", # Failure callback URL
              "hash": "649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb" # Security hash
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
          result = process_upi_payment()
          print(f"Status Code: {result['status_code']}")
          if 'error' in result:
              print(f"Error: {result['error']}")
          print(f"Response: {result['response']}")

      ```
      ```php
      <?php
      /**
       * Process UPI payment using PayU's Merchant Hosted Checkout
       * 
       * IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
       * 
       * @return array Response from PayU API
       */
      function processUpiPayment() {
          // API endpoint
          $url = "https://test.payu.in/_payment";
          
          // Prepare the form data
          $payload = [
              "key" => "JP***g",                    // Replace with actual merchant key
              "txnid" => "xdB9G7qYpfqszo",          // Generate unique transaction ID
              "amount" => "10",                     // Amount to be charged
              "firstname" => "PayU User",           // Customer's name
              "email" => "test@gmail.com",          // Customer's email
              "phone" => "9876543210",              // Customer's phone number
              "productinfo" => "iPhone",            // Description of product/service
              "pg" => "UPI",                        // Payment gateway (UPI)
              "bankcode" => "UPI",                  // Bank code (UPI)
              "vpa" => "VPA-anything@payu",         // UPI Virtual Payment Address
              "surl" => "https://apiplayground-response.herokuapp.com/", // Success callback URL
              "furl" => "https://apiplayground-response.herokuapp.com/", // Failure callback URL
              "hash" => "649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb" // Security hash
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
      $result = processUpiPayment();
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
       * PayU UPI Payment Processor for Merchant Hosted Checkout
       * 
       * IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
       */
      public class PayUUpiPaymentProcessor {
          
          // API endpoint
          private static final String PAYU_TEST_URL = "https://test.payu.in/_payment";
          
          /**
           * Process UPI payment through PayU
           * @return PaymentResponse containing status and response data
           */
          public PaymentResponse processUpiPayment() {
              try {
                  // Initialize URL
                  URL url = new URL(PAYU_TEST_URL);
                  
                  // Prepare form parameters
                  Map<String, String> params = new HashMap<>();
                  params.put("key", "JP***g");                    // Replace with actual merchant key
                  params.put("txnid", "xdB9G7qYpfqszo");          // Generate unique transaction ID
                  params.put("amount", "10");                     // Amount to be charged
                  params.put("firstname", "PayU User");           // Customer's name
                  params.put("email", "test@gmail.com");          // Customer's email
                  params.put("phone", "9876543210");              // Customer's phone number
                  params.put("productinfo", "iPhone");            // Description of product/service
                  params.put("pg", "UPI");                        // Payment gateway (UPI)
                  params.put("bankcode", "UPI");                  // Bank code (UPI)
                  params.put("vpa", "VPA-anything@payu");         // UPI Virtual Payment Address
                  params.put("surl", "https://apiplayground-response.herokuapp.com/"); // Success callback URL
                  params.put("furl", "https://apiplayground-response.herokuapp.com/"); // Failure callback URL
                  params.put("hash", "649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb"); // Security hash
                  
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
              PayUUpiPaymentProcessor processor = new PayUUpiPaymentProcessor();
              PaymentResponse result = processor.processUpiPayment();
              
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

      namespace PayUUpiIntegration
      {
          /// <summary>
          /// PayU UPI Payment Processor for Merchant Hosted Checkout
          /// 
          /// IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
          /// </summary>
          public class PayUUpiPaymentProcessor
          {
              // API endpoint
              private const string PayuTestUrl = "https://test.payu.in/_payment";
              
              /// <summary>
              /// Process UPI payment through PayU
              /// </summary>
              /// <returns>PaymentResponse containing status and response data</returns>
              public async Task&lt;PaymentResponse&gt; ProcessUpiPaymentAsync()
              {
                  try
                  {
                      // Prepare form parameters
                      var formData = new Dictionary<string, string>
                      {
                          { "key", "JP***g" },                     // Replace with actual merchant key
                          { "txnid", "xdB9G7qYpfqszo" },           // Generate unique transaction ID
                          { "amount", "10" },                      // Amount to be charged
                          { "firstname", "PayU User" },            // Customer's name
                          { "email", "test@gmail.com" },           // Customer's email
                          { "phone", "9876543210" },               // Customer's phone number
                          { "productinfo", "iPhone" },             // Description of product/service
                          { "pg", "UPI" },                         // Payment gateway (UPI)
                          { "bankcode", "UPI" },                   // Bank code (UPI)
                          { "vpa", "VPA-anything@payu" },          // UPI Virtual Payment Address
                          { "surl", "https://apiplayground-response.herokuapp.com/" }, // Success callback URL
                          { "furl", "https://apiplayground-response.herokuapp.com/" }, // Failure callback URL
                          { "hash", "649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb" } // Security hash
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
                  var processor = new PayUUpiPaymentProcessor();
                  var result = await processor.ProcessUpiPaymentAsync();
                  
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

    <Tab title="👛 Wallets">
      **Additional Parameters for Wallet Payments**

      | Parameter | Type   | Description                 | Example                          |
      | --------- | ------ | --------------------------- | -------------------------------- |
      | pg        | String | Payment gateway (mandatory) | `CASH`                           |
      | bankcode  | String | Wallet provider code        | `PAYTM`, `PHONEPE`, `FREECHARGE` |

      **Supported Wallet Codes**

      | Wallet Name | Bank Code    |
      | ----------- | ------------ |
      | PayTM       | `PAYTM`      |
      | PhonePe     | `PHONEPE`    |
      | Mobikwik    | `MOBIKWIK`   |
      | FreeCharge  | `FREECHARGE` |
      | Ola Money   | `OLA`        |
      | Amazon Pay  | `AMAZONPAY`  |
      | JioMoney    | `JIO`        |

      **Sample Wallet Request**

      ```curl
      curl -X \
       POST "https://test.payu.in/_payment-H "accept: application/json" -H \
       "Content-Type: application/x-www-form-urlencoded" -d"key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cash&bankcode=paytm&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
      ```
      ```javascript
      /**
       * PayU Wallet (Paytm) Payment Integration using Fetch API
       * 
       * IMPORTANT: This should only be executed server-side (e.g., in Node.js), never in the browser,
       * as it contains sensitive payment information.
       */

      // Payment endpoint
      const url = 'https://test.payu.in/_payment';

      // Form data parameters
      const formData = new URLSearchParams();
      formData.append('key', 'J****g');                 // Replace with your actual merchant key
      formData.append('txnid', 'aI1UM19ONxLgPz');      // Transaction ID (unique for each transaction)
      formData.append('amount', '10.00');              // Payment amount
      formData.append('firstname', 'Ashish');          // Customer's name
      formData.append('email', 'test@gmail.com');      // Customer's email
      formData.append('phone', '9876543210');          // Customer's phone number
      formData.append('productinfo', 'iPhone');        // Product information
      formData.append('pg', 'cash');                   // Payment gateway type (cash for wallets)
      formData.append('bankcode', 'paytm');            // Wallet provider (paytm in this case)
      formData.append('surl', 'https://apiplayground-response.herokuapp.com/'); // Success URL
      formData.append('furl', 'https://apiplayground-response.herokuapp.com/'); // Failure URL
      formData.append('hash', '6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa'); // Security hash

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

      def process_wallet_payment() -> Dict[str, Any]:
          """
          Process wallet payment using PayU's Merchant Hosted Checkout (Paytm wallet)
          
          IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
          
          Returns:
              Dictionary with response from PayU API
          """
          # API endpoint
          url = "https://test.payu.in/_payment"
          
          # Prepare the form data
          payload = {
              "key": "J****g",                   # Replace with your actual merchant key
              "txnid": "aI1UM19ONxLgPz",         # Transaction ID (unique for each transaction)
              "amount": "10.00",                 # Payment amount
              "firstname": "Ashish",             # Customer's name
              "email": "test@gmail.com",         # Customer's email
              "phone": "9876543210",             # Customer's phone number
              "productinfo": "iPhone",           # Product information
              "pg": "cash",                      # Payment gateway type (cash for wallets)
              "bankcode": "paytm",               # Wallet provider (paytm in this case)
              "surl": "https://apiplayground-response.herokuapp.com/", # Success URL
              "furl": "https://apiplayground-response.herokuapp.com/", # Failure URL
              "hash": "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa" # Security hash
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
          result = process_wallet_payment()
          print(f"Status Code: {result['status_code']}")
          if 'error' in result:
              print(f"Error: {result['error']}")
          print(f"Response: {result['response']}")

      ```
      ```php
      <?php
      /**
       * Process wallet payment using PayU's Merchant Hosted Checkout (Paytm wallet)
       * 
       * IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
       * 
       * @return array Response from PayU API
       */
      function processWalletPayment() {
          // API endpoint
          $url = "https://test.payu.in/_payment";
          
          // Prepare the form data
          $payload = [
              "key" => "J****g",                    // Replace with your actual merchant key
              "txnid" => "aI1UM19ONxLgPz",          // Transaction ID (unique for each transaction)
              "amount" => "10.00",                  // Payment amount
              "firstname" => "Ashish",              // Customer's name
              "email" => "test@gmail.com",          // Customer's email
              "phone" => "9876543210",              // Customer's phone number
              "productinfo" => "iPhone",            // Product information
              "pg" => "cash",                       // Payment gateway type (cash for wallets)
              "bankcode" => "paytm",                // Wallet provider (paytm in this case)
              "surl" => "https://apiplayground-response.herokuapp.com/", // Success URL
              "furl" => "https://apiplayground-response.herokuapp.com/", // Failure URL
              "hash" => "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa" // Security hash
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
      $result = processWalletPayment();
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
       * PayU Wallet Payment Processor for Merchant Hosted Checkout (Paytm)
       * 
       * IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
       */
      public class PayUWalletPaymentProcessor {
          
          // API endpoint
          private static final String PAYU_TEST_URL = "https://test.payu.in/_payment";
          
          /**
           * Process wallet payment through PayU
           * @return PaymentResponse containing status and response data
           */
          public PaymentResponse processWalletPayment() {
              try {
                  // Initialize URL
                  URL url = new URL(PAYU_TEST_URL);
                  
                  // Prepare form parameters
                  Map<String, String> params = new HashMap<>();
                  params.put("key", "J****g");                    // Replace with your actual merchant key
                  params.put("txnid", "aI1UM19ONxLgPz");          // Transaction ID (unique for each transaction)
                  params.put("amount", "10.00");                  // Payment amount
                  params.put("firstname", "Ashish");              // Customer's name
                  params.put("email", "test@gmail.com");          // Customer's email
                  params.put("phone", "9876543210");              // Customer's phone number
                  params.put("productinfo", "iPhone");            // Product information
                  params.put("pg", "cash");                       // Payment gateway type (cash for wallets)
                  params.put("bankcode", "paytm");                // Wallet provider (paytm in this case)
                  params.put("surl", "https://apiplayground-response.herokuapp.com/"); // Success URL
                  params.put("furl", "https://apiplayground-response.herokuapp.com/"); // Failure URL
                  params.put("hash", "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"); // Security hash
                  
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
              PayUWalletPaymentProcessor processor = new PayUWalletPaymentProcessor();
              PaymentResponse result = processor.processWalletPayment();
              
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

      namespace PayUWalletIntegration
      {
          /// <summary>
          /// PayU Wallet Payment Processor for Merchant Hosted Checkout (Paytm)
          /// 
          /// IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
          /// </summary>
          public class PayUWalletPaymentProcessor
          {
              // API endpoint
              private const string PayuTestUrl = "https://test.payu.in/_payment";
              
              /// <summary>
              /// Process wallet payment through PayU
              /// </summary>
              /// <returns>PaymentResponse containing status and response data</returns>
              public async Task&lt;PaymentResponse&gt; ProcessWalletPaymentAsync()
              {
                  try
                  {
                      // Prepare form parameters
                      var formData = new Dictionary<string, string>
                      {
                          { "key", "J****g" },                     // Replace with your actual merchant key
                          { "txnid", "aI1UM19ONxLgPz" },           // Transaction ID (unique for each transaction)
                          { "amount", "10.00" },                   // Payment amount
                          { "firstname", "Ashish" },               // Customer's name
                          { "email", "test@gmail.com" },           // Customer's email
                          { "phone", "9876543210" },               // Customer's phone number
                          { "productinfo", "iPhone" },             // Product information
                          { "pg", "cash" },                        // Payment gateway type (cash for wallets)
                          { "bankcode", "paytm" },                 // Wallet provider (paytm in this case)
                          { "surl", "https://apiplayground-response.herokuapp.com/" }, // Success URL
                          { "furl", "https://apiplayground-response.herokuapp.com/" }, // Failure URL
                          { "hash", "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa" } // Security hash
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
                  var processor = new PayUWalletPaymentProcessor();
                  var result = await processor.ProcessWalletPaymentAsync();
                  
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

    <Tab title="💰 EMI">
      **Additional Parameters for EMI Payments**

      | Parameter   | Type   | Description                 | Example                 |
      | ----------- | ------ | --------------------------- | ----------------------- |
      | pg          | String | Payment gateway (mandatory) | `EMI`                   |
      | bankcode    | String | Bank EMI code               | Bank-specific EMI codes |
      | ccnum       | String | Card number for EMI         | `4111111111111111`      |
      | ccname      | String | Name on card                | `John Doe`              |
      | ccvv        | String | CVV                         | `123`                   |
      | ccexpmon    | String | Expiry month                | `12`                    |
      | ccexpyr     | String | Expiry year                 | `2025`                  |
      | emi\_planid | String | EMI plan identifier         | `1`                     |
      | emi\_tenure | String | EMI tenure in months        | `6`                     |

      **Sample EMI Request**

      ```html
      <form action="https://test.payu.in/_payment" method="post">
        <input type="hidden" name="key" value="JP***g" />
        <input type="hidden" name="txnid" value="EMI_TXN123" />
        <input type="hidden" name="amount" value="10000.00" />
        <input type="hidden" name="productinfo" value="Mobile" />
        <input type="hidden" name="firstname" value="John" />
        <input type="hidden" name="email" value="john@example.com" />
        <input type="hidden" name="phone" value="9876543210" />
        <input type="hidden" name="pg" value="EMI" />
        <input type="hidden" name="bankcode" value="HDFC" />
        <input type="hidden" name="ccnum" value="4111111111111111" />
        <input type="hidden" name="ccname" value="John Doe" />
        <input type="hidden" name="ccvv" value="123" />
        <input type="hidden" name="ccexpmon" value="12" />
        <input type="hidden" name="ccexpyr" value="2025" />
        <input type="hidden" name="emi_planid" value="1" />
        <input type="hidden" name="emi_tenure" value="6" />
        <input type="hidden" name="surl" value="https://yoursite.com/success" />
        <input type="hidden" name="furl" value="https://yoursite.com/failure" />
        <input type="hidden" name="hash" value="[computed_hash]" />
        <input type="submit" value="Pay with EMI" />
      </form>
      ```
    </Tab>

    <Tab title="📅 BNPL">
      **Additional Parameters for BNPL Payments**

      | Parameter | Type   | Description                 | Example                         |
      | --------- | ------ | --------------------------- | ------------------------------- |
      | pg        | String | Payment gateway (mandatory) | `BNPL`                          |
      | bankcode  | String | BNPL provider code          | `LAZYPAY`, `SIMPL`, `ZESTMONEY` |

      **BNPL Provider Codes**

      | Provider  | Bank Code   |
      | --------- | ----------- |
      | LazyPay   | `LAZYPAY`   |
      | Simpl     | `SIMPL`     |
      | ZestMoney | `ZESTMONEY` |
      | TwidPay   | `TWID`      |
      | FlexMoney | `FLEXMONEY` |

      **Sample BNPL Request**

      ```curl
      curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=J****g&txnid=5jJ9xYceXX1ydT&amount=1000.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=BNPL&bankcode=LAZYPAY&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
      ```
    </Tab>

    <Tab title="🎫 Pluxee Card">
      **Additional Parameters for Pluxee Card Payments**

      | Parameter          | Type   | Description                  | Example                        |
      | ------------------ | ------ | ---------------------------- | ------------------------------ |
      | pg                 | String | Payment gateway (mandatory)  | `MC`                           |
      | bankcode           | String | Pluxee identifier            | `SODEXO`                       |
      | ccnum              | String | 16-digit card number         | `637513XXXXXX9318`             |
      | ccname             | String | Name on card                 | `John Doe`                     |
      | ccvv               | String | 3-digit CVV                  | `123`                          |
      | ccexpmon           | String | Expiry month                 | `05`                           |
      | ccexpyr            | String | Expiry year                  | `2025`                         |
      | save\_sodexo\_card | String | Save card for future use     | `1` (save), `0` (don't save)   |
      | is\_check\_balance | String | Check balance before payment | `1` (check), `0` (don't check) |

      **Sample Pluxee Card Request**

      ```curl
      curl -X \
       POST "https://test.payu.in/_payment-H "accept: application/json" -H \
       "Content-Type: application/x-www-form-urlencoded" -d”key=JP***g&txnid=bvRCCBO4YiGGHE&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=MC&bankcode=SODEXO&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=637513XXXXXX9318
      &ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=Ashish&hash=ad36b3253313753088c662053b043fbe6d7a10112b31fbf20c4b0945b6a70c3a12239c5330ec2d0a0956bcd28a689f08c94fbb9cc2c5e06bb08dc81968672f64”
      ```
      ```javascript
      /**
       * PayU Pluxee Card Payment Integration using Fetch API
       * 
       * IMPORTANT: This should only be executed server-side (e.g., in Node.js), never in the browser,
       * as it contains sensitive payment information.
       */

      // Payment endpoint
      const url = 'https://test.payu.in/_payment';

      // Form data parameters
      const formData = new URLSearchParams();
      formData.append('key', 'JP***g');                 // Replace with your actual merchant key
      formData.append('txnid', 'bvRCCBO4YiGGHE');      // Transaction ID (unique for each transaction)
      formData.append('amount', '10.00');              // Payment amount
      formData.append('firstname', 'Ashish');          // Customer's name
      formData.append('email', 'test@gmail.com');      // Customer's email
      formData.append('phone', '9876543210');          // Customer's phone number
      formData.append('productinfo', 'iPhone');        // Product information
      formData.append('pg', 'MC');                     // Payment gateway (MC for meal cards)
      formData.append('bankcode', 'SODEXO');           // Specific card type (Sodexo/Pluxee)
      formData.append('surl', 'https://apiplayground-response.herokuapp.com/'); // Success URL
      formData.append('furl', 'https://apiplayground-response.herokuapp.com/'); // Failure URL
      formData.append('ccnum', '637513XXXXXX9318');    // Card number
      formData.append('ccexpmon', '05');               // Card expiry month
      formData.append('ccexpyr', '2022');              // Card expiry year
      formData.append('ccvv', '123');                  // Card verification value
      formData.append('ccname', 'Ashish');             // Cardholder name
      formData.append('hash', 'ad36b3253313753088c662053b043fbe6d7a10112b31fbf20c4b0945b6a70c3a12239c5330ec2d0a0956bcd28a689f08c94fbb9cc2c5e06bb08dc81968672f64'); // Security hash

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

      def process_pluxee_payment() -> Dict[str, Any]:
          """
          Process Pluxee (Sodexo) card payment using PayU's Merchant Hosted Checkout
          
          IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
          
          Returns:
              Dictionary with response from PayU API
          """
          # API endpoint
          url = "https://test.payu.in/_payment"
          
          # Prepare the form data
          payload = {
              "key": "JP***g",                   # Replace with your actual merchant key
              "txnid": "bvRCCBO4YiGGHE",         # Transaction ID (unique for each transaction)
              "amount": "10.00",                 # Payment amount
              "firstname": "Ashish",             # Customer's name
              "email": "test@gmail.com",         # Customer's email
              "phone": "9876543210",             # Customer's phone number
              "productinfo": "iPhone",           # Product information
              "pg": "MC",                        # Payment gateway (MC for meal cards)
              "bankcode": "SODEXO",              # Specific card type (Sodexo/Pluxee)
              "surl": "https://apiplayground-response.herokuapp.com/", # Success URL
              "furl": "https://apiplayground-response.herokuapp.com/", # Failure URL
              "ccnum": "637513XXXXXX9318",       # Card number
              "ccexpmon": "05",                  # Card expiry month
              "ccexpyr": "2022",                 # Card expiry year
              "ccvv": "123",                     # Card verification value
              "ccname": "Ashish",                # Cardholder name
              "hash": "ad36b3253313753088c662053b043fbe6d7a10112b31fbf20c4b0945b6a70c3a12239c5330ec2d0a0956bcd28a689f08c94fbb9cc2c5e06bb08dc81968672f64" # Security hash
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
          result = process_pluxee_payment()
          print(f"Status Code: {result['status_code']}")
          if 'error' in result:
              print(f"Error: {result['error']}")
          print(f"Response: {result['response']}")

      ```
      ```php
      /**
       * Process Pluxee (Sodexo) card payment using PayU's Merchant Hosted Checkout
       * 
       * IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
       * 
       * @return array Response from PayU API
       */
      function processPluxeeCardPayment() {
          // API endpoint
          $url = "https://test.payu.in/_payment";
          
          // Prepare the form data
          $payload = [
              "key" => "JP***g",                    // Replace with your actual merchant key
              "txnid" => "bvRCCBO4YiGGHE",          // Transaction ID (unique for each transaction)
              "amount" => "10.00",                  // Payment amount
              "firstname" => "Ashish",              // Customer's name
              "email" => "test@gmail.com",          // Customer's email
              "phone" => "9876543210",              // Customer's phone number
              "productinfo" => "iPhone",            // Product information
              "pg" => "MC",                         // Payment gateway (MC for meal cards)
              "bankcode" => "SODEXO",               // Specific card type (Sodexo/Pluxee)
              "surl" => "https://apiplayground-response.herokuapp.com/", // Success URL
              "furl" => "https://apiplayground-response.herokuapp.com/", // Failure URL
              "ccnum" => "637513XXXXXX9318",        // Card number
              "ccexpmon" => "05",                   // Card expiry month
              "ccexpyr" => "2022",                  // Card expiry year
              "ccvv" => "123",                      // Card verification value
              "ccname" => "Ashish",                 // Cardholder name
              "hash" => "ad36b3253313753088c662053b043fbe6d7a10112b31fbf20c4b0945b6a70c3a12239c5330ec2d0a0956bcd28a689f08c94fbb9cc2c5e06bb08dc81968672f64" // Security hash
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
      $result = processPluxeeCardPayment();
      echo "Status Code: " . $result["status_code"] . "\n";
      if (isset($result["error"])) {
          echo "Error: " . $result["error"] . "\n";
      }
      echo "Response: " . $result["response"] . "\n";

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
       * PayU Pluxee Card Payment Processor for Merchant Hosted Checkout
       * 
       * IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
       */
      public class PayUPluxeeCardPaymentProcessor {
          
          // API endpoint
          private static final String PAYU_TEST_URL = "https://test.payu.in/_payment";
          
          /**
           * Process Pluxee card payment through PayU
           * @return PaymentResponse containing status and response data
           */
          public PaymentResponse processPluxeeCardPayment() {
              try {
                  // Initialize URL
                  URL url = new URL(PAYU_TEST_URL);
                  
                  // Prepare form parameters
                  Map<String, String> params = new HashMap<>();
                  params.put("key", "JP***g");                    // Replace with your actual merchant key
                  params.put("txnid", "bvRCCBO4YiGGHE");          // Transaction ID (unique for each transaction)
                  params.put("amount", "10.00");                  // Payment amount
                  params.put("firstname", "Ashish");              // Customer's name
                  params.put("email", "test@gmail.com");          // Customer's email
                  params.put("phone", "9876543210");              // Customer's phone number
                  params.put("productinfo", "iPhone");            // Product information
                  params.put("pg", "MC");                         // Payment gateway (MC for meal cards)
                  params.put("bankcode", "SODEXO");               // Specific card type (Sodexo/Pluxee)
                  params.put("surl", "https://apiplayground-response.herokuapp.com/"); // Success URL
                  params.put("furl", "https://apiplayground-response.herokuapp.com/"); // Failure URL
                  params.put("ccnum", "637513XXXXXX9318");        // Card number
                  params.put("ccexpmon", "05");                   // Card expiry month
                  params.put("ccexpyr", "2022");                  // Card expiry year
                  params.put("ccvv", "123");                      // Card verification value
                  params.put("ccname", "Ashish");                 // Cardholder name
                  params.put("hash", "ad36b3253313753088c662053b043fbe6d7a10112b31fbf20c4b0945b6a70c3a12239c5330ec2d0a0956bcd28a689f08c94fbb9cc2c5e06bb08dc81968672f64"); // Security hash
                  
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
              PayUPluxeeCardPaymentProcessor processor = new PayUPluxeeCardPaymentProcessor();
              PaymentResponse result = processor.processPluxeeCardPayment();
              
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

      namespace PayUPluxeeIntegration
      {
          /// <summary>
          /// PayU Pluxee Card Payment Processor for Merchant Hosted Checkout
          /// 
          /// IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
          /// </summary>
          public class PayUPluxeeCardPaymentProcessor
          {
              // API endpoint
              private const string PayuTestUrl = "https://test.payu.in/_payment";
              
              /// <summary>
              /// Process Pluxee card payment through PayU
              /// </summary>
              /// <returns>PaymentResponse containing status and response data</returns>
              public async Task&lt;PaymentResponse&gt; ProcessPluxeeCardPaymentAsync()
              {
                  try
                  {
                      // Prepare form parameters
                      var formData = new Dictionary<string, string>
                      {
                          { "key", "JP***g" },                     // Replace with your actual merchant key
                          { "txnid", "bvRCCBO4YiGGHE" },           // Transaction ID (unique for each transaction)
                          { "amount", "10.00" },                   // Payment amount
                          { "firstname", "Ashish" },               // Customer's name
                          { "email", "test@gmail.com" },           // Customer's email
                          { "phone", "9876543210" },               // Customer's phone number
                          { "productinfo", "iPhone" },             // Product information
                          { "pg", "MC" },                          // Payment gateway (MC for meal cards)
                          { "bankcode", "SODEXO" },                // Specific card type (Sodexo/Pluxee)
                          { "surl", "https://apiplayground-response.herokuapp.com/" }, // Success URL
                          { "furl", "https://apiplayground-response.herokuapp.com/" }, // Failure URL
                          { "ccnum", "637513XXXXXX9318" },         // Card number
                          { "ccexpmon", "05" },                    // Card expiry month
                          { "ccexpyr", "2022" },                   // Card expiry year
                          { "ccvv", "123" },                       // Card verification value
                          { "ccname", "Ashish" },                  // Cardholder name
                          { "hash", "ad36b3253313753088c662053b043fbe6d7a10112b31fbf20c4b0945b6a70c3a12239c5330ec2d0a0956bcd28a689f08c94fbb9cc2c5e06bb08dc81968672f64" } // Security hash
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
                  var processor = new PayUPluxeeCardPaymentProcessor();
                  var result = await processor.ProcessPluxeeCardPaymentAsync();
                  
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

    <Tab title="🏛️ NEFT/RTGS">
      **Additional Parameters for NEFT/RTGS Payments**

      | Parameter | Type   | Description                 | Example    |
      | --------- | ------ | --------------------------- | ---------- |
      | pg        | String | Payment gateway (mandatory) | `NEFTRTGS` |
      | bankcode  | String | Bank NEFT/RTGS code         | `EFTAXIS`  |

      **NEFT/RTGS Bank Codes**

      | Bank Name  | Bank Code  |
      | ---------- | ---------- |
      | Axis Bank  | `EFTAXIS`  |
      | HDFC Bank  | `EFTHDFC`  |
      | ICICI Bank | `EFTICICI` |

      ### Optional configuration

      PayU provides an optional **Back to Merchant** button on the payment challan of a NEFT/RTGS payment. This button enables your customer to go back to the merchant portal once the transaction is done.

      In this scenario, if a customer clicks on **Back to Merchant** button the merchant will receive the response on the furl shared in the [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted).

      *Sample challan of a NEFT/RTGS transaction*

      <img
        src="https://files.readme.io/4f959a8-neftrtgs_challan.jpeg"
        alt=""
        style={{
    display: "block",
    margin: "0 auto",
    width: "400px"
  }}
      />

      **Sample NEFT/RTGS Request**

      ```curl
      curl -X \
       POST "https://test.payu.in/_payment-H "accept: application/json" -H \
       "Content-Type: application/x-www-form-urlencoded" -d"key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=NEFTRTGS&bankcode=EFTAXIS&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
      ```
      ```javascript
      /**
       * PayU NEFT/RTGS Payment Integration using Fetch API
       * 
       * IMPORTANT: This should only be executed server-side (e.g., in Node.js), never in the browser,
       * as it contains sensitive payment information.
       */

      // Payment endpoint
      const url = 'https://test.payu.in/_payment';

      // Form data parameters
      const formData = new URLSearchParams();
      formData.append('key', 'J****g');                 // Replace with your actual merchant key
      formData.append('txnid', 'aI1UM19ONxLgPz');      // Transaction ID (unique for each transaction)
      formData.append('amount', '10.00');              // Payment amount
      formData.append('firstname', 'Ashish');          // Customer's name
      formData.append('email', 'test@gmail.com');      // Customer's email
      formData.append('phone', '9876543210');          // Customer's phone number
      formData.append('productinfo', 'iPhone');        // Product information
      formData.append('pg', 'NEFTRTGS');               // Payment gateway (NEFT/RTGS)
      formData.append('bankcode', 'EFTAXIS');          // Bank code (Axis Bank NEFT)
      formData.append('surl', 'https://apiplayground-response.herokuapp.com/'); // Success URL
      formData.append('furl', 'https://apiplayground-response.herokuapp.com/'); // Failure URL
      formData.append('hash', '6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa'); // Security hash

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
          // Typically, for NEFT/RTGS, you'll get bank details to show to the customer
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

      def process_neft_payment() -> Dict[str, Any]:
          """
          Process NEFT/RTGS payment using PayU's Merchant Hosted Checkout
          
          IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
          
          Returns:
              Dictionary with response from PayU API
          """
          # API endpoint
          url = "https://test.payu.in/_payment"
          
          # Prepare the form data
          payload = {
              "key": "J****g",                   # Replace with your actual merchant key
              "txnid": "aI1UM19ONxLgPz",         # Transaction ID (unique for each transaction)
              "amount": "10.00",                 # Payment amount
              "firstname": "Ashish",             # Customer's name
              "email": "test@gmail.com",         # Customer's email
              "phone": "9876543210",             # Customer's phone number
              "productinfo": "iPhone",           # Product information
              "pg": "NEFTRTGS",                  # Payment gateway (NEFT/RTGS)
              "bankcode": "EFTAXIS",             # Bank code (Axis Bank NEFT)
              "surl": "https://apiplayground-response.herokuapp.com/", # Success URL
              "furl": "https://apiplayground-response.herokuapp.com/", # Failure URL
              "hash": "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa" # Security hash
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
          result = process_neft_payment()
          print(f"Status Code: {result['status_code']}")
          if 'error' in result:
              print(f"Error: {result['error']}")
          print(f"Response: {result['response']}")
          # For NEFT/RTGS, display the bank details to the customer for making the transfer

      ```
      ```php
      <?php
      /**
       * Process NEFT/RTGS payment using PayU's Merchant Hosted Checkout
       * 
       * IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
       * 
       * @return array Response from PayU API
       */
      function processNeftPayment() {
          // API endpoint
          $url = "https://test.payu.in/_payment";
          
          // Prepare the form data
          $payload = [
              "key" => "J****g",                    // Replace with your actual merchant key
              "txnid" => "aI1UM19ONxLgPz",          // Transaction ID (unique for each transaction)
              "amount" => "10.00",                  // Payment amount
              "firstname" => "Ashish",              // Customer's name
              "email" => "test@gmail.com",          // Customer's email
              "phone" => "9876543210",              // Customer's phone number
              "productinfo" => "iPhone",            // Product information
              "pg" => "NEFTRTGS",                   // Payment gateway (NEFT/RTGS)
              "bankcode" => "EFTAXIS",              // Bank code (Axis Bank NEFT)
              "surl" => "https://apiplayground-response.herokuapp.com/", // Success URL
              "furl" => "https://apiplayground-response.herokuapp.com/", // Failure URL
              "hash" => "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa" // Security hash
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
      $result = processNeftPayment();
      echo "Status Code: " . $result["status_code"] . "\n";
      if (isset($result["error"])) {
          echo "Error: " . $result["error"] . "\n";
      }
      echo "Response: " . $result["response"] . "\n";
      // For NEFT/RTGS, display the bank details to the customer for making the transfer
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
       * PayU NEFT/RTGS Payment Processor for Merchant Hosted Checkout
       * 
       * IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
       */
      public class PayUNeftPaymentProcessor {
          
          // API endpoint
          private static final String PAYU_TEST_URL = "https://test.payu.in/_payment";
          
          /**
           * Process NEFT/RTGS payment through PayU
           * @return PaymentResponse containing status and response data
           */
          public PaymentResponse processNeftPayment() {
              try {
                  // Initialize URL
                  URL url = new URL(PAYU_TEST_URL);
                  
                  // Prepare form parameters
                  Map<String, String> params = new HashMap<>();
                  params.put("key", "J****g");                    // Replace with your actual merchant key
                  params.put("txnid", "aI1UM19ONxLgPz");          // Transaction ID (unique for each transaction)
                  params.put("amount", "10.00");                  // Payment amount
                  params.put("firstname", "Ashish");              // Customer's name
                  params.put("email", "test@gmail.com");          // Customer's email
                  params.put("phone", "9876543210");              // Customer's phone number
                  params.put("productinfo", "iPhone");            // Product information
                  params.put("pg", "NEFTRTGS");                   // Payment gateway (NEFT/RTGS)
                  params.put("bankcode", "EFTAXIS");              // Bank code (Axis Bank NEFT)
                  params.put("surl", "https://apiplayground-response.herokuapp.com/"); // Success URL
                  params.put("furl", "https://apiplayground-response.herokuapp.com/"); // Failure URL
                  params.put("hash", "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"); // Security hash
                  
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
              PayUNeftPaymentProcessor processor = new PayUNeftPaymentProcessor();
              PaymentResponse result = processor.processNeftPayment();
              
              System.out.println("Status Code: " + result.getStatusCode());
              if (result.isSuccess()) {
                  System.out.println("Response: " + result.getResponse());
                  // For NEFT/RTGS, display the bank details to the customer for making the transfer
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

      namespace PayUNeftIntegration
      {
          /// <summary>
          /// PayU NEFT/RTGS Payment Processor for Merchant Hosted Checkout
          /// 
          /// IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
          /// </summary>
          public class PayUNeftPaymentProcessor
          {
              // API endpoint
              private const string PayuTestUrl = "https://test.payu.in/_payment";
              
              /// <summary>
              /// Process NEFT/RTGS payment through PayU
              /// </summary>
              /// <returns>PaymentResponse containing status and response data</returns>
              public async Task&lt;PaymentResponse&gt; ProcessNeftPaymentAsync()
              {
                  try
                  {
                      // Prepare form parameters
                      var formData = new Dictionary<string, string>
                      {
                          { "key", "J****g" },                     // Replace with your actual merchant key
                          { "txnid", "aI1UM19ONxLgPz" },           // Transaction ID (unique for each transaction)
                          { "amount", "10.00" },                   // Payment amount
                          { "firstname", "Ashish" },               // Customer's name
                          { "email", "test@gmail.com" },           // Customer's email
                          { "phone", "9876543210" },               // Customer's phone number
                          { "productinfo", "iPhone" },             // Product information
                          { "pg", "NEFTRTGS" },                    // Payment gateway (NEFT/RTGS)
                          { "bankcode", "EFTAXIS" },               // Bank code (Axis Bank NEFT)
                          { "surl", "https://apiplayground-response.herokuapp.com/" }, // Success URL
                          { "furl", "https://apiplayground-response.herokuapp.com/" }, // Failure URL
                          { "hash", "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa" } // Security hash
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
                  var processor = new PayUNeftPaymentProcessor();
                  var result = await processor.ProcessNeftPaymentAsync();
                  
                  Console.WriteLine($"Status Code: {result.StatusCode}");
                  if (result.IsSuccess)
                  {
                      Console.WriteLine($"Response: {result.Response}");
                      // For NEFT/RTGS, display the bank details to the customer for making the transfer
                  }
                  else
                  {
                      Console.WriteLine($"Error: {result.Error}");
                  }
              }
          }
      }

      ```

      **Note**: Customer will be redirected to bank interface for completing NEFT/RTGS transfer.
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Step 1.3: Generate Hash" icon="fa-key">
  ```json
  key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|SALT
  ```

  tab: PHP \`\`\`php $key = "JP\*\*\*g"; $txnid = "TXN" . time(); $amount = "100.00"; $productinfo = "Test Product"; $firstname = "John"; $email = "[john@example.com](mailto:john@example.com)"; $salt = "your\_salt\_here";  $hash\_string = $key . "|" . $txnid . "|" . $amount . "|" . $productinfo . "|" . $firstname . "|" . $email . "|||||||||||" . $salt; $hash = strtolower(hash('sha512', $hash\_string));
  tab: Node.js
  const crypto = require('crypto');  const hashString = `${key}|${txnid}|${amount}|${productinfo}|${firstname}|${email}|||||||||||${salt}`; const hash = crypto.createHash('sha512').update(hashString).digest('hex');

  ````
    * Use empty strings for missing udf fields
    * Always compute hash on server-side
    * Include the lowercase hex digest as hash parameter
  </Accordion>

  <Accordion title="Step 1.4: Response handling & hash verification" icon="fa-shield-check">
    **Response Handling:**

    After the customer completes or abandons the payment, PayU POSTs back to your return URL with URL-encoded fields (form post). This payload includes the transaction status, txnid, mihpayid, and a hash you must verify (reverse hashing) before trusting the result.

    Sample surl/furl payload:

    ```json Success
    mihpayid=403993715531077182
    mode=CC
    status=success
    unmappedstatus=captured
    key=JPM7Fg
    txnid=TXN12345
    amount=1000.00
    productinfo=Pro Plan
    firstname=Aditi
    email=aditi@example.com
    phone=9999999999
    udf1=
    ...
    udf5=
    PG_TYPE=CC-PG
    bankcode=CC
    bank_ref_num=896193988312194700
    field1=...
    field9=Transaction is Successful
    hash=&lt;response_hash&gt;
  ````
  ```json Failure
  mihpayid=403993715531077182
  mode=CC
  status=failure
  unmappedstatus=failed
  key=JPM7Fg
  txnid=TXN12345
  amount=1000.00
  productinfo=Pro Plan
  firstname=Aditi
  email=aditi@example.com
  phone=9999999999
  udf1=
  ...
  udf5=
  PG_TYPE=CC-PG
  bankcode=CC
  bank_ref_num=
  field1=
  field2=
  ...
  field9=Transaction Failed
  error=E000
  error_Message=Bank was unable to authenticate
  hash=&lt;response_hash&gt;
  ```

  **PHP Response Verification**

  ```php
  $salt = "your_salt_here";
  $status = $_POST['status'];
  $firstname = $_POST['firstname'];
  $amount = $_POST['amount'];
  $txnid = $_POST['txnid'];
  $hash = $_POST['hash'];

  $retHashSeq = $salt.'|'.$status.'|||||||||||'.$_POST['udf5'].'|'.$_POST['udf4'].'|'.$_POST['udf3'].'|'.$_POST['udf2'].'|'.$_POST['udf1'].'|'.$_POST['email'].'|'.$firstname.'|'.$_POST['productinfo'].'|'.$amount.'|'.$txnid.'|'.$_POST['key'];

  $retHash = hash("sha512", $retHashSeq);

  if(hash_equals($retHash, $hash)) {
      // Hash verified - process the response
      if($status == 'success') {
          // Payment successful
      } else {
          // Payment failed
      }
  } else {
      // Hash verification failed
  }
  ```
</Accordion>

<Accordion title="Step 1.5: Verify the payment" icon="fa-magnifying-glass">
  <Tabs>
    <Tab title="1. Verify using Webhooks">
      Configure the webhooks to monitor the status of payments.\
      Webhooks enable a server to communicate with another server by sending an HTTP callback or message.\
      These callbacks are triggered by specific events or instances and operate at the server-to-server (S2S) level.

      👉 For more details, refer to [Webhooks for Payments](https://docs.payu.in/reference/webhooks). <br />
    </Tab>

    <Tab title="2. Verify using Verify Payments API">
      **Environment**

      |                        |                                                                                                              |
      | :--------------------- | :----------------------------------------------------------------------------------------------------------- |
      | Test Environment       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
      | Production Environment | [https://info.payu.in/merchant/postservice.php?form=2](https://info.payu.in/merchant/postservice.php?form=2) |

      <Accordion title="Sample request" icon="fa-code">
        ```curl
        curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
        --header 'Content-Type: application/x-www-form-urlencoded' \
        --data-urlencode 'key=JP***g' \
        --data-urlencode 'command=verify_payment' \
        --data-urlencode 'var1=IhfgcZnXR4o4nB' \
        --data-urlencode 'hash=<&lt;calculated_hash_here&gt;>'
        ```
      </Accordion>

      <Accordion title="Sample response" icon="fa-reply">
        <br />

        ```json Success Response
        If credit card payment is made, the response is similar to the following:
        {
        "status": 1,
        "msg": "1 out of 1 Transactions Fetched Successfully",
        "transaction_details": {
           "1733900931584": {
               "mihpayid": "21820644083",
               "request_id": null,
               "bank_ref_num": null,
               "amt": "1.00",
               "transaction_amount": "1.00",
               "txnid": "1733900931584",
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
               "field9": "OTP/ATM page expired due to no user action",
               "error_code": "E1602",
               "addedon": "2024-12-11 12:43:03",
               "payment_source": "payu",
               "card_type": "MAST",
               "error_Message": "Bank was unable to authenticate.",
               "net_amount_debit": "0.00",
               "disc": "0.00",
               "mode": "DC",
               "PG_TYPE": "DC-PG",
               "card_no": "XXXXXXXXXXXX7596",
               "status": "failure",
               "unmappedstatus": "dropped",
               "Merchant_UTR": null,
               "Settled_At": null,
               "cardhash": "095d184331be367bb92aa3eeecb57d0728de96cc598dd563d407982d75021149",
               "name_on_card": null,
               "card_token": "4e97156bc2d6320cdfe15",
               "field4": null,
               "threeDSVersion": "2.2.0",
               "offerAvailed": null
           }
        }
        }
        ```
        ```json Failure Response

        If txnID is not found, the response is similar to the following
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
      </Accordion>

      <Accordion title="Response parameters" icon="fa-list">
        <Table align={["left","left","left"]}>
          <thead>
            <tr>
              <th style={{ textAlign: "left" }}>
                **Parameter**
              </th>

              <th style={{ textAlign: "left" }}>
                **Description**
              </th>

              <th style={{ textAlign: "left" }}>
                **Example**
              </th>
            </tr>
          </thead>

          <tbody>
            <tr>
              <td style={{ textAlign: "left" }}>
                status
              </td>

              <td style={{ textAlign: "left" }}>
                This parameter returns the status of web service call. The status can be any of the following:

                * 0 - If web service call failed.
                * 1 - If web service call succeeded
              </td>

              <td style={{ textAlign: "left" }}>
                0
              </td>
            </tr>

            <tr>
              <td style={{ textAlign: "left" }}>
                msg
              </td>

              <td style={{ textAlign: "left" }}>
                This parameter returns the reason string.
              </td>

              <td style={{ textAlign: "left" }}>
                For example, any of the following messages are displayed:

                * Parameter missing
                * Token is empty
                * Amount is empty
                * Transaction not exists
              </td>
            </tr>

            <tr>
              <td style={{ textAlign: "left" }}>
                transaction\_details
              </td>

              <td style={{ textAlign: "left" }}>
                This parameter contains the response in a JSON format. For more information refer to [JSON fields description for transaction\_details parameter ](#json-field-description-for-transaction_details-parameter).
              </td>

              <td style={{ textAlign: "left" }} />
            </tr>

            <tr>
              <td style={{ textAlign: "left" }}>
                request\_id
              </td>

              <td style={{ textAlign: "left" }}>
                PayU Request ID for a request in a Transaction. For example, a transaction can have a refund request.
              </td>

              <td style={{ textAlign: "left" }}>
                7800456
              </td>
            </tr>

            <tr>
              <td style={{ textAlign: "left" }}>
                bank\_ref\_num
              </td>

              <td style={{ textAlign: "left" }}>
                This parameter returns the bank reference number. If the bank provides after a successful action.
              </td>

              <td style={{ textAlign: "left" }}>
                204519474956
              </td>
            </tr>
          </tbody>
        </Table>

        To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).
      </Accordion>
    </Tab>
  </Tabs>
</Accordion>

<br />

## Step 2: Test Integration

Test your merchant hosted integration thoroughly across all payment modes:

<Accordion title="Step 2.1: Pre-Integration Security Checklist" icon="fa-check-circle">
  Before testing payments, ensure your security setup is complete:

  **Security Requirements**

  1. **SSL Certificate**: Ensure your website has a valid SSL certificate
  2. **HTTPS Enforcement**: All payment pages must use HTTPS
  3. **PCI DSS Assessment**: Complete Self-Assessment Questionnaire if handling card data
  4. **Input Validation**: Implement client and server-side validation
  5. **Hash Validation**: Verify request and response hashes
  6. **Error Handling**: Implement proper error handling for failed payments

  **Test Environment Setup**

  * Use test merchant credentials
  * Point to `https://test.payu.in/_payment`
  * Implement proper logging for debugging
</Accordion>

<Accordion title="Step 2.2: Pre-Payment Validation" icon="fa-check-circle">
  Before initiating a transaction, ensure your server-side implementation is correct.

  1. **Verify API Credentials:** Double-check that you are using the correct key and salt for the test environment.
  2. **Validate Hash Calculation:** The most common point of failure is an incorrect hash.
     1. Temporarily print the string that you are passing into the hash function on your server.
     2. Ensure the order of the parameters (key|txnid|amount|productinfo|firstname|email...|salt) exactly matches the format specified in the documentation.
     3. Verify that there are no empty or null values for mandatory parameters in the hash string.
     4. If you encounter a "Checksum failed" error upon redirection, this is the first thing to debug.
</Accordion>

<Accordion title="Step 2.3: Simulate a Successful Transaction (The Happy Path)" icon="fa-thumbs-up">
  This test ensures that a successful payment is correctly processed and recorded.

  1. **Initiate Payment:** On your website or app, add items to the cart and proceed to payment. This should trigger your code to send the transaction details to PayU and redirect the user to the PayU payment page.
  2. **Error Check:** If you are not redirected and see an error message on your own site, check your server-side logs. If you are redirected to a PayU error page, refer to the Error Handling section to diagnose the issue.
  3. **Verify Payment Page:** Once on the PayU page, confirm the following:
     1. The transaction amount and product details are displayed correctly.
     2. All the payment methods (Credit/Debit Card, UPI, Net Banking, etc.) that should be active on your account are visible. If a payment method is missing, please contact your Key Account Manager (KAM) or PayU Support.
  4. **Test a Card Transaction**:
     1. Select Credit Card as the payment method.
     2. Use the following test card details:
        1. Card Number: 5123456789012346
        2. Expiry Date: Any valid future date (e.g., 12/2030)
        3. CVV: 123
        4. Name on Card: Test Name
     3. Click Pay Now. You will be redirected to a dummy bank page to simulate 3D Secure authentication.
     4. Enter the test OTP 123456 and click Submit.
  5. **Test a UPI Transaction:**
     1. Select UPI as the payment method.
     2. Enter a test UPI ID: testsuccess\@gpay
     3. Click Verify and then Pay Now. This will simulate a successful UPI transaction.

  For more test credentials, refer to the [Test Cards, UPI ID and Wallets guide](https://docs.payu.in/docs/test-cards-upi-id-and-wallets).
</Accordion>

<Accordion title="Step 2.4: Simulate a Failed Transaction" icon="fa-times-circle">
  It's equally important to test how your system handles failed payments.

  1. Initiate a New Payment as you did in Step 2.
  2. Test a Failing Card Transaction:
     1. Select Credit Card as the payment method.
     2. Use a test card designed to fail, for example:
        1. Card Number: 5123456789012340 (Payment failed by user)
     3. Complete the payment flow. The transaction should fail.
</Accordion>

<Accordion title="Step 2.5: Post-Transaction Verification" icon="fa-magnifying-glass">
  After both the successful and failed transactions, you must verify the final status at multiple points.

  1. **Check the Return URL (surl / furl):**
     1. After a successful payment, PayU will redirect the user to the Success URL (surl) you provided. Verify that your application handles this redirect correctly and displays an appropriate success message to the user.
     2. After a failed payment, PayU will redirect the user to the Failure URL (furl). Verify that your application displays a clear failure message and provides the user with options to retry.
  2. **Verify the Server-to-Server (S2S) Webhook:**
     1. This is the most reliable way to confirm transaction status.
     2. Check your server logs to ensure that you have received the S2S POST request from PayU for the transaction.
     3. Validate the hash in the webhook response to ensure the data is authentic.
     4. Update the transaction status in your database based on the status received in the S2S webhook, not based on the browser redirect (surl/furl).
  3. **Cross-Verify in the PayU Dashboard:**
     1. Log in to your PayU test dashboard.
     2. Navigate to the "Transactions" section.
     3. Verify that both the successful and failed transactions are logged correctly with the corresponding status (success, failure). Check that details like txnid and amount match your records.
</Accordion>

## Step 3: Going Live: Your Final Checklist

Complete security requirements and deploy to production:

<Accordion title="Step 3.1: Security Compliance Requirements" icon="fa-lock">
  **PCI DSS Compliance (For Card Payments)**

  If you're collecting card details on your website, you must complete:

  1. **Self-Assessment Questionnaire A-EP**: Download and complete the [PCI DSS SAQ A-EP form](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf)
  2. **Attestation of Compliance**: Submit completed form to PayU
  3. **Network Security**: Implement proper firewall and network security
  4. **Data Protection**: Never store sensitive card data (PAN, CVV, etc.)
  5. **Access Control**: Implement proper user access controls
  6. **Monitoring**: Set up security monitoring and logging

  **SSL/TLS Requirements**

  * Valid SSL certificate from trusted CA
  * TLS 1.2 or higher
  * Strong cipher suites
  * Proper certificate chain

  **Code Security Requirements**

  * Input validation on all payment fields
  * SQL injection prevention
  * XSS protection
  * CSRF protection
  * Secure session management

  <Callout icon="⚠️" theme="warning">
    **Important**: Failure to comply with PCI DSS requirements may result in account suspension and liability for fraud.
  </Callout>
</Accordion>

<Accordion title="Step 3.2: Update to Production Credentials" icon="fa-key">
  **Switch to Live Environment**

  1. **Update API Credentials**
     * Replace test merchant key with live key
     * Replace test salt with live salt
     * Update endpoint URL to `https://secure.payu.in/_payment`

  2. **Update Verification API URL**
     * Change from test to production verification endpoint
     * Update URL to `https://info.payu.in/merchant/postservice.php?form=2`

  3. **Update Webhook URLs**
     * Configure production webhook endpoints
     * Ensure HTTPS URLs are accessible from internet
     * Test webhook reception

  **Production Configuration Sample**

  ```php
  // Production configuration
  define('PAYU_BASE_URL', 'https://secure.payu.in');
  define('PAYU_PAYMENT_URL', PAYU_BASE_URL . '/_payment');
  define('PAYU_VERIFY_URL', 'https://info.payu.in/merchant/postservice.php?form=2');
  define('MERCHANT_KEY', 'your_live_merchant_key');
  define('MERCHANT_SALT', 'your_live_salt');
  ```
</Accordion>

<Accordion title="Step 3.3: Final Integration Verification" icon="fa-clipboard-check">
  **Pre-Launch Checklist**

  **✅ Security Verification**

  * [ ] PCI DSS compliance completed (if applicable)
  * [ ] SSL certificate installed and verified
  * [ ] All payment forms use HTTPS
  * [ ] Hash validation implemented for requests and responses
  * [ ] Input validation on all fields
  * [ ] No sensitive data logged or stored
  * [ ] Error handling implemented
  * [ ] Security headers configured

  **✅ Technical Integration**

  * [ ] Production credentials configured
  * [ ] Payment endpoints updated to production URLs
  * [ ] All payment modes tested in production
  * [ ] Webhook endpoints configured and tested
  * [ ] Response handling and hash verification working
  * [ ] Transaction verification API integration tested
  * [ ] Database integration for transaction storage
  * [ ] Email/SMS notifications configured

  **✅ Live Transaction Testing**

  * [ ] Conduct small live transactions for each payment mode
  * [ ] Verify successful transactions in PayU dashboard
  * [ ] Test failed transaction handling
  * [ ] Verify webhook reception for live transactions
  * [ ] Test refund process (if applicable)
  * [ ] Verify settlement process

  <Callout icon="🚀" theme="success">
    **Go Live!** Once all checklist items are completed and verified, your Merchant Hosted PayU integration is ready for production use.
  </Callout>
</Accordion>

<br />

## Additional Resources

* [Merchant Hosted Checkout Integration Introduction](https://docs.payu.in/docs/custom-checkout-merchant-hosted)
* [Hash Generation](https://docs.payu.in/docs/generate-hash-payu-hosted)
* [Webhooks](https://docs.payu.in/docs/webhooks-for-payments)
* [Error Codes Reference](https://docs.payu.in/reference/error-codes)
* [Test Credentials](https://docs.payu.in/docs/test-cards-upi-id-and-wallets)

<br />
