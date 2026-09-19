---
title: Hash Verification Fails
excerpt: 'PayU Go SDK guide: Hash Verification Fails'
deprecated: false
hidden: false
metadata:
  title: 'Hash Verification Fails | PayU Go SDK'
  description: 'PayU Go SDK guide: Hash Verification Fails'
  keywords:
    - payu go sdk
    - hash verification fails
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Decision tree: Hash verification fails.

```
Correct salt? → No → Match test/live salt to environment
        ↓ Yes
Field order correct? → No → See Hash Field Order
        ↓ Yes
SHA512 used? → No → Switch to SHA512
        ↓ Yes
Amount format correct? → No → Use 2 decimal places
        ↓ Yes
Re-test with manual hash comparison
```

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
