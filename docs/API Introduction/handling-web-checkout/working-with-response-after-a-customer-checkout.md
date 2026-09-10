---
title: Working with Response after a Customer Checkout
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You will require to wrAll PayU India APIs use cURL format for posting requests to endpoints and endpoints provide a response in encoded URL format. You need to convert the encoded URL format to an array format.ite some amount of code to collect the details from your customer and submit those details with PayU using a cURL with PayU Hosted Checkout integration.

The response will contain response parameters and a few response parameters may contain the values in a JSON format. Therefore, you need to learn how to read and write data in the array format and JSON format. The array and JSON formats are similar, where the data is stored in key-value pairs. For instance, the following response is an example of a successful response to a **Collect Payment API** request.

```
Array
(
    [mihpayid] => 4***********2
    [mode] => NB
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => ewP8oRopzdHEtC
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2021-09-06 13:27:08
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
    [hash] => 1be7e6e97ab1ea9034b9a107e7cf9718308aa9637b4dbbd1a3343c91b0da02b34a40d00ac7267ebe81c20ea1129b931371c555d565bc6e11f470c3d2cf69b5a3
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
    [PG_TYPE] => NB-PG
    [bank_ref_num] => 87d3b2a1-5a60-4169-8692-649f61923b3d
    [bankcode] => TESTPGNB
    [error] => E000
    [error_Message] => No Error
)
```

## Adding a make Payment button to your website (HTML)

After your customer completes adding the products on your website to the cart, the customer will checkout. Here, in this example, start by creating an HTML where a button.

```plaintext
<button id="button" type='button'>Get Joke</button>
```

Later, you will reference the button in the JS. The `type="button"` tells the browser that this isn’t a typical form submission button.

You need to parse this response as per the programming language you are using to implement. For example, the following sample code is in JS, Java, Python, and PHP:

```python
# This would be a Flask/Django/FastAPI route that handles the PayU redirect

import hashlib
import os
from flask import Flask, request, render_template
 
app = Flask(__name__)

@app.route('/payment/success', methods=['POST'])
def payment_success():
    # Get all POST data from PayU
    post_data = request.form.to_dict()
    
    # Log the response for debugging
    app.logger.info(f"PayU Response: {post_data}")
    
    # Verify response hash
    is_valid = verify_payu_response(post_data)
    
    if not is_valid:
        # Hash validation failed, potential security issue
        app.logger.error(f"PayU response hash validation failed: {post_data.get('txnid')}")
        return render_template('payment_error.html', 
                              message="Invalid response hash. Transaction verification failed.")
    
    # Process based on payment status
    if post_data.get('status') == 'success':
        # Payment successful
        txn_id = post_data.get('txnid')
        payu_id = post_data.get('mihpayid')
        amount = post_data.get('amount')
        
        # Update your database with the successful payment
        update_order_status(txn_id, 'PAID', payu_id)
        
        # Show success page to user
        return render_template('payment_success.html', 
                              txn_id=txn_id,
                              payu_id=payu_id,
                              amount=amount)
    else:
        # Payment failed
        txn_id = post_data.get('txnid')
        error_message = post_data.get('error_Message', 'Unknown error')
        
        # Update your database with the failed payment
        update_order_status(txn_id, 'FAILED', error_message=error_message)
        
        # Show failure page to user
        return render_template('payment_failure.html', 
                              txn_id=txn_id,
                              error=error_message)

def verify_payu_response(params):
    # Get salt from environment variable
    salt = os.environ.get('PAYU_SALT')
    
    # Check if all required parameters exist
    required_params = ['status', 'txnid', 'amount', 'productinfo', 'firstname', 'email', 'key', 'hash']
    if not all(param in params for param in required_params):
        return False
    
    # Create hash string with exact parameter sequence
    # Reverse hash format for response validation:
    # sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
    
    hash_string = f"{salt}|{params.get('status')}||||||"
    
    # Add UDFs if present
    hash_string += f"{params.get('udf5', '')}|"
    hash_string += f"{params.get('udf4', '')}|"
    hash_string += f"{params.get('udf3', '')}|"
    hash_string += f"{params.get('udf2', '')}|"
    hash_string += f"{params.get('udf1', '')}|"
    
    # Add remaining fields
    hash_string += f"{params.get('email')}|"
    hash_string += f"{params.get('firstname')}|"
    hash_string += f"{params.get('productinfo')}|"
    hash_string += f"{params.get('amount')}|"
    hash_string += f"{params.get('txnid')}|"
    hash_string += f"{params.get('key')}"
    
    # Calculate hash
    calculated_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
    
    # Compare the calculated hash with the hash received in the response
    return calculated_hash == params.get('hash')

def update_order_status(txn_id, status, payu_id=None, error_message=None):
    # Database update logic here (implementation depends on your database and ORM)
    pass

if __name__ == '__main__':
    app.run(debug=True)

```
```php
<?php
// This file would be your success.php or failure.php URL that PayU redirects to

// Get all POST data from PayU
$postData = $_POST;

// Log the response for debugging (in a production environment, log securely)
error_log('PayU Response: ' . json_encode($postData));

// Verify response hash
function verifyPayuResponse($params, $salt) {
    // Check if all required parameters exist
    if (!isset($params['status'], $params['txnid'], $params['amount'], 
               $params['productinfo'], $params['firstname'], $params['email'], 
               $params['key'], $params['hash'])) {
        return false;
    }
    
    // Create hash string with exact parameter sequence 
    // Reverse hash format for response validation:
    // sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
    
    $hashString = $salt . '|' . $params['status'] . '||||||';
    
    // Add UDFs if present
    $hashString .= (isset($params['udf5']) ? $params['udf5'] : '') . '|';
    $hashString .= (isset($params['udf4']) ? $params['udf4'] : '') . '|';
    $hashString .= (isset($params['udf3']) ? $params['udf3'] : '') . '|';
    $hashString .= (isset($params['udf2']) ? $params['udf2'] : '') . '|';
    $hashString .= (isset($params['udf1']) ? $params['udf1'] : '') . '|';
    
    // Add remaining fields
    $hashString .= $params['email'] . '|' . 
                  $params['firstname'] . '|' . 
                  $params['productinfo'] . '|' . 
                  $params['amount'] . '|' . 
                  $params['txnid'] . '|' . 
                  $params['key'];
    
    // Calculate hash
    $calculatedHash = strtolower(hash('sha512', $hashString));
    
    // Compare the calculated hash with the hash received in the response
    return $calculatedHash === $params['hash'];
}

// Get salt from a secure source (environment variable recommended)
$salt = getenv('PAYU_SALT');

// Verify the response hash
$isValidHash = verifyPayuResponse($postData, $salt);

if (!$isValidHash) {
    // Hash validation failed, potential security issue
    error_log('PayU response hash validation failed: ' . $postData['txnid']);
    echo "Invalid response hash. Transaction verification failed.";
    exit;
}

// Process based on payment status
if ($postData['status'] === 'success') {
    // Payment successful
    $txnId = $postData['txnid'];
    $payuId = $postData['mihpayid'];
    $amount = $postData['amount'];
    
    // Update your database with the successful payment
    // (implementation depends on your database and business logic)
    updateOrderStatus($txnId, 'PAID', $payuId);
    
    // Show success message to user
    echo "<h2>Payment Successful!</h2>";
    echo "<p>Transaction ID: " . htmlspecialchars($txnId) . "</p>";
    echo "<p>PayU Reference: " . htmlspecialchars($payuId) . "</p>";
} else {
    // Payment failed
    $txnId = $postData['txnid'];
    $errorMessage = isset($postData['error_Message']) ? $postData['error_Message'] : 'Unknown error';
    
    // Update your database with the failed payment
    updateOrderStatus($txnId, 'FAILED', null, $errorMessage);
    
    // Show failure message to user
    echo "<h2>Payment Failed</h2>";
    echo "<p>Transaction ID: " . htmlspecialchars($txnId) . "</p>";
    echo "<p>Error: " . htmlspecialchars($errorMessage) . "</p>";
}

// Helper function to update order status (implement according to your database)
function updateOrderStatus($txnId, $status, $payuId = null, $errorMessage = null) {
    // Database update logic here
    // ...
}
?>

```
```javascript
document.addEventListener("click", function (event) {
  // Checking if the button was clicked
  if (!event.target.matches("#button")) return;

  fetch("<https://https://test.payu.in/_payment>")
    .then((response) => response.json())
    .then((data) => console.log(data));
});
```
```java
package com.example.payuhandler;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Enumeration;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Logger;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/payment/callback")
public class PayUResponseHandler extends HttpServlet {
    private static final long serialVersionUID = 1L;
    private static final Logger LOGGER = Logger.getLogger(PayUResponseHandler.class.getName());
    
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        
        // Extract all POST parameters from PayU
        Map<String, String> params = extractRequestParams(request);
        
        // Log the response for debugging (in production, ensure sensitive data is protected)
        LOGGER.info("PayU Response: " + params);
        
        try {
            // Get your salt from a secure location (environment variable, config file, etc.)
            String salt = System.getenv("PAYU_SALT");
            if (salt == null || salt.isEmpty()) {
                LOGGER.severe("PayU salt not configured");
                response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Payment configuration error");
                return;
            }
            
            // Verify the hash in the response
            boolean isValid = verifyPayuResponseHash(params, salt);
            
            if (!isValid) {
                // Hash validation failed, potential security issue
                LOGGER.warning("PayU response hash validation failed: " + params.get("txnid"));
                response.sendRedirect(request.getContextPath() + "/payment-error.jsp?error=hash_validation_failed");
                return;
            }
            
            // Process based on payment status
            String status = params.get("status");
            String txnId = params.get("txnid");
            
            if ("success".equals(status)) {
                // Payment successful
                String payuId = params.get("mihpayid");
                String amount = params.get("amount");
                
                // Update your database with successful payment
                updateOrderStatus(txnId, "PAID", payuId, null);
                
                // Redirect to success page
                response.sendRedirect(request.getContextPath() + 
                        "/payment-success.jsp?txnid=" + txnId + "&payuid=" + payuId);
            } else {
                // Payment failed
                String errorMessage = params.get("error_Message");
                if (errorMessage == null) {
                    errorMessage = "Unknown error";
                }
                
                // Update your database with failed payment
                updateOrderStatus(txnId, "FAILED", null, errorMessage);
                
                // Redirect to failure page
                response.sendRedirect(request.getContextPath() + 
                        "/payment-failure.jsp?txnid=" + txnId + "&error=" + errorMessage);
            }
        } catch (Exception e) {
            LOGGER.severe("Error processing PayU response: " + e.getMessage());
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Error processing payment response");
        }
    }
    
    /**
     * Extracts all parameters from the request
     */
    private Map<String, String> extractRequestParams(HttpServletRequest request) {
        Map<String, String> params = new HashMap<>();
        Enumeration<String> paramNames = request.getParameterNames();
        
        while (paramNames.hasMoreElements()) {
            String paramName = paramNames.nextElement();
            String paramValue = request.getParameter(paramName);
            params.put(paramName, paramValue);
        }
        
        return params;
    }
    
    /**
     * Verifies the response hash from PayU
     */
    private boolean verifyPayuResponseHash(Map<String, String> params, String salt) {
        // Check if all required parameters exist
        if (!params.containsKey("status") || !params.containsKey("txnid") || 
            !params.containsKey("amount") || !params.containsKey("productinfo") || 
            !params.containsKey("firstname") || !params.containsKey("email") || 
            !params.containsKey("key") || !params.containsKey("hash")) {
            return false;
        }
        
        // Extract the hash received from PayU
        String receivedHash = params.get("hash");
        
        // Create hash string with exact parameter sequence
        // Reverse hash format for response validation:
        // sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
        
        StringBuilder hashBuilder = new StringBuilder();
        hashBuilder.append(salt)
                   .append('|')
                   .append(params.get("status"))
                   .append("||||||");
        
        // Add UDFs if present
        hashBuilder.append(params.getOrDefault("udf5", "")).append('|');
        hashBuilder.append(params.getOrDefault("udf4", "")).append('|');
        hashBuilder.append(params.getOrDefault("udf3", "")).append('|');
        hashBuilder.append(params.getOrDefault("udf2", "")).append('|');
        hashBuilder.append(params.getOrDefault("udf1", "")).append('|');
        
        // Add remaining fields
        hashBuilder.append(params.get("email")).append('|')
                   .append(params.get("firstname")).append('|')
                   .append(params.get("productinfo")).append('|')
                   .append(params.get("amount")).append('|')
                   .append(params.get("txnid")).append('|')
                   .append(params.get("key"));
        
        String hashString = hashBuilder.toString();
        
        try {
            // Calculate hash using SHA-512
            String calculatedHash = sha512(hashString).toLowerCase();
            
            // Compare the calculated hash with the hash received in the response
            return calculatedHash.equals(receivedHash.toLowerCase());
        } catch (NoSuchAlgorithmException e) {
            LOGGER.severe("Error calculating hash: " + e.getMessage());
            return false;
        }
    }
    
    /**
     * Calculates SHA-512 hash for a given input string
     */
    private String sha512(String input) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] hashBytes = md.digest(input.getBytes(StandardCharsets.UTF_8));
        
        StringBuilder sb = new StringBuilder();
        for (byte b : hashBytes) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }
    
    /**
     * Updates order status in the database (implement according to your system)
     */
    private void updateOrderStatus(String txnId, String status, String payuId, String errorMessage) {
        // Implementation depends on your database and business logic
        // For example:
        try {
            // DatabaseConnection db = DatabaseConnection.getInstance();
            // String query = "UPDATE orders SET status = ?, payu_id = ?, error_message = ? WHERE txn_id = ?";
            // PreparedStatement pstmt = db.prepareStatement(query);
            // pstmt.setString(1, status);
            // pstmt.setString(2, payuId);
            // pstmt.setString(3, errorMessage);
            // pstmt.setString(4, txnId);
            // pstmt.executeUpdate();
            
            LOGGER.info("Order status updated: " + txnId + " -> " + status);
        } catch (Exception e) {
            LOGGER.severe("Error updating order status: " + e.getMessage());
        }
    }
}

```

In the above code snippet:

* **Javascript**:

Here, the code snippet is for listening for all clicks. The **Fetch** API (provided by the browser) makes requests and fetches resources. Here, the `fetch()` and two instances of `.then()`.

```plaintext
fetch("<https://https://test.payu.in/_payment>")
.then((response) => response.json())
.then((data) => console.log(data));
```

* **Java**: The Java HTTP client is used to make an asynchronous HTTP request to the specified URL. Then, log the response data to the console.
* **Python**: A function `button_click` checks if the button was clicked and fetches the specified URL using the `requests` library. Then, decoding the JSON response using the `.json()` method and printing it using `print()`. The document.addEventListener line is specific to the browser environment and won’t work in Python. You’ll need to adjust that part of the code to fit your specific use case.
* **PHP**: The code checks if the button was clicked by checking if the HTTP request method is POST and if the ‘button’ parameter was sent in the request. Later, posting a cURL request to the specified URL and decoding the JSON response using `json_decode()`. Finally, the output of the decoded data using `var_dump()`.
