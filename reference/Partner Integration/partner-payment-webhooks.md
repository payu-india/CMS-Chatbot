---
title: Partner Payment Webhooks
deprecated: false
hidden: false
metadata:
  robots: index
---
After the customer completes payment (or if account validation fails), PayU sends a webhook notification to your configured partner webhook URL.

## Sample Success Webhook Payload (UPI TPV

```json
{
  "key": "JPM7Fg",
  "txnid": "TPVUPI20240315001",
  "mihpayid": "30478359671",
  "status": "success",
  "unmappedstatus": "captured",
  "mode": "UPI",
  "bankcode": "INTTPV",
  "amount": "518.02",
  "productinfo": "Loan EMI Payment",
  "firstname": "Amit",
  "email": "amit.kumar@example.com",
  "phone": "919876543210",
  "udf1": "loan_account_123",
  "udf2": "emi_month_06",
  "udf3": "tpv_reference_001",
  "udf4": "",
  "udf5": "partner_tpv_channel",
  "merchant_id": "8739528",
  "error": "No Error",
  "error_Message": "No Error",
  "hash": "webhook_hash_from_payu"
}
```

**UPI TPV-Specific Fields:**

| Field            | Value for UPI TPV                                                |
| ---------------- | ---------------------------------------------------------------- |
| `mode`           | `"UPI"`                                                          |
| `bankcode`       | `"INTTPV"` (automatically set by PayU)                           |
| `unmappedstatus` | `"captured"` (success) or `"failed"` (failure/validation failed) |

### Step 3.2: Verify Webhook Hash

**Always verify the webhook hash** before processing.

**Reverse Hash Formula:**

```
client_secret|status|||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|merchant_id
```

<Warning>
**Critical Verification Rules:**
- There are **five consecutive pipes** (`|||||`) between `status` and `udf5`
- Use OAuth **client_secret** (NOT merchant salt)
- Do NOT add a trailing pipe after `merchant_id`
- Compute SHA-512 and compare as **case-insensitive**
- **Reject webhook if hash doesn't match**
</Warning>

**Sample Verification Code:**

**Python:**

```python
import hashlib

def verify_upi_tpv_webhook_hash(webhook_payload, client_secret):
    status = webhook_payload.get('status', '')
    udf5 = webhook_payload.get('udf5', '')
    udf4 = webhook_payload.get('udf4', '')
    udf3 = webhook_payload.get('udf3', '')
    udf2 = webhook_payload.get('udf2', '')
    udf1 = webhook_payload.get('udf1', '')
    email = webhook_payload.get('email', '')
    firstname = webhook_payload.get('firstname', '')
    productinfo = webhook_payload.get('productinfo', '')
    amount = webhook_payload.get('amount', '')
    txnid = webhook_payload.get('txnid', '')
    merchant_id = webhook_payload.get('merchant_id', '')
    received_hash = webhook_payload.get('hash', '')
    
    hash_string = f"{client_secret}|{status}|||||{udf5}|{udf4}|{udf3}|{udf2}|{udf1}|{email}|{firstname}|{productinfo}|{amount}|{txnid}|{merchant_id}"
    
    computed_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
    
    return computed_hash.lower() == received_hash.lower()

# Example
is_valid = verify_upi_tpv_webhook_hash(webhook_data, "your_client_secret")

if is_valid:
    print("✅ UPI TPV webhook verified — account validation successful")
else:
    print("❌ Invalid webhook hash — reject")
```

**Java:**

```java
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class UPITPVWebhookVerifier {
    public static boolean verifyHash(
        String status, String udf5, String udf4, String udf3, String udf2, String udf1,
        String email, String firstname, String productinfo, String amount,
        String txnid, String merchantId, String receivedHash, String clientSecret
    ) throws NoSuchAlgorithmException {
        
        String hashString = clientSecret + "|" + status + "|||||" + 
                          udf5 + "|" + udf4 + "|" + udf3 + "|" + udf2 + "|" + udf1 + "|" +
                          email + "|" + firstname + "|" + productinfo + "|" + 
                          amount + "|" + txnid + "|" + merchantId;
        
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] hashBytes = md.digest(hashString.getBytes());
        
        StringBuilder hexString = new StringBuilder();
        for (byte b : hashBytes) {
            String hex = Integer.toHexString(0xff & b);
            if (hex.length() == 1) hexString.append('0');
            hexString.append(hex);
        }
        
        return hexString.toString().equalsIgnoreCase(receivedHash);
    }
}
```

### Step 3.3: Process Webhook

**Python Flask Webhook Handler:**

```python
from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/partner/webhook/success', methods=['POST'])
def handle_upi_tpv_webhook():
    webhook_data = request.json
    
    # Verify hash
    if not verify_upi_tpv_webhook_hash(webhook_data, "your_client_secret"):
        return jsonify({"error": "Invalid hash"}), 400
    
    # Extract details
    txnid = webhook_data.get('txnid')
    mihpayid = webhook_data.get('mihpayid')
    status = webhook_data.get('status')
    bankcode = webhook_data.get('bankcode')
    amount = webhook_data.get('amount')
    
    # Verify it's a TPV transaction
    if bankcode == "INTTPV":
        print(f"✅ UPI TPV Payment: {status} | {txnid} | PayU ID: {mihpayid} | Amount: ₹{amount}")
        print(f"   Account validation successful - payment from verified beneficiary account")
    
    # Update database
    # db.update_payment_status(txnid=txnid, mihpayid=mihpayid, status=status, bankcode=bankcode)
    
    # Respond with 200 OK
    return jsonify({"message": "Webhook received"}), 200

if __name__ == '__main__':
    app.run(port=5000)
```
