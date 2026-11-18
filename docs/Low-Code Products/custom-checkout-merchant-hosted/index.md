---
title: Merchant Hosted Checkout
excerpt: Build your own payment form and post the payment to PayU
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Build a custom checkout on your site and post payments to PayU. Cards, UPI,
    net banking, and wallets use a server-side SHA-512 hash and surl/furl callbacks.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Banner
  isInline={true}
  message="Integration effort: you build the payment form and post to _payment"
  color="#FF6B00"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

# Merchant Hosted Checkout

Merchant Hosted Checkout is PayU's custom checkout. You design the payment form, collect the payment details on your site, and post them to PayU. PayU processes the payment and sends the customer through bank authentication when the method requires it. After the bank step, PayU redirects the customer to your success or failure URL.

<Callout icon="👍" theme="okay">
  Merchant Hosted Checkout is a specific PayU product. This guide covers that product and its APIs. It is distinct from simply placing payment fields on a page.
</Callout>

## What Can I Build with Merchant Hosted Checkout?

<Accordion title="A checkout UI that matches your site" icon="fa-paintbrush">
  You control the look and feel of the payment form. PayU does not render the payment page for this product. The customer enters payment details on your website.
</Accordion>

<Accordion title="One collect endpoint for many methods" icon="fa-credit-card">
  A browser form POST to `_payment` collects cards, net banking, wallets, UPI, EMI, BNPL, PayPal, Pluxee, and EFTNET. The method is chosen with `pg` and `bankcode`. Each method has its own extra fields.
</Accordion>

<Accordion title="The customer stays on your site until bank authentication" icon="fa-arrow-right-arrow-left">
  The payment starts as a form post from the customer's browser into PayU. The customer is then taken through PayU's secured environment and, when required, to the card ACS or the bank's net banking page. PayU redirects the customer back to your site with the result.
</Accordion>

<Accordion title="Card data collected by you" icon="fa-shield-halved">
  For cards and Pluxee you collect the card number, name, expiry, and CVV on your page. If you store, process, or transmit cardholder data, the source says you must be PCI-DSS compliant. The source names the Self-Assessment Questionnaire A-EP.
</Accordion>

<Accordion title="A direct customer relationship" icon="fa-user">
  You keep the customer on your checkout from the start of payment until the redirect back. You decide what the form asks for, within the parameters each method requires.
</Accordion>

## Is Merchant Hosted Checkout Right for Me?

<!-- NEW CONTENT: Comparison rows are drawn only from statements in the Merchant Hosted source. Checkout Plus, Payment Links, and the mobile SDK are not compared in that source. -->

| I want to… | Works? |
| --- | --- |
| Build the payment form on my own website | ✅ |
| Accept cards, and I can meet PCI-DSS (the source names SAQ A-EP) | ✅ |
| Accept UPI or wallets without collecting card numbers | ✅ Keep the site on HTTPS. The source's warning for UPI-and-wallet-only is to keep the website secure. |
| Send the customer to a prebuilt PayU payment page | ⚠️ That is PayU Hosted Checkout, which this source distinguishes from Merchant Hosted Checkout. |

<!-- DOCUMENTATION GAP: The Merchant Hosted source has no comparison with Checkout Plus, Payment Links, or the mobile SDK. Do not add those rows from the separate Low-Code overview page unless that content is approved. -->

<Callout icon="📘" theme="info">
  Not sure? This product is the PayU Merchant Hosted Checkout API. It is not a generic pattern for hosting payment fields yourself.
</Callout>

## Supported Payment Methods

You choose the method by posting `pg` and `bankcode` on `_payment`. Values below are the overview table in the current Merchant Hosted docs. Where a method page disagrees, the note under the table says so. Do not treat the conflicting cell as settled.

| Method | pg | bankcode | Guide |
| --- | --- | --- | --- |
| Credit and debit cards | CC | CC | [Cards](./integration-guide/build-integration/cards) |
| Net banking | NB | Bank-specific | [Net Banking](./integration-guide/build-integration/net-banking) |
| Wallets | CASH | Wallet-specific | [Wallets](./integration-guide/build-integration/wallets) |
| UPI | UPI | See the note | [UPI Collect](./integration-guide/build-integration/upi-collect) and [UPI Intent](./integration-guide/build-integration/upi-intent) |
| EMI | CC | N/A in the overview table | [EMI](./integration-guide/build-integration/emi) |
| BNPL | Varies by provider | Varies by provider | [BNPL](./integration-guide/build-integration/bnpl) |
| PayPal | PAYPAL | N/A in the overview table | [PayPal](./integration-guide/build-integration/paypal) |
| Pluxee (Sodexo) | MC | SODEXO | [Pluxee](./integration-guide/build-integration/pluxee) |
| EFTNET (NEFT/RTGS) | NB in the overview table | EFTAXTPV in the overview table | [EFTNET](./integration-guide/build-integration/eftnet) |
| QR | UPI | N/A in the overview table | Not part of this guide. The source points at Dynamic Storefront QR. |

<!-- VALIDATION NEEDED: Payment-method matrix conflicts inside the current Merchant Hosted docs.
- Cards: the overview says bankcode CC. The cards page also uses MAST, AMEX, VISA, and MASTERCARD.
- UPI: the overview says bankcode N/A, then INTENT for UPI Intent and UPIDBQR for UPI QR. The UPI Collect page uses bankcode UPI. Collect is not a row in the overview table.
- PayPal: the overview says no bankcode is required. The PayPal page requires bankcode PAYPAL.
- Net banking: the overview says pg NB. The net-banking step card says pg NEFT. The test sample uses pg TESTPG and bankcode TESTPGNB.
- EFTNET: the overview prose says pg NEFTRTGS and a bank-specific bankcode. The overview table says pg NB and bankcode EFTAXTPV.
- EMI: the overview says bankcode N/A and also points at EMI codes.
- QR is described here and documented as Dynamic Storefront QR, which is outside this folder. -->

<Callout icon="📘" theme="info">
  `bankcode` values are case-sensitive. Enable each method on your PayU merchant account before you use it. PayPal must be activated from the PayU Dashboard. UPI Collect is allowed only for MCC 6012 and 6211.
</Callout>

<Callout icon="❗️" theme="error">
  **UPI Collect disablement (NPCI).** For Merchant Hosted integrations using `txn_s2s_flow = 2` or `txn_s2s_flow = 4`:

  - Android apps must implement Smart Intent. The source points at UPI Smart Intent (non-SDK) or the PayU Android SDKs.
  - iOS apps can use a deeplink and continue with UPI Collect.
  - Web must build a QR from the deeplink returned by UPI Intent S2S, instead of UPI Collect.
  - Seamless form post must move to `txn_s2s_flow` (UPI Intent S2S). The source says Intent is not supported in the seamless form post flow for Android and desktop web.
</Callout>

## Common Use Cases

<!-- DOCUMENTATION GAP: The Merchant Hosted source has no use-case list. Do not invent retail, subscription, or marketplace examples here. -->

## What Do I Need to Get Started?

- A PayU merchant account. Use a test account while you integrate, then a production account.
- The merchant key and salt from the PayU Dashboard. The key identifies the account. The salt is the secret used in the hash.
- Test key and salt while you build. Live key and salt only after you go live. The source says live credentials are under Live Mode, then **Payment Gateway → Web Integration → Key Salt Details**.
- HTTPS on your site.
- PCI-DSS compliance if you store, process, or transmit cardholder data. The source names SAQ A-EP, and it says Merchant Hosted Checkout collects card details on your site, so you must be PCI-DSS compliant for cards.
- A success URL (`surl`) and a failure URL (`furl`).
- Webhooks, so PayU can notify your server if the browser callback does not arrive. Confirm the status with the Verify Payment API in that case.
- Enough in-house ownership to run the checkout: the payment flows, the page, and the usability of the form.

<Callout icon="🚧" theme="warn">
  If you use only UPI and wallets with Merchant Hosted Checkout, the source says to keep your website secure.
</Callout>

## How Do I Integrate Merchant Hosted Checkout?

<Accordion title="1. Generate the hash on your server" icon="fa-circle-1">
  Build the SHA-512 hash from the payment fields and your salt. The salt never goes in the browser. The formula used on the method pages is `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||Salt)`.
</Accordion>

<Accordion title="2. Post _payment from the browser" icon="fa-circle-2">
  Submit a form POST to `https://test.payu.in/_payment` in test, or `https://secure.payu.in/_payment` in production. Set `pg` and `bankcode` for the method the customer chose, plus that method's extra fields.
</Accordion>

<Accordion title="3. Handle surl and furl" icon="fa-circle-3">
  PayU redirects the customer to `surl` or `furl` and posts the result. Read `status`, `mihpayid`, `txnid`, and `error` from that post.
</Accordion>

<Accordion title="4. Check the reverse hash" icon="fa-circle-4">
  Recreate the response hash with your salt before you trust the callback. The formula written on the UPI Collect page is `sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)`.
</Accordion>

<Accordion title="5. Verify the payment on the server" icon="fa-circle-5">
  Call Verify Payment (`verify_payment`) from your server. If the callback fails, use webhooks and still confirm with Verify Payment. Do not fulfil an order from the browser redirect alone.
</Accordion>

<Callout icon="📘" theme="info">
  Parameter tables, samples, and pre-steps are in [Build the Integration](./integration-guide/build-integration).
</Callout>

## Is My Integration Secure?

Generate the hash on the server. Keep the salt on the server. Serve the site over HTTPS. Do not store the CVV or the full card number. For cards, the source says to implement 3DS 2.0 and to verify the response hash. If the callback does not arrive, confirm the transaction with Verify Payment. Tokenization, or PayU Save Cards, is what the source recommends when a card has to be reused. See [Best Practices](./best-practices).

## How Does My Customer Pay?

The source's customer journey is a saved-card example. Other methods differ after the form post. The bank step below is the card ACS.

<Accordion title="1. The customer pays with a saved card" icon="fa-circle-1">
  The customer finishes shopping on your site and starts the payment with saved card credentials. The source uses a Visa card as the example.
</Accordion>

<Accordion title="2. The customer enters the CVV" icon="fa-circle-2">
  The customer enters the CVV on your page and continues.
</Accordion>

<Accordion title="3. PayU shows a secured page with the transaction id" icon="fa-circle-3">
  After the payment is launched, the customer passes through a secured PayU environment that shows the transaction id.
</Accordion>

<Accordion title="4. The customer completes the bank OTP" icon="fa-circle-4">
  The customer reaches the bank ACS page and enters the OTP the bank sent to the registered mobile number.
</Accordion>

<Accordion title="5. Your site shows success or failure" icon="fa-circle-5">
  You show the result from the PayU transaction status.
</Accordion>

## Post-Payment Actions

<Cards columns={2}>
  <Card title="Verify Payment" icon="fa-circle-check" href="./merchant-hosted-checkout-apis">
    Confirm every transaction from your server with verify_payment, including when the browser callback does not arrive.
  </Card>
  <Card title="Webhooks" icon="fa-plug" href="./best-practices">
    The source says to use webhooks when the callback fails. Event names are not listed in this folder.
  </Card>
  <Card title="Refunds" icon="fa-rotate-left" href="./integration-guide/build-integration/paypal">
    Refunds can be started from the PayU Dashboard or the Refund Transaction API (command cancel_refund_transaction). PayPal refunds need funds in the PayPal wallet.
  </Card>
</Cards>

<!-- DOCUMENTATION GAP: Chargeback handling and the settlements dashboard are not documented in the Merchant Hosted source folder. Do not add steps for them here. -->

## Use AI to Help You

<!-- DOCUMENTATION GAP: The Merchant Hosted source has no AI prompt and no MCP instructions. Do not copy the PayU Hosted Checkout skill prompt onto this page. -->

The source links two Integration Lab flows:

- Net banking: [https://payu.in/integrationlab/seamless/sm-nb-status](https://payu.in/integrationlab/seamless/sm-nb-status)
- UPI: [https://payu.in/integrationlab/seamless/sm-upiflow](https://payu.in/integrationlab/seamless/sm-upiflow)

## Next Steps

<Cards columns={2}>
  <Card title="How It Works" icon="fa-diagram-project" href="./how-it-works">
    The form post, the endpoints, and the hash.
  </Card>
  <Card title="Quick Start" icon="fa-bolt" href="./quick-start">
    One test net-banking payment.
  </Card>
  <Card title="Build the Integration" icon="fa-code" href="./integration-guide/build-integration">
    Parameters and samples for each payment method.
  </Card>
  <Card title="Best Practices" icon="fa-shield-halved" href="./best-practices">
    Card data, the hash, and how to confirm a payment.
  </Card>
  <Card title="APIs" icon="fa-rectangle-api" href="./merchant-hosted-checkout-apis">
    _payment and the postservice commands used by this integration.
  </Card>
</Cards>
