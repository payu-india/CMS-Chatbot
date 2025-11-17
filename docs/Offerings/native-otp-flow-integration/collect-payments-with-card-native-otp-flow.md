---
title: Cards - Native OTP Flow
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  title: ''
  description: ''
  robots: index
---
The steps involved in cardless EMI with Native OTP:

1. [Check pre-EMI eligibility](#step-1-check-pre-emi-eligibility)
2. [Initiate the payment request](#step-2-initiate-the-payment-to-payu)
3. [Submit the OTP](#step-3-submit-the-OTP)

## Step 1: Check pre-EMI eligibility

Before initiating a payment request for a customer, it is necessary to check their eligibility using the **Get Checkout Details** API. For more information, refer to [Get Checkout Details API](ref:get_checkout_details#check-customer-eligibility).

## Step 2: Initiate the payment request

### Request parameters

Send the following additional parameters to PayU through a server-to-server curl request to initiate the payment. As a result of this API call, the customer will receive the OTP. For sample request and response, refer to [Collect Payment API - Server-to-Server](ref:_payment_server_to_server).

<Table align={["left","left","left"]}>
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
        panNumber
        `mandatory`
      </td>

      <td>
        `String`  PAN number of the customer.
      </td>

      <td>
        ABCDE1234A
      </td>
    </tr>

    <tr>
      <td>
        s2s_device_info
        `mandatory`
      </td>

      <td>
        `String`  This parameter must have the customer agent’s device.
      </td>

      <td>
        Mozilla
      </td>
    </tr>

    <tr>
      <td>
        s2s_client_ip
        `mandatory`
      </td>

      <td>
        `String` This parameter must have the source IP of the customer.
      </td>

      <td>
        10.11.101.11
      </td>
    </tr>

    <tr>
      <td>
        txn_s2s_flow
        `mandatory`
      </td>

      <td>
        `StringString` This parameter must be passed with the value as 4.
      </td>

      <td>
        4
      </td>
    </tr>
  </tbody>
</Table>

<Callout icon="📘" theme="info">
  **Notes for panNumber**:

  * **Only 4-digit number of the PAN**: Pass the 4-digit numeral in a sequential order as in the PAN.
  * This parameter is mandatory for ICICI Bank and HDFC Bank Cardless EMI. Not mandatory for other banks
  * The data validation performed is either the whole PAN card number or 4-dig-t number of the PAN.
    * Whole PAN card Number: For validating the whole PAN Card number:
      * It should be ten characters long.
      * The first five characters should be any upper case alphabets.
      * The next four-characters should be any number from 0 to 9.
      * The last(tenth) character should be any upper case alphabet. It should not contain any white spaces.
</Callout>

### Sample request

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
-d "pg=CC" \
-d "bankcode=CC" \
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
```javascript
/**
 * PayU Cardless EMI Payment with Native OTP Flow Integration
 * 
 * IMPORTANT: This should only be executed server-side (e.g., in Node.js), never in the browser,
 * as it contains sensitive payment and PAN information.
 */

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
formData.append('surl', 'https://apiplayground-response.herokuapp.com/'); // Success URL
formData.append('furl', 'https://apiplayground-response.herokuapp.com/'); // Failure URL
// Card and token details
formData.append('ccnum', '1234');                 // Limited card details
formData.append('ccexpmon', '05');                // Expiry month
formData.append('ccexpyr', '2022');               // Expiry year 
formData.append('ccvv', '123');                   // CVV
formData.append('ccname', 'undefined');           // Cardholder name
formData.append('store_card_token', '1234 4567 2456 3566'); // Tokenized card
formData.append('storecard_token_type', '1');     // Token type
formData.append('additional_info', JSON.stringify(additionalInfo)); // Tokenization details

// Native OTP flow parameters
formData.append('panNumber', 'ABCDE1234A');       // Customer PAN number
formData.append('s2s_device_info', 'Mozilla');    // Customer device info
formData.append('s2s_client_ip', '10.11.101.11'); // Customer IP address
formData.append('txn_s2s_flow', '4');             // Server-to-server flow (4 for Native OTP)

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
fetch('https://test.payu.in/_payment', requestOptions)
  .then(response => {
    console.log('Status Code:', response.status);
    return response.text(); // or response.json() if you're sure it returns JSON
  })
  .then(data => {
    console.log('Response:', data);
    // Process payment response here and handle OTP flow
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

def process_cardless_emi_with_native_otp() -> Dict[str, Any]:
    """
    Process cardless EMI payment with Native OTP flow using PayU's S2S integration
    
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
        "surl": "https://apiplayground-response.herokuapp.com/", # Success URL
        "furl": "https://apiplayground-response.herokuapp.com/", # Failure URL
        # Card and token details
        "ccnum": "1234",                     # Limited card details
        "ccexpmon": "05",                    # Expiry month
        "ccexpyr": "2022",                   # Expiry year
        "ccvv": "123",                       # CVV
        "ccname": "undefined",               # Cardholder name
        "store_card_token": "1234 4567 2456 3566", # Tokenized card
        "storecard_token_type": "1",         # Token type
        "additional_info": json.dumps(additional_info), # Tokenization details
        
        # Native OTP flow parameters
        "panNumber": "ABCDE1234A",           # Customer PAN number
        "s2s_device_info": "Mozilla",        # Customer device info
        "s2s_client_ip": "10.11.101.11",     # Customer IP address
        "txn_s2s_flow": "4",                 # Server-to-server flow (4 for Native OTP)
        
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
    result = process_cardless_emi_with_native_otp()
    print(f"Status Code: {result['status_code']}")
    if 'error' in result:
        print(f"Error: {result['error']}")
    print(f"Response: {result['response']}")
    
    # Handle OTP flow based on the response
    # In Native OTP flow, you'll need to handle OTP verification

```
```php
<?php
/**
 * Process cardless EMI payment with Native OTP flow using PayU's S2S integration
 * 
 * IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
 * 
 * @return array Response from PayU API
 */
function processCardlessEmiWithNativeOtp() {
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
        "surl" => "https://apiplayground-response.herokuapp.com/", // Success URL
        "furl" => "https://apiplayground-response.herokuapp.com/", // Failure URL
        // Card and token details
        "ccnum" => "1234",                      // Limited card details
        "ccexpmon" => "05",                     // Expiry month
        "ccexpyr" => "2022",                    // Expiry year
        "ccvv" => "123",                        // CVV
        "ccname" => "undefined",                // Cardholder name
        "store_card_token" => "1234 4567 2456 3566", // Tokenized card
        "storecard_token_type" => "1",          // Token type
        "additional_info" => json_encode($additionalInfo), // Tokenization details
        
        // Native OTP flow parameters
        "panNumber" => "ABCDE1234A",            // Customer PAN number
        "s2s_device_info" => "Mozilla",         // Customer device info
        "s2s_client_ip" => "10.11.101.11",      // Customer IP address
        "txn_s2s_flow" => "4",                  // Server-to-server flow (4 for Native OTP)
        
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
    
    // Process the response
    // In Native OTP flow, you'll need to handle OTP verification
    return [
        "status_code" => $statusCode,
        "response" => $response
    ];
}

// Example usage
$result = processCardlessEmiWithNativeOtp();
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
 * PayU Cardless EMI Payment with Native OTP Flow Integration
 * 
 * IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
 */
public class PayUCardlessEmiWithNativeOtpProcessor {
    
    // API endpoint
    private static final String PAYU_TEST_URL = "https://test.payu.in/_payment";
    
    /**
     * Process cardless EMI payment with Native OTP flow through PayU
     * @return PaymentResponse containing status and response data
     */
    public PaymentResponse processCardlessEmiWithNativeOtp() {
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
            params.put("surl", "https://apiplayground-response.herokuapp.com/"); // Success URL
            params.put("furl", "https://apiplayground-response.herokuapp.com/"); // Failure URL
            // Card and token details
            params.put("ccnum", "1234");                      // Limited card details
            params.put("ccexpmon", "05");                     // Expiry month
            params.put("ccexpyr", "2022");                    // Expiry year
            params.put("ccvv", "123");                        // CVV
            params.put("ccname", "undefined");                // Cardholder name
            params.put("store_card_token", "1234 4567 2456 3566"); // Tokenized card
            params.put("storecard_token_type", "1");          // Token type
            params.put("additional_info", additionalInfo);    // Tokenization details
            
            // Native OTP flow parameters
            params.put("panNumber", "ABCDE1234A");            // Customer PAN number
            params.put("s2s_device_info", "Mozilla");         // Customer device info
            params.put("s2s_client_ip", "10.11.101.11");      // Customer IP address
            params.put("txn_s2s_flow", "4");                  // Server-to-server flow (4 for Native OTP)
            
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
            
            // Process the response
            // In Native OTP flow, you'll need to handle OTP verification
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
        PayUCardlessEmiWithNativeOtpProcessor processor = new PayUCardlessEmiWithNativeOtpProcessor();
        PaymentResponse result = processor.processCardlessEmiWithNativeOtp();
        
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

namespace PayUCardlessEmiNativeOtpIntegration
{
    /// <summary>
    /// PayU Cardless EMI Payment with Native OTP Flow Processor
    /// 
    /// IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
    /// </summary>
    public class PayUCardlessEmiWithNativeOtpProcessor
    {
        // API endpoint
        private const string PayuTestUrl = "https://test.payu.in/_payment";
        
        /// <summary>
        /// Process cardless EMI payment with Native OTP flow through PayU
        /// </summary>
        /// <returns>PaymentResponse containing status and response data</returns>
        public async Task<PaymentResponse> ProcessCardlessEmiWithNativeOtpAsync()
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
                    { "surl", "https://apiplayground-response.herokuapp.com/" }, // Success URL
                    { "furl", "https://apiplayground-response.herokuapp.com/" }, // Failure URL
                    // Card and token details
                    { "ccnum", "1234" },                       // Limited card details
                    { "ccexpmon", "05" },                      // Expiry month
                    { "ccexpyr", "2022" },                     // Expiry year
                    { "ccvv", "123" },                         // CVV
                    { "ccname", "undefined" },                 // Cardholder name
                    { "store_card_token", "1234 4567 2456 3566" }, // Tokenized card
                    { "storecard_token_type", "1" },           // Token type
                    { "additional_info", additionalInfoJson }, // Tokenization details
                    
                    // Native OTP flow parameters
                    { "panNumber", "ABCDE1234A" },             // Customer PAN number
                    { "s2s_device_info", "Mozilla" },          // Customer device info
                    { "s2s_client_ip", "10.11.101.11" },       // Customer IP address
                    { "txn_s2s_flow", "4" },                   // Server-to-server flow (4 for Native OTP)
                    
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
                    
                    // Process the response
                    // In Native OTP flow, you'll need to handle OTP verification
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
            var processor = new PayUCardlessEmiWithNativeOtpProcessor();
            var result = await processor.ProcessCardlessEmiWithNativeOtpAsync();
            
            Console.WriteLine($"Status Code: {result.StatusCode}");
            if (result.IsSuccess)
            {
                Console.WriteLine($"Response: {result.Response}");
                // Handle OTP verification here
            }
            else
            {
                Console.WriteLine($"Error: {result.Error}");
            }
        }
    }
}

```

<br />

## Step 3: Submit the OTP

Once your customer enters the OTP on the payment page (postUrl/acsTemplate), pass the OTP using the **Submit OTP** API. For more information, refer to [Submit OTP API](ref:submit-otp-to-payu).

#### Resend OTP

If the customer enters the incorrect OTP or an expired OTP, use [Resend OTP API](ref:resend-otp-api) to handle the **Resend OTP** request made by a customer.