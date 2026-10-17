---
title: Idempotency & Duplicate Detection
excerpt: 'PayU Go SDK guide: Idempotency & Duplicate Detection'
deprecated: false
hidden: false
metadata:
  title: 'Idempotency & Duplicate Detection | PayU Go SDK'
  description: 'PayU Go SDK guide: Idempotency & Duplicate Detection'
  keywords:
    - payu go sdk
    - idempotency & duplicate detection
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Prevent duplicate order updates from retries and duplicate webhooks.

- Store processed `txnid` values
- Check before updating order status
- Use database unique constraints on `txnid`

See [Handle Duplicate Webhooks](doc:handle-duplicate-webhooks).

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
