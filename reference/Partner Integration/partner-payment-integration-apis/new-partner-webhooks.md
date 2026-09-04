---
title: '[NEW] Partner Webhooks'
deprecated: false
hidden: true
metadata:
  robots: index
---
After a customer completes a payment, PayU sends a webhook POST request to your configured partner webhook URL with the complete transaction details. This page covers the webhook payload structure, hash verification, and database configuration.

## Webhook Flow

1. Customer completes payment (success/failure/cancel)
2. PayU receives callback from payment gateway
3. PayU validates internal hash
4. PayU calls internal verify payment API
5. PayU sends webhook POST to your configured partner URL
6. Your endpoint verifies webhook hash
7. Your endpoint responds with HTTP 200
8. You call verify payment API for final confirmation

***

## Database Configuration

Before receiving webhooks, you must configure the following database tables:

### Table 1: partner_webhook_urls

Configure partner-level or merchant-level webhook URLs.

**Schema:**

| Column                       | Type    | Description                                       |
| ---------------------------- | ------- | ------------------------------------------------- |
| `partner_uuid`               | string  | Your partner/reseller UUID                        |
| `merchant_id`                | integer | Specific merchant ID, or `NULL` for partner-level |
| `partner_webhook_success`    | string  | URL for successful payment webhooks               |
| `partner_webhook_failure`    | string  | URL for failed payment webhooks                   |
| `partner_webhook_cancelled`  | string  | URL for cancelled payment webhooks                |
| `partner_webhook_default`    | string  | Default/fallback webhook URL                      |
| `partner_name`               | string  | Partner display name                              |
| `is_payment_webhook_enabled` | boolean | **Must be&#x20;**`true` to enable webhooks        |
| `is_json_payment_payload`    | boolean | `true` for JSON payload, `false` for form-encoded |

**Example INSERT (Partner-Level Configuration):**

```sql
INSERT INTO partner_webhook_urls (
  partner_uuid,
  merchant_id,
  partner_webhook_success,
  partner_webhook_failure,
  partner_webhook_cancelled,
  partner_webhook_default,
  partner_name,
  is_payment_webhook_enabled,
  is_json_payment_payload
) VALUES (
  '11ee-0e7e-5403fde2-9523-0a696b110fde',
  NULL,  -- NULL for partner-level (applies to all merchants)
  'https://partner.example.com/webhook/payment/success',
  'https://partner.example.com/webhook/payment/failure',
  'https://partner.example.com/webhook/payment/cancelled',
  'https://partner.example.com/webhook/payment/default',
  'WhatsApp Partner',
  true,  -- MUST be true
  false
);
```

<Info>
**Partner-Level vs Merchant-Level:**
- Set `merchant_id = NULL` for partner-level webhooks (applies to all merchants under this partner)
- Set specific `merchant_id` value for merchant-specific webhook URLs
- PayU looks up merchant-level first, then falls back to partner-level
</Info>

***

### Table 2: partner_merchant_params

Configure partner-merchant behavior flags.

**Example: Disable Core Webhook Fallback**

```sql
INSERT INTO partner_merchant_params (
  partner_uuid,
  merchant_id,
  key,
  value,
  is_active
) VALUES (
  '11ee-0e7e-5403fde2-9523-0a696b110fde',
  '8739528',
  'disable_core_payment_webhook_url',
  '1',
  true
);
```

<Info>
**Fallback Behavior:**
- **Without this parameter**: If no partner webhook URL is found, PayU falls back to merchant's core webhook URLs (`PAYMENT_SUCCESS_URL`, `PAYMENT_FAILURE_URL`)
- **With `disable_core_payment_webhook_url = '1'`**: PayU will **only** send to partner webhook URLs and skip merchant core URLs
</Info>

***

## Webhook Payload Structure

PayU sends a `POST` request with `Map<String, String>` payload containing:

**Sample Webhook Payload:**

```json
{
  "key": "7o583a",
  "txnid": "28471834809170981",
  "mihpayid": "30478359671",
  "status": "success",
  "unmappedstatus": "captured",
  "mode": "UPI",
  "bankcode": "INTENT",
  "amount": "518.02",
  "productinfo": "28471834809170981",
  "firstname": "",
  "lastname": "",
  "email": "",
  "phone": "919820988398",
  "udf1": "",
  "udf2": "1370625260",
  "udf3": "r-hway-LDnTRBuFK8STTTeTEc2SuD",
  "udf4": "",
  "udf5": "whatsapp",
  "merchant_id": "8739528",
  "error": "E000",
  "error_Message": "No Error",
  "hash": "b8f3a5d2e1c7b4a9e6d3c8b1a2f4e7d9c3b6a2e1d5f4c7a8b3e6d2f1c9a5b4e7"
}
```

***

## Webhook Parameters

| Parameter        | Type   | Description                                                                    |
| ---------------- | ------ | ------------------------------------------------------------------------------ |
| `key`            | string | Merchant key                                                                   |
| `txnid`          | string | Transaction ID (from payment request)                                          |
| `mihpayid`       | string | PayU payment ID                                                                |
| `status`         | string | Payment status: `success`, `failure`, `pending`, `userCancelled`               |
| `unmappedstatus` | string | Internal status: `captured`, `failed`, `initiated`, `bounced`, `userCancelled` |
| `mode`           | string | Payment mode: `UPI`, `CC`, `DC`, `NB`, `WALLET`                                |
| `bankcode`       | string | Payment instrument code (e.g., `INTENT`, `INTTPV`, `ICICI`)                    |
| `amount`         | string | Transaction amount                                                             |
| `productinfo`    | string | Product description                                                            |
| `firstname`      | string | Customer first name                                                            |
| `lastname`       | string | Customer last name                                                             |
| `email`          | string | Customer email                                                                 |
| `phone`          | string | Customer phone number                                                          |
| `udf1` - `udf5`  | string | User-defined fields (echoed from payment request)                              |
| `merchant_id`    | string | Merchant ID                                                                    |
| `error`          | string | Error code (`E000` for no error)                                               |
| `error_Message`  | string | Error description                                                              |
| `hash`           | string | SHA-512 hash for webhook verification                                          |

***

## Webhook Hash Verification

**Always verify** the webhook hash before processing the payload. Use the **reverse hash formula**:

### Reverse Hash Formula

```
client_secret|status|||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|merchant_id
```

<Warning>
**Critical Hash Notes:**
- There are **five consecutive pipe characters** (`|||||`) between `status` and `udf5`
- The field order is **reversed** compared to the payment request hash
- Use your OAuth `client_secret`, **not** the merchant salt
- **Do not** include a trailing pipe after `merchant_id`
- Compute SHA-512 and compare **case-insensitively** with the `hash` field
</Warning>

***

### Webhook Verification Code (Java)

```java
import java.security.MessageDigest;
import java.util.Map;

public class PartnerWebhookVerifier {
    
    public static boolean verifyWebhookHash(Map<String, String> payload, String clientSecret) 
        throws Exception {
        
        StringBuilder hashString = new StringBuilder();
        hashString.append(clientSecret).append("|");
        hashString.append(payload.get("status")).append("|||||");
        hashString.append(getOrEmpty(payload, "udf5")).append("|");
        hashString.append(getOrEmpty(payload, "udf4")).append("|");
        hashString.append(getOrEmpty(payload, "udf3")).append("|");
        hashString.append(getOrEmpty(payload, "udf2")).append("|");
        hashString.append(getOrEmpty(payload, "udf1")).append("|");
        hashString.append(getOrEmpty(payload, "email")).append("|");
        hashString.append(getOrEmpty(payload, "firstname")).append("|");
        hashString.append(getOrEmpty(payload, "productinfo")).append("|");
        hashString.append(getOrEmpty(payload, "amount")).append("|");
        hashString.append(getOrEmpty(payload, "txnid")).append("|");
        hashString.append(getOrEmpty(payload, "merchant_id"));
        
        String expectedHash = sha512Hex(hashString.toString());
        return expectedHash.equalsIgnoreCase(payload.get("hash"));
    }
    
    private static String getOrEmpty(Map<String, String> map, String key) {
        return map.getOrDefault(key, "");
    }
    
    private static String sha512Hex(String input) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] digest = md.digest(input.getBytes("UTF-8"));
        StringBuilder hex = new StringBuilder();
        for (byte b : digest) {
            String h = Integer.toHexString(0xFF & b);
            if (h.length() == 1) hex.append("0");
            hex.append(h);
        }
        return hex.toString();
    }
}
```

***

### Webhook Verification Code (Python)

```python
import hashlib

def verify_webhook_hash(payload: dict, client_secret: str) -> bool:
    # Build hash string
    hash_string = (
        f"{client_secret}|"
        f"{payload.get('status', '')}|||||"
        f"{payload.get('udf5', '')}|"
        f"{payload.get('udf4', '')}|"
        f"{payload.get('udf3', '')}|"
        f"{payload.get('udf2', '')}|"
        f"{payload.get('udf1', '')}|"
        f"{payload.get('email', '')}|"
        f"{payload.get('firstname', '')}|"
        f"{payload.get('productinfo', '')}|"
        f"{payload.get('amount', '')}|"
        f"{payload.get('txnid', '')}|"
        f"{payload.get('merchant_id', '')}"
    )
    
    # Compute SHA-512 hash
    expected_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
    
    # Compare case-insensitively
    return expected_hash.lower() == payload.get('hash', '').lower()

# Usage
if verify_webhook_hash(webhook_payload, YOUR_CLIENT_SECRET):
    print("✅ Webhook hash verified")
    # Process payment
else:
    print("❌ Invalid webhook hash - discarding payload")
```

***

### Webhook Verification Code (PHP)

```php
<?php

function verifyWebhookHash($payload, $clientSecret) {
    $hashString = $clientSecret . "|" .
                 ($payload['status'] ?? '') . "|||||" .
                 ($payload['udf5'] ?? '') . "|" .
                 ($payload['udf4'] ?? '') . "|" .
                 ($payload['udf3'] ?? '') . "|" .
                 ($payload['udf2'] ?? '') . "|" .
                 ($payload['udf1'] ?? '') . "|" .
                 ($payload['email'] ?? '') . "|" .
                 ($payload['firstname'] ?? '') . "|" .
                 ($payload['productinfo'] ?? '') . "|" .
                 ($payload['amount'] ?? '') . "|" .
                 ($payload['txnid'] ?? '') . "|" .
                 ($payload['merchant_id'] ?? '');
    
    $expectedHash = hash('sha512', $hashString);
    
    return strcasecmp($expectedHash, $payload['hash'] ?? '') === 0;
}

// Usage
if (verifyWebhookHash($webhookPayload, $clientSecret)) {
    echo "✅ Webhook hash verified";
    // Process payment
} else {
    echo "❌ Invalid webhook hash";
    http_response_code(400);
}
?>
```

***

## Webhook Handler Best Practices

### 1. Always Respond with HTTP 200

PayU expects your webhook endpoint to respond with HTTP 200 status:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook/payment/success', methods=['POST'])
def handle_webhook():
    payload = request.get_json() or request.form.to_dict()
    
    # Verify hash
    if not verify_webhook_hash(payload, CLIENT_SECRET):
        return jsonify({"error": "Invalid hash"}), 400
    
    # Process asynchronously
    process_payment_async(payload)
    
    # Always return 200 quickly
    return jsonify({"status": "received"}), 200
```

### 2. Process Asynchronously

Don't block the webhook response with database writes or API calls:

```java
@RestController
public class WebhookController {
    
    @Autowired
    private AsyncPaymentProcessor processor;
    
    @PostMapping("/webhook/payment/success")
    public ResponseEntity<String> handleWebhook(@RequestBody Map<String, String> payload) {
        // Quick hash verification
        if (!verifyWebhookHash(payload, clientSecret)) {
            return ResponseEntity.status(400).body("Invalid hash");
        }
        
        // Process asynchronously
        CompletableFuture.runAsync(() -> processor.processPayment(payload));
        
        // Return 200 immediately
        return ResponseEntity.ok("Received");
    }
}
```

### 3. Idempotency Protection

Handle duplicate webhooks gracefully:

```python
def process_payment_webhook(payload):
    txnid = payload['txnid']
    mihpayid = payload['mihpayid']
    
    # Check if already processed
    if payment_exists(txnid, mihpayid):
        print(f"Payment {txnid} already processed, skipping")
        return
    
    # Process payment (with database transaction)
    with transaction():
        save_payment(payload)
        update_order_status(txnid, payload['status'])
```

### 4. Always Call Verify Payment API

Even after webhook verification, call the verify payment API:

```javascript
async function handleWebhook(payload) {
    // 1. Verify webhook hash
    if (!verifyWebhookHash(payload, CLIENT_SECRET)) {
        throw new Error('Invalid webhook hash');
    }
    
    // 2. Call verify payment API
    const verification = await verifyPayment(
        payload.txnid,
        payload.merchant_id,
        RESELLER_ID
    );
    
    // 3. Reconcile
    if (verification.mihpayid !== payload.mihpayid) {
        throw new Error('Payment ID mismatch');
    }
    
    // 4. Update database
    await updatePaymentStatus(payload);
}
```

***

## Testing Webhooks

### Local Testing with ngrok

Use ngrok to expose your local webhook endpoint:

```bash
# Install ngrok
brew install ngrok  # macOS
# or download from https://ngrok.com

# Start your local server on port 3000
node server.js

# Expose with ngrok
ngrok http 3000

# Use the ngrok URL in database
# e.g., https://abc123.ngrok.io/webhook/payment/success
```

### Webhook Simulation

Create a test script to simulate PayU webhooks:

```python
import requests
import hashlib

def simulate_webhook(txnid, status="success"):
    payload = {
        "txnid": txnid,
        "mihpayid": "30478359671",
        "status": status,
        "unmappedstatus": "captured" if status == "success" else "failed",
        "amount": "518.02",
        "merchant_id": "8739528",
        # ... other fields
    }
    
    # Compute hash
    payload['hash'] = compute_reverse_hash(payload, CLIENT_SECRET)
    
    # Send to your endpoint
    response = requests.post(
        "http://localhost:3000/webhook/payment/success",
        json=payload
    )
    print(f"Response: {response.status_code}")
```

***

## Common Errors

| Issue                   | Cause                                          | Resolution                       |
| ----------------------- | ---------------------------------------------- | -------------------------------- |
| Webhooks not received   | `is_payment_webhook_enabled` is `false`        | Set to `true` in database        |
| Webhooks not received   | No row in `partner_webhook_urls`               | Insert configuration row         |
| Hash verification fails | Using merchant salt instead of `client_secret` | Use OAuth `client_secret`        |
| Hash verification fails | Incorrect field order                          | Use reverse hash formula exactly |
| Duplicate webhooks      | PayU retry mechanism                           | Implement idempotency checks     |

***

## Next Steps

- [POST /partner/verifyPayment](ref:verify-payment-partner-api) — Verify payment status API
- [Partner Payments Integration Guide](doc:partner-payments-integration-guide) — Complete integration flow
- [Testing and Troubleshooting](doc:testing-and-troubleshooting-partner-payments) — Error resolution guide

<Success>
**Webhook Integration Complete!** Your endpoint can now receive, verify, and process real-time payment status updates from PayU.
</Success>
