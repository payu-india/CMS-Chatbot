---
title: Verify Dependencies
excerpt: 'PayU Go SDK guide: Verify Dependencies'
deprecated: false
hidden: false
metadata:
  title: 'Verify Dependencies | PayU Go SDK'
  description: 'PayU Go SDK guide: Verify Dependencies'
  keywords:
    - payu go sdk
    - verify dependencies
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Verify all Go module dependencies resolve correctly.

```bash
go mod verify
go mod download
go build ./...
```

## Success Criteria

Build completes without dependency errors.

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Dependency Troubleshooting](doc:dependency-troubleshooting)
