---
title: Partner Payment Webhooks
deprecated: false
hidden: false
metadata:
  robots: index
---
After the customer completes payment (or if account validation fails), PayU sends a webhook notification to your configured partner webhook URL.

## Step 1: Get the Webhook Payload

### Sample Webhook Payloads
#### Payloads for Hosted Checkout
**Webhook Configuration:**

Ensure these URLs are configured:

\- `partner_webhook_success` — Called on successful payment
\- `partner_webhook_failure` — Called on failed payment
\- `partner_webhook_cancelled` — Called when payment is cancelled

<Callout icon="⚠️" theme="info">
  ### Contact your Account Manager to register for the Webhooks.
</Callout>

<Accordion title="Sample Payload" icon="fa-code">
  **Sample Success Webhook Payload**

  ```json
  {
    "key": "JPM7Fg",
    "txnid": "PPHOST20240315001",
    "mihpayid": "403993715521899234",
    "status": "success",
    "unmappedstatus": "captured",
    "mode": "CC",
    "bankcode": "VISA",
    "amount": "1500.00",
    "productinfo": "Premium Subscription - Monthly",
    "firstname": "Priya",
    "email": "priya.sharma@example.com",
    "phone": "919876543210",
    "udf1": "subscription_plan_premium",
    "udf2": "monthly_billing",
    "udf3": "",
    "udf4": "",
    "udf5": "partner_web_checkout",
    "merchant_id": "8739528",
    "error": "No Error",
    "error_Message": "No Error",
    "hash": "webhook_hash_from_payu"
  }
  ```

  **Sample Failure Webhook Payload:**

  ```json
  {
    "key": "JPM7Fg",
    "txnid": "PPHOST20240315001",
    "mihpayid": "403993715521899241",
    "status": "failure",
    "unmappedstatus": "failed",
    "mode": "NB",
    "bankcode": "ICIC",
    "amount": "1500.00",
    "productinfo": "Premium Subscription - Monthly",
    "firstname": "Priya",
    "email": "priya.sharma@example.com",
    "phone": "919876543210",
    "udf1": "subscription_plan_premium",
    "udf2": "monthly_billing",
    "udf3": "",
    "udf4": "",
    "udf5": "partner_web_checkout",
    "merchant_id": "8739528",
    "error": "E000",
    "error_Message": "Payment declined by bank",
    "hash": "webhook_hash_from_payu"
  }
  ```
</Accordion>

#### Payloads for Hosted Checkout TPV

**Webhook URLs (configured in PayU system):**

- `partner_webhook_success` — Triggered on successful payment
- `partner_webhook_failure` — Triggered on failed payment
- `partner_webhook_cancelled` — Triggered when customer cancels

**Webhook Payload (POST request):**

```json
{
  "mihpayid": "403993715529111111",
  "txnid": "HC_TPV_20240315_001",
  "status": "success",
  "amount": "1500.00",
  "productinfo": "Loan EMI Payment - March 2024",
  "firstname": "Rajesh",
  "email": "rajesh.kumar@example.com",
  "phone": "9876543210",
  "mode": "UPI",
  "bankcode": "INTTPV",
  "unmappedstatus": "captured",
  "merchant_id": "8739528",
  "udf1": "session_12345",
  "udf2": "1370625260",
  "udf3": "loan-ref-ABC123",
  "udf4": "",
  "udf5": "whatsapp",
  "hash": "a1b2c3d4e5f6...",
  "payment_source": "payu"
}
```

**Key TPV Fields in Webhook:**

| Field          | Value for TPV                                   | Description                    |
| -------------- | ----------------------------------------------- | ------------------------------ |
| mode           | `"UPI"`                                         | Payment method used            |
| bankcode       | `"INTTPV"`                                      | Confirms TPV validation passed |
| unmappedstatus | `"captured"` (success) or `"bounced"` (failure) | Final payment status           |


#### Payload for S2S UPI Intent
Ensure these URLs are configured in PayU's system:

\- `partner_webhook_success` — Called on successful payment
\- `partner_webhook_failure` — Called on failed payment
\- `partner_webhook_cancelled` — Called when payment is cancelled

**Sample Success Webhook Payload:**

```json
{
  "key": "JPM7Fg",
  "txnid": "UPIINT20240315001",
  "mihpayid": "30478359672",
  "status": "success",
  "unmappedstatus": "captured",
  "mode": "UPI",
  "bankcode": "INTENT",
  "amount": "500.00",
  "productinfo": "UPI Payment for Order #12345",
  "firstname": "Rajesh",
  "email": "rajesh@example.com",
  "phone": "919876543210",
  "udf1": "",
  "udf2": "",
  "udf3": "",
  "udf4": "",
  "udf5": "partner_channel_001",
  "merchant_id": "8739528",
  "error": "No Error",
  "error_Message": "No Error",
  "hash": "webhook_hash_from_payu"
}
```

**UPI Intent-Specific Fields:**

| Field            | Value for UPI Intent                           |
| ---------------- | ---------------------------------------------- |
| `mode`           | `"UPI"`                                        |
| `bankcode`       | `"INTENT"`                                     |
| `unmappedstatus` | `"captured"` (success) or `"failed"` (failure) |

<Info>
**Note on txnStatus "pending":**

The initial API response shows `txnStatus: "pending"`. The webhook is sent only after the customer completes the UPI authentication. Do NOT rely on polling — always use the webhook for final status updates.
</Info>


##### Payload for S2S UPI TPV
**Sample Success Webhook Payload (UPI TPV):**

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

### S

### Step 2: Verify Webhook Hash

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

### Step 3: Process Webhook

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
