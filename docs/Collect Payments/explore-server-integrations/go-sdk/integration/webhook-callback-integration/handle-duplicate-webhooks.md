---
title: Handle Duplicate Webhooks
excerpt: 'PayU Go SDK guide: Handle Duplicate Webhooks'
deprecated: false
hidden: false
metadata:
  title: 'Handle Duplicate Webhooks | PayU Go SDK'
  description: 'PayU Go SDK guide: Handle Duplicate Webhooks'
  keywords:
    - payu go sdk
    - handle duplicate webhooks
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

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

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
