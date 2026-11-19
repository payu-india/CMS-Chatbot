---
title: How Merchant Hosted Checkout Works
excerpt: >-
  Understand the _payment API architecture, the form POST flow, PCI-DSS scope,  
  and how Merchant Hosted Checkout differs from PayU's other checkout products.
deprecated: false
hidden: true
metadata:
  robots: index
---
Merchant Hosted Checkout is a direct form POST integration. Your website builds the payment UI, your backend generates the hash, and your server POSTs directly to PayU's `_payment` endpoint. PayU handles payment processing and authentication, then redirects the customer back to your callback URL.

***

## Checkout Flow

The following diagram depicts the merchant Hosted Checkout flow.


<Image src="https://files.readme.io/b0d79404a9835b750ae97ca34bdfc6b4d1b5c98bbfe14d56901e72f785fd4296-payu-payment-flow.png" align="center" caption="Merchant Hosted Checkout Flow" framed={true} />


<AccordionOpen title="Step 1 — Customer fills the payment form">

The customer enters their payment details — card number, UPI ID, or netbanking credentials — directly on a payment form hosted on your website.

This step happens entirely in the customer's browser. Your backend is not involved yet. The form is typically rendered using your own UI, which is what distinguishes Merchant Hosted Checkout from PayU Hosted Checkout.
</AccordionOpen>

<AccordionOpen title="Step 2 — Your backend collects fields and builds the hash">

Once the customer submits the form, your backend receives the payment parameters: `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, and optional UDF fields.

Before sending anything to PayU, your backend must generate a **SHA-512 hash** using the formula:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

This hash acts as a tamper-proof signature. PayU will reject any request where the hash does not match, so this step must always happen server-side — never in the browser where the SALT could be exposed.
</AccordionOpen>

<AccordionOpen title="Step 3 — Your backend POSTs to PayU">

Your backend submits the payment parameters and the hash to PayU's payment endpoint (`/_payment`) via an HTTP POST. This is the handoff from your system to PayU.

At this point, control of the payment flow passes to PayU. The customer may be redirected to a PayU-hosted page for 3DS authentication, depending on the payment method.
</AccordionOpen>

<AccordionOpen title="Step 4 — PayU validates and routes the payment">

PayU receives the request and immediately re-computes the hash on its own side. If the hash matches, the request is considered authentic and processing begins.

PayU then determines the correct payment route — card network, UPI rail, netbanking gateway — and initiates the authentication flow with the issuing bank. If the card requires 3DS verification, PayU triggers that process now.
</AccordionOpen>

<AccordionOpen title="Step 5 — Bank authenticates the customer">

The issuing bank (or the 3DS server) sends an OTP or biometric challenge to the customer. The customer completes the verification step — entering their OTP, approving via their banking app, or passing the biometric check.

Once the customer responds, the bank sends an authentication result back to PayU. A successful authentication does not mean the payment is approved yet — it means the customer's identity has been verified.
</AccordionOpen>

<AccordionOpen title="Step 6 — PayU sends the callback to your backend">

After processing the payment result, PayU sends an HTTP POST to either your `surl` (success URL) or `furl` (failure URL), depending on the outcome. This callback contains the payment status and all relevant transaction parameters.

This is a **server-to-server notification**. It arrives at your backend, not the customer's browser.

> **Important:** Do not treat this callback as the final word on payment status. Callbacks can be tampered with or replayed. Always verify independently (see Step 7).
</AccordionOpen>

<AccordionOpen title="Step 7 — Your backend verifies the payment">

When the callback arrives, your backend must do two things before updating your order:

1. **Re-verify the hash** in the callback parameters to confirm the response has not been tampered with.
2. **Call the Verify Payment API** to independently confirm the transaction status directly from PayU's servers.

Skipping this step is a security risk. A fraudulent actor could forge a success callback and claim a payment was completed when it was not. Server-side verification is the only reliable way to confirm a payment.
</AccordionOpen>

<AccordionOpen title="Step 8 — Your backend redirects the customer to the result page">

Once the payment status is confirmed server-side, your backend sends an HTTP redirect to the customer's browser — to your success page if the payment went through, or to your failure page if it did not.

The customer sees the final outcome on a page you control, giving you full flexibility over the post-payment experience: order confirmation, download links, error messages, or retry options.
</AccordionOpen>

***

## PCI-DSS Scope

The PCI-DSS (Payment Card Industry Data Security Standard) scope is one of the most important architectural considerations for Merchant Hosted Checkout card integrations.

### **Why are You in Scope?**&#x20;

Your website collects raw card numbers and CVV directly from the customer in your own HTML form. Because cardholder data passes through your browser and backend, your infrastructure is in PCI-DSS scope.

### **What This Means in Practice?**

- HTTPS is required on all pages of your checkout — not just the payment page
- CVV must never be stored — not in databases, logs, or caches
- Card numbers must not be stored without tokenization
- Your servers must meet PCI-DSS requirements or use a compliant hosting provider
- You must complete the [PCI-DSS SAQ A-EP](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf) assessment

### **PCI Scope for Other Payment Methods**

Wallets, UPI, and Net Banking integrations do not involve raw card data — your PCI-DSS obligations for those methods are significantly reduced.

<Callout icon="ℹ️" theme="info">
  ### **Tips:**

  If reducing PCI-DSS scope is a priority, consider [Checkout Plus](../checkout-plus-integration) — card data is collected in PayU's Bolt-hosted fields, keeping your servers out of PCI scope.
</Callout>

***

## Merchant Hosted Checkout vs Other Checkout Products

| Feature                   | PayU Hosted Checkout             | Checkout Plus (Bolt SDK)              | Merchant Hosted Checkout            |
| ------------------------- | -------------------------------- | ------------------------------------- | ----------------------------------- |
| Payment UI                | Hosted by PayU                   | PayU modal on your site               | Built entirely by you               |
| PayU branding visible     | Yes                              | Partial (modal)                       | No                                  |
| Redirect to PayU page     | Yes                              | No                                    | No (except bank auth)               |
| PCI-DSS scope for cards   | Low — PayU collects card data    | Low — PayU's Bolt fields collect data | High — your form collects card data |
| Integration complexity    | Low                              | Medium                                | High                                |
| Per-method setup required | No                               | No                                    | Yes                                 |
| Full brand control        | No                               | Partial                               | Yes                                 |
| Mobile WebView support    | Yes                              | Yes (with workaround)                 | Yes                                 |
| Suitable for              | Low-integration-effort merchants | Brand-conscious web merchants         | Enterprise / high-customization     |

***

## BIN Validation (Cards)

For card integrations, you can optionally call the `getBinInfo` API before submitting the payment. This returns card type (credit/debit), issuing bank, card network, and EMI eligibility for the BIN (first 6 digits of the card number). This is used to:

- Display the correct card network logo
- Show EMI options for eligible cards
- Confirm accepted card types before the customer submits

See [Build Integration — Cards](./integration-guide/build-integration/cards) for the full BIN validation flow.

***

## Callback URLs

PayU POSTs the payment response to your `surl` (success URL) or `furl` (failure URL). Both URLs must:

- Be publicly reachable over HTTPS in production
- Accept POST requests
- Return a 200 HTTP status after processing

<Callout icon="far fa-circle-info" theme="info">
  ### **Tips:**

  Implement a webhook handler as a fallback. If the customer closes the browser before the redirect completes, your `surl`/`furl` may not receive the callback. Configure PayU webhooks in the Dashboard to receive server-to-server notifications as a backup.
</Callout>

***

## Responsibilities

<Accordion title="What Does PayU Handle?" icon="fa-server">
  - **Payment processing** — PayU receives the form POST to `_payment` and processes the transaction with the bank, card network, UPI provider, or wallet.
  - **Authentication** — PayU sends the customer to the bank ACS, net banking login, wallet, or UPI step when that method requires it.
  - **Returning the result** — PayU posts the payment outcome to your `surl` or `furl` and redirects the customer's browser back to your site.
</Accordion>

<Accordion title="What Does Your Application Handle?" icon="fa-code">
  - **The payment form** — Your website collects the payment details. For cards, that includes the card number, expiry, and CVV. You choose the method with `pg` and `bankcode`.
  - **Securing the request** — Your server generates the SHA-512 hash. The salt stays on the server.
  - **Posting the payment** — The browser posts the form to `_payment` with the parameters and the hash.
  - **Receiving the payment result** — Your `surl` and `furl` accept the POST PayU sends after the transaction.
  - **Verifying the result** — Your server checks the reverse hash, then confirms the payment with the Verify Payment API. The browser redirect alone is not enough.
  - **Updating order state** — After verification, your application marks the order from the PayU status.
</Accordion>

***

## Key Concepts

| Concept      | Definition                                                                                                  |
| ------------ | ----------------------------------------------------------------------------------------------------------- |
| `_payment`   | PayU's payment processing endpoint. All MHC payments POST here.                                             |
| `pg`         | Payment gateway parameter. Specifies the payment method type (`CC`, `NB`, `UPI`, `CASH`, `PAYPAL`, `MC`).   |
| `bankcode`   | Bank or provider code within a payment method type.                                                         |
| `hash`       | SHA-512 signature computed from transaction parameters. Required on all requests.                           |
| `txnid`      | Your unique transaction identifier. Must be unique per transaction.                                         |
| `surl`       | Success URL — PayU redirects here after a successful payment.                                               |
| `furl`       | Failure URL — PayU redirects here after a failed or cancelled payment.                                      |
| `mihpayid`   | PayU's unique transaction reference, returned in the callback. Use this for refunds and support queries.    |
| Reverse hash | Hash computed from the callback response to verify PayU sent it. Formula is reversed from the request hash. |
| BIN          | First 6 digits of a card number. Used to identify card type, network, and issuing bank.                     |

***

## Next Steps

<Cards columns="2">
  <Card title="Merchant Hosted Checkout" icon="fab fa-readme">
    Go through and understand the Merchant Hosted Checkout.
  </Card>

  <Card title="Quick Start" href="./quick-start" icon="fa-play">
    Make your first test card payment in minutes — hash generation, form POST, and callback handling.
  </Card>

  <Card title="APIs" href="./merchant-hosted-checkout-apis" icon="fa-rectangle-api">
    API reference index for \_payment, Verify Payment, and transaction management.
  </Card>
</Cards>

/accor
