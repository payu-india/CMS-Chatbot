---
title: Merchant Hosted Checkout
excerpt: Collect payment details on your own checkout and post them to PayU for processing
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Build a custom PayU checkout on your site. Form-post card, UPI, net banking, wallet, PayPal, and Pluxee payments to _payment with a server-side SHA-512 hash.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Banner
  isInline={true}
  message="Integration effort: you host the checkout UI and collect payment details"
  color="#FF6B00"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

# Merchant Hosted Checkout

Merchant Hosted Checkout, also called Custom Checkout, lets you collect payment details on your website and post them to PayU. You design the checkout. PayU processes the payment, sends the customer through the bank, wallet, or UPI flow when that is required, and redirects the customer back to your success or failure URL.

## What Can I Build with Merchant Hosted Checkout?

<Accordion title="A checkout that matches your site" icon="fa-paintbrush">
  You collect the payment details on your page and post them to PayU. The source describes this as control over the look and feel of checkout, with the customer relationship staying on your site.
</Accordion>

<Accordion title="Card payments on your page" icon="fa-credit-card">
  Visa, Mastercard, American Express, Diners, and RuPay. You collect the card fields and post them with `pg=CC`. Card data on your site is in PCI-DSS scope.
</Accordion>

<Accordion title="Net banking, wallets, and UPI Collect" icon="fa-building-columns">
  Net banking, wallets, and UPI Collect each use the same `_payment` endpoint with their own `pg` and `bankcode`. UPI Collect also needs the customer's VPA.
</Accordion>

<Accordion title="PayPal for international payments" icon="fa-globe">
  PayPal uses `pg=PAYPAL` and `bankcode=PAYPAL`. Activate PayPal on the PayU Dashboard before you use it. Settlements are processed in INR.
</Accordion>

<Accordion title="Pluxee meal cards" icon="fa-utensils">
  Pluxee (formerly Sodexo) uses `pg=MC` and `bankcode=SODEXO`. The source recommends checking the card balance before you post the payment.
</Accordion>

## Is Merchant Hosted Checkout Right for Me?

| I want to… | Works? |
| --- | --- |
| Design the payment form on my own website | ✅ |
| Choose the payment method in the request with `pg` and `bankcode` | ✅ |
| Let PayU host the payment page | ⚠️ Use [PayU Hosted Checkout](https://docs.payu.in/docs/payu-hosted-checkout-1) instead |
| Accept payments without a website | ⚠️ Use [Payment Links](https://docs.payu.in/docs/payment-links-dashboard) instead |
| Accept payments inside a native mobile app | ⚠️ Use [PayU Mobile SDK](https://docs.payu.in/docs/mobile-sdk-integration) instead |
| Set up recurring auto-debit | ⚠️ Use [Recurring Payments](https://docs.payu.in/docs/introduction-recurring-payments-integration) instead |

<Callout icon="📘" theme="info">
  Not sure? Compare this with PayU Hosted Checkout. Hosted Checkout collects payment details on PayU's page. Merchant Hosted Checkout collects them on yours.
</Callout>

## Supported Payment Methods

Each method is selected with `pg` and `bankcode` on the `_payment` request. Bank codes are case-sensitive, and the method must be enabled on your PayU account.

| Method | pg | bankcode | Guide |
| --- | --- | --- | --- |
| Credit and debit cards | CC | Network-specific. Samples in the source use CC, MAST, AMEX, and VISA | [Cards](./integration-guide/build-integration/cards) |
| Net banking | NB in the parameter table. Samples use TESTPG | Bank-specific. The test sample uses TESTPGNB | [Net Banking](./integration-guide/build-integration/net-banking) |
| Wallets | CASH. Advantage Club uses RD | Wallet-specific. The Paytm sample uses PAYTM. Advantage Club uses ADVCLUB | [Wallets](./integration-guide/build-integration/wallets) |
| UPI Collect | UPI | UPI | [UPI Collect](./integration-guide/build-integration/upi-collect) |
| PayPal | PAYPAL | PAYPAL | [PayPal](./integration-guide/build-integration/paypal) |
| Pluxee (Sodexo) | MC | SODEXO | [Pluxee](./integration-guide/build-integration/pluxee) |

<!-- VALIDATION NEEDED: The overview table in the legacy Merchant Hosted page says PayPal bankcode is N/A. The PayPal integration page says bankcode=PAYPAL. The net banking steps card says pg=NEFT, the parameter table says pg=NB, and the samples use pg=TESTPG. The overview also says every net banking request must include account number and IFSC; those fields are not on the net banking page. EFTNET is described once as pg=NEFTRTGS and once as pg=NB with bankcode=EFTAXTPV. -->

<Callout icon="📘" theme="info">
  EMI, BNPL, EFTNET (NEFT/RTGS), and Net Banking TPV are listed on the legacy pages as links to other guides. Those guides are not rewritten here. UPI Intent is a server-to-server flow, not this form POST. QR points at Dynamic Storefront, which is a different product.
</Callout>

<Callout icon="⚠️" theme="warn">
  **NPCI mandate on UPI Collect.** For Merchant Hosted integrations using `txn_s2s_flow = 2` or `txn_s2s_flow = 4`: Android apps must use Smart Intent; web must use the UPI Intent S2S deeplink to build a QR, not UPI Collect; iOS may keep a deeplink and UPI Collect. Seamless form POST does not support Intent. UPI Collect is allowed only for MCC 6012 and 6211.
</Callout>

## Common Use Cases

<Cards columns={3}>
  <Card title="Branded web checkout" icon="fa-store" href="./integration-guide/build-integration">
    Collect the payment on your site and post it to PayU with the method the customer chose.
  </Card>
  <Card title="Saved-card repeat payment" icon="fa-credit-card" href="./integration-guide/build-integration/cards">
    Post a network token with `store_card_token` instead of the full card number.
  </Card>
  <Card title="UPI Collect" icon="fa-mobile-screen" href="./integration-guide/build-integration/upi-collect">
    Validate the VPA, then post `pg=UPI`, `bankcode=UPI`, and `vpa`.
  </Card>
  <Card title="International PayPal" icon="fa-globe" href="./integration-guide/build-integration/paypal">
    Post `pg=PAYPAL` and `bankcode=PAYPAL` after PayPal is activated on the Dashboard.
  </Card>
  <Card title="Pluxee meal cards" icon="fa-utensils" href="./integration-guide/build-integration/pluxee">
    Check the balance, then post the Pluxee card with `pg=MC` and `bankcode=SODEXO`.
  </Card>
</Cards>

## What Do I Need to Get Started?

- A PayU merchant account. Use a test account while you integrate, then a production account.
- The merchant key and salt from the PayU Dashboard. The salt is used to generate the hash.
- HTTPS on your site.
- A backend that generates the SHA-512 hash. Do not put the salt in the browser.
- A success URL (`surl`) and a failure URL (`furl`) that PayU can reach.
- PCI-DSS compliance, including SAQ A-EP, if you store, process, or transmit cardholder data. The source states that Merchant Hosted Checkout collects card details on your site, so card flows are in scope.
- Webhooks if you need a server-to-server update when the browser callback does not arrive. Confirm the transaction with the Verify Payment API.

<Callout icon="⚠️" theme="warn">
  If you use only UPI and wallet modes, the source still says your website must be secure.
</Callout>

## How Do I Integrate Merchant Hosted Checkout?

<Accordion title="1. Choose the payment method" icon="fa-circle-1">
  Set `pg` and `bankcode` for the method the customer selected. Card, UPI Collect, and Pluxee requests also include the method-specific fields.
</Accordion>

<Accordion title="2. Generate the hash on your server" icon="fa-circle-2">
  Build the hash string in the documented field order and hash it with SHA-512 and your salt. The salt stays on the server.
</Accordion>

<Accordion title="3. Post the payment from the browser" icon="fa-circle-3">
  Form-post the parameters and the hash to `https://test.payu.in/_payment` in test, or `https://secure.payu.in/_payment` in production.
</Accordion>

<Accordion title="4. Handle surl and furl" icon="fa-circle-4">
  PayU redirects the customer to your success or failure URL and posts the transaction response. Verify the reverse hash before you accept the result.
</Accordion>

<Accordion title="5. Verify the payment on the server" icon="fa-circle-5">
  Call Verify Payment (`command=verify_payment`) and use webhooks when the callback does not arrive. Do not fulfil an order from the browser callback alone.
</Accordion>

<Callout icon="📘" theme="info">
  Parameter tables, samples, and method-specific pre-steps are in [Build the Integration](./integration-guide/build-integration).
</Callout>

## Is My Integration Secure?

Generate the hash on your server. The salt is known only to you and PayU. Never store the CVV. Do not store the full card number or expiry on your server. For repeat card payments, the source points to PayU Save Cards or another PCI-DSS tokenization service. Verify the reverse hash on the callback, then confirm the status with Verify Payment. Use HTTPS between the browser and your site, and between your server and PayU. PayU supports 3DS 2.0 on this integration.

## How Does My Customer Pay?

<Accordion title="1. The customer pays on your site" icon="fa-circle-1">
  The customer finishes checkout on your website and submits the payment details you collected, such as a saved card and CVV.
</Accordion>

<Accordion title="2. PayU receives the form post" icon="fa-circle-2">
  The browser posts the payment to PayU. The source describes a secured PayU environment that shows the transaction ID.
</Accordion>

<Accordion title="3. The bank, wallet, or UPI app authenticates" icon="fa-circle-3">
  For cards, the customer completes the bank ACS page with the OTP the bank sends. Net banking, wallets, UPI, PayPal, and Pluxee follow the flow for that method.
</Accordion>

<Accordion title="4. The customer returns to your site" icon="fa-circle-4">
  PayU redirects to your site. You show success or failure from the transaction status PayU returns.
</Accordion>

## Post-Payment Actions

<Cards columns={2}>
  <Card title="Verify Payment" icon="fa-circle-check" href="https://docs.payu.in/reference/verify_payment_api">
    Confirm the status with `command=verify_payment` before you fulfil the order.
  </Card>
  <Card title="Get Transaction Info" icon="fa-receipt" href="https://docs.payu.in/reference/get_transaction_info_api">
    Look up a transaction by txnid with `command=get_transaction_info`.
  </Card>
  <Card title="Refund" icon="fa-rotate-left" href="https://docs.payu.in/reference/refund_transaction_api">
    Refund with `command=cancel_refund_transaction`, or from the PayU Dashboard.
  </Card>
  <Card title="Webhooks" icon="fa-plug" href="https://docs.payu.in/docs/webhooks">
    Use webhooks when the browser callback does not arrive. This folder does not list webhook event names.
  </Card>
</Cards>

## Use AI to Help You

Ask an assistant to look up the hash formula, the `_payment` fields for one method, or the callback checks. Use the docs as the source. Do not paste your salt into a chat.

<Callout icon="📘" theme="info">
  Example prompts: "What is the SHA-512 request hash field order for PayU Merchant Hosted Checkout?" "Which pg and bankcode does UPI Collect use?" "What does the cards callback field error E1903 mean in the Merchant Hosted sample?"
</Callout>

<Cards columns={2}>
  <Card title="PayU Developer MCP" icon="fa-server" href="https://docs.payu.in/docs/payu-devguide-builder-mcp-configuration">
    Connect the PayU docs MCP so an assistant can read these guides from the editor.
  </Card>
  <Card title="Integration Lab" icon="fa-flask" href="https://payu.in/integrationlab/seamless/sm-nb-status">
    The net banking and UPI Collect source pages link to Integration Lab flows that generate sample code.
  </Card>
</Cards>

## Next Steps

<Cards columns={2}>
  <Card title="How It Works" icon="fa-diagram-project" href="./how-it-works">
    Endpoints, hash formulas, and the payment flow.
  </Card>
  <Card title="Quick Start" icon="fa-play" href="./quick-start">
    Post one net banking test payment and verify the callback.
  </Card>
  <Card title="Build the Integration" icon="fa-code" href="./integration-guide/build-integration">
    Parameter tables and samples for each payment method.
  </Card>
  <Card title="Best Practices" icon="fa-list-check" href="./best-practices">
    Card data handling, pre-checks, and callback verification.
  </Card>
  <Card title="APIs" icon="fa-rectangle-api" href="./merchant-hosted-checkout-apis">
    `_payment`, pre-payment commands, and post-payment commands.
  </Card>
</Cards>
