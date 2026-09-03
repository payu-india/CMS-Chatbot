---
title: Initialization Errors & Solutions
excerpt: 'PayU Go SDK guide: Initialization Errors & Solutions'
deprecated: false
hidden: false
metadata:
  title: 'Initialization Errors & Solutions | PayU Go SDK'
  description: 'PayU Go SDK guide: Initialization Errors & Solutions'
  keywords:
    - payu go sdk
    - initialization errors & solutions
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Diagnose and fix SDK initialization failures.

## Checklist

- [ ] `PAYU_MERCHANT_KEY` set? `echo $PAYU_MERCHANT_KEY`
- [ ] `PAYU_MERCHANT_SALT` set? `echo $PAYU_MERCHANT_SALT`
- [ ] Both non-empty?
- [ ] Keys match your PayU account (test vs live)?

See [SDK Won't Initialize](doc:sdk-wont-initialize) decision tree.

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Go SDK Overview](doc:go-sdk)
