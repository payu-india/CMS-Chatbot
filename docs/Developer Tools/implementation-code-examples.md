---
title: Implementation Code Examples
deprecated: false
hidden: false
metadata:
  robots: index
---
This section provides code examples for common PayU v2 implementation patterns across multiple programming languages. Use these examples as starting points for your integration.

## 🔧 Payment Initialization

<br />

```java
import java.util.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class PayUPaymentInitializer {
    private static final String MERCHANT_KEY = "your_merchant_key";
    private static final String SALT = "your_salt";
    private static final String BASE_URL = "https://secure.payu.in/_payment";
    
    public class PaymentRequest {
        public Map<String, String> createPaymentParams(String txnid, double amount, 
                                                       String productinfo, String firstname, 
                                                       String email, String phone, String surl, 
                                                       String furl) {
            Map<String, String> params = new HashMap<>();
            
            // Basic parameters
            params.put("key", MERCHANT_KEY);
            params.put("txnid", txnid);
            params.put("amount", String.valueOf(amount));
            params.put("productinfo", productinfo);
            params.put("firstname", firstname);
            params.put("email", email);
            params.put("phone", phone);
            params.put("surl", surl);
            params.put("furl", furl);
            
            // Generate hash
            String hashString = MERCHANT_KEY + "|" + txnid + "|" + amount + "|" + 
                               productinfo + "|" + firstname + "|" + email + "|||||||||||" + SALT;
            String hash = generateSHA512Hash(hashString);
            params.put("hash", hash);
            
            return params;
        }
        
        private String generateSHA512Hash(String input) {
            try {
                MessageDigest md = MessageDigest.getInstance("SHA-512");
                byte[] messageDigest = md.digest(input.getBytes());
                
                StringBuilder hexString = new StringBuilder();
                for (byte b : messageDigest) {
                    String hex = Integer.toHexString(0xff & b);
                    if (hex.length() == 1) {
                        hexString.append('0');
                    }
                    hexString.append(hex);
                }
                
                return hexString.toString();
            } catch (NoSuchAlgorithmException e) {
                throw new RuntimeException("SHA-512 algorithm not found", e);
            }
        }
    }
}
```

### PHP Example

```php
<?php
class PayUPaymentInitializer {
    private $merchantKey;
    private $salt;
    private $baseUrl;
    
    public function __construct($merchantKey, $salt) {
        $this->merchantKey = $merchantKey;
        $this->salt = $salt;
        $this->baseUrl = "https://secure.payu.in/_payment";
    }
    
    public function createPaymentParams($txnid, $amount, $productinfo, $firstname, 
                                      $email, $phone, $surl, $furl) {
        $params = array(
            'key' => $this->merchantKey,
            'txnid' => $txnid,
            'amount' => $amount,
            'productinfo' => $productinfo,
            'firstname' => $firstname,
            'email' => $email,
            'phone' => $phone,
            'surl' => $surl,
            'furl' => $furl
        );
        
        // Generate hash
        $hashString = $this->merchantKey . "|" . $txnid . "|" . $amount . "|" . 
                     $productinfo . "|" . $firstname . "|" . $email . "|||||||||||" . $this->salt;
        $params['hash'] = hash('sha512', $hashString);
        
        return $params;
    }
    
    public function generatePaymentForm($params) {
        $form = '<form action="' . $this->baseUrl . '" method="post" id="payuForm">';
        
        foreach ($params as $key => $value) {
            $form .= '<input type="hidden" name="' . $key . '" value="' . $value . '" />';
        }
        
        $form .= '<input type="submit" value="Pay Now" />';
        $form .= '</form>';
        
        return $form;
    }
}
?>
```

### JavaScript (Node.js) Example

```javascript
const crypto = require('crypto');
const axios = require('axios');

class PayUPaymentInitializer {
    constructor(merchantKey, salt) {
        this.merchantKey = merchantKey;
        this.salt = salt;
        this.baseUrl = 'https://secure.payu.in/_payment';
    }
    
    createPaymentParams(txnid, amount, productinfo, firstname, email, phone, surl, furl) {
        const params = {
            key: this.merchantKey,
            txnid: txnid,
            amount: amount,
            productinfo: productinfo,
            firstname: firstname,
            email: email,
            phone: phone,
            surl: surl,
            furl: furl
        };
        
        // Generate hash
        const hashString = `${this.merchantKey}|${txnid}|${amount}|${productinfo}|${firstname}|${email}|||||||||||${this.salt}`;
        params.hash = crypto.createHash('sha512').update(hashString).digest('hex');
        
        return params;
    }
    
    async initiatePayment(params) {
        try {
            const response = await axios.post(this.baseUrl, params, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            });
            
            return response.data;
        } catch (error) {
            throw new Error(`Payment initialization failed: ${error.message}`);
        }
    }
}

module.exports = PayUPaymentInitializer;
```

### Python Example

```python
import hashlib
import requests
from typing import Dict, Any

class PayUPaymentInitializer:
    def __init__(self, merchant_key: str, salt: str):
        self.merchant_key = merchant_key
        self.salt = salt
        self.base_url = "https://secure.payu.in/_payment"
    
    def create_payment_params(self, txnid: str, amount: float, productinfo: str, 
                            firstname: str, email: str, phone: str, 
                            surl: str, furl: str) -> Dict[str, Any]:
        params = {
            'key': self.merchant_key,
            'txnid': txnid,
            'amount': str(amount),
            'productinfo': productinfo,
            'firstname': firstname,
            'email': email,
            'phone': phone,
            'surl': surl,
            'furl': furl
        }
        
        # Generate hash
        hash_string = f"{self.merchant_key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|||||||||||{self.salt}"
        params['hash'] = hashlib.sha512(hash_string.encode()).hexdigest()
        
        return params
    
    def initiate_payment(self, params: Dict[str, Any]) -> requests.Response:
        try:
            response = requests.post(
                self.base_url,
                data=params,
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            raise Exception(f"Payment initialization failed: {str(e)}")
```

## 🔍 Payment Status Verification

### Java Example

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import org.json.JSONObject;

public class PaymentStatusVerifier {
    private static final String VERIFY_URL = "https://info.payu.in/merchant/postservice?form=2";
    private String merchantKey;
    private String salt;
    
    public PaymentStatusVerifier(String merchantKey, String salt) {
        this.merchantKey = merchantKey;
        this.salt = salt;
    }
    
    public JSONObject verifyPayment(String txnid) {
        try {
            String command = "verify_payment";
            String var1 = txnid;
            String hashString = merchantKey + "|" + command + "|" + var1 + "|" + salt;
            String hash = generateSHA512Hash(hashString);
            
            String postData = "key=" + merchantKey + 
                            "&command=" + command + 
                            "&var1=" + var1 + 
                            "&hash=" + hash;
            
            URL url = new URL(VERIFY_URL);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            conn.setDoOutput(true);
            
            conn.getOutputStream().write(postData.getBytes());
            
            BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            StringBuilder response = new StringBuilder();
            String line;
            
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
            
            return new JSONObject(response.toString());
            
        } catch (Exception e) {
            throw new RuntimeException("Payment verification failed", e);
        }
    }
}
```

### PHP Example

```php
<?php
class PaymentStatusVerifier {
    private $merchantKey;
    private $salt;
    private $verifyUrl;
    
    public function __construct($merchantKey, $salt) {
        $this->merchantKey = $merchantKey;
        $this->salt = $salt;
        $this->verifyUrl = "https://info.payu.in/merchant/postservice?form=2";
    }
    
    public function verifyPayment($txnid) {
        $command = "verify_payment";
        $var1 = $txnid;
        $hashString = $this->merchantKey . "|" . $command . "|" . $var1 . "|" . $this->salt;
        $hash = hash('sha512', $hashString);
        
        $postData = array(
            'key' => $this->merchantKey,
            'command' => $command,
            'var1' => $var1,
            'hash' => $hash
        );
        
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $this->verifyUrl);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        
        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        
        if ($httpCode == 200) {
            return json_decode($response, true);
        } else {
            throw new Exception("Payment verification failed with HTTP code: " . $httpCode);
        }
    }
}
?>
```

## 💰 Refund Processing

### JavaScript (Node.js) Example

```javascript
class PayURefundProcessor {
    constructor(merchantKey, salt) {
        this.merchantKey = merchantKey;
        this.salt = salt;
        this.refundUrl = 'https://info.payu.in/merchant/postservice?form=2';
    }
    
    async processRefund(payuId, refundAmount, reason = 'Customer Request') {
        const command = 'cancel_refund_transaction';
        const var1 = payuId;
        const var2 = refundAmount;
        const var3 = reason;
        
        const hashString = `${this.merchantKey}|${command}|${var1}|${this.salt}`;
        const hash = crypto.createHash('sha512').update(hashString).digest('hex');
        
        const postData = {
            key: this.merchantKey,
            command: command,
            var1: var1,
            var2: var2,
            var3: var3,
            hash: hash
        };
        
        try {
            const response = await axios.post(this.refundUrl, postData, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            });
            
            return response.data;
        } catch (error) {
            throw new Error(`Refund processing failed: ${error.message}`);
        }
    }
    
    async checkRefundStatus(refundId) {
        const command = 'check_action_status';
        const var1 = refundId;
        
        const hashString = `${this.merchantKey}|${command}|${var1}|${this.salt}`;
        const hash = crypto.createHash('sha512').update(hashString).digest('hex');
        
        const postData = {
            key: this.merchantKey,
            command: command,
            var1: var1,
            hash: hash
        };
        
        try {
            const response = await axios.post(this.refundUrl, postData, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            });
            
            return response.data;
        } catch (error) {
            throw new Error(`Refund status check failed: ${error.message}`);
        }
    }
}
```

## 🔔 Webhook Handler

### Express.js Example

```javascript
const express = require('express');
const crypto = require('crypto');
const bodyParser = require('body-parser');

class PayUWebhookHandler {
    constructor(merchantKey, salt) {
        this.merchantKey = merchantKey;
        this.salt = salt;
        this.app = express();
        this.setupMiddleware();
        this.setupRoutes();
    }
    
    setupMiddleware() {
        this.app.use(bodyParser.urlencoded({ extended: true }));
        this.app.use(bodyParser.json());
    }
    
    setupRoutes() {
        this.app.post('/payu/webhook', (req, res) => {
            try {
                if (this.verifyWebhookSignature(req.body)) {
                    this.processWebhook(req.body);
                    res.status(200).send('OK');
                } else {
                    res.status(400).send('Invalid signature');
                }
            } catch (error) {
                console.error('Webhook processing error:', error);
                res.status(500).send('Internal server error');
            }
        });
    }
    
    verifyWebhookSignature(payload) {
        const receivedHash = payload.hash;
        const computedHash = this.generateWebhookHash(payload);
        return receivedHash === computedHash;
    }
    
    generateWebhookHash(payload) {
        const hashString = `${this.salt}|${payload.status}||||||||||${payload.udf5}|${payload.udf4}|${payload.udf3}|${payload.udf2}|${payload.udf1}|${payload.email}|${payload.firstname}|${payload.productinfo}|${payload.amount}|${payload.txnid}|${this.merchantKey}`;
        return crypto.createHash('sha512').update(hashString).digest('hex');
    }
    
    processWebhook(payload) {
        console.log('Processing webhook for transaction:', payload.txnid);
        
        switch (payload.status) {
            case 'success':
                this.handleSuccessfulPayment(payload);
                break;
            case 'failure':
                this.handleFailedPayment(payload);
                break;
            case 'pending':
                this.handlePendingPayment(payload);
                break;
            default:
                console.log('Unknown payment status:', payload.status);
        }
    }
    
    handleSuccessfulPayment(payload) {
        // Update order status to paid
        console.log(`Payment successful for transaction: ${payload.txnid}`);
        // Add your business logic here
    }
    
    handleFailedPayment(payload) {
        // Update order status to failed
        console.log(`Payment failed for transaction: ${payload.txnid}`);
        // Add your business logic here
    }
    
    handlePendingPayment(payload) {
        // Keep order status as pending
        console.log(`Payment pending for transaction: ${payload.txnid}`);
        // Add your business logic here
    }
    
    start(port = 3000) {
        this.app.listen(port, () => {
            console.log(`PayU webhook handler listening on port ${port}`);
        });
    }
}

module.exports = PayUWebhookHandler;
```

## 📱 Mobile SDK Integration (React Native)

### React Native Example

```javascript
import React, { Component } from 'react';
import { View, Button, Alert } from 'react-native';
import PayUBizSdk from 'payu-non-seam-less-react';

class PayUPaymentScreen extends Component {
    constructor(props) {
        super(props);
        this.state = {
            isLoading: false
        };
    }
    
    initiatePayment = () => {
        this.setState({ isLoading: true });
        
        const paymentData = {
            key: 'your_merchant_key',
            txnid: this.generateTransactionId(),
            amount: '100.00',
            productinfo: 'Test Product',
            firstname: 'John',
            email: 'john@example.com',
            phone: '9876543210',
            surl: 'https://your-success-url.com',
            furl: 'https://your-failure-url.com',
            hash: this.generatePaymentHash()
        };
        
        PayUBizSdk.openCheckoutScreen({
            paymentData: paymentData,
            config: {
                showExitConfirmation: true,
                showBackButton: true
            }
        }).then((response) => {
            this.handlePaymentResponse(response);
        }).catch((error) => {
            this.handlePaymentError(error);
        }).finally(() => {
            this.setState({ isLoading: false });
        });
    }
    
    generateTransactionId = () => {
        return 'TXN_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    }
    
    generatePaymentHash = () => {
        // Implement hash generation logic
        // This should be done on your server for security
        return 'generated_hash_from_server';
    }
    
    handlePaymentResponse = (response) => {
        if (response.status === 'success') {
            Alert.alert('Success', 'Payment completed successfully');
            // Navigate to success screen or update order status
        } else {
            Alert.alert('Failed', 'Payment failed. Please try again.');
            // Handle failed payment
        }
    }
    
    handlePaymentError = (error) => {
        console.error('Payment error:', error);
        Alert.alert('Error', 'An error occurred during payment');
    }
    
    render() {
        return (
            <View style={{ flex: 1, justifyContent: 'center', padding: 20 }}>
                <Button
                    title={this.state.isLoading ? "Processing..." : "Pay Now"}
                    onPress={this.initiatePayment}
                    disabled={this.state.isLoading}
                />
            </View>
        );
    }
}

export default PayUPaymentScreen;
```

## 🔒 Error Handling Patterns

### Comprehensive Error Handler (JavaScript)

```javascript
class PayUErrorHandler {
    static ERROR_CODES = {
        E000: 'Unknown error occurred',
        E001: 'Mandatory parameter missing',
        E002: 'Invalid amount',
        E003: 'Invalid transaction ID',
        E004: 'Hash verification failed',
        E005: 'Merchant authentication failed',
        E006: 'Transaction already processed',
        E007: 'Payment method not available',
        E008: 'Card declined by bank',
        E009: 'Transaction timeout',
        E010: 'Network connectivity issue'
    };
    
    static handlePaymentError(error) {
        if (error.response) {
            // Server responded with error status
            const errorCode = error.response.data.error_code || 'E000';
            const errorMessage = this.ERROR_CODES[errorCode] || 'Unknown error occurred';
            
            return {
                type: 'server_error',
                code: errorCode,
                message: errorMessage,
                details: error.response.data
            };
        } else if (error.request) {
            // Network error
            return {
                type: 'network_error',
                code: 'E010',
                message: 'Network connectivity issue',
                details: 'Please check your internet connection and try again'
            };
        } else {
            // Client-side error
            return {
                type: 'client_error',
                code: 'E000',
                message: 'Unknown error occurred',
                details: error.message
            };
        }
    }
    
    static getRetryStrategy(errorType) {
        switch (errorType) {
            case 'network_error':
                return {
                    retry: true,
                    maxRetries: 3,
                    delay: 2000 // 2 seconds
                };
            case 'server_error':
                return {
                    retry: false,
                    userAction: 'contact_support'
                };
            case 'client_error':
                return {
                    retry: false,
                    userAction: 'fix_input'
                };
            default:
                return {
                    retry: false,
                    userAction: 'contact_support'
                };
        }
    }
}

// Usage example
try {
    const paymentResponse = await payuService.initiatePayment(paymentData);
    // Process successful payment
} catch (error) {
    const errorInfo = PayUErrorHandler.handlePaymentError(error);
    const retryStrategy = PayUErrorHandler.getRetryStrategy(errorInfo.type);
    
    if (retryStrategy.retry) {
        // Implement retry logic
        setTimeout(() => {
            retryPayment(paymentData);
        }, retryStrategy.delay);
    } else {
        // Show error to user and suggest action
        showErrorToUser(errorInfo.message, retryStrategy.userAction);
    }
}
```

## 🔄 Retry Mechanism Implementation

### JavaScript Example with Exponential Backoff

```javascript
class PayURetryHandler {
    constructor(maxRetries = 3, baseDelay = 1000) {
        this.maxRetries = maxRetries;
        this.baseDelay = baseDelay;
    }
    
    async executeWithRetry(operation, ...args) {
        let lastError;
        
        for (let attempt = 0; attempt <= this.maxRetries; attempt++) {
            try {
                return await operation(...args);
            } catch (error) {
                lastError = error;
                
                if (attempt === this.maxRetries) {
                    throw new Error(`Operation failed after ${this.maxRetries + 1} attempts: ${error.message}`);
                }
                
                if (!this.shouldRetry(error)) {
                    throw error;
                }
                
                const delay = this.calculateDelay(attempt);
                console.log(`Attempt ${attempt + 1} failed, retrying in ${delay}ms...`);
                await this.sleep(delay);
            }
        }
    }
    
    shouldRetry(error) {
        // Retry only for network errors and specific server errors
        const retryableErrors = ['ECONNRESET', 'ETIMEDOUT', 'ENOTFOUND'];
        
        if (error.code && retryableErrors.includes(error.code)) {
            return true;
        }
        
        if (error.response && error.response.status >= 500) {
            return true;
        }
        
        return false;
    }
    
    calculateDelay(attempt) {
        // Exponential backoff with jitter
        const exponentialDelay = this.baseDelay * Math.pow(2, attempt);
        const jitter = Math.random() * 0.1 * exponentialDelay;
        return Math.floor(exponentialDelay + jitter);
    }
    
    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// Usage example
const retryHandler = new PayURetryHandler(3, 1000);

try {
    const result = await retryHandler.executeWithRetry(
        payuService.verifyPayment.bind(payuService),
        transactionId
    );
    console.log('Payment verification successful:', result);
} catch (error) {
    console.error('Payment verification failed after all retries:', error);
}
```

## 📊 Logging and Monitoring

### Structured Logging Example

```javascript
const winston = require('winston');

class PayULogger {
    constructor() {
        this.logger = winston.createLogger({
            level: 'info',
            format: winston.format.combine(
                winston.format.timestamp(),
                winston.format.errors({ stack: true }),
                winston.format.json()
            ),
            defaultMeta: { service: 'payu-integration' },
            transports: [
                new winston.transports.File({ filename: 'payu-error.log', level: 'error' }),
                new winston.transports.File({ filename: 'payu-combined.log' })
            ]
        });
        
        if (process.env.NODE_ENV !== 'production') {
            this.logger.add(new winston.transports.Console({
                format: winston.format.simple()
            }));
        }
    }
    
    logPaymentInitiation(txnid, amount, customerEmail) {
        this.logger.info('Payment initiated', {
            event: 'payment_initiated',
            txnid: txnid,
            amount: amount,
            customer_email: customerEmail,
            timestamp: new Date().toISOString()
        });
    }
    
    logPaymentSuccess(txnid, payuId, amount) {
        this.logger.info('Payment successful', {
            event: 'payment_success',
            txnid: txnid,
            payu_id: payuId,
            amount: amount,
            timestamp: new Date().toISOString()
        });
    }
    
    logPaymentFailure(txnid, errorCode, errorMessage) {
        this.logger.error('Payment failed', {
            event: 'payment_failure',
            txnid: txnid,
            error_code: errorCode,
            error_message: errorMessage,
            timestamp: new Date().toISOString()
        });
    }
    
    logWebhookReceived(payload) {
        this.logger.info('Webhook received', {
            event: 'webhook_received',
            txnid: payload.txnid,
            status: payload.status,
            payu_id: payload.mihpayid,
            timestamp: new Date().toISOString()
        });
    }
    
    logApiCall(endpoint, requestData, responseData, duration) {
        this.logger.info('API call completed', {
            event: 'api_call',
            endpoint: endpoint,
            request_size: JSON.stringify(requestData).length,
            response_size: JSON.stringify(responseData).length,
            duration_ms: duration,
            timestamp: new Date().toISOString()
        });
    }
}

module.exports = PayULogger;
```

## 🧪 Testing Utilities

### Payment Testing Helper

```javascript
class PayUTestingHelper {
    static TEST_CARDS = {
        visa_success: {
            number: '4444444444444448',
            expiry: '12/25',
            cvv: '123',
            name: 'Test User'
        },
        mastercard_success: {
            number: '5555555555554444',
            expiry: '12/25',
            cvv: '123',
            name: 'Test User'
        },
        visa_failure: {
            number: '4444444444444457',
            expiry: '12/25',
            cvv: '123',
            name: 'Test User'
        }
    };
    
    static TEST_UPI_IDS = {
        success: 'success@payu',
        failure: 'failure@payu',
        pending: 'pending@payu'
    };
    
    static generateTestTransaction(scenario = 'success') {
        const baseData = {
            txnid: 'TEST_' + Date.now(),
            amount: '100.00',
            productinfo: 'Test Product',
            firstname: 'Test',
            lastname: 'User',
            email: 'test@example.com',
            phone: '9876543210'
        };
        
        switch (scenario) {
            case 'success':
                return { ...baseData, amount: '100.00' };
            case 'failure':
                return { ...baseData, amount: '1.00' };
            case 'timeout':
                return { ...baseData, amount: '10.00' };
            default:
                return baseData;
        }
    }
    
    static validateTestResponse(response, expectedStatus) {
        const validations = [];
        
        if (response.status !== expectedStatus) {
            validations.push(`Expected status ${expectedStatus}, got ${response.status}`);
        }
        
        if (!response.txnid) {
            validations.push('Transaction ID is missing');
        }
        
        if (!response.amount) {
            validations.push('Amount is missing');
        }
        
        return {
            isValid: validations.length === 0,
            errors: validations
        };
    }
    
    static async runTestSuite(paymentService) {
        const results = [];
        
        // Test successful payment
        try {
            const successTransaction = this.generateTestTransaction('success');
            const successResponse = await paymentService.initiatePayment(successTransaction);
            const successValidation = this.validateTestResponse(successResponse, 'success');
            
            results.push({
                test: 'successful_payment',
                passed: successValidation.isValid,
                errors: successValidation.errors
            });
        } catch (error) {
            results.push({
                test: 'successful_payment',
                passed: false,
                errors: [error.message]
            });
        }
        
        // Test failed payment
        try {
            const failureTransaction = this.generateTestTransaction('failure');
            const failureResponse = await paymentService.initiatePayment(failureTransaction);
            const failureValidation = this.validateTestResponse(failureResponse, 'failure');
            
            results.push({
                test: 'failed_payment',
                passed: failureValidation.isValid,
                errors: failureValidation.errors
            });
        } catch (error) {
            results.push({
                test: 'failed_payment',
                passed: false,
                errors: [error.message]
            });
        }
        
        return results;
    }
}

module.exports = PayUTestingHelper;
```

This comprehensive code examples document provides ready-to-use implementations for all major PayU v2 integration patterns across multiple programming languages and scenarios.