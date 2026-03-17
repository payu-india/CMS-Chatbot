---
title: '[Internal Review] Authentication with PayU APIs'
deprecated: false
hidden: true
metadata:
  title: '[Internal Review]Authentication with PayU APIs'
  description: >-
    Learn how to securely authenticate and integrate with PayU India’s APIs.
    Explore topics such as merchant keys, salt, REST API authentication, hash
    parameters, and SHA512 encryption. Enhance your payment gateway integration
    with PayU’s robust security features.
  keywords:
    - PayU India API authentication
    - Merchant key and salt for PayU APIs
    - REST API authentication with PayU
    - Hash parameter in PayU API requests
    - SHA512 encryption for PayU API security
    - Reverse hashing using PayU node SDK
    - Generate hash for PayU API parameters
  robots: index
---
PayU India API uses merchant key and salt-based authentication. All requests must include a `hash` parameter computed using SHA-512 encryption and predefined formulas.

**Key Requirements:**

* Use SHA-512 for all hash calculations
* Follow exact parameter sequence as specified
* Include merchant SALT at the end of hash string
* Leave unused parameters empty but maintain pipe separators

***

## Payment APIs (_payment API)

### 1) General integration

##### Hash Formula

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

##### Sample Code

```php
<?php
function generatePaymentHash($params, $salt) {
    // Extract parameters or use empty string if not provided
    $key = $params['key'];
    $txnid = $params['txnid'];
    $amount = $params['amount'];
    $productinfo = $params['productinfo'];
    $firstname = $params['firstname'];
    $email = $params['email'];
    $udf1 = isset($params['udf1']) ? $params['udf1'] : '';
    $udf2 = isset($params['udf2']) ? $params['udf2'] : '';
    $udf3 = isset($params['udf3']) ? $params['udf3'] : '';
    $udf4 = isset($params['udf4']) ? $params['udf4'] : '';
    $udf5 = isset($params['udf5']) ? $params['udf5'] : '';
    
    // Construct hash string with exact parameter sequence
    $hashString = $key . '|' . $txnid . '|' . $amount . '|' . $productinfo . '|' . 
                  $firstname . '|' . $email . '|' . $udf1 . '|' . $udf2 . '|' . 
                  $udf3 . '|' . $udf4 . '|' . $udf5 . '||||||' . $salt;
    
    // Generate hash and convert to lowercase
    return strtolower(hash('sha512', $hashString));
}

// Example usage
$params = [
    'key' => 'yourKey',
    'txnid' => 'yourTxnId',
    'amount' => '100.00',
    'productinfo' => 'Test Product',
    'firstname' => 'John',
    'email' => 'john@example.com'
];
$salt = 'yourSalt';
$hash = generatePaymentHash($params, $salt);
?>
```
```java
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;

public class PaymentHashGenerator {

    public static String generatePaymentHash(Map<String, String> params, String salt) {
        // Extract parameters or use empty string if not provided
        String key = params.get("key");
        String txnid = params.get("txnid");
        String amount = params.get("amount");
        String productinfo = params.get("productinfo");
        String firstname = params.get("firstname");
        String email = params.get("email");
        String udf1 = params.getOrDefault("udf1", "");
        String udf2 = params.getOrDefault("udf2", "");
        String udf3 = params.getOrDefault("udf3", "");
        String udf4 = params.getOrDefault("udf4", "");
        String udf5 = params.getOrDefault("udf5", "");
        
        // Construct hash string with exact parameter sequence
        String hashString = key + "|" + txnid + "|" + amount + "|" + productinfo + "|" + 
                         firstname + "|" + email + "|" + udf1 + "|" + udf2 + "|" + 
                         udf3 + "|" + udf4 + "|" + udf5 + "||||||" + salt;
        
        return sha512(hashString);
    }

    private static String sha512(String input) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-512");
            byte[] hashBytes = md.digest(input.getBytes(StandardCharsets.UTF_8));
            StringBuilder sb = new StringBuilder();
            for (byte b : hashBytes) {
                sb.append(String.format("%02x", b));
            }
            return sb.toString().toLowerCase();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }
}
```
```csharp
using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Text;

public class PaymentHashGenerator
{
    public static string GeneratePaymentHash(Dictionary<string, string> parameters, string salt)
    {
        // Extract parameters or use empty string if not provided
        string key = parameters["key"];
        string txnid = parameters["txnid"];
        string amount = parameters["amount"];
        string productinfo = parameters["productinfo"];
        string firstname = parameters["firstname"];
        string email = parameters["email"];
        
        // Get UDF values if present, otherwise use empty string
        string udf1 = parameters.ContainsKey("udf1") ? parameters["udf1"] : "";
        string udf2 = parameters.ContainsKey("udf2") ? parameters["udf2"] : "";
        string udf3 = parameters.ContainsKey("udf3") ? parameters["udf3"] : "";
        string udf4 = parameters.ContainsKey("udf4") ? parameters["udf4"] : "";
        string udf5 = parameters.ContainsKey("udf5") ? parameters["udf5"] : "";
        
        // Construct hash string with exact parameter sequence
        string hashString = $"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{salt}";
        
        return Sha512(hashString);
    }

    private static string Sha512(string input)
    {
        using (SHA512 sha512 = SHA512.Create())
        {
            byte[] bytes = sha512.ComputeHash(Encoding.UTF8.GetBytes(input));
            StringBuilder sb = new StringBuilder();
            foreach (byte b in bytes)
            {
                sb.Append(b.ToString("x2"));
            }
            return sb.ToString().ToLower();
        }
    }
}
```
```python
import hashlib

def generate_payment_hash(params, salt):
    # Extract parameters or use empty string if not provided
    key = params['key']
    txnid = params['txnid']
    amount = params['amount']
    productinfo = params['productinfo']
    firstname = params['firstname']
    email = params['email']
    udf1 = params.get('udf1', '')
    udf2 = params.get('udf2', '')
    udf3 = params.get('udf3', '')
    udf4 = params.get('udf4', '')
    udf5 = params.get('udf5', '')
    
    # Construct hash string with exact parameter sequence
    hash_string = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{salt}"
    
    # Generate SHA-512 hash
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()

# Example usage
params = {
    'key': 'yourKey',
    'txnid': 'yourTxnId',
    'amount': '100.00',
    'productinfo': 'Test Product',
    'firstname': 'John',
    'email': 'john@example.com'
}
salt = 'yourSalt'
hash_value = generate_payment_hash(params, salt)
```
```javascript
const crypto = require('crypto');

function generatePaymentHash(params, salt) {
    // Extract parameters or use empty string if not provided
    const key = params.key;
    const txnid = params.txnid;
    const amount = params.amount;
    const productinfo = params.productinfo;
    const firstname = params.firstname;
    const email = params.email;
    const udf1 = params.udf1 || '';
    const udf2 = params.udf2 || '';
    const udf3 = params.udf3 || '';
    const udf4 = params.udf4 || '';
    const udf5 = params.udf5 || '';
    
    // Construct hash string with exact parameter sequence
    const hashString = `${key}|${txnid}|${amount}|${productinfo}|${firstname}|${email}|${udf1}|${udf2}|${udf3}|${udf4}|${udf5}||||||${salt}`;
    
    // Generate SHA-512 hash
    return crypto.createHash('sha512').update(hashString).digest('hex');
}

// Example usage
const params = {
    key: 'yourKey',
    txnid: 'yourTxnId',
    amount: '100.00',
    productinfo: 'Test Product',
    firstname: 'John',
    email: 'john@example.com'
};
const salt = 'yourSalt';
const hash = generatePaymentHash(params, salt);
```

***

### 2) Split Settlements

#### Hash Formula

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT|splitRequest)
```

#### Code Examples

```java
public static String generateSplitSettlementHash(Map<String, String> params, String salt, String splitRequest) {
    String key = params.get("key");
    String txnid = params.get("txnid");
    String amount = params.get("amount");
    String productinfo = params.get("productinfo");
    String firstname = params.get("firstname");
    String email = params.get("email");
    String udf1 = params.getOrDefault("udf1", "");
    String udf2 = params.getOrDefault("udf2", "");
    String udf3 = params.getOrDefault("udf3", "");
    String udf4 = params.getOrDefault("udf4", "");
    String udf5 = params.getOrDefault("udf5", "");
    
    String hashString = key + "|" + txnid + "|" + amount + "|" + productinfo + "|" + 
                     firstname + "|" + email + "|" + udf1 + "|" + udf2 + "|" + 
                     udf3 + "|" + udf4 + "|" + udf5 + "||||||" + salt + "|" + splitRequest;
    
    return sha512(hashString);
}
```
```php
<?php
function generateSplitSettlementHash($params, $salt, $splitRequest) {
    $key = $params['key'];
    $txnid = $params['txnid'];
    $amount = $params['amount'];
    $productinfo = $params['productinfo'];
    $firstname = $params['firstname'];
    $email = $params['email'];
    $udf1 = isset($params['udf1']) ? $params['udf1'] : '';
    $udf2 = isset($params['udf2']) ? $params['udf2'] : '';
    $udf3 = isset($params['udf3']) ? $params['udf3'] : '';
    $udf4 = isset($params['udf4']) ? $params['udf4'] : '';
    $udf5 = isset($params['udf5']) ? $params['udf5'] : '';
    
    $hashString = $key . '|' . $txnid . '|' . $amount . '|' . $productinfo . '|' . 
                  $firstname . '|' . $email . '|' . $udf1 . '|' . $udf2 . '|' . 
                  $udf3 . '|' . $udf4 . '|' . $udf5 . '||||||' . $salt . '|' . $splitRequest;
    
    return strtolower(hash('sha512', $hashString));
}
?>
```
```csharp
public static string GenerateSplitSettlementHash(Dictionary<string, string> parameters, string salt, string splitRequest)
{
    string key = parameters["key"];
    string txnid = parameters["txnid"];
    string amount = parameters["amount"];
    string productinfo = parameters["productinfo"];
    string firstname = parameters["firstname"];
    string email = parameters["email"];
    
    string udf1 = parameters.ContainsKey("udf1") ? parameters["udf1"] : "";
    string udf2 = parameters.ContainsKey("udf2") ? parameters["udf2"] : "";
    string udf3 = parameters.ContainsKey("udf3") ? parameters["udf3"] : "";
    string udf4 = parameters.ContainsKey("udf4") ? parameters["udf4"] : "";
    string udf5 = parameters.ContainsKey("udf5") ? parameters["udf5"] : "";
    
    string hashString = $"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{salt}|{splitRequest}";
    
    return Sha512(hashString);
}
```
```python
def generate_split_settlement_hash(params, salt, split_request):
    key = params['key']
    txnid = params['txnid']
    amount = params['amount']
    productinfo = params['productinfo']
    firstname = params['firstname']
    email = params['email']
    udf1 = params.get('udf1', '')
    udf2 = params.get('udf2', '')
    udf3 = params.get('udf3', '')
    udf4 = params.get('udf4', '')
    udf5 = params.get('udf5', '')
    
    hash_string = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{salt}|{split_request}"
    
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
```
```javascript
function generateSplitSettlementHash(params, salt, splitRequest) {
    const key = params.key;
    const txnid = params.txnid;
    const amount = params.amount;
    const productinfo = params.productinfo;
    const firstname = params.firstname;
    const email = params.email;
    const udf1 = params.udf1 || '';
    const udf2 = params.udf2 || '';
    const udf3 = params.udf3 || '';
    const udf4 = params.udf4 || '';
    const udf5 = params.udf5 || '';
    
    const hashString = `${key}|${txnid}|${amount}|${productinfo}|${firstname}|${email}|${udf1}|${udf2}|${udf3}|${udf4}|${udf5}||||||${salt}|${splitRequest}`;
    
    return crypto.createHash('sha512').update(hashString).digest('hex');
}
```

***

### 3) Offers Integration

#### Hash Formula

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|offer_key|offer_auto_apply|SALT
```

#### Code Examples

```php
<?php
function generateOffersHash($params, $salt) {
    $key = $params['key'];
    $txnid = $params['txnid'];
    $amount = $params['amount'];
    $productinfo = $params['productinfo'];
    $firstname = $params['firstname'];
    $email = $params['email'];
    
    // Handle udf1 to udf10
    $udf1 = isset($params['udf1']) ? $params['udf1'] : '';
    $udf2 = isset($params['udf2']) ? $params['udf2'] : '';
    $udf3 = isset($params['udf3']) ? $params['udf3'] : '';
    $udf4 = isset($params['udf4']) ? $params['udf4'] : '';
    $udf5 = isset($params['udf5']) ? $params['udf5'] : '';
    $udf6 = isset($params['udf6']) ? $params['udf6'] : '';
    $udf7 = isset($params['udf7']) ? $params['udf7'] : '';
    $udf8 = isset($params['udf8']) ? $params['udf8'] : '';
    $udf9 = isset($params['udf9']) ? $params['udf9'] : '';
    $udf10 = isset($params['udf10']) ? $params['udf10'] : '';
    
    $offer_key = isset($params['offer_key']) ? $params['offer_key'] : '';
    $offer_auto_apply = isset($params['offer_auto_apply']) ? $params['offer_auto_apply'] : '';
    
    $hashString = $key . '|' . $txnid . '|' . $amount . '|' . $productinfo . '|' . 
                  $firstname . '|' . $email . '|' . $udf1 . '|' . $udf2 . '|' . 
                  $udf3 . '|' . $udf4 . '|' . $udf5 . '|' . $udf6 . '|' . 
                  $udf7 . '|' . $udf8 . '|' . $udf9 . '|' . $udf10 . '|' . 
                  $offer_key . '|' . $offer_auto_apply . '|' . $salt;
    
    return strtolower(hash('sha512', $hashString));
}
?>
```
```java
public static String generateOffersHash(Map<String, String> params, String salt) {
    String key = params.get("key");
    String txnid = params.get("txnid");
    String amount = params.get("amount");
    String productinfo = params.get("productinfo");
    String firstname = params.get("firstname");
    String email = params.get("email");
    
    // Handle udf1 to udf10
    String udf1 = params.getOrDefault("udf1", "");
    String udf2 = params.getOrDefault("udf2", "");
    String udf3 = params.getOrDefault("udf3", "");
    String udf4 = params.getOrDefault("udf4", "");
    String udf5 = params.getOrDefault("udf5", "");
    String udf6 = params.getOrDefault("udf6", "");
    String udf7 = params.getOrDefault("udf7", "");
    String udf8 = params.getOrDefault("udf8", "");
    String udf9 = params.getOrDefault("udf9", "");
    String udf10 = params.getOrDefault("udf10", "");
    
    String offerKey = params.getOrDefault("offer_key", "");
    String offerAutoApply = params.getOrDefault("offer_auto_apply", "");
    
    String hashString = key + "|" + txnid + "|" + amount + "|" + productinfo + "|" + 
                     firstname + "|" + email + "|" + udf1 + "|" + udf2 + "|" + 
                     udf3 + "|" + udf4 + "|" + udf5 + "|" + udf6 + "|" + 
                     udf7 + "|" + udf8 + "|" + udf9 + "|" + udf10 + "|" + 
                     offerKey + "|" + offerAutoApply + "|" + salt;
    
    return sha512(hashString);
}
```
```csharp
public static string GenerateOffersHash(Dictionary<string, string> parameters, string salt)
{
    string key = parameters["key"];
    string txnid = parameters["txnid"];
    string amount = parameters["amount"];
    string productinfo = parameters["productinfo"];
    string firstname = parameters["firstname"];
    string email = parameters["email"];
    
    // Handle udf1 to udf10
    string udf1 = parameters.ContainsKey("udf1") ? parameters["udf1"] : "";
    string udf2 = parameters.ContainsKey("udf2") ? parameters["udf2"] : "";
    string udf3 = parameters.ContainsKey("udf3") ? parameters["udf3"] : "";
    string udf4 = parameters.ContainsKey("udf4") ? parameters["udf4"] : "";
    string udf5 = parameters.ContainsKey("udf5") ? parameters["udf5"] : "";
    string udf6 = parameters.ContainsKey("udf6") ? parameters["udf6"] : "";
    string udf7 = parameters.ContainsKey("udf7") ? parameters["udf7"] : "";
    string udf8 = parameters.ContainsKey("udf8") ? parameters["udf8"] : "";
    string udf9 = parameters.ContainsKey("udf9") ? parameters["udf9"] : "";
    string udf10 = parameters.ContainsKey("udf10") ? parameters["udf10"] : "";
    
    string offerKey = parameters.ContainsKey("offer_key") ? parameters["offer_key"] : "";
    string offerAutoApply = parameters.ContainsKey("offer_auto_apply") ? parameters["offer_auto_apply"] : "";
    
    string hashString = $"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}|{udf6}|{udf7}|{udf8}|{udf9}|{udf10}|{offerKey}|{offerAutoApply}|{salt}";
    
    return Sha512(hashString);
}
```
```python
def generate_offers_hash(params, salt):
    key = params['key']
    txnid = params['txnid']
    amount = params['amount']
    productinfo = params['productinfo']
    firstname = params['firstname']
    email = params['email']
    
    # Handle udf1 to udf10
    udf1 = params.get('udf1', '')
    udf2 = params.get('udf2', '')
    udf3 = params.get('udf3', '')
    udf4 = params.get('udf4', '')
    udf5 = params.get('udf5', '')
    udf6 = params.get('udf6', '')
    udf7 = params.get('udf7', '')
    udf8 = params.get('udf8', '')
    udf9 = params.get('udf9', '')
    udf10 = params.get('udf10', '')
    
    offer_key = params.get('offer_key', '')
    offer_auto_apply = params.get('offer_auto_apply', '')
    
    hash_string = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}|{udf6}|{udf7}|{udf8}|{udf9}|{udf10}|{offer_key}|{offer_auto_apply}|{salt}"
    
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
```
```javascript
function generateOffersHash(params, salt) {
    const key = params.key;
    const txnid = params.txnid;
    const amount = params.amount;
    const productinfo = params.productinfo;
    const firstname = params.firstname;
    const email = params.email;
    
    // Handle udf1 to udf10
    const udf1 = params.udf1 || '';
    const udf2 = params.udf2 || '';
    const udf3 = params.udf3 || '';
    const udf4 = params.udf4 || '';
    const udf5 = params.udf5 || '';
    const udf6 = params.udf6 || '';
    const udf7 = params.udf7 || '';
    const udf8 = params.udf8 || '';
    const udf9 = params.udf9 || '';
    const udf10 = params.udf10 || '';
    
    const offerKey = params.offer_key || '';
    const offerAutoApply = params.offer_auto_apply || '';
    
    const hashString = `${key}|${txnid}|${amount}|${productinfo}|${firstname}|${email}|${udf1}|${udf2}|${udf3}|${udf4}|${udf5}|${udf6}|${udf7}|${udf8}|${udf9}|${udf10}|${offerKey}|${offerAutoApply}|${salt}`;
    
    return crypto.createHash('sha512').update(hashString).digest('hex');
}
```

***

### 4) Cross-Border Payments (PACB)

#### 4.1 General Integration (Without api_version)

##### Hash Formula

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt
```

#### Code Examples

```php
<?php
function generatePACBGeneralHash($params, $salt) {
    $key = $params['key'];
    $txnid = $params['txnid'];
    $amount = $params['amount'];
    $productinfo = $params['productinfo'];
    $firstname = $params['firstname'];
    $email = $params['email'];
    
    // Handle udf1 to udf10
    $udf1 = isset($params['udf1']) ? $params['udf1'] : '';
    $udf2 = isset($params['udf2']) ? $params['udf2'] : '';
    $udf3 = isset($params['udf3']) ? $params['udf3'] : '';
    $udf4 = isset($params['udf4']) ? $params['udf4'] : '';
    $udf5 = isset($params['udf5']) ? $params['udf5'] : '';
    $udf6 = isset($params['udf6']) ? $params['udf6'] : '';
    $udf7 = isset($params['udf7']) ? $params['udf7'] : '';
    $udf8 = isset($params['udf8']) ? $params['udf8'] : '';
    $udf9 = isset($params['udf9']) ? $params['udf9'] : '';
    $udf10 = isset($params['udf10']) ? $params['udf10'] : '';
    
    $hashString = $key . '|' . $txnid . '|' . $amount . '|' . $productinfo . '|' . 
                  $firstname . '|' . $email . '|' . $udf1 . '|' . $udf2 . '|' . 
                  $udf3 . '|' . $udf4 . '|' . $udf5 . '|' . $udf6 . '|' . 
                  $udf7 . '|' . $udf8 . '|' . $udf9 . '|' . $udf10 . '|' . $salt;
    
    return strtolower(hash('sha512', $hashString));
}
?>
```

#### 4.2 With Additional Charges

##### Hash Formula

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt|additional_charges
```

#### Code Examples

```python
def generate_pacb_additional_charges_hash(params, salt, additional_charges):
    key = params['key']
    txnid = params['txnid']
    amount = params['amount']
    productinfo = params['productinfo']
    firstname = params['firstname']
    email = params['email']
    
    # Handle udf1 to udf10
    udf_values = []
    for i in range(1, 11):
        udf_values.append(params.get(f'udf{i}', ''))
    
    udf_string = '|'.join(udf_values)
    
    hash_string = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf_string}|{salt}|{additional_charges}"
    
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
```

#### 4.3 With Additional Charges and Buyer Type

##### Hash Formula

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt|additional_charges|buyer_type_business
```

#### 4.4 With API Version, Additional Charges, and Buyer Type

##### Hash Formula

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|si_details|salt|udf_params|buyer_type_business
```

***

### 5) SI Integration (Subscription APIs)

#### Hash Formula

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT)
```

#### Code Examples

```php
<?php
function generateSIHash($params, $salt, $siDetails) {
    $key = $params['key'];
    $txnid = $params['txnid'];
    $amount = $params['amount'];
    $productinfo = $params['productinfo'];
    $firstname = $params['firstname'];
    $email = $params['email'];
    $udf1 = isset($params['udf1']) ? $params['udf1'] : '';
    $udf2 = isset($params['udf2']) ? $params['udf2'] : '';
    $udf3 = isset($params['udf3']) ? $params['udf3'] : '';
    $udf4 = isset($params['udf4']) ? $params['udf4'] : '';
    $udf5 = isset($params['udf5']) ? $params['udf5'] : '';
    
    $hashString = $key . '|' . $txnid . '|' . $amount . '|' . $productinfo . '|' . 
                  $firstname . '|' . $email . '|' . $udf1 . '|' . $udf2 . '|' . 
                  $udf3 . '|' . $udf4 . '|' . $udf5 . '||||||' . $siDetails . '|' . $salt;
    
    return strtolower(hash('sha512', $hashString));
}
?>
```
```python
def generate_si_hash(params, salt, si_details):
    key = params['key']
    txnid = params['txnid']
    amount = params['amount']
    productinfo = params['productinfo']
    firstname = params['firstname']
    email = params['email']
    udf1 = params.get('udf1', '')
    udf2 = params.get('udf2', '')
    udf3 = params.get('udf3', '')
    udf4 = params.get('udf4', '')
    udf5 = params.get('udf5', '')
    
    hash_string = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{si_details}|{salt}"
    
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
```

### 6) TPV Integration

#### Hash Formula

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT)
```

#### Code Examples

```php
<?php
function generateTPVHash($params, $salt, $beneficiaryDetail) {
    $key = $params['key'];
    $txnid = $params['txnid'];
    $amount = $params['amount'];
    $productinfo = $params['productinfo'];
    $firstname = $params['firstname'];
    $email = $params['email'];
    $udf1 = isset($params['udf1']) ? $params['udf1'] : '';
    $udf2 = isset($params['udf2']) ? $params['udf2'] : '';
    $udf3 = isset($params['udf3']) ? $params['udf3'] : '';
    $udf4 = isset($params['udf4']) ? $params['udf4'] : '';
    $udf5 = isset($params['udf5']) ? $params['udf5'] : '';
    
    $hashString = $key . '|' . $txnid . '|' . $amount . '|' . $productinfo . '|' . 
                  $firstname . '|' . $email . '|' . $udf1 . '|' . $udf2 . '|' . 
                  $udf3 . '|' . $udf4 . '|' . $udf5 . '||||||' . $beneficiaryDetail . '|' . $salt;
    
    return strtolower(hash('sha512', $hashString));
}
?>
```
```python
def generate_tpv_hash(params, salt, beneficiary_detail):
    key = params['key']
    txnid = params['txnid']
    amount = params['amount']
    productinfo = params['productinfo']
    firstname = params['firstname']
    email = params['email']
    udf1 = params.get('udf1', '')
    udf2 = params.get('udf2', '')
    udf3 = params.get('udf3', '')
    udf4 = params.get('udf4', '')
    udf5 = params.get('udf5', '')
    
    hash_string = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{beneficiary_detail}|{salt}"
    
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
```

### 7) Payment API by Version

| api_version | hash logic                                                                            |                                                                                                                               |
| :---------- | :------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------- |
| 1           | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\<br/>       | udf5\|udf6\|udf7\|udf8\|udf9\|udf10                                                                                           |
| 2           | key\|txnid\|amount\|offer_key\|api_version                                            |                                                                                                                               |
| 3           | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\<br/>       | udf5\|udf6\|udf7\|udf8\|udf9\|udf10\|offer_key\|user_credentials\|si\|visaToVisa                                              |
| 5           | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\<br/>       | udf5\|udf6\|udf7\|udf8\|udf9\|udf10\|ccnum\|ccvv\|ccexpmon\|ccexpyr                                                           |
| 6           | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\<br/>       | udf5\|udf6\|udf7\|udf8\|udf9\|udf10\|beneficiarydetail                                                                        |
| 7           | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\<br/>       | udf5\|udf6\|udf7\|udf8\|udf9\|udf10\|si_details                                                                               |
| 8           | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\<br/>       | udf5\|udf6\|udf7\|udf8\|udf9\|udf10\|surl\|furl                                                                               |
| 9           | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\<br/>       | udf5\|udf6\|udf7\|udf8\|udf9\|udf10\|ccnum\|ccvv\|ccexpmon\|ccexpyr\|pg\|bankcode                                             |
| 10          | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\<br/>       | udf5\|udf6\|udf7\|udf8\|udf9\|udf10\|offer_key\|offer_product_id\|offer_brand_id                                              |
| 11          | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\<br/>       | udf5\|udf6\|udf7\|udf8\|udf9\|udf10\|si_details\|free_trial                                                                   |
| 12          | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\<br/> | udf6\|udf7\|udf8\|udf9\|udf10\|card_no                                                                                        |
| 13          | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\<br/> | udf6\|udf7\|udf8\|udf9\|udf10\|splitInfo                                                                                      |
| 14          | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\<br/> | udf6\|udf7\|udf8\|udf9\|udf10\|offer_key\|offer_auto_apply                                                                    |
| 15          | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\<br/> | udf6\|udf7\|udf8\|udf9\|udf10\|user_token\|offer_key\|offer_auto_apply\|cart_details                                          |
| 16          | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\<br/> | udf6\|udf7\|udf8\|udf9\|udf10\|base_split_id                                                                                  |
| 17          | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\<br/> | udf6\|udf7\|udf8\|udf9\|udf10\|user_token\|offer_key\|offer_auto_apply\|cart_details\|extra_charges                           |
| 18          | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\<br/> | udf6\|udf7\|udf8\|udf9\|udf10\|phone                                                                                          |
| 19          | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\<br/> | udf6\|udf7\|udf8\|udf9\|udf10\|user_token\|offer_key\|offer_auto_apply\|cart_details\|extra_charges\|phone                    |
| 20          | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\<br/> | udf6\|udf7\|udf8\|udf9\|udf10\|beneficiarydetail\|si_details\|user_token\|offer_key\|offer_auto_apply\|cart_details           |
| 21          | key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\<br/> | udf6\|udf7\|udf8\|udf9\|udf10\|beneficiarydetail\|si_details\|user_token\|offer_key\|offer_auto_apply\|cart_details\|products |

#### Code Examples

```php
<?php
function generateV19Hash($params, $salt) {
    $key = $params['key'];
    $txnid = $params['txnid'];
    $amount = $params['amount'];
    $productinfo = $params['productinfo'];
    $firstname = $params['firstname'];
    $email = $params['email'];
    
    // Handle udf1 to udf10
    $udf_values = [];
    for ($i = 1; $i <= 10; $i++) {
        $udf_values[] = isset($params["udf{$i}"]) ? $params["udf{$i}"] : '';
    }
    
    $user_token = isset($params['user_token']) ? $params['user_token'] : '';
    $offer_key = isset($params['offer_key']) ? $params['offer_key'] : '';
    $offer_auto_apply = isset($params['offer_auto_apply']) ? $params['offer_auto_apply'] : '';
    $cart_details = isset($params['cart_details']) ? $params['cart_details'] : '';
    $extra_charges = isset($params['extra_charges']) ? $params['extra_charges'] : '';
    $phone = isset($params['phone']) ? $params['phone'] : '';
    
    $hashString = $key . '|' . $txnid . '|' . $amount . '|' . $productinfo . '|' . 
                  $firstname . '|' . $email . '|' . implode('|', $udf_values) . '|' .
                  $user_token . '|' . $offer_key . '|' . $offer_auto_apply . '|' .
                  $cart_details . '|' . $extra_charges . '|' . $phone . '|' . $salt;
    
    return strtolower(hash('sha512', $hashString));
}
?>
```
```python
def generate_v19_hash(params, salt):
    key = params['key']
    txnid = params['txnid']
    amount = params['amount']
    productinfo = params['productinfo']
    firstname = params['firstname']
    email = params['email']
    
    # Handle udf1 to udf10
    udf_values = []
    for i in range(1, 11):
        udf_values.append(params.get(f'udf{i}', ''))
    
    user_token = params.get('user_token', '')
    offer_key = params.get('offer_key', '')
    offer_auto_apply = params.get('offer_auto_apply', '')
    cart_details = params.get('cart_details', '')
    extra_charges = params.get('extra_charges', '')
    phone = params.get('phone', '')
    
    udf_string = '|'.join(udf_values)
    
    hash_string = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf_string}|{user_token}|{offer_key}|{offer_auto_apply}|{cart_details}|{extra_charges}|{phone}|{salt}"
    
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
```

***

## _payment Reverse Hashing

Reverse hashing is used to validate responses from PayU. The reverse hash helps ensure that the response data hasn't been tampered with during transmission.

### General Reverse Hash Formula

```
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

### Code Examples

```php
<?php
function verifyReverseHash($params, $salt, $receivedHash) {
    $key = $params['key'];
    $txnid = $params['txnid'];
    $amount = $params['amount'];
    $productinfo = $params['productinfo'];
    $firstname = $params['firstname'];
    $email = $params['email'];
    $status = $params['status'];
    $udf1 = isset($params['udf1']) ? $params['udf1'] : '';
    $udf2 = isset($params['udf2']) ? $params['udf2'] : '';
    $udf3 = isset($params['udf3']) ? $params['udf3'] : '';
    $udf4 = isset($params['udf4']) ? $params['udf4'] : '';
    $udf5 = isset($params['udf5']) ? $params['udf5'] : '';
    
    $reverseHashString = $salt . '|' . $status . '||||||' . $udf5 . '|' . $udf4 . '|' . 
                        $udf3 . '|' . $udf2 . '|' . $udf1 . '|' . $email . '|' . 
                        $firstname . '|' . $productinfo . '|' . $amount . '|' . $txnid . '|' . $key;
    
    $calculatedHash = strtolower(hash('sha512', $reverseHashString));
    
    return $calculatedHash === strtolower($receivedHash);
}
?>
```
```python
def verify_reverse_hash(params, salt, received_hash):
    key = params['key']
    txnid = params['txnid']
    amount = params['amount']
    productinfo = params['productinfo']
    firstname = params['firstname']
    email = params['email']
    status = params['status']
    udf1 = params.get('udf1', '')
    udf2 = params.get('udf2', '')
    udf3 = params.get('udf3', '')
    udf4 = params.get('udf4', '')
    udf5 = params.get('udf5', '')
    
    reverse_hash_string = f"{salt}|{status}||||||{udf5}|{udf4}|{udf3}|{udf2}|{udf1}|{email}|{firstname}|{productinfo}|{amount}|{txnid}|{key}"
    
    calculated_hash = hashlib.sha512(reverse_hash_string.encode('utf-8')).hexdigest()
    
    return calculated_hash.lower() == received_hash.lower()
```

## General APIs

### Hash Formula

```
sha512(key|command|var1|salt)
```

### Code Examples

```php
<?php
function generateGeneralAPIHash($key, $command, $var1, $salt) {
    $hashString = $key . '|' . $command . '|' . $var1 . '|' . $salt;
    return strtolower(hash('sha512', $hashString));
}

// Example usage
$hash = generateGeneralAPIHash('yourKey', 'verify_payment', 'txnid123', 'yourSalt');
?>
```
```java
public static String generateGeneralAPIHash(String key, String command, String var1, String salt) {
    String hashString = key + "|" + command + "|" + var1 + "|" + salt;
    return sha512(hashString);
}
```
```csharp
public static string GenerateGeneralAPIHash(string key, string command, string var1, string salt)
{
    string hashString = $"{key}|{command}|{var1}|{salt}";
    return Sha512(hashString);
}
```
```python
def generate_general_api_hash(key, command, var1, salt):
    hash_string = f"{key}|{command}|{var1}|{salt}"
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
```
```javascript
function generateGeneralAPIHash(key, command, var1, salt) {
    const hashString = `${key}|${command}|${var1}|${salt}`;
    return crypto.createHash('sha512').update(hashString).digest('hex');
}
```

***

##
