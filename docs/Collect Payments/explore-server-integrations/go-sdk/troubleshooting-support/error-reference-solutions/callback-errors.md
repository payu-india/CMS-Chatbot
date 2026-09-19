---
title: Callback Errors
excerpt: 'PayU Go SDK guide: Callback Errors'
deprecated: false
hidden: false
metadata:
  title: 'Callback Errors | PayU Go SDK'
  description: 'PayU Go SDK guide: Callback Errors'
  keywords:
    - payu go sdk
    - callback errors
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Callback-specific errors.

- Invalid hash → reject and log
- Missing fields → return 400
- Duplicate processing → return 200 (idempotent)

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
