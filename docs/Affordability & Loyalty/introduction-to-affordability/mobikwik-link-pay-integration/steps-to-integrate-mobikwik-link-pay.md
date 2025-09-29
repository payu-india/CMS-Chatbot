---
title: Steps to Integrate - Mobikwik Link & Pay
deprecated: false
hidden: false
metadata:
  robots: index
---
PayU's Mobikwik Link & Pay integration is a streamlined one-click payment solution that enhances user experience by eliminating the need for repeated logins and multi-step wallet interactions. This integration guide provides step-by-step instructions for implementing Mobikwik Link & Pay payments on your platform.

## Step 1: Check User Balance and Link Status

Before initiating a payment, check if the user's Mobikwik wallet is linked and verify the available balance.

### Environment

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Environment</th>
      <th>Endpoint</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Test</td>
      <td><code>https://test.mobikwik.com/userbalance</code></td>
    </tr>
    <tr>
      <td>Production</td>
      <td><code>https://api.mobikwik.com/userbalance</code></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

<Accordion title="Sample request" icon="fa-table">
  <HTMLBlock>{`
                <table>
                  <thead>
                    <tr>
                      <th>Parameter</th>
                      <th>Description</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>mid<br/><code>mandatory</code></td>
                      <td>Merchant ID assigned by Mobikwik</td>
                    </tr>
                    <tr>
                      <td>cell<br/><code>mandatory</code></td>
                      <td>User's mobile number</td>
                    </tr>
                    <tr>
                      <td>msgcode<br/><code>mandatory</code></td>
                      <td>Message code for the request</td>
                    </tr>
                    <tr>
                      <td>checksum<br/><code>mandatory</code></td>
                      <td>HMAC SHA256 hash for security</td>
                    </tr>
                    <tr>
                      <td>aggregatedMerchantId<br/><code>optional</code></td>
                      <td>Aggregated merchant identifier</td>
                    </tr>
                  </tbody>
                </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://test.mobikwik.com/userbalance' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'mid=YOUR_MERCHANT_ID' \
  --data-urlencode 'cell=9560012582' \
  --data-urlencode 'msgcode=CHECK_BALANCE' \
  --data-urlencode 'checksum=GENERATED_CHECKSUM'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  **Success Response:**

  ```json
  {
    "status": "success",
    "statusCode": "S001",
    "statusDescription": "Balance Retrieved Successfully",
    "availableBalance": "5000.00",
    "customerLinked": "true",
    "walletStatus": "active"
  }
  ```

  **Wallet Not Linked Response:**

  ```json
  {
    "status": "failure",
    "statusCode": "ERR002",
    "statusDescription": "Wallet not linked",
    "customerLinked": "false"
  }
  ```

  If `customerLinked` is `false`, proceed with the first-time user flow. If `true`, proceed with the repeat user flow.
</Accordion>

***

## Step 2: Payment Initiation API

The Payment Initiation API enables merchants to seamlessly initiate payment requests for transactions using the Mobikwik Link & Pay flow.

### Environment

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Environment</th>
      <th>Endpoint</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Test</td>
      <td><code>https://test.payu.in/v2/payments</code></td>
    </tr>
    <tr>
      <td>Production</td>
      <td><code>https://api.payu.in/v2/payments</code></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

### Required Parameters

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>key<br/><code>mandatory</code></td>
      <td>Merchant key from PayU Dashboard</td>
    </tr>
    <tr>
      <td>transactionId<br/><code>mandatory</code></td>
      <td>Unique transaction identifier</td>
    </tr>
    <tr>
      <td>amount<br/><code>mandatory</code></td>
      <td>Transaction amount (decimal format)</td>
    </tr>
    <tr>
      <td>productInfo<br/><code>mandatory</code></td>
      <td>Product description for the transaction</td>
    </tr>
    <tr>
      <td>firstName<br/><code>mandatory</code></td>
      <td>Customer first name</td>
    </tr>
    <tr>
      <td>email<br/><code>mandatory</code></td>
      <td>Customer email address</td>
    </tr>
    <tr>
      <td>phone<br/><code>mandatory</code></td>
      <td>Customer mobile number</td>
    </tr>
    <tr>
      <td>surl<br/><code>mandatory</code></td>
      <td>Success URL where user will be redirected after successful payment</td>
    </tr>
    <tr>
      <td>furl<br/><code>mandatory</code></td>
      <td>Failure URL where user will be redirected after failed payment</td>
    </tr>
    <tr>
      <td>bankcode<br/><code>mandatory</code></td>
      <td>Must be "MOBIKWIK" for Mobikwik payments</td>
    </tr>
    <tr>
      <td>hash<br/><code>mandatory</code></td>
      <td>SHA512 hash for security and data integrity</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

### Sample Request

##### S2S Merchant Request

```curl
curl --location 'https://test.payu.in/v2/payments' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=YOUR_MERCHANT_KEY' \
--data-urlencode 'txnid=TXN123456789' \
--data-urlencode 'amount=1000.00' \
--data-urlencode 'productinfo=Mobikwik Payment' \
--data-urlencode 'firstname=John' \
--data-urlencode 'email=john@example.com' \
--data-urlencode 'phone=9560012582' \
--data-urlencode 'surl=https://yoursite.com/success' \
--data-urlencode 'furl=https://yoursite.com/failure' \
--data-urlencode 'bankcode=MOBIKWIK' \
--data-urlencode 'hash=GENERATED_HASH'
```
```javascript
const crypto = require('crypto');
const axios = require('axios');
const querystring = require('querystring');

class MobikwikLinkPayClient {
    constructor(merchantId, merchantKey, secretKey) {
        this.merchantId = merchantId;
        this.merchantKey = merchantKey;
        this.secretKey = secretKey;
        this.testBaseUrl = 'https://test.mobikwik.com';
        this.payuTestUrl = 'https://test.payu.in';
    }

    generateChecksum(data) {
        // Create string from data parameters
        const sortedKeys = Object.keys(data).sort();
        const paramString = sortedKeys.map(key => data[key]).join('|');
        
        return crypto
            .createHmac('sha256', this.secretKey)
            .update(paramString)
            .digest('hex');
    }

    generatePayuHash(data) {
        // PayU hash format: key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT
        const hashString = `${data.key}|${data.txnid}|${data.amount}|${data.productinfo}|${data.firstname}|${data.email}|||||||||||${this.secretKey}`;
        
        return crypto
            .createHash('sha512')
            .update(hashString)
            .digest('hex');
    }
}

// 1. Check User Balance and Link Status
async function checkUserBalance(client, mobileNumber) {
    const url = `${client.testBaseUrl}/userbalance`;
    
    const data = {
        mid: client.merchantId,
        cell: mobileNumber,
        msgcode: 'CHECK_BALANCE'
    };
    data.checksum = client.generateChecksum(data);
    
    const config = {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    };
    
    try {
        const response = await axios.post(url, querystring.stringify(data), config);
        return response.data;
    } catch (error) {
        console.error('Error checking user balance:', error.message);
        return null;
    }
}

// 2. Payment Initiation API
async function initiatePayment(client, transactionData) {
    const url = `${client.payuTestUrl}/v2/payments`;
    
    const data = {
        key: client.merchantKey,
        txnid: transactionData.txnid,
        amount: transactionData.amount,
        productinfo: transactionData.productinfo,
        firstname: transactionData.firstname,
        email: transactionData.email,
        phone: transactionData.phone,
        surl: transactionData.surl,
        furl: transactionData.furl,
        bankcode: 'MOBIKWIK'
    };
    data.hash = client.generatePayuHash(data);
    
    const config = {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    };
    
    try {
        const response = await axios.post(url, querystring.stringify(data), config);
        return response.data;
    } catch (error) {
        console.error('Error initiating payment:', error.message);
        return null;
    }
}

// 3. Submit OTP and Generate Token
async function generateToken(client, otpData) {
    const url = `${client.testBaseUrl}/tokengenerate`;
    
    const data = {
        mid: client.merchantId,
        cell: otpData.cell,
        msgcode: 'TOKEN_GENERATE',
        otp: otpData.otp,
        amount: otpData.amount,
        tokentype: 'WALLET_LINK'
    };
    data.checksum = client.generateChecksum(data);
    
    const config = {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    };
    
    try {
        const response = await axios.post(url, querystring.stringify(data), config);
        return response.data;
    } catch (error) {
        console.error('Error generating token:', error.message);
        return null;
    }
}

```
```java
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

public class MobikwikLinkPayClient {
    private final String merchantId;
    private final String merchantKey;
    private final String secretKey;
    private final String testBaseUrl = "https://test.mobikwik.com";
    private final String payuTestUrl = "https://test.payu.in";

    public MobikwikLinkPayClient(String merchantId, String merchantKey, String secretKey) {
        this.merchantId = merchantId;
        this.merchantKey = merchantKey;
        this.secretKey = secretKey;
    }

    /**
     * Generate HMAC SHA256 checksum for Mobikwik API requests
     */
    public String generateChecksum(Map<String, String> data) throws Exception {
        List<String> keys = new ArrayList<>(data.keySet());
        Collections.sort(keys);
        
        StringBuilder paramString = new StringBuilder();
        for (String key : keys) {
            if (paramString.length() > 0) {
                paramString.append("|");
            }
            paramString.append(data.get(key));
        }
        
        Mac sha256Hmac = Mac.getInstance("HmacSHA256");
        SecretKeySpec secretKeySpec = new SecretKeySpec(secretKey.getBytes(StandardCharsets.UTF_8), "HmacSHA256");
        sha256Hmac.init(secretKeySpec);
        
        byte[] hmacBytes = sha256Hmac.doFinal(paramString.toString().getBytes(StandardCharsets.UTF_8));
        return bytesToHex(hmacBytes);
    }
    
    /**
     * Generate SHA512 hash for PayU payment requests
     */
    public String generatePayuHash(Map<String, String> data) throws NoSuchAlgorithmException {
        // PayU hash format: key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT
        String hashString = data.get("key") + "|" + data.get("txnid") + "|" + data.get("amount") + "|" + 
                         data.get("productinfo") + "|" + data.get("firstname") + "|" + data.get("email") + 
                         "|||||||||||" + secretKey;
        
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] hashBytes = md.digest(hashString.getBytes(StandardCharsets.UTF_8));
        return bytesToHex(hashBytes);
    }
    
    /**
     * Convert bytes to hex string
     */
    private String bytesToHex(byte[] bytes) {
        StringBuilder hexString = new StringBuilder();
        for (byte b : bytes) {
            String hex = Integer.toHexString(0xff & b);
            if (hex.length() == 1) {
                hexString.append('0');
            }
            hexString.append(hex);
        }
        return hexString.toString();
    }
    
    /**
     * Send HTTP POST request with form data
     */
    private String sendPostRequest(String urlString, Map<String, String> formData) throws IOException {
        URL url = new URL(urlString);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");
        connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
        connection.setDoOutput(true);
        
        StringBuilder formDataString = new StringBuilder();
        for (Map.Entry<String, String> entry : formData.entrySet()) {
            if (formDataString.length() > 0) {
                formDataString.append("&");
            }
            formDataString.append(entry.getKey()).append("=").append(java.net.URLEncoder.encode(entry.getValue(), "UTF-8"));
        }
        
        try (DataOutputStream outputStream = new DataOutputStream(connection.getOutputStream())) {
            outputStream.writeBytes(formDataString.toString());
            outputStream.flush();
        }
        
        int responseCode = connection.getResponseCode();
        StringBuilder response = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(
                responseCode >= 400 ? connection.getErrorStream() : connection.getInputStream()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
        }
        
        connection.disconnect();
        return response.toString();
    }
    
    /**
     * Check user balance and link status
     */
    public String checkUserBalance(String mobileNumber) {
        try {
            String url = testBaseUrl + "/userbalance";
            Map<String, String> data = new HashMap<>();
            data.put("mid", merchantId);
            data.put("cell", mobileNumber);
            data.put("msgcode", "CHECK_BALANCE");
            data.put("checksum", generateChecksum(data));
            
            return sendPostRequest(url, data);
        } catch (Exception e) {
            System.err.println("Error checking user balance: " + e.getMessage());
            e.printStackTrace();
            return null;
        }
    }
    
    /**
     * Initiate payment through PayU
     */
    public String initiatePayment(Map<String, String> transactionData) {
        try {
            String url = payuTestUrl + "/v2/payments";
            Map<String, String> data = new HashMap<>();
            data.put("key", merchantKey);
            data.put("txnid", transactionData.get("txnid"));
            data.put("amount", transactionData.get("amount"));
            data.put("productinfo", transactionData.get("productinfo"));
            data.put("firstname", transactionData.get("firstname"));
            data.put("email", transactionData.get("email"));
            data.put("phone", transactionData.get("phone"));
            data.put("surl", transactionData.get("surl"));
            data.put("furl", transactionData.get("furl"));
            data.put("bankcode", "MOBIKWIK");
            data.put("hash", generatePayuHash(data));
            
            return sendPostRequest(url, data);
        } catch (Exception e) {
            System.err.println("Error initiating payment: " + e.getMessage());
            e.printStackTrace();
            return null;
        }
    }
    
    /**
     * Submit OTP and generate token
     */
    public String generateToken(Map<String, String> otpData) {
        try {
            String url = testBaseUrl + "/tokengenerate";
            Map<String, String> data = new HashMap<>();
            data.put("mid", merchantId);
            data.put("cell", otpData.get("cell"));
            data.put("msgcode", "TOKEN_GENERATE");
            data.put("otp", otpData.get("otp"));
            data.put("amount", otpData.get("amount"));
            data.put("tokentype", "WALLET_LINK");
            data.put("checksum", generateChecksum(data));
            
            return sendPostRequest(url, data);
        } catch (Exception e) {
            System.err.println("Error generating token: " + e.getMessage());
            e.printStackTrace();
            return null;
        }
    }
}

```
```python
import requests
import urllib.parse
import hashlib
import hmac
import json

class MobikwikLinkPayClient:
    def __init__(self, merchant_id, merchant_key, secret_key):
        self.merchant_id = merchant_id
        self.merchant_key = merchant_key
        self.secret_key = secret_key
        self.test_base_url = "https://test.mobikwik.com"
        self.payu_test_url = "https://test.payu.in"
    
    def generate_checksum(self, data):
        """Generate HMAC SHA256 checksum"""
        # Create string from data parameters
        param_string = '|'.join([str(data[key]) for key in sorted(data.keys())])
        return hmac.new(
            self.secret_key.encode('utf-8'), 
            param_string.encode('utf-8'), 
            hashlib.sha256
        ).hexdigest()
    
    def generate_payu_hash(self, data):
        """Generate SHA512 hash for PayU"""
        # PayU hash format: key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT
        hash_string = f"{data['key']}|{data['txnid']}|{data['amount']}|{data['productinfo']}|{data['firstname']}|{data['email']}|||||||||||{self.secret_key}"
        return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()

# 1. Check User Balance and Link Status
def check_user_balance(client, mobile_number):
    url = f"{client.test_base_url}/userbalance"
    
    data = {
        'mid': client.merchant_id,
        'cell': mobile_number,
        'msgcode': 'CHECK_BALANCE'
    }
    data['checksum'] = client.generate_checksum(data)
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    try:
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error checking user balance: {e}")
        return None

# 2. Payment Initiation API
def initiate_payment(client, transaction_data):
    url = f"{client.payu_test_url}/v2/payments"
    
    data = {
        'key': client.merchant_key,
        'txnid': transaction_data['txnid'],
        'amount': transaction_data['amount'],
        'productinfo': transaction_data['productinfo'],
        'firstname': transaction_data['firstname'],
        'email': transaction_data['email'],
        'phone': transaction_data['phone'],
        'surl': transaction_data['surl'],
        'furl': transaction_data['furl'],
        'bankcode': 'MOBIKWIK'
    }
    data['hash'] = client.generate_payu_hash(data)
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    try:
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error initiating payment: {e}")
        return None

# 3. Submit OTP and Generate Token
def generate_token(client, otp_data):
    url = f"{client.test_base_url}/tokengenerate"
    
    data = {
        'mid': client.merchant_id,
        'cell': otp_data['cell'],
        'msgcode': 'TOKEN_GENERATE',
        'otp': otp_data['otp'],
        'amount': otp_data['amount'],
        'tokentype': 'WALLET_LINK'
    }
    data['checksum'] = client.generate_checksum(data)
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    try:
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error generating token: {e}")
        return None

```
```php
class MobikwikLinkPayClient {
    private $merchantId;
    private $merchantKey;
    private $secretKey;
    private $testBaseUrl = 'https://test.mobikwik.com';
    private $payuTestUrl = 'https://test.payu.in';
    
    public function __construct($merchantId, $merchantKey, $secretKey) {
        $this->merchantId = $merchantId;
        $this->merchantKey = $merchantKey;
        $this->secretKey = $secretKey;
    }
    
    /**
     * Generate HMAC SHA256 checksum for Mobikwik API requests
     */
    public function generateChecksum($data) {
        // Sort keys alphabetically
        ksort($data);
        
        // Create parameter string
        $paramString = implode('|', $data);
        
        // Generate HMAC SHA256 hash
        return hash_hmac('sha256', $paramString, $this->secretKey);
    }
    
    /**
     * Generate SHA512 hash for PayU payment requests
     */
    public function generatePayuHash($data) {
        // PayU hash format: key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT
        $hashString = $data['key'] . '|' . $data['txnid'] . '|' . $data['amount'] . '|' . 
                      $data['productinfo'] . '|' . $data['firstname'] . '|' . $data['email'] . 
                      '|||||||||||' . $this->secretKey;
        
        return hash('sha512', $hashString);
    }
    
    /**
     * Alternative POST method using cURL
     */
    private function curlPostRequest($url, $data) {
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false); // For testing only, enable in production
        
        $response = curl_exec($ch);
        $error = curl_error($ch);
        
        if ($error) {
            error_log('cURL Error: ' . $error);
            return null;
        }
        
        curl_close($ch);
        return $response;
    }
    
    /**
     * Check user balance and link status
     */
    public function checkUserBalance($mobileNumber) {
        $url = $this->testBaseUrl . '/userbalance';
        
        $data = [
            'mid' => $this->merchantId,
            'cell' => $mobileNumber,
            'msgcode' => 'CHECK_BALANCE'
        ];
        $data['checksum'] = $this->generateChecksum($data);
        
        return $this->curlPostRequest($url, $data);
    }
    
    /**
     * Initiate payment through PayU
     */
    public function initiatePayment($transactionData) {
        $url = $this->payuTestUrl . '/v2/payments';
        
        $data = [
            'key' => $this->merchantKey,
            'txnid' => $transactionData['txnid'],
            'amount' => $transactionData['amount'],
            'productinfo' => $transactionData['productinfo'],
            'firstname' => $transactionData['firstname'],
            'email' => $transactionData['email'],
            'phone' => $transactionData['phone'],
            'surl' => $transactionData['surl'],
            'furl' => $transactionData['furl'],
            'bankcode' => 'MOBIKWIK'
        ];
        $data['hash'] = $this->generatePayuHash($data);
        
        return $this->curlPostRequest($url, $data);
    }
    
    /**
     * Submit OTP and generate token
     */
    public function generateToken($otpData) {
        $url = $this->testBaseUrl . '/tokengenerate';
        
        $data = [
            'mid' => $this->merchantId,
            'cell' => $otpData['cell'],
            'msgcode' => 'TOKEN_GENERATE',
            'otp' => $otpData['otp'],
            'amount' => $otpData['amount'],
            'tokentype' => 'WALLET_LINK'
        ];
        $data['checksum'] = $this->generateChecksum($data);
        
        return $this->curlPostRequest($url, $data);
    }
}

```

### Sample Response

There will be different scenarios and the response according to different scenarios:

* Success scenario
  ```json
  {
    "status": "success",
    "data": {
      "paymentId": "PAY_12345",
      "transactionId": "TXN123456789",
      "amount": "1000.00",
      "status": "pending",
      "redirectUrl": "https://mobikwik.payment.url",
      "message": "Payment initiated successfully"
    }
  }
  ```

* Failure scenario
  ```json
  {
    "status": "error",
    "errorCode": "INVALID_AMOUNT",
    "message": "Invalid amount provided",
    "data": null
  }
  ```

### Payment Flow Types

The Payment Initiation API automatically determines the appropriate flow based on user status:

#### For Linked Users (Auto-debit Flow)

* API directly processes payment using stored token
* Faster checkout experience
* Immediate payment confirmation

#### For Unlinked Users (Redirect Flow)

* User redirected to Mobikwik authentication
* OTP verification for wallet linking
* Token generation for future transactions

<Accordion title="Important Notes" icon="fa-info-circle">
  • The Payment Initiation API handles flow determination automatically\
  • Ensure `bankcode=MOBIKWIK` is included in all requests\
  • User identification via mobile number is mandatory\
  • Hash/Checksum generation is required for security\
  • Test thoroughly in sandbox before production deployment
</Accordion>

***

## Step 3: Process Payment Based on User Status

After initiating the payment via the Payment Initiation API, the system will process the payment based on whether the user's wallet is linked or not.

## Step 4: Submit OTP and Generate Token

After the user enters the OTP, submit it to generate a wallet token for future transactions.

### Environment

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Environment</th>
      <th>Endpoint</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Test</td>
      <td><code>https://test.mobikwik.com/tokengenerate</code></td>
    </tr>
    <tr>
      <td>Production</td>
      <td><code>https://api.mobikwik.com/tokengenerate</code></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

<Accordion title="Request parameters" icon="fa-info-table">
  <HTMLBlock>{`
                <table>
                  <thead>
                    <tr>
                      <th>Parameter</th>
                      <th>Description</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>mid<br/><code>mandatory</code></td>
                      <td>Merchant ID</td>
                    </tr>
                    <tr>
                      <td>cell<br/><code>mandatory</code></td>
                      <td>User's mobile number</td>
                    </tr>
                    <tr>
                      <td>msgcode<br/><code>mandatory</code></td>
                      <td>Message code</td>
                    </tr>
                    <tr>
                      <td>otp<br/><code>mandatory</code></td>
                      <td>OTP entered by user</td>
                    </tr>
                    <tr>
                      <td>amount<br/><code>mandatory</code></td>
                      <td>Transaction amount</td>
                    </tr>
                    <tr>
                      <td>tokentype<br/><code>mandatory</code></td>
                      <td>Token type identifier</td>
                    </tr>
                    <tr>
                      <td>checksum<br/><code>mandatory</code></td>
                      <td>HMAC SHA256 hash</td>
                    </tr>
                  </tbody>
                </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://test.mobikwik.com/tokengenerate' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'mid=YOUR_MERCHANT_ID' \
  --data-urlencode 'cell=9560012582' \
  --data-urlencode 'msgcode=TOKEN_GENERATE' \
  --data-urlencode 'otp=123456' \
  --data-urlencode 'amount=1000.00' \
  --data-urlencode 'tokentype=WALLET_LINK' \
  --data-urlencode 'checksum=GENERATED_CHECKSUM'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  **Success Response:**

  ```json
  {
    "status": "success",
    "statusCode": "S003",
    "statusDescription": "Token Generated Successfully",
    "token": "TKN_ABC123XYZ789",
    "tokenExpiry": "365",
    "orderid": "ORD123456"
  }
  ```

  **Invalid OTP Response:**

  ```json
  {
    "status": "failure",
    "statusCode": "ERR003",
    "statusDescription": "Invalid OTP"
  }
  ```
</Accordion>

<Accordion title="Note" icon="fa-info-circle">
  Store the generated token securely for future transactions. Tokens are valid for 365 days by default.
</Accordion>

***

<Callout icon="📘" theme="info">
  ## References:

  * When the wallet balance is insufficient, use the **Add Money & Debit** API to allow users to load money and complete the transaction in a single flow. For more information, refer to [Add Money to Wallet And Debit API](ref:add-money-to-wallet-and-debit-api-mobikwik)
  * Verify the transaction status using the **Check Status** API. For more information, refer to [Check Status API](ref:check-status-api).
  * Process refunds using the standard PayU refund mechanism. Refunds are processed in the T+1 settlement cycle. For more information, refer to [Refund Transaction API](ref:refund_transaction_api).
  * If a token expires or becomes invalid, regenerate it using the Token Regenerate API. For more information, refer to Regenerate Token API.
</Callout>

## Error handling

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Error Code</th>
      <th>Description</th>
      <th>Recommended Action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ERR001</td>
      <td>Insufficient Balance</td>
      <td>Redirect to Add Money flow</td>
    </tr>
    <tr>
      <td>ERR002</td>
      <td>Wallet not linked</td>
      <td>Initiate first-time user flow</td>
    </tr>
    <tr>
      <td>ERR003</td>
      <td>Invalid OTP</td>
      <td>Allow OTP retry (max 3 attempts)</td>
    </tr>
    <tr>
      <td>ERR004</td>
      <td>Transaction Failed</td>
      <td>Show error message, offer retry</td>
    </tr>
    <tr>
      <td>ERR005</td>
      <td>Invalid Token</td>
      <td>Regenerate token</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>