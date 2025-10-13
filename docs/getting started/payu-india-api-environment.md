---
title: PayU India API Environment
deprecated: false
hidden: true
metadata:
  robots: index
---
This section consolidates all environment details you need before integrating any PayU India API.

## Environment Types

PayU provides two primary environments:

* **Test Environment (Sandbox)**: For development, testing, and integration validation
* **Production Environment (Live)**: For processing real payments and transactions

<Callout icon="📘" theme="info">
  **Important:** Always use matching credentials and endpoints for your target environment.
</Callout>

## Payment APIs (Web Checkout & Hosted Checkout)

These APIs handle payment collection via redirect or embedded forms.

<PaymentAPIEnvironment />

#### Authentication

| Environment    | Credential Type          | How to Obtain                               |
| -------------- | ------------------------ | ------------------------------------------- |
| **Test**       | Test Merchant Key & Salt | Generate via [Test Credentials Guide](#)    |
| **Production** | Live Merchant Key & Salt | Available after KYC completion in Dashboard |

#### Quick Code Examples

```

// Test Environment
const endpoint = 'https://test.payu.in/_payment';
const key      = 'YOUR_TEST_KEY';
const salt     = 'YOUR_TEST_SALT';

// Production Environment
const endpoint = 'https://secure.payu.in/_payment';
const key      = 'YOUR_LIVE_KEY';
const salt     = 'YOUR_LIVE_SALT';

```

***

### General APIs

These APIs support transaction verification, settlements, BIN and health check.

<GENERALAPIsEnvironment />

#### Authentication

| Environment    | Credential Type          | How to Obtain                               |
| -------------- | ------------------------ | ------------------------------------------- |
| **Test**       | Test Merchant Key & Salt | Generate via [Test Credentials Guide](#)    |
| **Production** | Live Merchant Key & Salt | Available after KYC completion in Dashboard |

### Payouts APIs

<PAYOUTSEnvironment />

#### Authentication

| Environment    | Method           | Credential Setup                            |
| -------------- | ---------------- | ------------------------------------------- |
| **Test**       | API Key + Secret | Register at `uat-onepayuonboarding.payu.in` |
| **Production** | API Key + Secret | Obtain from live Dashboard after KYC        |

***

## Configuration by Integration Type

### Hosted Checkout Integration

* **Test**: `https://test.payu.in/_payment` + Test Key/Salt
* **Production**: `https://secure.payu.in/_payment` + Live Key/Salt

### Merchant Hosted Checkout

* **Test**: `https://test.payu.in/_payment` + Test Key/Salt
* **Production**: `https://secure.payu.in/_payment` + Live Key/Salt

### Payment Links API

* **Test**: `https://test.payu.in/` + Test API Key/Secret
* **Production**: `https://secure.payu.in/` + Live API Key/Secret

### Payouts Integration

* **Test**: `https://uat-payouts.payu.in/` + Test Account Credentials
* **Production**: `https://payouts.payu.in/` + Live Account Credentials

### Mobile SDK Integration

* **Test**: Configure SDK with test endpoints & credentials
* **Production**: Configure SDK with production endpoints & credentials

***

## Troubleshooting Environment Issues

### Common Misconfigurations

```

// ❌ Mismatched Environment
const endpoint = 'https://secure.payu.in/_payment';
const key      = 'TEST_MERCHANT_KEY';

```

```

// ✅ Correct Test Setup
const endpoint = 'https://test.payu.in/_payment';
const key      = 'TEST_MERCHANT_KEY';

```

### Validation Checklist

* Endpoint URL matches environment
* Credentials match environment
* Hash salt corresponds to environment
* Webhook URLs are correct for target environment
* Dashboard access aligns with environment

### Error Indicators

| Error Message           | Likely Cause              | Solution                                |
| ----------------------- | ------------------------- | --------------------------------------- |
| “Invalid merchant key”  | Credential mismatch       | Verify key matches endpoint environment |
| “Authentication failed” | Wrong endpoint/credential | Check environment consistency           |
| “Hash mismatch”         | Incorrect salt            | Use environment-appropriate salt        |

***

## Migrating from Test to Production

### Pre-Migration Checklist

1. Complete KYC for live access
2. Generate production Key & Salt in Dashboard
3. Update all test URLs to production equivalents
4. Update webhook URLs to live endpoints
5. Verify with a small live transaction

### Migration Steps

1. **Code Updates**

```

- const baseURL = 'https://test.payu.in/_payment';
+ const baseURL = 'https://secure.payu.in/_payment';
- const merchantKey = 'TEST_KEY';
+ const merchantKey = 'LIVE_KEY';

```

2. **Config Updates**

* Environment variables
* Database settings
* Webhook registrations
* Dashboard callbacks

3. **Validation**

* Process a small transaction
* Confirm webhook delivery
* Verify transaction in live Dashboard
