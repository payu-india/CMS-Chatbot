---
title: FAQs — Merchant Hosted Checkout
excerpt: Answers drawn from the Merchant Hosted Checkout source, with gaps marked where the source is silent
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Merchant Hosted Checkout FAQs | PayU Developer Docs
  description: >-
    FAQs for PayU Merchant Hosted Checkout: difference from PayU Hosted, PCI-DSS, server-side hash, production endpoint, and UPI Collect limits.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# FAQs — Merchant Hosted Checkout

<Accordion title="How does Merchant Hosted Checkout differ from PayU Hosted Checkout?" icon="fa-circle-question">
  Merchant Hosted Checkout collects the payment details on your site and form-posts them to `_payment` with `pg` and `bankcode`. PayU Hosted Checkout sends the customer to a PayU payment page, and PayU collects the payment details there. Use PayU Hosted Checkout when you do not want to build the payment form.
</Accordion>

<Accordion title="Do I need PCI-DSS compliance?" icon="fa-shield-halved">
  Yes, if you store, process, or transmit cardholder data. The source names SAQ A-EP. It also says that Merchant Hosted Checkout collects card details on your website, so that collection is in scope. If you use only UPI and wallets, the source says the website must still be secure. It does not say those modes remove PCI scope for cards you also accept.
</Accordion>

<Accordion title="Should I generate the hash on the frontend or the backend?" icon="fa-code">
  Generate it on the server. The salt is a secret known to you and PayU. The source does not describe a frontend hash as a valid option.
</Accordion>

<Accordion title="How do I handle the pending status?" icon="fa-clock">
  <!-- DOCUMENTATION GAP: The test steps say to simulate pending transactions. They do not define the status value or the fulfilment rule. -->
</Accordion>

<Accordion title="What happens if the customer closes the browser before the redirect?" icon="fa-window-maximize">
  <!-- DOCUMENTATION GAP: The source does not describe this case. The production checklist says to confirm the transaction on the server if the callback fails, and to use webhooks. It does not give a timeout. -->
</Accordion>

<Accordion title="How is surl/furl different from webhooks?" icon="fa-plug">
  `surl` and `furl` are the URLs PayU redirects the customer's browser to, with the payment response. The production checklist says to use webhooks to hear callbacks when you confirm status on the server after a callback failure. Webhook event names are not in this folder.

  <!-- DOCUMENTATION GAP: The source does not compare reliability of surl/furl and webhooks beyond that instruction. -->
</Accordion>

<Accordion title="How do I enable specific payment methods?" icon="fa-toggle-on">
  The legacy overview says the methods you support must be enabled on your PayU merchant account. PayPal must be activated from the PayU Dashboard. The source does not give a click-path for other methods.
</Accordion>

<Accordion title="What is the production endpoint?" icon="fa-server">
  `POST https://secure.payu.in/_payment`.

  The production checklist also writes the production environment as `https://secure.payu.in/`.

  Post-service production is written two ways in the source: `https://info.payu.in/merchant/postservice?form=2` and `https://info.payu.in/merchant/postservice.php?form=2`.

  <!-- VALIDATION NEEDED: Confirm which post-service path is current before you hard-code it. -->
</Accordion>

<Accordion title="How do I debug a hash mismatch?" icon="fa-bug">
  Check the field order. The method pages use `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)`. A second sample on the legacy overview drops the UDF fields. Use the same values in the hash and in the form post, including empty UDF positions.
</Accordion>

<Accordion title="Can I use UPI Collect on the web?" icon="fa-mobile-screen">
  The source says UPI Collect is allowed only for MCC 6012 and 6211. For web, it says to use the UPI Intent S2S deeplink and render that deeplink as a QR, instead of UPI Collect. Seamless form POST does not support Intent. Android must use Smart Intent. iOS may keep a deeplink and UPI Collect.
</Accordion>

<Accordion title="What is bankcode for each method?" icon="fa-list">
  | Method | pg | bankcode |
  | --- | --- | --- |
  | Cards | CC | Network-specific. Samples use CC, MAST, AMEX, VISA, and MASTERCARD |
  | Net banking | NB in the parameter text. Samples use TESTPG | Bank-specific. Test sample is TESTPGNB |
  | Wallets | CASH. Advantage Club uses RD | Wallet-specific. Paytm sample PAYTM. Advantage Club ADVCLUB |
  | UPI Collect | UPI | UPI |
  | PayPal | PAYPAL | PAYPAL. The overview table says N/A |
  | Pluxee | MC | SODEXO |

  <!-- VALIDATION NEEDED: Do not treat the conflicting pg and bankcode values as settled. They are copied from the legacy pages and flagged on the method pages. -->
</Accordion>
