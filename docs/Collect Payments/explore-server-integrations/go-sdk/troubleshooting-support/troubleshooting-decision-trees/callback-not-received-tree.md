---
title: Callback Not Received
excerpt: 'PayU Go SDK guide: Callback Not Received'
deprecated: false
hidden: false
metadata:
  title: 'Callback Not Received | PayU Go SDK'
  description: 'PayU Go SDK guide: Callback Not Received'
  keywords:
    - payu go sdk
    - callback not received
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Decision tree: Callback not received.

```
HTTPS URL? → No → Switch to HTTPS
        ↓ Yes
Publicly accessible? → No → Fix firewall/DNS
        ↓ Yes
Returns 200? → No → Fix handler errors
        ↓ Yes
Webhook enabled in Dashboard? → No → Enable webhook
        ↓ Yes
Use reconciliation as backup
```

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
