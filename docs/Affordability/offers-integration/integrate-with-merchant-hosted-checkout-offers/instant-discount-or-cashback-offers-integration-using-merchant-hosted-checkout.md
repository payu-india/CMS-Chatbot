---
title: Instant Discount or Cashback using Merchant Hosted Checkout
excerpt: >-
  With the Merchant Hosted Checkout integration, the entire payment experience
  can be controlled by merchants and PayU provides APIs to power this checkout
  experience. This section describes how PayU will help you to discover Offer
  (not only on Checkout page but anywhere on the merchant app/website), validate
  Offer & apply Offer (along with payment).  ##
deprecated: false
hidden: false
metadata:
  title: >-
    Instant Discount or Cashback using Merchant Hosted Checkout - Offers
    Integration
  description: ''
  keywords:
    - Integrate an Instant Discount Offer with Merchant Hosted Checkout
    - Integrate Merchant Hosted Checkout with Cashback Offer
    - Integrate Cashback Offer with Seamless Integration
    - Instant Discount Offer with Seamless Integration
    - Integrating Instant Discount Offers with Merchant Hosted Checkout
    - Integrate an Cashback Offer with Merchant Hosted Checkout
    - Integrate Merchant Hosted Checkout Cashback Offer
    - Integrate a Cashback Offer with Seamless Integration
    - Cashback Offer with Seamless Integration
    - Integrating Cashback Offers with Merchant Hosted Checkout
    - Cash Back Offer Integration
  robots: index
next:
  description: ''
---
## Customer journey on Merchant Hosted Checkout

The following video walks through the customer journey:

The steps involves in the customer journey are:

1. User logs in to the merchant’s app/website.
2. User chooses the product(s)/service(s) he/she wishes to purchase.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/merchant_hosted_offers_checkout1-1024x576.png)

3. User reaches the checkout page. The merchant can use the Fetch offers API to display all the live applicable offers for this transaction. As part of this API the merchant would get all the necessary information to display to the user regarding the offer include Offer Title, description, terms and conditions, applicable payment modes & the offer value.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/merchant_hosted_offers_checkout3-1024x576.png)

4. User would make his/her decision and pay through a specific payment option. After the customer has entered all the required details, the merchant can use the Validate Offer API to check whether the offer would be applied to the transaction or not.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/merchant_hosted_offers_checkout4-1024x576.png)

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/merchant_hosted_offers_checkout7-1.png)

5. The merchant would initiate the payment along with the offer using the **\_payment** API
6. In case of Instant discount, the amount would be reduced on application of offer, in case of cashback the amount would not be charged.
7. User would complete the 2FA (2 Form Authentication) payment on the adjusted amount.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/merchant_hosted_offers_checkout8.png)

8. User would be redirected back to the merchant app/website.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/merchant_hosted_offers_checkout9.png)

The merchant can use the Fetch offers API to display the offers on **Product Display Page** & **Cart** screens or in case merchant wishes to have a separate **Offers section** on their website/app

## Integration steps

To integrate offers using Merchant Hosted Checkout integration:

> 📘 Reference:
> 
> For the Merchant Hosted Checkout workflow, refer [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted)

1. On the checkout page (or earlier on PDP, Cart, Offers) use the **Fetch Offers** API to get the offers and display all the offers. For more information, refer to [Fetch Offers API](ref:fetch-offers-api).
2. Use the **Validate Offer** API to validate if the offer will be applied on this transaction or not. For more information, refer to [Validate Offer API](ref:validate-offer-api).
3. Make the payment request using the **\_payment** API using the following additional parameters for Offers. For more information on the complete list of parameters to be posted, refer to [Collect Payment API - Merchant Hosted Checkout](ref:_payment-merchant-hosted)

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "api\\_version  \n**mandatory**",
    "0-1": "The API version of the \\_payment API must be specified as **14**.",
    "0-2": "14",
    "1-0": "user\\_token  \n**mandatory for UPI, NB, Wallet**",
    "1-1": "The use for this param is to allow the offer engine to apply velocity rules at a user level.  \n  \n- **Card Based Offers (CC, DC, EMI)**: In case of card payment mode offers, if this parameter is passed the velocity rules would be applied on this token, if not passed the same would be applied on the card number.\n- **UPI, NB, Wallet**: It is mandatory for UPI, NB, and Wallet payment modes. If not passed the validation rules would not apply.",
    "1-2": "",
    "2-0": "hash  \n**mandatory**",
    "2-1": "It is used to avoid the possibility of transaction tampering.  \n**Note**: The following order must be used for hashing:  \n`key\\|txnid\\|amount\\|productinfo\\|firstname\\|email\\|udf1\\|udf2\\|udf3\\|udf4\\|udf5\\|udf6\\|udf7\\|udf8\\|udf9\\|udf10\\|offer_key\\|offer_auto_apply\\|SALT`  \nFor more information on hash generation process, refer to [Generate Hash](doc:generate-hash-merchant-hosted) .",
    "2-2": ""
  },
  "cols": 3,
  "rows": 3,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


> **Notes**:  
>
> - The following order must be used for hashing:  
>   `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|offer_key|offer_auto_apply|SALT`  
>   For more information on hash generation process, refer to [Hashing Request and Response](ref:generate-hash-merchant-hosted).
> - If any of the keys is null/not configured, "|" character must be concatenated.
> - The above hash logic is for \_payment API version 10 or later

**Sample Request with cart_details JSON object:**

```curl
curl -X POST "https://test.payu.in/_payment" \
-H "accept: application/json" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "key=JP***g" \
-d "txnid=ewP8oRopzdHEtC" \
-d "amount=10.00" \
-d "firstname=Ashish" \
-d "email=test@gmail.com" \
-d "phone=9876543210" \
-d "productinfo=iPhone" \
-d "pg=TESTPG" \
-d "bankcode=TESTPGNB" \
-d "surl=https://apiplayground-response.herokuapp.com/" \
-d "furl=https://apiplayground-response.herokuapp.com/" \
-d 'cart_details={
  "amount": 55000,
  "items": 2,
  "surcharges": 10,
  "pre_discount": 5,
  "sku_details": [
    {
      "sku_id": "smartphone234",
      "sku_name": "Smartphone",
      "amount_per_sku": "45000",
      "quantity": 1,
      "offer_key": null,
      "offer_auto_apply": true
    },
    {
      "sku_id": "smartwatch132",
      "sku_name": "Smartwatch",
      "amount_per_sku": "10000",
      "quantity": 1,
      "offer_key": ["flat500@2022"],
      "offer_auto_apply": false
    }
  ]
}' \
-d "hash=bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"

```
```javascript
/**
 * PayU Card Payment with Cart Details using Fetch API
 * 
 * IMPORTANT: This should only be executed server-side (e.g., in Node.js), never in the browser,
 * as it contains sensitive payment information.
 */

// Payment endpoint
const url = 'https://test.payu.in/_payment';

// Cart details object
const cartDetails = {
  amount: 55000,
  items: 2,
  surcharges: 10,
  pre_discount: 5,
  sku_details: [
    {
      sku_id: "smartphone234",
      sku_name: "Smartphone",
      amount_per_sku: "45000",
      quantity: 1,
      offer_key: null,
      offer_auto_apply: true
    },
    {
      sku_id: "smartwatch132",
      sku_name: "Smartwatch",
      amount_per_sku: "10000",
      quantity: 1,
      offer_key: ["flat500@2022"],
      offer_auto_apply: false
    }
  ]
};

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
// Add cart details as JSON string
formData.append('cart_details', JSON.stringify(cartDetails));
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

def process_card_payment_with_cart_details() -> Dict[str, Any]:
    """
    Process card payment with cart details using PayU's Merchant Hosted Checkout
    
    IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
    
    Returns:
        Dictionary with response from PayU API
    """
    # API endpoint
    url = "https://test.payu.in/_payment"
    
    # Cart details object
    cart_details = {
        "amount": 55000,
        "items": 2,
        "surcharges": 10,
        "pre_discount": 5,
        "sku_details": [
            {
                "sku_id": "smartphone234",
                "sku_name": "Smartphone",
                "amount_per_sku": "45000",
                "quantity": 1,
                "offer_key": None,
                "offer_auto_apply": True
            },
            {
                "sku_id": "smartwatch132",
                "sku_name": "Smartwatch",
                "amount_per_sku": "10000",
                "quantity": 1,
                "offer_key": ["flat500@2022"],
                "offer_auto_apply": False
            }
        ]
    }
    
    # Prepare the form data
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
        # Add cart details as JSON string
        "cart_details": json.dumps(cart_details),
        "hash": "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
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
    result = process_card_payment_with_cart_details()
    print(f"Status Code: {result['status_code']}")
    if 'error' in result:
        print(f"Error: {result['error']}")
    print(f"Response: {result['response']}")

```
```php
<?php
/**
 * Process card payment with cart details using PayU's Merchant Hosted Checkout
 * 
 * IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
 * 
 * @return array Response from PayU API
 */
function processCardPaymentWithCartDetails() {
    // API endpoint
    $url = "https://test.payu.in/_payment";
    
    // Cart details object
    $cartDetails = [
        "amount" => 55000,
        "items" => 2,
        "surcharges" => 10,
        "pre_discount" => 5,
        "sku_details" => [
            [
                "sku_id" => "smartphone234",
                "sku_name" => "Smartphone",
                "amount_per_sku" => "45000",
                "quantity" => 1,
                "offer_key" => null,
                "offer_auto_apply" => true
            ],
            [
                "sku_id" => "smartwatch132",
                "sku_name" => "Smartwatch",
                "amount_per_sku" => "10000",
                "quantity" => 1,
                "offer_key" => ["flat500@2022"],
                "offer_auto_apply" => false
            ]
        ]
    ];
    
    // Prepare the form data
    $payload = [
        "key" => "JP***g",
        "txnid" => "ewP8oRopzdHEtC",
        "amount" => "10.00",
        "firstname" => "Ashish",
        "email" => "test@gmail.com",
        "phone" => "9876543210",
        "productinfo" => "iPhone",
        "pg" => "TESTPG",
        "bankcode" => "TESTPGNB",
        "surl" => "https://apiplayground-response.herokuapp.com/",
        "furl" => "https://apiplayground-response.herokuapp.com/",
        // Add cart details as JSON string
        "cart_details" => json_encode($cartDetails),
        "hash" => "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
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
$result = processCardPaymentWithCartDetails();
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

// For JSON processing
import javax.json.Json;
import javax.json.JsonArray;
import javax.json.JsonArrayBuilder;
import javax.json.JsonObject;
import javax.json.JsonObjectBuilder;

/**
 * PayU Card Payment Processor with Cart Details for Merchant Hosted Checkout
 * 
 * IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
 */
public class PayUCardPaymentProcessor {
    
    // API endpoint
    private static final String PAYU_TEST_URL = "https://test.payu.in/_payment";
    
    /**
     * Process card payment with cart details through PayU
     * @return PaymentResponse containing status and response data
     */
    public PaymentResponse processCardPaymentWithCartDetails() {
        try {
            // Initialize URL
            URL url = new URL(PAYU_TEST_URL);
            
            // Create cart details JSON
            JsonObjectBuilder cartDetailsBuilder = Json.createObjectBuilder()
                .add("amount", 55000)
                .add("items", 2)
                .add("surcharges", 10)
                .add("pre_discount", 5);
            
            // Create SKU details array
            JsonArrayBuilder skuDetailsBuilder = Json.createArrayBuilder();
            
            // First SKU item
            JsonObjectBuilder smartphone = Json.createObjectBuilder()
                .add("sku_id", "smartphone234")
                .add("sku_name", "Smartphone")
                .add("amount_per_sku", "45000")
                .add("quantity", 1)
                .addNull("offer_key")
                .add("offer_auto_apply", true);
            
            // Second SKU item
            JsonArrayBuilder offerKeys = Json.createArrayBuilder().add("flat500@2022");
            JsonObjectBuilder smartwatch = Json.createObjectBuilder()
                .add("sku_id", "smartwatch132")
                .add("sku_name", "Smartwatch")
                .add("amount_per_sku", "10000")
                .add("quantity", 1)
                .add("offer_key", offerKeys)
                .add("offer_auto_apply", false);
            
            // Add items to the SKU details array
            skuDetailsBuilder.add(smartphone);
            skuDetailsBuilder.add(smartwatch);
            
            // Finalize cart details JSON
            JsonObject cartDetails = cartDetailsBuilder
                .add("sku_details", skuDetailsBuilder)
                .build();
            
            // Prepare form parameters
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
            // Add cart details as JSON string
            params.put("cart_details", cartDetails.toString());
            params.put("hash", "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319");
            
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
        PayUCardPaymentProcessor processor = new PayUCardPaymentProcessor();
        PaymentResponse result = processor.processCardPaymentWithCartDetails();
        
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

namespace PayUCardIntegration
{
    /// <summary>
    /// PayU Card Payment Processor with Cart Details for Merchant Hosted Checkout
    /// 
    /// IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
    /// </summary>
    public class PayUCardPaymentProcessor
    {
        // API endpoint
        private const string PayuTestUrl = "https://test.payu.in/_payment";
        
        /// <summary>
        /// Process card payment with cart details through PayU
        /// </summary>
        /// <returns>PaymentResponse containing status and response data</returns>
        public async Task<PaymentResponse> ProcessCardPaymentWithCartDetailsAsync()
        {
            try
            {
                // Create cart details object
                var cartDetails = new
                {
                    amount = 55000,
                    items = 2,
                    surcharges = 10,
                    pre_discount = 5,
                    sku_details = new[]
                    {
                        new {
                            sku_id = "smartphone234",
                            sku_name = "Smartphone",
                            amount_per_sku = "45000",
                            quantity = 1,
                            offer_key = (string)null,
                            offer_auto_apply = true
                        },
                        new {
                            sku_id = "smartwatch132",
                            sku_name = "Smartwatch",
                            amount_per_sku = "10000",
                            quantity = 1,
                            offer_key = new[] { "flat500@2022" },
                            offer_auto_apply = false
                        }
                    }
                };
                
                // Serialize cart details to JSON
                string cartDetailsJson = JsonSerializer.Serialize(cartDetails);
                
                // Prepare form parameters
                var formData = new Dictionary<string, string>
                {
                    { "key", "JP***g" },
                    { "txnid", "ewP8oRopzdHEtC" },
                    { "amount", "10.00" },
                    { "firstname", "Ashish" },
                    { "email", "test@gmail.com" },
                    { "phone", "9876543210" },
                    { "productinfo", "iPhone" },
                    { "pg", "TESTPG" },
                    { "bankcode", "TESTPGNB" },
                    { "surl", "https://apiplayground-response.herokuapp.com/" },
                    { "furl", "https://apiplayground-response.herokuapp.com/" },
                    // Add cart details as JSON string
                    { "cart_details", cartDetailsJson },
                    { "hash", "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319" }
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
            var processor = new PayUCardPaymentProcessor();
            var result = await processor.ProcessCardPaymentWithCartDetailsAsync();
            
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

<br />

4. Check the following response parameters (for Offers) from PayU to handle the payment response, as the net amount debit may be different from the amount sent by you in the request.

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "discount",
    "0-1": "This will specify the offer value provided to the user.",
    "0-2": "10.00",
    "1-0": "net\\_amount\\_debit",
    "1-1": "This will specify the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request.",
    "1-2": "100.00",
    "2-0": "offer",
    "2-1": "This parameter is used to post the offer key.",
    "2-2": "newoffer1@5686",
    "3-0": "offer\\_type",
    "3-1": "This parameter is used to post any of the following offer\\_type:  \n - instant  \n  \n- cashback",
    "3-2": "instant"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


For a sample response, refer to the [Additional Info for Payment APIs](ref:addl_info-payment-apis).

5. Verify the payment.

Similar to the payment response, same params can be handled as part of the **Verify Payment** API. For more information, For API reference, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a>. For the sample response using the **Verify Payment **API from PayU involving offers, refer to <a href="addl-info-general-apis#sample-response" target="_blank">Additional Info for General APIsI</a>.

| **Parameter**       | **Description**                                                                                                                                                                                  | **Example** |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| transaction\_amount | This parameter contains the total transaction amount before discount.                                                                                                                            | 50000.00    |
| net\_amount\_debit  | This parameter contains the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request. | 47500.00    |
| discount            | This parameter contains the offer value provided to the user. This value will specify the offer amount for both Instant discount and Cashback offers.                                            | 2500.00     |

PayU would refund the exact amount passed by you in the Refund request. For more information, refer to [Refunds for Offers](doc:refunds-for-offers)

> 📘 Note:
> 
> You can enable the **Enforce Offer** flag by requesting your PayU Key Account Manager. If you enable the **Enforce Offer** flag, the best offer out of the all the offers passed will be applied for the customer.