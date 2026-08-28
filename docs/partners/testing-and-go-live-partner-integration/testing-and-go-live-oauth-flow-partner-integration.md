---
title: Testing and Go Live - OAuth Flow Partner Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
# Testing and Go-Live Checklist: OAuth Integration

> This checklist covers everything you need to test and validate the Co-Branded OAuth flow before going live.

## Postman Collection

<Callout icon="📘" theme="success">
  Accelerate your integration workflow with our Postman collection for OAuth Integration. Click the Download Postman Collection button below to download and get started.

  <HTMLBlock>{`
                  <style>
                  .tooltip-btn {
                      position: relative;
                      background-color: #4CAF50;
                      color: white;
                      padding: 10px 20px;
                      border: none;
                      border-radius: 5px;
                      cursor: pointer;
                      font-weight: bold;
                  }
                  .tooltip-btn:hover::after {
                      content: attr(data-tooltip);
                      position: absolute;
                      bottom: 125%;
                      left: 50%;
                      transform: translateX(-50%);
                      background-color: #333;
                      color: white;
                      padding: 5px 10px;
                      border-radius: 4px;
                      white-space: nowrap;
                      font-size: 12px;
                      z-index: 1;
                  }
                  </style>

                  <button onclick="window.open('https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/collection/3ztf96f/payu-oauth2-collection', '_blank')"
                          class="tooltip-btn"
                          data-tooltip="Click to download the Postman collection and explore OAuth APIs.">
                      Access Postman Collection
                  </button>
  `}</HTMLBlock>
</Callout>

---

## Test Environment

Use the following test environment endpoints for OAuth Integration:

| Resource | Test Environment URL | Production Environment URL |
|----------|---------------------|---------------------------|
| Authorization Page | `https://onboardingtest.payu.in/merchant/partner-oauth` | `https://onboarding.payu.in/merchant/partner-oauth` |
| Validate Auth Code | `https://testdashboard.payu.in/oauth/validate-auth-code` | `https://dashboard.payu.in/oauth/validate-auth-code` |
| Get Merchant Credentials | `https://testdashboard.payu.in/oauth/get-merchant-credentials` | `https://dashboard.payu.in/oauth/get-merchant-credentials` |
| Payment APIs (Hosted Checkout) | `https://test.payu.in/_payment` | `https://secure.payu.in/_payment` |

> **Note:** All OAuth endpoints use test environment URLs with `test` subdomain for testing.

---

## Testing OAuth Integration

Follow these steps to test the complete OAuth onboarding flow:

<Accordion title="1. Setup Test Credentials" icon="fa-list-check">

**Prerequisites:**
- Partner Client ID and Client Secret (test environment)
- Whitelisted redirect URL (test environment)
- Access to PayU Partner Portal (test mode)

> Contact your PayU Key Account Manager (KAM) to:
> - Enable OAuth onboarding for your partner account
> - Obtain test environment Client ID and Secret
> - Whitelist your test redirect URL(s)

**How to Download Credentials:**
1. Log in to [PayU Partner Portal](https://test-partner.payu.in) (test environment)
2. Navigate to **Merchant Integration** → **Partner Integration**
3. Click **Download Credentials**
4. Save Client ID and Client Secret securely

</Accordion>

<Accordion title="2. Test Authorization URL Construction" icon="fa-list-check">

  <Accordion title="Step 1: Build Authorization URL" icon="fa-list-check">

Construct the authorization URL with proper URL encoding:

**Test URL Format:**
```
https://onboardingtest.payu.in/merchant/partner-oauth?client_id={{client_id}}&redirect_url={{encoded_redirect_url}}
```

**Sample Authorization URLs:**

```
# Basic redirect URL
https://onboardingtest.payu.in/merchant/partner-oauth?client_id=ABC123&redirect_url=https%3A%2F%2Fpartner.example.com%2Fcallback

# Redirect URL with parameters
https://onboardingtest.payu.in/merchant/partner-oauth?client_id=ABC123&redirect_url=https%3A%2F%2Fpartner.example.com%2Fcallback%3Fsession_id%3D12345
```

**Validation Points:**
- [ ] Client ID is correct
- [ ] Redirect URL is properly URL-encoded
- [ ] Redirect URL matches whitelisted URL in Partner Portal
- [ ] URL opens PayU authorization page
- [ ] No browser errors or warnings

  </Accordion>

  <Accordion title="Step 2: URL Encoding Test" icon="fa-list-check">

Verify URL encoding is correct:

| Original URL | URL Encoded |
|--------------|-------------|
| `https://partner.example.com/callback` | `https%3A%2F%2Fpartner.example.com%2Fcallback` |
| `https://partner.example.com/callback?session=123` | `https%3A%2F%2Fpartner.example.com%2Fcallback%3Fsession%3D123` |
| `https://partner.example.com/callback?a=1&b=2` | `https%3A%2F%2Fpartner.example.com%2Fcallback%3Fa%3D1%26b%3D2` |

> 📘 **Tip:** Use online URL encoding tools or programming language built-in functions:
> - JavaScript: `encodeURIComponent(url)`
> - Python: `urllib.parse.quote(url, safe='')`
> - PHP: `urlencode($url)`
> - Java: `URLEncoder.encode(url, "UTF-8")`

  </Accordion>

</Accordion>

<Accordion title="3. Test Merchant Authorization Flow" icon="fa-list-check">

  <Accordion title="Scenario 1: New Merchant Registration" icon="fa-list-check">

**Test Steps:**
1. Click authorization URL
2. PayU authorization page loads
3. Click "Create New Account"
4. Fill merchant registration form:
   - Business name: `Test Business OAuth`
   - Email: `test.oauth.{timestamp}@example.com`
   - Mobile: `9999999999`
   - PAN: `AAAPA1234A` (test PAN)
5. Complete OTP verification
6. Grant authorization to partner app
7. Redirected to partner redirect URL with `auth_code`

**Validation Points:**
- [ ] Registration form loads correctly
- [ ] Mobile OTP received and verified
- [ ] Email verification completed
- [ ] Partner branding visible (if configured)
- [ ] Authorization grant screen displays correctly
- [ ] Redirect to partner URL successful
- [ ] `auth_code` present in URL parameters

  </Accordion>

  <Accordion title="Scenario 2: Existing Merchant Login" icon="fa-list-check">

**Test Steps:**
1. Click authorization URL
2. PayU authorization page loads
3. Login with existing test merchant credentials
4. Grant authorization to partner app
5. Redirected to partner redirect URL with `auth_code`

**Validation Points:**
- [ ] Login form loads correctly
- [ ] Authentication successful
- [ ] Authorization grant screen displays
- [ ] Partner app details shown correctly
- [ ] Redirect successful with `auth_code`

  </Accordion>

  <Accordion title="Scenario 3: Already Onboarded Merchant" icon="fa-list-check">

**Test Steps:**
1. Click authorization URL with merchant already onboarded through partner
2. Auto-redirect should occur with `auth_code`

**Validation Points:**
- [ ] No additional consent required
- [ ] Immediate redirect to partner URL
- [ ] Valid `auth_code` received

  </Accordion>

  <Accordion title="Scenario 4: Merchant Denies Authorization" icon="fa-list-check">

**Test Steps:**
1. Click authorization URL
2. Login as merchant
3. Click "Deny" or "Cancel" on authorization screen
4. Redirected to partner URL

**Validation Points:**
- [ ] Redirect occurs even on denial
- [ ] Error parameter in redirect URL (e.g., `?error=access_denied`)
- [ ] Partner app handles denial gracefully
- [ ] User-friendly error message displayed

  </Accordion>

</Accordion>

<Accordion title="4. Test Authorization Code Exchange" icon="fa-key">

**API:** [Validate Auth Code and Client API](ref:validate_authcode_and_client_api)

  <Accordion title="Step 1: Capture Authorization Code" icon="fa-list-check">

From the redirect URL, extract the `auth_code` parameter:

```
https://partner.example.com/callback?auth_code=ABC123XYZ789DEF456
```

Extract: `auth_code=ABC123XYZ789DEF456`

  </Accordion>

  <Accordion title="Step 2: Exchange Code for Credentials" icon="fa-code">

Call the Validate Auth Code API immediately:

**Sample Request:**
```bash
curl --location 'https://testdashboard.payu.in/oauth/validate-auth-code' \
--header 'Content-Type: application/json' \
--data '{
    "client_id": "ABC123",
    "client_secret": "your_client_secret",
    "auth_code": "ABC123XYZ789DEF456"
}'
```

**Expected Success Response:**
```json
{
    "status": 1,
    "msg": "Success",
    "merchant_key": "mK3j2L9p",
    "salt": "sA7x9B2c"
}
```

**Validation Points:**
- [ ] API responds within 2 seconds
- [ ] `status` is `1` for success
- [ ] `merchant_key` received (8 characters)
- [ ] `salt` received (8 characters)
- [ ] Both values are alphanumeric

  </Accordion>

  <Accordion title="Step 3: Test Error Scenarios" icon="fa-shield-check">

**Invalid Client ID:**
```json
{
    "client_id": "INVALID",
    "client_secret": "your_client_secret",
    "auth_code": "valid_auth_code"
}
```

**Expected Response:**
```json
{
    "status": 0,
    "msg": "Invalid client credentials"
}
```

**Invalid Client Secret:**
```json
{
    "client_id": "ABC123",
    "client_secret": "INVALID",
    "auth_code": "valid_auth_code"
}
```

**Expected Response:**
```json
{
    "status": 0,
    "msg": "Invalid client credentials"
}
```

**Expired/Invalid Auth Code:**
```json
{
    "client_id": "ABC123",
    "client_secret": "your_client_secret",
    "auth_code": "EXPIRED_OR_INVALID"
}
```

**Expected Response:**
```json
{
    "status": 0,
    "msg": "Invalid auth code"
}
```

**Reused Auth Code:**
```json
{
    "client_id": "ABC123",
    "client_secret": "your_client_secret",
    "auth_code": "ALREADY_USED_CODE"
}
```

**Expected Response:**
```json
{
    "status": 0,
    "msg": "Auth code already used"
}
```

**Validation Points:**
- [ ] Invalid credentials rejected with `status: 0`
- [ ] Expired codes rejected appropriately
- [ ] Reused codes cannot be exchanged again
- [ ] Error messages are clear and actionable
- [ ] No sensitive information leaked in errors

  </Accordion>

  <Accordion title="Step 4: Test Auth Code Expiration" icon="fa-shield-check">

**Test Steps:**
1. Generate auth code
2. Wait 10 minutes (or configured expiry time)
3. Attempt to exchange expired code
4. Verify rejection

**Validation Points:**
- [ ] Expired codes rejected
- [ ] Appropriate error message
- [ ] Must generate new auth code

  </Accordion>

</Accordion>

<Accordion title="5. Test Credential Storage and Security" icon="fa-shield-check">

  <Accordion title="Test 1: Secure Storage" icon="fa-shield-check">

**Validation Points:**
- [ ] `merchant_key` stored encrypted in database
- [ ] `salt` stored encrypted in database
- [ ] Credentials never logged in plain text
- [ ] Credentials not exposed in client-side code
- [ ] Database access controlled and audited

  </Accordion>

  <Accordion title="Test 2: Credential Retrieval" icon="fa-key">

**Test Steps:**
1. Store credentials after receiving from API
2. Associate with partner's internal merchant ID
3. Retrieve credentials for payment processing
4. Decrypt and use for hash generation

**Validation Points:**
- [ ] Credentials retrieved successfully
- [ ] Decryption works correctly
- [ ] Associated with correct merchant
- [ ] Audit log created for retrieval

  </Accordion>

  <Accordion title="Test 3: Access Control" icon="fa-shield-check">

**Test Steps:**
1. Implement role-based access control
2. Test admin access to credentials
3. Test non-admin access denied
4. Test API-level access restrictions

**Validation Points:**
- [ ] Only authorized roles can access credentials
- [ ] Access attempts logged
- [ ] Failed access attempts trigger alerts
- [ ] No credentials visible in application logs

  </Accordion>

</Accordion>

<Accordion title="6. Test Get Merchant Credentials API" icon="fa-magnifying-glass">

**API:** [Get Merchant Credentials API](ref:get_merchant_credentials_api)

**Use Case:** Retrieve credentials at a later time if needed

  <Accordion title="Step 1: Basic Retrieval" icon="fa-code">

```bash
curl --location 'https://testdashboard.payu.in/oauth/get-merchant-credentials' \
--header 'Content-Type: application/json' \
--data '{
    "client_id": "ABC123",
    "client_secret": "your_client_secret"
}'
```

**Expected Response:**
```json
{
    "status": 1,
    "msg": "Success",
    "merchant_key": "mK3j2L9p",
    "salt": "sA7x9B2c"
}
```

**Validation Points:**
- [ ] Credentials match those received earlier
- [ ] API responds within 2 seconds
- [ ] Can be called multiple times
- [ ] Same credentials returned consistently

  </Accordion>

  <Accordion title="Step 2: Error Scenarios" icon="fa-shield-check">

**Invalid Client Credentials:**
```json
{
    "client_id": "INVALID",
    "client_secret": "INVALID"
}
```

**Expected Response:**
```json
{
    "status": 0,
    "msg": "Invalid client credentials"
}
```

**No Merchant Onboarded:**

For a valid partner client that hasn't onboarded any merchant via OAuth:

**Expected Response:**
```json
{
    "status": 0,
    "msg": "No merchant found for this partner"
}
```

**Validation Points:**
- [ ] Invalid credentials rejected
- [ ] Appropriate error messages
- [ ] No sensitive data in error responses

  </Accordion>

</Accordion>

<Accordion title="7. Test Payment Integration with OAuth Credentials" icon="fa-check-circle">

After receiving merchant credentials via OAuth, test payment collection:

  <Accordion title="Step 1: Generate Payment Hash" icon="fa-key">

Use the received `merchant_key` and `salt` to generate payment hash:

**Hash Formula:**
```
hash = sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

**Sample Hash Generation (PHP):**
```php
<?php
$key = "mK3j2L9p"; // From OAuth
$salt = "sA7x9B2c"; // From OAuth
$txnid = "TEST" . time();
$amount = "10.00";
$productinfo = "Test Product";
$firstname = "Test User";
$email = "test@example.com";
$udf1 = $udf2 = $udf3 = $udf4 = $udf5 = "";

$hashString = $key.'|'.$txnid.'|'.$amount.'|'.$productinfo.'|'.$firstname.'|'.$email.'|'.$udf1.'|'.$udf2.'|'.$udf3.'|'.$udf4.'|'.$udf5.'||||||'.$salt;

$hash = strtolower(hash('sha512', $hashString));
?>
```

**Sample Hash Generation (Python):**
```python
import hashlib

key = "mK3j2L9p"  # From OAuth
salt = "sA7x9B2c"  # From OAuth
txnid = f"TEST{int(time.time())}"
amount = "10.00"
productinfo = "Test Product"
firstname = "Test User"
email = "test@example.com"
udf1 = udf2 = udf3 = udf4 = udf5 = ""

hash_string = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{salt}"

hash_value = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
```

**Validation Points:**
- [ ] Hash generated correctly using OAuth credentials
- [ ] Hash is 128 characters (SHA-512)
- [ ] Hash is lowercase
- [ ] No extra spaces in hash string

  </Accordion>

  <Accordion title="Step 2: Test Payment Request" icon="fa-code">

Submit payment to PayU Hosted Checkout:

**Sample HTML Form:**
```html
<form action="https://test.payu.in/_payment" method="post">
    <input type="hidden" name="key" value="mK3j2L9p" />
    <input type="hidden" name="txnid" value="TEST123456789" />
    <input type="hidden" name="amount" value="10.00" />
    <input type="hidden" name="productinfo" value="Test Product" />
    <input type="hidden" name="firstname" value="Test User" />
    <input type="hidden" name="email" value="test@example.com" />
    <input type="hidden" name="phone" value="9999999999" />
    <input type="hidden" name="surl" value="https://partner.example.com/success" />
    <input type="hidden" name="furl" value="https://partner.example.com/failure" />
    <input type="hidden" name="hash" value="{{generated_hash}}" />
    <input type="submit" value="Pay Now" />
</form>
```

**Test Payment Methods:**

**Credit Card (Test):**
- Card Number: `5123456789012346`
- CVV: `123`
- Expiry: `12/2025`
- Name: `Test User`
- OTP: `123456`

**Net Banking:**
- Bank: ICICI (Test)
- User will be redirected to test bank page
- Auto-success in test mode

**UPI:**
- UPI ID: `success@payu`
- Auto-success in test mode

**Validation Points:**
- [ ] Payment page loads successfully
- [ ] Merchant name displayed correctly
- [ ] Payment methods available
- [ ] Test transaction succeeds
- [ ] Redirected to success URL (SURL)
- [ ] Transaction details match request

  </Accordion>

  <Accordion title="Step 3: Verify Payment Response" icon="fa-shield-check">

Handle the callback from PayU:

**Success Response (POST to SURL):**
```php
<?php
$mihpayid = $_POST['mihpayid'];
$status = $_POST['status'];
$txnid = $_POST['txnid'];
$amount = $_POST['amount'];
$hash = $_POST['hash'];

// Reverse hash verification
$reverseHashString = $salt.'|'.$status.'|||||||||||'.$email.'|'.$firstname.'|'.$productinfo.'|'.$amount.'|'.$txnid.'|'.$key;
$reverseHash = strtolower(hash('sha512', $reverseHashString));

if ($reverseHash == $hash) {
    // Hash verified - payment is genuine
    if ($status == 'success') {
        // Payment successful
    }
}
?>
```

**Validation Points:**
- [ ] Reverse hash calculated correctly
- [ ] Reverse hash matches received hash
- [ ] Payment status is 'success'
- [ ] Transaction ID matches request
- [ ] Amount matches request
- [ ] PayU ID (mihpayid) received

  </Accordion>

</Accordion>

<Accordion title="8. Test Multiple Merchant Onboarding" icon="fa-list-check">

Test onboarding multiple merchants through OAuth:

**Test Steps:**
1. Onboard Merchant A via OAuth
2. Store Merchant A credentials
3. Onboard Merchant B via OAuth
4. Store Merchant B credentials
5. Verify both sets of credentials work independently

**Validation Points:**
- [ ] Each merchant has unique `merchant_key` and `salt`
- [ ] Credentials stored separately and correctly associated
- [ ] Payments for Merchant A use Merchant A credentials
- [ ] Payments for Merchant B use Merchant B credentials
- [ ] No credential cross-contamination

</Accordion>

<Accordion title="9. Test Error Handling and Edge Cases" icon="fa-shield-check">

  <Accordion title="Scenario 1: Redirect URL Mismatch" icon="fa-times-circle">

**Test Steps:**
1. Whitelist URL: `https://partner.example.com/callback`
2. Use redirect URL: `https://different.example.com/callback`
3. Attempt authorization

**Expected Result:**
- [ ] Authorization blocked
- [ ] Error message displayed
- [ ] No auth code generated

  </Accordion>

  <Accordion title="Scenario 2: Missing Parameters" icon="fa-times-circle">

**Test Steps:**
1. Build auth URL without `client_id`
2. Build auth URL without `redirect_url`
3. Attempt authorization

**Expected Result:**
- [ ] Error message displayed
- [ ] User not able to proceed

  </Accordion>

  <Accordion title="Scenario 3: Network Timeout" icon="fa-times-circle">

**Test Steps:**
1. Simulate slow network during API call
2. Test timeout handling
3. Test retry logic

**Validation Points:**
- [ ] Timeout handled gracefully
- [ ] User-friendly error message
- [ ] Retry mechanism works
- [ ] No duplicate credential storage

  </Accordion>

  <Accordion title="Scenario 4: Concurrent OAuth Flows" icon="fa-list-check">

**Test Steps:**
1. Start OAuth flow for Merchant X
2. Before completing, start OAuth flow for Merchant Y
3. Complete both flows

**Validation Points:**
- [ ] Both flows complete successfully
- [ ] Correct credentials stored for each merchant
- [ ] No session confusion
- [ ] State management working correctly

  </Accordion>

</Accordion>

---

## End-to-End Testing Scenarios

Test the complete integration flow from OAuth authorization to payment collection:

<Accordion title="Scenario 1: Complete OAuth Flow + First Payment" icon="fa-thumbs-up">

1. Build and open authorization URL
2. Register new test merchant or login existing
3. Grant authorization to partner app
4. Receive auth code in redirect
5. Exchange auth code for credentials via [Validate Auth Code API](ref:validate_authcode_and_client_api)
6. Store credentials securely
7. Generate payment hash using credentials
8. Submit test payment to PayU
9. Verify payment success
10. Validate payment callback and reverse hash

**Expected Duration:** 3–5 minutes

**Validation Points:**
- [ ] All steps complete without errors
- [ ] Credentials received and stored
- [ ] Payment successful
- [ ] Callback received with valid data

</Accordion>

<Accordion title="Scenario 2: OAuth Re-authorization" icon="fa-magnifying-glass">

1. Complete initial OAuth flow for a merchant
2. Store credentials
3. Later, initiate OAuth flow again for same merchant
4. Verify auto-redirect with new auth code
5. Exchange new auth code for credentials
6. Verify credentials match previously stored

**Validation Points:**
- [ ] Re-authorization works smoothly
- [ ] Merchant not asked for consent again
- [ ] Same credentials returned
- [ ] No duplicate merchant records

</Accordion>

<Accordion title="Scenario 3: Bulk Merchant Onboarding via OAuth" icon="fa-list-check">

1. Prepare list of 10 test merchants
2. Send OAuth links to each
3. Track completion status
4. Store all credentials
5. Test payment for each merchant

**Validation Points:**
- [ ] All merchants onboarded successfully
- [ ] Each has unique credentials
- [ ] Parallel processing works
- [ ] No credential mix-ups

</Accordion>

<Accordion title="Scenario 4: Error Recovery" icon="fa-times-circle">

1. Start OAuth flow
2. Receive auth code
3. API call fails (simulate network error)
4. Retry auth code exchange
5. Verify success on retry

**Validation Points:**
- [ ] Retry successful
- [ ] Auth code still valid within expiry
- [ ] Credentials received
- [ ] No duplicate processing

</Accordion>

---

## Go-Live Checklist

Use this checklist before moving to production:

### OAuth Integration — Go-Live Checklist

- [ ] **Legal Agreements**
  - [ ] Partner Reseller Agreement signed
  - [ ] OAuth integration terms accepted
  - [ ] Data Processing Addendum in place

- [ ] **Production Credentials**
  - [ ] Production Client ID obtained from Partner Portal
  - [ ] Production Client Secret obtained
  - [ ] Production redirect URL(s) whitelisted
  - [ ] Credentials stored securely (secrets manager/vault)
  - [ ] No test credentials in production code

- [ ] **OAuth Configuration**
  - [ ] OAuth scope enabled by PayU KAM for production
  - [ ] Production authorization URL configured: `https://onboarding.payu.in/merchant/partner-oauth`
  - [ ] Production API endpoints configured
  - [ ] Redirect URLs use HTTPS
  - [ ] All redirect URLs whitelisted in Partner Portal

- [ ] **Authorization Flow**
  - [ ] Authorization URL construction tested
  - [ ] URL encoding implemented correctly
  - [ ] Merchant login and registration tested
  - [ ] Authorization grant screen tested
  - [ ] Callback handling implemented
  - [ ] Auth code extraction working
  - [ ] State parameter used (recommended for security)

- [ ] **API Integration**
  - [ ] Validate Auth Code API integration complete
  - [ ] Get Merchant Credentials API integration complete (optional)
  - [ ] API error handling implemented
  - [ ] Timeout handling (30 second default)
  - [ ] Retry logic with exponential backoff
  - [ ] Rate limiting handled (429 responses)

- [ ] **Credential Management**
  - [ ] Auth code exchange happens immediately after redirect
  - [ ] Merchant key and salt stored securely
  - [ ] Credentials encrypted at rest
  - [ ] Credentials associated with correct merchant
  - [ ] Credential retrieval tested
  - [ ] No credentials logged in plain text
  - [ ] No credentials exposed to client-side

- [ ] **Payment Integration**
  - [ ] Hash generation using OAuth credentials tested
  - [ ] Test payments successful with OAuth merchant keys
  - [ ] Success callback (SURL) implemented
  - [ ] Failure callback (FURL) implemented
  - [ ] Reverse hash validation implemented
  - [ ] Transaction verification integrated
  - [ ] All payment methods tested

- [ ] **Security Best Practices**
  - [ ] HTTPS enforced on all endpoints
  - [ ] Redirect URLs validated before use
  - [ ] State parameter used to prevent CSRF
  - [ ] Auth codes used only once
  - [ ] Auth code expiry handled
  - [ ] Client secret never exposed to client
  - [ ] XSS protection implemented
  - [ ] SQL injection prevention in place

- [ ] **Error Handling**
  - [ ] Invalid client credentials handled
  - [ ] Expired auth code handled
  - [ ] Used auth code rejection handled
  - [ ] Network errors handled gracefully
  - [ ] User-friendly error messages displayed
  - [ ] Error logging implemented
  - [ ] Alert notifications for critical errors

- [ ] **Data Privacy & Compliance**
  - [ ] GDPR/data privacy compliance verified
  - [ ] User consent captured appropriately
  - [ ] Minimal PII stored
  - [ ] Data retention policy implemented
  - [ ] Right to erasure implemented (if applicable)
  - [ ] Privacy policy updated to mention OAuth

- [ ] **Monitoring & Logging**
  - [ ] OAuth flow events logged
  - [ ] API requests/responses logged (excluding secrets)
  - [ ] Credential storage/retrieval audited
  - [ ] Error tracking system integrated
  - [ ] Performance monitoring setup
  - [ ] Alert notifications configured
  - [ ] Dashboard for merchant onboarding status

- [ ] **Testing Completed**
  - [ ] End-to-end OAuth flow tested in production (test merchants)
  - [ ] Multiple merchant onboarding tested
  - [ ] Payment with OAuth credentials tested
  - [ ] Error scenarios tested
  - [ ] Edge cases validated
  - [ ] Load testing completed

- [ ] **Documentation**
  - [ ] Internal documentation for OAuth flow
  - [ ] Runbooks for common issues
  - [ ] Escalation procedures defined
  - [ ] Knowledge base updated
  - [ ] Training provided to support team

---

## Production URLs Reference

Once all testing is complete and checklist items are verified, update all endpoints to production:

| Resource | Production URL |
|----------|---------------|
| Authorization Page | `https://onboarding.payu.in/merchant/partner-oauth` |
| Validate Auth Code | `https://dashboard.payu.in/oauth/validate-auth-code` |
| Get Merchant Credentials | `https://dashboard.payu.in/oauth/get-merchant-credentials` |
| Payment (Hosted Checkout) | `https://secure.payu.in/_payment` |
| Verify Payment | `https://info.payu.in/merchant/postservice?form=2` |

---

## Common Issues & Troubleshooting

<Accordion title="Issue 1: Authorization URL Not Loading" icon="fa-times-circle">

**Symptoms:** Authorization page shows error or doesn't load

**Possible Causes:**
- Invalid Client ID
- Client ID not enabled for OAuth
- Redirect URL not properly encoded
- OAuth not enabled for partner account

**Solution:**
1. Verify Client ID is correct
2. Contact PayU KAM to confirm OAuth is enabled
3. Check redirect URL encoding: use `encodeURIComponent()` or equivalent
4. Verify using test environment URL for testing

</Accordion>

<Accordion title="Issue 2: Redirect URL Mismatch Error" icon="fa-times-circle">

**Symptoms:** Error message: "Redirect URL not whitelisted"

**Possible Causes:**
- Redirect URL not whitelisted in Partner Portal
- URL encoding mismatch (encoded vs decoded)
- HTTP vs HTTPS mismatch
- Trailing slash mismatch

**Solution:**
1. Log in to Partner Portal → Settings → OAuth Configuration
2. Add exact redirect URL to whitelist (including protocol and path)
3. Ensure URL in authorization request matches exactly
4. Use HTTPS for all redirect URLs
5. Be consistent with trailing slashes

**Examples:**
```
✅ Correct: https://partner.example.com/callback
❌ Wrong: http://partner.example.com/callback (HTTP instead of HTTPS)

✅ Correct: https://partner.example.com/callback/
❌ Wrong: https://partner.example.com/callback (missing trailing slash if whitelisted with it)
```

</Accordion>

<Accordion title="Issue 3: Invalid Auth Code" icon="fa-times-circle">

**Symptoms:** "Invalid auth code" error when calling Validate Auth Code API

**Possible Causes:**
- Auth code already used
- Auth code expired
- Incorrect auth code copied from URL
- Special characters not handled properly

**Solution:**
1. Extract auth code immediately from redirect URL
2. Exchange auth code within 5 minutes of receiving it
3. Use auth code only once
4. Handle URL decoding properly if auth code contains special characters
5. Generate new auth code by repeating OAuth flow

</Accordion>

<Accordion title="Issue 4: Merchant Credentials Not Received" icon="fa-times-circle">

**Symptoms:** API returns success but no merchant_key or salt

**Possible Causes:**
- Merchant not fully onboarded
- KYC pending for merchant
- Merchant account not activated

**Solution:**
1. Check merchant status in PayU dashboard
2. Ensure merchant completed KYC
3. Wait for merchant approval (if under review)
4. Contact PayU support if merchant shows as active but credentials not received

</Accordion>

<Accordion title="Issue 5: Hash Mismatch in Payment" icon="fa-times-circle">

**Symptoms:** Payment page shows "Invalid hash" error

**Possible Causes:**
- Using incorrect merchant_key or salt
- Parameter order wrong in hash string
- Extra spaces in hash string
- Incorrect salt retrieved
- Using test credentials in production

**Solution:**
1. Verify merchant_key and salt from OAuth are correct
2. Check hash string parameter order:
   ```
   key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT
   ```
3. Use lowercase hash: `strtolower(hash('sha512', $hashString))`
4. Trim all parameters to remove spaces
5. Verify using production credentials in production environment
6. Use [PayU Hash Verification Tool](https://test.payu.in/merchant/postservice?form=2) to test

</Accordion>

<Accordion title="Issue 6: Payment Callback Not Received" icon="fa-times-circle">

**Symptoms:** Payment completed but SURL/FURL not triggered

**Possible Causes:**
- SURL/FURL not publicly accessible
- Firewall blocking PayU servers
- Incorrect URL in payment request
- Server timeout during callback

**Solution:**
1. Verify SURL/FURL are publicly accessible (use external tools to test)
2. Whitelist PayU IP ranges in firewall
3. Ensure URLs use HTTPS
4. Check server logs for incoming requests
5. Implement Verify Payment API as fallback
6. Return HTTP 200 OK quickly in callback handler

</Accordion>

<Accordion title="Issue 7: Multiple OAuth Sessions Confusion" icon="fa-times-circle">

**Symptoms:** Wrong merchant credentials stored or retrieved

**Possible Causes:**
- Session management issues
- State parameter not used
- Concurrent OAuth flows not handled
- Cache issues

**Solution:**
1. Use `state` parameter in authorization URL:
   ```
   https://onboarding.payu.in/merchant/partner-oauth?client_id=ABC&redirect_url=...&state=SESSION_ID
   ```
2. Verify state parameter in callback matches session
3. Store credentials immediately after receiving
4. Use unique identifiers to track each OAuth flow
5. Implement proper session management

</Accordion>

<Accordion title="Issue 8: Auth Code Expiry" icon="fa-times-circle">

**Symptoms:** Auth code rejected even when exchanged quickly

**Possible Causes:**
- Auth code expired (5-minute window)
- Clock skew between servers

**Solution:**
1. Exchange auth code immediately after redirect — do not store or delay
2. Auth codes are valid for 5 minutes only
3. Ensure server clocks are synchronized (NTP)
4. Generate a new auth code by restarting the OAuth flow

</Accordion>

---

## Performance Optimization

<Accordion title="Best Practices" icon="fa-list-check">

1. **Parallel Processing**
   - Process multiple OAuth flows concurrently
   - Use asynchronous API calls where possible
   - Implement queuing for credential storage

2. **Caching**
   - Cache merchant credentials securely
   - Cache frequently accessed data
   - Use Redis or similar for session management

3. **Database Optimization**
   - Index merchant_key and client_id columns
   - Use connection pooling
   - Optimize credential retrieval queries

4. **API Call Optimization**
   - Batch credential retrievals if possible
   - Implement exponential backoff for retries
   - Set appropriate timeouts (30 seconds recommended)

5. **Monitoring**
   - Track OAuth flow completion rates
   - Monitor API response times
   - Set up alerts for high error rates
   - Track credential storage success rates

</Accordion>

---

## Security Checklist

- [ ] **Transport Security**
  - [ ] All OAuth URLs use HTTPS
  - [ ] TLS 1.2 or higher enforced
  - [ ] Valid SSL certificates installed
  - [ ] HSTS headers configured

- [ ] **Data Protection**
  - [ ] Client secret stored in secrets manager (AWS Secrets Manager, HashiCorp Vault, etc.)
  - [ ] Merchant credentials encrypted at rest (AES-256)
  - [ ] Encryption keys rotated regularly
  - [ ] No credentials in application logs
  - [ ] No credentials in error messages

- [ ] **Access Control**
  - [ ] Role-based access control (RBAC) implemented
  - [ ] API endpoints require authentication
  - [ ] Admin access audited
  - [ ] Principle of least privilege applied

- [ ] **CSRF Protection**
  - [ ] State parameter used in OAuth flow
  - [ ] State parameter validated in callback
  - [ ] CSRF tokens on all forms
  - [ ] SameSite cookie attribute set

- [ ] **Input Validation**
  - [ ] Auth code validated before use
  - [ ] Client ID and Secret validated
  - [ ] Redirect URL validated against whitelist
  - [ ] All user inputs sanitized

- [ ] **Rate Limiting**
  - [ ] API rate limits implemented
  - [ ] Brute force protection on OAuth endpoints
  - [ ] IP-based rate limiting
  - [ ] Account lockout after multiple failures

- [ ] **Audit Logging**
  - [ ] All OAuth events logged
  - [ ] Credential access logged
  - [ ] Failed authentication attempts logged
  - [ ] Logs retained according to policy
  - [ ] Log tampering protection

---

## Support & Escalation

<Accordion title="When to Contact PayU Support" icon="fa-list-check">

Contact PayU support in these scenarios:
- OAuth not enabled for your partner account
- Redirect URL whitelisting issues
- Merchant credentials not received despite successful OAuth
- Repeated API failures (not related to your implementation)
- Security concerns or suspected compromise

</Accordion>

<Accordion title="Contact Information" icon="fa-list-check">

- **Partner Support Email:** partner-support@payu.in
- **Technical Support:** tech-support@payu.in
- **Key Account Manager:** (provided during onboarding)

</Accordion>

<Accordion title="Information to Provide When Contacting Support" icon="fa-list-check">

When contacting support, include:
1. Partner Client ID (never share Client Secret)
2. Timestamp of issue
3. Error messages received
4. API request/response (redact sensitive data)
5. Steps to reproduce
6. Environment (test/production)

</Accordion>

---

> 🚧 **Important**
>
> Always test thoroughly in the test environment before going live. Conduct small-scale production testing with a few merchants before full rollout.

> 📘 **Best Practice**
>
> Implement comprehensive logging and monitoring to quickly identify and resolve issues. Set up alerts for high error rates or unusual patterns.

> 🔒 **Security Reminder**
>
> Never share your Client Secret, merchant keys, or salts in logs, error messages, or support tickets. Treat them as passwords.
