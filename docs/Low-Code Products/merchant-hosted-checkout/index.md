---
title: Merchant Hosted Checkout
excerpt: >-
  Build a fully custom payment form on your website and post payment data
  directly to PayU. You own the UI, the flow, and the customer experience.
deprecated: false
hidden: true
updatedAt: "2026-11-05T00:00:00.000Z"
metadata:
  title: Merchant Hosted Checkout — Overview | PayU Developer Docs
  description: >-
    PayU Merchant Hosted Checkout: build your own payment form, collect payment
    details directly, and post to PayU's _payment API. Full UI control,
    PCI-DSS required for card handling. Supports cards, UPI, net banking,
    wallets, EMI, BNPL, Apple Pay, Flipkart SuperCoins, Rewards SPLITPAY,
    and Closed-Loop Wallet.
  keywords:
    - payu merchant hosted checkout integration
    - payu custom checkout build your own payment form
    - payu seamless integration cards upi net banking
    - payu _payment api merchant hosted
    - payu pci-dss merchant checkout india
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Banner
  isInline={true}
  message="Integration effort: Developer required"
  color="#E9A23B"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

## How Does Merchant Hosted Checkout Simplify My Business?

<Accordion title="Complete control over the payment UI and customer experience">

You design and build the entire payment form. PayU does not include any UI elements into your page. Card number fields, UPI input, net banking dropdowns, wallet selectors, all built by you, styled to match your brand, integrated into your existing checkout flow.

</Accordion>

<Accordion title="One API, all payment methods">

A single endpoint:`POST https://secure.payu.in/_payment` accepts payments across all methods. The payment method is determined by the `pg` and `bankcode` parameters you send. Cards, UPI, Net Banking, Wallets, EMI, and BNPL all use the same endpoint with different parameter sets.

</Accordion>

<Accordion title="Seamless payment flow — no bank redirect unless required">

For most payment methods, the customer never leaves your website until the bank's 3DS or authentication page opens. After authentication completes, the customer is redirected back to your `surl` or `furl`. You control what they see at every point before and after.

</Accordion>

<Accordion title="PCI-DSS scope: Card data handled by you">

Because your website collects raw card numbers and CVV directly from the customer, your servers and infrastructure are in scope for PCI-DSS. If you store, process, or transmit cardholder data, you must complete the [PCI-DSS Self-Assessment Questionnaire A-EP](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf).

PCI-DSS scope applies only to card payment methods and not for wallets and UPI. 

</Accordion>

<Accordion title="Per-method integration: Each payment type has specific parameters">

Unlike PayU Hosted Checkout or Checkout Plus where a single form handles all payment methods, Merchant Hosted Checkout requires a separate integration for each payment method. Cards, net banking, UPI collect, UPI intent, wallets, EMI, and BNPL each have their own required parameters and flows.

</Accordion>

***

## Is Merchant Hosted Checkout Right for Me?

| I want to… | Works? |
|---|---|
| Full design control over every field and step of the payment UI | ✅ |
| Custom-branded checkout without PayU UI on my page | ✅ |
| Cards, UPI, net banking, wallets, EMI, and BNPL from one endpoint | ✅ |
| Accept card payments (PCI-DSS compliance acceptable) | ✅ |
| A prebuilt PayU-branded payment page with minimal code | ⚠️ Use [PayU Hosted Checkout](../prebuilt-checkout-payu-hosted) instead |
| Payment modal that opens on my website without redirect | ⚠️ Use [Checkout Plus](../checkout-plus-integration) instead |
| Accept payments without a website or technical setup | ⚠️ Use [Payment Links](../../introduction-no-code-payments-integration/payment-links-dashboard) instead |
| Accept payments natively in a mobile app | ⚠️ Use [PayU Mobile SDK](../../mobile-sdks) instead |

<Callout icon="🤔" theme="info">
  **Not sure which solution fits?** See [Start Here](https://docs.payu.in/docs/start-here) for a guided comparison of all PayU integration options.
</Callout>

***

## Supported Payment Methods

Merchant Hosted Checkout supports the following payment methods. Each method requires a separate integration with its own parameters. You should use the `pg` and `bankcode` values to identify the correct method in your POST request. Refer to the respective document for more information.

| Payment Method | Guide |
|---|---|
| Credit / Debit / Prepaid Cards | [Cards](./integration-guide/build-integration/cards) |
| Net Banking | `NB` | Bank-specific code (e.g. `HDFCB`, `ICICI`) | [Net Banking](./integration-guide/build-integration/net-banking) |
| UPI Collect | [UPI](./integration-guide/build-integration/upi) |
| UPI TPV (Mutual Funds / Stock Broking) | [UPI TPV](./integration-guide/build-integration/upi-tpv) |
| PayTM, PhonePe, Amazon Pay & other wallets | [Wallets](./integration-guide/build-integration/wallets) |
| Advantage Club Wallet | [Wallets](./integration-guide/build-integration/wallets) |
| Credit Card EMI | [EMI](./integration-guide/build-integration/emi) |
| Debit Card EMI | [EMI](./integration-guide/build-integration/emi) |
| Cardless / BNPL EMI | [EMI](./integration-guide/build-integration/emi) |
| Buy Now Pay Later (BNPL) | [BNPL](./integration-guide/build-integration/bnpl) |
| Apple Pay | [Apple Pay](./integration-guide/build-integration/apple-pay) |
| Flipkart SuperCoins | [Flipkart SuperCoins](./integration-guide/build-integration/flipkart-supercoins) |
| Rewards SPLITPAY (TWID / Zillion) | [Rewards SPLITPAY](./integration-guide/build-integration/rewards-splitpay) |
| Closed-Loop Wallet (CLW) | [Closed-Loop Wallet](./integration-guide/build-integration/closed-loop-wallet) |
| PayPal | [Other Methods](./integration-guide/build-integration/other-methods) |
| Pluxee (Sodexo) Card | [Other Methods](./integration-guide/build-integration/other-methods) |
| EFTNET (NEFT/RTGS) | [Other Methods](./integration-guide/build-integration/other-methods) |

<Callout icon="📘" theme="info">
  Not all payment methods are enabled by default. Some methods including Apple Pay, Flipkart SuperCoins, Rewards SPLITPAY, and Closed-Loop Wallet require explicit activation by your PayU account manager. Check with your key account manager before building an integration for these methods.
</Callout>

***

## Common Use Cases

<Cards columns={3}>
  <Card title="E-commerce with Custom Checkout">
    Full-brand checkout where card fields, UPI input, and net banking selectors match your site's design without any redirects until bank authentication.
  </Card>
  <Card title="Financial Services and Lending">
    Loan repayments, insurance premiums, and investment platforms that need tight integration with their own KYC and account management flows.
  </Card>
  <Card title="Enterprise B2B Payments">
    Invoice payments via net banking or NEFT/RTGS with full control over the payer experience and post-payment workflow.
  </Card>
  <Card title="Travel and Hospitality">
    Booking platforms that need EMI on cards and specific bank offers surfaced directly in the payment UI, not in a third-party modal.
  </Card>
  <Card title="EdTech and Healthcare">
    Fee collection platforms that need branded, accessible payment flows with UPI and wallet support tailored to their user base.
  </Card>
</Cards>

***

## What Do I Need to Get Started?

Before you integrate, make sure you have:

- A **PayU merchant account:** [Register here](https://onboarding.payu.in/) if you don't have one.
- Your **test merchant key and salt:** From **PayU Dashboard** → **Developer** → **API Keys** in the test mode.
- Your **live merchant key and salt:** From **PayU Dashboard** → **Developer** → **API Keys** in the live mode
- A **backend server:** To generate SHA-512 hashes and post payment requests to PayU's `_payment` API.
- An **HTTPS-enabled website:** Required for all production card integrations.
- **PCI-DSS compliance:** If you are collecting card numbers and CVV on your website. Complete the [SAQ A-EP form](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf).
- **Publicly reachable `surl` and `furl` callback URLs** over HTTPS.

<HTMLBlock>{`
                <style>
                .tooltip-btn {
                    position: relative;
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-weight: bold; /* Added this line */
                }
                .tooltip-btn:hover::after {
                    content: attr(data-tooltip);
                    position: absolute;
                    bottom: 125%;
                    left: 50%;
                    transform: translateX(-50%);
                    background-color: #333;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 4px;
                    white-space: nowrap;
                    font-size: 12px;
                    z-index: 1;
                }
                </style>

                <button onclick="window.open('https://docs.payu.in/docs/payu-hosted-checkout-quick-start', '_blank')" 
                        class="tooltip-btn" 
                        data-tooltip="Follow the guided steps to set up and test your first payment.">
                    Set Up and Test Your First Payment →
                </button>
`}</HTMLBlock>

***

## Is My Integration Secure?

Merchant Hosted Checkout places significant security responsibility on you as your website handles raw payment data directly.<br/>

**Hash generation is always server-side.** Your backend generates the SHA-512 hash using your merchant salt. The salt must never appear in any frontend code, HTML, or client-accessible endpoint.

**PCI-DSS is required for card integrations.** If your website collects card numbers and CVV, your servers are in PCI-DSS scope. Ensure HTTPS on all pages, never store CVV, and complete the SAQ A-EP assessment.

**Verify every payment server-side.** The `surl`/`furl` callback can be replayed or tampered with. Always verify the response hash and call the [Verify Payment API](https://docs.payu.in/reference/verify_payment_api) before fulfilling any order.

**Implement reverse hash verification.** For every response received at `surl`/`furl`, recompute the hash using the reverse formula and compare it to the `hash` field in the response. Reject any response where they don't match.

***

## How Does My Customer Pay?

<Accordion title="1. Customer fills your payment form">

Your website presents the payment form you built. The customer enters their payment details such as card number, UPI VPA, or selects their bank directly on your page.

</Accordion>

<Accordion title="2. Your backend generates the hash and posts to PayU">

Your server generates the transaction hash and submits a form POST to `https://secure.payu.in/_payment` with the payment parameters and hash. PayU receives and validates the request.

</Accordion>

<Accordion title="3. Bank authentication (if required)">

For card payments, PayU redirects the customer to the issuing bank's 3DS authentication page. For net banking, the customer is redirected to their bank's login page. For UPI intent, the customer's UPI app opens. For wallets, PayU handles the redirect.

</Accordion>

<Accordion title="4. Customer returns and your server handles the callback">

After authentication, the customer is redirected to your `surl` or `furl`. PayU POSTs the transaction response to that URL. Your server verifies the response hash and calls the Verify Payment API before updating the order state

</Accordion>

***

## What Happens After a Payment

After the customer completes a payment:

  - PayU determines the transaction result.
  - PayU redirects the customer to your surl if the payment succeeds, or to your furl if it fails.
  - PayU posts the payment response to that URL, including `mihpayid`, `status`, `txnid`, `amount`, `hash`, `error`, and `error_Message`.

<Callout icon="💬" theme="warn">
  **Important**

  Do not treat the browser redirect alone as confirmation that a payment succeeded. Check the reverse hash on the response, then confirm the transaction with the Verify Payment API before you fulfil the order. If the callback does not arrive, use webhooks and confirm the status on your server.

  Learn how to verify the response and confirm the payment in the Integration Guide.
</Callout>

## What If My Customer Wants the Money Back?

<Tabs>
  <Tab title="Refunds">
    Use PayU refunds to initiate. Issue a partial or full refund to a customer directly from the Dashboard or via the Refunds API
  </Tab>

  <Tab title="Settlements">
    You are waiting for the amount to reach your account. PayU settlements can help you find out when the amount will be settled.
  </Tab>

  <Tab title="Disputes and Chargebacks">
    Respond to customer disputes and chargebacks raised through their bank — track status and submit evidence from the Dashboard.
  </Tab>
</Tabs>

***

## Use AI to Help You

Use an AI coding assistant with the PayU Developer MCP to search these docs, scaffold your payment form, generate hash code in any language, and debug callback issues without leaving your editor.

<Callout icon="💬" theme="info">
  **Example prompts for AI coding assistants**

  - "How do I generate a SHA-512 hash for PayU Merchant Hosted Checkout in Node.js?"
  - "What parameters do I need for a PayU cards seamless integration?"
  - "How do I validate a UPI VPA before posting to PayU _payment?"
  - "What is the reverse hash formula for PayU Merchant Hosted Checkout callback verification?"
  - "How do I handle surl and furl callbacks for PayU seamless integration?"
  - "What is the difference between PayU Hosted Checkout and Merchant Hosted Checkout?"
</Callout>

<Cards columns={2}>
  <Card title="PayU Developer MCP" href="doc:payu-devguide-builder-mcp-configuration">
    Add the PayU docs MCP to Cursor, VS Code, or Claude Desktop. Search documentation and fetch integration code directly from your AI assistant.
  </Card>
  <Card title="Integration Lab" href="https://www.payu.in/integrationlab/">
    Test individual payment method flows end-to-end and generate integration code without writing it from scratch.
  </Card>
</Cards>

***

## Next Steps

<Cards columns={2}>
  <Card title="How It Works" icon="fa-diagram-project" href="./how-it-works">
    Architecture, the _payment API flow, PCI-DSS scope, and how MHC differs from other PayU products.
  </Card>
  <Card title="Quick Start" icon="fa-play" href="./quick-start">
    Make your first test card payment in minutes — hash generation, form POST, and callback handling.
  </Card>
  <Card title="APIs" icon="fa-rectangle-api" href="./merchant-hosted-checkout-apis">
    API reference index for _payment, Verify Payment, and transaction management.
  </Card>
</Cards>
