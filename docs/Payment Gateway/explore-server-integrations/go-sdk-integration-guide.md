---
title: Go SDK - Integration Guide
deprecated: false
hidden: true
metadata:
  robots: index
---
This guide covers the PayU Go SDK integration workflow. Before implementing:

1. **Verify all SDK methods** against your installed SDK version
2. **Test hash calculation** with PayU's official payment specification
3. **Consult the official PayU documentation** at [https://docs.payu.in](https://docs.payu.in)
4. **Test all code examples** in your environment before production use

This guide provides workflow guidance and conceptual examples. Always verify technical implementation details with:

- Official PayU SDK source: [https://github.com/payu-india/web-sdk-go](https://github.com/payu-india/web-sdk-go)
- PayU API documentation: [https://docs.payu.in](https://docs.payu.in)
- Your SDK version's changelog and method signatures

***

## Quick Navigation

**First time?** → [Quick Start (5 Minutes)](#quick-start-5-minutes)<br />**Need troubleshooting?** → [Troubleshooting](#troubleshooting)<br />**Ready to go live?** → [Production Readiness](#production-readiness-checklist)

***

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites & Setup](#prerequisites--setup)
3. [Quick Start (5 Minutes)](#quick-start-5-minutes)
4. [Installation & Verification](#installation--verification)
5. [SDK Initialization with Merchant Credentials](#sdk-initialization-with-merchant-credentials)
6. [Payment Integration Workflow](#payment-integration-workflow)
7. [Handling Payment Responses](#handling-payment-responses)
8. [Webhook Integration](#webhook-integration)
9. [Testing Guide](#testing-guide)
10. [Payment Lifecycle & Reconciliation](#payment-lifecycle--reconciliation)
11. [Production Readiness](#production-readiness-checklist)
12. [Troubleshooting](#troubleshooting)
13. [API Methods Reference](#api-methods-reference)
14. [FAQ](#faq)

***

## Overview

### What the PayU Go SDK Does

The PayU Go SDK is a server-side library that integrates PayU's payment processing into Go applications.

**Core Capabilities:**

- Redirect customers to PayU's hosted checkout
- Process payment responses from PayU
- Verify payment authenticity via hash validation
- Query payment status
- Manage refunds and settlements
- Check payment method availability

**Important:** Verify your SDK version supports each feature before implementing.

### When to Use This SDK

✅ **Use this SDK if:**

- Your backend is written in Go
- You want PayU to host the payment form (reduces PCI compliance burden)
- You need server-side payment verification

❌ **Don't use this SDK if:**

- Your frontend is JavaScript/React and you want client-side integration → Use Web SDK
- Your app is Android → Use Android SDK
- Your app is iOS → Use iOS SDK

### Supported Payment Methods

The SDK works with any payment method enabled in your PayU Dashboard:

- Cards (Debit, Credit, Co-branded)
- UPI
- Net Banking
- Digital Wallets
- EMI/Installments
- BNPL options

Verify which methods are actually configured in your PayU account.

***

## Prerequisites & Setup

### 1. PayU Merchant Account

- [ ] **PayU Merchant Account** — [Create here](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard)
- [ ] **Test Credentials** — Available from Dashboard (Test Mode)
- [ ] **Live Credentials** — Only after account approval

### 2. Get Your Credentials

**For Testing:**

1. Log in to PayU Dashboard
2. Switch to **Test Mode**
3. Go to **Developers** → **API Keys**
4. Copy **Merchant Key** and **Merchant Salt**

**For Production:**

1. Switch to **Live Mode**
2. Go to **Developers** → **API Keys**
3. Copy **Merchant Key** and **Merchant Salt**

**CRITICAL:** Never hardcode credentials. Use environment variables.

### 3. Technical Requirements

- Go 1.18 or higher
- go.mod initialized
- Outbound HTTPS access to PayU servers
- Publicly accessible callback/webhook URLs (HTTPS only)

### 4. Environment Setup

```bash
# For testing
export PAYU_MERCHANT_KEY="your_test_key"
export PAYU_MERCHANT_SALT="your_test_salt"
export PAYU_ENV="test"

# For production (use a secrets manager in real environments)
# export PAYU_MERCHANT_KEY="your_live_key"
# export PAYU_MERCHANT_SALT="your_live_salt"
# export PAYU_ENV="production"
```

***

## Quick Start (5 Minutes)

### Goal

Verify the SDK is installed and your client can be initialized.

### Step 1: Install the SDK

```bash
go get github.com/payu-india/web-sdk-go
go mod tidy
```

### Step 2: Initialize the Client

Create `main.go`:

```go
package main

import (
	"log"
	"os"

	payu "github.com/payu-india/web-sdk-go"
)

func main() {
	// Load credentials from environment
	merchantKey := os.Getenv("PAYU_MERCHANT_KEY")
	merchantSalt := os.Getenv("PAYU_MERCHANT_SALT")
	environment := os.Getenv("PAYU_ENV")

	if merchantKey == "" || merchantSalt == "" {
		log.Fatal("❌ PAYU_MERCHANT_KEY and PAYU_MERCHANT_SALT must be set")
	}

	if environment == "" {
		environment = "test"
	}

	// Initialize PayU client
	client, err := payu.NewClient(merchantKey, merchantSalt, environment)
	if err != nil {
		log.Fatalf("❌ Failed to initialize: %v", err)
	}

	log.Println("✅ PayU client initialized successfully")
}
```

### Step 3: Run It

```bash
export PAYU_MERCHANT_KEY="your_test_key"
export PAYU_MERCHANT_SALT="your_test_salt"
export PAYU_ENV="test"

go run main.go
```

**Expected:** ✅ `PayU client initialized successfully`

***

## Installation & Verification

### Step 1: Download the Module

```bash
go get github.com/payu-india/web-sdk-go
```

### Step 2: Update Dependencies

```bash
go mod tidy
go mod verify
```

### Step 3: Verify Installation

```bash
go list -m github.com/payu-india/web-sdk-go
```

***

## SDK Initialization with Merchant Credentials

### Initialize the Client

Initialize the client **once** when your application starts:

```go
package main

import (
	"log"
	"os"

	payu "github.com/payu-india/web-sdk-go"
)

var payuClient *payu.Client

func init() {
	var err error

	merchantKey := os.Getenv("PAYU_MERCHANT_KEY")
	merchantSalt := os.Getenv("PAYU_MERCHANT_SALT")
	environment := os.Getenv("PAYU_ENV")

	if environment == "" {
		environment = "test" // Default to sandbox
	}

	payuClient, err = payu.NewClient(merchantKey, merchantSalt, environment)
	if err != nil {
		log.Fatalf("❌ Failed to initialize PayU: %v", err)
	}

	log.Printf("✅ PayU client initialized (%s)", environment)
}

func main() {
	log.Println("Application running with PayU ready")
}
```

### Environment Parameter

| Value          | Purpose                   | Server       |
| -------------- | ------------------------- | ------------ |
| `"test"`       | Sandbox (no real charges) | test.payu.in |
| `"production"` | Live (real payments)      | payu.in      |

**Always test thoroughly with "test" before using "production".**

***

## Payment Integration Workflow

### Understanding the Payment Flow

```
1. Customer clicks "Pay Now"
2. Your app creates payment request
3. Your app generates security hash
4. Your app redirects to PayU checkout
5. Customer enters payment details on PayU
6. PayU processes payment
7. PayU redirects to your success/failure URL
8. Your app verifies response hash
9. Your app updates order database
```

### Step 1: Create a Payment Request

Build payment request with order and customer information:

```go
package main

import (
	"fmt"
	"time"
)

type PaymentRequest struct {
	MerchantKey string
	Key         string // Merchant key
	Txnid       string // Unique order ID
	Amount      string // Amount as string (e.g., "999.99")
	ProductInfo string // What's being purchased
	FirstName   string // Customer name
	Email       string // Customer email
	Phone       string // Customer phone (10 digits)
	Surl        string // Success URL (HTTPS)
	Furl        string // Failure URL (HTTPS)
	Curl        string // Callback/webhook URL (optional)
	Hash        string // Will be set after hash generation
}

func CreatePaymentRequest(merchantKey string) *PaymentRequest {
	return &PaymentRequest{
		Key:         merchantKey,
		Txnid:       fmt.Sprintf("ORD-%d", time.Now().Unix()), // Unique ID
		Amount:      "100.00", // Must be string with 2 decimals
		ProductInfo: "Test Product",
		FirstName:   "John",
		Email:       "john@example.com",
		Phone:       "9876543210",
		Surl:        "https://yoursite.com/payment/success",
		Furl:        "https://yoursite.com/payment/failure",
		Curl:        "https://yoursite.com/webhook/payu",
	}
}
```

### Step 2: Generate Security Hash

**CRITICAL:** The hash implementation is security-sensitive.

**Before implementing:**

1. Consult PayU's official payment specification for hash field order
2. Verify your SDK documentation for hash method details
3. Test hash generation with PayU's test environment

**Pseudo-code for hash generation:**

```
Hash input fields (verify exact order with PayU spec):
key|txnid|amount|productinfo|firstname|email|udf1|salt

Generate: SHA512 hash of above string
Result: Hex-encoded hash string
```

**Important:** Never hardcode hash logic without verifying against:

- Official PayU API specification
- Your SDK's hash method (if provided)
- PayU's test credentials

### Step 3: Redirect to PayU Checkout

After hash generation, redirect the customer to PayU's checkout:

```go
func redirectToCheckout(paymentRequest *PaymentRequest) string {
	// Pseudo-code: refer to your SDK's documentation
	// This should be replaced with actual SDK method
	
	environment := "test" // or "production"
	baseURL := "https://test.payu.in"
	
	if environment == "production" {
		baseURL = "https://payu.in"
	}
	
	checkoutURL := fmt.Sprintf(
		"%s/?key=%s&hash=%s&txnid=%s&amount=%s&productinfo=%s&firstname=%s&email=%s&phone=%s&surl=%s&furl=%s",
		baseURL,
		paymentRequest.Key,
		paymentRequest.Hash,
		paymentRequest.Txnid,
		paymentRequest.Amount,
		paymentRequest.ProductInfo,
		paymentRequest.FirstName,
		paymentRequest.Email,
		paymentRequest.Phone,
		paymentRequest.Surl,
		paymentRequest.Furl,
	)
	
	return checkoutURL
}
```

***

## Handling Payment Responses

### Step 1: Receive the Response

After payment, PayU redirects to your success or failure URL with a response.

**CRITICAL STEP:** You must verify the response hash to prevent fraud.

```go
package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

func PaymentSuccessHandler(w http.ResponseWriter, r *http.Request) {
	responseJSON := r.FormValue("response")

	// STEP 1: Parse response
	var response map[string]interface{}
	err := json.Unmarshal([]byte(responseJSON), &response)
	if err != nil {
		log.Printf("❌ Failed to parse response: %v", err)
		http.Error(w, "Invalid response", http.StatusBadRequest)
		return
	}

	// STEP 2: Verify hash (prevent fraud)
	if !verifyResponseHash(response) {
		log.Printf("❌ Hash verification failed - rejecting response")
		http.Error(w, "Hash verification failed", http.StatusUnauthorized)
		return
	}

	log.Printf("✅ Hash verified - response is authentic")

	// STEP 3: Check payment status
	status, ok := response["status"].(string)
	if !ok || status != "success" {
		log.Printf("❌ Payment failed or pending")
		http.Redirect(w, r, "/payment/failed", http.StatusSeeOther)
		return
	}

	// STEP 4: Update database
	txnid, _ := response["txnid"].(string)
	log.Printf("✅ Payment successful: %s", txnid)
	
	// TODO: updateOrderStatus(txnid, "PAID")
	// TODO: sendConfirmationEmail(email)

	http.Redirect(w, r, "/payment/success", http.StatusSeeOther)
}

func verifyResponseHash(response map[string]interface{}) bool {
	// Hash verification is CRITICAL and security-sensitive
	// 
	// Before implementing:
	// 1. Verify expected field order with PayU spec
	// 2. Check your SDK's hash verification method
	// 3. Test with PayU's test environment
	//
	// Pseudo-code:
	// 1. Extract hash from response
	// 2. Rebuild hash from fields in correct order
	// 3. Compare hashes
	//
	// Return true only if hashes match exactly

	// TODO: Implement hash verification
	return true // Placeholder
}
```

***

## Webhook Integration

### Why Webhooks Matter

Webhooks are automatic notifications from PayU when payment status changes. They're more reliable than redirect URLs because they don't depend on the user's browser.

### Enable Webhook in PayU Dashboard

1. Go to **Settings → Webhooks**
2. Enter your endpoint: `https://yoursite.com/webhook/payu`
3. Must be HTTPS (not HTTP)
4. Must be publicly accessible

### Create Webhook Handler

```go
package main

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"
)

func WebhookHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "POST only", http.StatusMethodNotAllowed)
		return
	}

	// Read webhook body
	body, err := ioutil.ReadAll(r.Body)
	if err != nil {
		log.Printf("❌ Failed to read webhook: %v", err)
		w.WriteHeader(http.StatusBadRequest)
		return
	}
	defer r.Body.Close()

	// Parse webhook
	var payload map[string]interface{}
	err = json.Unmarshal(body, &payload)
	if err != nil {
		log.Printf("❌ Invalid webhook JSON: %v", err)
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	log.Printf("📬 Webhook received: %v", payload["txnid"])

	// CRITICAL: Verify webhook hash (same as response hash)
	if !verifyWebhookHash(payload) {
		log.Printf("❌ Webhook hash verification failed")
		w.WriteHeader(http.StatusUnauthorized)
		return
	}

	// Handle payment status
	status, _ := payload["status"].(string)
	txnid, _ := payload["txnid"].(string)

	switch status {
	case "success":
		log.Printf("✅ Payment successful: %s", txnid)
		// TODO: updateOrderStatus(txnid, "PAID")

	case "failed":
		log.Printf("❌ Payment failed: %s", txnid)
		// TODO: updateOrderStatus(txnid, "FAILED")

	case "pending":
		log.Printf("⏳ Payment pending: %s", txnid)
		// TODO: updateOrderStatus(txnid, "PENDING")
	}

	// Always return 200 OK
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(map[string]string{"status": "received"})
}

func verifyWebhookHash(payload map[string]interface{}) bool {
	// Same hash verification as payment response
	// Verify against PayU specification before implementing
	return true // Placeholder
}
```

***

## Testing Guide

### Understand Test Environment

- No real money charged
- Instant transaction processing
- Use test credentials only
- Use test card numbers only

### Get Test Credentials

1. Log in to PayU Dashboard
2. Switch to **Test Mode**
3. Go to **Developers → API Keys**
4. Copy credentials

### Test Credentials

**Net Banking (Works in test mode):**

```
Username: payu
Password: payu
OTP: 123456
```

**Test Cards (EMI):**

- Kotak DC EMI: 4706-1378-0509-9594
- AXIS DC EMI: 4011-5100-0000-0007
- HDFC CC EMI: 4453-3410-65876437
- ICICI CC EMI: 4453-3410-65876437

(For all: Expiry = any future date, CVV = 123, OTP = 111111)

**Test Wallets:**

- PayTM: 7777777777 / 888888
- PhonePe: Use their pre-prod app
- Amazon Pay: Use real account

**Note:** UPI in-app and intent flows NOT available in test mode. Use Net Banking instead.

### Test Payment Flow

Before going live, verify:

- [ ] Payment request created successfully
- [ ] Hash generated without errors
- [ ] Checkout URL contains "test.payu.in" (not "payu.in")
- [ ] Payment completed successfully
- [ ] Success/failure URL was called
- [ ] Response hash was verified
- [ ] Order status updated in database
- [ ] Webhook received (if enabled)

***

## Payment Lifecycle & Reconciliation

### Payment States

Payments move through these states:

```
initiated
    ↓
pending (waiting for bank)
    ↓
success (payment complete)
  OR
failed (payment rejected)
  OR
cancelled (user cancelled)
    ↓
(optional) refunded
```

### Critical: Handling Asynchronous Payments

Payments are asynchronous. Customer may:

1. Close browser before success URL is called
2. Internet connection drops
3. Webhook delivery delayed

**Solution:** Implement **reconciliation strategy**

```go
// Reconciliation approach:
// 1. When order is created, mark as "PENDING_PAYMENT"
// 2. When callback/webhook received, update to PAID/FAILED
// 3. Periodically (every hour), verify pending payments:

func ReconcilePayments() {
	// Pseudo-code
	pendingOrders := getAllOrdersWithStatus("PENDING_PAYMENT")
	
	for _, order := range pendingOrders {
		// Check if payment was actually successful
		// Use SDK's verify payment method (if available)
		// or PayU's status API
		
		actualStatus := queryPaymentStatus(order.TransactionID)
		
		if actualStatus == "success" {
			updateOrderStatus(order.ID, "PAID")
		} else if time.Since(order.CreatedAt) > 24*time.Hour {
			updateOrderStatus(order.ID, "FAILED")
		}
	}
}
```

### Idempotency: Handling Duplicate Notifications

PayU may send the same webhook multiple times.

**Solution:** Track processed transactions

```go
// Check if already processed
if isTransactionProcessed(txnid) {
	log.Printf("Already processed: %s, ignoring duplicate", txnid)
	return
}

// Mark as processed
markTransactionProcessed(txnid)

// Now handle the transaction
updateOrderStatus(txnid, "PAID")
```

***

## Production Readiness Checklist

### Phase 1: Verification

- [ ] All SDK methods verified in actual SDK code
- [ ] Hash implementation validated against PayU specification
- [ ] Code examples tested in your environment
- [ ] All errors handled properly (no ignored errors)
- [ ] Credentials stored in environment variables (not hardcoded)

### Phase 2: Security

- [ ] Response hash verification implemented
- [ ] Webhook hash verification implemented
- [ ] No sensitive data logged
- [ ] Credentials in secrets manager (not in code)
- [ ] HTTPS enforced for all payment URLs

### Phase 3: Operational

- [ ] Reconciliation strategy implemented
- [ ] Duplicate detection implemented
- [ ] Timeout handling implemented (>24 hrs pending)
- [ ] All payment states handled (success, failed, pending, cancelled)
- [ ] Error messages don't expose sensitive data

### Phase 4: Testing

- [ ] End-to-end test with live credentials
- [ ] Payment succeeded and order updated
- [ ] Webhook received
- [ ] Response hash verified correctly

### Phase 5: Go-Live

- [ ] Code reviewed by team
- [ ] Switch to production credentials
- [ ] Change environment from "test" to "production"
- [ ] Monitor first 100 transactions
- [ ] Check settlement reports

***

## Troubleshooting

### Initialization Fails

**Error:** `Failed to initialize PayU client`

**Check:**

1. Is `PAYU_MERCHANT_KEY` set? `echo $PAYU_MERCHANT_KEY`
2. Is `PAYU_MERCHANT_SALT` set? `echo $PAYU_MERCHANT_SALT`
3. Are values non-empty? `[ -z "$PAYU_MERCHANT_KEY" ] && echo "EMPTY"`
4. Do they match your PayU account? (Test vs Live)

***

### Hash Verification Fails

**Error:** `Hash verification failed`

**Check:**

1. Verify hash field order matches PayU specification
2. Verify amount has exactly 2 decimal places (999.99, not 999.9)
3. Verify salt is correct
4. Verify all fields are included in hash (even empty ones)

**Before going live:** Validate hash implementation with PayU support.

***

### Response/Webhook Not Received

**Check:**

1. Is your URL publicly accessible? `curl -I https://yoursite.com/webhook/payu`
2. Does it return 200 or 405? (Not 404 or 500)
3. Is webhook enabled in PayU Dashboard?
4. Is URL HTTPS (not HTTP)?

***

### Payment Stuck in Pending State

**Check:**

1. Use reconciliation to query actual payment status
2. Check PayU Dashboard → Reports → Transactions
3. Verify settlement details
4. If payment succeeded but order not updated, manually reconcile

***

### Duplicate Orders Created

**Check:**

1. Use unique transaction ID for each payment
2. Check for duplicate txnid submissions
3. Implement idempotency (detect duplicate webhooks)

***

## API Methods Reference

### Initialization

```go
// Initialize PayU client
client, err := payu.NewClient(
    merchantKey string,
    merchantSalt string,
    environment string, // "test" or "production"
) (*payu.Client, error)
```

**Verify all available methods in your SDK version before use.**

Potential methods (verify in your SDK):

- NewClient()
- GetPaymentURL()
- VerifyPaymentHash()
- ParsePaymentResponse()
- VerifyPayment()
- CreateRefund()
- GetRefundStatus()
- GetSettlements()

**Important:** Before using any method, verify it exists in your SDK version by:

1. Checking SDK source code
2. Running `go doc` on the SDK
3. Checking official documentation

***

## FAQ

### Q: Do I need PCI compliance?

**A:** No. The hosted checkout means you never handle raw credit card data.

***

### Q: Can I test with real card numbers?

**A:** No. Test mode only accepts the test credentials provided.

***

### Q: What if webhook delivery fails?

**A:** Use reconciliation strategy (query payment status periodically).

***

### Q: How long does payment take?

**A:** Usually seconds to minutes, but can take longer for some banks.

***

### Q: When do I receive the funds?

**A:** Check PayU Dashboard → Reports → Settlements. Usually T+1 or T+2 business days.

***

### Q: What should I do if payment response is not received?

**A:**

1. Don't update order status immediately based only on callback
2. Use reconciliation (verify status periodically)
3. Implement timeout handling (mark as failed if pending >24hrs)

***

## Support & Next Steps

### Official Resources

- PayU Documentation: [https://docs.payu.in](https://docs.payu.in)
- PayU Dashboard: [https://payumoney.com](https://payumoney.com)
- SDK Repository: [https://github.com/payu-india/web-sdk-go](https://github.com/payu-india/web-sdk-go)
- Support: [support@payu.in](mailto:support@payu.in)

### Before Implementing

1. **Verify all SDK methods** exist in your version
2. **Test hash calculation** with PayU's test environment
3. **Read PayU's official documentation** for payment specification
4. **Consult with PayU support** before going live

### Before Going Live

1. **Code review** by another engineer
2. **Test all payment scenarios** (success, failure, pending, timeout)
3. **Verify reconciliation** works correctly
4. **Monitor first transactions** closely
5. **Check settlements** match your records

<br />
