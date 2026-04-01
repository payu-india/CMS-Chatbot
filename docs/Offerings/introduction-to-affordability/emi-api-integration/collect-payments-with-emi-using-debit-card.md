---
title: Debit Card - Merchant Hosted Checkout
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: >-
    Integrate with Debit Card with EMI using Merchant Hosted Checkout
    Integration
  description: ''
  keywords:
    - Seamless EMI Debit Card Integration
    - Merchant Hosted EMI Debit Card
    - PayU Debit Card EMI API
    - Debit Card EMI Conversion PayU
  robots: index
next:
  description: ''
---
When your customer wants to opt for the EMI option with debit cards, you can use EMI APIs to check the pre-eligibility of the debit card and calculate the EMI amount, interest, processing fee, or No-Cost EMI, and tenure. If the customer is eligible, you can post the transaction with EMI conversion.

<Callout icon="📘" theme="info">
  **Notes**: 

  * You can create EMI offers using the PayU Dashboard and use them for collecting payments as described in this procedure. For more information, refer to the [Create a No-Cost EMI Offer](doc:create-a-no-cost-emi-offer).
  * You can handle Guest Checkout transactions for EMI integration. For more information, refer to[ Cards Integration > Handling Guest Checkout Transactions](doc:collect-payments-with-cards-seamless#handling-guest-checkout-transactions).
</Callout>

The following video explains how Debit Card EMIs will help your business and how to enable it:

<Embed url="https://www.youtube.com/watch?v=HCD16tnCsek" href="https://www.youtube.com/watch?v=HCD16tnCsek" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FHCD16tnCsek%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DHCD16tnCsek%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FHCD16tnCsek%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

<br />

**Steps to integrate**

<Cards columns={3}>
  <Card title="1. Check pre-EMI eligibility for debit card" href="#step-1-check-pre-emi-eligibility-for-debit-card">
    Verify if the debit card is eligible for EMI before proceeding with the transaction

    <br />
  </Card>

  <Card title="2. Calculate the EMI interest" href="#step-2-calculate-the-emi-interest">
    Calculate the EMI interest rates and payment schedule for the transaction

    <br />
  </Card>

  <Card title="3. Post the transaction request and check response" href="#step-3-post-the-transaction-request-and-check-response">
    Submit the EMI transaction request to PayU and verify the initial response

    <br />
  </Card>

  <Card title="4. Check the PayU response" href="#step-4-check-the-payu-response">
    Process and handle the response received from PayU after transaction submission

    <br />
  </Card>

  <Card title="5. Verify the payment" href="#step-5-verify-the-payment">
    Verify the payment status and ensure successful EMI transaction completion
  </Card>

  <br />
</Cards>

<Callout icon="📮" theme="default">
  **Postman Collection**: Download the **Merchant Hosted Checkout > Debit Card EMI** Postman Collection from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/p8thbg4/integrate-with-debit-card](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/p8thbg4/integrate-with-debit-card)
</Callout>

## Step 1: Check pre-EMI eligibility for debit card

After collecting the customer’s card and the amount to be paid, check the Pre-EMI eligibility based on the customer’s mobile number using the getCheckoutDetails API. For more information on how to use the **getCheckoutDetails** API, refer to [Get Checkout Details API](ref:get_checkout_details#check-customer-eligibility)

## Step 2: Calculate the EMI interest

Use the **getEmiAmountAccordingToInterest** API to calculate the EMI interest. For more information, refer to [Get EMI According to Interest API](ref:get_emi_according_to_interest_api).

## Step 3: Post the transaction request and check response

Post the following parameters for using the Debit Card  EMI. For complete list of parameters, refer to [Collect Payment API - EMI](ref:_payment_merchant_hosted_emi) for the complete list parameters with **Try It** experience.

### Request parameters

<Accordion title="Request parameters" icon="fa-database">
  <HTMLBlock>{`
                          <table>
                            <thead>
                              <tr>
                                <th>Parameter</th>
                                <th>Description</th>
                                <th>Example</th>
                              </tr>
                            </thead>
                            <tbody>
                              <tr>
                                <td>key <code>mandatory</code></td>
                                <td><code>String</code> Merchant key provided by PayU during onboarding.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>txnid <code>mandatory</code></td>
                                <td><code>String</code> The transaction ID is a reference number for a specific order that is generated by the merchant.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>amount <code>mandatory</code></td>
                                <td><code>String</code> The payment amount for the transaction.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>productinfo <code>mandatory</code></td>
                                <td><code>String</code> A brief description of the product.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>firstname <code>mandatory</code></td>
                                <td><code>String</code> The first name of the customer.</td>
                                <td>Ashish</td>
                              </tr>
                              <tr>
                                <td>email <code>mandatory</code></td>
                                <td><code>String</code> The email address of the customer.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>phone <code>mandatory</code></td>
                                <td><code>String</code> The phone number of the customer.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>pg <code>mandatory</code></td>
                                <td><code>String</code> It defines the payment category that the merchant wants the customer to see by default on the PayU's payment page. In this integration, "EMI" must be specified.</td>
                                <td>EMI</td>
                              </tr>
                              <tr>
                                <td>bankcode <code>mandatory</code></td>
                                <td><code>String</code> Post this parameter to identify payment options with unique bank codes and use getEmiAmountAccordingToInterest API to check for EMI code for corresponding tenure. For the list of EMI codes, refer to EMI Codes.</td>
                                <td>EMI03</td>
                              </tr>
                              <tr>
                                <td>ccnum <code>mandatory</code></td>
                                <td><code>String</code> Use 13-19 digit card number for credit/debit cards (15 digits for AMEX, 13-19 for Maestro) and validate with LUHN algorithm. Refer to Card Number Formats and display error message on invalid input.</td>
                                <td>5123456789012346</td>
                              </tr>
                              <tr>
                                <td>ccname <code>mandatory</code></td>
                                <td><code>String</code> This parameter must contain the name on card – as entered by the customer for the transaction.</td>
                                <td>Ashish Kumar</td>
                              </tr>
                              <tr>
                                <td>ccvv <code>mandatory</code></td>
                                <td><code>String</code> Use 3-digit CVV number for credit/debit cards and 4-digit security code (4DBC/CID) for AMEX cards. Validate with BIN API.</td>
                                <td>123</td>
                              </tr>
                              <tr>
                                <td>ccexpmon <code>mandatory</code></td>
                                <td><code>String</code> This parameter must contain the card's expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format. For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively.</td>
                                <td>10</td>
                              </tr>
                              <tr>
                                <td>ccexpyr <code>mandatory</code></td>
                                <td><code>String</code> This parameter must contain the card's expiry year – as entered by the customer for the transaction. It must be of four digits.</td>
                                <td>2021</td>
                              </tr>
                              <tr>
                                <td>threeDS2RequestData <code>optional</code></td>
                                <td><code>JSON</code> This parameter must contain the following information in JSON format. For more information, refer to Handling 3DS Secure 2.0 Transaction.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>furl <code>mandatory</code></td>
                                <td><code>String</code> The success URL, which is the page PayU will redirect to if the transaction is successful.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>surl <code>mandatory</code></td>
                                <td><code>String</code> The Failure URL, which is the page PayU will redirect to if the transaction is failed.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>hash <code>mandatory</code></td>
                                <td><code>String</code> It is the hash calculated by the merchant. The hash calculation logic is: <code>sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)</code></td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>address1 <code>optional</code></td>
                                <td><code>String</code> The first line of the billing address. <em>For Fraud Detection</em>: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>address2 <code>optional</code></td>
                                <td><code>String</code> The second line of the billing address.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>city <code>optional</code></td>
                                <td><code>String</code> The city where your customer resides as part of the billing address.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>state <code>optional</code></td>
                                <td><code>String</code> The state where your customer resides as part of the billing address.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>country <code>optional</code></td>
                                <td><code>String</code> The country where your customer resides.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>zipcode <code>optional</code></td>
                                <td><code>String</code> Billing address zip code is mandatory for the cardless EMI option. <code>Character Limit</code>-20</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>udf1 <code>optional</code></td>
                                <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>udf2 <code>optional</code></td>
                                <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>udf3 <code>optional</code></td>
                                <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>udf4 <code>optional</code></td>
                                <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                                <td></td>
                              </tr>
                              <tr>
                                <td>udf5 <code>optional</code></td>
                                <td><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</td>
                                <td></td>
                              </tr>
                            </tbody>
                          </table>
  `}</HTMLBlock>
</Accordion>

<HashingRequestParameters />

### Sample request

<Accordion title="Sample request" icon="fa-server">
  ```curl
  curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=H6mUfE0ccAY94j&amount=20000.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=EMI&bankcode=EMIA3&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=&hash=782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36"
  ```
  ```javascript
  /**
   * PayU Debit Card EMI Payment Integration using Fetch API
   * 
   * IMPORTANT: This should only be executed server-side (e.g., in Node.js), never in the browser,
   * as it contains sensitive payment information.
   */

  // Payment endpoint
  const url = 'https://test.payu.in/_payment';

  // Form data parameters
  const formData = new URLSearchParams();
  formData.append('key', 'JP***g');                // Your merchant key
  formData.append('txnid', 'H6mUfE0ccAY94j');     // Unique transaction ID
  formData.append('amount', '20000.00');          // Payment amount
  formData.append('firstname', 'Ashish');         // Customer's name
  formData.append('email', 'test@gmail.com');     // Customer's email
  formData.append('phone', '9876543210');         // Customer's phone
  formData.append('productinfo', 'iPhone');       // Product information
  formData.append('pg', 'EMI');                   // Payment gateway (EMI)
  formData.append('bankcode', 'EMIA3');           // Bank code (Axis Bank EMI)
  formData.append('surl', 'https://apiplayground-response.herokuapp.com/'); // Success URL
  formData.append('furl', 'https://apiplayground-response.herokuapp.com/'); // Failure URL
  // Card details - SENSITIVE DATA
  formData.append('ccnum', '5123456789012346');   // Card number
  formData.append('ccexpmon', '05');              // Expiry month
  formData.append('ccexpyr', '2022');             // Expiry year 
  formData.append('ccvv', '123');                 // CVV
  formData.append('ccname', '');                  // Cardholder name
  // Security hash
  formData.append('hash', '782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36');

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

  def process_debit_card_emi_payment() -> Dict[str, Any]:
      """
      Process debit card EMI payment using PayU's Merchant Hosted Checkout
      
      IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
      
      Returns:
          Dictionary with response from PayU API
      """
      # API endpoint
      url = "https://test.payu.in/_payment"
      
      # Prepare the form data
      payload = {
          "key": "JP***g",                   # Your merchant key
          "txnid": "H6mUfE0ccAY94j",         # Unique transaction ID
          "amount": "20000.00",              # Payment amount
          "firstname": "Ashish",             # Customer's name
          "email": "test@gmail.com",         # Customer's email
          "phone": "9876543210",             # Customer's phone
          "productinfo": "iPhone",           # Product information
          "pg": "EMI",                       # Payment gateway (EMI)
          "bankcode": "EMIA3",               # Bank code (Axis Bank EMI)
          "surl": "https://apiplayground-response.herokuapp.com/", # Success URL
          "furl": "https://apiplayground-response.herokuapp.com/", # Failure URL
          # Card details - SENSITIVE DATA
          "ccnum": "5123456789012346",       # Card number
          "ccexpmon": "05",                  # Expiry month
          "ccexpyr": "2022",                 # Expiry year
          "ccvv": "123",                     # CVV
          "ccname": "",                      # Cardholder name
          # Security hash
          "hash": "782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36"
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
      result = process_debit_card_emi_payment()
      print(f"Status Code: {result['status_code']}")
      if 'error' in result:
          print(f"Error: {result['error']}")
      print(f"Response: {result['response']}")

  ```
  ```php
  <?php
  /**
   * Process debit card EMI payment using PayU's Merchant Hosted Checkout
   * 
   * IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
   * 
   * @return array Response from PayU API
   */
  function processDebitCardEmiPayment() {
      // API endpoint
      $url = "https://test.payu.in/_payment";
      
      // Prepare the form data
      $payload = [
          "key" => "JP***g",                    // Your merchant key
          "txnid" => "H6mUfE0ccAY94j",          // Unique transaction ID
          "amount" => "20000.00",               // Payment amount
          "firstname" => "Ashish",              // Customer's name
          "email" => "test@gmail.com",          // Customer's email
          "phone" => "9876543210",              // Customer's phone
          "productinfo" => "iPhone",            // Product information
          "pg" => "EMI",                        // Payment gateway (EMI)
          "bankcode" => "EMIA3",                // Bank code (Axis Bank EMI)
          "surl" => "https://apiplayground-response.herokuapp.com/", // Success URL
          "furl" => "https://apiplayground-response.herokuapp.com/", // Failure URL
          // Card details - SENSITIVE DATA
          "ccnum" => "5123456789012346",        // Card number
          "ccexpmon" => "05",                   // Expiry month
          "ccexpyr" => "2022",                  // Expiry year
          "ccvv" => "123",                      // CVV
          "ccname" => "",                       // Cardholder name
          // Security hash
          "hash" => "782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36"
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
  $result = processDebitCardEmiPayment();
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
   * PayU Debit Card EMI Payment Processor for Merchant Hosted Checkout
   * 
   * IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
   */
  public class PayUDebitCardEmiPaymentProcessor {
      
      // API endpoint
      private static final String PAYU_TEST_URL = "https://test.payu.in/_payment";
      
      /**
       * Process debit card EMI payment through PayU
       * @return PaymentResponse containing status and response data
       */
      public PaymentResponse processDebitCardEmiPayment() {
          try {
              // Initialize URL
              URL url = new URL(PAYU_TEST_URL);
              
              // Prepare form parameters
              Map<String, String> params = new HashMap<>();
              params.put("key", "JP***g");                    // Your merchant key
              params.put("txnid", "H6mUfE0ccAY94j");          // Unique transaction ID
              params.put("amount", "20000.00");               // Payment amount
              params.put("firstname", "Ashish");              // Customer's name
              params.put("email", "test@gmail.com");          // Customer's email
              params.put("phone", "9876543210");              // Customer's phone
              params.put("productinfo", "iPhone");            // Product information
              params.put("pg", "EMI");                        // Payment gateway (EMI)
              params.put("bankcode", "EMIA3");                // Bank code (Axis Bank EMI)
              params.put("surl", "https://apiplayground-response.herokuapp.com/"); // Success URL
              params.put("furl", "https://apiplayground-response.herokuapp.com/"); // Failure URL
              // Card details - SENSITIVE DATA
              params.put("ccnum", "5123456789012346");        // Card number
              params.put("ccexpmon", "05");                   // Expiry month
              params.put("ccexpyr", "2022");                  // Expiry year
              params.put("ccvv", "123");                      // CVV
              params.put("ccname", "");                       // Cardholder name
              // Security hash
              params.put("hash", "782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36");
              
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
          PayUDebitCardEmiPaymentProcessor processor = new PayUDebitCardEmiPaymentProcessor();
          PaymentResponse result = processor.processDebitCardEmiPayment();
          
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

  namespace PayUDebitCardEmiIntegration
  {
      /// <summary>
      /// PayU Debit Card EMI Payment Processor for Merchant Hosted Checkout
      /// 
      /// IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
      /// </summary>
      public class PayUDebitCardEmiPaymentProcessor
      {
          // API endpoint
          private const string PayuTestUrl = "https://test.payu.in/_payment";
          
          /// <summary>
          /// Process debit card EMI payment through PayU
          /// </summary>
          /// <returns>PaymentResponse containing status and response data</returns>
          public async Task<PaymentResponse> ProcessDebitCardEmiPaymentAsync()
          {
              try
              {
                  // Prepare form parameters
                  var formData = new Dictionary<string, string>
                  {
                      { "key", "JP***g" },                     // Your merchant key
                      { "txnid", "H6mUfE0ccAY94j" },           // Unique transaction ID
                      { "amount", "20000.00" },                // Payment amount
                      { "firstname", "Ashish" },               // Customer's name
                      { "email", "test@gmail.com" },           // Customer's email
                      { "phone", "9876543210" },               // Customer's phone
                      { "productinfo", "iPhone" },             // Product information
                      { "pg", "EMI" },                         // Payment gateway (EMI)
                      { "bankcode", "EMIA3" },                 // Bank code (Axis Bank EMI)
                      { "surl", "https://apiplayground-response.herokuapp.com/" }, // Success URL
                      { "furl", "https://apiplayground-response.herokuapp.com/" }, // Failure URL
                      // Card details - SENSITIVE DATA
                      { "ccnum", "5123456789012346" },         // Card number
                      { "ccexpmon", "05" },                    // Expiry month
                      { "ccexpyr", "2022" },                   // Expiry year
                      { "ccvv", "123" },                       // CVV
                      { "ccname", "" },                        // Cardholder name
                      // Security hash
                      { "hash", "782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36" }
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
              var processor = new PayUDebitCardEmiPaymentProcessor();
              var result = await processor.ProcessDebitCardEmiPaymentAsync();
              
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

## Step 4: Check the PayU response

<ReverseHashing />

### Sample response

The formatted sample response body is similar to the following, and you need to look for the following parameters:

* PG_TYPE
* bankcode

<br />

<Accordion title="Sample response" icon="fa-check-circle">
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
      [phone] => 9123412345
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
      [field1] => 
      [field2] => 
      [field3] => 
      [field4] => 
      [field5] => 
      [field6] => 
      [field7] =>
      [field8] => 
      [field9] => Transaction Completed Successfully
      [payment_source] => payu
      [PG_TYPE] => EMI-PG
      [bank_ref_num] => 3d7cc4a4-00c8-4705-a0e7-5708d2c2bb75
      [bankcode]=> ICICID03
      [error] => E000
      [error_Message] => No Error
      [name_on_card] => payu
      [cardnum] =>437541XXXXXX2346
  )
  ```
</Accordion>

## Step 5: Verify the payment

<Verify_Payment_Tabs />
