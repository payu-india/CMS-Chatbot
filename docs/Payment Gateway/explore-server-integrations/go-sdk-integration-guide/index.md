---
title: Go SDK
deprecated: false
hidden: true
metadata:
  robots: index
---
Use the PayU Go SDK to integrate PayU payments into your website built using Go. The PayU Go SDK handles low-level API integration details, enabling you to start collecting payments with just a few lines of code and a function call.

***

## Payment Workflow with PayU Go SDK

The PayU Go SDK supports the complete payment lifecycle—from payment initiation to post-payment operations.

<Accordion title="1. Accept Payments" icon="fa-money-check-dollar">
Start collecting payments from customers by creating a payment form.
</Accordion>

<Accordion title="2. Verify Payment Status" icon="fa-circle-check">
After payment completion, verify whether the transaction was successful or check its current status.
</Accordion>

<Accordion title="3. Handle Post-Payment Operations" icon="fa-receipt">
Manage these payment-related operations after a transaction is completed.
- **Handle Refunds:** Initiate or cancel refunds and check refund status.
- **Manage Invoices:** Create or expire invoice links through SDK functions.
</Accordion>

<Accordion title="4. Reconcile Payments" icon="fa-scale-balanced">
Track settlements and ensure payments are settled correctly to your account.
</Accordion>

<Accordion title="5. Optimize Payment Experience" icon="fa-gauge-high">
Improve payment success rates by checking payment availability and offering eligible payment options.
- **Check Bank Downtime Status:** Get information on eligible payment options and PG/bank downtime details.
- **Check Eligibility:** Check customer eligibility for EMI and get the amount according to EMI interest.
</Accordion>

### When to Use This SDK

You can use this SDK when:

✅ Your Backend is Go<br />✅ You want PayU-hosted payment form<br />✅ You need server-side payment verification

These are some of the use cases:

<Accordion title="E-commerce Order Fulfillment Gated on Verified Payment (UrbanCart)" icon="fa-box-open">
UrbanCart, a D2C e-commerce marketplace processing 50,000 orders a day through Go microservices, needs to confirm that a customer's payment has been verified server-side before it reserves inventory permanently and triggers shipment. This happens at the boundary between checkout completion and order fulfillment, and it matters because releasing inventory or shipping against an unconfirmed or reversible payment creates direct financial loss and inventory discrepancies at scale.<br/>

Using PayU Go SDK UrbanCart can:<br/>
- Generate the request hash and build hosted checkout payment requests to securely collect payments at high volume.
- Independently verify transaction status and validate the reverse hash on every callback, rather than trusting the browser redirect alone to confirm a payment before fulfilling an order.
- Use the PayU Go SDK's refund initiation and refund status check to support returns and cancellations.
</Accordion>

<Accordion title="EdTech Enrollment Activation Gated on Confirmed Payment (LearnSphere)" icon="fa-user-graduate">
earnSphere, an EdTech platform selling certification courses priced between ₹15,000–₹1,20,000, needs to activate a learner's enrollment and unlock course content only once payment — including EMI-based payment — is confirmed. This happens between checkout and content access, and it matters because EMI transactions can confirm with a delay, and premature activation risks granting access without settled payment or regulatory-compliant refund handling.<br/>

Using PayU Go SDK LearnSphere can:<br/>
- Check EMI eligibility for the customer's card/bank before checkout to offer EMI as a payment option.
- Generate the hash and create the checkout request for the selected plan to collect payment for a course
- Validate the reverse hash and verify transaction status before touching enrollment state to activate enrollment only on confirmed payment.
- Honor cooling-off-period refund policies by using Go SDK's refund initiation.
</Accordion>

<Accordion title="Travel Booking Confirmation Synchronized with Payment and Supplier Hold (TripWing)" icon="fa-plane-departure">
TripWing, an online travel aggregator booking flights and hotels through a Go orchestration service, needs to confirm payment within a supplier's time-boxed inventory hold window and only then confirm the booking with the airline or hotel. This happens between the inventory hold and supplier confirmation, and it matters because travel inventory is finite and time-sensitive — a slow or unverified payment can mean a customer is charged without a seat or room, or vice versa.<br/>

Using PayU Go SDK TripWing can:<br/>
- Generate the hash and create a checkout request with expiry aligned to that window to collect payment within a supplier hold window.
- Validate the reverse hash and check transaction status before calling the supplier's confirm-booking API to confirm a booking only on verified payments.
- Automatically compensate the customer if a supplier confirmation later fails.
- Check bank/PG downtime status and route customers accordingly to reduce failed payments during peak booking periods.
</Accordion>

***

## Other Options

If you want:

- Frontend JavaScript integration → You can choose Web SDK.
- Mobile app → You can choose Android/iOS SDK.

***

## Supported Payment Methods

_Need Content Here._

## Prerequisites & Setup

### 1. PayU Account

- [ ] Create PayU merchant account
- [ ] Get test credentials (Test Mode)
- [ ] Get live credentials (Live Mode, after approval)

### 2. Credentials

**Get test credentials:**

1. PayU Dashboard → Test Mode
2. Developers → API Keys
3. Copy Merchant Key and Merchant Salt

**Get live credentials:**

1. PayU Dashboard → Live Mode
2. Developers → API Keys
3. Copy Live Merchant Key and Salt

### 3. Technical Requirements

- Go 1.18+
- go.mod initialized
- HTTPS URLs for callbacks/webhooks
- Internet access to PayU servers

### 4. Environment Setup

```bash
# Test environment
export PAYU_MERCHANT_KEY="your_test_key"
export PAYU_MERCHANT_SALT="your_test_salt"
export PAYU_ENV="test"
```

**Never hardcode credentials.**

***

## Quick Start

### Install SDK

```bash
go get github.com/payu-india/web-sdk-go
go mod tidy
```

### Verify Installation

```bash
go list -m github.com/payu-india/web-sdk-go
```

### Initialize Client

```go
package main

import (
	"log"
	"os"

	payu "github.com/payu-india/web-sdk-go"
)

func main() {
	// Load credentials
	key := os.Getenv("PAYU_MERCHANT_KEY")
	salt := os.Getenv("PAYU_MERCHANT_SALT")
	env := os.Getenv("PAYU_ENV")

	if key == "" || salt == "" {
		log.Fatal("PAYU credentials not set")
	}

	if env == "" {
		env = "test"
	}

	// Initialize client
	client, err := payu.NewClient(key, salt, env)
	if err != nil {
		log.Fatalf("Failed to initialize: %v", err)
	}

	log.Println("✅ PayU client ready")
}
```

**Run:**

```bash
go run main.go
```

**Expected:** ✅ `PayU client ready`

***

## Installation & Verification

### Download Module

```bash
go get github.com/payu-india/web-sdk-go
go mod tidy
go mod verify
```

### Check Installation

```bash
go list -m github.com/payu-india/web-sdk-go
```

### Import in Code

```go
import payu "github.com/payu-india/web-sdk-go"
```

***

## SDK Initialization with Merchant Credentials

### Pattern: Initialize Once at Startup

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
	
	key := os.Getenv("PAYU_MERCHANT_KEY")
	salt := os.Getenv("PAYU_MERCHANT_SALT")
	env := os.Getenv("PAYU_ENV")

	if env == "" {
		env = "test"
	}

	payuClient, err = payu.NewClient(key, salt, env)
	if err != nil {
		log.Fatalf("PayU init failed: %v", err)
	}

	log.Printf("✅ PayU initialized (%s)", env)
}

func main() {
	// payuClient is ready to use
}
```

### Environment Values

| Value          | Purpose | Server       |
| -------------- | ------- | ------------ |
| `"test"`       | Sandbox | test.payu.in |
| `"production"` | Live    | payu.in      |

**Always test thoroughly before switching to production.**

***

## Payment Integration Workflow

### Payment Flow Pattern

```
1. Customer initiates payment
2. Your app creates payment request
3. Your app generates hash (security verification)
4. Your app redirects to PayU checkout
5. Customer completes payment at PayU
6. PayU redirects to your callback URL
7. Your app verifies response hash
8. Your app updates order status
```

### Step 1: Build Payment Request

**Pattern:** Create a struct with required payment data

```go
type PaymentRequest struct {
	Key         string // Merchant key
	Txnid       string // Unique order ID
	Amount      string // "999.99" (string with 2 decimals)
	ProductInfo string // What's being purchased
	FirstName   string // Customer name
	Email       string // Customer email
	Phone       string // Customer phone
	Surl        string // Success URL (HTTPS)
	Furl        string // Failure URL (HTTPS)
	Curl        string // Callback URL (HTTPS)
	Hash        string // Generated hash
}

// Example:
func createPaymentRequest(merchantKey string) *PaymentRequest {
	return &PaymentRequest{
		Key:         merchantKey,
		Txnid:       generateUniqueID(), // Must be unique per payment
		Amount:      "999.99",
		ProductInfo: "Order #123",
		FirstName:   "John",
		Email:       "john@example.com",
		Phone:       "9876543210",
		Surl:        "https://yoursite.com/success",
		Furl:        "https://yoursite.com/failure",
		Curl:        "https://yoursite.com/webhook",
	}
}

func generateUniqueID() string {
	// Implement: Use timestamp, UUID, or order ID
	// Each payment must have unique txnid
	return "ORD-" + fmt.Sprintf("%d", time.Now().Unix())
}
```

### Step 2: Generate Hash

**⚠️ CRITICAL: Hash is security-sensitive**

**Before implementing:**

1. Check PayU's hash specification for field order
2. Verify your SDK provides hash method (if yes, use it)
3. If implementing manually, validate against official spec
4. Test with PayU test credentials

**Pattern for hash generation:**

```go
import "crypto/sha512"
import "fmt"

// Pattern: hash = SHA512(field1|field2|...|fieldN|salt)
// 
// Field order matters. Before implementing:
// 1. Check PayU documentation for correct order
// 2. Verify with your SDK's hash method
// 3. Test with test credentials

func generateHash(request *PaymentRequest, salt string) (string, error) {
	// IMPORTANT: Verify field order with PayU spec
	// Example order (verify this is correct):
	// key|txnid|amount|productinfo|firstname|email|udf1|salt
	
	hashInput := fmt.Sprintf("%s|%s|%s|%s|%s|%s|%s|%s",
		request.Key,
		request.Txnid,
		request.Amount,
		request.ProductInfo,
		request.FirstName,
		request.Email,
		"", // udf1 (empty if not used)
		salt,
	)

	// CRITICAL: Use SHA512 (not SHA256 or MD5)
	hash := sha512.Sum512([]byte(hashInput))
	return fmt.Sprintf("%x", hash), nil
}
```

**Must verify:**

- [ ] Field order matches PayU spec
- [ ] Hash algorithm is SHA512 (not other algorithms)
- [ ] All required fields included
- [ ] Works with test credentials

### Step 3: Redirect to Checkout

**Pattern:** Get checkout URL and redirect customer

```go
func redirectToCheckout(w http.ResponseWriter, request *PaymentRequest) error {
	// Your SDK may provide a method like:
	// checkoutURL := payuClient.GetPaymentURL(request)
	//
	// If not, construct URL following PayU pattern:
	
	baseURL := "https://test.payu.in"
	if os.Getenv("PAYU_ENV") == "production" {
		baseURL = "https://payu.in" // Use only in production
	}

	checkoutURL := fmt.Sprintf(
		"%s/?key=%s&hash=%s&txnid=%s&amount=%s&...",
		baseURL,
		request.Key,
		request.Hash,
		request.Txnid,
		request.Amount,
	)

	http.Redirect(w, request, checkoutURL, http.StatusSeeOther)
	return nil
}
```

***

## Handling Payment Responses

### Pattern: Verify Then Process

**CRITICAL: Always verify hash before trusting response**

```go
func handlePaymentResponse(w http.ResponseWriter, r *http.Request) {
	// Step 1: Get response from PayU
	responseJSON := r.FormValue("response")

	// Step 2: Verify hash (prevents fraud)
	if !verifyResponseHash(responseJSON) {
		log.Printf("❌ Hash verification failed")
		http.Error(w, "Invalid response", http.StatusUnauthorized)
		return
	}

	// Step 3: Parse response
	var response map[string]interface{}
	json.Unmarshal([]byte(responseJSON), &response)

	// Step 4: Check status
	status, ok := response["status"].(string)
	if !ok || status != "success" {
		log.Printf("Payment failed or pending")
		handleFailure(w, response)
		return
	}

	// Step 5: Update order
	txnid, _ := response["txnid"].(string)
	log.Printf("✅ Payment successful: %s", txnid)
	
	// TODO: Update order status in database
	
	http.Redirect(w, r, "/success", http.StatusSeeOther)
}

func verifyResponseHash(responseJSON string) bool {
	// CRITICAL: Hash verification prevents fraud
	// 
	// Before implementing:
	// 1. Understand hash field order
	// 2. Validate against PayU spec
	// 3. Test with PayU test credentials
	// 4. Never skip this step
	//
	// Pattern:
	// 1. Extract hash from response
	// 2. Rebuild hash from fields in correct order
	// 3. Compare hashes
	// 4. Return true only if match
	
	// TODO: Implement hash verification
	return true
}
```

***

## Webhook Integration

### Pattern: Receive Async Notifications

**Why webhooks:** More reliable than redirect URLs (don't depend on user's browser)

**Setup in PayU Dashboard:**

1. Settings → Webhooks
2. Enter endpoint: `https://yoursite.com/webhook`
3. Must be HTTPS

**Handler pattern:**

```go
func webhookHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "POST only", http.StatusMethodNotAllowed)
		return
	}

	// Step 1: Read webhook body
	body, _ := ioutil.ReadAll(r.Body)
	defer r.Body.Close()

	// Step 2: Parse webhook
	var payload map[string]interface{}
	json.Unmarshal(body, &payload)

	log.Printf("📬 Webhook: %v", payload["txnid"])

	// Step 3: Verify hash
	if !verifyWebhookHash(payload) {
		http.Error(w, "Unauthorized", http.StatusUnauthorized)
		return
	}

	// Step 4: Process payment
	status, _ := payload["status"].(string)
	txnid, _ := payload["txnid"].(string)

	switch status {
	case "success":
		log.Printf("✅ Payment successful: %s", txnid)
		// TODO: updateOrder(txnid, "PAID")
	case "failed":
		log.Printf("❌ Payment failed: %s", txnid)
		// TODO: updateOrder(txnid, "FAILED")
	}

	// Step 5: Always return 200 OK
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(map[string]string{"status": "received"})
}

func verifyWebhookHash(payload map[string]interface{}) bool {
	// Same hash verification as payment response
	// Must verify before trusting webhook
	return true
}
```

***

## Testing Guide

### Test Environment

- No real charges
- Instant processing
- Test credentials only
- Test card numbers only

### Get Test Credentials

1. PayU Dashboard → Test Mode
2. Developers → API Keys
3. Copy Merchant Key and Salt

### Test Credentials

**Net Banking:**

```
User: payu
Password: payu
OTP: 123456
```

**Test Cards (EMI):**

```
4706-1378-0509-9594  (Kotak DC)
4011-5100-0000-0007  (AXIS DC)
4453-3410-65876437   (HDFC CC, ICICI CC)

For all:
Expiry: Any future date
CVV: 123
OTP: 111111
Mobile: 9123412345 (for EMI)
```

**Test Wallets:**

```
PayTM: 7777777777 / 888888
PhonePe: Use pre-prod app
Amazon: Use real account
```

### Test Workflow

Before going live:

- [ ] Payment request created
- [ ] Hash generated
- [ ] Checkout URL works (contains test.payu.in)
- [ ] Payment succeeded
- [ ] Response/webhook received
- [ ] Hash verified
- [ ] Order updated in database

***

## Payment Lifecycle & Reconciliation

### Payment States

```
INITIATED (order created)
    ↓
PENDING (awaiting bank/processor)
    ↓
SUCCESS (payment complete)
  OR
FAILED (rejected)
    ↓
(optional) REFUNDED
```

### Critical: Async Payment Handling

Payments are asynchronous. Customer may:

- Close browser before response received
- Internet drops
- Webhook delayed

**Solution: Reconciliation strategy**

```go
// Periodic reconciliation (every 1 hour):
func reconcilePayments() {
	// Get all orders still marked PENDING_PAYMENT
	pending := getAllPendingOrders()

	for _, order := range pending {
		// Query actual payment status
		// Pattern: Use SDK's verify payment method, or PayU API
		
		actualStatus := queryPaymentStatus(order.TransactionID)

		if actualStatus == "success" {
			updateOrder(order.ID, "PAID")
		} else if time.Since(order.CreatedAt) > 24*time.Hour {
			updateOrder(order.ID, "FAILED")
		}
	}
}

// Pattern: Query payment status
func queryPaymentStatus(txnid string) string {
	// Your SDK may provide: client.VerifyPayment(txnid)
	// If not, use PayU's status API
	
	// TODO: Implement using SDK or PayU API
	return "success" // placeholder
}
```

### Idempotency: Handle Duplicate Webhooks

```go
func handleWebhookIdempotent(payload map[string]interface{}) {
	txnid, _ := payload["txnid"].(string)

	// Check if already processed
	if alreadyProcessed(txnid) {
		log.Printf("Already processed: %s", txnid)
		return
	}

	// Mark as processed
	markProcessed(txnid)

	// Now process
	updateOrder(txnid, "PAID")
}

func alreadyProcessed(txnid string) bool {
	// Check database: has this txnid been processed?
	// Return true if already processed
	return false // placeholder
}

func markProcessed(txnid string) {
	// Record in database that we processed this txnid
	// Prevents duplicate processing
}
```

***

## Troubleshooting

### Initialization Fails

**Check:**

- [ ] `PAYU_MERCHANT_KEY` set? `echo $PAYU_MERCHANT_KEY`
- [ ] `PAYU_MERCHANT_SALT` set? `echo $PAYU_MERCHANT_SALT`
- [ ] Both non-empty?
- [ ] Match your PayU account (test vs live)?

***

### Hash Verification Fails

**Check:**

- [ ] Field order correct (verify against PayU spec)
- [ ] Amount has 2 decimals (999.99 not 999.9)
- [ ] Salt is correct
- [ ] All fields included (even empty ones)
- [ ] Using SHA512 (not other algorithms)

**Test:** Generate hash manually, compare with PayU's hash.

***

### Response/Webhook Not Received

**Check:**

- [ ] URL is HTTPS (not HTTP)
- [ ] URL is publicly accessible: `curl -I https://yoursite.com/webhook`
- [ ] URL returns 200 or 405 (not 404/500)
- [ ] Webhook enabled in PayU Dashboard

***

### Payment Stuck Pending

**Pattern:** Query payment status using reconciliation

```go
// Use reconciliation to verify actual status
status := queryPaymentStatus(txnid)

if status == "success" {
	// Update order (payment succeeded, webhook failed)
	updateOrder(txnid, "PAID")
}
```

***

## Production Readiness Checklist

### Before Going Live

**Code Verification:**

- [ ] Verified all SDK methods exist in your version
- [ ] Tested hash generation with PayU test credentials
- [ ] Tested all code examples in your environment
- [ ] Compile-tested all snippets
- [ ] Verified error handling (no ignored errors)

**Security:**

- [ ] Response hash verification implemented
- [ ] Webhook hash verification implemented
- [ ] No sensitive data logged
- [ ] Credentials in environment variables (not hardcoded)
- [ ] HTTPS enforced for all URLs

**Operational:**

- [ ] Reconciliation strategy implemented
- [ ] Idempotency handling implemented
- [ ] Timeout handling (mark pending as failed after 24hrs)
- [ ] All payment states handled (success, failed, pending)

**Testing:**

- [ ] Complete test cycle passed
- [ ] Webhook received and processed
- [ ] Order updated in database
- [ ] Settlement verified

**Go-Live:**

- [ ] Code reviewed
- [ ] Switch to production credentials
- [ ] Change environment to "production"
- [ ] Monitor first 100 transactions

***

## API Methods Reference

**Verify these methods exist in your SDK version before using:**

```go
// Initialization
client, err := payu.NewClient(key, salt, env)

// Potential payment methods (verify before use):
// GetPaymentURL(request) → checkout URL
// VerifyPaymentHash(response) → true/false
// VerifyPayment(txnid) → payment status
// CreateRefund(txnid, amount) → refund ID
// GetRefundStatus(refundID) → refund status
// GetSettlements(from, to) → settlement details
```

**To verify available methods:**

```bash
go doc github.com/payu-india/web-sdk-go
```

***

## FAQ

### Q: Do I need PCI compliance?

**A:** No. Hosted checkout means no raw credit card data on your servers.

***

### Q: Can I test with real cards?

**A:** No. Test mode only accepts test credentials.

***

### Q: What if I don't get the webhook?

**A:** Implement reconciliation (query payment status periodically).

***

### Q: How long until payment appears?

**A:** Usually seconds to minutes. Check Dashboard → Settlements for bank timing.

***

### Q: What if response hash is wrong?

**A:** Don't trust the response. Verify against PayU's spec. Check salt is correct.

***

## Getting Help

**Official Resources:**

- PayU Docs: [https://docs.payu.in](https://docs.payu.in)
- Dashboard: [https://payumoney.com](https://payumoney.com)
- SDK: [https://github.com/payu-india/web-sdk-go](https://github.com/payu-india/web-sdk-go)
- Support: [support@payu.in](mailto:support@payu.in)

**Before Implementing:**

1. Verify SDK methods in your version
2. Validate hash implementation with PayU spec
3. Test all examples in your environment

**Before Going Live:**

1. Code review completed
2. All payment scenarios tested
3. Reconciliation working
4. Monitoring configured

***

## Important Reminders

### Code is Patterns, Not Gospel

The code examples in this guide show **patterns and workflows**, not exact implementations.

**You must:**

- Verify all SDK methods exist in your version
- Validate hash implementation against PayU spec
- Test all code in your environment before production
- Validate security-critical logic (hash, webhook verification)

### This is Not Magic

SDK integration is technical work requiring:

- Understanding payment flows
- Testing before production
- Monitoring after go-live
- Reconciliation for async operations

**Do not skip verification steps.**

***

**End of Documentation**

_This guide provides workflow patterns and examples. Technical implementation details must be verified against official PayU documentation and your SDK version before production use._