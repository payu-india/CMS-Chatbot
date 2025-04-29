---
title: UPI Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collect Payments with UPI - Merchant Hosted Checkout
  description: >-
    Learn how to seamlessly collect payments through UPI transactions using
    PayU's Merchant Hosted Checkout integration. Discover the steps to validate
    the customer's Virtual Payment Address (VPA), initiate payments, and verify
    the payment status.
  robots: index
next:
  description: ''
---
PayU allows you to collect payments using UPI handles. For the list of UPI providers supported, refer to [UPI Handles](doc:upi-handles).

**Steps to Integrate:**

1. [Validate the UPI handle](#step1-validate-the-vpa-handle)
2. [Initiate the Payment to PayU](#step-2-initiate-the-payment-to-payu)
3. [Check response from PayU](#step-3-check-response-from-payu)
4. [Verify the payment](#step-4-verify-the-payment)

<RegisterMerchantPrerequiste />

## Step 1: Validate the UPI handle

When your customer makes payment through UPI, you can validate the customer’s Virtual Payment Address (VPA) and then initiate payment. The **validateVpa** API is used to validate the UPI handle. Validate the VPA (UPI handle) using the **validateVpa** API.  For more information, refer to [Validate VPA Handle API](ref:validate_vpa_api).

<details>
<summary>Sample VPA validation code</summary>

```javascript
	// JavaScript example for VPA validation before payment submission
// This should be run on your server, not client-side

async function validateVpa(vpa) {
    try {
        // Get hash from server endpoint
        const hashResponse = await fetch('/generate-vpa-hash', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ vpa })
        });
        const { hash } = await hashResponse.json();
        
        // Validate VPA with PayU
        const response = await fetch('https://test.payu.in/merchant/postservice?form=2', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({
                key: 'YOUR_MERCHANT_KEY',
                command: 'validateVPA',
                var1: vpa, // VPA to validate
                hash: hash
            })
        });
        
        const result = await response.json();
        
        // Sample response:
        // {"status":1,"msg":"VPA is valid","isVPAValid":1,"isUPIBarredBank":0}
        // OR
        // {"status":0,"msg":"VPA is invalid","isVPAValid":0}
        
        return {
            isValid: result.isVPAValid === 1,
            message: result.msg
        };
    } catch (error) {
        console.error('VPA validation error:', error);
        return { isValid: false, message: 'Validation service error' };
    }
}

```
```curl
# Once you have the hash, make the API call

curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=YOUR_MERCHANT_KEY" \
  -d "command=validateVPA" \
  -d "var1=customer@upi" \
  -d "hash=$HASH"

```

<br />

</details>

<br />

## Step 2: Initiate the payment to PayU

### Post request syntax & composition

Post Request Syntax & Composition for UPI

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
<input type="hidden" name="pg" value="UPI" />
<input type="hidden" name="bankcode" value="UPI" />
<input type="hidden" name="vpa" value="test123@okhdfcbank" />
<input type="hidden" name="surl" value="your own success url" />
<input type="hidden" name="furl" value="your own failure url" />
<input type="hidden" name="phone" value="9988776655” />
<input type="hidden" name="hash" value="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />
<input type="submit" value="submit"> </form>
</body>
</html>
```

> 📘 Note
>
> The above HTML code block is for Merchant Checkout integration on the UPI call for the test environment.

### Request parameters

The following parameters vary for the UPI payment mode in the **Collect Payment** API (**\_payment** API).

<PaymentAPIEnvironment />

> 📘 Reference:
>
> For the **Try It** experience and response, refer to <a href="_payment_merchant_hosted_upi" target="_blank">Collect Payments API</a> under API Reference.

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
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        <Glossary>key</Glossary>
        `mandatory`
      </td>

      <td>
        `String`Merchant key provided by PayU during onboarding.
      </td>

      <td>
         JPg\*\*\*r
      </td>
    </tr>

    <tr>
      <td>
        <Glossary>txnid</Glossary>\
         `mandatory`
      </td>

      <td>
        `String`The transaction ID is a reference number for a specific order that is generated by the merchant.
      </td>

      <td>
         ypl938459435
      </td>
    </tr>

    <tr>
      <td>
        amount  `mandatory`
      </td>

      <td>
        `String`The payment amount for the transaction.
      </td>

      <td>
         10.00
      </td>
    </tr>

    <tr>
      <td>
        productinfo  `mandatory`
      </td>

      <td>
        `String`A brief description of the product.
      </td>

      <td>
         iPhone
      </td>
    </tr>

    <tr>
      <td>
        firstname  `mandatory`
      </td>

      <td>
        `String` The first name of the customer.
      </td>

      <td>
        Ashish
      </td>
    </tr>

    <tr>
      <td>
        email\
        `mandatory`
      </td>

      <td>
        `String`The email address of the customer.
      </td>

      <td>
         [abc@payu.in](mailto:abc@payu.in)
      </td>
    </tr>

    <tr>
      <td>
        phone\
         `mandatory`
      </td>

      <td>
        `String`The phone number of the customer.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        <Glossary>pg</Glossary> `mandatory`
      </td>

      <td>
        `String` It defines the payment category that the merchant wants the customer to see by default on the PayU’s payment page. This field must contain the value as "UPI" for UPI transactions.
      </td>

      <td>
        UPI
      </td>
    </tr>

    <tr>
      <td>
        <Glossary>bankcode</Glossary> `mandatory`
      </td>

      <td>
        `String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option’s bank code value in it. For a detailed list of bank codes, please contact the PayU Support.
      </td>

      <td>
        UPI
      </td>
    </tr>

    <tr>
      <td>
        vpa\
        `mandatory`
      </td>

      <td>
        String The VPA of the customer. For the list of bank name part of the handles, refer to [UPI Handles](doc:upi-handles) . **Reference**: For the list of test card numbers for EMI, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) 
      </td>

      <td>
        test123\@okhdfcbank
      </td>
    </tr>

    <tr>
      <td>
        furl\
        `mandatory`
      </td>

      <td>
        `String`The success URL, which is the page PayU will redirect to if the transaction is successful.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        surl\
        `mandatory`
      </td>

      <td>
        `String`The Failure URL, which is the page PayU will redirect to if the transaction is failed.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        hash\
        `mandatory`
      </td>

      <td>
        `String`It is the hash calculated by the merchant. The hash calculation logic is:\
        `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\||\||\||SALT)`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        address1\
        `optional`
      </td>

      <td>
        `String` The first line of the billing address.  

        * \*For Fraud Detection\*\*: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        address2\
        `optional`
      </td>

      <td>
        `String` The second line of the billing address.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        city\
        `optional`
      </td>

      <td>
        `String` The city where your customer resides as part of the billing address.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        state\
        `optional`
      </td>

      <td>
        `String` The state where your customer resides as part of the billing address,
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        country\
        `optional`
      </td>

      <td>
        `String` The country where your customer resides.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        zipcode\
        `optional`
      </td>

      <td>
        `String` Billing address zip code is mandatory for the cardless EMI option.\
        `Character Limit`-20
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf1\
        `optional`
      </td>

      <td>
        `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf2\
        `optional`
      </td>

      <td>
        `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf3\
        `optional`
      </td>

      <td>
        `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf4\
        `optional`
      </td>

      <td>
        `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf5\
        `optional`
      </td>

      <td>
        `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

<HashingRequestParameters />

### Sample request

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
        public async Task<PaymentResponse> ProcessUpiPaymentAsync()
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

## Step 3: Check response from PayU

<ReverseHashing />

### Sample response (parsed)

```
Array
(
    [mihpayid] => 403993715523409521
    [mode] => UPI
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => 5jJ9xRceXX1ydT
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 1000
    [addedon] => 2021-07-02 15:03:50
    [productinfo] => iPhone
    [firstname] => PayU User
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
    [hash] => 716f92a6452adadba68d133ba7f5ca3f3403f03f554e3ef850911f3e6727ee73402b249054170ad276c8b55ca12368a5e27cc69ffb0642ef6403dae9a5708794
    [field1] => vpa-anything@payu
    [field2] => 5jJ9xRceXX1ydT
    [field3] => 
    [field4] => PayU User
    [field5] => AXIhh4ExnaJ9dKiJvPxsewHwxMMmT3ba7UY
    [field6] => 
    [field7] => Transaction completed successfully
    [field8] => 
    [field9] => Transaction completed successfully
    [payment_source] => payu
    [PG_TYPE] => UPI-PG
    [bank_ref_num] => 5jJ9xRceXX1ydT
    [bankcode] => UPI
    [error] => E000
    [error_Message] => No Error
)
```

## Step 4: Verify the payment

Verify the transaction details using the Verification APIs. For API reference, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a> under API Reference.

> 📘 Tip
>
> The transaction ID that you posted in Step 2 with PayU must be used here.

## Recommended integrations for UPI

* **Recurring Payments**: Enable recurring payments or subscriptions for wallets. For more information, refer to [Recurring Payments Integration](doc:introduction-recurring-payments-integration).
* **Offers**: Configure offers for cards on Dashboard and then collect payments with offers. For more information, refer to [Offers Dashboard](doc:offers-dashboard) and [Offers Integration APIs](doc:offers-integration)
