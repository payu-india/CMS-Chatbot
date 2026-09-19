---
title: Payment Flow Overview
excerpt: 'PayU Go SDK guide: Payment Flow Overview'
deprecated: false
hidden: false
metadata:
  title: 'Payment Flow Overview | PayU Go SDK'
  description: 'PayU Go SDK guide: Payment Flow Overview'
  keywords:
    - payu go sdk
    - payment flow overview
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

End-to-end payment flow for PayU hosted checkout with the Go SDK.

> Flow Diagram: PayU Go SDK Payment Integration

```
1. Customer initiates payment
2. Your app creates payment request
3. Your app generates hash (security verification)
4. Your app redirects to PayU checkout
5. Customer completes payment at PayU
6. PayU redirects to your callback URL
7. Your app verifies response hash
8. Your app updates order status
```

## Workflow Overview

Hosted checkout keeps card data on PayU servers — you never handle raw card numbers.

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Create Payment Request](doc:create-payment-request)
