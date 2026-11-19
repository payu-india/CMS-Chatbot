---
title: Merchant Hosted Checkout
excerpt: Build your own checkout UI and send payment details to PayU with a secure form POST
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Build your own payment page and collect cards, UPI, net banking, wallets, PayPal, and Pluxee with PayU Merchant Hosted Checkout plus SHA-512 hash checks.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Banner
  isInline={true}
  message="Integration effort: You build the checkout and collect payment details. PCI-DSS applies for cards."
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

# Merchant Hosted Checkout

Merchant Hosted Checkout (also called Custom Checkout) lets you design the payment experience on your website. You collect the payment details, generate a SHA-512 hash on your server, and form-POST the request to PayU. PayU processes the payment in a secured environment and redirects the customer back to your success or failure URL.

## What Can I Build with Merchant Hosted Checkout?

<Accordion title="A checkout UI that matches your site" icon="fa-palette">
  You control the look and feel of the payment page and the customer relationship from start to finish. PayU processes the payment after your page posts the request.
</Accordion>

<Accordion title="Card payments, including saved cards, guest checkout, and 3DS 2.0" icon="fa-credit-card">
  Collect Visa, Mastercard, American Express, Diners, and RuPay on your page with `pg=CC`. You can validate the BIN, pay with a network token, pass an Alt ID for guest checkout, and send `threeDS2RequestData` for 3DS Secure 2.0. See [Cards](./integration-guide/build-integration/cards).
</Accordion>

<Accordion title="UPI Collect on your checkout" icon="fa-mobile-screen">
  Validate the customer's VPA, then post `pg=UPI` and `bankcode=UPI` with the VPA. NPCI allows UPI Collect only for MCC 6012 and 6211. Web integrations use a UPI Intent deeplink rendered as a QR. See [UPI Collect](./integration-guide/build-integration/upi-collect).
</Accordion>

<Accordion title="Net banking and wallets" icon="fa-building-columns">
  Post net banking with a bank-specific `bankcode`, or wallets with `pg=CASH` and the wallet code. Advantage Club uses `pg=RD` and `bankcode=ADVCLUB`. See [Net Banking](./integration-guide/build-integration/net-banking) and [Wallets](./integration-guide/build-integration/wallets).
</Accordion>

<Accordion title="PayPal and Pluxee" icon="fa-wallet">
  PayPal uses `pg=PAYPAL` and `bankcode=PAYPAL` after you activate it in the PayU Dashboard. Pluxee (Sodexo) uses `pg=MC` and `bankcode=SODEXO`. See [PayPal](./integration-guide/build-integration/paypal) and [Pluxee](./integration-guide/build-integration/pluxee).
</Accordion>

## Is Merchant Hosted Checkout Right for Me?

| I want to… | Works? |
| --- | --- |
| Design the payment page on my own website | ✅ |
| Collect card details on my page and post them to PayU | ✅ PCI-DSS SAQ A-EP applies |
| Accept UPI Collect | ✅ Only for MCC 6012 and 6211. Web uses UPI Intent as a QR |
| Accept net banking, wallets, PayPal, and Pluxee | ✅ PayPal must be activated in the Dashboard. International cards must be enabled by PayU |
| Keep the hash and salt on my server and verify every response | ✅ |

<!-- DOCUMENTATION GAP: This folder does not define when to choose Payment Links, PayU Hosted Checkout, or the Mobile SDK instead. Do not add those comparison rows until a source page states them. -->

<Callout icon="📘" theme="info">
  Not sure which PayU product to use? See [Start Here](https://docs.payu.in/docs/start-here).
</Callout>

## Supported Payment Methods

Each method is selected with `pg` and `bankcode` on `POST /_payment`. Values below are taken from the existing Merchant Hosted pages. Where those pages disagree, both values are shown.

<!-- VALIDATION NEEDED: pg and bankcode conflicts are documented in the Notes column. Cards bankcode is CC on the overview table and on one cURL, and MAST, AMEX, VISA, or MASTERCARD on other card samples. Net banking pg is NB on the overview, NEFT on the steps card, and TESTPG in samples. EFTNET prose says pg=NEFTRTGS; the overview table says pg=NB and bankcode=EFTAXTPV. The UPI overview cell says bankcode is N/A and also INTENT (Intent) and UPIDBQR (QR). UPI Collect uses bankcode=UPI. -->

| Method | pg | bankcode | Guide |
| --- | --- | --- | --- |
| Credit and debit cards | CC | CC, or a scheme code (see note) | [Cards](./integration-guide/build-integration/cards) |
| Net banking | NB (samples use TESTPG) | Bank-specific (samples use TESTPGNB) | [Net Banking](./integration-guide/build-integration/net-banking) |
| Wallets | CASH (Advantage Club: RD) | Wallet-specific (Advantage Club: ADVCLUB) | [Wallets](./integration-guide/build-integration/wallets) |
| UPI Collect | UPI | UPI | [UPI Collect](./integration-guide/build-integration/upi-collect) |
| UPI Intent | UPI | INTENT | [UPI Intent S2S](https://docs.payu.in/docs/upi-intent-server-to-server) |
| UPI QR | UPI | UPIDBQR | [UPI QR](doc:integrate-upi-qr) |
| PayPal | PAYPAL | PAYPAL | [PayPal](./integration-guide/build-integration/paypal) |
| Pluxee (Sodexo) | MC | SODEXO | [Pluxee](./integration-guide/build-integration/pluxee) |
| EMI | CC | See EMI guides | [EMI](doc:collect-payments-with-emi-using-credit-card) |
| BNPL | Varies by provider | Varies by provider | [BNPL workflow](https://docs.payu.in/docs/general-flow-bnpl-integration-with-merchant-hosted) |
| EFTNET (NEFT/RTGS) | NEFTRTGS in the overview prose; NB in the overview table | EFTAXTPV in the overview table | [EFTNET](https://docs.payu.in/docs/collect-payments-with-eftnet-neftrtgs-seamless/) |
| QR code | UPI | Not stated on the overview | [Dynamic Storefront QR](doc:integrated-dynamic-storefront) |
| Net banking TPV | Not stated in this folder | Not stated in this folder | [Net Banking TPV](https://docs.payu.in/docs/net-banking-integration-for-tpv/) |

<Callout icon="📘" theme="info">
  `bankcode` values are case-sensitive. Enable each method on your PayU merchant account before you use it. PayPal is activated from the PayU Dashboard. International card transactions are enabled by writing to the PayU Integration Team at integration@pay.in. For NEFT/RTGS, the overview says to pass the customer account number and IFSC, and to reconcile payments with orders.
</Callout>

<Callout icon="⚠️" theme="warn">
  **UPI Collect disablement (NPCI).** For Merchant Hosted integrations using `txn_s2s_flow = 2` or `txn_s2s_flow = 4`: Android apps must use Smart Intent. iOS can keep UPI Collect with a deeplink. Web must generate a QR from the UPI Intent S2S deeplink. Seamless form POST does not support Intent on Android and desktop web, so those merchants move to `txn_s2s_flow`.
</Callout>

## Common Use Cases

<!-- NEW CONTENT: The source overview has no use-case list. These four cards describe checkout situations that match methods documented in this folder. -->

<Cards columns={3}>
  <Card title="Branded retail checkout" icon="fa-bag-shopping" href="./integration-guide/build-integration/cards">
    Collect cards on a page you design, then post the payment to PayU.
  </Card>
  <Card title="UPI Collect for permitted MCCs" icon="fa-mobile-screen" href="./integration-guide/build-integration/upi-collect">
    Take a VPA on your checkout when your MCC is 6012 or 6211.
  </Card>
  <Card title="Wallets on your checkout" icon="fa-wallet" href="./integration-guide/build-integration/wallets">
    Post `pg=CASH` and the wallet `bankcode` from your payment page.
  </Card>
  <Card title="Pluxee meal cards" icon="fa-utensils" href="./integration-guide/build-integration/pluxee">
    Accept a Pluxee card with `pg=MC` and `bankcode=SODEXO`.
  </Card>
  <Card title="International PayPal payments" icon="fa-globe" href="./integration-guide/build-integration/paypal">
    Let customers pay with PayPal after you activate it in the Dashboard. Settlements are in INR.
  </Card>
</Cards>

## What Do I Need to Get Started?

- A PayU merchant account. Use a test account while you integrate, then a production account.
- The merchant key and salt from the PayU Dashboard. The salt is used to generate request and response hashes.
- A website served over HTTPS.
- A backend that can generate a SHA-512 hash. The salt stays on that server.
- Public success (`surl`) and failure (`furl`) URLs.
- PCI-DSS compliance, including SAQ A-EP, if you store, process, or transmit cardholder data. That applies when you collect card or Pluxee details on your site.
- A way to confirm the transaction on the server if the browser callback fails. The production checklist names webhooks and the Verify Payment API for this.

<Callout icon="⚠️" theme="warn">
  If you use only UPI and wallets, your site still has to be served securely.
</Callout>

You also need enough technical ownership to run the checkout yourself: payment workflows, page design, and the end-to-end web checkout process.

## How Do I Integrate Merchant Hosted Checkout?

<Accordion title="1. Choose the payment method" icon="fa-circle-1">
  Set `pg` and `bankcode` for the method the customer selected. Method-specific fields differ. Cards send card details. UPI Collect sends `vpa`. Pluxee can send `save_sodexo_card` or `source_id`.
</Accordion>

<Accordion title="2. Generate the hash on your server" icon="fa-circle-2">
  Hash `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||Salt)` with SHA-512. Leave unused `udf` values empty so the pipe count stays the same.
</Accordion>

<Accordion title="3. Form-POST the payment from the browser" icon="fa-circle-3">
  Post the fields to `https://test.payu.in/_payment` in test, or `https://secure.payu.in/_payment` in production.
</Accordion>

<Accordion title="4. Check the callback" icon="fa-circle-4">
  PayU redirects the customer to `surl` or `furl` and posts the result. Recompute the reverse hash before you trust the response.
</Accordion>

<Accordion title="5. Verify the payment on your server" icon="fa-circle-5">
  Call the Verify Payment API (`verify_payment`). If the browser callback does not arrive, use webhooks and verify on the server.
</Accordion>

<Callout icon="📘" theme="info">
  Parameter tables, samples, and pre-steps are in [Build the Integration](./integration-guide/build-integration).
</Callout>

## Is My Integration Secure?

Generate the hash on your server. The salt is known only to you and PayU. Serve the site over HTTPS. Do not store the CVV or the full card number. For Pluxee, do not store the full card number, expiry, or CVV even when the customer agrees to save the card. Use a saved-card token, an Alt ID, or Pluxee `source_id` instead.

Verify the reverse hash on the callback, then confirm the status with the Verify Payment API. Card collection on your site is in PCI-DSS scope. The cards guide names the SAQ A-EP form. PayU supports 3DS Secure 2.0 on this integration when you send `threeDS2RequestData`.

More guidance is on [Best Practices](./best-practices).

## How Does My Customer Pay?

The flow below is the card journey documented for Merchant Hosted Checkout. Other methods follow the same shape: collect details on your page, post to PayU, authenticate with the bank or provider, then return to your site.

<Accordion title="1. The customer pays on your site" icon="fa-circle-1">
  The customer finishes shopping and starts payment with the details your page collects. For a saved card, they enter the CVV.
</Accordion>

<Accordion title="2. Your page posts the payment to PayU" icon="fa-circle-2">
  The browser form-POSTs the payment data to PayU. The customer then moves through PayU's secured environment, which shows the transaction ID.
</Accordion>

<Accordion title="3. The bank authenticates the customer" icon="fa-circle-3">
  For cards, the customer reaches the bank ACS page and enters the OTP sent to the registered mobile number.
</Accordion>

<Accordion title="4. PayU returns the customer to you" icon="fa-circle-4">
  After the bank finishes, PayU redirects the customer to your website.
</Accordion>

<Accordion title="5. You show the result" icon="fa-circle-5">
  Your site shows success or failure from the PayU transaction status, after you verify the response.
</Accordion>

<Image src="https://files.readme.io/4aeeafdbefc392fa362522d8209dc7268178e104e699b067895a3408ff412c42-merchant_hosted_flow.png" alt="Merchant Hosted Checkout flow from the merchant site through PayU and the bank, then back to the merchant" align="center" />

## Post-Payment Actions

<Cards columns={2}>
  <Card title="Verify Payment" icon="fa-circle-check" href="./merchant-hosted-checkout-apis">
    Confirm the transaction with `verify_payment` after the callback.
  </Card>
  <Card title="Refund" icon="fa-rotate-left" href="./merchant-hosted-checkout-apis">
    Refund with `cancel_refund_transaction`. PayPal refunds also need funds in the PayPal wallet.
  </Card>
  <Card title="Check action status" icon="fa-magnifying-glass" href="./merchant-hosted-checkout-apis">
    Check an action with `check_action_status`.
  </Card>
  <Card title="Get transaction info" icon="fa-receipt" href="./merchant-hosted-checkout-apis">
    Look up a transaction with `get_transaction_info`.
  </Card>
</Cards>

The production checklist says to use webhooks when the browser callback fails. Webhook event names for this product are not listed in this folder. See [Webhooks](doc:webhooks).

## Next Steps

<Cards columns={2}>
  <Card title="How It Works" icon="fa-diagram-project" href="./how-it-works">
    Endpoints, hash formulas, and the payment flow.
  </Card>
  <Card title="Quick Start" icon="fa-bolt" href="./quick-start">
    Make one test card payment.
  </Card>
  <Card title="Build the Integration" icon="fa-code" href="./integration-guide/build-integration">
    Parameters and samples for each payment method.
  </Card>
  <Card title="Best Practices" icon="fa-shield-halved" href="./best-practices">
    Card data, validation, txnid, and callback checks.
  </Card>
  <Card title="APIs" icon="fa-rectangle-api" href="./merchant-hosted-checkout-apis">
    Collect Payment and the post-service commands used here.
  </Card>
</Cards>
