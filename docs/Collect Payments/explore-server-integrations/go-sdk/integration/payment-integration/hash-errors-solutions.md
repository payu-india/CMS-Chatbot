---
title: Hash Errors & Solutions
excerpt: 'PayU Go SDK guide: Hash Errors & Solutions'
deprecated: false
hidden: false
metadata:
  title: 'Hash Errors & Solutions | PayU Go SDK'
  description: 'PayU Go SDK guide: Hash Errors & Solutions'
  keywords:
    - payu go sdk
    - hash errors & solutions
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Fix hash generation and verification failures.

## Checklist

- [ ] Field order correct (verify against PayU spec)
- [ ] Amount has 2 decimals (`999.99` not `999.9`)
- [ ] Salt is correct for environment (test vs live)
- [ ] All fields included (even empty UDF fields)
- [ ] Using SHA512

**Test:** Generate hash manually and compare with PayU's hash.

See [Hash Verification Fails](doc:hash-verification-fails) decision tree.

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
