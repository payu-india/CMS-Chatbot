---
title: Instant Discount or Cashback using Merchant Hosted Checkout
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
With the Merchant Hosted Checkout integration, the entire payment experience can be controlled by merchants and PayU provides APIs to power this checkout experience. This section provides the step-by-step procedure to integrate PayU's Offer Engine with Merchant Hosted Checkout integration, which enables you to display, validate, and apply various offers including instant discounts, cashback, and EMI options throughout your customer's journey.
With this integration, you are not limited to showing offers only at checkout—you can surface them anywhere in your app or website where they make sense, whether that's on product pages, cart screens, or a dedicated offers section.

## Customer journey on Merchant Hosted Checkout

The following video walks through the customer journey:

<Embed typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=tRRbSzk9Egg" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FtRRbSzk9Egg%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DtRRbSzk9Egg%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FtRRbSzk9Egg%252Fhqdefault.jpg%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" href="https://www.youtube.com/watch?v=tRRbSzk9Egg" providerUrl="https://www.youtube.com/" providerName="YouTube" />

<br />

The steps involved in the customer journey are:

* **Step 1**: Login
  Your customer logs into your app or website. At this point, they're just browsing.

* **Step 2**: Product Selection
  The customer adds products or services to their cart. This is your first opportunity to show relevant offers using the **Fetch Offers** API, potentially influencing their purchase decision before they even reach checkout.

* **Step 3**: Checkout and Offer Discovery
  When the customer lands on your checkout page, you'll call the Fetch Offers API to retrieve all applicable offers for their specific transaction. PayU returns everything you need to display the offer attractively, including the title, description, terms and conditions, applicable payment methods, and the actual discount or cashback value. Think of this API as your offer catalog for this particular transaction.

* **Step 4**: Payment Method Selection and Validation
  After the customer chooses their preferred payment method and enters the required details, you must use the **Validate Offer** API to confirm whether the selected offer will actually apply to this transaction. This validation step is crucial because it prevents customer disappointment at the final stage.

  For EMI-specific flows, there's an additional step. When a customer selects EMI (whether credit card, debit card, or cardless EMI), you'll first call the **Calculate EMI** API. This API returns all available EMI plans along with applicable offers, letting you display complete pricing information upfront. You can call this API not just at checkout but anywhere you want to show EMI options, such as product detail pages. After the customer selects an EMI plan and completes their payment details, you'll then call the **Validate Offer** API to ensure the EMI offer will be honored.

* **Step 5**: Payment Initiation
  You initiate the actual payment using the payment API, passing along the validated offer. The behavior differs based on offer type. For instant discounts, the transaction amount is reduced immediately. For cashback, the full amount is charged but the customer receives credit later.

* **Step 6**: Two-Factor Authentication
  The customer completes their bank's 2FA process on the adjusted amount (reduced amount for instant discount, original amount for cashback).

* **Step 7**: Return to your Site.   
  After successful payment, the customer is redirected back to your app or website.

<Callout icon="👍" theme="okay">
  **Tip**: You're not limited to showing offers only at checkout. Consider using the **Fetch Offers** API on product pages to highlight "Buy now and get 10% instant discount" messaging, on cart pages to encourage completion, or in a dedicated offers section to drive engagement.
</Callout>

## Integration steps

To integrate offers using Merchant Hosted Checkout integration:

<Callout icon="❗️" theme="error">
  **Prerequisites**: Before starting, ensure you're familiar with the standard Merchant Hosted Checkout workflow. If you haven't implemented basic checkout yet, refer to the Merchant Hosted Checkout documentation first. For the Merchant Hosted Checkout workflow, refer [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted)
</Callout>

### Step 1: Fetch Offers

The first step is to retrieve offers using the **Fetch Offers** API, which you can call at multiple points in your user journey. This API returns a comprehensive list of offers applicable to the transaction context you provide.

**Where to implement this**: checkout page (essential), product detail pages (recommended for conversion), cart page (recommended), or a dedicated offers page (optional but valuable for discovery). For complete API specifications and request parameters, refer to [Fetch Offers API](ref:fetch-offers-api).

### Step 2: Calculate EMI plans with offers

If your checkout supports EMI as a payment option, there is a specialized API you need to integrate before the validation step. The Calculate EMI API is specifically designed for EMI transactions and serves a different purpose than the Fetch Offers API you used in [Step 1](#step-1-fetch-offers).

When a customer selects EMI as their payment method, whether through credit card, debit card, or cardless EMI, they need to see the available EMI plans along with any applicable offers before making their final decision. The **Calculate EMI** API returns the complete EMI breakdown including tenure options, monthly installment amounts, interest rates, and any EMI-specific offers that can be applied. For complete API specification and request parameters, refer to [EMI Calculator API](https://docs.payu.in/reference/emi-calculator-api).

### Step 3: Validate Offer

Use the **Validate Offer** API to validate if the offer will be applied on this transaction or not. For more information, refer to [Validate Offer API](ref:validate-offer-api).

### Step 4: Make Payment

Make the payment request using the **_payment** API using the following additional parameters for Offers. For more information on the complete list of parameters to be posted, refer to  <Anchor label="Collect Payment API - Merchant Hosted Checkout" target="_blank" href="ref:_payment_merchant_hosted">Collect Payment API - Merchant Hosted Checkout</Anchor>

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        api_version
        **mandatory**
      </td>

      <td>
        The API version of the _payment API must be specified as **14**.
      </td>

      <td>
        14
      </td>
    </tr>

    <tr>
      <td>
        user_token
        **mandatory for UPI, NB, Wallet**
      </td>

      <td>
        The use for this param is to allow the offer engine to apply velocity rules at a user level.

        * **Card Based Offers (CC, DC, EMI)**: In case of card payment mode offers, if this parameter is passed the velocity rules would be applied on this token, if not passed the same would be applied on the card number.
        * **UPI, NB, Wallet**: It is mandatory for UPI, NB, and Wallet payment modes. If not passed the validation rules would not apply.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        hash
        **mandatory**
      </td>

      <td>
        It is used to avoid the possibility of transaction tampering.

        * _Note_*: The following order must be used for hashing:
          `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|offer_key|offer_auto_apply|SALT`
          For more information on hash generation process, refer to [Generate Hash](doc:generate-hash-merchant-hosted) .
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

> 📘 Notes:
>
> * The following order must be used for hashing:
>   `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|offer_key|offer_auto_apply|SALT`
>   For more information on hash generation process, refer to [Hashing Request and Response](ref:generate-hash-merchant-hosted).
> * If any of the keys is null/not configured, "|" character must be concatenated.
> * The above hash logic is for _payment API version 10 or later

**Sample Request with cart_details JSON object**

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

### Step 5: Check the response from PayU

Check the following response parameters (for Offers) from PayU to handle the payment response, as the net amount debit may be different from the amount sent by you in the request.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        discount
      </td>

      <td>
        This will specify the offer value provided to the user.
      </td>

      <td>
        10.00
      </td>
    </tr>

    <tr>
      <td>
        net_amount_debit
      </td>

      <td>
        This will specify the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request.
      </td>

      <td>
        100.00
      </td>
    </tr>

    <tr>
      <td>
        offer
      </td>

      <td>
        This parameter is used to post the offer key.
      </td>

      <td>
        newoffer1@5686
      </td>
    </tr>

    <tr>
      <td>
        offer_type
      </td>

      <td>
        This parameter is used to post any of the following offer_type:
         - instant

        * cashback
      </td>

      <td>
        instant
      </td>
    </tr>
  </tbody>
</Table>

For a sample response, refer to the [Additional Info for Payment APIs](ref:addl_info-payment-apis).

### Step 6: Verify the payment

Similar to the payment response, same params can be handled as part of the **Verify Payment** API or webhooks. For more information, For more information, refer to following tabs.

| Parameter          | Description                                                                                                                                                                                      | **Example** |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| transaction_amount | This parameter contains the total transaction amount before discount.                                                                                                                            | 50000.00    |
| net_amount_debit   | This parameter contains the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request. | 47500.00    |
| discount           | This parameter contains the offer value provided to the user. This value will specify the offer amount for both Instant discount and Cashback offers.                                            | 2500.00     |

<Verify_Payment_Tabs />

<br />

PayU would refund the exact amount passed by you in the Refund request. For more information, refer to [Refunds for Offers](doc:refunds-for-offers)

<Callout icon="📘" theme="info">
  **Note**: You can enable the **Enforce Offer** flag by requesting your PayU Key Account Manager. If you enable the **Enforce Offer** flag, the best offer out of the all the offers passed will be applied for the customer.
</Callout>
