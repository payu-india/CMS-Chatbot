---
title: Payment Request Format
excerpt: 'PayU Go SDK guide: Payment Request Format'
deprecated: false
hidden: false
metadata:
  title: 'Payment Request Format | PayU Go SDK'
  description: 'PayU Go SDK guide: Payment Request Format'
  keywords:
    - payu go sdk
    - payment request format
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Payment request field specification.

| Field | Required | Format |
|-------|----------|--------|
| key | Yes | Merchant key |
| txnid | Yes | Unique string |
| amount | Yes | Decimal string (2 places) |
| productinfo | Yes | String |
| firstname | Yes | String |
| email | Yes | Valid email |
| phone | Yes | 10-digit mobile |
| surl | Yes | HTTPS URL |
| furl | Yes | HTTPS URL |
| hash | Yes | SHA512 hex |

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
