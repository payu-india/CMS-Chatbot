---
title: Payment States & Transitions
excerpt: 'PayU Go SDK guide: Payment States & Transitions'
deprecated: false
hidden: false
metadata:
  title: 'Payment States & Transitions | PayU Go SDK'
  description: 'PayU Go SDK guide: Payment States & Transitions'
  keywords:
    - payu go sdk
    - payment states & transitions
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

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

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
