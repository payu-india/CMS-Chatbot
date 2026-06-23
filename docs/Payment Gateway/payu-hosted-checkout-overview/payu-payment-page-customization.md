---
title: Customize PayU Hosted Checkout
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Customize PayU Payment Page or Checkout Page
  description: ''
  robots: index
next:
  description: ''
---
Customize the PayU Hosted Checkout experience by controlling:

- Which payment methods customers can see
- Which payment methods should be hidden
- Which checkout language should be displayed
- Which payment methods should be enabled for your business

Use this guide to reduce payment friction, improve conversion, and tailor checkout to your business needs.

***

# Quickstart

| Goal                                                   | Use This                     |
| ------------------------------------------------------ | ---------------------------- |
| Show only specific payment methods (example: UPI only) | `enforce_paymethod`          |
| Hide specific payment methods (example: wallets)       | `drop_category`              |
| Change checkout language                               | Language parameter           |
| Enable BNPL or other methods                           | PayU Dashboard configuration |

***

# Use Cases

<Accordion title="Common Use Cases" icon="fa-layer-group">
You can use this guide to:

- Show only UPI and cards
- Hide credit cards
- Hide wallets
- Display checkout in other languages
- Enable BNPL for eligible merchants
- Restrict checkout based on business rules
</Accordion>

<br />

***

# Prerequisites

<Accordion title="Checklist" icon="fa-list-check">
Before customizing checkout, ensure you have:

- Active PayU merchant account (test or production)
- API Key and Salt
- Hosted Checkout integration completed
- Merchant eligibility for payment methods you want to use
- Dashboard permissions (for enabling methods)
</Accordion>

> ✅ **Enable Payment Methods**
>
> Some payment methods (such as BNPL) require PayU approval or merchant eligibility before they appear in checkout. Get in touch with your key account manager to enable them in the dashboard.

***

# Configuration Decision Matrix

Use this decision matrix to choose the correct approach.

| If You Want To                      | Use                      |
| ----------------------------------- | ------------------------ |
| Allow only selected payment methods | Restrict Payment Methods |
| Hide selected payment methods       | Drop Payment Methods     |
| Change language                     | Set Checkout Language    |
| Enable new payment category         | Dashboard Configuration  |

***

# Restrict Checkout to Specific Payment Methods (`enforce_paymethod`)

You can append the parameter names in your transaction request to restrict checkout to some of the payment modes.

Examples:

- Show only UPI
- Show only cards
- Show only UPI + NetBanking

### How it Works

PayU will show only the payment methods in the checkout you explicitly pass in the request.

### Sample Request

<Accordion title="Sample Payload" icon="fa-code">
The `enforce_paymethod` parameter allows you to customize payment methods in the checkout. You can restrict specific payment modes, cards scheme, and specific banks under Net Banking using this parameter.


</Accordion>

```curl
```

***

## Example: Show Only UPI and Cards

```json
{
  "enforce_paymethod": "upi|cards"
}
```

***

## Example: Restrict Using Bank Codes

```json
{
  "enforce_paymethod": "nb",
  "bankcode": "HDFC"
}
```

***

## Common Failures for `enforce_paymethod`

### Payment method not showing

Possible causes:

- Invalid method value
- Method not enabled for merchant
- Bank code invalid
- Hash not regenerated

***

# Step 3: Hide Specific Payment Methods (`drop_category`)

Use this when you want a **blacklist**.

Examples:

- Hide wallets
- Hide credit cards
- Hide net banking

***

## Example: Hide Wallets

```json
{
  "drop_category": "wallet"
}
```

***

## Example: Hide Cards

```json
{
  "drop_category": "cards"
}
```

***

## Common Failures for Drop Configuration

### Method still visible

Possible causes:

- Invalid category
- Drop parameter not passed
- Conflicting rules
- Merchant-level override

***

# Step 4: Set Checkout Display Language

Use this to localize checkout.

Supported examples:

- English
- Hindi
- Tamil

***

## Example: Hindi Checkout

```json
{
  "language": "hi"
}
```

***

## Common Failures for Language Configuration

### Language not changing

Possible causes:

- Unsupported language
- Invalid parameter
- Language fallback to default

***

# Supported Parameter Reference

## Payment Method Values

Common supported values:

| Value    | Meaning            |
| -------- | ------------------ |
| `upi`    | UPI                |
| `cards`  | Credit/Debit Cards |
| `nb`     | Net Banking        |
| `wallet` | Wallets            |
| `emi`    | EMI                |

Refer to full PayU reference for all supported values.

***

## Bank Codes

Use bank codes when restricting specific banking methods.

Examples:

- HDFC
- ICICI
- SBI

***

## Scheme Codes

Use scheme codes for scheme-specific routing where applicable.

***

# Conflict & Precedence Rules

Understanding precedence prevents unexpected behavior.

***

## What Happens if You Use Both `enforce_paymethod` and `drop_category`?

Avoid using both unless explicitly supported.

This can create conflicting rules.

Example:

- enforce = cards
- drop = cards

Result may be:

- empty checkout
- fallback behavior
- invalid configuration

***

## Dashboard vs API Request Priority

General precedence:

1. Merchant eligibility
2. Dashboard enablement
3. Runtime request parameters

If a payment method is not enabled for your merchant, runtime parameters cannot force it to appear.

***

## Invalid Parameter Behavior

Depending on implementation, PayU may:

- ignore invalid values
- fallback to defaults
- reject request

Validate parameter values before production rollout.

***

# Validate Checkout After Customization

Validation should happen in four stages.

***

## 1. Request Validation

Verify:

- parameter exists in request
- value is correct
- delimiters are correct

***

## 2. Hash Validation

After adding customization parameters:

- regenerate hash
- verify parameter order
- confirm request signature

> **Warning**
> Invalid hash is one of the most common integration failures after adding customization parameters.

Common causes:

- wrong parameter order
- missing parameter in hash generation
- stale hash

***

## 3. Checkout Validation

Verify:

- expected methods appear
- hidden methods are absent
- language changed correctly

Test:

- desktop
- mobile
- multiple browsers

***

## 4. Production Validation

Before go-live:

- test with real merchant configuration
- validate dashboard enablement
- verify analytics and logs

***

# Common Errors & Troubleshooting

## Payment Method Not Showing

Possible causes:

- method not enabled
- invalid value
- merchant ineligible
- incorrect bank code

Fix:

- validate reference values
- verify dashboard setup
- check request payload

***

## Payment Method Still Visible After Drop

Possible causes:

- wrong category
- conflicting rules
- parameter ignored

Fix:

- verify category values
- check precedence rules

***

## Invalid Hash Error

Possible causes:

- parameter order issue
- stale hash
- missing parameter during signature generation

Fix:

- regenerate hash after every payload change
- verify hash logic

***

## Checkout Language Not Changing

Possible causes:

- unsupported language
- invalid language code
- fallback behavior

***

# Best Practices

Follow these recommendations:

- Prefer `enforce_paymethod` when you need strict control
- Use drop configuration sparingly
- Always test in sandbox before production
- Recalculate hash after request changes
- Validate on desktop and mobile
- Monitor conversion impact after customization

***

# FAQs

## Can I show only UPI?

Yes. Use `enforce_paymethod = upi`.

***

## Can I hide only credit cards?

Yes, if cards are exposed as a supported drop category.

***

## Can I use both enforce and drop together?

Avoid unless explicitly supported.

***

## Can I customize checkout per transaction?

Yes, using request-level parameters.

***

## Why is BNPL not available?

Possible reasons:

- merchant not eligible
- dashboard not enabled
- feature unavailable in environment

<br />
