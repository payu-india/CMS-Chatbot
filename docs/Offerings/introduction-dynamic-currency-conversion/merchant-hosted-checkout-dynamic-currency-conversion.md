---
title: Merchant Hosted Checkout Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: >-
    Merchant Hosted Checkout Integration for International Payments or Dynamic
    Currency Conversion
  description: >-
    Learn how to integrate PayU’s Merchant Hosted Checkout feature with Dynamic
    Currency Conversion (DCC) to offer your customers a customized and secure
    payment experience in their preferred currency. Follow the step-by-step
    procedure to set up your integration and start accepting international
    payments with PayU.
  keywords:
    - Dynamic Currency Conversion with Merchant Hosted Checkout
    - DCC with Seamless Integration
    - ' Currency Conversion with Merchant Hosted Checkout'
    - Seamless Integration for Currency Conversion
    - >-
      Multi-Currency Payment Integration with Merchant Hosted
      Checkout.International Payments with Merchant Hosted Integration
    - Foreign Currency Payment with Merchant Hosted Integration
  robots: index
next:
  description: ''
---
This section describes how to integrate Dynamic Currency Conversion with Merchant Hosted Checkout Integration (Seamless Integration).

<Callout icon="📘" theme="info">
  ###

  **Notes**:

  - You need to contact your PayU Key Account Manager to enable international payments.
  - For the list of supported currencies, <a href="https://docs.payu.in/docs/supported-currencies-for-international-payments/" target="_blank">Supported Currencies for International Payments</a>.
</Callout>

<Callout icon="👍" theme="okay">
  ###

  **Before you begin**: Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Callout>

**Steps to Integrate**

<Cards columns={2}>
  <Card title="1. Check the Card BIN" href="#step-1-check-the-card-bin">
    Validate the card Bank Identification Number (BIN) to determine card type and eligibility

    <br />
  </Card>

  <Card title="2. Post the Parameters to PayU" href="#step-2-post-the-parameters-to-payu">
    Send the required payment parameters to PayU for transaction processing

    <br />
  </Card>

  <Card title="3. Check the Response from PayU" href="#step-3-check-the-response-from-payu">
    Handle and process the response received from PayU after parameter submission
  </Card>

  <Card title="4. Verify the Payment" href="#step-4-verify-the-payment">
    Confirm the payment status and ensure successful transaction completion

    <br />
  </Card>
</Cards>

## Step 1: Check the card BIN

Check if the card number of the customer is international or domestic using the **Check is Domestic** API. This is to avoid payment failure and validation of the card BIN. For Try-It experience for the **Check is Domestic** API, refer to [Check is Domestic API](ref:check_is_domestic_api) under API Reference.

**Environment**

| Environment            | URL                                                                                                          |
| :--------------------- | :----------------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice?form=2](https://info.payu.in/merchant/postservice?form=2)         |

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&command=check_isDomestic&var1=462273&hash=df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2"
  ```

  **Example Values:**

  * `var1` (first six digit of the card): 512345
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ## If the card is domestic

  ```json
  {
    "isDomestic": "Y",
    "issuingBank": "SCB",
    "cardType": "VISA",
    "cardCategory": "CC"
  }
  ```

  ## If the card is international

  ```json
  {
    "isDomestic": "N",
    "issuingBank": "UNKNOWN",
    "cardType": "Unknown",
    "cardCategory": "CC"
  }
  ```
</Accordion>

## Step 2: Post the parameters to PayU

Make the transaction request with the payment details provided by the customer to PayU. For international payments, the \_payment request remains the same and no extra parameters required. For Try-It experience, refer to <a href="_payment_merchant_hosted" target="_blank">Collect Payments API</a>.

<Callout icon="📘" theme="info">
  ###

  **Note**: It is recommended to collect the customer’s e-mail address, phone, address, city, state, and country and then post those details along with the payment request with PayU. This will help in checking the risk of the transaction based on these data.
</Callout>

<Accordion title="Request parameters" icon="fa-code">
  | Parameter                                                                    | Description                                                                                                                                                                                                                                                                                                                        | Example               |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | -------- | ------------- | ----------- | ------- | ------ | ------ | ------ | ------ | ------ | -- | -- | -- | -- | -- | ------- | - |
  | key<br />`mandatory`                                                         | `String` Merchant key provided by PayU during onboarding.                                                                                                                                                                                                                                                                          | JP\*\*\*g             |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | txnid<br />`mandatory`                                                       | `String` The transaction ID is a reference number for a specific order that is generated by the merchant.                                                                                                                                                                                                                          | ashdfu72634           |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | amount<br />`mandatory`                                                      | `String` The payment amount for the transaction.                                                                                                                                                                                                                                                                                   |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | productinfo<br />`mandatory`                                                 | `String` A brief description of the product.                                                                                                                                                                                                                                                                                       |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | firstname<br />`mandatory`                                                   | `String` The first name of the customer.                                                                                                                                                                                                                                                                                           | Ashish                |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | email<br />`mandatory`                                                       | `String` The email address of the customer.                                                                                                                                                                                                                                                                                        |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | phone<br />`mandatory`                                                       | `String` The phone number of the customer.                                                                                                                                                                                                                                                                                         |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | pg<br />`mandatory`                                                          | `String` The pg parameter determines which payment tabs will be displayed on the PayU page. For cards, 'CC' will be the value.                                                                                                                                                                                                     | CC                    |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | bankcode<br />`mandatory`                                                    | `String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For more information, refer to [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards).                | AMEX                  |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | ccnum<br />`mandatory`                                                       | `String` Use 13-19 digit card number for credit/debit cards (15 digits for AMEX, 13-19 for Maestro) and validate with LUHN algorithm. Refer to [Card Number Formats](doc:card-number-formats) and display error message on invalid input.                                                                                          | 5123456789012346      |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | ccname<br />`mandatory`                                                      | `String` This parameter must contain the name on card – as entered by the customer for the transaction.                                                                                                                                                                                                                            | Ashish Kumar          |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | ccvv<br />`mandatory`                                                        | `String` Use 3-digit CVV number for credit/debit cards and 4-digit security code (4DBC/CID) for AMEX cards. Validate with BIN API.                                                                                                                                                                                                 | 123                   |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | ccexpmon<br />`mandatory`                                                    | `String` This parameter must contain the card's expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format. For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively. | 10                    |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | ccexpyr<br />`mandatory`                                                     | `String` This parameter must contain the card's expiry year – as entered by the customer for the transaction. It must be of four digits.                                                                                                                                                                                           | 2021                  |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | furl<br />`mandatory`                                                        | `String` The success URL, which is the page PayU will redirect to if the transaction is successful.                                                                                                                                                                                                                                |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | surl<br />`mandatory`                                                        | `String` The Failure URL, which is the page PayU will redirect to if the transaction is failed.                                                                                                                                                                                                                                    |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | hash<br />`mandatory`                                                        | `String` It is the hash calculated by the merchant. The hash calculation logic is:<br />\`sha512(key\\                                                                                                                                                                                                                             | txnid\\               | amount\\ | productinfo\\ | firstname\\ | email\\ | udf1\\ | udf2\\ | udf3\\ | udf4\\ | udf5\\ | \\ | \\ | \\ | \\ | \\ | SALT)\` |   |
  | transactionCurrency<br />`optional (mandatory for multi-currency merchants)` | `String` The payment currency for the transaction. Merchants initiating multi-currency payments must pass a valid 3-alpha currency code (ISO 4217 code) in this field. For more information, refer to [MCC Currency Codes](https://docs.payu.in/docs/mcc-currency-codes).                                                          | INR, USD, AED, OR GBP |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | address1<br />`optional`                                                     | `String` The first line of the billing address.<br />**For Fraud Detection**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is required to provide the correct information.                                                                                                |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | address2<br />`optional`                                                     | `String` The second line of the billing address.                                                                                                                                                                                                                                                                                   |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | city<br />`optional`                                                         | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                      |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | state<br />`optional`                                                        | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                     |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | country<br />`optional`                                                      | `String` The country where your customer resides.                                                                                                                                                                                                                                                                                  |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | zipcode<br />`optional`                                                      | `String` Billing address zip code is mandatory for the cardless EMI option.<br />`Character Limit`: 20                                                                                                                                                                                                                             |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | udf1<br />`optional`                                                         | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.                                                                                                                                |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | udf2<br />`optional`                                                         | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.                                                                                                                                |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | udf3<br />`optional`                                                         | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.                                                                                                                                                                                                                    |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | udf4<br />`optional`                                                         | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.                                                                                                                                                                                                                    |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |
  | udf5<br />`optional`                                                         | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction.                                                                                                                                                                                                                    |                       |          |               |             |         |        |        |        |        |        |    |    |    |    |    |         |   |

  <HashingRequestParameters />
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  # IMPORTANT: This is a server-side call, never execute this client-side
  # Replace placeholders with actual values
  # In production: Use environment variables for sensitive values

curl -X POST "[https://test.payu.in/\_payment](https://test.payu.in/_payment)" <br />-H "Content-Type: application/x-www-form-urlencoded" <br />-d "key=YOUR\_MERCHANT\_KEY" <br />-d "txnid=TXN\_12345" <br />-d "amount=1000.00" <br />-d "productinfo=Product+Description" <br />-d "firstname=Customer+Name" <br />-d "email=[customer@example.com](mailto:customer@example.com)" <br />-d "phone=9988776655" <br />-d "pg=CC" <br />-d "bankcode=CC" <br />-d "ccnum=CARD\_NUMBER" <br />-d "ccexpmon=MM" <br />-d "ccexpyr=YY" <br />-d "ccvv=CVV" <br />-d "ccname=NAME\_ON\_CARD" <br />-d "surl=[https://yourwebsite.com/success](https://yourwebsite.com/success)" <br />-d "furl=[https://yourwebsite.com/failure](https://yourwebsite.com/failure)" <br />-d "hash=HASH\_GENERATED\_ON\_SERVER"

````
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

````
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
        public async Task<PaymentResponse> ProcessPaymentAsync()
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

## Step 3: Check the response from PayU

<ReverseHashing />

### Sample response

```json
Array
(
    [mihpayid] => 4***9371***40***25
    [mode] => NB
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => bvRCCBO4YiGGHE
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2021-09-06 13:59:39
    [productinfo] => iPhone
    [firstname] => Ashish
    [lastname] => 
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => 
    [zipcode] => 
    [email] => abc@gmail.com
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
    [hash] => fa7bb889d25b2a60bcf32316d1c9346589ff3de012dd0c66aa47ec12f1349837163ef8a603bd8b357de610b768f08dc4fb3bb4702d1ca6d9751300667fd763a6
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
    [PG_TYPE] => CC-PG
    [bank_ref_num] => ae67e632-f4eb-4121-b47b-2d35dce5ec2e
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
)
```

## Step 4: Verify the payment

<Verify_Payment_Tabs />

<br />
