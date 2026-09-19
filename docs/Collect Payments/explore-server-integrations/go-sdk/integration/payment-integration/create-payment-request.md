---
title: Create Payment Request
excerpt: 'PayU Go SDK guide: Create Payment Request'
deprecated: false
hidden: false
metadata:
  title: 'Create Payment Request | PayU Go SDK'
  description: 'PayU Go SDK guide: Create Payment Request'
  keywords:
    - payu go sdk
    - create payment request
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

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

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Generate Security Hash](doc:generate-security-hash)
