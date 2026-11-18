---
title: Go-Live Checklist
excerpt: Switch Merchant Hosted Checkout from test credentials to production
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Merchant Hosted Checkout Go-Live Checklist | PayU Developer Docs
  description: >-
    Go-live checklist for PayU Merchant Hosted Checkout: production key and salt, secure.payu.in, server-side hash, callbacks, and verify payment.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Go-Live Checklist

Complete this before you accept live payments.

<Accordion title="Update credentials" icon="fa-key">
  Replace the test key and salt with the production key and salt.

  1. Log in to the PayU Dashboard and switch to Live Mode.
  2. Open **Payment Gateway → Web Integration → Key Salt Details**.
  3. Copy the key and salt.
  4. Replace the test values in your integration code.

  The legacy checklist says the production environment endpoint is [https://secure.payu.in/](https://secure.payu.in/). The method pages post to `https://secure.payu.in/_payment`.
</Accordion>

<Accordion title="Security" icon="fa-shield-halved">
  Generate the hash on the server. Do not put the salt in the browser. Use HTTPS. Do not store the CVV, and do not store the full card number.

  If you store, process, or transmit cardholder data, the source says you must complete PCI-DSS SAQ A-EP. Card collection on your site is in that scope.
</Accordion>

<Accordion title="Callback URLs" icon="fa-link">
  Confirm PayU can redirect to your `surl` and `furl`. The legacy checklist says to verify the response, confirm the reverse hash has not been tampered with, and confirm the transaction on the server if the callback fails. It says to use webhooks to hear callbacks. Webhook event names are not listed in this folder. See [Webhooks](https://docs.payu.in/docs/webhooks) and [Verify Payment](https://docs.payu.in/reference/verify_payment_api).
</Accordion>

<Accordion title="Error handling" icon="fa-triangle-exclamation">
  Do not fulfil an order from the browser callback alone. Call `verify_payment` on the server. The legacy overview also lists incorrect hash, invalid key or salt for the environment, a payment method that is not enabled, and webhook processing errors.

  <!-- DOCUMENTATION GAP: This folder does not define a pending status or say whether a pending callback may be fulfilled. -->
</Accordion>

<Accordion title="Payment method coverage" icon="fa-credit-card">
  Test every method you will enable. The legacy test steps say to test successful, failed, and pending transactions, to verify webhooks, and to test each payment method. Advantage Club has no sandbox in the source. Test that wallet on production.
</Accordion>

<Accordion title="PayU Dashboard access" icon="fa-gauge">
  Confirm you can open the Dashboard in Live Mode and read **Payment Gateway → Web Integration → Key Salt Details**.

  <!-- DOCUMENTATION GAP: Settlement screens, reporting configuration, and the webhook subscription click-path are not in the Merchant Hosted source. The checklist only says to enable webhooks and to monitor transactions in the first days after go-live. -->
</Accordion>

<Accordion title="Final verification" icon="fa-list-check">
  The legacy production checklist asks you to confirm that:

  - The required checkout fields are collected on your site and validated.
  - The PayU response is verified. It points to Collect Payment API — Merchant Hosted Checkout.
  - The callback reverse hash shows the response was not tampered with. It points to Hashing Request and Response.
  - The integration posts to the production endpoint.
</Accordion>
