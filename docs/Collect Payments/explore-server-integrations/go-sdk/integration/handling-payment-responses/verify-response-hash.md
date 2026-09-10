---
title: Verify Response Hash
excerpt: 'PayU Go SDK guide: Verify Response Hash'
deprecated: false
hidden: false
metadata:
  title: 'Verify Response Hash | PayU Go SDK'
  description: 'PayU Go SDK guide: Verify Response Hash'
  keywords:
    - payu go sdk
    - verify response hash
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

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

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Test Payment Flow](doc:test-payment-flow)
