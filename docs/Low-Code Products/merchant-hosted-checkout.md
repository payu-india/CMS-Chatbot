---
title: Merchant Hosted Checkout
excerpt: >-
  Build a fully custom payment form on your website and post payment data
  directly to PayU. You own the UI, the flow, and the customer experience.
deprecated: false
hidden: true
metadata:
  title: Merchant Hosted Checkout — Overview | PayU Developer Docs
  description: >-
    PayU Merchant Hosted Checkout: build your own payment form, collect card and
    payment details directly, and post to PayU's _payment API. Full UI control,
    PCI-DSS required for card handling, supports cards, UPI, netbanking,
    wallets, EMI, and BNPL.
  keywords:
    - payu merchant hosted checkout integration
    - payu custom checkout build your own payment form
    - payu seamless integration cards upi net banking
    - payu _payment api merchant hosted
    - payu pci-dss merchant checkout india
  robots: index
next:
  description: Explore related information and resources.
---
<Banner
  isInline={true}
  message="Integration effort: Developer required"
  color="#E9A23B"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

***

## What Can I Build with Merchant Hosted Checkout?

<Accordion title="Complete control over the payment UI and customer experience" icon="fa-paintbrush">
  You design and build the entire payment form. PayU does not inject any UI elements into your page. Card number fields, UPI input, net banking dropdowns, wallet selectors — all built by you, styled to match your brand, integrated into your existing checkout flow.

  No redirect. No modal. No PayU-branded page anywhere in the customer journey.
</Accordion>

<Accordion title="One API, all payment methods" icon="fa-credit-card">
  A single endpoint — `POST https://secure.payu.in/_payment` — accepts payments across all methods. The payment method is determined by the `pg` and `bankcode` parameters you send. Cards, UPI, Net Banking, Wallets, EMI, and BNPL all use the same endpoint with different parameter sets.
</Accordion>

<Accordion title="Seamless payment flow — no bank redirect unless required" icon="fa-arrow-right-arrow-left">
  For most payment methods, the customer never leaves your website until the bank's 3DS or authentication page opens. After authentication completes, the customer is redirected back to your `surl` or `furl`. You control what they see at every point before and after.
</Accordion>

<Accordion title="PCI-DSS scope — card data handled by you" icon="fa-shield-halved">
  Because your website collects raw card numbers and CVV directly from the customer, your servers and infrastructure are in scope for PCI-DSS. If you store, process, or transmit cardholder data, you must complete the [PCI-DSS Self-Assessment Questionnaire A-EP](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf).

  For wallets and UPI, card data is not collected — PCI-DSS scope applies only to card payment methods.
</Accordion>

<Accordion title="Per-method integration — each payment type has specific parameters" icon="fa-list-check">
  Unlike PayU Hosted Checkout or Checkout Plus where a single form handles all payment methods, Merchant Hosted Checkout requires a separate integration for each payment method. Cards, net banking, UPI collect, UPI intent, wallets, EMI, and BNPL each have their own required parameters and flows.
</Accordion>

***

## Is Merchant Hosted Checkout Right for Me?

| I want to…                                                      |                                                  Works?                                                 |
| --------------------------------------------------------------- | :-----------------------------------------------------------------------------------------------------: |
| Full design control over every field and step of the payment UI |                                                    ✅                                                    |
| Custom-branded checkout — zero PayU UI on my page               |                                                    ✅                                                    |
| Cards, UPI, net banking, wallets, EMI, BNPL from one endpoint   |                                                    ✅                                                    |
| Accept card payments (PCI-DSS compliance acceptable)            |                                                    ✅                                                    |
| A prebuilt PayU-branded payment page with minimal code          |                 ⚠️ Use [PayU Hosted Checkout](../prebuilt-checkout-payu-hosted) instead                 |
| Payment modal that opens on my website without redirect         |                       ⚠️ Use [Checkout Plus](../checkout-plus-integration) instead                      |
| Accept payments without a website or technical setup            | ⚠️ Use [Payment Links](../../introduction-no-code-payments-integration/payment-links-dashboard) instead |
| Accept payments natively in a mobile app                        |                           ⚠️ Use [PayU Mobile SDK](../../mobile-sdks) instead                           |

<Callout icon="🤔" theme="info">
  **Not sure which solution fits?** See [Start Here](https://docs.payu.in/docs/start-here) for a guided comparison of all PayU integration options.
</Callout>

***

## Common Use Cases

<Cards columns="3">
  <Card title="E-commerce with Custom Checkout" icon="fa-bag-shopping">
    Full-brand checkout where card fields, UPI input, and net banking selectors match your site's design — no redirects until bank authentication.
  </Card>

  <Card title="Financial Services & Lending" icon="fa-building-columns">
    Loan repayments, insurance premiums, and investment platforms that need tight integration with their own KYC and account management flows.
  </Card>

  <Card title="Enterprise B2B Payments" icon="fa-briefcase">
    Invoice payments via net banking or NEFT/RTGS with full control over the payer experience and post-payment workflow.
  </Card>

  <Card title="Travel & Hospitality" icon="fa-plane">
    Booking platforms that need EMI on cards and specific bank offers surfaced directly in the payment UI, not in a third-party modal.
  </Card>

  <Card title="EdTech & Healthcare" icon="fa-graduation-cap">
    Fee collection platforms that need branded, accessible payment flows with UPI and wallet support tailored to their user base.
  </Card>
</Cards>

***

## What Do I Need to Get Started?

Before you integrate, make sure you have:

- A **PayU merchant account**. [Register here](https://onboarding.payu.in/) if you don't have one.
- Your **test merchant key and salt** — from PayU Dashboard → Settings → Developer Settings → Test/Sandbox.
- Your **live merchant key and salt** — from PayU Dashboard → Settings → Developer Settings → Live/Production.
- A **backend server** to generate SHA-512 hashes and post payment requests to PayU's `_payment` API.
- An **HTTPS-enabled website** — required for all production card integrations.
- **PCI-DSS compliance** if you are collecting card numbers and CVV on your website. Complete the [SAQ A-EP form](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf).
- **Publicly reachable&#x20;**`surl`**&#x20;and&#x20;**`furl`**&#x20;callback URLs** over HTTPS.

***

## How Do I Integrate Merchant Hosted Checkout?

<Accordion title="Step 1: Choose your payment method" icon="fa-circle-1">
  Merchant Hosted Checkout requires a separate integration for each payment method. Start with the payment method your customers use most — Cards is the most common starting point.

  Each method uses the same `_payment` endpoint but with different `pg`, `bankcode`, and field parameters. See [Build Integration](./integration-guide/build-integration) for the per-method guides.
</Accordion>

<Accordion title="Step 2: Build your payment form" icon="fa-circle-2">
  Design and build the UI for your chosen payment method on your website. For cards, this means card number, CVV, expiry, and name fields. For net banking, a bank selector dropdown. For UPI, a VPA input or QR/intent flow.

  Your form collects payment details from the customer but does not submit them directly to PayU. The data goes to your backend first.
</Accordion>

<Accordion title="Step 3: Generate the hash on your backend" icon="fa-circle-3">
  Your backend generates the SHA-512 transaction hash using your merchant salt:

  ```
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
  ```

  The salt must never appear in frontend code. Only the computed hash is passed to the frontend or included in the form POST.
</Accordion>

<Accordion title="Step 4: POST to PayU's _payment endpoint" icon="fa-circle-4">
  Submit the payment parameters — including the hash and all payment-method-specific fields — as a form POST to PayU:

  | Environment | Endpoint                          |
  | ----------- | --------------------------------- |
  | Test        | `https://test.payu.in/_payment`   |
  | Production  | `https://secure.payu.in/_payment` |

  PayU processes the payment, handles bank authentication, and redirects the customer to your `surl` (success) or `furl` (failure).
</Accordion>

<Accordion title="Step 5: Handle the callback and verify server-side" icon="fa-circle-5">
  PayU POSTs the payment response to your `surl` or `furl`. Before marking any order as paid:

  1. Verify the response hash using the reverse hash formula
  2. Call the [Verify Payment API](https://docs.payu.in/reference/verify_payment_api) from your backend with the `txnid`
  3. Confirm `status === 'success'` and the `amount` matches your order

  Never trust the callback response alone — always verify server-side.
</Accordion>

<Callout icon="📘" theme="info">
  **Full implementation details** — all parameters, hash formula, code samples, and per-payment-method guides are in [Build Integration](./integration-guide/build-integration).
</Callout>

***

## Is My Integration Secure?

Merchant Hosted Checkout places significant security responsibility on you — more than Hosted Checkout or Checkout Plus — because your website handles raw payment data directly.

**Hash generation is always server-side.** Your backend generates the SHA-512 hash using your merchant salt. The salt must never appear in any frontend code, HTML, or client-accessible endpoint.

**PCI-DSS is required for card integrations.** If your website collects card numbers and CVV, your servers are in PCI-DSS scope. Ensure HTTPS on all pages, never store CVV, and complete the SAQ A-EP assessment.

**Verify every payment server-side.** The `surl`/`furl` callback can be replayed or tampered with. Always verify the response hash and call the Verify Payment API before fulfilling any order.

**Implement reverse hash verification.** For every response received at `surl`/`furl`, recompute the hash using the reverse formula and compare it to the `hash` field in the response. Reject any response where they don't match.

***

## How Does My Customer Pay?

<Accordion title="1. Customer fills your payment form" icon="fa-circle-1">
  Your website presents the payment form you built. The customer enters their payment details — card number, UPI VPA, or selects their bank — directly on your page.
</Accordion>

<Accordion title="2. Your backend generates the hash and posts to PayU" icon="fa-circle-2">
  Your server generates the transaction hash and submits a form POST to `https://secure.payu.in/_payment` with the payment parameters and hash. PayU receives and validates the request.
</Accordion>

<Accordion title="3. Bank authentication (if required)" icon="fa-circle-3">
  For card payments, PayU redirects the customer to the issuing bank's 3DS authentication page. For net banking, the customer is redirected to their bank's login page. For UPI intent, the customer's UPI app opens. For wallets, PayU handles the redirect.
</Accordion>

<Accordion title="4. Customer returns and your server handles the callback" icon="fa-circle-4">
  After authentication, the customer is redirected to your `surl` or `furl`. PayU POSTs the transaction response to that URL. Your server verifies the response hash and calls the Verify Payment API before updating the order state.
</Accordion>

***

## Post-Payment Actions

<Cards columns="2">
  <Card title="Refunds" href="https://docs.payu.in/docs/introduction-refunds" icon="fa-rotate-left">
    Initiate full or partial refunds from the PayU Dashboard or via the Refund API. Supports instant refunds for eligible transactions.
  </Card>

  <Card title="Refund APIs" href="https://docs.payu.in/docs/refund-apis-doc" icon="fa-rectangle-api">
    API reference for initiating refunds, checking refund status, and retrieving all refunds by transaction ID.
  </Card>

  <Card title="Settlements Dashboard" href="https://docs.payu.in/docs/settlements-dashboard" icon="fa-building-columns">
    View settlement records, download TDR reports, and track UTR details from the PayU Dashboard.
  </Card>

  <Card title="Webhooks" href="https://docs.payu.in/docs/webhooks" icon="fa-plug">
    Receive server-to-server payment and refund notifications. Use as a fallback when `surl`/`furl` callbacks fail.
  </Card>
</Cards>

***

## Use AI to Help You

Use an AI coding assistant with the PayU Developer MCP to search these docs, scaffold your payment form, generate hash code in any language, and debug callback issues — without leaving your editor.

<Callout icon="💬" theme="info">
  **Example prompts for AI coding assistants**

  - "How do I generate a SHA-512 hash for PayU Merchant Hosted Checkout in Node.js?"
  - "What parameters do I need for a PayU cards seamless integration?"
  - "How do I validate a UPI VPA before posting to PayU \_payment?"
  - "What is the reverse hash formula for PayU Merchant Hosted Checkout callback verification?"
  - "How do I handle surl and furl callbacks for PayU seamless integration?"
  - "What is the difference between PayU Hosted Checkout and Merchant Hosted Checkout?"
</Callout>

<Cards columns="2">
  <Card title="PayU Developer MCP" href="doc:payu-devguide-builder-mcp-configuration" icon="fa-server">
    Add the PayU docs MCP to Cursor, VS Code, or Claude Desktop. Search documentation and fetch integration code directly from your AI assistant.
  </Card>

  <Card title="Integration Lab" href="https://www.payu.in/integrationlab/" icon="fa-flask">
    Test individual payment method flows end-to-end and generate integration code without writing it from scratch.
  </Card>
</Cards>

***

## Next Steps

<Cards columns="2">
  <Card title="How It Works" href="./how-it-works" icon="fa-diagram-project">
    Architecture, the \_payment API flow, PCI-DSS scope, and how MHC differs from other PayU products.
  </Card>

  <Card title="Quick Start" href="./quick-start" icon="fa-play">
    Make your first test card payment in minutes — hash generation, form POST, and callback handling.
  </Card>

  <Card title="Build Integration" href="./integration-guide/build-integration" icon="fa-code">
    Per-method integration guides: Cards, Net Banking, UPI, Wallets, EMI, BNPL, and more.
  </Card>

  <Card title="APIs" href="./merchant-hosted-checkout-apis" icon="fa-rectangle-api">
    API reference index for \_payment, Verify Payment, and transaction management.
  </Card>
</Cards>