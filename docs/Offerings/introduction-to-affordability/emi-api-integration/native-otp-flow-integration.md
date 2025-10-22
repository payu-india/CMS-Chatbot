---
title: Native OTP Flow Integration
excerpt: >-
  Native OTP Flow is a method of capturing transaction OTPs that happens on the
  merchant or PayU Payment page, rather than on a bank’s page through multiple
  hops. This means that customers stay on the merchant or PayU website to
  complete the card authentication process, entering the OTP on the same page
  where they are making the purchase, rather than being redirected to a
  3D-secure page. This reduces the number of steps in the checkout process,
  resulting in a faster and smoother experience for customers and a higher
  success rate for merchants. As a result, Native OTP Flow is preferred over OTP
  on a bank’s page.
deprecated: false
hidden: false
metadata:
  title: Integrate with Native OTP Flow for EMI
  description: ''
  robots: index
next:
  description: ''
---
You can enable Native OTP flow in EMI payments and collect payments. Currently, Native OTP can be enabled for the following types of EMI payments:

* [Debit Card](#debit-card-emi)
* [Cardless EMI](#cardless-emi)

<Callout icon="📘" theme="info">
  **Note**: If you don’t have EMI enabled, try requesting using Dashboard. For more information, refer to [Configure Checkout Settings](doc:checkout-payment-modes). If you could not request through Dashboard, contact your PayU Key Account Manager or PayU Support.
</Callout>

## Benefits

What are the advantages and why should merchants integrate this flow with PayU?

* **Increase Success Rates** — Native OTP flow improves Success Rates of card transactions by 3-5% depending upon the source of transactions.
* **Less Redirection** — It improves the overall user experience since multiple redirections are removed. Also, the customer never leaves the merchant website, which helps in providing a seamless experience. It also reduces drop rates due to users’ fluctuating internet speed issues.
* **PayU supports all major banks** — 15+ banks including HDFC, AXIS, ICICI, SBI, KOTAK, RBL, etc. – on this flow for Cards, cardless, CC EMI, DC EMI’s, and BNPLs.

This flow supports the latest native OTP generation flow (server-to-server) via Initiate Payment API, followed by the Submit OTP API, to initiate an S2S=4 transaction.

## Debit Card EMI

The steps involved in debit card integration with native OTP flow:

### Step 1: Check Pre-EMI Eligibility

Before initiating a payment request for a customer, it is necessary to check their eligibility using the **Get Checkout Details** API. For more information, refer to [Get Checkout Details API](ref:get_checkout_details#check-customer-eligibility).

### Step 2: Initiate the payment request

#### Request parameters

Send the transaction information to PayU through a server-to-server curl request to initiate the transaction. As a result of this API call, the customer will receive the OTP. For more information, refer to [Collect Payment API - Server-to-Server](ref:_payment_server_to_server).

<Accordion title="Request parameters" icon="fa-table">
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
          s2s\_device\_info
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must have the customer agent’s device.  <br />**Note**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
        </td>

        <td style={{ textAlign: "left" }}>
          Mozilla
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          s2s\_client\_ip
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must have the source IP of the customer.  <br />**Note**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
        </td>

        <td style={{ textAlign: "left" }}>
          10.11.101.11'
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          txn\_s2s\_flow
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This parameter must be passed with the value as 4.
        </td>

        <td style={{ textAlign: "left" }}>
          4
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

<Accordion title="Sample request" icon="fa-server">
  ```curl
  curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g" \
  -d "txnid=H6mUfE0ccAY94j" \
  -d "amount=20000.00" \
  -d "firstname=Ashish" \
  -d "email=test@gmail.com" \
  -d "phone=9876543210" \
  -d "productinfo=iPhone" \
  -d "pg=EMI" \
  -d "bankcode=EMIA3" \
  -d "surl=https://apiplayground-response.herokuapp.com/" \
  -d "furl=https://apiplayground-response.herokuapp.com/" \
  -d "ccnum=5123456789012346" \
  -d "ccexpmon=05" \
  -d "ccexpyr=2022" \
  -d "ccvv=123" \
  -d "ccname=" \
  -d "s2s_device_info=Mozilla" \
  -d "s2s_client_ip=10.11.101.11" \
  -d "txn_s2s_flow=4" \
  -d "hash=782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36"

  ```
  ```javascript
  /**
   * PayU Credit Card EMI Payment with Native OTP Flow Integration
   * 
   * IMPORTANT: This should only be executed server-side (e.g., in Node.js), never in the browser,
   * as it contains sensitive payment information.
   */

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

  // Native OTP flow parameters
  formData.append('s2s_device_info', 'Mozilla');  // Customer's device info
  formData.append('s2s_client_ip', '10.11.101.11'); // Customer's IP address
  formData.append('txn_s2s_flow', '4');           // Native OTP flow identifier

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
  fetch('https://test.payu.in/_payment', requestOptions)
    .then(response => {
      console.log('Status Code:', response.status);
      return response.text(); // or response.json() if you're sure it returns JSON
    })
    .then(data => {
      console.log('Response:', data);
      // Process payment response here and handle OTP flow
      // For Native OTP flow, you'll need to display OTP input to the user
      // and submit it in a subsequent request
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

  def process_emi_payment_with_native_otp() -> Dict[str, Any]:
      """
      Process credit card EMI payment with Native OTP flow using PayU's S2S integration
      
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
          
          # Native OTP flow parameters
          "s2s_device_info": "Mozilla",      # Customer's device info
          "s2s_client_ip": "10.11.101.11",   # Customer's IP address
          "txn_s2s_flow": "4",               # Native OTP flow identifier
          
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
      result = process_emi_payment_with_native_otp()
      print(f"Status Code: {result['status_code']}")
      if 'error' in result:
          print(f"Error: {result['error']}")
      print(f"Response: {result['response']}")
      
      # For Native OTP flow, you'll need to display OTP input to the user
      # and submit it in a subsequent request

  ```
  ```php
  <?php
  /**
   * Process credit card EMI payment with Native OTP flow using PayU's S2S integration
   * 
   * IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
   * 
   * @return array Response from PayU API
   */
  function processEmiPaymentWithNativeOtp() {
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
          
          // Native OTP flow parameters
          "s2s_device_info" => "Mozilla",       // Customer's device info
          "s2s_client_ip" => "10.11.101.11",    // Customer's IP address
          "txn_s2s_flow" => "4",                // Native OTP flow identifier
          
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
      
      // Process the response
      // For Native OTP flow, you'll need to display OTP input to the user
      // and submit it in a subsequent request
      return [
          "status_code" => $statusCode,
          "response" => $response
      ];
  }

  // Example usage
  $result = processEmiPaymentWithNativeOtp();
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
   * PayU Credit Card EMI Payment with Native OTP Flow Integration
   * 
   * IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
   */
  public class PayUEmiPaymentWithNativeOtpProcessor {
      
      // API endpoint
      private static final String PAYU_TEST_URL = "https://test.payu.in/_payment";
      
      /**
       * Process credit card EMI payment with Native OTP flow through PayU
       * @return PaymentResponse containing status and response data
       */
      public PaymentResponse processEmiPaymentWithNativeOtp() {
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
              
              // Native OTP flow parameters
              params.put("s2s_device_info", "Mozilla");       // Customer's device info
              params.put("s2s_client_ip", "10.11.101.11");    // Customer's IP address
              params.put("txn_s2s_flow", "4");                // Native OTP flow identifier
              
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
              
              // Process the response
              // For Native OTP flow, you'll need to display OTP input to the user
              // and submit it in a subsequent request
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
          PayUEmiPaymentWithNativeOtpProcessor processor = new PayUEmiPaymentWithNativeOtpProcessor();
          PaymentResponse result = processor.processEmiPaymentWithNativeOtp();
          
          System.out.println("Status Code: " + result.getStatusCode());
          if (result.isSuccess()) {
              System.out.println("Response: " + result.getResponse());
              // Here you would extract OTP page details from the response
              // and display the OTP input to the user
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

  namespace PayUEmiNativeOtpIntegration
  {
      /// <summary>
      /// PayU Credit Card EMI Payment with Native OTP Flow Processor
      /// 
      /// IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
      /// </summary>
      public class PayUEmiPaymentWithNativeOtpProcessor
      {
          // API endpoint
          private const string PayuTestUrl = "https://test.payu.in/_payment";
          
          /// <summary>
          /// Process credit card EMI payment with Native OTP flow through PayU
          /// </summary>
          /// <returns>PaymentResponse containing status and response data</returns>
          public async Task<PaymentResponse> ProcessEmiPaymentWithNativeOtpAsync()
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
                      
                      // Native OTP flow parameters
                      { "s2s_device_info", "Mozilla" },        // Customer's device info
                      { "s2s_client_ip", "10.11.101.11" },     // Customer's IP address
                      { "txn_s2s_flow", "4" },                 // Native OTP flow identifier
                      
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
                      
                      // Process the response
                      // For Native OTP flow, you'll need to display OTP input to the user
                      // and submit it in a subsequent request
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
              var processor = new PayUEmiPaymentWithNativeOtpProcessor();
              var result = await processor.ProcessEmiPaymentWithNativeOtpAsync();
              
              Console.WriteLine($"Status Code: {result.StatusCode}");
              if (result.IsSuccess)
              {
                  Console.WriteLine($"Response: {result.Response}");
                  // Here you would extract OTP page details from the response
                  // and display the OTP input to the user
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
<Accordion title="Sample response" icon="fa-database">

  ```json
  {
     "metaData": {
        "message": "No Error",
        "referenceId": "b6035f64240b1862295bc571952cf984",
        "statusCode": "E000",
        "txnId": "payuTestTransaction2746829",
        "unmappedStatus": "success",
        "submitOtp": {
           "status": "success"
        }
     },
     "result": {
        "mihpayid": "15270336226",
        "mode": "CC",
        "status": "success",
        "key": "4wvMqy",
        "txnid": "payuTestTransaction2746829",
        "amount": "1.10",
        "addedon": "2022-06-01 17:39:29",
        "productinfo": "Product Info",
        "firstname": "Postman",
        "lastname": "",
        "address1": "",
        "address2": "",
        "city": "",
        "state": "",
        "country": "",
        "zipcode": "",
        "email": "test@payu.in",
        "phone": "9988776655",
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
        "card_token": "",
        "card_no": "XXXXXXXXXXXX8006",
        "field0": "",
        "field1": "6540854745166970506094",
        "field2": "947167",
        "field3": "1.10",
        "field4": "15270336226",
        "field5": "100",
        "field6": "",
        "field7": "AUTHPOSITIVE",
        "field8": "",
        "field9": "Transaction is Successful",
        "payment_source": "payuPureS2SAuth",
        "PG_TYPE": "DC-PG",
        "error": "E000",
        "error_Message": "No Error",
        "cardToken": "",
        "net_amount_debit": "1.1",
        "discount": "0.00",
        "offer_key": "",
        "offer_availed": "",
        "unmappedstatus": "captured",
        "hash": "cdc409dfd15a842b8d15d6627d0027619882ed800773fa413cef491ae8ff2ef0cdfa654680ba4c8f3567313c6a6b00b94cb3bb5e16bad21d26be01216a69af41",
        "bank_ref_no": "6540854745166970506094",
        "bank_ref_num": "6540854745166970506094",
        "bankcode": "CC",
        "surl": "",
        "curl": "",
        "furl": "",
        "card_hash": "fdb59253e36daf8b3969525ae3799ccb4bb41993a5d2fcaf22737ec3ac8b90ab"
     }
  }
  ```

  ### Step 3: Submit the OTP

  Once your customer enters the OTP on the payment page (postUrl/acsTemplate), pass the OTP using the **Submit OTP** API. For more information, refer to [Submit OTP API](ref:submit-otp-to-payu).

  **Resend OTP**

  If the customer enters the incorrect OTP or an expired OTP, use [Resend OTP API](ref:resend-otp-api) to handle the Resend OTP request made by a customer.
## Step 4: Verify Payment
  <Verify_Payment_Tabs />

  ## Cardless EMI

  The steps involved in cardless EMI with Native OTP:

  1. [Check pre-EMI eligibility](#step-1-check-pre-emi-eligibility)
  2. [Initiate the payment request](#step-2-initiate-the-payment-to-payu)
  3. [Submit the OTP](#step-3-submit-the-OTP)

## Step 1: Check pre-EMI eligibility
Before initiating a payment request for a customer, it is necessary to check their eligibility using the **Get Checkout Details** API. For more information, refer to [Get Checkout Details API](ref:get_checkout_details#check-customer-eligibility).


</Accordion>
## Step 2: Initiate the payment request
<Accordion title="Request parameters" icon="fa-table">
Send the following additional parameters to PayU through a server-to-server curl request to initiate the payment. As a result of this API call, the customer will receive the OTP. For sample request and response, refer to [Collect Payment API - Server-to-Server](ref:_payment_server_to_server).

| **Parameter**         | **Description**                                      | **Example**      |
|------------------------|------------------------------------------------------|------------------|
| panNumber `mandatory` | `String` PAN number of the customer.                  | ABCDE1234A       |
| s2s\_device\_info `mandatory` | `String` This parameter must have the customer agent's device. | Mozilla          |
| s2s\_client\_ip `mandatory`   | `String` This parameter must have the source IP of the customer. | 10.11.101.11     |
| txn\_s2s\_flow `mandatory`    | `String` This parameter must be passed with the value as 4.    | 4                |

📘 **Notes for panNumber**:
- **Only 4-digit number of the PAN**: Pass the 4-digit numeral in a sequential order as in the PAN.
- This parameter is mandatory for ICICI Bank and HDFC Bank Cardless EMI. Not mandatory for other banks.
- The data validation performed is either the whole PAN card number or 4-digit number of the PAN:
  - **Whole PAN card number**: For validating the whole PAN card number:
    - It should be ten characters long.
    - The first five characters should be any uppercase alphabets.
    - The next four characters should be any number from 0 to 9.
    - The last (tenth) character should be any uppercase alphabet. It should not contain white spaces.
</Accordion>

<Accordion title="Sample request" icon="fa-code">
Below is a sample cURL request for initiating the payment.

```curl
curl -X POST "https://test.payu.in/_payment" \
-H "accept: application/json" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "key=JP***g" \
-d "txnid=EaE4ZO3vU4iPsp" \
-d "amount=10.00" \
-d "firstname=Ashish" \
-d "email=test@gmail.com" \
-d "phone=9876543210" \
-d "productinfo=iPhone" \
-d "pg=EMI" \
-d "bankcode=EMI03" \
-d "surl=https://apiplayground-response.herokuapp.com/" \
-d "furl=https://apiplayground-response.herokuapp.com/" \
-d "ccnum=1234" \
-d "ccexpmon=05" \
-d "ccexpyr=2022" \
-d "ccvv=123" \
-d "ccname=undefined" \
-d "store_card_token=1234 4567 2456 3566" \
-d "storecard_token_type=1" \
-d 'additional_info={"last4Digits": "1234", "tavv": "ABCDEFGH","trid":"1234567890", "tokenRefNo":"abcde123456"}' \
-d "panNumber=ABCDE1234A" \
-d "s2s_device_info=Mozilla" \
-d "s2s_client_ip=10.11.101.11" \
-d "txn_s2s_flow=4" \
-d "hash=fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"
```

Additional examples for this request have been provided in **JavaScript, Python, PHP, Java**, and **C#**. Each programming language script includes detailed API integration examples for initiating a Cardless EMI payment.
</Accordion>


### Step 3: Submit the OTP
Once your customer enters the OTP on the payment page (postUrl/acsTemplate), pass the OTP using the **Submit OTP** API. For more information, refer to [Submit OTP API](ref:submit-otp-to-payu).
####Resend OTP
If the customer enters the incorrect OTP or an expired OTP, use [Resend OTP API](ref:resend-otp-api) to handle the **Resend OTP** request made by the customer.


## Step 4: Verify Payment
  <Verify_Payment_Tabs />