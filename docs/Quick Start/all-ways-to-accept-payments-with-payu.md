---
title: All Ways To Accept Payments With PayU
excerpt: >-
  A complete reference of every PayU integration path. Not sure which to pick?
  Use the Quick Start instead.
deprecated: false
hidden: true
metadata:
  robots: index
---
Not sure which option fits? Get a personalized recommendation → — this page is for browsing and comparing.

| Path                                                           | Best for                                                               | Typically set up by                                                         | Typical time                                    |
| -------------------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------- |
| \[Pay Handle / Payment Links — CONFIRM NAME]                   | Selling without a website — invoices, social media, WhatsApp           | You, from your dashboard                                                    | _\[TO CONFIRM]_                                 |
| PayU Hosted Checkout                                           | A website where a simple, secure PayU-hosted page is enough            | _\[TO CONFIRM]_                                                             | _\[TO CONFIRM]_                                 |
| \[Merchant Hosted Checkout / Seamless Checkout — CONFIRM NAME] | A website where the payment page must match your site's design exactly | A developer                                                                 | _\[TO CONFIRM]_                                 |
| Server-to-Server Integration                                   | Marketplaces or platforms paying out multiple sellers                  | _\[TO CONFIRM — not stated as strictly developer-required, see validation]_ | _\[TO CONFIRM]_                                 |
| UPI QR                                                         | In-person, counter, or kiosk collection                                | You, from your dashboard                                                    | _\[TO CONFIRM]_                                 |
| eCommerce plugins (Shopify, WooCommerce, Magento)              | You already sell through one of these platforms                        | You, via plugin install                                                     | _\[TO CONFIRM — current supported plugin list]_ |
| Recurring Payments                                             | Subscriptions or membership billing                                    | _\[TO CONFIRM — not stated as strictly developer-required, see validation]_ | _\[TO CONFIRM]_                                 |

Each row links to its technical documentation: [Hosted Checkout](#) · [Merchant/Seamless Checkout](#) · [Server-to-Server](#) · [UPI QR](#) · [Plugins](#) · [Recurring Payments](#)

{/* Mobile SDKs intentionally excluded pending Product validation on
     whether mobile integration volume warrants inclusion. GoQwik-related
     flows intentionally excluded pending Engineering validation on
     whether they fit this table's model at all. */}

\===== PAGE: Send This to Your Developer =====

***

title: "Send This to Your Developer"
excerpt: "Everything your developer needs to understand what you're building and get started."
category: quick-start
hidden: false
-------------

# Send this to your developer

If someone else is doing the technical work — a freelancer, an agency, or a colleague — share this with them.

**What to send**

```
What I want to achieve: [merchant's stated goal]
Where I want to accept payments: [merchant's stated setup]
Recommended PayU solution: [recommended product]
What's needed before starting: [filtered prerequisites from the result]
Technical guide: [link to the specific product's developer documentation]
```

**Getting your developer access to your PayU account**

<Callout icon="⚠️" theme="warn">
  ### \[REQUIRES SECURITY/ENGINEERING VALIDATION — NOT YET RESOLVED]

  This page does not specify how a developer who is not the account owner should obtain or use PayU credentials. Do not instruct merchants to share their Merchant Salt directly until PayU confirms an approved mechanism. This section stays blank until Security signs off — see the validation checklist.
</Callout>

**The technical guide covers:**

- Sandbox and production credentials, clearly labeled
- Complete, copy-paste, runnable code
- Webhook and callback handling
- Error codes and how to read logs
- A production go-live checklist

[Open the developer documentation →](#)
