---
title: Receive Success/Failure URL
excerpt: 'PayU Go SDK guide: Receive Success/Failure URL'
deprecated: false
hidden: false
metadata:
  title: 'Receive Success/Failure URL | PayU Go SDK'
  description: 'PayU Go SDK guide: Receive Success/Failure URL'
  keywords:
    - payu go sdk
    - receive success/failure url
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Handle success and failure redirect URLs after customer completes checkout.

PayU redirects the customer's browser to `surl` (success) or `furl` (failure) with payment response data.

## Best Practices

- Always verify hash before processing
- Do not fulfill orders on redirect alone — confirm via webhook or verify API

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Verify Response Hash](doc:verify-response-hash)
