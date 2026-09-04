---
title: Partner Payment Links UPI Intent Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
Create shareable payment links that launch the customer's UPI app directly using UPI Intent flow. This provides a seamless payment experience without redirecting to PayU's hosted page.

## How it works?

1. **Authentication** — Generate OAuth access token with `partner_payment_links` scope
2. **Create Payment Link** — Call Partner Payments API with `txn_s2s_flow=4` and S2S parameters
3. **Customer Payment** — Customer opens link, UPI app launches, payment completes
4. **Webhook Notification** — Receive real-time payment status update
5. **Verification** — Verify payment status using verify payment API

## Prerequisites

<Note>
✅ OAuth access token with `partner_payment_links` scope  
✅ Partner and merchant registered with PayU  
✅ Webhook URLs configured in `partner_webhook_urls` table  
✅ Customer device with UPI app installed
</Note>

***

## Step 1: Generate OAuth Access Token

You must obtain an OAuth access token with the `partner_payment_links` scope before creating payment links.

### OAuth Scopes Required

When requesting the authorization code (Step 2 of OAuth flow), include these scopes:

```
create_payment_links partner_payment_links partner_payments
```

**Authorization Code Request Example:**

```bash
curl --location 'https://uat-partner.payu.in/api/v1/merchants/auth_code' \
--header 'Authorization: Bearer <ACCESS_TOKEN_FROM_STEP_1>' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'merchant_id=8739528' \
--data-urlencode 'reseller_uuid=11ee-0e7e-5403fde2-9523-0a696b110fde' \
--data-urlencode 'redirect_uri=https://uat-partner.payu.in' \
--data-urlencode 'scopes=create_payment_links partner_payment_links partner_payments'
```

<Info>
For the complete OAuth token generation flow, refer to [Partner Payments Integration Guide - Step 1](doc:partner-payments-integration-guide#step-1-generate-oauth-access-token).
</Info>

***

## Step 2: Create Payment Link

### Step 2.1: Prepare the Request Parameters

Collect the required payment details and S2S parameters for UPI Intent:

**Endpoint:** `POST /partner/payments`

**Environment URLs:**

| Environment | URL                                                              |
| ----------- | ---------------------------------------------------------------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer/partner/payments` |
| Production  | `https://api.payu.in/partner/payments`                           |

**Mandatory Parameters:**

<table>
<thead>
<tr>
<th align="left">Parameter</th>
<th align="left">Type &amp; Description</th>
<th align="left">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>txnid</code></td>
<td>string — Unique transaction ID</td>
<td>UPIPL28471834809170985</td>
</tr>
<tr>
<td><code>amount</code></td>
<td>string — Payment amount</td>
<td>500.00</td>
</tr>
<tr>
<td><code>productinfo</code></td>
<td>string — Product description</td>
<td>UPI Payment for Order #12345</td>
</tr>
<tr>
<td><code>phone</code></td>
<td>string — Customer phone number (10 digits)</td>
<td>919876543210</td>
</tr>
<tr>
<td><code>merchant_id</code></td>
<td>integer — PayU merchant ID</td>
<td>8739528</td>
</tr>
<tr>
<td><code>reseller_id</code></td>
<td>string — Partner/reseller UUID</td>
<td>11ee-0e7e-5403fde2-9523-0a696b110fde</td>
</tr>
<tr>
<td><code>txn_s2s_flow</code></td>
<td>string — Must be "4" for UPI Intent</td>
<td>4</td>
</tr>
<tr>
<td><code>s2s_client_ip</code></td>
<td>string — Customer IP address (mandatory)</td>
<td>157.240.22.9</td>
</tr>
<tr>
<td><code>s2s_device_info</code></td>
<td>string — Device user-agent (mandatory)</td>
<td>Mozilla/5.0 (Linux; Android 10)</td>
</tr>
<tr>
<td><code>hash</code></td>
<td>string — SHA-512 hash</td>
<td>(computed hash)</td>
</tr>
</tbody>
</table>

<Warning>
**Mandatory S2S Fields:** When `txn_s2s_flow=4`, both `s2s_client_ip` and `s2s_device_info` are **required**. Omitting them will cause an error: *"s2s_client_ip or s2s_device_info mandatory"*.
</Warning>

**Optional Parameters:**

| Parameter            | Type & Description                                                                  | Example                                           |
| -------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------- |
| `firstname`, `email` | string — Customer details                                                           | Amit, [amit@example.com](mailto:amit@example.com) |
| `udf1` - `udf5`      | string — Custom tracking fields (use to track payment source, campaign codes, etc.) | udf5: whatsapp                                    |

***

### Step 2.2: Generate Payment Request Hash

Compute the SHA-512 hash using this exact formula:

```
merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||client_secret
```

<Warning>
**Important Hash Notes:**
- There are **six consecutive pipe characters** (`||||||`) between `udf5` and `client_secret`
- Use your OAuth `client_secret`, **not** the merchant salt
- For empty fields (firstname, email, udf1-udf5), use empty strings (resulting in consecutive pipes)
- Compute SHA-512 and convert to **lowercase hexadecimal**
</Warning>

**Hash Generation Example (Python):**

```python
import hashlib

def generate_payment_hash(merchant_id, txnid, amount, productinfo, client_secret):
    # All optional fields empty
    hash_string = f"{merchant_id}|{txnid}|{amount}|{productinfo}|||||||||||{client_secret}"
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
```

***

### Step 2.3: POST the Payment Request

Call the Partner Payments endpoint with the computed hash and all required parameters.

**Request Headers:**

```
Authorization: Bearer <FINAL_ACCESS_TOKEN>
Content-Type: application/json
```

**Sample Request:**

```bash
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payments' \
--header 'Authorization: Bearer 039e0d1d70f467f946e2d73bd43868df856cfaa352ea54591a76bfc4a08d3487' \
--header 'Content-Type: application/json' \
--data '{
  "txnid": "UPIPL28471834809170985",
  "amount": "500.00",
  "productinfo": "UPI Payment for Order #12345",
  "phone": "919876543210",
  "merchant_id": 8739528,
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "txn_s2s_flow": "4",
  "s2s_client_ip": "157.240.22.9",
  "s2s_device_info": "Mozilla/5.0 (Linux; Android 10)",
  "hash": "a3f5e8d2c1b4a6e9f7d3c8b2a1e4d6f9c3a5b7e2d1f4c6a8b3e5d2f7c1a9b4e6"
}'
```

```python
import requests
import hashlib
import time

def create_upi_intent_payment_link(phone, amount, description, client_ip, device_info):
    url = "https://test-partnerapilayer.payu.in/apilayer/partner/payments"
    
    txnid = f"UPIPL{int(time.time() * 1000)}"
    merchant_id = 8739528
    
    # Compute hash (all optional fields empty)
    hash_string = f"{merchant_id}|{txnid}|{amount}|{description}|||||||||||YOUR_CLIENT_SECRET"
    payment_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
    
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/json"
    }
    
    payload = {
        "txnid": txnid,
        "amount": amount,
        "productinfo": description,
        "phone": phone,
        "merchant_id": merchant_id,
        "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
        "txn_s2s_flow": "4",
        "s2s_client_ip": client_ip,
        "s2s_device_info": device_info,
        "hash": payment_hash
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# Usage
result = create_upi_intent_payment_link(
    phone="919876543210",
    amount="500.00",
    description="UPI Payment for Order #12345",
    client_ip="157.240.22.9",
    device_info="Mozilla/5.0 (Linux; Android 10)"
)

print(f"Payment Link: {result.get('redirectUri')}")
```

> **Note:** Replace `YOUR_CLIENT_SECRET` and `YOUR_ACCESS_TOKEN` with actual values.

***

### Step 2.4: Handle Payment Response

The response contains the payment link URL.

**Sample Response:**

```json
{
  "redirectUri": "https://secure.payu.in/_payment?mihpayid=403993715521855096&amount=500.00&txnid=UPIPL28471834809170985&key=JPM7Fg&productinfo=UPI+Payment+for+Order+%2312345&phone=919876543210&txn_s2s_flow=4..."
}
```

**Response Parameters:**

| Parameter     | Type   | Description                                                                          |
| ------------- | ------ | ------------------------------------------------------------------------------------ |
| `redirectUri` | string | **Payment link URL** — Share this URL with your customer via WhatsApp, SMS, or email |

**Customer Experience:**

When the customer opens the `redirectUri`:

1. PayU UPI Intent page loads
2. System detects installed UPI apps
3. Customer selects preferred UPI app (Google Pay, PhonePe, Paytm, etc.)
4. UPI app opens with pre-filled payment details
5. Customer enters UPI PIN
6. Payment is processed

<Note>
After initiating the payment, PayU will send a webhook to your configured partner webhook URL once the customer completes or cancels the payment. See Step 3 for webhook handling.
</Note>

***

## Step 3: Receive Payment Notification

After the customer completes payment, PayU sends notifications via webhooks.

### Step 3.1: Partner Webhook

PayU sends a webhook to your configured partner webhook URL:

**Sample Webhook Payload:**

```json
{
  "txnid": "UPIPL28471834809170985",
  "mihpayid": "30478359672",
  "status": "success",
  "unmappedstatus": "captured",
  "mode": "UPI",
  "bankcode": "INTENT",
  "amount": "500.00",
  "phone": "919876543210",
  "productinfo": "UPI Payment for Order #12345",
  "hash": "WEBHOOK_HASH"
}
```

**Key Indicators for UPI Intent:**

- `mode`: "UPI"
- `bankcode`: "INTENT"

***

### Step 3.2: Verify Webhook Hash (Reverse Hash)

**Always verify** the webhook hash before processing. Use the **reverse hash formula**:

```
client_secret|status|||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|merchant_id
```

<Warning>
**Reverse Hash Notes:**
- There are **five consecutive pipe characters** (`|||||`) between `status` and `udf5`
- The field order is **reversed** compared to the payment request hash
- Use your OAuth `client_secret`, **not** the merchant salt
- **Do not** include a trailing pipe after `merchant_id`
- Compute SHA-512 and compare **case-insensitively** with the `hash` field
</Warning>

**Webhook Verification Code (Python):**

```python
import hashlib

def verify_webhook_hash(payload, client_secret):
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
    
    expected_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
    return expected_hash.lower() == payload.get('hash', '').lower()

# Usage
if verify_webhook_hash(webhook_payload, YOUR_CLIENT_SECRET):
    print("✅ Webhook verified")
    # Process payment
else:
    print("❌ Invalid webhook - discarding")
```

For complete webhook verification code, see [Partner Webhook API](ref:partner-webhook-api).

***

### Step 3.3: Process Webhook

After verifying the hash, process the payment notification:

```python
from flask import request, jsonify

@app.route('/webhook/payment/success', methods=['POST'])
def webhook_handler():
    payload = request.get_json() or request.form.to_dict()
    
    # Verify webhook hash
    if not verify_webhook_hash(payload, CLIENT_SECRET):
        return jsonify({"error": "Invalid hash"}), 400
    
    # Extract payment details
    txnid = payload['txnid']
    status = payload['status']
    mihpayid = payload['mihpayid']
    
    # Update database
    update_payment_status(txnid, status, mihpayid)
    
    # Always return 200
    return jsonify({"status": "received"}), 200
```

<Success>
**Best Practice:** Always respond with HTTP 200 to acknowledge webhook receipt. Process payments asynchronously to avoid blocking the webhook response.
</Success>

***

## Step 4: Verify Payment

After receiving the webhook, call the Verify Payment API to confirm the final transaction status.

### Step 4.1: Generate Verify Payment Hash

Compute the SHA-512 hash using this formula:

```
merchant_id|verify_payment|txnid|client_secret
```

**Example:**

```
8739528|verify_payment|UPIPL28471834809170985|YOUR_CLIENT_SECRET
```

***

### Step 4.2: Call Verify Payment API

**Endpoint:** `POST /partner/verifyPayment`

**Environment URLs:**

| Environment | URL                                                                   |
| ----------- | --------------------------------------------------------------------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment` |
| Production  | `https://api.payu.in/partner/verifyPayment`                           |

**Sample Request:**

```bash
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment' \
--header 'Authorization: Bearer 039e0d1d70f467f946e2d73bd43868df856cfaa352ea54591a76bfc4a08d3487' \
--header 'Content-Type: application/json' \
--data '{
  "txnid": "UPIPL28471834809170985",
  "merchant_id": 8739528,
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "hash": "f3a8d2e5c1b7a4e9d6c3b8a2e1f4d7c9b3a6e2d1f5c4a7b8e3d6f2c1a9b5e4d7"
}'
```

```python
import hashlib
import requests

def verify_upi_payment(txnid):
    url = "https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment"
    
    merchant_id = 8739528
    hash_string = f"{merchant_id}|verify_payment|{txnid}|YOUR_CLIENT_SECRET"
    verify_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
    
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/json"
    }
    
    payload = {
        "txnid": txnid,
        "merchant_id": merchant_id,
        "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
        "hash": verify_hash
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()
```

***

### Step 4.3: Process Verification Response

**Sample Response:**

```json
{
  "status": "success",
  "unmappedstatus": "captured",
  "mihpayid": "30478359672",
  "txnid": "UPIPL28471834809170985",
  "amount": "500.00",
  "mode": "UPI",
  "bankcode": "INTENT"
}
```

**Reconciliation Steps:**

1. Compare `mihpayid` from verify response with webhook payload
2. Compare `status` and `unmappedstatus` values
3. Verify `txnid` matches your original transaction ID
4. Check `amount` matches the payment amount
5. If all match, mark the payment as verified in your system

<Success>
**Integration Complete!** You've successfully created a UPI Intent payment link, received webhook notification, and verified the payment status.
</Success>

***

## Use Cases

### WhatsApp Commerce

Send payment links directly in WhatsApp conversations:

```python
# Create payment link
link_response = create_upi_intent_payment_link(
    phone="919876543210",
    amount="500.00",
    description="Order #12345",
    client_ip=get_client_ip(),
    device_info=get_device_info()
)

# Send via WhatsApp
message = f"""Hi! Your order is confirmed.

Amount: Rs. 500.00
Pay with UPI: {link_response['redirectUri']}

Your UPI app will open automatically.
"""
send_whatsapp_message("919876543210", message)
```

### Invoice Payments

```python
invoice = get_invoice(invoice_id)

link_response = create_upi_intent_payment_link(
    phone=invoice.customer_phone,
    amount=str(invoice.total),
    description=f"Invoice #{invoice.number}",
    client_ip=request.remote_addr,
    device_info=request.headers.get('User-Agent')
)

send_sms(invoice.customer_phone, f"Pay invoice via UPI: {link_response['redirectUri']}")
```

***

## Error Handling

| Error                                      | Cause                    | Resolution                            |
| ------------------------------------------ | ------------------------ | ------------------------------------- |
| s2s_client_ip or s2s_device_info mandatory | Missing S2S fields       | Include both fields in request        |
| Invalid hash                               | Hash validation failed   | Verify hash formula and client_secret |
| No UPI app installed                       | Customer has no UPI app  | Provide alternate payment method      |
| Auth token is not valid                    | Token expired or invalid | Regenerate OAuth token                |

***

## Testing

### Test Environment

- **API URL:** `https://test-partnerapilayer.payu.in/apilayer/partner/payments`
- **OAuth URL:** `https://uat-accounts.payu.in/oauth/token`

### Test UPI

- **UPI ID:** `success@payu` (for successful test)
- **UPI Intent:** Use any UPI app in test mode

### Test Workflow

1. Create UPI Intent payment link in UAT
2. Open link on mobile device
3. Select UPI app
4. Complete test payment
5. Verify webhook received
6. Call verify payment API
7. Confirm status matches

***

## Best Practices

✅ **Capture Real Device Info** — Get actual device user-agent from HTTP headers<br />✅ **Capture Client IP** — Extract from `X-Forwarded-For` or request IP<br />✅ **Mobile-First** — UPI Intent works best on mobile devices<br />✅ **Handle Expiry** — Implement token refresh logic<br />✅ **Idempotency** — Check if link already exists before creating new one

***

## Next Steps

- [Payment Links for UPI TPV](doc:payment-links-upi-tpv) — TPV validation for payment links
- [Payment Links with Hosted Checkout](doc:payment-links-hosted-checkout) — Multi-method payment links
- [Partner Webhook API](ref:partner-webhook-api) — Complete webhook verification guide

<Success>
**UPI Intent Payment Links Ready!** Your customers can now pay directly from their UPI apps with a seamless one-click experience.
</Success>
