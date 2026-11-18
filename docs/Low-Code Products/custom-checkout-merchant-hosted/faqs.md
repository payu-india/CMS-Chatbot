---
title: FAQs — Merchant Hosted Checkout
excerpt: Answers that the Merchant Hosted source supports, and the questions it does not
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: FAQs — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    FAQs for PayU Merchant Hosted Checkout: PCI-DSS, where to hash, the production URL, UPI Collect limits, and what to do when the callback fails. Read on.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# FAQs — Merchant Hosted Checkout

<Accordion title="How is this different from PayU Hosted Checkout?" icon="fa-circle-question">
  Merchant Hosted Checkout collects the payment details on your site and posts them to `_payment`. The source distinguishes this from a prebuilt PayU payment page. The current overview's own meta description still describes that prebuilt page. The body of the overview does not.

  <!-- DOCUMENTATION GAP: This folder has no fuller comparison of the two products. -->
</Accordion>

<Accordion title="Do I need PCI-DSS compliance?" icon="fa-shield-halved">
  Yes, if you store, process, or transmit cardholder data. The source names the Self-Assessment Questionnaire A-EP. It also says that because you collect card details on your site, you must be PCI-DSS compliant.

  If you use only UPI and wallets, the source does not repeat SAQ A-EP. It says to keep the website secure. That is not a statement that PCI never applies.
</Accordion>

<Accordion title="Where do I generate the hash?" icon="fa-code">
  On the server. The cards cURL comment says the call is server-side and must not be executed in the browser. The salt stays on the server. The method-page formula is `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||Salt)`.
</Accordion>

<Accordion title="What is the production endpoint?" icon="fa-server">
  The method pages use `POST https://secure.payu.in/_payment`.

  <!-- VALIDATION NEEDED: The production checklist writes https://secure.payu.in/ without _payment. -->
</Accordion>

<Accordion title="How do I debug a hash mismatch?" icon="fa-bug">
  Recheck the parameter order against the method-page formula, including the empty `udf` pipes. The overview also contains a shorter Python string. A mismatch can come from mixing the two.

  <!-- DOCUMENTATION GAP: No hash-mismatch error code is in this folder. -->
</Accordion>

<Accordion title="How do I enable a payment method?" icon="fa-toggle-on">
  The method has to be enabled on the merchant account. PayPal is activated from the PayU Dashboard. International cards are enabled by writing to integration@pay.in, which is the address on the cards page.
</Accordion>

<Accordion title="What if the callback does not arrive?" icon="fa-plug">
  Confirm the transaction with Verify Payment. The source says to use webhooks when the callback fails.

  <!-- DOCUMENTATION GAP: Webhook event names are not listed in this folder. -->
</Accordion>

<Accordion title="Can I use UPI Collect on the web?" icon="fa-mobile-screen">
  The source says UPI Collect is allowed only for MCC 6012 and 6211. For web, the NPCI note says to build a QR from the UPI Intent deeplink instead of Collect. Seamless form post must move to UPI Intent S2S for Android and desktop web. iOS can keep Collect with a deeplink.
</Accordion>

<Accordion title="Why does UPI Intent fail in test mode?" icon="fa-flask">
  The test page says the UPI in-app flow and the UPI intent flow are not available in test mode.
</Accordion>

<Accordion title="Does Advantage Club have a sandbox?" icon="fa-wallet">
  No. The wallets page says there are no test credentials and no test environment, and that you test Advantage Club on production.
</Accordion>
