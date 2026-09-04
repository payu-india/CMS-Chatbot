---
title: Partner Payment Links UPI TPV Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
Create shareable payment links with UPI Third-Party Validation (TPV) to ensure payments are made from verified beneficiary accounts. This is essential for compliance scenarios where beneficiary validation is required.

## How it works?

1. **Authentication** — Generate OAuth access token with `partner_payment_links` scope
2. **Create Payment Link** — Call Partner Payments API with `beneficiarydetail` and S2S parameters
3. **Customer Payment** — Customer opens link, account is validated, payment completes
4. **Webhook Notification** — Receive payment status with TPV indicators
5. **Verification** — Verify payment using verify payment API

## Prerequisites

<Note>
✅ OAuth access token with `partner_payment_links` scope  
✅ Beneficiary bank account details (IFSC, account number, account holder name)  
✅ Webhook URLs configured  
✅ UPI S2S integration enabled
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

Collect the required payment details, beneficiary information, and S2S parameters:

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
<td>TPVPL28471834809170986</td>
</tr>
<tr>
<td><code>amount</code></td>
<td>string — Payment amount</td>
<td>1000.00</td>
</tr>
<tr>
<td><code>productinfo</code></td>
<td>string — Product description</td>
<td>TPV Payment for Invoice #INV456</td>
</tr>
<tr>
<td><code>phone</code></td>
<td>string — Customer phone number</td>
<td>919876543210</td>
</tr>
<tr>
<td><code>merchant_id</code></td>
<td>integer — PayU merchant ID</td>
<td>8739528</td>
</tr>
<tr>
<td><code>reseller_id</code></td>
<td>string — Partner UUID</td>
<td>11ee-0e7e-5403fde2-9523-0a696b110fde</td>
</tr>
<tr>
<td><code>txn_s2s_flow</code></td>
<td>string — Must be "4" for UPI S2S TPV</td>
<td>4</td>
</tr>
<tr>
<td><code>s2s_client_ip</code></td>
<td>string — Customer IP (mandatory)</td>
<td>157.240.22.9</td>
</tr>
<tr>
<td><code>s2s_device_info</code></td>
<td>string — Device user-agent (mandatory)</td>
<td>Mozilla/5.0 (Linux; Android 10)</td>
</tr>
<tr>
<td><code>beneficiarydetail</code></td>
<td>string — JSON with beneficiary details</td>
<td>{"ifscCode":"ICIC0001234",...}</td>
</tr>
<tr>
<td><code>hash</code></td>
<td>string — SHA-512 hash</td>
<td>(computed hash)</td>
</tr>
</tbody>
</table>

<Info>
When `beneficiarydetail` is included with `txn_s2s_flow=4`, PayU automatically sets:
- `bankcode=INTTPV`
- `api_version=6`
</Info>

**Optional Parameters:**

| Parameter            | Type & Description                        | Example                                              |
| -------------------- | ----------------------------------------- | ---------------------------------------------------- |
| `firstname`, `email` | string — Customer details                 | Priya, [priya@example.com](mailto:priya@example.com) |
| `udf1` - `udf5`      | string — Custom tracking fields           | udf3: loan_ref_12345                                 |
| `encrypted_data`     | string — Alternative to beneficiarydetail | (encrypted string)                                   |

### Beneficiary Detail Schema

The `beneficiarydetail` parameter must be a JSON string:

```json
{
  "ifscCode": "ICIC0001234",
  "accountNumber": "123456789012",
  "accountHolderName": "Priya Sharma"
}
```

| Field               | Type   | Description                 |
| ------------------- | ------ | --------------------------- |
| `ifscCode`          | string | 11-character bank IFSC code |
| `accountNumber`     | string | Beneficiary account number  |
| `accountHolderName` | string | Name as per bank records    |

<Warning>
**TPV Validation:** The account number used by the customer in their UPI app must match the `accountNumber` in `beneficiarydetail`. Mismatches will cause payment rejection.
</Warning>

> **⚠️ Info Gap:** The exact field validations and constraints for `beneficiarydetail` should be confirmed with the PayU integration team.

***

### Step 2.2: Generate Payment Request Hash

Compute the SHA-512 hash using this exact formula:

```
merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||client_secret
```

<Info>
**Note:** The `beneficiarydetail` field is **not included** in the hash formula. Only the standard payment fields are used for hash computation.
</Info>

<Warning>
**Important:**
- Six consecutive pipe characters (`||||||`) between `udf5` and `client_secret`
- Use OAuth `client_secret`, **not** merchant salt
- For empty fields, use empty strings (resulting in consecutive pipes)
- Compute SHA-512 and convert to lowercase hexadecimal
</Warning>

**Hash Generation Example (Python):**

```python
import hashlib

def generate_tpv_payment_hash(merchant_id, txnid, amount, productinfo, client_secret):
    # All optional fields empty (beneficiarydetail NOT in hash)
    hash_string = f"{merchant_id}|{txnid}|{amount}|{productinfo}|||||||||||{client_secret}"
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
```

***

### Step 2.3: POST the Payment Request

Call the Partner Payments endpoint with beneficiary details, S2S parameters, and computed hash.

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
  "txnid": "TPVPL28471834809170986",
  "amount": "1000.00",
  "productinfo": "TPV Payment for Invoice #INV456",
  "phone": "919876543210",
  "merchant_id": 8739528,
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "txn_s2s_flow": "4",
  "s2s_client_ip": "157.240.22.9",
  "s2s_device_info": "Mozilla/5.0 (Linux; Android 10)",
  "beneficiarydetail": "{\"ifscCode\":\"ICIC0001234\",\"accountNumber\":\"123456789012\",\"accountHolderName\":\"Priya Sharma\"}",
  "hash": "b8f3a5d2e1c7b4a9e6d3c8b1a2f4e7d9c3b6a2e1d5f4c7a8b3e6d2f1c9a5b4e7"
}'
```

```python
import requests
import hashlib
import json
import time

def create_upi_tpv_payment_link(phone, amount, description, beneficiary_details, 
                                client_ip, device_info):
    url = "https://test-partnerapilayer.payu.in/apilayer/partner/payments"
    
    txnid = f"TPVPL{int(time.time() * 1000)}"
    merchant_id = 8739528
    
    # Prepare beneficiary JSON
    beneficiary_json = json.dumps(beneficiary_details)
    
    # Compute hash (beneficiarydetail NOT in hash, all optional fields empty)
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
        "beneficiarydetail": beneficiary_json,
        "hash": payment_hash
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# Usage
beneficiary = {
    "ifscCode": "ICIC0001234",
    "accountNumber": "123456789012",
    "accountHolderName": "Priya Sharma"
}

result = create_upi_tpv_payment_link(
    phone="919876543210",
    amount="1000.00",
    description="TPV Payment for Invoice #INV456",
    beneficiary_details=beneficiary,
    client_ip="157.240.22.9",
    device_info="Mozilla/5.0 (Linux; Android 10)"
)

print(f"Payment Link: {result.get('redirectUri')}")
```

> **Note:** In the cURL example, the JSON string `beneficiarydetail` has escaped quotes (`\"`) to be valid within the outer JSON payload.

***

### Step 2.4: Handle Payment Response

The response contains the payment link URL.

**Sample Response:**

```json
{
  "redirectUri": "https://secure.payu.in/_payment?mihpayid=403993715521855097&amount=1000.00&txnid=TPVPL28471834809170986&key=JPM7Fg&productinfo=TPV+Payment+for+Invoice+%23INV456&phone=919876543210&txn_s2s_flow=4..."
}
```

**Response Parameters:**

| Parameter     | Type   | Description                                              |
| ------------- | ------ | -------------------------------------------------------- |
| `redirectUri` | string | **Payment link URL** — Share this URL with your customer |

**Customer Experience with TPV:**

1. **Link Opens** → PayU TPV payment page loads
2. **Beneficiary Info Display** → Shows registered account details
3. **UPI App Selection** → Customer chooses UPI app
4. **Account Verification** → PayU validates UPI account against beneficiary details
5. **Payment Authorization** → If validated, customer enters UPI PIN
6. **Completion** → Payment processed

**Validation Logic:**

```
Customer's UPI Account Number == beneficiarydetail.accountNumber
  ✅ YES → Payment proceeds
  ❌ NO  → Payment rejected with error
```

<Note>
After initiating the payment, PayU will send a webhook to your configured partner webhook URL once the customer completes or cancels the payment. See Step 3 for webhook handling.
</Note>

***

## Step 3: Receive Payment Notification

After the customer completes payment, PayU sends notifications via webhooks.

### Step 3.1: Partner Webhook

PayU sends a webhook to your configured partner webhook URL with TPV indicators:

**Sample Webhook Payload:**

```json
{
  "txnid": "TPVPL28471834809170986",
  "mihpayid": "30478359673",
  "status": "success",
  "unmappedstatus": "captured",
  "mode": "UPI",
  "bankcode": "INTTPV",
  "amount": "1000.00",
  "phone": "919876543210",
  "productinfo": "TPV Payment for Invoice #INV456",
  "hash": "WEBHOOK_HASH"
}
```

**TPV Indicators:**

- `mode`: "UPI"
- `bankcode`: "INTTPV" (automatically set by PayU)

***

### Step 3.2: Verify Webhook Hash (Reverse Hash)

**Always verify** the webhook hash before processing. Use the **reverse hash formula**:

```
client_secret|status|||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|merchant_id
```

<Warning>
**Reverse Hash Notes:**
- Five consecutive pipe characters (`|||||`) between `status` and `udf5`
- Field order is **reversed** from payment request hash
- Use OAuth `client_secret`
- No trailing pipe after `merchant_id`
- Compare case-insensitively
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
    print("✅ TPV Webhook verified")
    # Process payment
else:
    print("❌ Invalid webhook")
```

For complete webhook verification code, see [Partner Webhook API](ref:partner-webhook-api).

***

### Step 3.3: Process Webhook

After verifying the hash, process the TPV payment notification:

```python
from flask import request, jsonify

@app.route('/webhook/payment/success', methods=['POST'])
def webhook_handler():
    payload = request.get_json() or request.form.to_dict()
    
    # Verify webhook hash
    if not verify_webhook_hash(payload, CLIENT_SECRET):
        return jsonify({"error": "Invalid hash"}), 400
    
    # Check TPV indicator
    if payload.get('bankcode') == 'INTTPV':
        print("TPV payment received")
    
    # Update database
    update_payment_status(
        txnid=payload['txnid'],
        status=payload['status'],
        mihpayid=payload['mihpayid'],
        bankcode=payload['bankcode']
    )
    
    # Always return 200
    return jsonify({"status": "received"}), 200
```

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
8739528|verify_payment|TPVPL28471834809170986|YOUR_CLIENT_SECRET
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
  "txnid": "TPVPL28471834809170986",
  "merchant_id": 8739528,
  "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
  "hash": "f3a8d2e5c1b7a4e9d6c3b8a2e1f4d7c9b3a6e2d1f5c4a7b8e3d6f2c1a9b5e4d7"
}'
```

```python
import hashlib
import requests

def verify_tpv_payment(txnid):
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
  "mihpayid": "30478359673",
  "txnid": "TPVPL28471834809170986",
  "amount": "1000.00",
  "mode": "UPI",
  "bankcode": "INTTPV"
}
```

**Reconciliation Steps:**

1. Compare `mihpayid` with webhook payload
2. Verify `bankcode=INTTPV` confirming TPV validation occurred
3. Check `status` and `unmappedstatus` match
4. Confirm `amount` is correct
5. Mark payment as verified in your system

<Success>
**Integration Complete!** You've successfully created a UPI TPV payment link with beneficiary validation, received webhook notification, and verified the payment status.
</Success>

***

## Use Cases

### 1. Loan Repayments

Ensure loan repayment comes from borrower's registered account:

```python
loan = get_loan_details(loan_id)

beneficiary = {
    "ifscCode": loan.borrower_ifsc,
    "accountNumber": loan.borrower_account,
    "accountHolderName": loan.borrower_name
}

link = create_upi_tpv_payment_link(
    phone=loan.borrower_phone,
    amount=str(loan.emi_amount),
    description=f"EMI Payment - Loan #{loan.loan_id}",
    beneficiary_details=beneficiary,
    client_ip=get_client_ip(),
    device_info=get_device_info()
)

# Send link via SMS
send_sms(loan.borrower_phone, f"Pay EMI: {link['redirectUri']}")
```

### 2. Vendor Payments

Verify vendor payments come from registered business account:

```python
vendor = get_vendor(vendor_id)
invoice = get_invoice(invoice_id)

beneficiary = {
    "ifscCode": vendor.bank_ifsc,
    "accountNumber": vendor.bank_account,
    "accountHolderName": vendor.legal_name
}

link = create_upi_tpv_payment_link(
    phone=vendor.contact_phone,
    amount=str(invoice.amount),
    description=f"Payment for Invoice #{invoice.number}",
    beneficiary_details=beneficiary,
    client_ip=request.remote_addr,
    device_info=request.headers.get('User-Agent')
)

# Send link via email
send_email(vendor.email, f"Invoice Payment Link", link['redirectUri'])
```

### 3. Refund Collections

Collect refunds to the original payment account:

```python
original_payment = get_payment(payment_id)

beneficiary = {
    "ifscCode": original_payment.customer_ifsc,
    "accountNumber": original_payment.customer_account,
    "accountHolderName": original_payment.customer_name
}

link = create_upi_tpv_payment_link(
    phone=original_payment.customer_phone,
    amount=str(original_payment.refund_amount),
    description="Refund Collection",
    beneficiary_details=beneficiary,
    client_ip=get_client_ip(),
    device_info=get_device_info()
)
```

***

## Error Handling

| Error                            | Cause                                       | Resolution                               |
| -------------------------------- | ------------------------------------------- | ---------------------------------------- |
| Beneficiary account mismatch     | UPI account doesn't match beneficiarydetail | Instruct customer to use correct account |
| Invalid beneficiarydetail format | Malformed JSON                              | Validate JSON before sending             |
| IFSC code invalid                | Non-existent IFSC                           | Verify against RBI master list           |
| Missing TPV fields               | beneficiarydetail not provided              | Include beneficiary details in request   |

***

## Testing

### Test Environment

- **API URL:** `https://test-partnerapilayer.payu.in/apilayer/partner/payments`
- **OAuth URL:** `https://uat-accounts.payu.in/oauth/token`

### Test Beneficiary Details

> **⚠️ Info Gap:** Test IFSC codes and account numbers for UAT should be obtained from PayU integration team.

**Sample Test Data (to be confirmed):**

```json
{
  "ifscCode": "ICIC0001234",
  "accountNumber": "123456789012",
  "accountHolderName": "Test User"
}
```

### Test Workflow

1. Create TPV payment link with test beneficiary details
2. Open link on mobile device
3. Select UPI app
4. Use UPI account matching beneficiary details
5. Complete test payment
6. Verify webhook with `bankcode=INTTPV`
7. Call verify payment API
8. Confirm TPV validation succeeded

***

## Best Practices

✅ **Validate Beneficiary Data** — Verify IFSC and account number before creating link<br />✅ **Clear Communication** — Inform customer about account verification requirement<br />✅ **Handle Mismatches Gracefully** — Provide clear error messages and support contact<br />✅ **Log TPV Transactions** — Track TPV validations for compliance reporting<br />✅ **Test Thoroughly** — Test both success and failure scenarios

***

## Next Steps

- [Payment Links for UPI Intent](doc:payment-links-upi-intent) — Standard UPI Intent links
- [Payment Links with Hosted Checkout](doc:payment-links-hosted-checkout) — Multi-method payment links
- [Partner Webhook API](ref:partner-webhook-api) — Complete webhook verification guide

<Success>
**UPI TPV Payment Links Ready!** Ensure compliant payments with automatic beneficiary account validation.
</Success>
