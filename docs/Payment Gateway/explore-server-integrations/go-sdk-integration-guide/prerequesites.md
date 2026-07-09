---
title: Before You Start (Prerequisites)
deprecated: false
hidden: true
metadata:
  robots: index
---
Install the PayU Go SDK and integrate it with your Go-based website to accept payments, initiate refunds and do much more. Go through these prerequisites before you start integrating Go SDK.

## Create a PayU Account

You should create a PayU account before integrating the Go SDK.

### Expected Outcome

After creating an account, you get:

- Test Mode access with API keys
- Live Mode access after merchant approval

### Best Practices

Always follow these best practices while creating a PayU account:

- Complete KYC early to avoid go-live delays
- Use Test Mode for all development

***

## Understand Merchant Key and Salt

Merchant key and salt are unique identifiers that authenticates your server with PayU. These are required for hash generation and verification.

<ToggleList>
  <ToggleListItem title="How do I get test Merchant Key and Salt?">
    1. PayU Dashboard → **Test Mode**
    2. **Developers → API Keys**
    3. Copy **Merchant Key** and **Merchant Salt**
  </ToggleListItem>
  <ToggleListItem title="How do I get Merchant Key and Salt?">
    1. PayU Dashboard → **Live Mode**
    2. **Developers → API Keys**
    3. Copy **Live Merchant Key** and **Salt**
  </ToggleListItem>
</ToggleList>

### Best Practices

- Never hardcode credentials in source code
- Use only test keys for testing your integration.

***

## Technical Requirements

These are the technical prerequisites or requirements for PayU Go SDK integration.

- **Go 1.18+**
- `go.mod` initialized in your project
- **HTTPS URLs** for success, failure, and webhook callbacks
- Internet access to PayU servers (`test.payu.in` / `payu.in`)

***

## Environment Setup Guide

Configure environment variables for local and deployed environments.

```bash
# Test environment
export PAYU_MERCHANT_KEY="your_test_key"
export PAYU_MERCHANT_SALT="your_test_salt"
export PAYU_ENV="test"
```

### Best Practices

We recommend not to hardcode credentials. Use environment variables, `.env` files (not committed), or your platform's secret store.

***

## Next Steps

- Quick Start

<br />

<br />
