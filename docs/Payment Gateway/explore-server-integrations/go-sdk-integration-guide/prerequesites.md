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
  <ToggleListItem title="How do i get Test Credentials?">
    Hoooo-dunnits 🔎
  </ToggleListItem>
  <ToggleListItem title="What’s an owl’s favorite drink?">
    Hoot beer 🥤
  </ToggleListItem>
</ToggleList>

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

<br />

## Next Steps

- [Understand Merchant Key Salt](doc:understand-merchant-key-salt)

<br />

<br />
