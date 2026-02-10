---
title: General API Testing
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: General API Testing
excerpt: >-
  Comprehensive guide to testing PayU APIs effectively. Learn best practices,
  tools, and methodologies to ensure robust and reliable API integrations.
deprecated: false
hidden: false
metadata:
  title: General API Testing - PayU Developer Docs
  description: >-
    Learn how to test PayU APIs effectively with best practices, tools, and
    methodologies. Includes authentication setup, test environments, and
    comprehensive testing workflows.
  keywords:
    - PayU API testing
    - API testing guide
    - PayU integration testing
    - Test PayU APIs
    - API test environment
    - PayU sandbox testing
  robots: index
next:
  description: ''
---

Effective API testing is a critical component of any successful integration with PayU services. This guide provides best practices, tools, and methodologies to ensure your API implementations are robust and reliable.

## Getting Started with API Testing

This section guides you through setting up your environment for testing PayU APIs.

## Setting up the Test Environment

**Authentication:** PayU APIs use two primary authentication methods:

1. **Hash-based Authentication (SHA512)**: Used for Payment APIs and General APIs
   * Requires `merchant_key` and `salt`
   * Hash must be calculated using specific formulas based on API type
   * Refer to our [API Authentication and Security](/docs/api-authentication-and-security) guide for detailed instructions

2. **OAuth 2.0 Authentication**: Used for Payment Links API and newer REST APIs
   * Requires `client_id` and `client_secret`
   * Uses OAuth 2.0 Client Credentials flow
   * Access tokens are valid for a limited time (typically 3600 seconds)

**Test Data:** Some API calls may require existing resources (a merchant key, transaction ID, or payment link ID). You may need to create these resources first through the PayU Dashboard or via the API. Refer to the specific API's documentation for guidance on what data is needed for your test cases.

**Test Credentials:** For testing purposes, you can use test merchant keys and salts. For Integration APIs, use "JPTXg" as the Test merchant key. Refer to [Generate Test Merchant Key and Salt](/docs/generate-test-merchant-key-and-salt) for detailed instructions.

**Common Inputs:** Before you start testing, gather the following common inputs:

* **API Endpoint URL:** The base URL for the service you are testing (e.g., `https://test.payu.in/_payment` for Payment APIs).
* **Authentication Credentials:**
  * For Hash-based APIs: `merchant_key` and `salt`
  * For OAuth APIs: `client_id` and `client_secret`
* **Resource Identifiers:** Transaction IDs, payment link IDs, or merchant IDs for any existing resources you will be interacting with.
* **Request Body Payloads:** JSON or form-encoded payloads for POST or PUT requests, structured according to the API specification.

## Testing Environments

PayU provides separate test and production environments for your API integration:

| Environment    | Purpose                 | Base URLs                                                                                                                                                                                                           |
| -------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test**       | Development and testing | Payment APIs: `https://test.payu.in/_payment`<br />General APIs: `https://test.payu.in/merchant/postservice.php?form=2`<br />Payment Links: `https://uatoneapi.payu.in`<br />Payouts: `https://uat-payouts.payu.in` |
| **Production** | Live transactions       | Payment APIs: `https://secure.payu.in/_payment`<br />General APIs: `https://info.payu.in/merchant/postservice.php?form=2`<br />Payment Links: `https://oneapi.payu.in`<br />Payouts: `https://payouts.payu.in`      |

To use these environments, you'll need to:

* **Test Environment:** Generate test credentials via the PayU Dashboard or use default test keys
* **Production Environment:** Complete KYC verification and obtain production credentials from the PayU Dashboard

<Callout icon="📘" theme="info">
  **Important:** Always use matching credentials and endpoints for your target environment. Using test credentials with production endpoints (or vice versa) will result in authentication failures.
</Callout>

## Recommended Testing Tools

We recommend the following tools for testing PayU APIs:

* **Postman**: Create and share API collections for manual and automated testing
* **cURL**: Command-line tool for quick API interaction
* **Jest/Mocha**: JavaScript testing frameworks for automated tests
* **Python Requests**: Simple HTTP library for Python-based testing
* **PayU Hash Verification Tool**: Use the [PayU Hash Verification Tool](/docs/using-payu-hash-verification-tool) to validate your hash calculations

## Testing Workflow

### Validate Authentication

#### For Hash-based APIs (Payment APIs and General APIs)

```python
import hashlib
import requests

# Test hash generation for Payment API
def generate_payment_hash(key, txnid, amount, productinfo, firstname, email, salt, udf1="", udf2="", udf3="", udf4="", udf5=""):
    hash_string = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{salt}"
    return hashlib.sha512(hash_string.encode()).hexdigest()

# Test hash generation for General APIs
def generate_general_hash(key, command, var1, salt):
    hash_string = f"{key}|{command}|{var1}|{salt}"
    return hashlib.sha512(hash_string.encode()).hexdigest()

# Test credentials
test_key = "JPTXg"  # Test merchant key
test_salt = "YOUR_TEST_SALT"
test_txnid = "TXN123456789"
test_amount = "100.00"
test_productinfo = "Test Product"
test_firstname = "Test"
test_email = "test@example.com"

# Generate hash
hash_value = generate_payment_hash(
    test_key, test_txnid, test_amount, test_productinfo, 
    test_firstname, test_email, test_salt
)

print("Generated Hash:", hash_value)
print("Hash Length:", len(hash_value))  # Should be 128 characters for SHA512
```

#### For OAuth 2.0 APIs (Payment Links API)

```python
import requests

# OAuth 2.0 authentication test
auth_url = "https://uat-accounts.payu.in/oauth/token"
auth_payload = {
    "grant_type": "client_credentials",
    "client_id": "<your_client_id>",
    "client_secret": "<your_client_secret>"
}

response = requests.post(auth_url, data=auth_payload)
data = response.json()

print("Status code:", response.status_code)
print("Access token:", data.get("access_token"))
print("Token type:", data.get("token_type"))
print("Expires in:", data.get("expires_in"), "seconds")
```

### Create Comprehensive Test Scenarios

Create comprehensive test scenarios that cover complete user journeys:

* **Payment Flow:**
  * Initiate a payment transaction
  * Verify payment status
  * Handle payment success/failure callbacks
  * Process refunds (if applicable)

* **Payment Links Flow:**
  * Create a payment link
  * Share payment link
  * Query payment link status
  * Update payment link configuration
  * Expire or delete payment link

* **Transaction Management:**
  * Verify transaction details
  * Check transaction status
  * Retrieve transaction history
  * Process refunds

#### Example: Complete Payment API Test

```python
import requests
import hashlib
import json

# Setup authentication
def generate_hash(key, txnid, amount, productinfo, firstname, email, salt):
    hash_string = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}||||||||{salt}"
    return hashlib.sha512(hash_string.encode()).hexdigest()

# Test credentials
test_key = "JPTXg"
test_salt = "YOUR_TEST_SALT"
base_url = "https://test.payu.in/_payment"

# Payment request payload
txnid = "TXN" + str(int(time.time()))
amount = "100.00"
productinfo = "Test Product"
firstname = "John"
email = "john.doe@example.com"
phone = "9876543210"
surl = "https://merchant.com/success"
furl = "https://merchant.com/failure"

# Generate hash
hash_value = generate_hash(test_key, txnid, amount, productinfo, firstname, email, test_salt)

# Payment request data
payment_data = {
    "key": test_key,
    "txnid": txnid,
    "amount": amount,
    "productinfo": productinfo,
    "firstname": firstname,
    "email": email,
    "phone": phone,
    "surl": surl,
    "furl": furl,
    "hash": hash_value
}

# Test creating a payment
response = requests.post(base_url, data=payment_data)

# Verify response
print("Status code:", response.status_code)
print("Response:", response.text)

# For hosted checkout, PayU redirects to payment page
# For server-to-server, verify the response structure
if response.status_code == 200:
    print("✅ Payment request successful")
    # In hosted checkout, you'll get HTML redirect
    # In S2S, you'll get JSON response
else:
    print("❌ Payment request failed")
```

#### Example: Complete Payment Links API Test

```python
import requests
import json
import time

# Step 1: Get OAuth Token
auth_url = "https://uat-accounts.payu.in/oauth/token"
auth_payload = {
    "grant_type": "client_credentials",
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET"
}

auth_response = requests.post(auth_url, data=auth_payload)
token_data = auth_response.json()
access_token = token_data["access_token"]

# Step 2: Create Payment Link
base_url = "https://uatoneapi.payu.in"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "mid": "YOUR_MERCHANT_ID"
}

payment_link_payload = {
    "amount": "1000.00",
    "description": "Test Payment Link",
    "expiryDate": "2025-12-31T23:59:59Z",
    "customerName": "John Doe",
    "customerEmail": "john.doe@example.com",
    "customerPhone": "9876543210"
}

create_response = requests.post(
    f"{base_url}/partners/payment-links",
    headers=headers,
    data=json.dumps(payment_link_payload)
)

# Verify response
assert create_response.status_code in [200, 201], f"Failed to create payment link: {create_response.text}"
payment_link_data = create_response.json()
payment_link_id = payment_link_data.get("id") or payment_link_data.get("paymentLinkId")

print(f"✅ Payment link created: {payment_link_id}")

# Step 3: Retrieve Payment Link Details
get_response = requests.get(
    f"{base_url}/partners/payment-links/{payment_link_id}",
    headers=headers
)

assert get_response.status_code == 200, f"Failed to retrieve payment link: {get_response.text}"
print("✅ Payment link retrieved successfully")
print(json.dumps(get_response.json(), indent=2))
```

## Test Error Handling

Verify that your application correctly handles API errors:

* **Test with invalid parameters:**
  ```python
  # Test with invalid amount
  invalid_data = {
      "key": test_key,
      "txnid": txnid,
      "amount": "-100",  # Invalid negative amount
      "productinfo": productinfo,
      "firstname": firstname,
      "email": email,
      "hash": hash_value
  }
  response = requests.post(base_url, data=invalid_data)
  # Should return error response
  ```

* **Test with incorrect authentication:**
  ```python
  # Test with wrong merchant key
  wrong_key_data = {
      "key": "WRONG_KEY",
      "txnid": txnid,
      "amount": amount,
      # ... other params
      "hash": "wrong_hash"
  }
  response = requests.post(base_url, data=wrong_key_data)
  # Should return authentication error
  ```

* **Test with expired tokens (OAuth):**
  ```python
  # Use an expired token
  expired_token = "expired_token_here"
  headers = {
      "Authorization": f"Bearer {expired_token}",
      "Content-Type": "application/json"
  }
  response = requests.get(f"{base_url}/partners/payment-links/123", headers=headers)
  # Should return 401 Unauthorized
  assert response.status_code == 401
  ```

* **Verify error response formats:**
  ```python
  # Check error response structure
  error_response = response.json()
  assert "status" in error_response or "error" in error_response
  assert "message" in error_response or "error_description" in error_response
  ```

## Testing Checklist

Use this checklist to ensure comprehensive API testing:

<TestingChecklist />

### Additional Testing Considerations

1. **Hash Validation:**
   * Verify hash calculation matches PayU's expected format
   * Test with empty UDF fields (should use empty pipes)
   * Validate hash length (SHA512 should be 128 characters)
   * Use the [PayU Hash Verification Tool](/docs/using-payu-hash-verification-tool) to validate

2. **Environment Consistency:**
   * Ensure test credentials are used with test endpoints
   * Verify production credentials are used with production endpoints
   * Check that salt values match the environment

3. **Webhook Testing:**
   * Set up webhook endpoints to receive callbacks
   * Test success and failure callbacks
   * Verify webhook signature validation
   * Test webhook retry mechanisms

4. **Edge Cases:**
   * Test with minimum and maximum values
   * Test with special characters in input fields
   * Test with very long strings
   * Test with missing optional parameters
   * Test with invalid data types

## API Product Testing

PayU provides specific testing guides for individual product APIs:

* **Payment APIs Testing** - Testing payment collection APIs (Hosted Checkout, Merchant Hosted, Server-to-Server)
* **Payment Links API Testing** - Testing the Payment Links API for creating and managing payment links
* **General APIs Testing** - Testing transaction verification, refund, and status check APIs
* **Payouts API Testing** - Testing the Payouts API for merchant payouts
* **Subscription APIs Testing** - Testing recurring payment and subscription APIs

Each API type may have specific testing requirements. Refer to the individual API documentation for product-specific examples and best practices.

## Common Testing Scenarios

### Scenario 1: Test Payment Flow End-to-End

```python
# 1. Create payment request
# 2. Submit to PayU
# 3. Simulate payment success callback
# 4. Verify transaction in dashboard
# 5. Test refund if needed
```

### Scenario 2: Test Payment Link Lifecycle

```python
# 1. Create payment link
# 2. Share payment link via email/SMS
# 3. Verify link is accessible
# 4. Complete payment through link
# 5. Verify payment status
# 6. Expire or delete link
```

### Scenario 3: Test Error Recovery

```python
# 1. Simulate network failure
# 2. Test retry mechanism
# 3. Verify idempotency (if applicable)
# 4. Check error logging
```

## Troubleshooting Test Issues

### Common Issues and Solutions

| Issue                        | Likely Cause               | Solution                                         |
| ---------------------------- | -------------------------- | ------------------------------------------------ |
| "Invalid merchant key"       | Credential mismatch        | Verify key matches endpoint environment          |
| "Hash mismatch"              | Incorrect hash calculation | Check hash formula and salt value                |
| "Authentication failed"      | Wrong endpoint/credential  | Check environment consistency                    |
| "Invalid request parameters" | Missing required fields    | Review API documentation for required parameters |
| "Token expired"              | OAuth token expired        | Refresh token using client credentials           |

### Debugging Tips

1. **Enable verbose logging** in your HTTP client to see full request/response
2. **Validate hash calculation** using the PayU Hash Verification Tool
3. **Check request headers** to ensure correct Content-Type and Authorization
4. **Verify environment URLs** match your credentials
5. **Review API documentation** for exact parameter requirements

## Reference

If you encounter issues while testing PayU APIs:

* To generate key/Salt, refer the [Generate Test Merchant Key and Salt](/docs/generate-test-merchant-key-and-salt) section.
* Use the [PayU Hash Verification Tool](/docs/using-payu-hash-verification-tool) to validate hash calculations
* Contact [PayU Support](/docs/contact-payu) for assistance

<br />
