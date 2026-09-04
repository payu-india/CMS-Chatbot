---
title: Partner Payments Integration
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: ''
  description: ''
  robots: index
---
# Partner Payments Overview

Partner Payments API enables partners to integrate payment collection capabilities for their merchants and end-customers using PayU's secure, PCI-compliant payment infrastructure. You can choose from multiple integration methods based on your use case—hosted checkout for multi-method payments, UPI Intent for seamless mobile UPI flows, or UPI TPV for regulatory-compliant beneficiary account verification.

## Available Integration Methods

PayU offers three integration methods for Partner Payments, each optimized for specific payment scenarios:

### 1. Hosted Checkout Integration

Redirect customers to PayU's secure, fully-hosted checkout page that supports multiple payment methods—cards, UPI, net banking, and wallets—in a single integration.

**Best for:**

- E-commerce platforms managing payments for multiple merchants
- Subscription services requiring recurring payments
- B2B platforms and marketplaces
- Partners who want zero maintenance and automatic payment method updates

**Key Features:**

- Multi-method payment support in one flow
- PCI-DSS compliance — PayU handles all card data
- Proven, optimized checkout UI for higher conversion
- Customizable branding (logo, colors)
- Built-in webhook notifications and payment verification

**Integration Flow:** Create payment session via API → Receive `redirectUri` → Redirect customer to PayU → Customer completes payment → Webhook + callback URL → Verify payment

**[View Hosted Checkout Integration Guide →](ref:hosted-checkout-api-partner-integration)**

***

### 2. UPI Intent Integration

Server-to-server (S2S) UPI flow that directly invokes UPI apps on the customer's mobile device for a seamless, native payment experience.

**Best for:**

- Mobile-first applications with high UPI payment volume
- Quick checkout flows for ride-hailing, food delivery, e-commerce apps
- In-app purchases requiring frictionless payment experiences
- QR code alternatives for merchant-initiated UPI flows

**Key Features:**

- Native mobile experience with direct UPI app invocation
- Faster checkout — no form filling, no card details entry
- Returns `intentURIData` (UPI deep link) with pre-filled payment parameters
- Higher success rates due to reduced friction
- Real-time confirmation via webhooks

**Integration Flow:** Initiate payment with `txn_s2s_flow=4` → Receive `intentURIData` → Launch customer's UPI app → Customer authenticates with UPI PIN → Webhook + payment verification

**[View UPI Intent Integration Guide →](ref:upi-s2s-partner-integration-api)**

***

### 3. UPI TPV (Third-Party Verification) Integration

UPI flow with beneficiary account validation to ensure payments originate from a specific verified bank account, meeting regulatory and compliance requirements.

**Best for:**

- Loan repayments and EMI collections from borrower's registered account
- Vendor payments requiring verified business account
- Refund collections to original payment account
- Compliance-heavy industries (NBFC, lending, insurance, government payments)

**Key Features:**

- Account validation — ensures payment comes from authorized beneficiary account
- Regulatory compliance for KYC and anti-money laundering requirements
- Fraud prevention by blocking unauthorized account payments
- Complete audit trail of account-level transaction details
- Secure S2S flow with direct UPI app invocation

**Integration Flow:** Initiate payment with `txn_s2s_flow=4` + `beneficiarydetail` → PayU validates account → `intentURIData` returned → Customer's UPI app opens → Account verification → Payment with `bankcode=INTTPV` → Webhook + verification

**[View UPI TPV Integration Guide →](doc:partner-payments-upi-tpv-integration)**

***

## Payments Journey

The following sample screenshots illustrate the payment journey when partners integrate with WhatsApp using Partner Payments API:


<Image src="https://files.readme.io/ed4f484-image.png" align="center" border={true} />


***

## Prerequisites

Before integrating any Partner Payments method, ensure you have:

<Note>
**Required OAuth Scopes:**
- `create_payment_links`
- `partner_payment_links`
- `partner_payments`
</Note>

### General Requirements

- **Active PayU Partner Account** with Partner Payments API access
- **Partner OAuth Application** registered with PayU (with required scopes enabled)
- **OAuth Credentials:** `client_id` and `client_secret`
- **Merchant Credentials:** `merchant_id` (PayU merchant ID) and `reseller_id` (partner UUID)
- **Test Environment Access** to UAT endpoints (`https://test-partnerapilayer.payu.in`)

### Callback and Webhook URLs

All integration methods require:

- **Callback URLs** (Hosted Checkout only): `surl` (success), `furl` (failure), `curl` (cancel)
- **Partner Webhook URLs** configured in PayU: `partner_webhook_success`, `partner_webhook_failure`, `partner_webhook_cancelled`

### Integration-Specific Requirements

**For UPI Intent and UPI TPV (S2S flows):**

- S2S flow enabled (`txn_s2s_flow=4`) on your account
- Ability to capture customer IP address (`s2s_client_ip`) and device user-agent (`s2s_device_info`)

**For UPI TPV only:**

- UPI TPV feature enabled on your PayU account (contact PayU support)
- Beneficiary account details: IFSC code, account number, account holder name

<Warning>
**Critical Hash Computation Rule:**
All Partner Payments integrations use OAuth `client_secret` for hash generation, NOT merchant salt.
</Warning>

***

## Partner Payment Integration APIs

Explore the complete API documentation for each integration method:

### Authentication

- **[Getting Access Token](ref:getting-access-token)** — 3-step OAuth flow to obtain bearer token

### Payment Initiation

- **[Hosted Checkout Integration](ref:hosted-checkout-api-partner-integration)** — Multi-method payment via hosted page
- **[UPI Intent S2S Integration](ref:upi-s2s-partner-integration-api)** — Direct UPI app invocation
- **[UPI TPV Integration](doc:partner-payments-upi-tpv-integration)** — UPI with beneficiary account verification

### Payment Management

- **[Verify Payment API](doc:verify-payment-api)** — Confirm final transaction status and reconcile webhooks
- **[Refund Transaction API](ref:refund-transaction-api-partner-integration)** — Initiate refunds for partner payments
- **[Partner Refund Status API](ref:refund-status-api-partner-integration)** — Check refund transaction status

***

## Next Steps

1. **Choose your integration method** based on your use case (Hosted Checkout, UPI Intent, or UPI TPV)
2. **Review the integration guide** for your chosen method
3. **Set up test environment** with OAuth credentials and test merchant account
4. **Complete the OAuth flow** to generate access tokens
5. **Test your integration** using the sandbox environment
6. **Refer to [Testing and Troubleshooting Guide](doc:testing-and-troubleshooting)** for common errors and solutions
7. **Go live** after successful UAT and production credential updates

***

## Support

For technical support or to enable specific features (UPI TPV, S2S flow, etc.), contact PayU Partner Support with:

- Your `reseller_id` (partner UUID)
- Merchant ID(s) involved
- Integration method(s) you're implementing
- Detailed description of your use case or issue
