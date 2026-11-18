---
title: Payment Request Fails
excerpt: 'PayU Go SDK guide: Payment Request Fails'
deprecated: false
hidden: false
metadata:
  title: 'Payment Request Fails | PayU Go SDK'
  description: 'PayU Go SDK guide: Payment Request Fails'
  keywords:
    - payu go sdk
    - payment request fails
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

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

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
