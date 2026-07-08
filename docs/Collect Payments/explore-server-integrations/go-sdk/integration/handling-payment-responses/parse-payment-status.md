---
title: Parse Payment Status
excerpt: 'PayU Go SDK guide: Parse Payment Status'
deprecated: false
hidden: false
metadata:
  title: 'Parse Payment Status | PayU Go SDK'
  description: 'PayU Go SDK guide: Parse Payment Status'
  keywords:
    - payu go sdk
    - parse payment status
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Parse payment status from PayU response payload.

## Payment Status Values

| Status | Meaning |
|--------|---------|
| `success` | Payment completed |
| `failure` | Payment failed |
| `pending` | Awaiting confirmation |

Parse `status`, `txnid`, `mihpayid`, and `amount` from the response JSON.

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
