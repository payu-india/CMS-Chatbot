---
title: Retry Strategies
excerpt: 'PayU Go SDK guide: Retry Strategies'
deprecated: false
hidden: false
metadata:
  title: 'Retry Strategies | PayU Go SDK'
  description: 'PayU Go SDK guide: Retry Strategies'
  keywords:
    - payu go sdk
    - retry strategies
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Retry verify API calls with exponential backoff for transient network errors. Do not retry payment creation with the same `txnid` without idempotency checks.

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
