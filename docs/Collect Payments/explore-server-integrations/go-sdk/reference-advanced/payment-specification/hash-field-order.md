---
title: Hash Field Order
excerpt: 'PayU Go SDK guide: Hash Field Order'
deprecated: false
hidden: false
metadata:
  title: 'Hash Field Order | PayU Go SDK'
  description: 'PayU Go SDK guide: Hash Field Order'
  keywords:
    - payu go sdk
    - hash field order
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Hash field order for payment requests:

`sha512(key|txnid|amount|productinfo|firstname|email|||||||||||SALT)`

For API v19, see [Generate Hash](doc:hashing-request-and-response).

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
