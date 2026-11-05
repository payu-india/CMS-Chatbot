---
title: Checkout Plus
excerpt: >-
  Open PayU's payment modal directly on your website. Customers pay without ever
  leaving your page. JavaScript SDK integration with server-side hash.
deprecated: false
hidden: true
metadata:
  robots: index
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

## How Does Checkout Plus Simplify My Business?

<Accordion title="Payment modal opens on your website">
  Checkout Plus opens PayU's payment experience as a modal on your website, served from PayU's infrastructure. The customer's browser stays on your page throughout the payment. The underlying payment engine is <Anchor target="_blank" href="https://docs.payu.in/docs/payu-hosted-checkout-1">PayU Hosted Checkout</Anchor>, presented inline through the Bolt JavaScript SDK.
</Accordion>

<Accordion title="Built-in retry keeps customers in the payment flow">
  If a payment fails at the bank or during <Glossary>3D Secure (3DS) Authentication</Glossary> the modal resets to the payment form automatically without cancelling the order or navigating away. The customer can select a different card or payment method and try again immediately, without restarting the checkout process from scratch.
</Accordion>

<Accordion title="Supports all major Indian payment methods">
  A single `bolt.launch()` call opens a checkout that supports Credit Cards, Debit Cards, UPI, Net Banking, Wallets, EMI, and BNPL. There are no separate integrations per payment type. Payment methods can be enabled, disabled, or pre-selected per transaction using optional parameters.
</Accordion>

<Accordion title="PCI-DSS scope handled by PayU">
  Payment details are entered inside the PayU-served modal. Your website and servers never receive or handle raw card data. PCI-DSS compliance for card data handling is PayU's responsibility, not yours.
</Accordion>

***

## Is Checkout Plus Right for Me?

| I want to…                                                        |                                                  Works?                                                 |
| ----------------------------------------------------------------- | :-----------------------------------------------------------------------------------------------------: |
| Customers complete payment on my website without being redirected |                                                    ✅                                                    |
| Cards, UPI, netbanking, wallets, EMI, and BNPL in one integration |                                                    ✅                                                    |
| Built-in payment retry without restarting the checkout            |                                                    ✅                                                    |
| PCI-DSS scope reduction                                           |                                                    ✅                                                    |
| Redirect customers to a PayU-hosted page instead (simpler, no JS) |                 ⚠️ Use [PayU Hosted Checkout](../prebuilt-checkout-payu-hosted) instead                 |
| Full design control over every element of the payment UI          |              ⚠️ Use [Merchant Hosted Checkout](../custom-checkout-merchant-hosted) instead              |
| Accept payments without a website or technical setup              | ⚠️ Use [Payment Links](../../introduction-no-code-payments-integration/payment-links-dashboard) instead |
| Accept payments natively inside a mobile app                      |                           ⚠️ Use [PayU Mobile SDK](../../mobile-sdks) instead                           |
| Open PayU checkout in a mobile app WebView                        |                    ⚠️ See [WebView Integration](./integrate/webview-for-mobile-apps)                    |

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution is Right For You?**

  Tell us what you want to achieve and how you plan to accept payments. We will recommend the best PayU solution that fits your needs.<br />

  <Anchor target="_blank" href="https://docs.payu.in/docs/start-here">Find the Right Product for You</Anchor> →
</Callout>

***

## Common Use Cases

<Cards columns="3">
  <Card title="E-commerce and Online Retail" icon="fa-bag-shopping">
    Keep customers on the product or cart page throughout payment. The modal opens without navigating away, reducing drop-off at checkout.
  </Card>

  <Card title="EdTech and Online Courses" icon="fa-graduation-cap">
    Collect course and certification fees without redirecting learners away from the platform. Supports all major payment methods including EMI for higher-value courses.
  </Card>

  <Card title="SaaS and Subscription Platforms" icon="fa-layer-group">
    In-context payment on the plan selection or checkout page. For recurring auto-debit after the initial payment, combine with [Recurring Payments](https://docs.payu.in/docs/recurring-payments).
  </Card>

  <Card title="Travel and Hospitality" icon="fa-plane">
    Booking payment while keeping the customer on the itinerary or reservation page. Built-in retry handles bank-side failures without losing the booking context.
  </Card>

  <Card title="Healthcare and Diagnostics" icon="fa-stethoscope">
    Consultation fees and test payments collected while patients remain on the portal. Supports wallets and UPI for low-friction, quick transactions.
  </Card>
</Cards>

***

## What Do I Need to Get Started?

Before you integrate, make sure you have:

- A <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signup">**PayU merchant account**</Anchor>
- [**PayU Hosted Checkout**](https://docs.payu.in/docs/payu-hosted-checkout-1) already integrated or ready to set up. Checkout Plus wraps it in a modal.
- Your **test merchant key and salt&#x20;**&#x69;n the test mode for sandbox testing from **PayU Dashboard** → **Developer** → **API Keys**.
- Your **live merchant key and salt&#x20;**&#x69;n the live mode for production from **PayU Dashboard** → **Developer** → **API Keys**.
- A **backend server** capable of generating a SHA-512 hash (Node.js, Python, PHP, Java, or any server-side language).
- A **JavaScript-enabled website**, the Bolt SDK requires a browser environment.
- An **HTTPS-enabled, publicly reachable callback endpoint** for `surl` and `furl`.

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

                <button onclick="window.open('https://docs.payu.in/docs/create-a-payment-link#how-do-i-create-a-payment-link', '_blank')" 
                        class="tooltip-btn" 
                        data-tooltip="Follow the guided steps to set up and test your first payment.">
                    Set Up and Test Your First Payment →
                </button>
`}</HTMLBlock>

***

## Is My Integration Secure?

Checkout Plus uses the same security model as PayU Hosted Checkout, with one important difference in how the hash reaches the browser.

- **Hash generation is always server-side:&#x20;**&#x59;our backend computes the SHA-512 hash using your merchant salt and returns only the computed hash to the frontend. The salt must never appear in JavaScript code, HTML source, or any client-facing output.
- **Card data is collected inside the PayU modal:** Payment details are entered directly on PayU's infrastructure. Your website and servers never receive or process raw card data.
- **Verify the response after payment:&#x20;**&#x57;hen `responseHandler()` fires with a `SUCCESS` status, verify the transaction from your backend using the [Verify Payment API](https://docs.payu.in/reference/verify_payment_api) before marking the order as paid. The `txnStatus` returned to the browser can be spoofed by a malicious user whereas server-side verification cannot.

***

## How Does My Customer Pay?

<Accordion title="1. Customer clicks Pay on your website" icon="fa-mouse-pointer">
  The customer reaches your checkout page and clicks your payment button. Your page triggers the payment initiation flow.
</Accordion>

<Accordion title="2. Your backend generates the hash and your page calls bolt.launch()" icon="fa-server">
  Your frontend requests the transaction hash from your backend. Once received, your page calls `bolt.launch(data, handlers)` with the payment parameters. The Bolt SDK loads the PayU payment modal on your page.
</Accordion>

<Accordion title="3. The payment modal opens on your website" icon="fa-window-restore">
  The PayU-hosted payment modal appears over your page. Your website remains in the background — there is no browser redirect. The customer sees the payment methods enabled on your account.
</Accordion>

<Accordion title="4. The customer selects a payment method and completes payment" icon="fa-credit-card">
  The customer selects card, UPI, netbanking, wallet, EMI, or BNPL, enters their details, and completes authentication — all inside the modal, entirely on PayU's infrastructure.

  If payment fails, the modal resets to the payment form automatically. The customer can retry with a different payment method without any action from your application.
</Accordion>

<Accordion title="5. The modal closes and responseHandler() is called" icon="fa-check-circle">
  After payment completes, fails, or is cancelled, the Bolt SDK closes the modal and calls your `responseHandler()` with the result. Your page updates based on the `txnStatus` — confirming the order, showing an error, or offering retry — without any browser navigation.
</Accordion>

***

## Post-Payment Actions

Once payments are live, two areas become relevant depending on your business:

**Refunds** — Initiate full or partial refunds from the PayU Dashboard or via the Refund API. PayU also supports instant refunds for eligible transactions.

**Settlements** — PayU settles collected funds to your registered bank account on a regular cycle. View settlement records, download TDR reports, and track UTR details from the Settlements Dashboard.

<Cards columns="2">
  <Card title="Refunds" href="https://docs.payu.in/docs/introduction-refunds" icon="fa-rotate-left">
    Initiate full or partial refunds from the PayU Dashboard or via the Refund API. Includes instant refunds, status tracking, and webhook notifications.
  </Card>

  <Card title="Refund APIs" href="https://docs.payu.in/docs/refund-apis-doc" icon="fa-rectangle-api">
    API reference for initiating refunds, checking refund status, and retrieving all refunds against a transaction ID.
  </Card>

  <Card title="Settlements Dashboard" href="https://docs.payu.in/docs/settlements-dashboard" icon="fa-building-columns">
    View and export settlement records, download monthly TDR reports, filter by date and UTR, and configure priority settlements.
  </Card>

  <Card title="Webhooks for Refunds" href="https://docs.payu.in/docs/webhooks-for-refunds" icon="fa-plug">
    Receive automated server-to-server notifications when a refund status changes.
  </Card>
</Cards>

***

## Use AI to Help You

Use an AI coding assistant with the PayU Developer MCP to search these docs, scaffold your Bolt SDK integration, and debug `responseHandler()` without leaving your editor. The prompts below work well as starting points.

<Callout icon="💬" theme="info">
  ### **Example Prompts for AI Coding Assistants**

  - `How do I add the Bolt SDK to my website for PayU Checkout Plus?`
  - `What parameters do I pass to bolt.launch() for a PayU payment?`
  - `How do I generate a SHA-512 hash for Checkout Plus on the backend?`
  - `What is the difference between Checkout Plus and PayU Hosted Checkout?`
  - `Why is my responseHandler not being called after the payment modal closes?`
  - `How do I handle a CANCEL status in the Checkout Plus responseHandler?`
</Callout>

<Cards columns="2">
  <Card title="PayU Developer MCP" href="doc:payu-devguide-builder-mcp-configuration" icon="fa-server">
    Add the PayU docs MCP to Cursor, VS Code, or Claude Desktop. Search documentation and fetch integration code directly from your AI assistant.
  </Card>

  <Card title="PayU Hosted Checkout AI Skill" href="doc:payu-hosted-checkout-ai-skill" icon="fa-wand-magic-sparkles">
    AI skill that scaffolds the underlying PayU Hosted Checkout integration — required before adding the Checkout Plus modal layer.
  </Card>
</Cards>

***

## Split the Settlement Across Multiple Accounts

If your business operates as a **marketplace, aggregator, or platform**, collecting payments on behalf of vendors, service providers, or partners, PayU can automatically <Anchor target="_blank" href="https://docs.payu.in/docs/split-settlments">split the settlement</Anchor> from each Payment Link transaction into multiple bank accounts.

You define the split rules: by absolute amount or by percentage, applied either at the time of the transaction or after collection. Each sub-merchant receives their portion directly; you retain your platform fee.

***

## Next Steps

<Cards columns="2">
  <Card title="How It Works" href="./how-it-works" icon="fa-diagram-project">
    Understand the modal payment flow, the Bolt SDK's role, and how Checkout Plus relates to PayU Hosted Checkout.
  </Card>

  <Card title="Quick Start" href="./quick-start" icon="fa-play">
    Make your first test payment in minutes — SDK setup, hash generation, and bolt.launch() in the sandbox.
  </Card>

  <Card title="Build Integration" href="./integrate/build-integration" icon="fa-code">
    Complete implementation guide: all parameters, hash formula, response handling, and security requirements.
  </Card>

  <Card title="Checkout Plus APIs" href="./checkout-plus-apis" icon="fa-rectangle-api">
    API reference index: Bolt SDK, Collect Payment, Verify Payment, and transaction management APIs.
  </Card>
</Cards>