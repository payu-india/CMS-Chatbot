---
title: Partner Payment Links
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
Payment Links for Partners enables you to create secure, shareable payment URLs through PayU's Partner Payments API using OAuth 2.0 authentication. Generate payment links instantly and share them via SMS, WhatsApp, email, or any digital channel—customers can complete payments without navigating to your website or app.

Unlike direct merchant integrations, partner payment links are designed for resellers, aggregators, platforms, and service providers who manage payments on behalf of multiple merchants. All payment links use OAuth-based authentication with your partner credentials (`client_id`, `client_secret`, `reseller_id`) and support real-time webhook notifications for payment status updates.

**Three Integration Types Available:**

1. **Hosted Checkout** — Multi-payment method web-based checkout (cards, UPI, net banking, wallets)
2. **UPI Intent** — Direct UPI app invocation for instant mobile payments
3. **UPI TPV (Third-Party Verification)** — UPI payments with beneficiary account validation for compliance

Choose the integration type that matches your business model, customer experience requirements, and regulatory needs.

***

## How It Works

Payment Links for Partners follow a standardized OAuth-authenticated flow:

### 1. **Authenticate with OAuth 2.0**

Obtain an access token using your partner OAuth credentials with required scopes:

- `create_payment_links`
- `partner_payment_links`
- `partner_payments`

Your access token authenticates all API requests and ensures secure communication between your platform and PayU.

### 2. **Create Payment Link**

Call the Partner Payments API with transaction details:

- Transaction ID (`txnid`)
- Amount
- Product/service description
- Customer phone number
- Integration-specific parameters (hosted checkout callbacks OR UPI Intent S2S fields OR UPI TPV beneficiary details)
- SHA-512 hash computed with your OAuth `client_secret`

PayU returns a payment link URL (`redirectUri` for hosted checkout) or UPI intent data (`intentURIData` for UPI flows).

### 3. **Share Payment Link**

Distribute the payment link to your customer via:

- **SMS** — Quick payment links for invoices, bills, reminders
- **WhatsApp** — Commerce in chat, order confirmations
- **Email** — Professional invoices, payment requests
- **In-app/web** — Embedded links or QR codes

### 4. **Customer Completes Payment**

**Hosted Checkout:**

- Customer clicks the link → Redirected to PayU's hosted checkout page
- Selects payment method (card, UPI, net banking, wallet)
- Completes authentication (OTP, PIN, biometric)
- PayU redirects to your success/failure/cancel URL

**UPI Intent:**

- Customer opens the link on mobile → UPI app launches automatically
- Pre-filled payment details displayed in UPI app (Google Pay, PhonePe, BHIM, Paytm, etc.)
- Customer authenticates with UPI PIN
- Payment processed instantly

**UPI TPV:**

- Same as UPI Intent, but PayU validates the customer's UPI account against the beneficiary account details you provided
- Payment succeeds only if accounts match (ensures funds come from the authorized account)

### 5. **Receive Payment Notification**

PayU sends webhook notifications to your configured partner webhook URLs:

- `partner_webhook_success` — Payment succeeded
- `partner_webhook_failure` — Payment failed
- `partner_webhook_cancelled` — Customer cancelled

Always verify the webhook hash (SHA-512 reverse hash) before processing payment status updates.

### 6. **Verify Payment**

Call the Verify Payment API to confirm the final transaction status and reconcile:

- Provides authoritative payment status independent of webhooks
- Returns complete transaction details (PayU ID, status, amount, payment mode)
- Essential for reconciliation and dispute resolution

{/* diagram: Payment Links flow diagram showing OAuth → Create Link → Share → Customer Payment → Webhook → Verify Payment with icons for each step */}

***

## Customer Journey

### Hosted Checkout Flow

1. **Customer receives payment link** via SMS, email, or WhatsApp
   - Example: "Complete your payment for Order #12345: [https://secure.payu.in/\_payment](https://secure.payu.in/_payment)?..."

2. **Customer opens link** in browser (mobile or desktop)
   - Redirected to PayU's secure hosted checkout page
   - Transaction details displayed (merchant name, amount, product description)

3. **Customer selects payment method**
   - Credit/Debit Cards (Visa, Mastercard, Amex, Rupay)
   - UPI (Intent or VPA-based collect)
   - Net Banking (50+ banks supported)
   - Wallets (PayU Money, PhonePe, Paytm, etc.)

4. **Customer authenticates payment**
   - Card: CVV + OTP (3D Secure)
   - UPI: UPI PIN in app
   - Net Banking: Bank login credentials
   - Wallet: Wallet PIN/OTP

5. **Payment processed**
   - Success → Redirected to your success URL (`surl`)
   - Failure → Redirected to your failure URL (`furl`)
   - Cancel → Redirected to your cancel URL (`curl`)

6. **Customer sees confirmation**
   - Your custom success/failure page with order details and next steps

### UPI Intent Flow

1. **Customer receives payment link** via preferred channel
   - Example: "Pay ₹500 for your order: [https://secure.payu.in/\_payment](https://secure.payu.in/_payment)?..."

2. **Customer opens link on mobile device**
   - PayU detects mobile browser
   - Automatically invokes UPI Intent

3. **UPI app launcher appears**
   - System displays installed UPI apps (Google Pay, PhonePe, BHIM, Paytm, etc.)
   - Customer selects their preferred UPI app

4. **UPI app opens with pre-filled details**
   - Merchant VPA (e.g., payu\@axisbank)
   - Amount (₹500.00)
   - Transaction reference
   - Product description

5. **Customer authenticates with UPI PIN**
   - One-time PIN entry
   - Payment processed in real-time

6. **Instant confirmation**
   - Success/failure shown in UPI app
   - Customer returns to merchant app/website

### UPI TPV Flow

1. **Partner provides beneficiary account details during link creation**
   - IFSC code
   - Account number
   - Account holder name

2. **Customer receives and opens payment link**
   - Same as UPI Intent flow above

3. **UPI app launches with account validation**
   - PayU validates customer's UPI account against beneficiary details
   - Payment proceeds only if accounts match

4. **Customer authenticates with UPI PIN**
   - If account matches → Payment processed
   - If account mismatch → Payment rejected with error message

5. **Secure payment confirmation**
   - Ensures funds originated from the authorized account
   - Webhook includes TPV indicators (`bankcode: "INTTPV"`)

{/* diagram: Customer journey flowchart showing three parallel flows (Hosted, UPI Intent, UPI TPV) from link receipt to payment confirmation */}

***

## Features of Payment Links for Partners

### OAuth 2.0 Authentication

- Secure partner-level authentication using industry-standard OAuth 2.0
- Granular scope-based access control (`create_payment_links`, `partner_payment_links`, `partner_payments`)
- Automatic token refresh and expiry handling
- No exposure of merchant credentials to end customers

### Multi-Integration Support

- **Hosted Checkout** — Web-based payment gateway for all payment methods
- **UPI Intent** — Native mobile UPI app invocation for instant payments
- **UPI TPV** — UPI with beneficiary account verification for compliance

### Flexible Payment Methods (Hosted Checkout)

- **Cards:** Visa, Mastercard, Amex, Rupay (credit, debit, prepaid)
- **UPI:** All major UPI apps (Google Pay, PhonePe, BHIM, Paytm, Amazon Pay, etc.)
- **Net Banking:** 50+ banks including ICICI, HDFC, SBI, Axis, Kotak
- **Wallets:** PayU Money, PhonePe, Paytm, Freecharge, Mobikwik

### Real-Time Webhook Notifications

- Instant payment status updates via server-to-server webhooks
- Separate webhook URLs for success, failure, and cancellation events
- SHA-512 hash verification for webhook authenticity
- Retry mechanism for failed webhook deliveries
- Complete transaction payload (PayU ID, status, amount, mode, bank code)

### Payment Verification API

- Independent verification endpoint to confirm transaction status
- Useful for reconciliation and dispute resolution
- Returns authoritative payment status regardless of webhook delivery
- Supports bulk verification for transaction batches

### Security & Compliance

- PCI-DSS Level 1 certified hosted checkout
- SHA-512 hash-based request authentication
- Client_secret-based hash computation (never exposed to customers)
- Webhook hash verification (reverse hash with 5-pipe sequence)
- HTTPS-only communication
- Beneficiary account validation (UPI TPV)

### Partner-Friendly Features

- Single OAuth integration for multiple merchants
- Partner-specific webhook URLs (separate from merchant webhooks)
- Reseller ID tracking for multi-tenant platforms
- User-defined fields (udf1-udf5) for custom metadata
- Transaction-level merchant_id for routing payments to specific merchants

### Developer Experience

- RESTful JSON API
- Comprehensive code examples (Python, Java, PHP, cURL)
- Detailed error messages with resolution guidance
- Test environment with sandbox credentials
- Real-time status updates via webhooks

{/* diagram: Features overview infographic showing OAuth, Payment Methods, Webhooks, Security, and Partner Tools icons */}

***

## Benefits of Payment Links for Partners

### For Partners/Resellers

**Rapid Integration**

- Single OAuth integration supports multiple merchants under your platform
- No need to integrate separately for each merchant
- Reusable authentication flow across all payment link types

**Operational Efficiency**

- Generate payment links on-demand via API
- No manual payment collection or reconciliation
- Automated webhook notifications reduce manual status checks

**Revenue Opportunities**

- Offer payment solutions as a service to your merchant clients
- White-label payment link generation
- Value-added services (invoicing, reminders, collections)

**Control & Visibility**

- Partner-level dashboards for transaction monitoring
- Reseller ID tracking for merchant-wise reporting
- Custom webhook handlers for business logic

**Compliance Made Easy**

- UPI TPV for regulatory requirements (loan repayments, vendor payments)
- PCI-compliant hosted checkout (no card data handling required)
- Audit trails via transaction logs and verification API

### For Merchants (Your Clients)

**Faster Time to Market**

- Accept payments immediately without lengthy integration cycles
- No technical team required
- Partner handles all API complexity

**Broader Payment Acceptance**

- Support all major payment methods (cards, UPI, net banking, wallets)
- No need to integrate with multiple payment gateways
- Automatic access to new payment methods as PayU adds them

**Improved Cash Flow**

- Instant payment link generation for invoices
- Real-time payment confirmation
- Faster settlement cycles

**Better Customer Experience**

- Mobile-optimized checkout (hosted & UPI)
- One-click UPI payments (Intent flow)
- Secure PCI-compliant payment pages

### For End Customers

**Convenience**

- Pay via preferred method (cards, UPI, net banking, wallets)
- No app download or registration required (hosted checkout)
- Pre-filled payment details (UPI Intent/TPV)

**Speed**

- One-click UPI payments with PIN authentication
- No form filling or manual data entry
- Instant payment confirmation

**Security**

- PCI-DSS certified payment pages
- 3D Secure authentication for cards
- UPI PIN-based authorization
- HTTPS encryption for all transactions

**Trust**

- PayU-branded checkout (established payment gateway)
- Transparent transaction details before payment
- Clear success/failure confirmations

{/* diagram: Benefits matrix showing Partner Benefits, Merchant Benefits, and Customer Benefits in three columns */}

***

## Next Steps

Choose the integration type that best fits your business needs:

### 🌐 Hosted Checkout — Multi-Method Web Payments

Best for: E-commerce platforms, invoicing systems, B2B payment collection

**When to use:**

- Customers need multiple payment method options
- Desktop/laptop payment scenarios
- Professional invoice payments
- Request-money use cases

**[Go to Hosted Checkout Integration Guide →](doc:payment-links-hosted-checkout)**

***

### 📱 UPI Intent — Instant Mobile Payments

Best for: Mobile-first apps, quick checkout, in-app purchases

**When to use:**

- Mobile-native payment experience required
- UPI is the primary payment method
- Instant payment confirmation needed
- Ride-hailing, food delivery, e-commerce apps

**[Go to UPI Intent Integration Guide →](doc:payment-links-upi-intent)**

***

### 🔐 UPI TPV — Verified Account Payments

Best for: Loan repayments, vendor payments, refund collections, compliance-heavy industries

**When to use:**

- Payment must originate from a specific verified account
- Regulatory compliance requires beneficiary validation
- Fraud prevention via account matching
- Loan EMI collections, vendor disbursements

**[Go to UPI TPV Integration Guide →](doc:payment-links-upi-tpv)**

***

### 📚 Additional Resources

- **[Partner Payments API Reference](#)** — Complete API documentation
- **[Webhook Configuration Guide](#)** — Advanced webhook handling
- **[OAuth Authentication Guide](#)** — Token management best practices
- **[Verify Payment API](#)** — Transaction verification reference
- **[Error Handling Guide](#)** — Common errors and resolutions

***

<Info>
**Need Help Choosing?**

| Requirement | Recommended Integration |
|-------------|------------------------|
| Multiple payment methods needed | **Hosted Checkout** |
| Mobile-only, UPI-first flow | **UPI Intent** |
| Account verification required | **UPI TPV** |
| Invoice payments (email/SMS) | **Hosted Checkout** or **UPI Intent** |
| Loan repayments/vendor payments | **UPI TPV** |
| E-commerce checkout | **Hosted Checkout** |
| In-app purchases | **UPI Intent** |
| Compliance/regulatory needs | **UPI TPV** |
</Info>

<Note>
**Prerequisites for All Integrations:**

Before you begin, ensure you have:
- Partner OAuth application registered with PayU
- OAuth credentials (`client_id`, `client_secret`)
- Required scopes enabled: `create_payment_links`, `partner_payment_links`, `partner_payments`
- Merchant credentials (`merchant_id`, `reseller_id`)
- Partner webhook URLs configured
- Test environment access

Contact your PayU integration team to set up your partner account.
</Note>

***

**Ready to integrate?** Select your preferred payment link type above and follow the step-by-step integration guide.