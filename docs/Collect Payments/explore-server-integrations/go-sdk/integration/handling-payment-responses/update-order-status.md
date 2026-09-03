---
title: Update Order Status
excerpt: 'PayU Go SDK guide: Update Order Status'
deprecated: false
hidden: false
metadata:
  title: 'Update Order Status | PayU Go SDK'
  description: 'PayU Go SDK guide: Update Order Status'
  keywords:
    - payu go sdk
    - update order status
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Update your order database after verified payment.

## Workflow

1. Verify response hash
2. Confirm `status == "success"`
3. Match `txnid` to your order
4. Match `amount` to order total
5. Update order status atomically
6. Trigger fulfillment

## Best Practices

- Use database transactions
- Implement idempotency (same `txnid` processed once)

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
