---
title: EMI
api:
  file: updated_emi_merchant_hosted.json
  operationId: MerchantHostedCheckout-EMI
hidden: false
metadata:
  title: Collect Payments using EMI - Merchant Hosted Checkout
  description: >-
    Explore PayU's Merchant Hosted EMI solutions, enabling easy integration of
    EMI payment options for e-commerce platforms. Learn about API integration,
    supported banks, and flexible installment plans to enhance customer
    experience and boost sales.
  keywords:
    - EMI Merchant Hosted Checkout Collect Payment API
    - Simulator for PayU payment collection
    - EMI Custom Checkout integration with PayU
    - Collect payments using PayU API
    - Collect Payment API for EMI Merchant Hosted Checkout
    - _payment API for EMI Merchant Hosted Checkout
    - _payment API simulation for EMI Custom Checkout
    - _payment API simulation for EMI Merchant Hosted Checkout
    - "Equated Monthly Installment\_Merchant Hosted Checkout Collect Payment API"
    - Simulator for PayU payment collection
    - "Equated Monthly Installment\_Custom Checkout integration with PayU"
    - "Collect Payment API for Equated Monthly Installment\_Merchant Hosted Checkout"
---
EMI as a payment option gives your customers the freedom and affordability to purchase expensive items without having to deal with banks or NBFCs as intermediaries.

You can collect payments from customers in EMI using the Merchant Hosted integration. You need to ensure that **EMI** for the **pg** parameter and EMI code based on the card issuer and tenure for the **bankcode** parameter is posted.

<PaymentAPIEnvironment />

<Accordion title="Sample request" icon="fa-server">
  ```curl
  curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=H6mUfE0ccAY94j&amount=20000.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=EMI&bankcode=EMIA3&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=&hash=782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36"
  ```
  ```javascript
  /**
   * PayU Credit Card EMI Payment Integration using Fetch API
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
      // Process payment response here, which may include EMI options
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

  def process_credit_card_emi_payment() -> Dict[str, Any]:
      """
      Process credit card EMI payment using PayU's Merchant Hosted Checkout
      
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
      result = process_credit_card_emi_payment()
      print(f"Status Code: {result['status_code']}")
      if 'error' in result:
          print(f"Error: {result['error']}")
      print(f"Response: {result['response']}")

  ```
  ```php
  <?php
  /**
   * Process credit card EMI payment using PayU's Merchant Hosted Checkout
   * 
   * IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
   * 
   * @return array Response from PayU API
   */
  function processCreditCardEmiPayment() {
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
  $result = processCreditCardEmiPayment();
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
   * PayU Credit Card EMI Payment Processor for Merchant Hosted Checkout
   * 
   * IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
   */
  public class PayUCreditCardEmiPaymentProcessor {
      
      // API endpoint
      private static final String PAYU_TEST_URL = "https://test.payu.in/_payment";
      
      /**
       * Process credit card EMI payment through PayU
       * @return PaymentResponse containing status and response data
       */
      public PaymentResponse processCreditCardEmiPayment() {
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
          PayUCreditCardEmiPaymentProcessor processor = new PayUCreditCardEmiPaymentProcessor();
          PaymentResponse result = processor.processCreditCardEmiPayment();
          
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

  namespace PayUCreditCardEmiIntegration
  {
      /// <summary>
      /// PayU Credit Card EMI Payment Processor for Merchant Hosted Checkout
      /// 
      /// IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
      /// </summary>
      public class PayUCreditCardEmiPaymentProcessor
      {
          // API endpoint
          private const string PayuTestUrl = "https://test.payu.in/_payment";
          
          /// <summary>
          /// Process credit card EMI payment through PayU
          /// </summary>
          /// <returns>PaymentResponse containing status and response data</returns>
          public async Task<PaymentResponse> ProcessCreditCardEmiPaymentAsync()
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
              var processor = new PayUCreditCardEmiPaymentProcessor();
              var result = await processor.ProcessCreditCardEmiPaymentAsync();
              
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

<br />

<Accordion title="Sample response" icon="fa-reply">
  The formatted sample response from PayU is similar to the following:

  ```
  Array
  (
      [mihpayid] => 403993715523602563
      [status] => success
      [unmappedstatus] => captured
      [key] => JP***g
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
      [bankcode]=> EMIA3
      [error] => E000
      [error_Message] => No Error
      [name_on_card] => payu
      [cardnum] =>512345XXXXXX2346
  )
  ```
</Accordion>

## Request parameters

<Callout icon="📘" theme="info">
  **Reference**: For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
</Callout>

<Accordion title="Values to be used in Test environment" icon="fa-flask">
  * You can used any EMI code listed in the <a href="emi-codes" target="_blank">EMI Codes</a> section. section and test cards listed in the <a href="https://docs.payu.in/docs/test-cards-upi-id-and-wallets#emi-test-cards" target="_blank">Test Cards</a> section. For example, the following values can be used:

  |                   |                         |                   |
  | :---------------- | :---------------------- | :---------------- |
  | bankcode: EMIA3   | ccnum: 5123456789012346 | ccexpmon: 05      |
  | ccexpyr: 2025     | ccvv: 123               | ccname: Any value |
  | phone: 9123412345 |                         |                   |

  * For the **amount** parameter, use **>=INR 1000** in the Test environment.
</Accordion>

> ❗️ Error handling
>
> If any error message is displayed with an error code, refer to the [Error Codes](ref:error-codes) section. to understand the reason for these error codes.
