---
title: Integrating on your Website
excerpt: >-
  You will require to write some amount of code to collect the details from your
  customer and submit those details with PayU using a cURL with PayU Hosted
  Checkout integration.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This section provides some sample code blocks to submit the details you collected from your customer and they click **Pay Now**.

[block:tutorial-tile]
{
  "backgroundColor": "#018FF4",
  "emoji": "🦉",
  "id": "64ddc9dedc4121001ff5871c",
  "link": "https://payu-hosted-checkout.readme.io/v1.3.0/recipes/submitting-payment-request-on-your-website",
  "slug": "submitting-payment-request-on-your-website",
  "title": "Submitting Payment Request on your Website"
}
[/block]


```python
import hashlib
import urllib

# Set the API endpoint URL
apiEndpoint = "https://test.payu.in/_payment"

# Set the merchant key and salt
merchantKey = "your_merchant_key"
salt = "your_salt"

# Set the order details
amount = "100.00"
productInfo = "Test Product"
firstName = "John"
email = "john@example.com"
phone = "9999999999"
txnId = "TXN" + str(int(time.time()))
surl = "https://yourwebsite.com/payment-success"
furl = "https://yourwebsite.com/payment-failure"

# Create a map of parameters to pass to the PayU API
params = {
    "key": merchantKey,
    "txnid": txnId,
    "amount": amount,
    "productinfo": productInfo,
    "firstname": firstName,
    "email": email,
    "phone": phone,
    "surl": surl,
    "furl": furl,
}

# Generate the hash
hashValue = generateHash(params, salt)

# Add the hash to the parameter map
params["hash"] = hashValue

# Encode the parameters for use in the URL
encodedParams = urllib.parse.urlencode(params)

# Build the URL for the PayU API request
url = apiEndpoint + "?" + encodedParams

# Output the URL for the PayU API request
print(url)

def generateHash(params, salt):
    hashString = params["key"] + "|" + params["txnid"] + "|" + params["amount"] + "|" + params["productinfo"] + "|" +
```
```php
<?php

// Set the API endpoint URL
$apiEndpoint = "https://sandboxsecure.payu.in/_payment";

// Set the merchant key and salt
$merchantKey = "your_merchant_key";
$salt = "your_salt";

// Set the order details
$amount = "100.00";
$productInfo = "Test Product";
$firstName = "John";
$email = "john@example.com";
$phone = "9999999999";
$txnId = "TXN" . time();
$surl = "https://yourwebsite.com/payment-success";
$furl = "https://yourwebsite.com/payment-failure";

// Create a map of parameters to pass to the PayU API
$params = array(
    "key" => $merchantKey,
    "txnid" => $txnId,
    "amount" => $amount,
    "productinfo" => $productInfo,
    "firstname" => $firstName,
    "email" => $email,
    "phone" => $phone,
    "surl" => $surl,
    "furl" => $furl,
);

// Generate the hash
$hash = generateHash($params, $salt);

// Add the hash to the parameter map
$params["hash"] = $hash;

// Build the URL for the PayU API request
$url = $apiEndpoint . "?" . http_build_query($params);

// Output the URL for the PayU API request
echo $url;

function generateHash($params, $salt) {
    $hashString = $params["key"] . "|" . $params["txnid"] . "|" . $params["amount"] . "|" . $params["productinfo"] . "|" . $params["firstname"] . "|" . $params["email"] . "||||||" . $salt;

    // Generate the hash
    $hash = hash("sha512", $hashString);

    return $hash;
}
?>
```
```javascript
// Set the API endpoint URL
const apiEndpoint = "https://test.payu.in/_payment";

// Set the merchant key and salt
const merchantKey = "your_merchant_key";
const salt = "your_salt";

// Set the order details
const amount = "100.00";
const productInfo = "Test Product";
const firstName = "John";
const email = "john@example.com";
const phone = "9999999999";
const txnId = "TXN" + Date.now();
const surl = "https://yourwebsite.com/payment-success";
const furl = "https://yourwebsite.com/payment-failure";

// Create a map of parameters to pass to the PayU API
const params = {
  "key": merchantKey,
  "txnid": txnId,
  "amount": amount,
  "productinfo": productInfo,
  "firstname": firstName,
  "email": email,
  "phone": phone,
  "surl": surl,
  "furl": furl,
};

// Generate the hash
const hash = generateHash(params, salt);

// Add the hash to the parameter map
params["hash"] = hash;

// Encode the parameters for use in the URL
const encodedParams = new URLSearchParams(params).toString();

// Build the URL for the PayU API request
const url = apiEndpoint + "?" + encodedParams;

// Output the URL for the PayU API request
console.log(url);

function generateHash(params, salt) {
  let hashString = params["key"] + "|" + params["txnid"] + "|" + params["amount"] + "|" + params["productinfo"] + "|" + params["firstname"] + "|" + params["email"] + "||||||" + salt;

  // Generate the hash
  const hash = sha512(hashString);

  return hash;
}

function sha512(str) {
  return crypto.createHash("sha512").update(str).digest("hex");
}
```
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.HashMap;
import java.util.Map;

public class PayUHostedCheckout {

    public static void main(String[] args) throws Exception {

        // Set the API endpoint URL
        String apiEndpoint = "https://test.payu.in/_payment";

        // Set the merchant key and salt
        String merchantKey = "your_merchant_key";
        String salt = "your_salt";

        // Set the order details
        String amount = "100.00";
        String productInfo = "Test Product";
        String firstName = "John";
        String email = "john@example.com";
        String phone = "9999999999";
        String txnId = "TXN" + System.currentTimeMillis();
        String surl = "https://yourwebsite.com/payment-success";
        String furl = "https://yourwebsite.com/payment-failure";

        // Create a map of parameters to pass to the PayU API
        Map<String, String> params = new HashMap<>();
        params.put("key", merchantKey);
        params.put("txnid", txnId);
        params.put("amount", amount);
        params.put("productinfo", productInfo);
        params.put("firstname", firstName);
        params.put("email", email);
        params.put("phone", phone);
        params.put("surl", surl);
        params.put("furl", furl);

        // Generate the hash
        String hash = generateHash(params, salt);

        // Add the hash to the parameter map
        params.put("hash", hash);

        // Encode the parameters for use in the URL
        String encodedParams = encodeParams(params);

        // Build the URL for the PayU API request
        URL url = new URL(apiEndpoint + "?" + encodedParams);

        // Open a connection to the PayU API endpoint
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");

        // Read the response from the PayU API
        BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        String line;
        StringBuilder response = new StringBuilder();
        while ((line = reader.readLine()) != null) {
            response.append(line);
        }
        reader.close();

        // Output the response from the PayU API
        System.out.println(response.toString());
    }

    private static String generateHash(Map<String, String> params, String salt) throws Exception {
        StringBuilder hashString = new StringBuilder();
        hashString.append(params.get("key"));
        hashString.append("|");
        hashString.append(params.get("txnid"));
        hashString.append("|");
        hashString.append(params.get("amount"));
        hashString.append("|");
        hashString.append(params.get("productinfo"));
        hashString.append("|");
        hashString.append(params.get("firstname"));
        hashString.append("|");
        hashString.append(params.get("email"));
        hashString.append("|");
        hashString.append(params.get("udf1"));
        hashString.append("||||||");
        hashString.append(salt);

        // Generate the hash
        String hash = hashString.toString();
        String hashValue = hashCal("SHA-512", hash);

        return hashValue;
    }

    private static String encodeParams(Map<String, String> params) throws Exception {
        StringBuilder encodedParams = new StringBuilder();
        for (Map.Entry<String, String> entry : params.entrySet()) }
```

> 📘 Note: 
> 
> Javascript requires a crypto library to generate the hash. In this example, the crypto library that is built into Node.js is used, but if you’re running this code in a browser environment, you’ll need to use a different library.