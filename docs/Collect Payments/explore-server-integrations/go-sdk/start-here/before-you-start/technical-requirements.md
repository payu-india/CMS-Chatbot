---
title: Technical Requirements
excerpt: 'PayU Go SDK guide: Technical Requirements'
deprecated: false
hidden: false
metadata:
  title: 'Technical Requirements | PayU Go SDK'
  description: 'PayU Go SDK guide: Technical Requirements'
  keywords:
    - payu go sdk
    - technical requirements
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Technical prerequisites for PayU Go SDK integration.

## Prerequisites

- **Go 1.18+**
- `go.mod` initialized in your project
- **HTTPS URLs** for success, failure, and webhook callbacks
- Internet access to PayU servers (`test.payu.in` / `payu.in`)

## Success Criteria

- `go version` shows 1.18 or higher
- Callback URLs are publicly reachable over HTTPS

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Environment Setup Guide](doc:environment-setup-guide)
