---
title: Reconciliation Pattern
excerpt: 'PayU Go SDK guide: Reconciliation Pattern'
deprecated: false
hidden: false
metadata:
  title: 'Reconciliation Pattern | PayU Go SDK'
  description: 'PayU Go SDK guide: Reconciliation Pattern'
  keywords:
    - payu go sdk
    - reconciliation pattern
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

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

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
