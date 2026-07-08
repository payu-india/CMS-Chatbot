---
title: Install Go Module
excerpt: 'PayU Go SDK guide: Install Go Module'
deprecated: false
hidden: false
metadata:
  title: 'Install Go Module | PayU Go SDK'
  description: 'PayU Go SDK guide: Install Go Module'
  keywords:
    - payu go sdk
    - install go module
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Install the PayU Go SDK module in under a minute.

## Step-by-Step Guide

```bash
go get github.com/payu-india/web-sdk-go
go mod tidy
```

## Expected Output

Module added to `go.mod` with no errors.

## Code Examples

```go
import payu "github.com/payu-india/web-sdk-go"
```

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Initialize Sdk Client](doc:initialize-sdk-client)
