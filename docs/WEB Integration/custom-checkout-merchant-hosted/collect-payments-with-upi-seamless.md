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

When your customer makes payment through UPI, you can validate the customer’s Virtual Payment Address (VPA) and then initiate payment. The **validateVpa** API is used to validate the UPI handle. Validate the VPA (UPI handle) using the **validateVpa** API.  For more information, refer to <Anchor label="Validate VPA Handle API" target="_blank" href="ref:validate_vpa_api">Validate VPA Handle API</Anchor>.

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

The following parameters vary for the UPI payment mode in the **Collect Payment** API (**_payment** API).

**Environment**

|                            |                                                                         |
| :------------------------- | :---------------------------------------------------------------------- |
| **Test Environment**       | \<[https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | \<[https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

> 📘 Reference:
>
> For the **Try It** experience and response, refer to [Collect Payment API - Merchant Hosted Checkout](doc:_payment_merchant_hosted) under API Reference.

| Parameter | Description | **Example** |
| :-------- | :---------- | :---------- |
|           |             |             |

<Glossary>key</Glossary>
`mandatory`

|    | `String`Merchant key provided by PayU during onboarding. | JPg***r |
| :- | :------------------------------------------------------- | :------ |
|    |                                                          |         |

<Glossary>txnid</Glossary>
`mandatory`

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>

      </th>

      <th>
        `String`The transaction ID is a reference number for a specific order that is generated by the merchant.
      </th>

      <th>
        ypl938459435
      </th>
    </tr>
  </thead>

  <tbody>
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
        email
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
        phone
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
        vpa
        `mandatory`
      </td>

      <td>
        String The VPA of the customer. For the list of bank name part of the handles, refer to

        [UPI Handles](doc:upi-handles)

        . **Reference**: For the list of test card numbers for EMI, refer to

        [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets)
      </td>

      <td>
        test123@okhdfcbank
      </td>
    </tr>

    <tr>
      <td>
        furl
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
        surl
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
        hash
        `mandatory`
      </td>

      <td>
        `String`It is the hash calculated by the merchant. The hash calculation logic is:
        `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        address1
        `optional`
      </td>

      <td>
        `String` The first line of the billing address.

        * _For Fraud Detection_*: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        address2
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
        city
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
        state
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
        country
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
        zipcode
        `optional`
      </td>

      <td>
        `String` Billing address zip code is mandatory for the cardless EMI option.
        `Character Limit`-20
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf1
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
        udf2
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
        udf3
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
        udf4
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
        udf5
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

Verify the transaction details using the Verification APIs. For more information, refer to <Anchor label="Verify Payment API" target="_blank" href="ref:verify_payment_api">Verify Payment API</Anchor> under API Reference.

<Callout icon="📘" theme="info">
  **Tip**: The transaction ID that you posted in Step 1 with PayU must be used here.
</Callout>

**Environment**

|                        |                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| Test Environment       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice.php?form=2](https://info.payu.in/merchant/postservice.php?form=2) |

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'command=verify_payment' \
  --data-urlencode 'var1=IhfgcZnXR4o4nB' \
  --data-urlencode 'hash=a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  * If credit card payment is made, the response is similar to the following:

  ```plaintext
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

  * Offer availed on cart level

  ```
  {
      "status": 1,
      "msg": "1 out of 1 Transactions Fetched Successfully",
      "transaction_details": {
          "1036-f0cf85f2": {
              "mihpayid": "21564143078",
              "request_id": "",
              "bank_ref_num": "431998369241",
              "amt": "2.00",
              "transaction_amount": "2.00",
              "txnid": "1036-f0cf85f2",
              "additional_charges": "0.00",
              "productinfo": "EXPRESS",
              "firstname": "guest",
              "bankcode": "TEZOMNI",
              "udf1": "Magento2",
              "udf2": "",
              "udf3": "",
              "udf4": "",
              "udf5": "qs8rbc1ng2hmqtakk381en6j2p",
              "field2": "114390824407",
              "field9": "SUCCESS|Completed Using Callback",
              "error_code": "E000",
              "addedon": "2024-11-14 16:06:40",
              "payment_source": "express",
              "card_type": null,
              "error_Message": "NO ERROR",
              "net_amount_debit": 2.00,
              "disc": "0.00",
              "mode": "UPI",
              "PG_TYPE": "UPI-PG",
              "card_no": "",
              "status": "success",
              "unmappedstatus": "captured",
              "Merchant_UTR": null,
              "Settled_At": "0000-00-00 00:00:00",
              "App_Name": "GooglePay",
              "card_token": null,
              "field4": null,
              "offerAvailed": null,
              "cart_details": {
                  "id": "2446425",
                  "payu_id": "21564143078",
                  "total_items": "1",
                  "total_cart_amount": "2.00",
                  "offer_applied": null,
                  "offer_availed": null,
                  "offer_auto_apply": "0",
                  "instant_discount": "0.00",
                  "cashback_discount": "0.00",
                  "total_discount": "0.00",
                  "net_cart_amount": "2.00",
                  "created_at": "2024-11-14 16:06:40",
                  "updated_at": "2024-11-14 16:06:40",
                  "sku_details": [
                      {
                          "id": "3468748",
                          "cart_id": "2446425",
                          "payu_id": "21564143078",
                          "mid": "2",
                          "sku_id": "Sample Sofa Design-Red",
                          "sku_name": "Sample Sofa Designtest?=!name",
                          "amount_per_sku": "2.00",
                          "quantity": "1",
                          "amount_before_discount": "2.00",
                          "discount": "0.00",
                          "amount_after_discount": "2.00",
                          "offer_applied": null,
                          "offer_availed": null,
                          "offer_status": null,
                          "offer_type": null,
                          "offer_auto_apply": "0",
                          "is_nce": "0",
                          "failure_reason": null,
                          "created_at": "2024-11-14 16:06:40",
                          "updated_at": "2024-11-14 16:06:40",
                          "offer_title": null,
                          "offer_description": null,
                          "instant_discount": null,
                          "cashback_discount": null,
                          "offers_raw_response": null,
                          "raw_response": null
                      }
                  ]
              }
          }
      }
  }
  ```

  * Offer availed at Transaction level

  ```
  {
      "status": 1,
      "msg": "1 out of 1 Transactions Fetched Successfully",
      "transaction_details": {
          "1725950872187": {
              "mihpayid": "20911942990",
              "request_id": null,
              "bank_ref_num": null,
              "amt": "9900.00",
              "transaction_amount": "10000.00",
              "txnid": "1725950872187",
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
              "field9": "You have reached credit card load limit. Please use other payment options to continue.",
              "error_code": "E4936",
              "addedon": "2024-09-10 12:18:20",
              "payment_source": "payu",
              "card_type": "MAST",
              "error_Message": "Bank was unable to authenticate.",
              "net_amount_debit": "0.00",
              "disc": "100.00",
              "mode": "DC",
              "PG_TYPE": "DC-PG",
              "card_no": "XXXXXXXXXXXX9528",
              "status": "failure",
              "unmappedstatus": "failed",
              "Merchant_UTR": null,
              "Settled_At": null,
              "cardhash": "31056eb2112b68cdc90896f1953ca26605bb525249096172c178881bcd45ac93",
              "name_on_card": null,
              "card_token": null,
              "field4": null,
              "offerApplied": "LoadTest1@m3phN7YptAA6",
              "offerAvailed": "LoadTest1@m3phN7YptAA6",
              "transactionOffer": "{"offer_data":[{"offer_key":"LoadTest1@m3phN7YptAA6","discount":100,"offer_type":"INSTANT","isNoCost":false,"flag_to_fail":false,"status":"SUCCESS","failure_code":null,"failure_reason":"Offer Applied Successfully","offer_description":"Load Test 1","offer_title":"Load Test 1","record_type":"OFFER","parent_offer_key":null,"offer_category":null,"isDpEmi":false}],"discount_data":{"total_discount":100,"cashback_discount":0,"instant_discount":100,"total_nce_discount":0,"instant_nce_discount":0,"cashback_nce_discount":0,"gstSubventedViaOffer":false,"downPaymentAmount":0}}",
              "offerType": "instant",
              "offerLevel": "TRANSACTION_LEVEL"
          }
      }
  }
  ```

  #### Failure Responses

  * If txnID is not found, the response is similar to the following:

  ```plaintext
  {
  "status":0,"msg":"0 out of 1 Transactions Fetched

  Successfully","transaction_details":{"IhfgcZnXR4o4nB":{"mihpayid":"Not Found","status":"Not Found"}}
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

## Recommended integrations for UPI

* **Recurring Payments**: Enable recurring payments or subscriptions for wallets. For more information, refer to [Recurring Payments Integration](doc:introduction-recurring-payments-integration).
* **Offers**: Configure offers for cards on Dashboard and then collect payments with offers. For more information, refer to [Offers Dashboard](doc:offers-dashboard) and [Offers Integration APIs](doc:offers-integration)
