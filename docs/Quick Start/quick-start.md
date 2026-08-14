---
title: ' Start Here — Accept Payments with PayU'
excerpt: >-
  Not sure where to start? Tell us what you're trying to do, and we'll show you
  the fastest way to accept payments with PayU — no technical background needed.
deprecated: false
hidden: true
metadata:
  robots: index
---
{/*
EDITORIAL NOTES (delete before publishing — not part of the rendered page):

1. This page assumes the PayUIntegrationPathRecommender component (or a successor
   built for this flow) is updated to begin with GOAL, not "How will you collect
   payments?" — see the research addendum. The embed point is marked below.
   Until that rebuild ships, the static "All integration paths" table further
   down the page is the fallback and should stay in place either way (it's also
   what keeps this page AI/SEO-readable — see the AI-readiness notes from the
   component review).

2. Product naming fix: the merchant-facing name for the no-code, dashboard-first
   product is "Pay Handle" (confirmed dominant in merchant interviews), not the
   generic "Payment Links" used in earlier drafts. This page uses "Pay Handle"
   throughout, with "payment link" as the plain-language gloss. The underlying
   PRODUCTS data key should be renamed to match — currently still "Payment Links"
   in the component data file.

3. Anchor links below (e.g. #activation-diagnostic) assume this ships as one
   page. If it's later split across multiple ReadMe pages, update these to full
   paths and add redirects.
*/}

## Let's Get you Accepting Payments

You don't need to know anything about payment gateways, APIs, or checkout types to start. Answer a couple of quick questions below and we will show you exactly what to do next — whether that's something you do yourself, something you hand to a developer, or something an AI assistant builds for you.

<Tabs>
  <Tab title="What is PayU, in one sentence?" icon="far fa-pen-line">
    PayU helps you accept money from your customers — online, through a link, or in person — and get it into your bank account safely. You don't need to be technical to use it.
  </Tab>

  <Tab title="What is a payment gateway?" icon="far fa-money-bills">
    A payment gateway is the service that securely takes your customer's card or bank details and confirms whether the payment went through. PayU is yours.
  </Tab>
</Tabs>

***

## New Here, or Picking Back Up?

<Cards>
  <Card title="If this is your first time setting up payments with PayU" icon="far fa-rectangle-new">
    skip straight to [What do you want to do?](#what-do-you-want-to-do) below.
  </Card>

  <Card title="If you've already started" icon="far fa-square-list">
    pick the option that matches where you are — it'll save you from repeating steps you have already done:

    - **I've set things up but haven't taken a real payment yet** → go to the [Activation Diagnostic](#activation-diagnostic)

    - **I'm already accepting payments and want to do more** → see [Add more to your setup](#add-more-to-your-setup)

    - **Just getting started** → continue to [What do you want to do?](#what-do-you-want-to-do)
  </Card>
</Cards>

<br />

***

## What do you want to do?

{/* Embed point: interactive path finder. Update underlying question set to
     start here (Goal), then Setup, then show the recommendation, then ask
     Builder — per the research-driven redesign. */}

<PayUIntegrationPathRecommender />

If you'd rather just browse everything PayU offers instead of answering questions, every path is listed below.

<details>
<summary><b>See all PayU integration paths</b></summary>

| Path                                                           | Best for                                                         | Do you need a developer? | Typical time     |
| -------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------ | ---------------- |
| **Pay Handle** (payment link)                                  | Selling without a website — invoices, social media, WhatsApp     | No                       | Minutes          |
| **PayU Hosted Checkout**                                       | A website where you want PayU to handle the whole payment page   | Usually not, but helps   | A few days       |
| **Merchant Hosted Checkout**                                   | A website where you want full control of the payment page design | Yes                      | 1–2 weeks        |
| **Server-to-Server Integration**                               | Marketplaces or platforms paying out multiple parties            | Yes                      | 2–3 weeks        |
| **UPI QR**                                                     | In-person, counter, or kiosk collection                          | No                       | Under a week     |
| **eCommerce plugins** (Shopify, WooCommerce, Magento)          | You already sell through one of these platforms                  | No                       | Minutes to hours |
| **Mobile SDKs** (Android, iOS, React Native, Flutter, Cordova) | A mobile app                                                     | Yes                      | 1–2 weeks        |
| **Recurring Payments**                                         | Subscriptions or membership billing                              | Usually yes              | 2–3 weeks        |

</details>

***

## Who's going to set this up?

Once you've got a recommendation above, this decides how it's presented to you — not what's recommended.

- **I'll do it myself** → you'll get a fully guided, step-by-step walkthrough with no assumed technical knowledge, using your PayU Dashboard wherever possible instead of code.
- **I have a developer** → jump to [Send this to your developer](#send-this-to-your-developer).
- **I'll use an AI assistant (ChatGPT, Claude, Gemini) to help me build it** → jump to [Build this with AI](#build-this-with-ai).
- **I use a plugin, so I don't think I need code** → your platform's plugin guide already has everything you need — no further questions here.
- **Not sure** → that's fine. If you have someone at your business who writes code or manages your website, choose "I have a developer." Otherwise, start with "I'll do it myself" — the guided path is written for exactly this situation.

***

## Send this to your developer

If someone else — a freelancer, an agency, or a colleague — is going to do the technical work, don't make them start from scratch or wait on dashboard access they may not have.

<Callout icon="👍" theme="okay">
  ### Share this directly

  Copy the summary below and send it to your developer as-is. It works whether or not they have a PayU Dashboard login.
</Callout>

**Developer handoff summary**

```
Integration: [recommended product from above, e.g. PayU Hosted Checkout]
Goal: [e.g. one-time card/UPI payment on a product page]
Platform: [e.g. custom website, Node.js backend]
What you'll need: Merchant Key and Salt (found in Dashboard → Settings → API Keys —
ask the account owner to share these securely if you don't have dashboard access)
Full technical guide: https://docs.payu.in/collect-payments/introduction-web/[path]
```

Your developer's version of this page skips everything above and goes straight to:

- Sandbox and production credentials, clearly labeled
- Complete, copy-paste, runnable code
- Webhook and callback handling
- Error codes and how to read logs
- A production go-live checklist

→ [Open the developer documentation](#)

***

## Build this with AI

Most developers who successfully integrate PayU today use an AI assistant — ChatGPT, Claude, or Gemini — to write the actual code. This works well if you give it the right instructions and the right reference material.

<Callout icon="⚠️" theme="warn">
  ### Review before you use it live

  Your AI assistant will write real code from this. Review what it produces before using it with real payments — especially anything that touches your Salt or handles customer data.
</Callout>

Copy these two prompts one at a time — splitting the work like this avoids running into your AI tool's response length limits partway through.

**Prompt 1 — core integration**

```
Help me integrate [recommended product, e.g. PayU Hosted Checkout] into my
[your platform, e.g. Node.js website]. My goal is [your goal, e.g. a one-time
card/UPI payment on a product page].

Here's what I need you to do:
1. Generate a signed payment request using a Merchant Key and Salt (I'll provide
   these separately — do not hardcode them).
2. Build the request with the required fields: transaction ID, amount, product
   info, customer details, and success/failure redirect URLs.
3. Generate the request hash following PayU's documented algorithm.
4. Redirect the customer to the PayU Hosted Checkout URL with the signed payload.

Reference documentation: https://docs.payu.in/collect-payments/introduction-web/[path]
```

**Prompt 2 — success and failure handling**

```
Now help me handle the response PayU sends back after a payment attempt:
1. Receive and verify the redirect to my success/failure URLs.
2. Verify the response hash to confirm the response actually came from PayU.
3. Handle the webhook/callback PayU sends server-to-server for the same
   transaction, and reconcile it against my order records.
4. Log both the redirect response and the webhook so I can debug mismatches.

Reference documentation: https://docs.payu.in/developer-tools/webhooks-consolidated
```

Once your AI assistant produces code, test it in sandbox before going live — see [Test it safely](#test-it-safely) below.

***

## What happens after you choose

Every PayU integration follows the same shape, no matter which path above you took:

1. **Understand what you're using** — you just did this
2. **See what you need before you start** — plain-language prerequisites, not jargon
3. **Set it up** — guided steps, a developer handoff, an AI prompt, or a plugin install
4. **Test it safely** — try a payment that doesn't use real money
5. **Go live** — switch on real payments
6. **Confirm your first real payment came through**
7. **Know what to do next**

***

## Test it safely

Before any real customer pays you, try it yourself in test mode — this uses fake payment details and doesn't touch real money.

- No signed contract or completed KYC is required to test.
- Use PayU's test card numbers, UPI IDs, and wallet credentials to try a successful payment, a failed payment, and a pending payment.
- Confirm the result appears in your Dashboard under **Transactions**.

→ [See test card and UPI details](#)

***

## Activation Diagnostic

If you've already set things up but haven't taken a real payment yet, tell us what's stopping you — the fix is different depending on where the hold-up actually is.

**Things PayU can fix for you:**

- **My website/business verification is still pending** → [Check your verification status](#) — most verifications complete within a few business days; if yours has taken longer, [escalate here](#).
- **I don't have my keys yet, or can't find them** → your Merchant Key and Salt are in **Dashboard → Settings → API Keys**. If you don't see them, your account may still be finishing verification — check the status above first.
- **My pricing isn't clear to me** → [See a plain-language breakdown of PayU's fees](#).
- **I need international payments enabled** → [Request international activation](#).
- **I tried a test payment but I'm not sure it worked** → [Verify your test payment](#test-it-safely) using the same steps above.

**Things that are on your side, not PayU's — and that's okay:**

- **My website or store isn't ready yet** — no rush. Your integration will be waiting when you are. [Get a reminder in a few weeks](#) instead of working through steps that don't apply yet.
- **I don't have traffic or orders yet** — same as above. Nothing further to do on the payments side until you're ready to launch.
- **I'm waiting on a partner, developer, or a fixed go-live date** (e.g. a school term or system rollout) — your setup is fine as-is; there's nothing blocking it on PayU's end.

***

## Add more to your setup

Already accepting payments? Here's what most merchants add next:

- [Accept UPI, wallets, EMI, or netbanking](#) alongside cards
- [Set up refunds](#) so you can reverse a payment from your dashboard or API
- [Add recurring or subscription billing](#)
- [Enable saved cards](#) for faster repeat checkout
- [Split payouts across multiple vendors](#) if you run a marketplace

***

## Still not sure?

Describe your business in your own words to Ask AI — for example, _"I sell handmade candles on Instagram and want people to be able to pay me directly."_ It'll point you to the right starting point, whether you're technical or not.

<Callout icon="📘" theme="info">
  ### Ask AI can help with questions like:

  - "What is PayU?"
  - "What is a payment gateway?"
  - "Which PayU product should I use?"
  - "Do I need a developer?"
  - "How do I integrate Hosted Checkout?"
  - "How do I generate the hash?"
  - "How do I verify a payment?"
</Callout>

***

## Get help

- **[Ask AI](#)** — ask in plain language or technical terms, it'll match your question
- **[Postman Collection](#)** — every endpoint, pre-configured
- **[Troubleshooting & error codes](#)**
- **[FAQs](#)**
- **[Contact support](#)** — if you've checked the above and you're still stuck
