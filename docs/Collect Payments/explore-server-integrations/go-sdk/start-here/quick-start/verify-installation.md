---
title: Verify Installation
excerpt: 'PayU Go SDK guide: Verify Installation'
deprecated: false
hidden: false
metadata:
  title: 'Verify Installation | PayU Go SDK'
  description: 'PayU Go SDK guide: Verify Installation'
  keywords:
    - payu go sdk
    - verify installation
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Confirm the SDK module is installed correctly.

## Step-by-Step Guide

```bash
go list -m github.com/payu-india/web-sdk-go
go mod verify
```

## Success Criteria

- Module version is listed
- `go mod verify` reports all modules verified

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Quick Start Next Steps](doc:quick-start-next-steps)
