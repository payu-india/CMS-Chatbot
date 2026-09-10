---
title: Enable Logging
excerpt: 'PayU Go SDK guide: Enable Logging'
deprecated: false
hidden: false
metadata:
  title: 'Enable Logging | PayU Go SDK'
  description: 'PayU Go SDK guide: Enable Logging'
  keywords:
    - payu go sdk
    - enable logging
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Enable structured logging for payment debugging.

```go
log.Printf("Payment request: txnid=%s amount=%s", req.Txnid, req.Amount)
log.Printf("Hash input length: %d", len(hashInput))
```

**Never log salt or full card data.**

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
