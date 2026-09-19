---
title: Configure Test vs Production
excerpt: 'PayU Go SDK guide: Configure Test vs Production'
deprecated: false
hidden: false
metadata:
  title: 'Configure Test vs Production | PayU Go SDK'
  description: 'PayU Go SDK guide: Configure Test vs Production'
  keywords:
    - payu go sdk
    - configure test vs production
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Configure test vs production environments.

| Value | Purpose | Server |
|-------|---------|--------|
| `"test"` | Sandbox | test.payu.in |
| `"production"` | Live | payu.in |

**Always test thoroughly before switching to production.**

```go
client, err := payu.NewClient(key, salt, "test") // or "production"
```

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Verify Client Is Ready](doc:verify-client-is-ready)
