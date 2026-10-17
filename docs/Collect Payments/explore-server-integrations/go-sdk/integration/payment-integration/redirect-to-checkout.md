---
title: Redirect to Checkout
excerpt: 'PayU Go SDK guide: Redirect to Checkout'
deprecated: false
hidden: false
metadata:
  title: 'Redirect to Checkout | PayU Go SDK'
  description: 'PayU Go SDK guide: Redirect to Checkout'
  keywords:
    - payu go sdk
    - redirect to checkout
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

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

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Receive Success Failure Url](doc:receive-success-failure-url)
