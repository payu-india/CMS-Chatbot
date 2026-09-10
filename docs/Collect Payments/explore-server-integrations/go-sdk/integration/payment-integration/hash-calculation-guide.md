---
title: Hash Calculation Guide
excerpt: 'PayU Go SDK guide: Hash Calculation Guide'
deprecated: false
hidden: false
metadata:
  title: 'Hash Calculation Guide | PayU Go SDK'
  description: 'PayU Go SDK guide: Hash Calculation Guide'
  keywords:
    - payu go sdk
    - hash calculation guide
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Detailed hash calculation for PayU Go SDK integrations.

For complete hash logic, refer to [Generate Hash](doc:hashing-request-and-response).

## Basic Payment Request Hash

`sha512(key|txnid|amount|productinfo|firstname|email|||||||||||SALT)`

## Response Hash (Reverse Hashing)

Always verify the response hash before trusting payment status. See [Verify Response Hash](doc:verify-response-hash).

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
