---
title: How Merchant Hosted Checkout Works
excerpt: >-
  Understand the payment journey. From your checkout to PayU and back,
  including the bank step, the callback, and verification.
deprecated: false
hidden: false
next:
  pages: []
metadata:
  title: How Merchant Hosted Checkout Works
  description: >-
    Step-by-step Merchant Hosted Checkout flow: collect details, form POST to
    _payment, bank authentication, surl/furl response, and verification.
  keywords:
    - how payu merchant hosted checkout works
    - payu custom checkout payment flow
    - payu _payment form post flow
    - payu surl furl merchant hosted
  robots: index
---
Merchant Hosted Checkout collects payment details on your website and form-posts them to PayU. PayU processes the payment, sends the customer to the bank, wallet, or UPI step when that method requires it, and posts the result back to your callback URL.

***

## How Does the Payment Flow Work?


<Image src="https://files.readme.io/4aeeafdbefc392fa362522d8209dc7268178e104e699b067895a3408ff412c42-merchant_hosted_flow.png" alt="Merchant Hosted Checkout payment flow" align="center" border={true} />


The payment moves through six stages:<br />

1. **Initiation**: The customer proceeds to pay on your website. Your checkout collects the payment details for the method they chose.
2. **Form post**: The browser posts the payment to PayU at `_payment`, including `pg`, `bankcode`, and the hash your server generated.
3. **Payment details**: The customer has already entered the details on your page. PayU does not ask them to pick a method on a PayU-hosted page.
4. **Authentication**: The customer may complete the bank ACS OTP, a net banking login, a wallet redirect, or a UPI collect request.
5. **Processing**: PayU sends the transaction to the bank, card network, or payment provider and receives the result.
6. **Return**: PayU redirects the customer to your `surl` or `furl` and posts the payment result.

***

## What Happens After the Payment?

After the transaction completes, PayU returns the outcome to your application:<br />

| Outcome | Callback | What the source shows |
| --- | --- | --- |
| **Success** | `surl` | Samples show `status=success`, `unmappedstatus=captured`, `error=E000` |
| **Failure** | `furl` | The cards failure sample shows `status=failure`, `error=E1903` |
| **Pending** | <!-- DOCUMENTATION GAP: The test steps say to simulate pending. They do not say which URL receives it or what status value to expect. --> | Not defined in this folder |
| **Cancelled** | <!-- DOCUMENTATION GAP: A cancelled outcome is not described in the Merchant Hosted pages. --> | Not defined in this folder |

<!-- VALIDATION NEEDED: Cards, UPI Collect, PayPal, and Pluxee describe surl as success and furl as failure. The net banking and wallets parameter tables swap those descriptions. -->

The payment result arrives at your application in two ways described in the source:<br />

- **Browser redirect**: PayU redirects the customer's browser to your `surl` or `furl` and posts the result.
- **Webhook**: The production checklist says to use webhooks to hear callbacks if the browser callback fails. Event names are not listed in this folder.<br />

Your application should verify the reverse hash and call Verify Payment before treating the payment as confirmed.<br />

For implementation details, see [Build the Integration](./integration-guide/build-integration).

***

## Responsibilities

<Accordion title="What Does PayU Handle?" icon="fa-server">
  - **Payment processing** — PayU sends the transaction to the bank, card network, UPI provider, or wallet.
  - **Authentication handoff** — For cards, the customer is taken to the bank ACS page. Net banking goes to the bank login. Wallets, UPI, PayPal, and Pluxee follow that method's flow.
  - **Returning the result** — PayU posts the outcome to your callback URL and redirects the customer's browser back to your site.
</Accordion>

<Accordion title="What Does Your Application Handle?" icon="fa-code">
  - **The payment form** — You collect the payment details, including card fields when the customer pays by card.
  - **Choosing the method** — You send `pg` and `bankcode`.
  - **Securing the request** — You generate the SHA-512 hash on the server. The salt never goes to the browser.
  - **Receiving the payment result** — You expose `surl` and `furl`.
  - **Verifying the result** — You check the reverse hash and call `verify_payment` before you fulfil the order.
</Accordion>

***

## Key Concepts

<Accordion title="Transaction" icon="fa-exchange-alt">
  A single payment attempt. You assign `txnid`. The saved-card parameter text says PayU will not accept a duplicate transaction id.
</Accordion>

<Accordion title="Payment Request" icon="fa-file-alt">
  The form post to `_payment`: amount, customer details, `pg`, `bankcode`, method fields, `surl`, `furl`, and the hash.
</Accordion>

<Accordion title="Form Post" icon="fa-arrows-alt-h">
  The browser posts the payment from your page to PayU. Test URL: `https://test.payu.in/_payment`. Production URL: `https://secure.payu.in/_payment`.
</Accordion>

<Accordion title="surl / furl" icon="fa-link">
  `surl` is the success URL. `furl` is the failure URL, on the cards, UPI Collect, PayPal, and Pluxee pages. PayU posts the result to the URL it redirects to.
</Accordion>

<Accordion title="Payment Response" icon="fa-reply-all">
  The fields PayU posts back. Samples include `mihpayid`, `status`, `txnid`, `amount`, `mode`, `bankcode`, `hash`, `error`, and `error_Message`.
</Accordion>

***

## Next Steps

- [Quick Start:](./quick-start) Run your first net banking test payment.
- [Build the Integration:](./integration-guide/build-integration) Parameters, hash, form post, reverse hash, and Verify Payment for each method.
