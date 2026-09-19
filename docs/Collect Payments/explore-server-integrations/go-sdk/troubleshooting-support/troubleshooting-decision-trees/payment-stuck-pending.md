---
title: Payment Stuck Pending
excerpt: 'PayU Go SDK guide: Payment Stuck Pending'
deprecated: false
hidden: false
metadata:
  title: 'Payment Stuck Pending | PayU Go SDK'
  description: 'PayU Go SDK guide: Payment Stuck Pending'
  keywords:
    - payu go sdk
    - payment stuck pending
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Decision tree: Payment stuck pending.

```
Query verify API → success? → Update order to PAID
        ↓ failed
Mark order FAILED
        ↓ still pending
Wait + reconcile → >24h? → Mark FAILED or contact support
```

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
