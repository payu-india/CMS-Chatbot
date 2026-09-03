---
title: Understand Merchant Key & Salt
excerpt: 'PayU Go SDK guide: Understand Merchant Key & Salt'
deprecated: false
hidden: false
metadata:
  title: 'Understand Merchant Key & Salt | PayU Go SDK'
  description: 'PayU Go SDK guide: Understand Merchant Key & Salt'
  keywords:
    - payu go sdk
    - understand merchant key & salt
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Merchant Key and Salt authenticate your server with PayU and are required for hash generation and verification.

## Get Test Credentials

1. PayU Dashboard → **Test Mode**
2. **Developers → API Keys**
3. Copy **Merchant Key** and **Merchant Salt**

## Get Live Credentials

1. PayU Dashboard → **Live Mode**
2. **Developers → API Keys**
3. Copy **Live Merchant Key** and **Salt**

See also [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy).

## Best Practices

- Never hardcode credentials in source code
- Use environment variables or a secrets manager
- Use test keys only in test environment

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Technical Requirements](doc:technical-requirements)
