---
title: Testing and Troubleshooting Partner Integration
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
This section covers common errors, their resolutions, debugging techniques, and test data for Partner Payments integration.

***

## Common Errors and Resolutions

### Error: Invalid hash

**Error Message:**

```
Could not validate hash
```

**Cause:**<br />The payment request hash computed by your system doesn't match PayU's computed hash. This typically indicates:

- Incorrect field order in hash string
- Using merchant `salt` instead of partner `client_secret`
- Missing or extra pipe characters (`|`) in the hash formula
- Encoding issues or incorrect SHA-512 implementation

**Resolution:**

1. **Verify the hash formula** — Ensure you're using the correct partner payment hash formula:
   ```
   merchant_id|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||client_secret
   ```
   Note: **Six consecutive pipes** (`||||||`) between `udf5` and `client_secret`

2. **Use client_secret, not salt** — Partner Payments API requires `client_secret` (from OAuth credentials), not the merchant's `salt` value

3. **Check for empty fields** — Empty fields (e.g., `firstname=""`) should be represented as empty strings between pipes, resulting in consecutive pipes

4. **Verify SHA-512 hex output** — Ensure your hash is lowercase hexadecimal (128 characters)

**Debug Example (Java):**

```java
String hashString = merchantId + "|" + txnid + "|" + amount + "|" + productinfo + "|" +
                   firstname + "|" + email + "|" + udf1 + "|" + udf2 + "|" + udf3 + "|" +
                   udf4 + "|" + udf5 + "||||||" + clientSecret;

System.out.println("Hash String: " + hashString);
// Expected: 8739528|28471834809170981|518.02|Payment for service|||||||||||whatsapp||||||YOUR_CLIENT_SECRET

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
- Token doesn't have the required `partner_payments` scope
- Token was generated for a different environment (UAT token used in production)
- Token is missing from the `Authorization` header

**Resolution:**

1. **Regenerate the token** — Complete all three OAuth steps again:
   - Step 1: Password grant with reseller credentials
   - Step 2: Request authorization code for merchant
   - Step 3: Exchange code for final access token

2. **Verify scopes** — Ensure the authorization code request (Step 2) includes:
   ```
   scopes=create_payment_links partner_payment_links partner_payments
   ```

3. **Check header format** — Ensure the Authorization header is correctly formatted:
   ```
   Authorization: Bearer YOUR_ACCESS_TOKEN
   ```
   (Note: There's a space between "Bearer" and the token)

4. **Use correct environment** — Ensure UAT tokens are used with UAT endpoints, and production tokens with production endpoints

**Token Expiry Handling:**

```java
// Cache token with expiry time
class TokenCache {
    private String accessToken;
    private long expiryTime;
    
    public String getToken() {
        if (System.currentTimeMillis() >= expiryTime) {
            // Token expired, regenerate
            accessToken = regenerateToken();
            expiryTime = System.currentTimeMillis() + 3600000; // 1 hour
        }
        return accessToken;
    }
}
```

***

### Error: Payment transaction not found in core payments

**Error Message:**

```
Transaction not found
```

**Cause:**<br />The transaction hasn't been persisted in PayU's core payment system yet. This can occur when:

- Calling verify payment API immediately after payment initiation
- Network latency between partner layer and core payments
- Transaction ID (txnid) is incorrect or doesn't exist

**Resolution:**

1. **Wait and retry** — Add a 2-3 second delay before calling verify payment:
   ```java
   // Initiate payment
   PaymentResponse response = initiatePayment(request);

   // Wait for persistence
   Thread.sleep(3000); // 3 seconds

   // Now verify
   VerifyResponse verification = verifyPayment(txnid);
   ```

2. **Implement exponential backoff** — Retry verification with increasing delays:
   ```python
   import time

   def verify_with_retry(txnid, max_retries=3):
       for attempt in range(max_retries):
           try:
               return verify_payment(txnid)
           except TransactionNotFoundError:
               if attempt < max_retries - 1:
                   sleep_time = 2 ** attempt  # 1s, 2s, 4s
                   time.sleep(sleep_time)
               else:
                   raise
   ```

3. **Verify txnid** — Ensure the `txnid` used in verify payment matches the one sent in the payment request

***

### Error: partner payment webhook url not present or not enabled

**Error Message:**

```
partner payment webhook url not present or not enabled
```

**Cause:**<br />No row exists in the `partner_webhook_urls` table for your partner, or the `is_payment_webhook_enabled` flag is set to `false`.

**Resolution:**

1. **Insert webhook configuration** — Add a row to `partner_webhook_urls`:
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
     NULL,
     'https://partner.example.com/webhook/payment/success',
     'https://partner.example.com/webhook/payment/failure',
     'https://partner.example.com/webhook/payment/cancelled',
     'https://partner.example.com/webhook/payment/default',
     'Your Partner Name',
     true,  -- MUST be true
     false
   );
   ```

2. **Enable the flag** — If row exists but webhooks aren't working:
   ```sql
   UPDATE partner_webhook_urls
   SET is_payment_webhook_enabled = true
   WHERE partner_uuid = '11ee-0e7e-5403fde2-9523-0a696b110fde';
   ```

3. **Check merchant_id** — Use `merchant_id = NULL` for partner-level webhooks (applies to all merchants)

***

### Error: s2s_client_ip or s2s_device_info mandatory

**Error Message:**

```
s2s_client_ip or s2s_device_info mandatory
```

**Cause:**<br />You've set `txn_s2s_flow = "4"` to enable UPI Intent S2S, but didn't include the mandatory `s2s_client_ip` and `s2s_device_info` fields.

**Resolution:**

1. **Add both mandatory S2S fields** to your payment request:
   ```json
   {
     "txn_s2s_flow": "4",
     "s2s_client_ip": "157.240.22.9",
     "s2s_device_info": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.4.6"
   }
   ```

2. **Capture real values** — Extract these from the customer's request:
   ```java
   // Get client IP from HTTP request
   String clientIp = request.getHeader("X-Forwarded-For");
   if (clientIp == null) {
       clientIp = request.getRemoteAddr();
   }

   // Get device info from User-Agent header
   String deviceInfo = request.getHeader("User-Agent");
   ```

3. **Don't use S2S flow for redirect** — If you want redirect checkout, **omit** `txn_s2s_flow` entirely

***

### Error: Could not validate HMAC header

**Error Message:**

```
Could not validate HMAC header
```

**Cause:**<br />This error occurs in omnichannel QR flows when the HMAC signature in request headers is malformed or doesn't match PayU's computed signature.

**Resolution:**

> **⚠️ Info Gap:** The exact HMAC header format and signing algorithm for omnichannel QR flows should be confirmed with the PayU integration team.

1. **Check HMAC header format** — Ensure headers include:
   - `X-HMAC-Signature`
   - `X-HMAC-Date` (request timestamp)
   - `X-HMAC-Algorithm` (e.g., "HmacSHA256")

2. **Verify signing date** — Ensure the timestamp is recent (within allowed clock skew, typically ±5 minutes)

3. **Confirm signing key** — Verify you're using the correct secret key for HMAC computation

***

## Log Patterns for Debugging

Use these grep patterns to troubleshoot issues in PayU application logs:

### Hash Validation Failures

```bash
grep "Could not validate hash" application.log
```

**What to look for:** Transaction IDs and timestamps of failed hash validations. Compare your hash computation with these events.

***

### Webhook Sending Events

```bash
grep "Sending.*payment webhook" application.log
```

**What to look for:** Confirmation that PayU is attempting to send webhooks to your URLs. If you're not receiving webhooks, check if this log entry exists.

***

### Verify Payment API Calls

```bash
grep "verifyPayment" application.log
```

**What to look for:** Verify payment requests and responses. Useful for checking if PayU is receiving your verification calls and what status is being returned.

***

### Transaction Not Found Errors

```bash
grep "Transaction not found" application.log
```

**What to look for:** Frequency of this error. If it appears frequently, you may need to add retry logic with delays.

***

## Test Data

### Test Credentials (UAT Environment)

> **⚠️ Info Gap:** Complete test credentials including `client_id`, `client_secret`, reseller username, and password should be obtained from your PayU integration team.

**Sample Test Data (from documentation):**

| Parameter                      | Value                                |
| ------------------------------ | ------------------------------------ |
| `merchant_id`                  | 8739528                              |
| `reseller_id` / `partner_uuid` | 11ee-0e7e-5403fde2-9523-0a696b110fde |

### Sample Transaction IDs

Use these patterns for generating test transaction IDs:

- `28408067218883788`
- `28471834809170981`
- `28471834809170982`

**Format:** Numeric string, typically 17-20 digits, unique per transaction

### Sample Customer Data

```json
{
  "phone": "919820988398",
  "firstname": "",
  "email": "",
  "amount": "518.02"
}
```

### Sample UDF Values

User-defined fields for partner-specific metadata:

```json
{
  "udf1": "",
  "udf2": "1370625260",
  "udf3": "r-hway-LDnTRBuFK8STTTeTEc2SuD",
  "udf4": "",
  "udf5": "whatsapp"
}
```

**Common udf5 values:**

- `"whatsapp"` — Payment initiated via WhatsApp
- `"web"` — Payment initiated via web portal
- `"mobile_app"` — Payment initiated via mobile app

### Sample Beneficiary Detail (UPI TPV)

```json
{
  "ifscCode": "ICIC0001234",
  "accountNumber": "123456789012",
  "accountHolderName": "Test User"
}
```

> **⚠️ Info Gap:** Valid test IFSC codes and account numbers for UAT should be provided by PayU.

***

## Test Flow Checklist

Use this checklist to verify your integration end-to-end:

### ✅ OAuth Token Generation

- [ ] Step 1: Password grant returns `access_token` with `expires_in: 3600`
- [ ] Step 2: Authorization code request returns `attributes.code`
- [ ] Step 3: Code exchange returns final `access_token`
- [ ] Token includes required scopes: `partner_payments`

### ✅ Payment Initiation

- [ ] Payment request hash computed correctly (6 pipes before `client_secret`)
- [ ] Request includes all mandatory fields (`txnid`, `amount`, `merchant_id`, `reseller_id`)
- [ ] For S2S: `txn_s2s_flow=4`, `s2s_client_ip`, and `s2s_device_info` included
- [ ] Response returns `metaData.txnStatus` and either `intentURIData` or `redirectUri`

### ✅ Webhook Configuration

- [ ] Row inserted in `partner_webhook_urls` with `is_payment_webhook_enabled=true`
- [ ] Webhook endpoint URLs are publicly accessible
- [ ] Webhook endpoint returns HTTP 200 status
- [ ] Webhook hash verification passes (reverse hash formula)

### ✅ Payment Verification

- [ ] Verify payment hash computed correctly (`merchant_id|verify_payment|txnid|client_secret`)
- [ ] Verify payment API returns transaction status
- [ ] `mihpayid` from verify response matches webhook payload
- [ ] `status` and `unmappedstatus` match between webhook and verification

### ✅ Error Handling

- [ ] 401 errors trigger token regeneration
- [ ] Hash validation failures are logged with full hash string
- [ ] Transaction not found errors trigger retry with delay
- [ ] Webhook signature failures reject the payload

***

## Next Steps

- [Partner Payments Integration Guide](doc:partner-payments-integration-guide) — Main integration flow
- [UPI TPV Integration](doc:upi-tpv-integration) — Third-party validation setup
- [API Reference: POST /partner/payments](ref:partner-payments-api) — Complete API specification

<Info>
**Need Help?** If you encounter errors not covered in this guide, contact PayU support with:
- Full error message
- Transaction ID (txnid)
- Timestamp of the error
- Relevant log excerpts
</Info>
