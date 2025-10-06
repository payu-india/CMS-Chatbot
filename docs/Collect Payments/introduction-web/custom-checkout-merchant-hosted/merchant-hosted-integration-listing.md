---
title: Merchant Hosted Integration - Listing
deprecated: false
hidden: true
metadata:
  robots: index
---
# What you're building

A custom payment experience where you collect payment details on your own website and securely process them through PayU's APIs. Unlike the hosted solution, you have complete control over the UI/UX while PayU handles the secure payment processing. You pass order details, customer information, payment method-specific parameters (pg, bankcode), and a server-generated SHA-512 hash for integrity.

<Image align="center" border={false} src="https://files.readme.io/1f792ebae03e452e754b9d1cf24c20aa418f64ff16ff60d875dedbca50595479-cards_icon.jpg" />

<Image align="center" border={false} src="https://files.readme.io/5502490a82288eb8787bf81dc023ede806938cd540812f3ecdf022ea6e8c435b-netbankng_icon.jpg" />

<Image align="center" border={false} src="https://files.readme.io/5ffcdb1346fcca21e28403b3a977bf37173ea26123a18219b0a68604863661a4-upi_icon.jpg" />

<Image align="center" border={false} src="https://files.readme.io/94a34047e589e3bc24c04d9c6453dd3012dd04438cec1e593ea43cd208354da3-wallets_icon.jpg" />

<Image align="center" border={false} src="https://files.readme.io/c06a7440a3c1aacb53438f037f85bcc6e707cd9816c5cfcd7c2aa8513eae2500-emi_icon.jpg" />

<Image align="center" border={false} src="https://files.readme.io/cf2dea0bbe5f41336b561e78bed1daac4a80d6f268e6bbb925fa0cfadedddd16-bnpl_icon.jpg" />

<Image align="center" border={false} src="https://files.readme.io/bf87f75f97171660faf61fe526357dd3ff6a141aec0f849d4d2d08d18cec0d98-neft_icon.jpg" />

<Image align="center" border={false} src="https://files.readme.io/0a4bb0ba9604b82f7b75dbb4e40756e8674ec644ba5743d54420678f91579694-sodexo_icon.jpg" />

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
  This step is to ensure the following:

  * Improve your customer experience.
  * Validate the card number or UPI handle based on the payment mode before initiating the payment request to increase the transaction success rate.
  * Check the eligibility of your customer's card.
</Accordion>

<Accordion title="Step 1.2: Prepare the request parameters" icon="fa-cogs">
  ### Before you begin

  * Ensure the you have set up your eCommerce page to collect the details according to the payment modes with which you wish to integration. For example, for Cards integration, you require the following fields on your eCommerce page:
  * Card number
  * Expiry Date (MM/YY)
  * CVV
  * Name on card

  ### Validate inputs based on payment mode

  Select the card to refer to the API that you have to use for validating the input based on the payment mode.

  <Cards columns={3}>
    <Card>
      [![Net Banking](https://files.readme.io/852ff36002aae339313722c8832cc7b5443c1bf7e5ca47571e9dd6971d51a2ae-netbanking_icon.png)](https://docs.payu.in/reference/get_net_banking_status_api/)
    </Card>

    <Card>
      [![Cards](https://files.readme.io/049c1e19c22dc0dee8f0f2b0a7facd89231c96a6b86d188af824cf1e87154d8e-cards_icon.png)](https://docs.payu.in/reference/check_is_domestic_api/)
    </Card>

    <Card>
      [![UPI](https://files.readme.io/f5fe8045de9902d7ed2d1bb0a31568151638acaba086331df01826e0a4ebe1f2-upi_icon.png)](https://docs.payu.in/reference/validate_vpa_api/)
    </Card>

    <Card>
      ![Wallets](https://files.readme.io/0af7178db0a6130d39fb7b5270109e4251b0fd1b1455e54a936f29c145a97c87-wallets_icon.png)
    </Card>

    <Card>
      [![EMI](https://files.readme.io/e32726065ea0eb0243a5c47583c54908d2f0732ea259206bae93f113f5284d52-emi_icon.png)](https://docs.payu.in/reference/eligible-bins-for-emi-v20/)
    </Card>

    <Card>
      [![BNPL](https://files.readme.io/04bb870171161dcaaa5363972d8d0277441ed578ce84d3c62c7bda91a421643d-bnpl_icon.png)](https://docs.payu.in/reference/get_checkout_details/)
    </Card>

    <Card>
      ![NEFT](https://files.readme.io/9392c375fc2fccecae588e5c287466be6cda1b0f039ace7a6f4139959e991189-neft_icon.png)
    </Card>
  </Cards>

  <br />

  ### Common Request Parameters (Required for all payment modes)

  The following are the common request parameters applicable for all the payment modes with Merchant Hosted Checkout integration:

  <HTMLBlock>{`
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
                                    <td>key<br><code>mandatory</code></td>
                                    <td style="white-space: normal; word-break: break-word;"><code>String</code> Merchant key provided by PayU during onboarding.</td>
                                    <td>JPG****.k</td>
                                    </tr>
                                    <tr>
                                    <td>txnid<br><code>mandatory</code></td>
                                    <td style="white-space: normal; word-break: break-word;"><code>String (25 characters)</code> The transaction ID is a reference number for a specific order generated by the merchant.</td>
                                    <td>ypl938459435</td>
                                    </tr>
                                    <tr>
                                    <td>amount<br><code>mandatory</code></td>
                                    <td style="white-space: normal; word-break: break-word;"><code>Float</code> The payment amount for the transaction.</td>
                                    <td>10.00</td>
                                    </tr>
                                    <tr>
                                    <td>productinfo<br><code>mandatory</code></td>
                                    <td style="white-space: normal; word-break: break-word;"><code>String (100 characters)</code> A brief description of the product.</td>
                                    <td>iPhone</td>
                                    </tr>
                                    <tr>
                                    <td>firstname<br><code>mandatory</code></td>
                                    <td style="white-space: normal; word-break: break-word;"><code>String (60 characters for production, 20 characters for test environment)</code> The first name of the customer.</td>
                                    <td>Ashish</td>
                                    </tr>
                                    <tr>
                                    <td>email<br><code>mandatory</code></td>
                                    <td style="white-space: normal; word-break: break-word;"><code>String (50 characters)</code> The email address of the customer.</td>
                                    <td>test@payu.in</td>
                                    </tr>
                                    <tr>
                                    <td>phone<br><code>mandatory</code></td>
                                    <td style="white-space: normal; word-break: break-word;"><code>String (50 characters)</code> The phone number of the customer.</td>
                                    <td>9876543210</td>
                                    </tr>
                                    <tr>
                                    <td>pg<br><code>mandatory</code></td>
                                    <td style="white-space: normal; word-break: break-word;"><code>String</code> Payment gateway/method identifier. <strong>This is the key difference from hosted checkout.</strong></td>
                                    <td>CC, NB, UPI, CASH</td>
                                    </tr>
                                    <tr>
                                    <td>bankcode<br><code>conditional</code></td>
                                    <td style="white-space: normal; word-break: break-word;"><code>String</code> Bank or payment provider specific code. Required for specific payment methods.</td>
                                    <td>HDFC, PAYTM, UPI</td>
                                    </tr>
                                    <tr>
                                    <td>surl<br><code>mandatory</code></td>
                                    <td style="white-space: normal; word-break: break-word;"><code>String (50 characters)</code> The success URL, which is the page PayU will redirect to if the transaction is successful.</td>
                                    <td>https://yoursite.com/success</td>
                                    </tr>
                                    <tr>
                                    <td>furl<br><code>mandatory</code></td>
                                    <td style="white-space: normal; word-break: break-word;"><code>String (50 characters)</code> The failure URL, which is the page PayU will redirect to if the transaction fails.</td>
                                    <td>https://yoursite.com/failure</td>
                                    </tr>
                                    <tr>
                                    <td>hash<br><code>mandatory</code></td>
                                    <td style="white-space: normal; word-break: break-word;"><code>String</code> It is the hash calculated by the merchant using SHA-512.</td>
                                    <td>[computed hash]</td>
                                    </tr>
                                    </tbody>
                                    </table>
  `}</HTMLBlock>

  ### Payment mode integration

  Select the card to get the step-by-step integration for the payment mode you wish to integrate:

  <Cards columns={3}>
    <Card>
      [![Net Banking Integration](https://files.readme.io/852ff36002aae339313722c8832cc7b5443c1bf7e5ca47571e9dd6971d51a2ae-netbanking_icon.png)](https://docs.payu.in/docs/collect-payments-with-net-banking-seamless)
    </Card>

    <Card>
      [![Cards Integration](https://files.readme.io/049c1e19c22dc0dee8f0f2b0a7facd89231c96a6b86d188af824cf1e87154d8e-cards_icon.png)](https://docs.payu.in/docs/collect-payments-with-cards-seamless)
    </Card>

    <Card>
      [![UPI Integration](https://files.readme.io/f5fe8045de9902d7ed2d1bb0a31568151638acaba086331df01826e0a4ebe1f2-upi_icon.png)](https://docs.payu.in/docs/collect-payments-with-upi-seamless)
    </Card>

    <Card>
      [![Wallets Integration](https://files.readme.io/0af7178db0a6130d39fb7b5270109e4251b0fd1b1455e54a936f29c145a97c87-wallets_icon.png)](https://docs.payu.in/docs/collect-payments-with-wallets-seamless)
    </Card>

    <Card>
      [![EMI Integration](https://files.readme.io/e32726065ea0eb0243a5c47583c54908d2f0732ea259206bae93f113f5284d52-emi_icon.png)](https://docs.payu.in/docs/collect-payments-with-emi-seamless)
    </Card>

    <Card>
      [![BNPL Integration](https://files.readme.io/04bb870171161dcaaa5363972d8d0277441ed578ce84d3c62c7bda91a421643d-bnpl_icon.png)](https://docs.payu.in/docs/collect-payments-with-bnpl)
    </Card>

    <Card>
      [![Pluxee Card Integration](https://files.readme.io/9392c375fc2fccecae588e5c287466be6cda1b0f039ace7a6f4139959e991189-neft_icon.png)](https://docs.payu.in/docs/collect-payments-with-eftnet-neftrtgs-seamless)
    </Card>

    <Card>
      [![EFTNET (NEFT/RTGS) Integration](https://files.readme.io/9392c375fc2fccecae588e5c287466be6cda1b0f039ace7a6f4139959e991189-neft_icon.png)](https://docs.payu.in/docs/collect-payments-with-eftnet-neftrtgs-seamless)
    </Card>
  </Cards>

  ## Sample request

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

      > **Note**: The hash logic for Verify Payment API is:
      > `sha512(key|command|var1|salt) sha512`

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
     2. Enter a test UPI ID: testsuccess\@gpay or 999999999\@payu
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
