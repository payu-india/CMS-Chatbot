---
title: Testing and Troubleshooting Partner Integration
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
This guide provides comprehensive testing procedures, common error resolutions, debugging techniques, and test data for all Partner Payments integration methods: Hosted Checkout, UPI Intent, and UPI TPV.

***

## Testing Overview by Integration Method

Before diving into specific tests, understand which testing steps apply to your integration:

| Test Category            | Hosted Checkout    | UPI Intent    | UPI TPV                        |
| ------------------------ | ------------------ | ------------- | ------------------------------ |
| OAuth Token Generation   | ✅                  | ✅             | ✅                              |
| Hash Generation          | ✅                  | ✅             | ✅ (beneficiarydetail excluded) |
| S2S Flow Parameters      | ❌                  | ✅ (mandatory) | ✅ (mandatory)                  |
| Beneficiary Validation   | ❌                  | ❌             | ✅ (mandatory)                  |
| Redirect URL Handling    | ✅ (surl/furl/curl) | ⚠️ (optional) | ⚠️ (optional)                  |
| intentURIData Validation | ❌                  | ✅             | ✅                              |
| Webhook Verification     | ✅                  | ✅             | ✅ (bankcode=INTTPV)            |
| Payment Verification API | ✅                  | ✅             | ✅                              |

***

## Step 1: Pre-Integration Validation

### 1.1 Verify OAuth Credentials

<Note>
Complete this step before initiating any payment flow.
</Note>

**Test:** Generate OAuth access token using the 3-step flow

**Expected Result:**

- Step 1 (Reseller Password Grant): Returns `access_token` with `scope=hub_session`
- Step 2 (Merchant Authorization Code): Returns `authorization_code`
- Step 3 (Code Exchange): Returns final `access_token` with scopes `create_payment_links partner_payment_links partner_payments`

**Validation Checklist:**

- [ ] All three OAuth steps complete successfully
- [ ] Final access token contains all required scopes
- [ ] Token expiry time (`expires_in`) is typically 3600 seconds
- [ ] Token is cached and reused until expiry

**Common Failures:** See [Error: Auth token is not valid](#error-auth-token-is-not-valid) below

***

### 1.2 Verify Hash Generation

<Warning>
Partner Payments hash uses **OAuth `client_secret`**, NOT merchant salt.
</Warning>

**Hash Formula (Standard Payment):**

```
merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||client_secret
```

**Note:** Six consecutive pipes (`||||||`) between `udf5` and `client_secret`

**Hash Formula (UPI TPV):**

```
merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||client_secret
```

**Important:** `beneficiarydetail` is **NOT** included in hash calculation

**Test:** Compute hash for a sample transaction

**Sample Hash String (Standard):**

```
8739528|TXN20240315123456|518.02|Payment for service|John|john@example.com|||||||||YOUR_CLIENT_SECRET
```

**Expected Output:**

- SHA-512 hash: 128-character lowercase hexadecimal string
- Example: `a1b2c3d4e5f6...` (128 chars)

**Validation Checklist:**

- [ ] Hash function uses SHA-512
- [ ] Output is lowercase hexadecimal
- [ ] Empty fields result in consecutive pipes (e.g., `||`)
- [ ] client_secret is used (not merchant salt)
- [ ] beneficiarydetail excluded from hash (UPI TPV only)

**Debug Example (Python):**

```python
import hashlib

merchant_id = "8739528"
txnid = "TXN20240315123456"
amount = "518.02"
productinfo = "Payment for service"
firstname = "John"
email = "john@example.com"
udf1 = udf2 = udf3 = udf4 = udf5 = ""
client_secret = "YOUR_CLIENT_SECRET"

hash_string = f"{merchant_id}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{client_secret}"
print(f"Hash String: {hash_string}")

hash_value = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
print(f"Computed Hash: {hash_value}")
print(f"Hash Length: {len(hash_value)}")  # Should be 128
```

**Common Failures:** See [Error: Invalid hash](#error-invalid-hash) below

***

## Step 2: Test Each Integration Method

### 2.1 Hosted Checkout Testing

<details>
<summary><strong>2.1.1: Initiate Hosted Checkout Payment</strong></summary>

**Endpoint:** `POST https://test-partnerapilayer.payu.in/payment`

**Test Payload:**

```json
{
  "merchant_id": "8739528",
  "reseller_id": "your-partner-uuid",
  "txnid": "HC_TEST_001",
  "amount": "100.00",
  "productinfo": "Test Product",
  "firstname": "Test",
  "email": "test@example.com",
  "phone": "9876543210",
  "surl": "https://yoursite.com/success",
  "furl": "https://yoursite.com/failure",
  "curl": "https://yoursite.com/cancel",
  "hash": "<computed_hash>"
}
```

**Expected Response:**

```json
{
  "status": "success",
  "redirectUri": "https://test.payu.in/checkout?token=abc123xyz...",
  "txnid": "HC_TEST_001"
}
```

**Validation Checklist:**

- [ ] API returns `200 OK` status
- [ ] Response contains `redirectUri`
- [ ] `txnid` in response matches request
- [ ] No `error` or `message` fields in response

</details>

<details>
<summary><strong>2.1.2: Complete Payment on Hosted Page</strong></summary>

**Test Steps:**

1. Open the `redirectUri` in a browser
2. Hosted checkout page loads with merchant branding
3. Select payment method (Card / UPI / Net Banking / Wallet)

**For Card Payment (Test Cards):**

| Card Number      | Expiry  | CVV | Name      | Expected Result |
| ---------------- | ------- | --- | --------- | --------------- |
| 5123456789012346 | 05/2026 | 123 | Test User | Success         |
| 4012001037141112 | 12/2025 | 123 | Test User | Success         |
| 6011111111111117 | 06/2027 | 999 | Test User | Failure         |

**For UPI Payment (Test UPI IDs):**

- `success@payu` — Success
- `failure@payu` — Failure

**Validation Checklist:**

- [ ] Hosted page displays correctly
- [ ] Payment method selection works
- [ ] Test payment completes
- [ ] Customer is redirected to `surl` (success) or `furl` (failure)

</details>

<details>
<summary><strong>2.1.3: Verify Redirect URL Parameters</strong></summary>

When customer is redirected to your `surl`/`furl`, PayU appends transaction details as POST parameters.

**Expected Parameters:**

```
mihpayid=<PayU_Transaction_ID>
txnid=HC_TEST_001
status=success
amount=100.00
productinfo=Test Product
firstname=Test
email=test@example.com
hash=<response_hash>
...
```

**Validation Checklist:**

- [ ] All expected parameters are present
- [ ] `txnid` matches original request
- [ ] `mihpayid` (PayU transaction ID) is present
- [ ] `status` is `success` or `failure`
- [ ] Response hash verification passes (see [Webhook Hash Verification](#webhook-hash-verification))

</details>

***

### 2.2 UPI Intent Testing

<details>
<summary><strong>2.2.1: Initiate UPI Intent Payment</strong></summary>

**Endpoint:** `POST https://test-partnerapilayer.payu.in/payment`

**Test Payload:**

```json
{
  "merchant_id": "8739528",
  "reseller_id": "your-partner-uuid",
  "txnid": "UPI_INTENT_001",
  "amount": "250.00",
  "productinfo": "UPI Test",
  "firstname": "Customer",
  "email": "customer@example.com",
  "phone": "9123456789",
  "txn_s2s_flow": "4",
  "s2s_client_ip": "192.168.1.100",
  "s2s_device_info": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36",
  "hash": "<computed_hash>"
}
```

**Expected Response:**

```json
{
  "status": "success",
  "txnid": "UPI_INTENT_001",
  "intentURIData": "upi://pay?pa=payu@icici&pn=PayU&tr=UPI_INTENT_001&am=250.00&cu=INR&tn=Payment..."
}
```

**Validation Checklist:**

- [ ] API returns `200 OK` status
- [ ] Response contains `intentURIData`
- [ ] `intentURIData` starts with `upi://pay?`
- [ ] Transaction amount and ID are present in URI
- [ ] No error messages in response

</details>

<details>
<summary><strong>2.2.2: Invoke UPI App</strong></summary>

**Test Steps (Android/iOS):**

1. **Parse intentURIData:** Extract the UPI deep link from API response

2. **Launch UPI App:**
   - Android: Use `Intent` with `ACTION_VIEW` and `intentURIData` as URI
   - iOS: Use `UIApplication.shared.open()` with the UPI URI

3. **Select UPI App:** System prompts customer to choose UPI app (Google Pay, PhonePe, BHIM, etc.)

4. **Authenticate:** Customer enters UPI PIN in the app

**Test UPI Apps:**

- Google Pay (recommended for testing)
- PhonePe
- BHIM UPI
- Paytm

**Validation Checklist:**

- [ ] UPI app opens automatically
- [ ] Payment details are pre-filled (amount, merchant name, transaction ID)
- [ ] Customer can complete payment
- [ ] UPI app shows success/failure message

</details>

<details>
<summary><strong>2.2.3: Simulate Success and Failure Transactions</strong></summary>

**Success Scenario:**

- Use a test UPI account registered with PayU sandbox
- Complete payment with correct UPI PIN
- Expected webhook: `status=success`, `mode=UPI`

**Failure Scenario:**

- Use an invalid UPI PIN
- OR decline payment in UPI app
- Expected webhook: `status=failure`

**Validation Checklist:**

- [ ] Success transaction triggers success webhook
- [ ] Failure transaction triggers failure webhook
- [ ] Webhook arrives within 5–10 seconds
- [ ] Webhook contains correct `txnid` and `mihpayid`

</details>

***

### 2.3 UPI TPV Testing

<details>
<summary><strong>2.3.1: Initiate UPI TPV Payment</strong></summary>

**Endpoint:** `POST https://test-partnerapilayer.payu.in/payment`

**Test Payload:**

```json
{
  "merchant_id": "8739528",
  "reseller_id": "your-partner-uuid",
  "txnid": "TPV_TEST_001",
  "amount": "500.00",
  "productinfo": "TPV Payment",
  "firstname": "Borrower",
  "email": "borrower@example.com",
  "phone": "9988776655",
  "txn_s2s_flow": "4",
  "s2s_client_ip": "203.0.113.50",
  "s2s_device_info": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0)",
  "beneficiarydetail": "{\"ifscCode\":\"SBIN0001234\",\"accountNumber\":\"12345678901\",\"accountHolderName\":\"BORROWER NAME\"}",
  "hash": "<computed_hash>"
}
```

<Warning>
**Critical:** `beneficiarydetail` is a JSON string but is **NOT** included in hash calculation.
</Warning>

**Expected Response:**

```json
{
  "status": "success",
  "txnid": "TPV_TEST_001",
  "intentURIData": "upi://pay?pa=payu@icici&pn=PayU&tr=TPV_TEST_001&am=500.00...",
  "bankcode": "INTTPV",
  "api_version": "6"
}
```

**Validation Checklist:**

- [ ] Response contains `intentURIData`
- [ ] `bankcode` is automatically set to `INTTPV`
- [ ] `api_version` is `6`
- [ ] No errors in response

</details>

<details>
<summary><strong>2.3.2: Test Beneficiary Account Validation</strong></summary>

**Test Scenarios:**

**Scenario 1: Matching Account (Success)**

- Customer pays from UPI account linked to the beneficiary details provided
- Expected: Payment succeeds, webhook status = `success`

**Scenario 2: Mismatched Account (Failure)**

- Customer pays from a different UPI account (not linked to beneficiary details)
- Expected: Payment rejected, webhook status = `failure`

**Test Data:**

<Note>
Request test beneficiary account details from PayU support for sandbox testing. Real production accounts cannot be used in UAT.
</Note>

**Validation Checklist:**

- [ ] Matching account completes successfully
- [ ] Mismatched account is rejected
- [ ] Webhook contains `bankcode=INTTPV`
- [ ] Verify Payment API confirms TPV validation

</details>

<details>
<summary><strong>2.3.3: Verify TPV-Specific Webhook Fields</strong></summary>

**Expected Webhook Fields (Success):**

```
mihpayid=<PayU_Transaction_ID>
txnid=TPV_TEST_001
status=success
amount=500.00
bankcode=INTTPV
mode=UPI
unmappedstatus=captured
hash=<webhook_hash>
```

**Validation Checklist:**

- [ ] `bankcode` is `INTTPV` (confirms TPV flow)
- [ ] `mode` is `UPI`
- [ ] `unmappedstatus` is `captured` (for success)
- [ ] All beneficiary validation passed

</details>

***

## Step 3: Webhook Testing

### 3.1 Configure Partner Webhooks

<Warning>
Partner Payments webhooks are **different** from merchant-level webhooks. They must be configured separately in PayU's system.
</Warning>

**Required Webhook URLs:**

- `partner_webhook_success` — Triggered on successful payment
- `partner_webhook_failure` — Triggered on failed payment
- `partner_webhook_cancelled` — Triggered when customer cancels payment

**Configuration:**
Contact PayU support to register your partner webhook URLs. Provide:

- Your `reseller_id` (partner UUID)
- HTTPS URLs for all three webhook types
- IP whitelist (if required for your firewall)

***

### 3.2 Webhook Hash Verification

All webhooks from PayU include a `hash` parameter for verification.

**Reverse Hash Formula:**

```
client_secret|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|merchant_id
```

**Note:** Five pipes after `status`, then reverse order of request parameters

**Verification Steps:**

1. Extract parameters from webhook POST body
2. Compute reverse hash using formula above
3. Compare computed hash with webhook `hash` parameter
4. **Case-sensitive comparison** — hashes must match exactly

**Example (Python):**

```python
import hashlib

def verify_webhook_hash(webhook_data, client_secret):
    hash_string = (
        f"{client_secret}|{webhook_data['status']}||||||"
        f"{webhook_data.get('udf5', '')}|{webhook_data.get('udf4', '')}|"
        f"{webhook_data.get('udf3', '')}|{webhook_data.get('udf2', '')}|"
        f"{webhook_data.get('udf1', '')}|{webhook_data['email']}|"
        f"{webhook_data['firstname']}|{webhook_data['productinfo']}|"
        f"{webhook_data['amount']}|{webhook_data['txnid']}|"
        f"{webhook_data['merchant_id']}"
    )
    
    computed_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
    return computed_hash == webhook_data['hash']

# Usage
if verify_webhook_hash(webhook_data, client_secret):
    # Process webhook
    pass
else:
    # Reject webhook
    pass
```

**Validation Checklist:**

- [ ] Webhook arrives within 5–10 seconds of payment
- [ ] All expected fields are present (mihpayid, txnid, status, amount, hash)
- [ ] Hash verification passes
- [ ] Webhook is idempotent (handle duplicate webhooks)

***

### 3.3 Webhook Testing Checklist

**For Each Integration Method:**

| Test Case          | Expected Result                                         |
| ------------------ | ------------------------------------------------------- |
| Successful payment | `partner_webhook_success` called with `status=success`  |
| Failed payment     | `partner_webhook_failure` called with `status=failure`  |
| Cancelled payment  | `partner_webhook_cancelled` called with `status=cancel` |
| Hash verification  | Computed hash matches webhook `hash` parameter          |
| Duplicate webhook  | System handles idempotently (no duplicate processing)   |
| Delayed webhook    | Webhook retries after timeout (if first attempt fails)  |

***

## Step 4: Payment Verification API Testing

<Note>
Always use the Verify Payment API as the final source of truth for transaction status, even after receiving webhooks.
</Note>

### 4.1 Call Verify Payment API

**Endpoint:** `POST https://test-partnerapilayer.payu.in/verifyPayment`

**Test Payload:**

```json
{
  "merchant_id": "8739528",
  "txnid": "TPV_TEST_001"
}
```

**Expected Response (Success):**

```json
{
  "status": "success",
  "mihpayid": "403993715529111111",
  "txnid": "TPV_TEST_001",
  "amount": "500.00",
  "productinfo": "TPV Payment",
  "firstname": "Borrower",
  "email": "borrower@example.com",
  "mode": "UPI",
  "bankcode": "INTTPV",
  "unmappedstatus": "captured",
  "payment_source": "payu"
}
```

### 4.2 Reconcile Webhook vs Verify API

**Validation Checklist:**

- [ ] `mihpayid` matches in both webhook and verify response
- [ ] `txnid` matches original request
- [ ] `status` and `unmappedstatus` are consistent
- [ ] `amount` matches original request
- [ ] For TPV: `bankcode` is `INTTPV`
- [ ] No discrepancies between webhook and verify API

**Reconciliation Logic:**

```
IF webhook.status == verify_api.status
  AND webhook.mihpayid == verify_api.mihpayid
  AND webhook.amount == verify_api.amount
THEN
  Mark transaction as confirmed
ELSE
  Flag for manual review
```

***

## Common Errors and Resolutions

### Error: Invalid hash

**Error Message:**

```
Could not validate hash
```

**Cause:**<br />The payment request hash computed by your system doesn't match PayU's computed hash.

**Resolution:**

1. **Verify the hash formula:**
   ```
   merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||client_secret
   ```
   **Note:** Six consecutive pipes (`||||||`) between `udf5` and `client_secret`

2. **Use client_secret, not salt** — Partner Payments API requires `client_secret` (from OAuth credentials)

3. **Check for empty fields** — Empty fields should be represented as empty strings between pipes

4. **Verify SHA-512 hex output** — Ensure your hash is lowercase hexadecimal (128 characters)

5. **For UPI TPV:** Ensure `beneficiarydetail` is **NOT** included in hash calculation

**Debug Example (Java):**

```java
String hashString = merchantId + "|" + txnid + "|" + amount + "|" + productinfo + "|" +
                   firstname + "|" + email + "|" + udf1 + "|" + udf2 + "|" + udf3 + "|" +
                   udf4 + "|" + udf5 + "||||||" + clientSecret;

System.out.println("Hash String: " + hashString);
// Expected: 8739528|TXN001|518.02|Payment|||||||||||whatsapp||||||YOUR_CLIENT_SECRET

String hash = sha512Hex(hashString);
System.out.println("Computed Hash: " + hash);
System.out.println("Hash Length: " + hash.length()); // Should be 128
```

***

### Error: Auth token is not valid

**Error Message:**

```
Auth token is not valid
```

**Cause:**

- Access token has expired (default expiry: 3600 seconds)
- Token doesn't have the required scopes
- Token was generated for different environment (UAT vs production)
- Token is missing from the `Authorization` header

**Resolution:**

1. **Regenerate the token** — Complete all three OAuth steps:
   - Step 1: Password grant with reseller credentials
   - Step 2: Request authorization code for merchant
   - Step 3: Exchange code for final access token

2. **Verify scopes:**
   ```
   scopes=create_payment_links partner_payment_links partner_payments
   ```

3. **Check header format:**
   ```
   Authorization: Bearer YOUR_ACCESS_TOKEN
   ```

4. **Implement token caching:**

```python
import time

class TokenCache:
    def __init__(self):
        self.access_token = None
        self.expiry_time = 0
    
    def get_token(self):
        if time.time() >= self.expiry_time:
            # Regenerate token
            self.access_token = self._generate_new_token()
            self.expiry_time = time.time() + 3600  # 1 hour
        return self.access_token
```

***

### Error: Transaction not found

**Error Message:**

```
Transaction not found / No data found for given transaction details
```

**Cause:**<br />Transaction has not yet been persisted in PayU's system. This can happen immediately after initiating a payment.

**Resolution:**

1. **Wait 2–3 seconds** before calling Verify Payment API
2. **Implement retry logic** with exponential backoff
3. **Verify txnid** is correct and matches original request

**Retry Logic Example (Python):**

```python
import time
import requests

def verify_payment_with_retry(merchant_id, txnid, max_retries=3):
    for attempt in range(max_retries):
        response = requests.post(
            'https://test-partnerapilayer.payu.in/verifyPayment',
            json={'merchant_id': merchant_id, 'txnid': txnid}
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get('status') != 'Transaction not found':
                return data
        
        # Exponential backoff: 2s, 4s, 8s
        wait_time = 2 ** attempt
        time.sleep(wait_time)
    
    raise Exception(f"Transaction {txnid} not found after {max_retries} retries")
```

***

### Error: partner payment webhook not present/enabled

**Error Message:**

```
partner payment webhook not present/enabled for given merchant
```

**Cause:**<br />Partner-level webhooks are not configured in PayU's system for your `reseller_id`.

**Resolution:**

1. **Contact PayU Support** to configure partner webhooks
2. **Provide the following:**
   - Your `reseller_id` (partner UUID)
   - Webhook URLs (success, failure, cancel)
   - Whether webhooks should be enabled globally for all your merchants

**Important:** Partner webhooks are configured at the **partner level** (reseller), not individual merchant level.

***

### Error: s2s_client_ip or s2s_device_info is mandatory

**Error Message:**

```
s2s_client_ip and s2s_device_info are mandatory when txn_s2s_flow is 4
```

**Cause:**<br />UPI Intent and UPI TPV flows (`txn_s2s_flow=4`) require customer IP address and device information for security and fraud prevention.

**Resolution:**

1. **Capture customer IP address:**
   - From HTTP headers: `X-Forwarded-For` or `REMOTE_ADDR`
   - Send as string in `s2s_client_ip` parameter

2. **Capture device user-agent:**
   - From HTTP header: `User-Agent`
   - Send as string in `s2s_device_info` parameter

**Example (Node.js/Express):**

```javascript
app.post('/initiate-payment', (req, res) => {
  const clientIp = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
  const deviceInfo = req.headers['user-agent'];
  
  const paymentPayload = {
    merchant_id: '8739528',
    txnid: 'TXN001',
    amount: '100.00',
    txn_s2s_flow: '4',
    s2s_client_ip: clientIp,
    s2s_device_info: deviceInfo,
    // ... other parameters
  };
  
  // Send to PayU API
});
```

***

### Error: Could not validate HMAC header

**Error Message:**

```
Could not validate HMAC header signature
```

**Cause:**<br />HMAC signature validation failed for QR/omnichannel payment requests.

**Resolution:**

1. **Verify all required headers are present:**
   - `X-Payu-Signature`
   - `X-Payu-Timestamp`
   - `X-Payu-Nonce`

2. **Check timestamp** — Must be within ±5 minutes of current server time

3. **Confirm signing key** — Use the correct HMAC secret provided by PayU

<Warning>
⚠️ **Info Gap:** Exact HMAC signing algorithm and key derivation details needed from PayU documentation.
</Warning>

***

## Log Patterns for Debugging

Use these `grep` patterns to locate relevant log entries:

**Hash Validation Failures:**

```bash
grep -i "hash.*invalid\|could not validate hash" app.log
```

**Webhook Send/Receive:**

```bash
grep -i "webhook.*sent\|partner_webhook" app.log
```

**Payment Verification Calls:**

```bash
grep -i "verifyPayment\|verify.*payment" app.log
```

**Transaction Not Found Errors:**

```bash
grep -i "transaction not found\|no data found" app.log
```

**S2S Flow Errors:**

```bash
grep -i "s2s_client_ip\|s2s_device_info\|txn_s2s_flow" app.log
```

**OAuth Token Issues:**

```bash
grep -i "auth token.*not valid\|token.*expired\|401" app.log
```

***

## Test Data

### UAT Credentials

<Note>
Request complete UAT credentials from PayU support, including:
- Test `merchant_id`
- Test `client_id` and `client_secret`
- Test `reseller_id`
- Sandbox beneficiary account details (for UPI TPV testing)
</Note>

### Sample Transaction IDs

Use descriptive, unique transaction IDs for easy tracking:

```
HC_UAT_20240315_001    (Hosted Checkout)
UPI_INTENT_20240315_001 (UPI Intent)
TPV_UAT_20240315_001   (UPI TPV)
```

### Sample Customer Data

```json
{
  "firstname": "TestUser",
  "email": "testuser@example.com",
  "phone": "9876543210"
}
```

### Sample UDF Values

```json
{
  "udf1": "session_12345",
  "udf2": "app_android",
  "udf3": "v2.1.0",
  "udf4": "",
  "udf5": ""
}
```

### Sample Beneficiary Details (UPI TPV)

<Warning>
⚠️ **Info Gap:** Valid test IFSC codes and account numbers for UAT environment needed from PayU.
</Warning>

```json
{
  "ifscCode": "SBIN0001234",
  "accountNumber": "12345678901",
  "accountHolderName": "TEST ACCOUNT HOLDER"
}
```

***

## End-to-End Integration Checklist

Use this checklist to validate your complete integration before going live:

### OAuth Flow

- [ ] Step 1: Reseller password grant succeeds
- [ ] Step 2: Merchant authorization code obtained
- [ ] Step 3: Final access token contains all required scopes
- [ ] Token caching and refresh logic implemented

### Payment Initiation

- [ ] Hash generation follows correct formula
- [ ] `client_secret` used (not merchant salt)
- [ ] All mandatory parameters included
- [ ] For S2S: `s2s_client_ip` and `s2s_device_info` captured
- [ ] For TPV: `beneficiarydetail` excluded from hash

### Hosted Checkout (if applicable)

- [ ] `redirectUri` returned successfully
- [ ] Customer redirect to PayU works
- [ ] Hosted page loads with correct branding
- [ ] Test payments complete successfully
- [ ] Customer redirected to `surl`/`furl` based on outcome

### UPI Intent/TPV (if applicable)

- [ ] `intentURIData` returned in response
- [ ] UPI app launches correctly on mobile device
- [ ] Payment details pre-filled in UPI app
- [ ] Customer can authenticate and complete payment
- [ ] For TPV: Account validation works (success and failure scenarios)

### Webhook Handling

- [ ] Partner webhooks configured in PayU system
- [ ] Webhook URLs are HTTPS and publicly accessible
- [ ] Webhook hash verification implemented
- [ ] Idempotency handling prevents duplicate processing
- [ ] Webhook arrival time acceptable (\< 10 seconds)
- [ ] For TPV: `bankcode=INTTPV` validated

### Payment Verification

- [ ] Verify Payment API called after webhook
- [ ] Response reconciled with webhook data
- [ ] `mihpayid`, `txnid`, `amount`, `status` match
- [ ] Retry logic handles "transaction not found" errors
- [ ] Final payment status persisted in your system

### Error Handling

- [ ] Hash validation errors logged and debugged
- [ ] Token expiry handled with automatic refresh
- [ ] Transaction not found errors retry with backoff
- [ ] Invalid webhook signatures rejected
- [ ] All errors logged with sufficient context

### Reconciliation

- [ ] Daily reconciliation process in place
- [ ] Webhook vs Verify API discrepancies flagged
- [ ] Manual review process for failed/stuck transactions
- [ ] Settlement reports downloaded from PayU dashboard

***

## Going Live Checklist

Before switching to production:

### Credential Updates

- [ ] Production `client_id` and `client_secret` obtained
- [ ] Production `merchant_id` and `reseller_id` configured
- [ ] Production OAuth endpoints updated in code
- [ ] Production API endpoints updated (`https://partnerapilayer.payu.in`)

### Final Validation

- [ ] Conduct live transaction in production (small amount)
- [ ] Verify production webhook delivery
- [ ] Confirm production Verify Payment API works
- [ ] Validate production reconciliation process
- [ ] Check production settlement in PayU dashboard

### Infrastructure

- [ ] Webhook URLs whitelisted on firewall
- [ ] SSL certificates valid for all callback URLs
- [ ] Load balancing configured (if high volume expected)
- [ ] Monitoring and alerting set up for payment failures

### Documentation

- [ ] API integration document updated
- [ ] Runbook created for common errors
- [ ] Contact information for PayU support documented
- [ ] Escalation process defined for critical issues

***

## Support

For unresolved issues or technical questions, contact PayU Partner Support with:

**Required Information:**

- Your `reseller_id` (partner UUID)
- Merchant ID(s) involved
- Integration method (Hosted Checkout / UPI Intent / UPI TPV)
- Detailed error description
- Sample `txnid` exhibiting the issue
- Timestamp of the transaction
- Full error message and relevant logs
- Steps to reproduce (if applicable)

**Support Channels:**

- Partner Portal: [https://partner.payu.in/support](https://partner.payu.in/support)
- Email: [partner-support@payu.in](mailto:partner-support@payu.in)
- Phone: \[Contact information from PayU]

***

## Related Documentation

- [Partner Payments Overview](doc:partner-payments-overview)
- [Hosted Checkout Integration Guide](ref:hosted-checkout-api-partner-integration)
- [UPI Intent Integration Guide](ref:upi-s2s-partner-integration-api)
- [UPI TPV Integration Guide](doc:partner-payments-upi-tpv-integration)
- [Getting Access Token (OAuth)](ref:getting-access-token)
- [Verify Payment API](doc:verify-payment-api)
