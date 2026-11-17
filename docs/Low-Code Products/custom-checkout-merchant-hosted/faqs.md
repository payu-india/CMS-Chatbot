---
title: FAQs — Merchant Hosted Checkout
excerpt: Answers drawn from the Merchant Hosted Checkout guides for hash, PCI, UPI Collect, and callbacks
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Merchant Hosted Checkout FAQs | PayU Developer Docs
  description: >-
    FAQs for PayU Merchant Hosted Checkout. PCI-DSS scope, where to generate the hash, the production endpoint, UPI Collect limits, and Pluxee card storage.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# FAQs — Merchant Hosted Checkout

<!-- NEW CONTENT: This folder had no FAQ page. Answers below use only statements already in the Merchant Hosted guides. -->

<Accordion title="How does Merchant Hosted Checkout differ from a PayU-hosted page?" icon="fa-circle-question">
  Merchant Hosted Checkout collects payment details on your website and form-POSTs them to PayU. PayU processes the payment and redirects the customer to your `surl` or `furl`. The overview calls this a defined PayU product with its own APIs.

  PayPal is the method the source explicitly says can run on PayU Hosted Checkout or on Merchant Hosted Checkout. For Merchant Hosted, post `pg=PAYPAL` and `bankcode=PAYPAL` after you activate PayPal in the Dashboard.
</Accordion>

<Accordion title="Do I need PCI-DSS compliance?" icon="fa-shield-halved">
  Yes, if you store, process, or transmit cardholder data. The overview and the cards guide name the SAQ A-EP form. Collecting card details on your site for this product puts you in that scope. Pluxee card numbers are also handled under PCI-DSS, and you must not store the full number, expiry, or CVV.

  If you use only UPI and wallets, the overview still says the site must be secure. It does not say those modes remove the need for HTTPS.
</Accordion>

<Accordion title="Should I generate the hash on the frontend or the backend?" icon="fa-code">
  The salt is a secret known only to you and PayU. The hash is SHA-512 of the payment fields plus that salt. Request samples put a finished `hash` in the browser form. They do not put the salt in the form.

  <!-- NEW CONTENT: The guides do not use the words "frontend" or "backend". The salt definition and the form samples are the basis for generating the hash where the salt is stored. -->
</Accordion>

<Accordion title="How do I handle a pending status?" icon="fa-clock">
  <!-- DOCUMENTATION GAP: The overview says to test pending transactions. It does not say what pending means or how to update the order. -->
</Accordion>

<Accordion title="What if the customer never returns to surl or furl?" icon="fa-browser">
  The production checklist says to confirm the transaction on the server if the callback fails, and to use webhooks for that path. Call `verify_payment` with the `txnid`.

  <!-- DOCUMENTATION GAP: There is no separate description of the customer closing the browser. -->
</Accordion>

<Accordion title="How is surl or furl different from webhooks?" icon="fa-plug">
  `surl` and `furl` are the URLs PayU redirects the browser to, with the payment result posted to them. The checklist describes webhooks as the way to hear the result when that callback fails. See [Webhooks](doc:webhooks).

  <!-- DOCUMENTATION GAP: This folder does not rank which channel is more reliable beyond that checklist instruction. -->
</Accordion>

<Accordion title="How do I enable a payment method?" icon="fa-toggle-on">
  Enable the method on your PayU merchant account. `bankcode` values are case-sensitive. Activate PayPal from the PayU Dashboard. International cards are enabled by writing to integration@pay.in. Guest checkout is enabled through your PayU Key Account Manager or PayU Integration Support.
</Accordion>

<Accordion title="What is the production endpoint?" icon="fa-server">
  Post payments to `https://secure.payu.in/_payment`. The production checklist also gives the production base as `https://secure.payu.in/`.

  Post-service production URLs in this folder are `https://info.payu.in/merchant/postservice?form=2` (cards BIN) and `https://info.payu.in/merchant/postservice.php?form=2` (API index). See [How It Works](./how-it-works).
</Accordion>

<Accordion title="How do I debug a hash mismatch?" icon="fa-bug">
  Rebuild the string in this order and hash it with SHA-512:

  ```
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||Salt)
  ```

  Keep empty `udf` values empty so the pipes remain. Use the salt for the same environment as the key. The overview's other troubleshooting checks are invalid key or salt, a method that is not enabled, and webhook logs.

  <!-- DOCUMENTATION GAP: No hash-mismatch error code is named in this folder. -->
</Accordion>

<Accordion title="Can I use UPI Collect on the web?" icon="fa-mobile-screen">
  UPI Collect is allowed only for MCC 6012 and 6211. The UPI page says web merchants must use the UPI Intent S2S deeplink and show it as a QR. Android uses Smart Intent. iOS can continue with UPI Collect using a deeplink. Seamless form POST must migrate to `txn_s2s_flow` because Intent is not supported there for Android and desktop web.
</Accordion>

<Accordion title="Can I store a Pluxee card?" icon="fa-wallet">
  You must not store the full card number, expiry, or CVV. If the customer agrees to save the card, post `save_sodexo_card=1`. PayU returns the sourceId in `field3`. Later payments send that value as `source_id` and do not send the card fields.
</Accordion>
