---
title: SDK Won't Initialize
excerpt: 'PayU Go SDK guide: SDK Won't Initialize'
deprecated: false
hidden: false
metadata:
  title: 'SDK Won't Initialize | PayU Go SDK'
  description: 'PayU Go SDK guide: SDK Won't Initialize'
  keywords:
    - payu go sdk
    - sdk won't initialize
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Decision tree: SDK won't initialize.

```
Credentials set? → No → Set PAYU_MERCHANT_KEY and PAYU_MERCHANT_SALT
        ↓ Yes
Keys match environment? → No → Use test keys with "test" env
        ↓ Yes
NewClient() error? → Check error message → Fix credentials or network
        ↓ Success
Client ready ✅
```

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
