---
title: Go-Live Checklist
excerpt: Switch to the live key, salt, and production endpoint before you accept real payments
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Merchant Hosted Checkout Go-Live Checklist | PayU Developer Docs
  description: >-
    Go-live checklist for PayU Merchant Hosted Checkout. Switch the key, salt, and endpoint, verify hashes and callbacks, and confirm each payment method.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Go-Live Checklist

Complete this checklist before you accept live payments.

<Accordion title="Update credentials" icon="fa-key">
  Replace the test key and salt with the production key and salt.

  1. Log in to the PayU Dashboard and switch to Live Mode.
  2. Open **Payment Gateway → Web Integration → Key Salt Details**.
  3. Copy the key and salt.
  4. Replace the test key and test salt in the payment integration.
</Accordion>

<Accordion title="Switch the endpoint" icon="fa-server">
  The production checklist states the production environment as [https://secure.payu.in/](https://secure.payu.in/). Method guides post payments to `https://secure.payu.in/_payment`.

  The API index states the production post-service URL as `POST https://info.payu.in/merchant/postservice.php?form=2`. The cards BIN guide states production as `https://info.payu.in/merchant/postservice?form=2`.

  <!-- VALIDATION NEEDED: postservice versus postservice.php. See How It Works. -->
</Accordion>

<Accordion title="Security" icon="fa-shield-halved">
  Generate the hash on the server. Keep the salt off the frontend. Serve the site over HTTPS. Do not store the CVV or the full card number.

  If you store, process, or transmit cardholder data, complete PCI-DSS SAQ A-EP. That applies when card or Pluxee details are collected on your site. Pluxee also forbids storing the full card number, expiry, or CVV.
</Accordion>

<Accordion title="Callback URLs" icon="fa-link">
  Receive the PayU response on `surl` and `furl`. Verify the reverse hash so the callback is not tampered with. If the callback fails, confirm the transaction on the server. The checklist says to use webhooks for that path. See [Webhooks](doc:webhooks) and [Verify Payment API](ref:verify_payment_api).
</Accordion>

<Accordion title="Error handling" icon="fa-triangle-exclamation">
  Confirm every transaction with `verify_payment`. The checklist says not to rely on the callback alone when it fails.
</Accordion>

<Accordion title="Payment method coverage" icon="fa-credit-card">
  Test each method you will offer in production. Activate PayPal in the Dashboard before you use it. International cards are enabled by the PayU Integration Team at integration@pay.in.
</Accordion>

<Accordion title="PayU Dashboard access" icon="fa-gauge">
  Confirm you can open Live Mode and copy the key and salt from **Payment Gateway → Web Integration → Key Salt Details**. Confirm PayPal is activated if you use it.

  <!-- DOCUMENTATION GAP: This folder does not document settlement screens or the webhook subscription screen. -->
</Accordion>

<Accordion title="Final checkout verification" icon="fa-list-check">
  The production checklist asks you to confirm all of the following:

  1. Required checkout details are collected on your website and validated. See [Submitting Payment Request on your Website](doc:submitting-payment-request-on-your-website) and [Working with Response after a Customer Checkout](doc:working-with-response-after-a-customer-checkout).
  2. The response from PayU is verified. See [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted).
  3. The callback reverse hash shows the response was not tampered with. See [Hashing Request and Response](doc:generate-hash-merchant-hosted).
  4. The transaction status is confirmed on the server if the callback fails, using webhooks and [Verify Payment API](ref:verify_payment_api).
  5. The integration points at the production endpoint.
</Accordion>
