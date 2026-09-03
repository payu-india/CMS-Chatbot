---
title: NewClient()
excerpt: 'PayU Go SDK guide: NewClient()'
deprecated: false
hidden: false
metadata:
  title: 'NewClient() | PayU Go SDK'
  description: 'PayU Go SDK guide: NewClient()'
  keywords:
    - payu go sdk
    - newclient()
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

```go
client, err := payu.NewClient(key, salt, env)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| key | string | Merchant key |
| salt | string | Merchant salt |
| env | string | `"test"` or `"production"` |

Verify signature: `go doc github.com/payu-india/web-sdk-go`

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
