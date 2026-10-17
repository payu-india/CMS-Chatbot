---
title: Handling the Redirect URLs
excerpt: >-
  The `surl` and `furl` parameters in the **Collect Payment** API refer to the
  success and failure URLs respectively. These URLs are used to redirect the
  customer to your website after a successful or failed transaction.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
To handle **surl** and **furl** parameters with the **Collect Payment** API (\_payment), you can include them as part of the request payload. Here’s an example of how to do this:

```curl
{
    "txnid": "12345",
    "amount": "100.00",
    "productinfo": "Test Product",
    "firstname": "John",
    "email": "john@example.com",
    "phone": "9999999999",
    "surl": "http://example.com/success",
    "furl": "http://example.com/failure"
}
```

In the above example, the surl parameter is set to “[http://example.com/success”](http://example.com/success”) and the furl parameter is set to “[http://example.com/failure“](http://example.com/failure“). These URLs will be used by the PayU India API to redirect the customer to your website after a successful or failed transaction.

> 📘 Note:
>
> The URLs you provide for the surl & furl parameters must be accessible and valid.

The following sample code that demonstrates how to handle surl and furl parameters with the Collect Payment API:

```python
import hashlib
import requests
import os
import logging
from urllib.parse import urljoin

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def generate_payu_hash(params, salt):
    """
    Generate secure hash for PayU transaction
    Using the correct format: key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT
    """
    # Extract required parameters
    key = params['key']
    txnid = params['txnid']
    amount = params['amount']
    productinfo = params['productinfo']
    firstname = params['firstname']
    email = params['email']
    
    # Get optional udf values or use empty string
    udf1 = params.get('udf1', '')
    udf2 = params.get('udf2', '')
    udf3 = params.get('udf3', '')
    udf4 = params.get('udf4', '')
    udf5 = params.get('udf5', '')
    
    # Create hash string with the exact format (11 pipes after email)
    hash_string = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{salt}"
    
    # Generate SHA-512 hash
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()

def main():
    try:
        # Get credentials from environment variables (more secure)
        # Set these using: export PAYU_KEY=your_key && export PAYU_SALT=your_salt
        key = os.environ.get('PAYU_KEY')
        salt = os.environ.get('PAYU_SALT')
        
        if not key or not salt:
            raise ValueError("PayU credentials not found in environment variables. Set PAYU_KEY and PAYU_SALT.")
            
        # Set environment (test or production)
        is_test_env = os.environ.get('PAYU_TEST_MODE', 'true').lower() == 'true'
        base_url = "https://test.payu.in" if is_test_env else "https://secure.payu.in"
        payment_url = urljoin(base_url, "_payment")
            
        # Transaction details
        txnid = "txn" + str(int(time.time()))  # Unique transaction ID
        amount = "100.00"
        productinfo = "Product Description"
        firstname = "Customer Name"
        email = "customer@example.com"
        phone = "9876543210"
        
        # Redirect URLs - must be valid and accessible
        surl = "https://yourdomain.com/payment/success"
        furl = "https://yourdomain.com/payment/failure"
        
        # Prepare parameters dictionary
        params = {
            "key": key,
            "txnid": txnid,
            "amount": amount,
            "productinfo": productinfo,
            "firstname": firstname,
            "email": email,
            "phone": phone,
            "surl": surl,
            "furl": furl,
            # Optional UDFs for your reference
            "udf1": "reference-123"  # You can use this for order ID or other reference
        }
        
        # Generate hash and add to parameters
        params["hash"] = generate_payu_hash(params, salt)
        
        logger.info(f"Initiating PayU transaction: {txnid}")
        
        # Send POST request to PayU API
        response = requests.post(payment_url, data=params, timeout=30)
        
        # Check response status
        if response.status_code == 200:
            logger.info(f"Successfully initiated payment for transaction: {txnid}")
            # Note: For actual integration, PayU will redirect the user to payment page
            # This direct API access is typically for testing only
            return response.text
        else:
            logger.error(f"Failed to initiate payment. Status code: {response.status_code}")
            logger.error(f"Response: {response.text}")
            return f"Error: {response.status_code} - {response.text}"
            
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        return f"Error: {str(e)}"
    except ValueError as e:
        logger.error(f"Value error: {str(e)}")
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return f"Error: {str(e)}"

if __name__ == "__main__":
    import time
    result = main()
    print(result)

```
```php
<?php
/**
 * PayU Payment Integration - Handling Redirect URLs
 * This sample demonstrates the correct way to integrate with PayU's payment API
 */

// Set proper error reporting for development
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// Function to generate the PayU hash for secure transactions
function generatePayuHash($params, $salt) {
    // Extract required parameters
    $key = $params['key'];
    $txnid = $params['txnid'];
    $amount = $params['amount'];
    $productinfo = $params['productinfo'];
    $firstname = $params['firstname'];
    $email = $params['email'];
    
    // Get optional UDFs or use empty string
    $udf1 = isset($params['udf1']) ? $params['udf1'] : '';
    $udf2 = isset($params['udf2']) ? $params['udf2'] : '';
    $udf3 = isset($params['udf3']) ? $params['udf3'] : '';
    $udf4 = isset($params['udf4']) ? $params['udf4'] : '';
    $udf5 = isset($params['udf5']) ? $params['udf5'] : '';
    
    // Create hash string with exact format (11 pipes after email)
    $hashString = $key . '|' . $txnid . '|' . $amount . '|' . $productinfo . '|' . 
                  $firstname . '|' . $email . '|' . $udf1 . '|' . $udf2 . '|' . 
                  $udf3 . '|' . $udf4 . '|' . $udf5 . '||||||' . $salt;
    
    // Generate SHA-512 hash and convert to lowercase
    return strtolower(hash('sha512', $hashString));
}

// Main function to handle the payment process
function initiatePayuPayment() {
    try {
        // Get credentials from environment variables (more secure)
        // Set these in your server environment or .env file
        $key = getenv('PAYU_KEY');
        $salt = getenv('PAYU_SALT');
        
        if (!$key || !$salt) {
            throw new Exception("PayU credentials not found. Please set PAYU_KEY and PAYU_SALT environment variables.");
        }
        
        // Determine environment
        $isTestEnv = strtolower(getenv('PAYU_TEST_MODE') ?: 'true') === 'true';
        $paymentUrl = $isTestEnv ? 'https://test.payu.in/_payment' : 'https://secure.payu.in/_payment';
        
        // Transaction details
        $txnid = 'txn' . time();  // Unique transaction ID
        $amount = '100.00';
        $productinfo = 'Product Description';
        $firstname = 'Customer Name';
        $email = 'customer@example.com';
        $phone = '9876543210';
        
        // Redirect URLs - must be valid and accessible
        $surl = 'https://yourdomain.com/payment/success';
        $furl = 'https://yourdomain.com/payment/failure';
        
        // Validate redirect URLs
        if (!filter_var($surl, FILTER_VALIDATE_URL) || !filter_var($furl, FILTER_VALIDATE_URL)) {
            throw new Exception("Invalid redirect URLs. Please provide valid success and failure URLs.");
        }
        
        // Prepare parameters array
        $params = array(
            'key' => $key,
            'txnid' => $txnid,
            'amount' => $amount,
            'productinfo' => $productinfo,
            'firstname' => $firstname,
            'email' => $email,
            'phone' => $phone,
            'surl' => $surl,
            'furl' => $furl,
            'udf1' => 'reference-123'  // Optional - can be used for order reference
        );
        
        // Generate hash and add to parameters
        $params['hash'] = generatePayuHash($params, $salt);
        
        // Log the transaction initiation
        error_log("Initiating PayU transaction: {$txnid}");
        
        // Using cURL for better control and error handling
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $paymentUrl);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($params));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 30);
        curl_setopt($ch, CURLOPT_TIMEOUT, 30);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
        
        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $error = curl_error($ch);
        curl_close($ch);
        
        // Check for errors
        if ($error) {
            error_log("cURL Error: {$error}");
            throw new Exception("Connection error: {$error}");
        }
        
        // Process response
        if ($httpCode == 200) {
            error_log("Successfully initiated payment for transaction: {$txnid}");
            
            // Note: For actual integration, PayU typically redirects the user
            // This direct API call approach is mainly for testing
            return [
                'success' => true,
                'message' => 'Payment initiated successfully',
                'txnid' => $txnid,
                'response' => $response
            ];
        } else {
            error_log("Failed to initiate payment. Status code: {$httpCode}");
            error_log("Response: {$response}");
            throw new Exception("Error initiating payment: HTTP {$httpCode}");
        }
        
    } catch (Exception $e) {
        error_log("PayU payment error: " . $e->getMessage());
        return [
            'success' => false,
            'message' => $e->getMessage()
        ];
    }
}

// Execute the payment function
$result = initiatePayuPayment();

// Output the result
if ($result['success']) {
    echo "Payment initiated successfully. Transaction ID: " . $result['txnid'];
} else {
    echo "Payment initiation failed: " . $result['message'];
}
?>

```
```javascript
/**
 * PayU Payment Integration - Handling Redirect URLs (Node.js)
 * Server-side implementation for security best practices
 */

const crypto = require('crypto');
const axios = require('axios');
const express = require('express');
const bodyParser = require('body-parser');
require('dotenv').config(); // For loading environment variables

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

/**
 * Generates the PayU hash for secure transactions
 * @param {Object} params - The payment parameters
 * @param {string} salt - The PayU salt
 * @returns {string} - The generated hash
 */
function generatePayuHash(params, salt) {
    // Extract required parameters
    const key = params.key;
    const txnid = params.txnid;
    const amount = params.amount;
    const productinfo = params.productinfo;
    const firstname = params.firstname;
    const email = params.email;
    
    // Get optional UDFs or use empty string
    const udf1 = params.udf1 || '';
    const udf2 = params.udf2 || '';
    const udf3 = params.udf3 || '';
    const udf4 = params.udf4 || '';
    const udf5 = params.udf5 || '';
    
    // Create hash string with exact format (11 pipes after email)
    const hashString = `${key}|${txnid}|${amount}|${productinfo}|${firstname}|${email}|${udf1}|${udf2}|${udf3}|${udf4}|${udf5}||||||${salt}`;
    
    // Generate SHA-512 hash and convert to lowercase
    return crypto.createHash('sha512').update(hashString).digest('hex').toLowerCase();
}

/**
 * Initiates a payment with PayU
 */
app.post('/api/initiate-payment', async (req, res) => {
    try {
        // Get credentials from environment variables
        const key = process.env.PAYU_KEY;
        const salt = process.env.PAYU_SALT;
        
        if (!key || !salt) {
            throw new Error('PayU credentials not configured. Set PAYU_KEY and PAYU_SALT environment variables.');
        }
        
        // Determine environment
        const isTestEnv = (process.env.PAYU_TEST_MODE || 'true').toLowerCase() === 'true';
        const paymentUrl = isTestEnv ? 'https://test.payu.in/_payment' : 'https://secure.payu.in/_payment';
        
        // Get customer and payment details from request
        // In a real app, validate all inputs thoroughly
        const { productinfo, amount, firstname, email, phone } = req.body;
        
        // Validate required fields
        if (!productinfo || !amount || !firstname || !email || !phone) {
            return res.status(400).json({ 
                success: false, 
                message: 'Missing required fields' 
            });
        }
        
        // Generate unique transaction ID
        const txnid = 'txn' + Date.now();
        
        // Redirect URLs - must be valid and accessible
        // In production, these should be configured in your app settings
        const baseUrl = process.env.APP_BASE_URL || 'https://yourdomain.com';
        const surl = `${baseUrl}/payment/success`;
        const furl = `${baseUrl}/payment/failure`;
        
        // Prepare parameters object
        const params = {
            key,
            txnid,
            amount,
            productinfo,
            firstname,
            email,
            phone,
            surl,
            furl,
            udf1: req.body.reference || '' // Optional - can be used for order reference
        };
        
        // Generate hash and add to parameters
        params.hash = generatePayuHash(params, salt);
        
        console.log(`Initiating PayU transaction: ${txnid}`);
        
        // Option 1: Return form data for client-side form submission
        // This is the recommended approach as it allows PayU to handle the redirect
        return res.status(200).json({
            success: true,
            message: 'Payment initiated',
            txnid,
            paymentUrl,
            formData: params
        });
        
        /* 
        // Option 2: Server-side API call (for testing only)
        // Note: In production, PayU expects a user's browser to submit the form
        const response = await axios.post(paymentUrl, params, {
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            timeout: 30000
        });
        
        console.log(`Payment initiated: ${txnid}`);
        return res.status(200).json({
            success: true,
            message: 'Payment initiated',
            txnid,
            data: response.data
        });
        */
        
    } catch (error) {
        console.error('PayU payment error:', error.message);
        return res.status(500).json({
            success: false,
            message: `Payment initiation failed: ${error.message}`
        });
    }
});

// Example route to render a payment form
app.get('/payment', (req, res) => {
    res.send(`
        <h1>Payment Form</h1>
        <form id="paymentForm">
            <div>
                <label for="productinfo">Product:</label>
                <input type="text" id="productinfo" name="productinfo" value="Product Description" required>
            </div>
            <div>
                <label for="amount">Amount:</label>
                <input type="text" id="amount" name="amount" value="100.00" required>
            </div>
            <div>
                <label for="firstname">Name:</label>
                <input type="text" id="firstname" name="firstname" required>
            </div>
            <div>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div>
                <label for="phone">Phone:</label>
                <input type="text" id="phone" name="phone" required>
            </div>
            <div>
                <label for="reference">Reference (Optional):</label>
                <input type="text" id="reference" name="reference">
            </div>
            <button type="submit">Pay Now</button>
        </form>
        
        <script>
            document.getElementById('paymentForm').addEventListener('submit', async function(e) {
                e.preventDefault();
                
                // Get form data
                const formData = new FormData(this);
                const formObject = {};
                formData.forEach((value, key) => { formObject[key] = value });
                
                try {
                    // Send to your server endpoint
                    const response = await fetch('/api/initiate-payment', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(formObject)
                    });
                    
                    const result = await response.json();
                    
                    if (result.success) {
                        // Create and submit a form to PayU
                        const form = document.createElement('form');
                        form.method = 'POST';
                        form.action = result.paymentUrl;
                        
                        // Add all parameters as hidden fields
                        for (const key in result.formData) {
                            const input = document.createElement('input');
                            input.type = 'hidden';
                            input.name = key;
                            input.value = result.formData[key];
                            form.appendChild(input);
                        }
                        
                        // Add the form to the document and submit it
                        document.body.appendChild(form);
                        form.submit();
                    } else {
                        alert('Error: ' + result.message);
                    }
                } catch (error) {
                    console.error('Error:', error);
                    alert('An error occurred. Please try again.');
                }
            });
        </script>
    `);
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

```
```java
package com.example.payuintegration;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.time.Instant;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * PayU Payment Integration - Handling Redirect URLs
 * Java implementation with proper error handling and security practices
 */
public class PayURedirectUrlsHandler {
    private static final Logger LOGGER = Logger.getLogger(PayURedirectUrlsHandler.class.getName());
    
    // Environment variables for configuration (more secure)
    private static final String PAYU_KEY = System.getenv("PAYU_KEY");
    private static final String PAYU_SALT = System.getenv("PAYU_SALT");
    private static final boolean IS_TEST_ENV = "true".equalsIgnoreCase(System.getenv("PAYU_TEST_MODE"));
    
    /**
     * Generates the PayU hash for secure transactions
     * 
     * @param params Payment parameters
     * @param salt PayU salt for hash generation
     * @return Generated hash string
     * @throws NoSuchAlgorithmException If SHA-512 algorithm is not available
     */
    public static String generatePayuHash(Map<String, String> params, String salt) throws NoSuchAlgorithmException {
        // Extract required parameters
        String key = params.get("key");
        String txnid = params.get("txnid");
        String amount = params.get("amount");
        String productinfo = params.get("productinfo");
        String firstname = params.get("firstname");
        String email = params.get("email");
        
        // Get optional UDFs or use empty string
        String udf1 = params.getOrDefault("udf1", "");
        String udf2 = params.getOrDefault("udf2", "");
        String udf3 = params.getOrDefault("udf3", "");
        String udf4 = params.getOrDefault("udf4", "");
        String udf5 = params.getOrDefault("udf5", "");
        
        // Create hash string with exact format (11 pipes after email)
        String hashString = key + "|" + txnid + "|" + amount + "|" + productinfo + "|" + 
                           firstname + "|" + email + "|" + udf1 + "|" + udf2 + "|" + 
                           udf3 + "|" + udf4 + "|" + udf5 + "||||||" + salt;
        
        // Generate SHA-512 hash
        return hashCal("SHA-512", hashString).toLowerCase();
    }
    
    /**
     * Calculates hash using specified algorithm
     * 
     * @param algo Hash algorithm (e.g., SHA-512)
     * @param data Input string to hash
     * @return Hash value as hexadecimal string
     * @throws NoSuchAlgorithmException If the algorithm is not available
     */
    public static String hashCal(String algo, String data) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance(algo);
        byte[] digest = md.digest(data.getBytes(StandardCharsets.UTF_8));
        
        StringBuilder hash = new StringBuilder();
        for (byte b : digest) {
            hash.append(String.format("%02x", b & 0xff));
        }
        
        return hash.toString();
    }
    
    /**
     * URL-encodes a map of parameters
     * 
     * @param params Map of parameters to encode
     * @return URL-encoded string
     * @throws IOException If encoding fails
     */
    private static String encodeParams(Map<String, String> params) throws IOException {
        StringBuilder result = new StringBuilder();
        boolean first = true;
        
        for (Map.Entry<String, String> entry : params.entrySet()) {
            if (first) {
                first = false;
            } else {
                result.append("&");
            }
            
            result.append(URLEncoder.encode(entry.getKey(), "UTF-8"));
            result.append("=");
            result.append(URLEncoder.encode(entry.getValue(), "UTF-8"));
        }
        
        return result.toString();
    }
    
    /**
     * Initiates a payment with PayU
     * 
     * @return Result of the payment initiation
     */
    public static Map<String, Object> initiatePayment() {
        Map<String, Object> result = new HashMap<>();
        HttpURLConnection connection = null;
        
        try {
            // Validate credentials
            if (PAYU_KEY == null || PAYU_KEY.isEmpty() || PAYU_SALT == null || PAYU_SALT.isEmpty()) {
                throw new IllegalStateException("PayU credentials not found. Set PAYU_KEY and PAYU_SALT environment variables.");
            }
            
            // Determine API URL based on environment
            String paymentUrl = IS_TEST_ENV ? 
                "https://test.payu.in/_payment" : 
                "https://secure.payu.in/_payment";
            
            // Transaction details
            String txnid = "txn" + Instant.now().getEpochSecond();
            String amount = "100.00";
            String productinfo = "Product Description";
            String firstname = "Customer Name";
            String email = "customer@example.com";
            String phone = "9876543210";
            
            // Redirect URLs - must be valid and accessible
            String surl = "https://yourdomain.com/payment/success";
            String furl = "https://yourdomain.com/payment/failure";
            
            // Prepare parameters map
            Map<String, String> params = new HashMap<>();
            params.put("key", PAYU_KEY);
            params.put("txnid", txnid);
            params.put("amount", amount);
            params.put("productinfo", productinfo);
            params.put("firstname", firstname);
            params.put("email", email);
            params.put("phone", phone);
            params.put("surl", surl);
            params.put("furl", furl);
            params.put("udf1", "reference-123");  // Optional - for your reference
            
            // Generate hash and add to parameters
            params.put("hash", generatePayuHash(params, PAYU_SALT));
            
            LOGGER.info("Initiating PayU transaction: " + txnid);
            
            // Encode parameters
            String postData = encodeParams(params);
            byte[] postDataBytes = postData.getBytes(StandardCharsets.UTF_8);
            
            // Set up connection
            URL url = new URL(paymentUrl);
            connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            connection.setRequestProperty("Content-Length", String.valueOf(postDataBytes.length));
            connection.setRequestProperty("User-Agent", "Java PayU Integration");
            connection.setConnectTimeout(30000);
            connection.setReadTimeout(30000);
            connection.setDoOutput(true);
            
            // Send request
            try (OutputStream os = connection.getOutputStream()) {
                os.write(postDataBytes);
                os.flush();
            }
            
            // Get response code
            int responseCode = connection.getResponseCode();
            
            // Read response
            StringBuilder response = new StringBuilder();
            try (BufferedReader in = new BufferedReader(
                    new InputStreamReader(
                        responseCode >= 400 ? 
                        connection.getErrorStream() : 
                        connection.getInputStream(), 
                        StandardCharsets.UTF_8))) {
                
                String line;
                while ((line = in.readLine()) != null) {
                    response.append(line);
                }
            }
            
            // Process response
            if (responseCode == 200) {
                LOGGER.info("Successfully initiated payment for transaction: " + txnid);
                result.put("success", true);
                result.put("txnid", txnid);
                result.put("message", "Payment initiated successfully");
                result.put("response", response.toString());
            } else {
                LOGGER.log(Level.WARNING, "Failed to initiate payment. Status code: {0}", responseCode);
                LOGGER.warning("Response: " + response);
                result.put("success", false);
                result.put("message", "Error initiating payment: HTTP " + responseCode);
                result.put("response", response.toString());
            }
            
        } catch (Exception e) {
            LOGGER.log(Level.SEVERE, "Error in payment initiation", e);
            result.put("success", false);
            result.put("message", e.getMessage());
        } finally {
            if (connection != null) {
                connection.disconnect();
            }
        }
        
        return result;
    }
    
    /**
     * Main method for testing
     */
    public static void main(String[] args) {
        // For testing, you can set environment variables programmatically
        // In production, set these in your environment
        if (System.getenv("PAYU_KEY") == null) {
            // This is for testing only - in production use proper environment variables
            System.out.println("Setting test environment variables - FOR TESTING ONLY");
            
            Map<String, String> testEnv = new HashMap<>();
            testEnv.put("PAYU_KEY", "your_test_key");  // Replace with your test key
            testEnv.put("PAYU_SALT", "your_test_salt");  // Replace with your test salt
            testEnv.put("PAYU_TEST_MODE", "true");
            
            // Set environment variables (Java 9+ way)
            testEnv.forEach(System::setProperty);
        }
        
        Map<String, Object> result = initiatePayment();
        
        if ((boolean) result.get("success")) {
            System.out.println("Payment initiated successfully!");
            System.out.println("Transaction ID: " + result.get("txnid"));
        } else {
            System.out.println("Payment initiation failed: " + result.get("message"));
        }
    }
}

```

The following sections provide how it is implemented in the various language bindings:

* [Java](#java-implementation)
* [JavaScript](#javascript-implementation)
* [Python](#python-implementation)
* [PHP](#php-implementation)

## Java implementation

This Java implementation provides a comprehensive example of initiating PayU payments with proper redirect URL handling. The code follows Java best practices for security, exception handling, and HTTP communication.

#### Key Components:

1. **Hash Generation Methods**:
   * `generatePayuHash()` creates the properly formatted hash string
   * `hashCal()` computes the SHA-512 hash using Java's MessageDigest
   * Handles optional parameters with sensible defaults

2. **Environment Configuration**:
   * Uses system environment variables for secure credential storage
   * Supports runtime environment detection (test/production)
   * Includes fallback for testing purposes only

3. **HTTP Connection Handling**:
   * Properly configures HttpURLConnection with timeouts and headers
   * Handles both successful and error responses
   * Implements proper resource cleanup with try-finally blocks

4. **Comprehensive Logging**:
   * Uses Java's built-in Logger for consistent logging
   * Records transaction initiation, success, and failures
   * Provides detailed error information for troubleshooting

#### Implementation Notes:

* In a web application context, this code would typically be part of a service class
* For production use, integrate with your application's configuration management
* Set the redirect URLs (`surl` and `furl`) to valid endpoints in your application
* The example includes main() for testing, but in practice would be called by your application logic
* Consider using a modern HTTP client library like Apache HttpClient or OkHttp in production systems

## JavaScript implementation

This Node.js example demonstrates a complete server implementation for handling PayU payments with proper redirect URL configuration. It provides both server-side security and client-side convenience.

#### Key Components:

1. **Express Server Setup**:
   * Configures routes for payment initiation and form rendering
   * Implements body parsing for form submissions
   * Uses environment variables for configuration

2. **Hash Generation Function**:
   * Uses Node.js `crypto` module for secure hash generation
   * Properly formats the hash string with all required parameters
   * Converts the resulting hash to lowercase as required by PayU

3. **Client-Side Form Handling**:
   * Demonstrates secure client-side to server-side communication
   * Creates and submits a dynamic form to PayU
   * Handles user feedback during the payment process

4. **Two-Step Payment Flow**:
   * Separates hash generation (server-side) from form submission (client-side)
   * Prevents exposure of sensitive credentials to end users
   * Maintains a seamless user experience

#### Implementation Notes:

* Store your `PAYU_KEY` and `PAYU_SALT` in environment variables, never in client-side code
* The server endpoint returns form data that is then submitted by the browser to PayU
* This approach maintains security while providing a smooth redirect experience
* Remember to implement the success and failure URL handlers to process PayU's response
* For production, enhance form validation and add CSRF protection

### Python implementation

This example demonstrates how to securely initiate a payment with PayU while properly configuring redirect URLs. The code follows security best practices and includes robust error handling.

1. **Hash Generation Function**: 
   * Properly formats the payment parameters with the correct number of pipes (11 after email)
   * Generates a SHA-512 hash to ensure data integrity

2. **Environment Variable Usage**: 
   * Retrieves API credentials from environment variables instead of hardcoding them
   * Supports both test and production environments

3. **Payment Parameter Preparation**:
   * Creates a unique transaction ID for each payment request
   * Organizes all required and optional parameters in a dictionary
   * Adds the generated hash to secure the transaction

4. **Robust Error Handling**:
   * Implements proper exception handling for network issues
   * Validates required parameters
   * Uses logging for debugging and auditing

#### Implementation Notes:

* Ensure you set `PAYU_KEY` and `PAYU_SALT` environment variables
* Configure valid, accessible redirect URLs at `surl` and `furl`
* In production, integrate this into your web application's payment flow
* The transaction response typically contains HTML that should be rendered to the user's browser to facilitate the redirect

## PHP implementation

This example demonstrates a secure PHP implementation for initiating payments with PayU. It follows PHP best practices while ensuring proper redirect URL handling and hash generation.

#### Key Components:

1. **Hash Generation Function**:
   * Creates the hash string with proper parameter ordering and pipe delimiters
   * Uses PHP's built-in `hash()` function with SHA-512 algorithm
   * Handles optional parameters correctly

2. **Secure Credential Management**:
   * Retrieves API credentials from environment variables using `getenv()`
   * Supports runtime environment detection (test/production)

3. **cURL Implementation**:
   * Uses PHP's cURL extension for reliable API communication
   * Sets appropriate headers and timeout values
   * Provides detailed error reporting

4. **URL Validation**:
   * Validates redirect URLs using `filter_var()` with `FILTER_VALIDATE_URL`
   * Ensures redirect endpoints are properly formatted

#### Implementation Notes:

* Configure your web server with `PAYU_KEY` and `PAYU_SALT` environment variables
* Customize the success and failure URLs to point to valid endpoints on your domain
* Adjust logging to use your application's existing logging system
* The initiation function returns an array with success status and relevant messages
* In a production environment, this code would typically be part of a controller class
