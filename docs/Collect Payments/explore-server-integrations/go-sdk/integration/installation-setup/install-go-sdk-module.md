---
title: Install Go SDK Module
excerpt: 'PayU Go SDK guide: Install Go SDK Module'
deprecated: false
hidden: false
metadata:
  title: 'Install Go SDK Module | PayU Go SDK'
  description: 'PayU Go SDK guide: Install Go SDK Module'
  keywords:
    - payu go sdk
    - install go sdk module
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Download and verify the PayU Go SDK module.

## Step-by-Step Guide

```bash
go get github.com/payu-india/web-sdk-go
go mod tidy
go mod verify
```

```bash
go list -m github.com/payu-india/web-sdk-go
```

```go
import payu "github.com/payu-india/web-sdk-go"
```

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Verify Dependencies](doc:verify-dependencies)
