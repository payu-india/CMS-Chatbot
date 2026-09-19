#!/usr/bin/env python3
"""Generate PayU Go SDK documentation structure from IA specification."""

import os
from pathlib import Path

BASE = Path("/workspace/docs/Collect Payments/explore-server-integrations/go-sdk")

# (section_folder, subsection_folder, [(slug, title, content), ...])
STRUCTURE = {
    "start-here": {
        "order": ["overview-use-cases", "before-you-start", "quick-start"],
        "subsections": {
            "overview-use-cases": [
                ("what-is-payu-go-sdk", "What is PayU Go SDK?", "what_is"),
                ("when-to-use-go-sdk", "When to Use This SDK", "when_to_use"),
                ("supported-payment-methods", "Supported Payment Methods", "supported_methods"),
            ],
            "before-you-start": [
                ("create-payu-merchant-account", "Create PayU Merchant Account", "create_account"),
                ("understand-merchant-key-salt", "Understand Merchant Key & Salt", "key_salt"),
                ("technical-requirements", "Technical Requirements", "tech_req"),
                ("environment-setup-guide", "Environment Setup Guide", "env_setup"),
            ],
            "quick-start": [
                ("install-go-module", "Install Go Module", "install_module"),
                ("initialize-sdk-client", "Initialize SDK Client", "init_client"),
                ("verify-installation", "Verify Installation", "verify_install"),
                ("quick-start-next-steps", "Next Steps", "quick_next"),
            ],
        },
    },
    "integration": {
        "order": [
            "installation-setup", "sdk-initialization", "payment-integration",
            "handling-payment-responses", "webhook-callback-integration",
            "payment-lifecycle-reconciliation",
        ],
        "subsections": {
            "installation-setup": [
                ("install-go-sdk-module", "Install Go SDK Module", "install_sdk"),
                ("verify-dependencies", "Verify Dependencies", "verify_deps"),
                ("dependency-troubleshooting", "Dependency Troubleshooting", "dep_troubleshoot"),
            ],
            "sdk-initialization": [
                ("initialize-with-credentials", "Initialize with Credentials", "init_credentials"),
                ("configure-test-vs-production", "Configure Test vs Production", "test_prod"),
                ("initialization-errors-solutions", "Initialization Errors & Solutions", "init_errors"),
                ("verify-client-is-ready", "Verify Client is Ready", "verify_client"),
            ],
            "payment-integration": [
                ("payment-flow-overview", "Payment Flow Overview", "payment_flow"),
                ("create-payment-request", "Create Payment Request", "create_payment"),
                ("generate-security-hash", "Generate Security Hash", "gen_hash"),
                ("redirect-to-checkout", "Redirect to Checkout", "redirect_checkout"),
                ("hash-calculation-guide", "Hash Calculation Guide", "hash_guide"),
                ("hash-errors-solutions", "Hash Errors & Solutions", "hash_errors"),
            ],
            "handling-payment-responses": [
                ("receive-success-failure-url", "Receive Success/Failure URL", "receive_urls"),
                ("verify-response-hash", "Verify Response Hash", "verify_hash"),
                ("parse-payment-status", "Parse Payment Status", "parse_status"),
                ("update-order-status", "Update Order Status", "update_order"),
                ("response-verification-errors", "Response Verification Errors", "response_errors"),
            ],
            "webhook-callback-integration": [
                ("why-webhooks-matter", "Why Webhooks Matter", "why_webhooks"),
                ("enable-webhook-dashboard", "Enable Webhook in Dashboard", "enable_webhook"),
                ("build-webhook-handler", "Build Webhook Handler", "build_webhook"),
                ("webhook-security-verification", "Webhook Security & Verification", "webhook_security"),
                ("handle-duplicate-webhooks", "Handle Duplicate Webhooks", "dup_webhooks"),
                ("webhook-debugging", "Webhook Debugging", "webhook_debug"),
            ],
            "payment-lifecycle-reconciliation": [
                ("payment-states-transitions", "Payment States & Transitions", "payment_states"),
                ("async-payment-handling", "Async Payment Handling", "async_payment"),
                ("webhook-failure-recovery", "Webhook Failure Recovery", "webhook_recovery"),
                ("reconciliation-pattern", "Reconciliation Pattern", "reconciliation"),
                ("idempotency-duplicate-detection", "Idempotency & Duplicate Detection", "idempotency"),
                ("timeout-handling", "Timeout Handling", "timeout"),
            ],
        },
    },
    "validation-testing": {
        "order": ["test-environment-setup", "test-credentials-scenarios", "end-to-end-testing", "debugging-guide"],
        "subsections": {
            "test-environment-setup": [
                ("get-test-credentials", "Get Test Credentials", "get_test_creds"),
                ("understand-test-mode-limits", "Understand Test Mode Limits", "test_limits"),
                ("reset-test-data", "Reset Test Data", "reset_test"),
            ],
            "test-credentials-scenarios": [
                ("test-net-banking", "Test Net Banking", "test_nb"),
                ("test-cards-emi", "Test Cards (EMI)", "test_cards"),
                ("test-digital-wallets", "Test Digital Wallets", "test_wallets"),
                ("test-upi", "Test UPI", "test_upi"),
                ("test-endpoints", "Test Endpoints", "test_endpoints"),
            ],
            "end-to-end-testing": [
                ("test-payment-flow", "Test Payment Flow", "test_flow"),
                ("test-response-handling", "Test Response Handling", "test_response"),
                ("test-webhook-delivery", "Test Webhook Delivery", "test_webhook"),
                ("test-error-scenarios", "Test Error Scenarios", "test_errors"),
                ("validation-checklist", "Validation Checklist", "validation_checklist"),
                ("common-test-failures", "Common Test Failures", "test_failures"),
            ],
            "debugging-guide": [
                ("enable-logging", "Enable Logging", "enable_logging"),
                ("debug-payment-requests", "Debug Payment Requests", "debug_requests"),
                ("debug-hash-generation", "Debug Hash Generation", "debug_hash"),
                ("debug-callbacks", "Debug Callbacks", "debug_callbacks"),
                ("use-test-dashboard", "Use Test Dashboard", "test_dashboard"),
            ],
        },
    },
    "production": {
        "order": ["production-readiness-checklist", "go-live-steps", "production-operations"],
        "subsections": {
            "production-readiness-checklist": [
                ("code-review-checklist", "Code Review Checklist", "code_review"),
                ("security-verification", "Security Verification", "security_verify"),
                ("testing-completion", "Testing Completion", "testing_complete"),
                ("monitoring-setup", "Monitoring Setup", "monitoring"),
                ("runbook-creation", "Runbook Creation", "runbook"),
            ],
            "go-live-steps": [
                ("switch-to-live-credentials", "Switch to Live Credentials", "live_creds"),
                ("change-environment-production", "Change Environment to Production", "change_env"),
                ("verify-live-urls", "Verify Live URLs", "verify_urls"),
                ("monitor-first-transactions", "Monitor First Transactions", "monitor_txns"),
                ("verify-settlements", "Verify Settlements", "verify_settlements"),
            ],
            "production-operations": [
                ("monitor-payment-success-rate", "Monitor Payment Success Rate", "monitor_success"),
                ("handle-payment-issues", "Handle Payment Issues", "handle_issues"),
                ("settlement-reconciliation", "Settlement Reconciliation", "settlement_recon"),
                ("incident-response", "Incident Response", "incident"),
            ],
        },
    },
    "troubleshooting-support": {
        "order": ["common-integration-issues", "error-reference-solutions", "troubleshooting-decision-trees", "faq-common-questions"],
        "subsections": {
            "common-integration-issues": [
                ("initialization-failures", "Initialization Failures", "init_failures"),
                ("payment-request-errors", "Payment Request Errors", "payment_errors"),
                ("hash-verification-failures", "Hash Verification Failures", "hash_failures"),
                ("response-webhook-issues", "Response/Webhook Issues", "webhook_issues"),
                ("callback-not-received", "Callback Not Received", "callback_not_received"),
                ("duplicate-transactions", "Duplicate Transactions", "dup_txns"),
            ],
            "error-reference-solutions": [
                ("error-code-reference", "Error Code Reference", "error_codes"),
                ("payment-failure-codes", "Payment Failure Codes", "failure_codes"),
                ("callback-errors", "Callback Errors", "callback_errors"),
                ("recovery-strategies", "Recovery Strategies", "recovery"),
            ],
            "troubleshooting-decision-trees": [
                ("sdk-wont-initialize", "SDK Won't Initialize", "tree_init"),
                ("payment-request-fails", "Payment Request Fails", "tree_payment"),
                ("hash-verification-fails", "Hash Verification Fails", "tree_hash"),
                ("callback-not-received-tree", "Callback Not Received", "tree_callback"),
                ("payment-stuck-pending", "Payment Stuck Pending", "tree_pending"),
            ],
            "faq-common-questions": [
                ("how-long-does-payment-take", "How long does payment take?", "faq_time"),
                ("when-receive-funds", "When do I receive funds?", "faq_funds"),
                ("pci-compliance-faq", "Do I need PCI compliance?", "faq_pci"),
                ("test-with-real-cards", "Can I test with real cards?", "faq_cards"),
                ("handle-failed-payments", "How do I handle failed payments?", "faq_failed"),
                ("go-sdk-faq-more", "More FAQs", "faq_more"),
            ],
        },
    },
    "reference-advanced": {
        "order": [
            "api-methods-reference", "payment-specification", "security-best-practices",
            "performance-optimization", "migration-versioning", "advanced-integration-patterns",
        ],
        "subsections": {
            "api-methods-reference": [
                ("newclient-reference", "NewClient()", "ref_newclient"),
                ("payment-methods-reference", "Payment Methods", "ref_payment"),
                ("refund-methods-reference", "Refund Methods", "ref_refund"),
                ("settlement-methods-reference", "Settlement Methods", "ref_settlement"),
                ("utility-methods-reference", "Utility Methods", "ref_utility"),
            ],
            "payment-specification": [
                ("payment-request-format", "Payment Request Format", "spec_request"),
                ("response-format", "Response Format", "spec_response"),
                ("webhook-payload-format", "Webhook Payload Format", "spec_webhook"),
                ("hash-field-order", "Hash Field Order", "spec_hash"),
                ("field-validation-rules", "Field Validation Rules", "spec_validation"),
            ],
            "security-best-practices": [
                ("credential-management", "Credential Management", "sec_credentials"),
                ("hash-validation", "Hash Validation", "sec_hash"),
                ("webhook-verification", "Webhook Verification", "sec_webhook"),
                ("pci-compliance", "PCI Compliance", "sec_pci"),
                ("data-security", "Data Security", "sec_data"),
            ],
            "performance-optimization": [
                ("connection-pooling", "Connection Pooling", "perf_pooling"),
                ("timeout-configuration", "Timeout Configuration", "perf_timeout"),
                ("retry-strategies", "Retry Strategies", "perf_retry"),
                ("caching-patterns", "Caching Patterns", "perf_cache"),
            ],
            "migration-versioning": [
                ("sdk-version-history", "SDK Version History", "mig_history"),
                ("breaking-changes", "Breaking Changes", "mig_breaking"),
                ("migration-guide", "Migration Guide", "mig_guide"),
                ("deprecation-notices", "Deprecation Notices", "mig_deprecation"),
            ],
            "advanced-integration-patterns": [
                ("multi-currency-setup", "Multi-currency Setup", "adv_multi"),
                ("recurring-payments", "Recurring Payments", "adv_recurring"),
                ("bulk-operations", "Bulk Operations", "adv_bulk"),
                ("custom-integrations", "Custom Integrations", "adv_custom"),
            ],
        },
    },
    "getting-help": {
        "order": ["support-resources", "community", "when-to-contact-support"],
        "subsections": {
            "support-resources": [
                ("official-documentation", "Official Documentation", "help_docs"),
                ("api-specification", "API Specification", "help_api"),
                ("github-repository", "GitHub Repository", "help_github"),
                ("support-channels", "Support Channels", "help_channels"),
            ],
            "community": [
                ("github-issues", "GitHub Issues", "comm_github"),
                ("stack-overflow-tags", "Stack Overflow Tags", "comm_stack"),
                ("developer-forum", "Developer Forum", "comm_forum"),
            ],
            "when-to-contact-support": [
                ("what-info-to-provide", "What Info to Provide", "contact_info"),
                ("how-to-get-help-fast", "How to Get Help Fast", "contact_fast"),
                ("known-limitations", "Known Limitations", "contact_limits"),
            ],
        },
    },
}

SECTION_TITLES = {
    "start-here": "Start Here",
    "integration": "Integration",
    "validation-testing": "Validation & Testing",
    "production": "Production",
    "troubleshooting-support": "Troubleshooting & Support",
    "reference-advanced": "Reference & Advanced",
    "getting-help": "Getting Help",
}

SUBSECTION_TITLES = {
    "overview-use-cases": "Overview & Use Cases",
    "before-you-start": "Before You Start (Prerequisites)",
    "quick-start": "Quick Start (5 Minutes)",
    "installation-setup": "Installation & Setup",
    "sdk-initialization": "SDK Initialization",
    "payment-integration": "Payment Integration (Core Feature)",
    "handling-payment-responses": "Handling Payment Responses",
    "webhook-callback-integration": "Webhook / Callback Integration",
    "payment-lifecycle-reconciliation": "Payment Lifecycle & Reconciliation",
    "test-environment-setup": "Test Environment Setup",
    "test-credentials-scenarios": "Test Credentials & Scenarios",
    "end-to-end-testing": "End-to-End Testing",
    "debugging-guide": "Debugging Guide",
    "production-readiness-checklist": "Production Readiness Checklist",
    "go-live-steps": "Go Live Steps",
    "production-operations": "Production Operations",
    "common-integration-issues": "Common Integration Issues",
    "error-reference-solutions": "Error Reference & Solutions",
    "troubleshooting-decision-trees": "Troubleshooting Decision Trees",
    "faq-common-questions": "FAQ & Common Questions",
    "api-methods-reference": "API Methods Reference",
    "payment-specification": "Payment Specification",
    "security-best-practices": "Security Best Practices",
    "performance-optimization": "Performance Optimization",
    "migration-versioning": "Migration & Versioning",
    "advanced-integration-patterns": "Advanced Integration Patterns",
    "support-resources": "Support Resources",
    "community": "Community",
    "when-to-contact-support": "When to Contact Support",
}


def frontmatter(title: str, description: str, keywords: list[str]) -> str:
    kw = "\n".join(f"    - {k}" for k in keywords)
    return f"""---
title: {title}
excerpt: '{description[:120]}'
deprecated: false
hidden: false
metadata:
  title: '{title} | PayU Go SDK'
  description: '{description[:200]}'
  keywords:
{kw}
  robots: index
next:
  description: ''
---
"""


def related_next(related: list[str], next_steps: list[str]) -> str:
    rel = "\n".join(f"- [{r[0]}](doc:{r[1]})" for r in related) if related else "- See the [Go SDK overview](doc:go-sdk)"
    nxt = "\n".join(f"- [{n[0]}](doc:{n[1]})" for n in next_steps) if next_steps else "- Return to [Go SDK overview](doc:go-sdk)"
    return f"""
## Related Pages

{rel}

## Next Steps

{nxt}
"""


# Content keyed by content_id
CONTENT = {}

def add(key, body):
    CONTENT[key] = body

add("what_is", """## Overview

The PayU Go SDK integrates PayU payment processing into Go applications. It provides payment request creation, response verification via hash validation, payment status queries, and refund and settlement management.

**Verify supported features in your SDK version before implementing.**

## Who Should Read This

Go backend developers integrating PayU hosted checkout for the first time.

## What the SDK Does

- Payment request creation and redirect to PayU checkout
- Response verification via hash validation
- Payment status queries
- Refund and settlement management

> 🚧 Download Go SDK
>
> GitHub: [https://github.com/payu-india/web-sdk-go](https://github.com/payu-india/web-sdk-go)

## Best Practices

- Verify SDK methods exist in your installed version: `go doc github.com/payu-india/web-sdk-go`
- Never copy-paste code without compiling and testing
- Validate hash implementation against PayU's official specification
""")

add("when_to_use", """## Overview

Choose the PayU Go SDK when your backend is written in Go and you want PayU-hosted checkout with server-side verification.

## When to Use This SDK

✅ Backend is Go  
✅ You want PayU-hosted payment form  
✅ You need server-side payment verification  

❌ Frontend JavaScript integration → Use [Web SDK](doc:introduction-web)  
❌ Mobile app → Use [Android](doc:explore-android-sdks) or [iOS SDKs](doc:explore-ios-sdks)

## Prerequisites

- PayU merchant account (test or live)
- Go 1.18+
- HTTPS callback URLs
""")

add("supported_methods", """## Overview

With the PayU Go SDK you can collect payments, verify transactions, handle refunds, check settlements, and more.

## Supported Payment Features

- **Collect Payments** — Create a payment form to collect payment
- **Verify Payments** — Verify the transaction or check transaction status
- **Handle Refunds** — Initiate/cancel refunds and check refund status
- **Check Settlements** — Retrieve settlement details
- **Check Bank Downtime** — Get eligible payment options and PG/BANK downtime details
- **Check Eligibility** — Check customer EMI eligibility
- **Manage Invoices** — Create/expire invoice links

Before integration, enable payment methods in **Dashboard → Settings → Payment methods**. Cards, UPI, and other methods are enabled by default.

## Related Guides

- [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets)
- [Configure payment methods](doc:configure-user-settings)
""")

add("create_account", """## Overview

Create a PayU merchant account before integrating the Go SDK.

## Step-by-Step Guide

<Accordion title="Create a PayU account" icon="fa-code">
  First, create a PayU account. See [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Accordion>

## Expected Outcome

- Test Mode access with API keys
- Live Mode access after merchant approval

## Best Practices

- Complete KYC early to avoid go-live delays
- Use Test Mode for all development
""")

add("key_salt", """## Overview

Merchant Key and Salt authenticate your server with PayU and are required for hash generation and verification.

## Get Test Credentials

1. PayU Dashboard → **Test Mode**
2. **Developers → API Keys**
3. Copy **Merchant Key** and **Merchant Salt**

## Get Live Credentials

1. PayU Dashboard → **Live Mode**
2. **Developers → API Keys**
3. Copy **Live Merchant Key** and **Salt**

See also [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy).

## Best Practices

- Never hardcode credentials in source code
- Use environment variables or a secrets manager
- Use test keys only in test environment
""")

add("tech_req", """## Overview

Technical prerequisites for PayU Go SDK integration.

## Prerequisites

- **Go 1.18+**
- `go.mod` initialized in your project
- **HTTPS URLs** for success, failure, and webhook callbacks
- Internet access to PayU servers (`test.payu.in` / `payu.in`)

## Success Criteria

- `go version` shows 1.18 or higher
- Callback URLs are publicly reachable over HTTPS
""")

add("env_setup", """## Overview

Configure environment variables for local and deployed environments.

## Step-by-Step Guide

```bash
# Test environment
export PAYU_MERCHANT_KEY="your_test_key"
export PAYU_MERCHANT_SALT="your_test_salt"
export PAYU_ENV="test"
```

## Best Practices

**Never hardcode credentials.** Use environment variables, `.env` files (not committed), or your platform's secret store.

## Common Mistakes

- Mixing test keys with production environment (or vice versa)
- Committing credentials to version control
""")

add("install_module", """## Overview

Install the PayU Go SDK module in under a minute.

## Step-by-Step Guide

```bash
go get github.com/payu-india/web-sdk-go
go mod tidy
```

## Expected Output

Module added to `go.mod` with no errors.

## Code Examples

```go
import payu "github.com/payu-india/web-sdk-go"
```
""")

add("init_client", """## Overview

Initialize the PayU client with merchant credentials.

## Step-by-Step Guide

```go
package main

import (
	"log"
	"os"

	payu "github.com/payu-india/web-sdk-go"
)

func main() {
	key := os.Getenv("PAYU_MERCHANT_KEY")
	salt := os.Getenv("PAYU_MERCHANT_SALT")
	env := os.Getenv("PAYU_ENV")

	if key == "" || salt == "" {
		log.Fatal("PAYU credentials not set")
	}

	if env == "" {
		env = "test"
	}

	client, err := payu.NewClient(key, salt, env)
	if err != nil {
		log.Fatalf("Failed to initialize: %v", err)
	}

	log.Println("✅ PayU client ready")
}
```

**Run:** `go run main.go`  
**Expected:** `✅ PayU client ready`
""")

add("verify_install", """## Overview

Confirm the SDK module is installed correctly.

## Step-by-Step Guide

```bash
go list -m github.com/payu-india/web-sdk-go
go mod verify
```

## Success Criteria

- Module version is listed
- `go mod verify` reports all modules verified
""")

add("quick_next", """## Overview

You have installed and initialized the PayU Go SDK. Continue with the full integration workflow.

## Next Steps

- [Install Go SDK Module](doc:install-go-sdk-module) — detailed installation
- [Payment Flow Overview](doc:payment-flow-overview) — understand the payment journey
- [Create Payment Request](doc:create-payment-request) — accept your first payment
- [Test Payment Flow](doc:test-payment-flow) — end-to-end sandbox test
""")

# Integration section content (abbreviated but complete patterns from Claude doc)
add("install_sdk", """## Overview

Download and verify the PayU Go SDK module.

## Step-by-Step Guide

```bash
go get github.com/payu-india/web-sdk-go
go mod tidy
go mod verify
```

```bash
go list -m github.com/payu-india/web-sdk-go
```

```go
import payu "github.com/payu-india/web-sdk-go"
```
""")

add("verify_deps", """## Overview

Verify all Go module dependencies resolve correctly.

```bash
go mod verify
go mod download
go build ./...
```

## Success Criteria

Build completes without dependency errors.
""")

add("dep_troubleshooting", """## Overview

Resolve common Go module and dependency issues.

## Common Issues

| Issue | Solution |
|-------|----------|
| Module not found | Run `go get github.com/payu-india/web-sdk-go` |
| Version conflict | Run `go mod tidy` |
| Proxy timeout | Set `GOPROXY=https://proxy.golang.org,direct` |

## Troubleshooting

See [Dependency Troubleshooting](doc:dependency-troubleshooting) and [Initialization Failures](doc:initialization-failures).
""")

add("init_credentials", """## Overview

Initialize the PayU client once at application startup.

## Pattern: Initialize Once at Startup

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
```
""")

add("test_prod", """## Overview

Configure test vs production environments.

| Value | Purpose | Server |
|-------|---------|--------|
| `"test"` | Sandbox | test.payu.in |
| `"production"` | Live | payu.in |

**Always test thoroughly before switching to production.**

```go
client, err := payu.NewClient(key, salt, "test") // or "production"
```
""")

add("init_errors", """## Overview

Diagnose and fix SDK initialization failures.

## Checklist

- [ ] `PAYU_MERCHANT_KEY` set? `echo $PAYU_MERCHANT_KEY`
- [ ] `PAYU_MERCHANT_SALT` set? `echo $PAYU_MERCHANT_SALT`
- [ ] Both non-empty?
- [ ] Keys match your PayU account (test vs live)?

See [SDK Won't Initialize](doc:sdk-wont-initialize) decision tree.
""")

add("verify_client", """## Overview

Confirm the PayU client is ready before processing payments.

## Success Criteria

- `payu.NewClient()` returns without error
- Log shows environment (`test` or `production`)
- No credential-related panics at startup
""")

add("payment_flow", """## Overview

End-to-end payment flow for PayU hosted checkout with the Go SDK.

> Flow Diagram: PayU Go SDK Payment Integration

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

## Workflow Overview

Hosted checkout keeps card data on PayU servers — you never handle raw card numbers.
""")

add("create_payment", """## Overview

Build a payment request with required transaction fields.

```go
type PaymentRequest struct {
	Key         string
	Txnid       string // Unique order ID
	Amount      string // "999.99" (string with 2 decimals)
	ProductInfo string
	FirstName   string
	Email       string
	Phone       string
	Surl        string // Success URL (HTTPS)
	Furl        string // Failure URL (HTTPS)
	Curl        string // Callback URL (HTTPS)
	Hash        string
}

func createPaymentRequest(merchantKey string) *PaymentRequest {
	return &PaymentRequest{
		Key:         merchantKey,
		Txnid:       generateUniqueID(),
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
```

Each payment must have a **unique** `txnid`.
""")

add("gen_hash", """## Overview

Generate the security hash for payment requests. Hash generation is security-critical.

⚠️ **CRITICAL:** Verify field order against [Hash Field Order](doc:hash-field-order) and [Generate Hash](doc:hashing-request-and-response).

```go
import (
	"crypto/sha512"
	"fmt"
)

func generateHash(request *PaymentRequest, salt string) (string, error) {
	hashInput := fmt.Sprintf("%s|%s|%s|%s|%s|%s|%s|%s",
		request.Key,
		request.Txnid,
		request.Amount,
		request.ProductInfo,
		request.FirstName,
		request.Email,
		"", // udf1
		salt,
	)
	hash := sha512.Sum512([]byte(hashInput))
	return fmt.Sprintf("%x", hash), nil
}
```

## Must Verify

- [ ] Field order matches PayU spec
- [ ] SHA512 algorithm (not SHA256 or MD5)
- [ ] Works with test credentials
""")

add("redirect_checkout", """## Overview

Redirect the customer to PayU hosted checkout.

```go
func redirectToCheckout(w http.ResponseWriter, request *PaymentRequest) error {
	baseURL := "https://test.payu.in"
	if os.Getenv("PAYU_ENV") == "production" {
		baseURL = "https://payu.in"
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

Use your SDK's `GetPaymentURL` method if available.
""")

add("hash_guide", """## Overview

Detailed hash calculation for PayU Go SDK integrations.

For complete hash logic, refer to [Generate Hash](doc:hashing-request-and-response).

## Basic Payment Request Hash

`sha512(key|txnid|amount|productinfo|firstname|email|||||||||||SALT)`

## Response Hash (Reverse Hashing)

Always verify the response hash before trusting payment status. See [Verify Response Hash](doc:verify-response-hash).
""")

add("hash_errors", """## Overview

Fix hash generation and verification failures.

## Checklist

- [ ] Field order correct (verify against PayU spec)
- [ ] Amount has 2 decimals (`999.99` not `999.9`)
- [ ] Salt is correct for environment (test vs live)
- [ ] All fields included (even empty UDF fields)
- [ ] Using SHA512

**Test:** Generate hash manually and compare with PayU's hash.

See [Hash Verification Fails](doc:hash-verification-fails) decision tree.
""")

add("receive_urls", """## Overview

Handle success and failure redirect URLs after customer completes checkout.

PayU redirects the customer's browser to `surl` (success) or `furl` (failure) with payment response data.

## Best Practices

- Always verify hash before processing
- Do not fulfill orders on redirect alone — confirm via webhook or verify API
""")

add("verify_hash", """## Overview

**CRITICAL: Always verify hash before trusting any payment response.**

```go
func handlePaymentResponse(w http.ResponseWriter, r *http.Request) {
	responseJSON := r.FormValue("response")

	if !verifyResponseHash(responseJSON) {
		log.Printf("❌ Hash verification failed")
		http.Error(w, "Invalid response", http.StatusUnauthorized)
		return
	}

	var response map[string]interface{}
	json.Unmarshal([]byte(responseJSON), &response)

	status, _ := response["status"].(string)
	if status != "success" {
		handleFailure(w, response)
		return
	}

	txnid, _ := response["txnid"].(string)
	log.Printf("✅ Payment successful: %s", txnid)
	http.Redirect(w, r, "/success", http.StatusSeeOther)
}
```

See [Generate Hash](doc:hashing-request-and-response) for reverse hashing logic.
""")

add("parse_status", """## Overview

Parse payment status from PayU response payload.

## Payment Status Values

| Status | Meaning |
|--------|---------|
| `success` | Payment completed |
| `failure` | Payment failed |
| `pending` | Awaiting confirmation |

Parse `status`, `txnid`, `mihpayid`, and `amount` from the response JSON.
""")

add("update_order", """## Overview

Update your order database after verified payment.

## Workflow

1. Verify response hash
2. Confirm `status == "success"`
3. Match `txnid` to your order
4. Match `amount` to order total
5. Update order status atomically
6. Trigger fulfillment

## Best Practices

- Use database transactions
- Implement idempotency (same `txnid` processed once)
""")

add("response_errors", """## Overview

Troubleshoot response verification failures.

## Common Causes

- Incorrect reverse hash field order
- Wrong salt (test vs live)
- Tampered response data
- Skipping verification entirely

See [Hash Verification Failures](doc:hash-verification-failures).
""")

add("why_webhooks", """## Overview

Webhooks deliver payment notifications server-to-server, independent of the customer's browser.

**Why webhooks matter:** More reliable than redirect URLs — they don't depend on the user completing the browser redirect.

See [Webhooks](doc:webhooks) for platform-wide webhook documentation.
""")

add("enable_webhook", """## Overview

Configure webhooks in the PayU Dashboard.

## Step-by-Step Guide

1. Dashboard → **Settings → Webhooks**
2. Enter endpoint: `https://yoursite.com/webhook`
3. Must be **HTTPS**
4. Save and test delivery

See [Manage Webhooks Using Dashboard](doc:manage-webhooks-using-dashboard).
""")

add("build_webhook", """## Overview

Build a webhook handler in Go.

```go
func webhookHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "POST only", http.StatusMethodNotAllowed)
		return
	}

	body, _ := ioutil.ReadAll(r.Body)
	defer r.Body.Close()

	var payload map[string]interface{}
	json.Unmarshal(body, &payload)

	if !verifyWebhookHash(payload) {
		http.Error(w, "Unauthorized", http.StatusUnauthorized)
		return
	}

	status, _ := payload["status"].(string)
	txnid, _ := payload["txnid"].(string)

	switch status {
	case "success":
		log.Printf("✅ Payment successful: %s", txnid)
	case "failed":
		log.Printf("❌ Payment failed: %s", txnid)
	}

	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(map[string]string{"status": "received"})
}
```

**Always return HTTP 200** after processing.
""")

add("webhook_security", """## Overview

Verify webhook authenticity before updating orders.

## Best Practices

- Verify hash on every webhook
- Use HTTPS only
- Reject unsigned or invalid payloads
- Log webhook IDs for audit

See [Webhook Security & Verification](doc:webhook-security-verification) and [Hash Validation](doc:hash-validation).
""")

add("dup_webhooks", """## Overview

PayU may send duplicate webhooks. Handle them idempotently.

```go
func handleWebhookIdempotent(payload map[string]interface{}) {
	txnid, _ := payload["txnid"].(string)

	if alreadyProcessed(txnid) {
		log.Printf("Already processed: %s", txnid)
		return
	}

	markProcessed(txnid)
	updateOrder(txnid, "PAID")
}
```
""")

add("webhook_debug", """## Overview

Debug webhook delivery issues.

## Checklist

- [ ] URL is HTTPS and publicly accessible
- [ ] Endpoint returns 200 (not 404/500)
- [ ] Webhook enabled in Dashboard
- [ ] Firewall allows PayU IPs

Test: `curl -I https://yoursite.com/webhook`
""")

add("payment_states", """## Overview

Payment state machine for PayU transactions.

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
""")

add("async_payment", """## Overview

Payments are asynchronous. Customers may close the browser, lose connectivity, or experience delayed webhooks.

**Solution:** Implement reconciliation — periodically query payment status for pending orders.
""")

add("webhook_recovery", """## Overview

Recover when webhooks fail but payment succeeded.

Use the Verify Payment API or SDK method to query actual status and update orders accordingly.

See [Reconciliation Pattern](doc:reconciliation-pattern).
""")

add("reconciliation", """## Overview

Periodic reconciliation catches missed webhooks and redirect callbacks.

```go
func reconcilePayments() {
	pending := getAllPendingOrders()

	for _, order := range pending {
		actualStatus := queryPaymentStatus(order.TransactionID)

		if actualStatus == "success" {
			updateOrder(order.ID, "PAID")
		} else if time.Since(order.CreatedAt) > 24*time.Hour {
			updateOrder(order.ID, "FAILED")
		}
	}
}
```

Run reconciliation every 1 hour (adjust for your volume).
""")

add("idempotency", """## Overview

Prevent duplicate order updates from retries and duplicate webhooks.

- Store processed `txnid` values
- Check before updating order status
- Use database unique constraints on `txnid`

See [Handle Duplicate Webhooks](doc:handle-duplicate-webhooks).
""")

add("timeout", """## Overview

Handle payments stuck in pending state.

Mark orders as failed after 24 hours if status remains unresolved, after reconciliation confirms no success.
""")

# Testing section
add("get_test_creds", """## Overview

Get test credentials from the PayU Dashboard.

1. PayU Dashboard → **Test Mode**
2. **Developers → API Keys**
3. Copy Merchant Key and Salt

<TestKeyAndSaltProcedure />
""")

add("test_limits", """## Overview

Test mode limitations:

- No real charges
- Instant processing
- Test credentials only
- Test card numbers only — **never use real cards in test mode**
""")

add("reset_test", """## Overview

Reset test data between test cycles.

Use unique `txnid` values for each test payment. Clear local order state between test runs.
""")

add("test_nb", """## Overview

Test Net Banking integration.

**Credentials:**
- User: `payu`
- Password: `payu`
- OTP: `123456`

<Test_your_integration />
""")

add("test_cards", """## Overview

Test card numbers for EMI and card payments.

**Test Cards (EMI):**
- 4706-1378-0509-9594 (Kotak DC)
- 4011-5100-0000-0007 (AXIS DC)
- 4453-3410-65876437 (HDFC CC, ICICI CC)

For all: Expiry any future date, CVV `123`, OTP `111111`, Mobile `9123412345` (EMI).

See [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) for the full list.
""")

add("test_wallets", """## Overview

Test digital wallet payments.

- PayTM: `7777777777` / `888888`
- PhonePe: Use pre-prod app
- Amazon: Use real account (test mode)

See [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).
""")

add("test_upi", """## Overview

Test UPI payments in sandbox.

See [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) for test VPAs and UPI handles.
""")

add("test_endpoints", """## Overview

PayU test environment endpoints.

| Environment | Base URL |
|-------------|----------|
| Test | `https://test.payu.in` |
| Production | `https://payu.in` |

Verify checkout URLs contain `test.payu.in` during testing.
""")

add("test_flow", """## Overview

End-to-end test payment workflow.

## Validation Checklist

- [ ] Payment request created
- [ ] Hash generated
- [ ] Checkout URL works (contains test.payu.in)
- [ ] Payment succeeded
- [ ] Response/webhook received
- [ ] Hash verified
- [ ] Order updated in database

<Test_your_integration />
""")

add("test_response", """## Overview

Test success and failure URL handling.

1. Complete a test payment
2. Confirm redirect to `surl` or `furl`
3. Verify hash on response
4. Confirm order status update
""")

add("test_webhook", """## Overview

Test webhook delivery end-to-end.

1. Configure webhook URL in Dashboard
2. Complete test payment
3. Confirm webhook received at your endpoint
4. Verify hash and return 200
""")

add("test_errors", """## Overview

Test failure scenarios:

- Declined test card
- Cancelled payment
- Invalid hash (should reject)
- Timeout / abandoned checkout
""")

add("validation_checklist", """## Overview

Pre-go-live validation checklist.

- [ ] Payment request created
- [ ] Hash generated and verified
- [ ] Checkout URL works
- [ ] Payment succeeded in test
- [ ] Response/webhook received
- [ ] Hash verified on response
- [ ] Order updated in database
- [ ] Reconciliation tested
- [ ] Idempotency tested
""")

add("test_failures", """## Overview

Common test failures and fixes.

| Failure | Fix |
|---------|-----|
| Hash mismatch | Check field order and salt |
| Checkout 404 | Verify base URL (test.payu.in) |
| No webhook | Check HTTPS and Dashboard config |
| Order not updated | Verify hash before update logic |
""")

add("enable_logging", """## Overview

Enable structured logging for payment debugging.

```go
log.Printf("Payment request: txnid=%s amount=%s", req.Txnid, req.Amount)
log.Printf("Hash input length: %d", len(hashInput))
```

**Never log salt or full card data.**
""")

add("debug_requests", """## Overview

Debug payment request issues.

- Log `txnid`, `amount`, environment
- Compare request fields with hash input
- Verify all required fields present
""")

add("debug_hash", """## Overview

Debug hash generation.

1. Log hash input string (without salt in production logs)
2. Compare with PayU expected hash
3. Verify SHA512 and field order

See [Hash Calculation Guide](doc:hash-calculation-guide).
""")

add("debug_callbacks", """## Overview

Debug callback and webhook issues.

- Log incoming request method and path
- Log response payload (redact sensitive fields)
- Confirm 200 response returned
""")

add("test_dashboard", """## Overview

Use the PayU Test Dashboard to inspect transactions.

Dashboard → **Transactions** (Test Mode) shows payment status, amounts, and errors.
""")

# Production
add("code_review", """## Overview

Code review checklist before go-live.

- [ ] Verified all SDK methods exist in your version
- [ ] Tested hash generation with test credentials
- [ ] Compile-tested all snippets
- [ ] Error handling implemented (no ignored errors)
""")

add("security_verify", """## Overview

Security verification before production.

- [ ] Response hash verification implemented
- [ ] Webhook hash verification implemented
- [ ] No sensitive data logged
- [ ] Credentials in environment variables
- [ ] HTTPS enforced for all URLs
""")

add("testing_complete", """## Overview

Confirm testing is complete.

- [ ] Complete test cycle passed
- [ ] Webhook received and processed
- [ ] Order updated in database
- [ ] Error scenarios tested

<Test_your_integration />
""")

add("monitoring", """## Overview

Set up monitoring before go-live.

- Payment success rate alerts
- Webhook failure alerts
- Reconciliation job monitoring
- Error rate dashboards
""")

add("runbook", """## Overview

Create an incident runbook covering:

- Payment stuck pending → reconciliation steps
- Hash verification failure → escalation
- Webhook outage → manual verify API
- Settlement discrepancies → support contact
""")

add("live_creds", """## Overview

Switch to live merchant credentials.

<ProductionKeyAndSaltProcedure />

**Never use test credentials in production.**
""")

add("change_env", """## Overview

Change SDK environment to production.

```go
client, err := payu.NewClient(liveKey, liveSalt, "production")
```

<Go_Live_Checklist />
""")

add("verify_urls", """## Overview

Verify production URLs.

- Checkout: `https://payu.in`
- Callback URLs use production domain
- Webhook URL is live HTTPS endpoint
""")

add("monitor_txns", """## Overview

Monitor first transactions after go-live.

- Watch Dashboard → Transactions (Live Mode)
- Alert on unexpected failure rate
- Manually verify first 10–100 transactions
""")

add("verify_settlements", """## Overview

Verify settlements after go-live.

Check Dashboard → **Settlements** for bank settlement timing and amounts.
""")

add("monitor_success", """## Overview

Monitor payment success rate in production.

Track success %, failure reasons, and latency. Set alerts for drops below baseline.
""")

add("handle_issues", """## Overview

Handle production payment issues.

1. Check transaction in Dashboard
2. Run verify API for status
3. Check webhook logs
4. Escalate with txnid and mihpayid
""")

add("settlement_recon", """## Overview

Reconcile settlements with your order records.

Match settlement reports to successful transactions by `txnid` and amount.
""")

add("incident", """## Overview

Incident response for payment outages.

1. Assess scope (all payments or specific method)
2. Check PayU status and Dashboard
3. Enable maintenance mode if needed
4. Contact support with merchant key and sample txnids
""")

# Troubleshooting
add("init_failures", """## Overview

Fix SDK initialization failures.

- [ ] `PAYU_MERCHANT_KEY` set?
- [ ] `PAYU_MERCHANT_SALT` set?
- [ ] Keys match environment (test vs live)?

See [SDK Won't Initialize](doc:sdk-wont-initialize).
""")

add("payment_errors", """## Overview

Fix payment request errors.

- Verify required fields
- Check amount format (2 decimals)
- Ensure unique `txnid`
""")

add("hash_failures", """## Overview

Fix hash verification failures.

See [Hash Verification Fails](doc:hash-verification-fails) and [Hash Errors & Solutions](doc:hash-errors-solutions).
""")

add("webhook_issues", """## Overview

Fix response and webhook issues.

- HTTPS required
- Publicly accessible endpoint
- Return 200 OK
- Webhook enabled in Dashboard
""")

add("callback_not_received", """## Overview

Callback or webhook not received.

- [ ] URL is HTTPS
- [ ] URL publicly accessible: `curl -I https://yoursite.com/webhook`
- [ ] Returns 200 or 405 (not 404/500)
- [ ] Webhook enabled in Dashboard
""")

add("dup_txns", """## Overview

Prevent and handle duplicate transactions.

- Use unique `txnid` per payment attempt
- Implement idempotency on order updates
- Reject duplicate `txnid` at creation
""")

add("error_codes", """## Overview

PayU error code reference.

See [Error Handling](doc:error-handling) and [Error Codes](doc:error-codes) for platform-wide error documentation.
""")

add("failure_codes", """## Overview

Common payment failure codes and meanings.

Refer to Dashboard transaction details for specific failure reasons per transaction.
""")

add("callback_errors", """## Overview

Callback-specific errors.

- Invalid hash → reject and log
- Missing fields → return 400
- Duplicate processing → return 200 (idempotent)
""")

add("recovery", """## Overview

Recovery strategies for failed integrations.

1. **Hash fails** → verify spec, re-test with test credentials
2. **Webhook missing** → run reconciliation
3. **Payment pending** → query verify API
4. **Duplicate charge** → initiate refund via SDK
""")

add("tree_init", """## Overview

Decision tree: SDK won't initialize.

```
Credentials set? → No → Set PAYU_MERCHANT_KEY and PAYU_MERCHANT_SALT
        ↓ Yes
Keys match environment? → No → Use test keys with "test" env
        ↓ Yes
NewClient() error? → Check error message → Fix credentials or network
        ↓ Success
Client ready ✅
```
""")

add("tree_payment", """## Overview

Decision tree: Payment request fails.

```
Required fields present? → No → Add missing fields
        ↓ Yes
Unique txnid? → No → Generate new txnid
        ↓ Yes
Hash valid? → No → See Hash Errors guide
        ↓ Yes
Checkout loads? → No → Check base URL and parameters
```
""")

add("tree_hash", """## Overview

Decision tree: Hash verification fails.

```
Correct salt? → No → Match test/live salt to environment
        ↓ Yes
Field order correct? → No → See Hash Field Order
        ↓ Yes
SHA512 used? → No → Switch to SHA512
        ↓ Yes
Amount format correct? → No → Use 2 decimal places
        ↓ Yes
Re-test with manual hash comparison
```
""")

add("tree_callback", """## Overview

Decision tree: Callback not received.

```
HTTPS URL? → No → Switch to HTTPS
        ↓ Yes
Publicly accessible? → No → Fix firewall/DNS
        ↓ Yes
Returns 200? → No → Fix handler errors
        ↓ Yes
Webhook enabled in Dashboard? → No → Enable webhook
        ↓ Yes
Use reconciliation as backup
```
""")

add("tree_pending", """## Overview

Decision tree: Payment stuck pending.

```
Query verify API → success? → Update order to PAID
        ↓ failed
Mark order FAILED
        ↓ still pending
Wait + reconcile → >24h? → Mark FAILED or contact support
```
""")

add("faq_time", """## Q: How long does payment take?

**A:** Usually seconds to minutes. Check Dashboard → Settlements for bank timing.
""")

add("faq_funds", """## Q: When do I receive funds?

**A:** Settlement timing depends on your merchant agreement. Check Dashboard → Settlements.
""")

add("faq_pci", """## Q: Do I need PCI compliance?

**A:** No. Hosted checkout means no raw credit card data on your servers.
""")

add("faq_cards", """## Q: Can I test with real cards?

**A:** No. Test mode only accepts test credentials and test card numbers.
""")

add("faq_failed", """## Q: How do I handle failed payments?

**A:** Verify hash, parse failure reason, update order status, and offer retry with a new `txnid`.
""")

add("faq_more", """## More FAQs

- **What if I don't get the webhook?** → Implement [reconciliation](doc:reconciliation-pattern)
- **What if response hash is wrong?** → Don't trust the response; verify against PayU spec
- **How do I refund?** → See [Refund Methods](doc:refund-methods-reference)

See also [General FAQs](doc:general-faqs) and [FAQs for Web Checkout](doc:faqs-for-web-checkout-integration).
""")

# Reference
add("ref_newclient", """## Overview

```go
client, err := payu.NewClient(key, salt, env)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| key | string | Merchant key |
| salt | string | Merchant salt |
| env | string | `"test"` or `"production"` |

Verify signature: `go doc github.com/payu-india/web-sdk-go`
""")

add("ref_payment", """## Overview

Potential payment methods (verify in your SDK version):

```go
// GetPaymentURL(request) → checkout URL
// VerifyPaymentHash(response) → true/false
// VerifyPayment(txnid) → payment status
```

```bash
go doc github.com/payu-india/web-sdk-go
```
""")

add("ref_refund", """## Overview

```go
// CreateRefund(txnid, amount) → refund ID
// GetRefundStatus(refundID) → refund status
```

Verify methods exist before use.
""")

add("ref_settlement", """## Overview

```go
// GetSettlements(from, to) → settlement details
```

See [Settlement Reconciliation](doc:settlement-reconciliation).
""")

add("ref_utility", """## Overview

Utility methods for eligibility, downtime, and invoices. Verify availability:

```bash
go doc github.com/payu-india/web-sdk-go
```
""")

add("spec_request", """## Overview

Payment request field specification.

| Field | Required | Format |
|-------|----------|--------|
| key | Yes | Merchant key |
| txnid | Yes | Unique string |
| amount | Yes | Decimal string (2 places) |
| productinfo | Yes | String |
| firstname | Yes | String |
| email | Yes | Valid email |
| phone | Yes | 10-digit mobile |
| surl | Yes | HTTPS URL |
| furl | Yes | HTTPS URL |
| hash | Yes | SHA512 hex |
""")

add("spec_response", """## Overview

Payment response includes `status`, `txnid`, `mihpayid`, `amount`, and `hash`.

Always verify `hash` before trusting `status`.
""")

add("spec_webhook", """## Overview

Webhook payload mirrors payment response fields. POST as JSON or form-encoded.

See [Webhooks](doc:webhooks).
""")

add("spec_hash", """## Overview

Hash field order for payment requests:

`sha512(key|txnid|amount|productinfo|firstname|email|||||||||||SALT)`

For API v19, see [Generate Hash](doc:hashing-request-and-response).
""")

add("spec_validation", """## Overview

Field validation rules:

- `txnid`: unique per transaction
- `amount`: positive, 2 decimal places
- `email`: valid format
- URLs: HTTPS only in production
""")

add("sec_credentials", """## Overview

- Store credentials in environment variables or secrets manager
- Rotate salts if compromised
- Never commit credentials to git
""")

add("sec_hash", """## Overview

- Always verify request and response hashes
- Use SHA512 per PayU specification
- Never skip verification in production
""")

add("sec_webhook", """## Overview

- Verify webhook hash on every request
- Use HTTPS endpoints only
- Return 200 after valid processing
""")

add("sec_pci", """## Overview

Hosted checkout eliminates PCI scope for card data — PayU handles card entry.

You remain responsible for securing your server and credentials.
""")

add("sec_data", """## Overview

- Do not log salt, card data, or full PII
- Encrypt data at rest where required
- Follow your organization's data retention policy
""")

add("perf_pooling", """## Overview

Reuse a single `payu.Client` instance initialized at startup. Do not create a new client per request.
""")

add("perf_timeout", """## Overview

Configure HTTP client timeouts for PayU API calls to avoid hung goroutines.
""")

add("perf_retry", """## Overview

Retry verify API calls with exponential backoff for transient network errors. Do not retry payment creation with the same `txnid` without idempotency checks.
""")

add("perf_cache", """## Overview

Cache bank downtime and eligibility responses with short TTL to reduce API calls.
""")

add("mig_history", """## Overview

Check SDK version history on [GitHub Releases](https://github.com/payu-india/web-sdk-go/releases).

```bash
go list -m -versions github.com/payu-india/web-sdk-go
```
""")

add("mig_breaking", """## Overview

Review release notes for breaking changes before upgrading.

```bash
go get github.com/payu-india/web-sdk-go@latest
go mod tidy
```
""")

add("mig_guide", """## Overview

When migrating SDK versions:

1. Read release notes
2. Update `go.mod`
3. Run tests
4. Verify hash and API method signatures
""")

add("mig_deprecation", """## Overview

Watch GitHub for deprecation notices. Update before deprecated methods are removed.
""")

add("adv_multi", """## Overview

Multi-currency support depends on your PayU merchant configuration. Contact your account manager for cross-border setup.

See [Cross-border Payments](doc:introduction-cross-border-payments-import) if applicable.
""")

add("adv_recurring", """## Overview

Recurring payments use PayU Subscriptions. See [Recurring Payments Integration](doc:introduction-recurring-payments-integration) if supported for your account.
""")

add("adv_bulk", """## Overview

Bulk operations (batch refunds, settlement exports) may be available via PayU APIs. Verify with `go doc` and PayU API reference.
""")

add("adv_custom", """## Overview

Custom integrations combining Go SDK with [Server-to-Server](doc:server-to-server-integration) or [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted) are possible with additional PCI requirements.
""")

# Getting help
add("help_docs", """## Overview

- PayU Docs: [https://docs.payu.in](https://docs.payu.in)
- [Go SDK Overview](doc:go-sdk)
""")

add("help_api", """## Overview

- [Generate Hash](doc:hashing-request-and-response)
- [Error Handling](doc:error-handling)
- [Webhooks](doc:webhooks)
""")

add("help_github", """## Overview

SDK source: [https://github.com/payu-india/web-sdk-go](https://github.com/payu-india/web-sdk-go)

```bash
go doc github.com/payu-india/web-sdk-go
```
""")

add("help_channels", """## Overview

- Email: support@payu.in
- Dashboard: [https://payumoney.com](https://payumoney.com)
""")

add("comm_github", """## Overview

Report SDK bugs via [GitHub Issues](https://github.com/payu-india/web-sdk-go/issues).
""")

add("comm_stack", """## Overview

Search Stack Overflow for `payu` + `golang` tags.
""")

add("comm_forum", """## Overview

Check PayU developer community channels for integration discussions.
""")

add("contact_info", """## Overview

When contacting support, provide:

- Merchant key (not salt)
- Sample `txnid` and `mihpayid`
- Timestamp and environment (test/live)
- Error message or logs (redact secrets)
""")

add("contact_fast", """## Overview

Get help faster by:

1. Checking [Troubleshooting](doc:common-integration-issues) first
2. Including reproducible steps
3. Specifying SDK version: `go list -m github.com/payu-india/web-sdk-go`
""")

add("contact_limits", """## Overview

- SDK method availability varies by version — always run `go doc`
- Hash logic must match PayU spec exactly
- Test mode does not process real payments
""")

# Navigation chains for next steps
NEXT_CHAIN = {
    "what-is-payu-go-sdk": ("when-to-use-go-sdk",),
    "when-to-use-go-sdk": ("supported-payment-methods",),
    "supported-payment-methods": ("create-payu-merchant-account",),
    "create-payu-merchant-account": ("understand-merchant-key-salt",),
    "understand-merchant-key-salt": ("technical-requirements",),
    "technical-requirements": ("environment-setup-guide",),
    "environment-setup-guide": ("install-go-module",),
    "install-go-module": ("initialize-sdk-client",),
    "initialize-sdk-client": ("verify-installation",),
    "verify-installation": ("quick-start-next-steps",),
    "install-go-sdk-module": ("verify-dependencies",),
    "verify-dependencies": ("dependency-troubleshooting",),
    "dependency-troubleshooting": ("initialize-with-credentials",),
    "initialize-with-credentials": ("configure-test-vs-production",),
    "configure-test-vs-production": ("verify-client-is-ready",),
    "verify-client-is-ready": ("payment-flow-overview",),
    "payment-flow-overview": ("create-payment-request",),
    "create-payment-request": ("generate-security-hash",),
    "generate-security-hash": ("redirect-to-checkout",),
    "redirect-to-checkout": ("receive-success-failure-url",),
    "receive-success-failure-url": ("verify-response-hash",),
    "verify-response-hash": ("test-payment-flow",),
    "test-payment-flow": ("production-readiness-checklist",),
    "code-review-checklist": ("security-verification",),
    "security-verification": ("testing-completion",),
    "testing-completion": ("switch-to-live-credentials",),
    "switch-to-live-credentials": ("change-environment-production",),
}


def get_related(slug: str) -> list[tuple[str, str]]:
    defaults = [
        ("Go SDK Overview", "go-sdk"),
        ("Troubleshooting", "common-integration-issues"),
    ]
    return defaults


def get_next(slug: str) -> list[tuple[str, str]]:
    if slug in NEXT_CHAIN:
        n = NEXT_CHAIN[slug]
        # map slug to title - simplified
        titles = {s: s.replace("-", " ").title() for s in n}
        return [(titles[s], s) for s in n]
    return [("Go SDK Overview", "go-sdk")]


def write_page(path: Path, title: str, content_key: str, slug: str):
    body = CONTENT.get(content_key, f"## Overview\n\nContent for {title}.\n")
    desc = f"PayU Go SDK guide: {title}"
    keywords = ["payu go sdk", title.lower(), "golang payment integration"]
    page = frontmatter(title, desc, keywords) + "\n" + body + related_next(get_related(slug), get_next(slug))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(page, encoding="utf-8")


def write_index(path: Path, title: str, intro: str, children: list[str]):
    desc = intro[:200]
    keywords = ["payu go sdk", title.lower()]
    links = "\n".join(f"- [{SUBSECTION_TITLES.get(c, c.replace('-', ' ').title())}](doc:{c})" if c in SUBSECTION_TITLES else f"- [{c.replace('-', ' ').title()}](doc:{c})" for c in children)
    # For subsection index, link to first page in subsection
    page = frontmatter(title, desc, keywords) + f"\n## Overview\n\n{intro}\n\n## In This Section\n\n{links}\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(page, encoding="utf-8")


def main():
    if BASE.exists():
        import shutil
        shutil.rmtree(BASE)
    BASE.mkdir(parents=True)

    # Root index
    root_intro = """The PayU Go SDK integrates PayU payment processing into Go applications. This documentation is organized as a workflow-centric developer journey — from installation through production.

**Version:** 5.0 | **SDK:** [github.com/payu-india/web-sdk-go](https://github.com/payu-india/web-sdk-go)

## Quick Navigation

- **Getting started?** → [Quick Start](doc:install-go-module)
- **Need help?** → [Common Integration Issues](doc:common-integration-issues)
- **Going live?** → [Production Readiness Checklist](doc:production-readiness-checklist)

## Critical: Code Verification Required

Before implementing any code examples:

1. Verify SDK methods exist in your installed version
2. Test hash implementation against PayU's payment specification
3. Compile and test all examples
4. Validate security-critical code (hash generation and verification)
"""
    root_fm = frontmatter(
        "Go SDK",
        "PayU Go server SDK: install, initialize, accept payments, verify responses, test, and go live.",
        ["payu go sdk", "golang payment gateway", "server side integration go"],
    )
    (BASE / "index.md").write_text(
        root_fm + "\n" + root_intro + "\n## Documentation Sections\n\n"
        + "\n".join(f"- [{SECTION_TITLES[s]}](doc:{s})" for s in STRUCTURE.keys())
        + "\n",
        encoding="utf-8",
    )

    section_order = list(STRUCTURE.keys())
    (BASE / "_order.yaml").write_text("\n".join(f"- {s}" for s in section_order) + "\n")

    for section, cfg in STRUCTURE.items():
        section_path = BASE / section
        section_path.mkdir(parents=True)
        (section_path / "_order.yaml").write_text(
            "\n".join(f"- {sub}" for sub in cfg["order"]) + "\n"
        )
        write_index(
            section_path / "index.md",
            SECTION_TITLES[section],
            f"Guides for {SECTION_TITLES[section].lower()} with the PayU Go SDK.",
            cfg["order"],
        )

        for subsection in cfg["order"]:
            sub_path = section_path / subsection
            sub_path.mkdir(parents=True)
            pages = cfg["subsections"][subsection]
            (sub_path / "_order.yaml").write_text(
                "\n".join(f"- {slug}" for slug, _, _ in pages) + "\n"
            )
            write_index(
                sub_path / "index.md",
                SUBSECTION_TITLES[subsection],
                f"{SUBSECTION_TITLES[subsection]} for PayU Go SDK.",
                [slug for slug, _, _ in pages],
            )
            for slug, title, content_key in pages:
                write_page(sub_path / f"{slug}.md", title, content_key, slug)

    print(f"Generated Go SDK docs at {BASE}")
    count = sum(1 for _ in BASE.rglob("*.md"))
    print(f"Total markdown files: {count}")


if __name__ == "__main__":
    main()
