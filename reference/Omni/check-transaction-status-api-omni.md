---
title: Check Transaction Status API - Omni
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Check Transaction Status API - Omni
excerpt: API reference for checking PayU Omni transaction status
category: 65ee4b13ba7bd6003d0c61b4
slug: check-transaction-status-api-omni
---

The Check Transaction Status API allows merchants and partners to query the status and retrieve complete details of transactions initiated via the PayU Omni Integrated Flow. This API is essential for payment verification, reconciliation, and handling delayed webhook scenarios.

---

## Endpoint

**HTTP Method:** `POST`

**URL Path:** `/v1/transaction/?mode=bqr`

**Content-Type:** `application/json`

**Required Header:** `Info-Command: check_bqr_txn_status`

---

## Environment URLs

| Environment | URL |
| ----------- | ----------------------------------------------- |
| Production  | `https://info.payu.in/v1/transaction/?mode=bqr` |

<Warning>
⚠️ **Info Gap:** Test/UAT environment URL not documented in source materials. Contact PayU Integration Support (integration-support@payu.in) for test endpoint details.
</Warning>

---

## When to Use This API

Use the Check Transaction Status API in the following scenarios:

✅ **Webhook not received** within 5 minutes of payment initiation  
✅ **Daily reconciliation** to verify all transactions  
✅ **Customer disputes** requiring transaction proof  
✅ **Retry logic** - verify transaction state before retrying  
✅ **Refund processing** - confirm payment status before initiating refund  
✅ **Audit trails** - maintain transaction history for compliance

---

## Sample Request

### cURL

```bash
curl --location 'https://info.payu.in/v1/transaction/?mode=bqr' \
--header 'mid: YOUR_MERCHANT_ID' \
--header 'Info-Command: check_bqr_txn_status' \
--header 'Content-Type: application/json' \
--data '{
  "merchantKey": "YOUR_MERCHANT_KEY",
  "merchantTransactionIds": ["TXN_2024011501", "TXN_2024011502"],
  "hash": "calculated_hash_value"
}'
```
```python
import requests
import hashlib
import json

def generate_status_hash(merchant_key, txn_ids, merchant_salt):
    # Join transaction IDs with pipe separator
    txn_ids_string = '|'.join(txn_ids)
    
    # Hash sequence: merchant_key|txn_ids_separated_by_pipe|merchant_salt
    hash_string = f"{merchant_key}|{txn_ids_string}|{merchant_salt}"
    
    # Generate SHA-512 hash
    hash_value = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
    
    return hash_value

# Example usage
merchant_key = "YOUR_MERCHANT_KEY"
merchant_salt = "YOUR_MERCHANT_SALT"
txn_ids = ["TXN_2024011501", "TXN_2024011502"]

hash_value = generate_status_hash(merchant_key, txn_ids, merchant_salt)

url = "https://info.payu.in/v1/transaction/?mode=bqr"
headers = {
    "mid": "YOUR_MERCHANT_ID",
    "Info-Command": "check_bqr_txn_status",
    "Content-Type": "application/json"
}
payload = {
    "merchantKey": merchant_key,
    "merchantTransactionIds": txn_ids,
    "hash": hash_value
}

try:
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
```php
<?php

function generateStatusHash($merchantKey, $txnIds, $merchantSalt) {
    // Join transaction IDs with pipe separator
    $txnIdsString = implode('|', $txnIds);
    
    // Hash sequence
    $hashString = $merchantKey . '|' . $txnIdsString . '|' . $merchantSalt;
    
    // Generate SHA-512 hash
    return hash('sha512', $hashString);
}

$merchantKey = "YOUR_MERCHANT_KEY";
$merchantSalt = "YOUR_MERCHANT_SALT";
$txnIds = ["TXN_2024011501", "TXN_2024011502"];

$hash = generateStatusHash($merchantKey, $txnIds, $merchantSalt);

$url = "https://info.payu.in/v1/transaction/?mode=bqr";
$headers = [
    "mid: YOUR_MERCHANT_ID",
    "Info-Command: check_bqr_txn_status",
    "Content-Type: application/json"
];
$payload = json_encode([
    "merchantKey" => $merchantKey,
    "merchantTransactionIds" => $txnIds,
    "hash" => $hash
]);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```
```java
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;
import java.security.MessageDigest;
import java.util.Arrays;
import com.google.gson.Gson;
import java.util.HashMap;
import java.util.Map;

public class CheckStatusAPI {
    
    public static String generateStatusHash(String merchantKey, String[] txnIds, String merchantSalt) throws Exception {
        // Join transaction IDs with pipe
        String txnIdsString = String.join("|", txnIds);
        
        // Hash sequence
        String hashString = merchantKey + "|" + txnIdsString + "|" + merchantSalt;
        
        // Generate SHA-512 hash
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] hashBytes = md.digest(hashString.getBytes("UTF-8"));
        
        // Convert to hex
        StringBuilder hexString = new StringBuilder();
        for (byte b : hashBytes) {
            String hex = Integer.toHexString(0xff & b);
            if (hex.length() == 1) hexString.append('0');
            hexString.append(hex);
        }
        
        return hexString.toString();
    }
    
    public static void main(String[] args) throws Exception {
        String merchantKey = "YOUR_MERCHANT_KEY";
        String merchantSalt = "YOUR_MERCHANT_SALT";
        String[] txnIds = {"TXN_2024011501", "TXN_2024011502"};
        
        String hash = generateStatusHash(merchantKey, txnIds, merchantSalt);
        
        // Build payload
        Map<String, Object> payload = new HashMap<>();
        payload.put("merchantKey", merchantKey);
        payload.put("merchantTransactionIds", Arrays.asList(txnIds));
        payload.put("hash", hash);
        
        String jsonPayload = new Gson().toJson(payload);
        
        // Build request
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://info.payu.in/v1/transaction/?mode=bqr"))
            .header("mid", "YOUR_MERCHANT_ID")
            .header("Info-Command", "check_bqr_txn_status")
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(jsonPayload))
            .build();
        
        HttpClient client = HttpClient.newHttpClient();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        
        System.out.println("Status: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```

---
## Request Parameters
### Request Headers

**Mandatory parameters**

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| mid | String | Merchant ID provided by PayU | YOUR_MERCHANT_ID |
| Info-Command | String | Must be "check_bqr_txn_status" | check_bqr_txn_status |
| Content-Type | String | Must be "application/json" | application/json |

---

### Body Parameters

**Mandatory parameters**

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| merchantKey | String | Merchant key provided by PayU | YOUR_MERCHANT_KEY |
| merchantTransactionIds | Array of Strings | List of transaction IDs to query (max 10 per request) | ["TXN_001", "TXN_002"] |
| hash | String | SHA-512 hash for authentication (see Hash Calculation below) | a3b2c1d0e9f8a7b6... |

---

## Hash Calculation

The hash ensures request authenticity and prevents tampering.

### Hash Sequence

```
hash_string = merchant_key + "|" + txn_id_1 + "|" + txn_id_2 + "|" + ... + "|" + merchant_salt

hash = SHA512(hash_string) (lowercase hexadecimal)
```

### Example

```python
import hashlib

merchant_key = "ABC123"
merchant_salt = "XYZ789"
txn_ids = ["TXN_001", "TXN_002", "TXN_003"]

# Join with pipe
hash_string = merchant_key + "|" + "|".join(txn_ids) + "|" + merchant_salt
# Result: "ABC123|TXN_001|TXN_002|TXN_003|XYZ789"

# Calculate SHA-512 hash
hash_value = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
```

<Warning>
**Important:**
- Hash must be **lowercase hexadecimal**
- Transaction IDs must be in the **same order** as in the request array
- Use pipe `|` separator between each component
- Include `merchant_salt` at the end
</Warning>

---

## Sample Response

### Success Scenario

```json
{
  "status": "success",
  "data": {
    "TXN_2024011501": {
      "txnId": "TXN_2024011501",
      "paymentId": "PAYU_TXN_12345ABC",
      "orderId": "ORD_2024011501",
      "amount": "500.00",
      "txnStatus": "SUCCESS",
      "paymentMethod": "CARD",
      "cardDetails": {
        "cardType": "CREDIT",
        "cardNetwork": "VISA",
        "last4Digits": "1234"
      },
      "timestamp": "2024-01-15T10:32:45Z",
      "settlementDate": "2024-01-16",
      "merchantMessage": "Transaction successful"
    },
    "TXN_2024011502": {
      "txnId": "TXN_2024011502",
      "paymentId": "PAYU_TXN_67890XYZ",
      "orderId": "ORD_2024011502",
      "amount": "1000.00",
      "txnStatus": "FAILED",
      "errorCode": "E_PAYMENT_DECLINED",
      "message": "Payment declined by bank",
      "timestamp": "2024-01-15T10:35:12Z"
    }
  }
}
```

### Failure Scenario
**Transaction Not Found**

```json
{
  "status": "failed",
  "message": "Transaction not found",
  "errorCode": "E_TXN_NOT_FOUND",
  "data": {
    "TXN_2024011503": {
      "status": "NOT_FOUND",
      "message": "No transaction found for this txnId"
    }
  }
}
```

**Invalid Hash**

```json
{
  "status": "failed",
  "message": "Invalid hash",
  "errorCode": "E_INVALID_HASH"
}
```

---


## Response Parameters

### Success Response Fields

| Field | Type | Description |
| :--- | :--- | :--- |
| status | String | "success" or "failed" |
| data | Object | Map of transaction IDs to transaction details |

### Transaction Details Object

| Field | Type | Description |
| :--- | :--- | :--- |
| txnId | String | Transaction ID from your system |
| paymentId | String | PayU-generated payment ID |
| orderId | String | Order ID from your system |
| amount | String | Transaction amount |
| txnStatus | String | "SUCCESS", "FAILED", "PENDING", "USER_CANCELLED", "INITIATED" |
| paymentMethod | String | "CARD", "UPI", "WALLET", "EMI", "QR" |
| cardDetails | Object | (If payment method is CARD) Card type, network, last 4 digits |
| timestamp | String | ISO 8601 timestamp |
| settlementDate | String | Expected settlement date (YYYY-MM-DD) |
| errorCode | String | (On failure) Error code |
| message | String | Human-readable message |

### Transaction Status Values

| Status Value | Description |
| :--- | :--- |
| SUCCESS | Payment completed successfully |
| FAILED | Payment failed (bank decline, insufficient funds, etc.) |
| PENDING | Payment in progress (waiting for customer action) |
| USER_CANCELLED | Customer cancelled payment on device |
| INITIATED | Payment request sent to device (customer hasn't acted yet) |
| NOT_FOUND | Transaction ID not found in PayU system |

---

## Error Codes

| Error Code | Message | Cause | Resolution |
|------------|---------|-------|------------|
| E_TXN_NOT_FOUND | Transaction not found | Transaction ID doesn't exist in PayU system | Verify `txnId` is correct and transaction was initiated |
| E_INVALID_HASH | Invalid hash | Hash calculation incorrect or credentials wrong | Regenerate hash with correct sequence and credentials |
| E_INVALID_MERCHANT | Invalid merchant | Merchant key or ID incorrect | Verify merchant credentials |
| E_RATE_LIMIT | Too many requests | Exceeded API rate limit | Implement backoff and retry after 1 minute |
| 401 | Unauthorized | Invalid merchant credentials | Verify `mid` and `merchantKey` are correct |

---

## Best Practices

### When to Call Status API

✅ **If webhook not received within 5 minutes** of payment initiation  
✅ **Before retrying** a failed transaction  
✅ **During daily reconciliation** to verify all transactions  
✅ **For high-value transactions** to cross-verify webhook data  
✅ **When customer disputes** transaction status

### Query Optimization

- **Batch queries:** Query up to 10 transactions per request (reduces API calls)
- **Cache results:** Store transaction status locally to avoid repeated queries
- **Use filters:** Only query transactions in specific time windows
- **Implement retry:** Use exponential backoff for failed API calls

### Security

- **Verify hash:** Always validate response data authenticity
- **Secure credentials:** Store `merchant_salt` in environment variables
- **Rate limiting:** Implement client-side rate limiting to avoid throttling
- **Log requests:** Maintain audit trail of all status queries

---

## Related Resources

- **[Collect Payment Using PayU Omni →](doc:collect-payment-using-payu-omni)** - Complete integration guide
- **[Initiate Payment API Reference →](doc:initiate-payment-api-omni)** - Initiate POS payments
- **[PayU Omni Overview →](doc:payu-omni)** - Product features and benefits

---

