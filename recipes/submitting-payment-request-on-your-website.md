---
title: Submitting Payment Request on your Website
description: >-
  You will require to write some amount of code to collect the details from your
  customer and submit those details with PayU using a cURL with PayU Hosted
  Checkout integration.
hidden: false
recipe:
  color: '#018FF4'
  icon: 🦉
---
```javascript JavaScript
const apiEndpoint = "https://test.payu.in/_payment";

const merchantKey = "your_merchant_key";
const salt = "your_salt";

const amount = "100.00";
const productInfo = "Test Product";
const firstName = "John";
const email = "john@example.com";
const phone = "9999999999";
const txnId = "TXN" + Date.now();
const surl = "https://yourwebsite.com/payment-success";
const furl = "https://yourwebsite.com/payment-failure";

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

const hash = generateHash(params, salt);

params["hash"] = hash;

const encodedParams = new URLSearchParams(params).toString();

const url = apiEndpoint + "?" + encodedParams;

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

```java Java
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

        String apiEndpoint = "https://test.payu.in/_payment";

        String merchantKey = "your_merchant_key";
        String salt = "your_salt";

        String amount = "100.00";
        String productInfo = "Test Product";
        String firstName = "John";
        String email = "john@example.com";
        String phone = "9999999999";
        String txnId = "TXN" + System.currentTimeMillis();
        String surl = "https://yourwebsite.com/payment-success";
        String furl = "https://yourwebsite.com/payment-failure";

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

        String hash = generateHash(params, salt);

        params.put("hash", hash);

        String encodedParams = encodeParams(params);

        URL url = new URL(apiEndpoint + "?" + encodedParams);

        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");

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

        String hash = hashString.toString();
        String hashValue = hashCal("SHA-512", hash);

        return hashValue;
    }

    private static String encodeParams(Map<String, String> params) throws Exception {
        StringBuilder encodedParams = new StringBuilder();
        for (Map.Entry<String, String> entry : params.entrySet()) }
```

```json Response Example
{"success":true}
```

# Set the API endpoint URL

<!-- javascript@1 -->
<!-- java@14 -->

The line of code you provided in JavaScript defines a constant variable named apiEndpoint and assigns it a specific URL: "https://test.payu.in/_payment".

# Set the merchant key and salt

<!-- javascript@3-4 -->
<!-- java@16-17 -->

The lines of code you provided in JavaScript are defining two constant variables: merchantKey and salt. These variables appear to be related to security measures.

By using these variables (merchantKey and salt), you can follow secure practices when communicating with the payment gateway. The actual values of these variables should be kept confidential and not exposed in your JavaScript code or any other public-facing parts of your application. It's common to store sensitive information like these in environment variables or server-side configurations to prevent them from being easily accessed by potential attackers.

# Set the order details

<!-- javascript@6-13 -->
<!-- java@19-27 -->

These parameters are to construct requests that are sent to the PG APIs. The payment gateway processes the information, including verifying the transaction, collecting payment details, and communicating the result back to the merchant's website using the success or failure URLs. It's important to handle this integration securely and handle errors to ensure a smooth payment experience for your customers.

# Create a map of parameters to pass to the PayU API

<!-- javascript@15-25 -->
<!-- java@28-37 -->



# Generate the hash

<!-- javascript@27 -->
<!-- java@39 -->

The purpose of generating a hash in the context of a payment integration is to ensure the integrity and authenticity of the data being sent to the payment gateway. By including the hash in the request, the payment gateway can verify that the data has not been tampered with during transmission. This helps prevent unauthorized modifications to the payment information and enhances security. For more information refer to Hashing Request and Response section of Integration Guide.

# Add the hash to the parameter map

<!-- javascript@29 -->
<!-- java@41 -->



# Encode the parameters for use in the URL

<!-- javascript@31 -->
<!-- java@43 -->

It is for constructing a URL-encoded string from a set of parameters. This process is often used as a step before hashing data, especially when constructing a secure hash for purposes like verifying data integrity or generating digital signatures.

# Build the URL for the PayU API request

<!-- javascript@33 -->
<!-- java@45 -->

The line of code is for constructing a URL by combining two variables: apiEndpoint and encodedParams.

# Output the URL for the PayU API request

<!-- javascript@35 -->
<!-- java@47-48 -->



# Read the response from the PayU API

<!-- java@50-60 -->



# Generate the hash

<!-- javascript@37-48 -->
<!-- java@80-83 -->

