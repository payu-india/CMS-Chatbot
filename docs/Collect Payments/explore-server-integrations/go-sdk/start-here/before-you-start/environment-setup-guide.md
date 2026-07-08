---
title: Environment Setup Guide
excerpt: 'PayU Go SDK guide: Environment Setup Guide'
deprecated: false
hidden: false
metadata:
  title: 'Environment Setup Guide | PayU Go SDK'
  description: 'PayU Go SDK guide: Environment Setup Guide'
  keywords:
    - payu go sdk
    - environment setup guide
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Configure environment variables for local and deployed environments.

## Step-by-Step Guide

```bash
# Test environment
export PAYU_MERCHANT_KEY="your_test_key"
export PAYU_MERCHANT_SALT="your_test_salt"
export PAYU_ENV="test"
```

## Best Practices

**Never hardcode credentials.** Use environment variables, `.env` files (not committed), or your platform's secret store.

## Common Mistakes

- Mixing test keys with production environment (or vice versa)
- Committing credentials to version control

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Install Go Module](doc:install-go-module)
