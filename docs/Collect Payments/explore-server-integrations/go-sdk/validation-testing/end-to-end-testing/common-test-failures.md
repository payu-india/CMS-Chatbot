---
title: Common Test Failures
excerpt: 'PayU Go SDK guide: Common Test Failures'
deprecated: false
hidden: false
metadata:
  title: 'Common Test Failures | PayU Go SDK'
  description: 'PayU Go SDK guide: Common Test Failures'
  keywords:
    - payu go sdk
    - common test failures
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Common test failures and fixes.

| Failure | Fix |
|---------|-----|
| Hash mismatch | Check field order and salt |
| Checkout 404 | Verify base URL (test.payu.in) |
| No webhook | Check HTTPS and Dashboard config |
| Order not updated | Verify hash before update logic |

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
