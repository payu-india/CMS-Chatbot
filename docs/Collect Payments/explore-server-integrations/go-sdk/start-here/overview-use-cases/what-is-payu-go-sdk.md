---
title: What is PayU Go SDK?
excerpt: 'PayU Go SDK guide: What is PayU Go SDK?'
deprecated: false
hidden: false
metadata:
  title: 'What is PayU Go SDK? | PayU Go SDK'
  description: 'PayU Go SDK guide: What is PayU Go SDK?'
  keywords:
    - payu go sdk
    - what is payu go sdk?
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

The PayU Go SDK integrates PayU payment processing into Go applications. It provides payment request creation, response verification via hash validation, payment status queries, and refund and settlement management.

**Verify supported features in your SDK version before implementing.**

## Who Should Read This

Go backend developers integrating PayU hosted checkout for the first time.

## What the SDK Does

- Payment request creation and redirect to PayU checkout
- Response verification via hash validation
- Payment status queries
- Refund and settlement management

> 🚧 Download Go SDK
>
> GitHub: [https://github.com/payu-india/web-sdk-go](https://github.com/payu-india/web-sdk-go)

## Best Practices

- Verify SDK methods exist in your installed version: `go doc github.com/payu-india/web-sdk-go`
- Never copy-paste code without compiling and testing
- Validate hash implementation against PayU's official specification

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [When To Use Go Sdk](doc:when-to-use-go-sdk)
