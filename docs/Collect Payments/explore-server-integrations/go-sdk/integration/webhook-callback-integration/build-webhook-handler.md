---
title: Build Webhook Handler
excerpt: 'PayU Go SDK guide: Build Webhook Handler'
deprecated: false
hidden: false
metadata:
  title: 'Build Webhook Handler | PayU Go SDK'
  description: 'PayU Go SDK guide: Build Webhook Handler'
  keywords:
    - payu go sdk
    - build webhook handler
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

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

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
