---
title: FAQs — Checkout Plus
excerpt: Short answers from the Checkout Plus pages, including the open questions
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Checkout Plus FAQs | PayU Developer Docs
  description: >-
    Answers on Checkout Plus versus PayU Hosted Checkout, PCI-DSS, pending
    status, payment methods, the production Bolt script, and using an in-app WebView.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Accordion title="How is Checkout Plus different from PayU Hosted Checkout?" icon="fa-circle-question">

Checkout Plus opens the payment experience as a modal on your page through `bolt.launch()`. It is only available for PayU Hosted Checkout. The API page says the modal collects payment through the hosted `_payment` flow.

PayU Hosted Checkout is the redirection integration. Use it when the customer should leave your page, including inside an app WebView. The Checkout Plus integrate page says the Bolt integration is not recommended for WebView or Chrome Custom Tabs.

</Accordion>

<Accordion title="Do I need PCI-DSS compliance?" icon="fa-shield-halved">

The overview says the modal is served from PayU, so you do not have to take on PCI-DSS compliance for collecting payment details on your site.

<!-- DOCUMENTATION GAP: No SAQ type is stated. -->

</Accordion>

<Accordion title="Should I generate the hash on the frontend or the backend?" icon="fa-code">

<!-- DOCUMENTATION GAP: The Checkout Plus pages do not say where to generate the hash. They mark hash as mandatory and link to https://docs.payu.in/docs/generate-hash-merchant-hosted. A wizard and an Ask AI note outside this product say to generate it on the backend. That is not stated in the product pages, so this answer is intentionally unanswered. -->

</Accordion>

<Accordion title="How do I handle pending?" icon="fa-clock">

The response table says possible `status` values are `success`, `failure`, and `pending`. It then says that if status is `failure` or `pending`, treat the transaction as failed.

<!-- VALIDATION NEEDED: Confirm this pending rule. Other PayU guides say pending is not a final failure and must be verified before you fulfil or cancel the order. -->

</Accordion>

<Accordion title="What if the customer closes the modal?" icon="fa-window-restore">

The handler sample checks `txnStatus` `CANCEL` and logs a retry message. The pages do not describe what happens if the customer closes the browser.

</Accordion>

<Accordion title="How is surl/furl different from responseHandler?" icon="fa-link">

Both exist in the product pages. `responseHandler` is the function Bolt calls on your page. `surl` and `furl` are mandatory URLs described as the place PayU redirects the final response, and the customer journey says the result page depends on them.

<!-- DOCUMENTATION GAP: The pages do not say which one is authoritative, or whether a browser redirect still happens when responseHandler runs. Webhooks are not mentioned. -->

</Accordion>

<Accordion title="How do I show or hide payment methods?" icon="fa-toggle-on">

`enforce_paymethod` customises the options for one transaction, including modes, card schemes, and specific net-banking banks. The sample value is `creditcard|debitcard|HDFB|AXIB`.

`drop_category` hides one or more options. The sample value is `creditcard|debitcard`.

`pg` chooses the payment category to display. The description says the default is `CC`.

<!-- DOCUMENTATION GAP: No complete code list is published for these fields. -->

</Accordion>

<Accordion title="What do I change between test and production?" icon="fa-server">

Change the Bolt script from `https://jssdk-uat.payu.in/bolt/bolt.min.js` to `https://jssdk.payu.in/bolt/bolt.min.js`.

<!-- DOCUMENTATION GAP: Live key retrieval and the production _payment host are not documented on the Checkout Plus pages. -->

</Accordion>

<Accordion title="Why was my transaction rejected as a duplicate?" icon="fa-copy">

`txnid` can be used only once. PayU does not accept a duplicate transaction ID.

<!-- DOCUMENTATION GAP: The error code for a duplicate txnid is not documented. -->

</Accordion>

<Accordion title="Can I use Checkout Plus inside a mobile app WebView?" icon="fa-mobile">

No. The integrate page says Checkout Plus is not recommended for WebView or Chrome Custom Tabs. Use redirection-based [PayU Hosted Checkout](../payu-hosted-checkout-1).

A hidden Android article still exists at [WebView for Mobile Apps](./integrate-webview-for-mobile-apps-checkout-plus). It loads a checkout URL. It does not call `bolt.launch()`.

</Accordion>

<Accordion title="What does Retry do after a failed payment?" icon="fa-rotate-right">

The overview says the customer returns to the Checkout Plus payment form and can continue the current order, without starting the checkout again. The UPI journey says Retry is available when the payment fails.

<!-- DOCUMENTATION GAP: The pages do not say whether your integration must send a new txnid for that retry. -->

</Accordion>
