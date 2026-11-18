---
title: FAQs (Frequently Asked Questions)
excerpt: >-
  Questions about Merchant Hosted Checkout: setup, hash, callbacks, PCI-DSS,
  and going live.
deprecated: false
hidden: true
metadata:
  title: Merchant Hosted Checkout FAQs
  description: >-
    FAQs for PayU Merchant Hosted Checkout: pg and bankcode, SHA-512 hash,
    surl and furl, PCI-DSS SAQ A-EP, and the production endpoint.
  keywords:
    - payu merchant hosted faq
    - payu custom checkout pci
    - payu hash faq merchant hosted
  robots: index
next:
  description: Explore related information and resources.
---
## Getting Started

1. #### What is Merchant Hosted Checkout?

<Accordion title="Answer" icon="fa-circle-question">
  You collect payment details on your website and form-post them to PayU. You choose the method with `pg` and `bankcode`. PayU processes the payment and redirects the customer to your `surl` or `furl`.
</Accordion>

2. #### What are the minimum prerequisites?

<Accordion title="Answer" icon="fa-circle-question">
  - A PayU merchant account
  - Test key and salt, then the live key and salt
  - A server that generates SHA-512
  - HTTPS callback URLs
  - PCI-DSS SAQ A-EP if you collect card data
</Accordion>

3. #### What payment methods are supported?

<Accordion title="Answer" icon="fa-circle-question">
  This guide has steps for cards (`pg=CC`), net banking, wallets (`pg=CASH`), UPI Collect (`pg=UPI`, `bankcode=UPI`), PayPal (`pg=PAYPAL`, `bankcode=PAYPAL`), and Pluxee (`pg=MC`, `bankcode=SODEXO`). EMI, BNPL, EFTNET, and Net Banking TPV stay on their existing guides.
</Accordion>

4. #### Do I need PCI-DSS?

<Accordion title="Answer" icon="fa-circle-question">
  Yes, if you store, process, or transmit cardholder data. The source names SAQ A-EP. Card details are entered on your site. UPI and wallet only still require a secure site.
</Accordion>

***

## Integration Setup

1. #### What are surl and furl?

<Accordion title="Answer" icon="fa-circle-question">
  On the cards, UPI Collect, PayPal, and Pluxee pages, `surl` is the success URL and `furl` is the failure URL.

  <!-- VALIDATION NEEDED: The net banking and wallets tables swap those descriptions. -->
</Accordion>

2. #### Where do I post the payment?

<Accordion title="Answer" icon="fa-circle-question">
  Test: `POST https://test.payu.in/_payment`. Production: `POST https://secure.payu.in/_payment`. Use `method="post"`.
</Accordion>

3. #### How do I choose a payment method?

<Accordion title="Answer" icon="fa-circle-question">
  Send `pg` and `bankcode`. Bank codes are case-sensitive. The method must be enabled on your PayU account. PayPal is activated from the Dashboard.
</Accordion>

***

## Hash Generation

1. #### Where do I generate the hash?

<Accordion title="Answer" icon="fa-circle-question">
  On the server. The salt stays on the server.
</Accordion>

2. #### What is the request hash formula?

<Accordion title="Answer" icon="fa-circle-question">
  The method pages use `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)`.

  <!-- VALIDATION NEEDED: The legacy overview also shows a formula with no UDF fields. -->
</Accordion>

***

## Checkout Experience

1. #### Does PayU show its own payment page?

<Accordion title="Answer" icon="fa-circle-question">
  No. The customer enters details on your page. PayU may still send them to a bank ACS, net banking login, wallet, or UPI step, then back to your site.
</Accordion>

***

## Testing

1. #### Which test values can I use?

<Accordion title="Answer" icon="fa-circle-question">
  Net banking: username `payu`, password `payu`, OTP `123456`. UPI: `anything@payu` or `9999999999@payu.in`. Paytm: mobile `7777777777`, OTP `888888`. Use the test key and salt only.
</Accordion>

***

## Reverse Hashing

1. #### What is the reverse hash order?

<Accordion title="Answer" icon="fa-circle-question">
  `sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)`. Compare it with the `hash` in the callback before you fulfil the order.
</Accordion>

***

## Callback vs Webhook

1. #### How is surl/furl different from webhooks?

<Accordion title="Answer" icon="fa-circle-question">
  `surl` and `furl` are the browser redirects. The production checklist says to use webhooks if the callback fails, and to confirm status with Verify Payment. Webhook event names are not in this folder.
</Accordion>

***

## Duplicate Processing

1. #### Can I reuse a txnid?

<Accordion title="Answer" icon="fa-circle-question">
  No. The saved-card text says PayU will not accept a duplicate transaction id. Use a new `txnid` and a new hash for another attempt.
</Accordion>

***

## Refunds & Cancellations

1. #### How do I refund?

<Accordion title="Answer" icon="fa-circle-question">
  Use the Dashboard or `command=cancel_refund_transaction`. The PayPal page says the PayPal account needs sufficient funds before a refund.
</Accordion>

***

## Taxation, Compliance & Identity Verification

1. #### What compliance does the source name?

<Accordion title="Answer" icon="fa-circle-question">
  PCI-DSS SAQ A-EP when you handle cardholder data. The cards page also says guest checkout with a plain card number was not allowed after 31 Oct 2023, and that the replacement is an Alt ID. International cards must be enabled by writing to integration@pay.in.
</Accordion>

***

## Advanced Features & Payment Methods

1. #### What are the UPI Collect limits?

<Accordion title="Answer" icon="fa-circle-question">
  UPI Collect is allowed only for MCC 6012 and 6211. Web and Android must move to UPI Intent S2S. Seamless form POST does not support Intent. iOS may keep a deeplink and UPI Collect.
</Accordion>

***

## Chargebacks & Dispute Resolution

1. #### What does the source say about chargebacks?

<Accordion title="Answer" icon="fa-circle-question">
  `email`, `phone`, and `address1` are described as useful for fraud detection and chargebacks. A dispute workflow is not in this folder.
</Accordion>

***

## Production Go-Live

1. #### What is the production endpoint and where is the live salt?

<Accordion title="Answer" icon="fa-circle-question">
  Post to `https://secure.payu.in/_payment`. In the Dashboard, switch to Live Mode and open **Payment Gateway → Web Integration → Key Salt Details**.
</Accordion>
