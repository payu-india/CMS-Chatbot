---
title: Integrate Server-to-Server
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
This part of the document provides technical specifications and implementation code across multiple programming languages (Node.js, Java, Python, and PHP) for integrating PayU Server-to-Server payments.

***

## Environment

| Environment        | Base URL         | Transaction Initiation Endpoint | Post-Service Endpoint |
| :----------------- | :--------------- | :------------------------------ | :-------------------- |
| **Test / Sandbox** | `<redacted URL>` | `<redacted URL>`                | `<redacted URL>`      |
| **Production**     | `<redacted URL>` | `<redacted URL>`                | `<redacted URL>`      |

***

## SHA-512 Hash Generation Formula

Every transaction request sent to PayU requires a cryptographically generated SHA-512 hash computed on your secure backend server:

```text
hash = SHA-512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

> **Note:** Empty UDFs (`udf1` to `udf5`) must be represented as empty strings between pipes (`||||||`). Never expose your merchant `SALT` in client-side code or public repositories.

***

## Multi-Language Integration Implementations

### 1. Node.js Implementation

```javascript
const crypto = require('crypto');
const axios = require('axios');
const querystring = require('querystring');

const PAYU_CONFIG = {
  key: 'gtKFFx',
  salt: 'eCwWELxi',
  envUrl: '<redacted URL>' // Use <redacted URL> for Production
};

/**
 * Generate SHA-512 Hash for PayU Payment Request
 */
function generatePayUHash(params, salt) {
  const hashString = `${params.key}|${params.txnid}|${params.amount}|${params.productinfo}|${params.firstname}|${params.email}|${params.udf1 || ''}|${params.udf2 || ''}|${params.udf3 || ''}|${params.udf4 || ''}|${params.udf5 || ''}||||||${salt}`;
  return crypto.createHash('sha512').update(hashString).digest('hex');
}

/**
 * Verify Reverse Hash received from PayU Callback (surl/furl)
 */
function verifyReverseHash(responseParams, salt) {
  const hashString = `${salt}|${responseParams.status}||||||${responseParams.udf5 || ''}|${responseParams.udf4 || ''}|${responseParams.udf3 || ''}|${responseParams.udf2 || ''}|${responseParams.udf1 || ''}|${responseParams.email}|${responseParams.firstname}|${responseParams.productinfo}|${responseParams.amount}|${responseParams.txnid}|${responseParams.key}`;
  const calculatedHash = crypto.createHash('sha512').update(hashString).digest('hex');
  return calculatedHash.toLowerCase() === (responseParams.hash || '').toLowerCase();
}

/**
 * Execute Cards Classic S2S Payment
 */
async function initiateCardsS2S() {
  const payload = {
    key: PAYU_CONFIG.key,
    txnid: 'TXN_' + Date.now(),
    amount: '500.00',
    productinfo: 'Electronics Item',
    firstname: 'John',
    email: 'john.doe@example.com',
    phone: '9876543210',
    surl: '<redacted URL>',
    furl: '<redacted URL>',
    pg: 'CC',
    bankcode: 'CC',
    ccnum: '5123456789012346',
    ccexpmon: '05',
    ccexpyr: '2028',
    ccvv: '123',
    ccname: 'John Doe',
    txn_s2s_flow: 1, // Standard Cards S2S Flow
    authentication_flow: 'REDIRECT'
  };

  payload.hash = generatePayUHash(payload, PAYU_CONFIG.salt);

  try {
    const response = await axios.post(PAYU_CONFIG.envUrl, querystring.stringify(payload), {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    });

    console.log('PayU S2S Response:', response.data);
    // If 3DS challenge is required, response contains base64 acsTemplate
    if (response.data && response.data.result && response.data.result.acsTemplate) {
      const decodedHtml = Buffer.from(response.data.result.acsTemplate, 'base64').toString('utf-8');
      return { status: '3DS_CHALLENGE', html: decodedHtml };
    }
    return response.data;
  } catch (error) {
    console.error('Payment Initiation Error:', error.message);
    throw error;
  }
}

/**
 * Execute UPI Intent S2S Payment
 */
async function initiateUpiIntentS2S() {
  const payload = {
    key: PAYU_CONFIG.key,
    txnid: 'TXN_UPI_' + Date.now(),
    amount: '350.00',
    productinfo: 'Subscription Plan',
    firstname: 'Rahul',
    email: 'rahul@example.com',
    phone: '9876543210',
    surl: '<redacted URL>',
    furl: '<redacted URL>',
    pg: 'UPI',
    bankcode: 'INTENT',
    txn_s2s_flow: 4 // Required for UPI Intent
  };

  payload.hash = generatePayUHash(payload, PAYU_CONFIG.salt);

  const response = await axios.post(PAYU_CONFIG.envUrl, querystring.stringify(payload), {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
  });

  // Returns intent_uri, deep_links (gpay, phonepe, paytm), and qr_data
  return response.data;
}

module.exports = { generatePayUHash, verifyReverseHash, initiateCardsS2S, initiateUpiIntentS2S };
```

***

### 2. Java Implementation

```java
package com.payu.s2s;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.util.HashMap;
import java.util.Map;
import java.util.StringJoiner;

public class PayUS2SService {

    private static final String MERCHANT_KEY = "gtKFFx";
    private static final String MERCHANT_SALT = "eCwWELxi";
    private static final String ENDPOINT_URL = "<redacted URL>"; // Use <redacted URL> for Prod

    /**
     * Compute SHA-512 Hash
     */
    public static String calculateHash(String input) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] digest = md.digest(input.getBytes(StandardCharsets.UTF_8));
        StringBuilder sb = new StringBuilder();
        for (byte b : digest) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }

    /**
     * Generate Forward Request Hash
     */
    public static String generateRequestHash(Map<String, String> params, String salt) throws Exception {
        String hashSequence = String.format("%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s||||||%s",
                params.get("key"),
                params.get("txnid"),
                params.get("amount"),
                params.get("productinfo"),
                params.get("firstname"),
                params.get("email"),
                params.getOrDefault("udf1", ""),
                params.getOrDefault("udf2", ""),
                params.getOrDefault("udf3", ""),
                params.getOrDefault("udf4", ""),
                params.getOrDefault("udf5", ""),
                salt
        );
        return calculateHash(hashSequence);
    }

    /**
     * Verify Callback Reverse Hash
     */
    public static boolean verifyReverseHash(Map<String, String> responseParams, String salt) throws Exception {
        String reverseSequence = String.format("%s|%s||||||%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s",
                salt,
                responseParams.get("status"),
                responseParams.getOrDefault("udf5", ""),
                responseParams.getOrDefault("udf4", ""),
                responseParams.getOrDefault("udf3", ""),
                responseParams.getOrDefault("udf2", ""),
                responseParams.getOrDefault("udf1", ""),
                responseParams.get("email"),
                responseParams.get("firstname"),
                responseParams.get("productinfo"),
                responseParams.get("amount"),
                responseParams.get("txnid"),
                responseParams.get("key")
        );
        String expectedHash = calculateHash(reverseSequence);
        return expectedHash.equalsIgnoreCase(responseParams.get("hash"));
    }

    /**
     * Execute S2S HTTP POST Request
     */
    public static String sendPostRequest(String targetUrl, Map<String, String> params) throws Exception {
        URL url = new URL(targetUrl);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
        conn.setDoOutput(true);

        StringJoiner sj = new StringJoiner("&");
        for (Map.Entry<String, String> entry : params.entrySet()) {
            sj.add(URLEncoder.encode(entry.getKey(), "UTF-8") + "=" + URLEncoder.encode(entry.getValue(), "UTF-8"));
        }

        byte[] postData = sj.toString().getBytes(StandardCharsets.UTF_8);
        try (OutputStream os = conn.getOutputStream()) {
            os.write(postData);
        }

        StringBuilder response = new StringBuilder();
        try (BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
            String line;
            while ((line = in.readLine()) != null) {
                response.append(line);
            }
        }
        return response.toString();
    }

    public static void main(String[] args) {
        try {
            Map<String, String> params = new HashMap<>();
            params.put("key", MERCHANT_KEY);
            params.put("txnid", "TXN_JAVA_" + System.currentTimeMillis());
            params.put("amount", "1000.00");
            params.put("productinfo", "Flight Booking");
            params.put("firstname", "Ananya");
            params.put("email", "ananya@example.com");
            params.put("phone", "9876543210");
            params.put("surl", "<redacted URL>");
            params.put("furl", "<redacted URL>");
            params.put("pg", "CC");
            params.put("bankcode", "CC");
            params.put("ccnum", "5123456789012346");
            params.put("ccexpmon", "12");
            params.put("ccexpyr", "2029");
            params.put("ccvv", "456");
            params.put("ccname", "Ananya Sharma");
            params.put("txn_s2s_flow", "1");
            params.put("authentication_flow", "REDIRECT");

            // Calculate and append hash
            params.put("hash", generateRequestHash(params, MERCHANT_SALT));

            // Execute S2S Call
            String response = sendPostRequest(ENDPOINT_URL, params);
            System.out.println("PayU Response: " + response);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

***

### 3. Python Implementation

```python
import hashlib
import base64
import requests
import json
import time

PAYU_KEY = "gtKFFx"
PAYU_SALT = "eCwWELxi"
PAYU_URL = "<redacted URL>"  # Use <redacted URL> for Production

def generate_payu_hash(params: dict, salt: str) -> str:
    """
    Computes SHA-512 Hash for outbound PayU transaction request.
    """
    hash_sequence = (
        f"{params.get('key')}|{params.get('txnid')}|{params.get('amount')}|"
        f"{params.get('productinfo')}|{params.get('firstname')}|{params.get('email')}|"
        f"{params.get('udf1', '')}|{params.get('udf2', '')}|{params.get('udf3', '')}|"
        f"{params.get('udf4', '')}|{params.get('udf5', '')}||||||{salt}"
    )
    return hashlib.sha512(hash_sequence.encode('utf-8')).hexdigest()

def verify_reverse_hash(response_params: dict, salt: str) -> bool:
    """
    Validates Reverse Hash received from PayU on surl/furl or Webhook.
    """
    reverse_sequence = (
        f"{salt}|{response_params.get('status')}||||||"
        f"{response_params.get('udf5', '')}|{response_params.get('udf4', '')}|"
        f"{response_params.get('udf3', '')}|{response_params.get('udf2', '')}|"
        f"{response_params.get('udf1', '')}|{response_params.get('email')}|"
        f"{response_params.get('firstname')}|{response_params.get('productinfo')}|"
        f"{response_params.get('amount')}|{response_params.get('txnid')}|"
        f"{response_params.get('key')}"
    )
    calculated_hash = hashlib.sha512(reverse_sequence.encode('utf-8')).hexdigest()
    return calculated_hash.lower() == response_params.get('hash', '').lower()

def initiate_cards_s2s():
    """
    Executes Cards S2S Transaction (txn_s2s_flow=1)
    """
    payload = {
        "key": PAYU_KEY,
        "txnid": f"TXN_PY_{int(time.time())}",
        "amount": "750.00",
        "productinfo": "Consulting Services",
        "firstname": "Vikram",
        "email": "vikram@example.com",
        "phone": "9876543210",
        "surl": "<redacted URL>",
        "furl": "<redacted URL>",
        "pg": "CC",
        "bankcode": "CC",
        "ccnum": "5123456789012346",
        "ccexpmon": "07",
        "ccexpyr": "2028",
        "ccvv": "789",
        "ccname": "Vikram Rao",
        "txn_s2s_flow": "1",
        "authentication_flow": "REDIRECT"
    }

    # Attach generated hash
    payload["hash"] = generate_payu_hash(payload, PAYU_SALT)

    response = requests.post(
        PAYU_URL,
        data=payload,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    try:
        res_data = response.json()
        if "result" in res_data and "acsTemplate" in res_data["result"]:
            # Decode the base64 ACS template for rendering
            acs_html = base64.b64decode(res_data["result"]["acsTemplate"]).decode("utf-8")
            return {"status": "3DS_CHALLENGE", "html": acs_html}
        return res_data
    except Exception:
        return response.text

def initiate_upi_intent_s2s():
    """
    Executes UPI Intent Transaction (pg=UPI, bankcode=INTENT, txn_s2s_flow=4)
    """
    payload = {
        "key": PAYU_KEY,
        "txnid": f"TXN_UPI_{int(time.time())}",
        "amount": "299.00",
        "productinfo": "E-Book",
        "firstname": "Sneha",
        "email": "sneha@example.com",
        "phone": "9876543210",
        "surl": "<redacted URL>",
        "furl": "<redacted URL>",
        "pg": "UPI",
        "bankcode": "INTENT",
        "txn_s2s_flow": "4"
    }

    payload["hash"] = generate_payu_hash(payload, PAYU_SALT)

    response = requests.post(
        PAYU_URL,
        data=payload,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    return response.json()

if __name__ == "__main__":
    result = initiate_cards_s2s()
    print("Initiate Cards S2S Result:", result)
```

***

### 4. PHP Implementation

```php
<?php

$merchantKey  = "gtKFFx";
$merchantSalt = "eCwWELxi";
$payuUrl      = "<redacted URL>"; // Use <redacted URL> for Production

/**
 * Generate SHA-512 Hash for Outbound Request
 */
function getPayUHash($params, $salt) {
    $udf1 = isset($params['udf1']) ? $params['udf1'] : '';
    $udf2 = isset($params['udf2']) ? $params['udf2'] : '';
    $udf3 = isset($params['udf3']) ? $params['udf3'] : '';
    $udf4 = isset($params['udf4']) ? $params['udf4'] : '';
    $udf5 = isset($params['udf5']) ? $params['udf5'] : '';

    $hashSequence = $params['key'] . '|' .
                    $params['txnid'] . '|' .
                    $params['amount'] . '|' .
                    $params['productinfo'] . '|' .
                    $params['firstname'] . '|' .
                    $params['email'] . '|' .
                    $udf1 . '|' . $udf2 . '|' . $udf3 . '|' . $udf4 . '|' . $udf5 . '||||||' .
                    $salt;

    return hash('sha512', $hashSequence);
}

/**
 * Verify Reverse Hash on Callback
 */
function verifyPayUReverseHash($responseParams, $salt) {
    $udf1 = isset($responseParams['udf1']) ? $responseParams['udf1'] : '';
    $udf2 = isset($responseParams['udf2']) ? $responseParams['udf2'] : '';
    $udf3 = isset($responseParams['udf3']) ? $responseParams['udf3'] : '';
    $udf4 = isset($responseParams['udf4']) ? $responseParams['udf4'] : '';
    $udf5 = isset($responseParams['udf5']) ? $responseParams['udf5'] : '';

    $reverseSequence = $salt . '|' .
                       $responseParams['status'] . '||||||' .
                       $udf5 . '|' . $udf4 . '|' . $udf3 . '|' . $udf2 . '|' . $udf1 . '|' .
                       $responseParams['email'] . '|' .
                       $responseParams['firstname'] . '|' .
                       $responseParams['productinfo'] . '|' .
                       $responseParams['amount'] . '|' .
                       $responseParams['txnid'] . '|' .
                       $responseParams['key'];

    $calculatedHash = hash('sha512', $reverseSequence);
    return (strcasecmp($calculatedHash, $responseParams['hash']) === 0);
}

/**
 * Initiate Cards S2S Request
 */
function initiateCardsPayment($key, $salt, $url) {
    $postData = [
        'key'                 => $key,
        'txnid'               => 'TXN_PHP_' . time(),
        'amount'              => '1250.00',
        'productinfo'         => 'Apparel Purchase',
        'firstname'           => 'Rohan',
        'email'               => 'rohan@example.com',
        'phone'               => '9876543210',
        'surl'                => '<redacted URL>',
        'furl'                => '<redacted URL>',
        'pg'                  => 'CC',
        'bankcode'            => 'CC',
        'ccnum'               => '5123456789012346',
        'ccexpmon'            => '09',
        'ccexpyr'             => '2027',
        'ccvv'                => '321',
        'ccname'              => 'Rohan Verma',
        'txn_s2s_flow'        => '1',
        'authentication_flow' => 'REDIRECT'
    ];

    $postData['hash'] = getPayUHash($postData, $salt);

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/x-www-form-urlencoded']);

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    $decoded = json_decode($response, true);
    if (isset($decoded['result']['acsTemplate'])) {
        $acsHtml = base64_decode($decoded['result']['acsTemplate']);
        return ['status' => '3DS_CHALLENGE', 'html' => $acsHtml];
    }

    return $decoded ?: $response;
}

// Execute payment
$result = initiateCardsPayment($merchantKey, $merchantSalt, $payuUrl);
header('Content-Type: application/json');
echo json_encode($result);
?>
```

***

## Summary of Integration Parameters

| Payment Flow                         | `pg`    | `bankcode`   | `txn_s2s_flow` | Specific Required Parameters                                                     |
| :----------------------------------- | :------ | :----------- | :------------- | :------------------------------------------------------------------------------- |
| **Cards Classic (3DS 2.0)**          | `CC`    | `CC` or `DC` | `1`            | `ccnum`, `ccexpmon`, `ccexpyr`, `ccvv`, `ccname`, `authentication_flow=REDIRECT` |
| **Cards Decoupled (Auth & Capture)** | `CC`    | `CC` or `DC` | `4`            | `auth_only=1`, `authentication_flow=decoupled` or `REDIRECT`                     |
| **Cards Decoupled (Auth Only)**      | `CC`    | `CC` or `DC` | `4`            | `auth_only=2`, `authentication_flow=decoupled`                                   |
| **Cards Direct Authorization**       | `CC`    | `CC` or `DC` | `3`            | `threeDS2RequestData`, `authentication_info`                                     |
| **UPI Intent**                       | `UPI`   | `INTENT`     | `4`            | Returns `intent_uri`, `deep_links`, `qr_data`                                    |
| **UPI Collect**                      | `UPI`   | `UPI`        | `1`            | `vpa` (Customer VPA address)                                                     |
| **UPI Credit Card (UPICC)**          | `UPICC` | `INTCC`      | `4`            | Returns UPICC-compliant intent links                                             |
