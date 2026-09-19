---
title: Recovery Strategies
excerpt: 'PayU Go SDK guide: Recovery Strategies'
deprecated: false
hidden: false
metadata:
  title: 'Recovery Strategies | PayU Go SDK'
  description: 'PayU Go SDK guide: Recovery Strategies'
  keywords:
    - payu go sdk
    - recovery strategies
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Recovery strategies for failed integrations.

1. **Hash fails** → verify spec, re-test with test credentials
2. **Webhook missing** → run reconciliation
3. **Payment pending** → query verify API
4. **Duplicate charge** → initiate refund via SDK

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
