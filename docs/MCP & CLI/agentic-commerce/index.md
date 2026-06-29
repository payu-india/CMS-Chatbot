---
title: PayU Agentic Commerce Suite
excerpt: >-
  Get started with accepting orders and payments from AI apps, on your own AI
  Agents or via 3rd Party AI Agents 3rd party AI agents.
deprecated: false
hidden: false
metadata:
  robots: index
---
# Agentic Commerce for Merchants

**Sell where your customers already shop — in conversation.**

Your customers are no longer only browsing your website. They are asking ChatGPT what to buy, reordering essentials through WhatsApp, and expecting an assistant to find the right product and help them pay — without leaving the chat.

This guide explains what that shift means for your business, shows which option fits your situation, and tells you what to do next. You do not need an AI team to begin.

***

## What is agentic commerce?

**Agentic commerce** is shopping where an AI assistant acts on behalf of the customer — finding products, building a cart, and completing payment — while the customer stays in control.

Think of it as moving from _clicks_ to _conversations_:

| Today                                                             | Agentic commerce                                                                            |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Customer searches Google, lands on your site, browses, checks out | Customer says _"Reorder my usual coffee"_ or _"Find white sneakers under ₹2,000"_           |
| You optimise for SEO and page design                              | You make your catalogue and checkout **readable and callable by AI**                        |
| Payment happens on your checkout page                             | Payment happens inside the conversation — securely, with the customer approving when needed |

The assistant does not replace your brand or your fulfilment. It removes friction between **intent** and **purchase**. For D2C and SMB merchants, that usually means fewer abandoned carts, faster repeat orders, and a new channel where early movers stand out.

PayU sits at the settlement layer: we help you accept UPI and cards inside these AI journeys without exposing sensitive payment data to the assistant.

***

## Why this matters for merchants

Three shifts are already underway:

1. **Discovery is moving to AI.** Shoppers use ChatGPT, Gemini, and similar assistants to research and shortlist products — the way they once used search and social feeds.
2. **Conversations convert.** When discovery and checkout happen in the same thread, there are fewer redirects and fewer drop-offs.
3. **Trust follows familiarity.** Customers who already chat with your brand on WhatsApp or inside an AI app are more willing to buy there — if payment feels as safe as your website.

Merchants who adopt early gain a new acquisition channel, better conversion on repeat purchases, and the ability to serve customers who would never have completed a long browse-and-checkout flow on their own.

You do not need to rebuild your entire stack on day one. Most merchants start with one option, prove results, and add others over time.

***

## Where agentic commerce happens

### ChatGPT and other AI apps

AI platforms are becoming storefronts. A customer discovers your products inside ChatGPT, confirms what they want, and pays — without opening your website.

**See it live:** [KwikStore on ChatGPT](https://chatgpt.com/apps/kwikstore/asdk_app_6a2bb1e159e88191b0721ceddd9e04ca) — a shopping journey built by GoKwik in partnership with PayU. Browse the catalogue, build a cart, and complete checkout inside ChatGPT. Use it as a reference for what a conversational store can feel like.

### WhatsApp Commerce

If you already sell on **WhatsApp Commerce**, you are in an excellent position. WhatsApp is where natural, back-and-forth conversations already happen — product questions, size checks, order confirmations. Agentic commerce extends that same pattern: the assistant helps the customer decide, and PayU handles payment when they are ready.

WhatsApp is often the **fastest place to start** for SMB merchants who already have catalogue, customer relationships, and order workflows on the channel.

### Your own website or app

You can also run a **merchant-owned AI assistant** on your site — a branded helper that knows your catalogue, policies, and loyalty rules. The customer never leaves your property; PayU still powers secure payment.

***

## Which option works when

These options do not compete — many merchants use more than one. Pick what matches your situation today; add others as you grow.

| Option                                             | When to choose it                                                                                                                     | What it does                                                                                                                                                                 |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sell on AI apps** (ChatGPT, Gemini, and similar) | You want **new customers** from AI discovery; you have a product catalogue; you want to go live in **weeks**, not months              | Your products appear where shoppers already ask AI for recommendations. They discover, cart, and pay inside the AI app — PayU handles settlement.                            |
| **WhatsApp Commerce**                              | You **already reach customers on WhatsApp** — orders, support, or catalogue sharing happen there today                                | You extend the conversation you already have: the assistant helps the customer choose, and PayU powers payment when they confirm. Often the fastest start for SMB merchants. |
| **Build your own AI assistant**                    | You want **full control** of the experience on your website or app; you have developers (in-house or agency) to build and maintain it | A branded AI helper on your property knows your catalogue, loyalty, and policies. The customer never leaves your site; PayU powers secure checkout.                          |
| **Allow AI shoppers on your site**                 | Your **website and checkout already work well**; you want **low disruption** — no rebuild, just open the door to trusted AI buyers    | Verified AI assistants browse and buy through your existing checkout. Your store stays as-is; PayU adds agentic settlement and reconciliation.                               |

**Not sure where to start?** If you are already on WhatsApp, begin there. Otherwise, **sell on AI apps** is usually the quickest way to test demand. You can layer the other options once you see results.

***

## Choose how customers pay

Once you know _where_ the conversation happens, pick the **payment method** that fits how quickly money must move and how much automation you want.

### UPI

| Method                         | Best when                                                                                        | How it works                                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **UPI Intent URL**             | You want the customer to approve each payment; human-in-the-loop is fine                         | The assistant shares a UPI link; the customer taps, opens their UPI app, and pays. Simple and familiar.                              |
| **UPI OTM** (One Time Mandate) | Payment can happen later; you need one-time consent, not real-time debit                         | Customer gives consent once; the debit can be executed in the future within agreed limits. Good for scheduled or deferred purchases. |
| **UPI Reserve**                | Amount should be blocked in the account — especially for high-frequency, low-value, everyday use | Funds are reserved upfront; useful when the exact timing or amount may change slightly before capture.                               |
| **UPI Circle**                 | Delegated purchases within spending limits, without blocking full amounts                        | _Coming soon._ Contact your PayU Key Account Manager (KAM) to register interest and learn when it is available for your category.    |

### Cards

**Passkeys** make agentic card payments convenient: the customer approves with biometrics or device PIN where the issuer supports it, without re-entering card details in chat. Sensitive card data never passes through the AI assistant — it stays inside PayU's secure infrastructure.

### All payment methods in one surface

If you need **cards, UPI, net banking, wallets, and more** in a single flow, load **PayU Payment Links inside an iframe** (or hosted widget). The assistant confirms the order; the customer completes payment on PayU's trusted page embedded in the conversation. This is the most flexible option when you cannot narrow down to one rail.

***

## What to do next — by option

### Sell on AI apps

**When this fits:** you want new customers from ChatGPT and similar platforms, have a product catalogue to share, and want to go live quickly.

**What you need:**

- Product catalogue with price, variants, and availability (API, feed, or spreadsheet to start). **PayU will help structure your inventory** — drawing on our experience across categories in what convinces shoppers and what they actually buy.
- Basic order and fulfilment hooks (create order, send confirmation). **PayU will help you build an MCP server** on top of your commerce stack for **headless, API-led agentic checkout**.
- Returns and cancellation policies documented

**What to do:**

1. **Try the reference journey** — explore [KwikStore on ChatGPT](https://chatgpt.com/apps/kwikstore/asdk_app_6a2bb1e159e88191b0721ceddd9e04ca) to see discovery → cart → payment in one thread.
2. **Talk to your PayU KAM** — schedule a short discovery call. We align on catalogue format, payment method (UPI Intent, Payment Links, or cards via Passkeys), and pilot metrics (conversion, AOV, drop-off).
3. **Start a pilot** — PayU provides integration scaffolding; you connect catalogue and orders at a depth that matches your bandwidth. Expand in phases as results prove out.

**Build it yourself:** Merchants with engineering capacity can publish their own ChatGPT app using PayU Payment Links and the OpenAI Apps SDK. See [Build your own ChatGPT merchant app](https://docs.payu.in/update/docs/build-your-own-chatgpt-merchant-app).

***

### WhatsApp Commerce

**When this fits:** you already reach customers on WhatsApp — for orders, support, catalogue sharing, or payment links.

**What you need:**

- An active WhatsApp Business presence and a catalogue or order flow your team already runs
- Payment method aligned to how your customers pay today (see [Choose how customers pay](#choose-how-customers-pay))
- Returns and cancellation policies your team can honour in chat

**What to do:**

1. Map your current WhatsApp order flow — where does the customer ask, confirm, and pay today?
2. Identify the highest-frequency intent (reorder, catalogue browse, bill pay, appointment + pay) and automate that first.
3. Choose payment: **UPI Intent URL** for approve-each-time; **UPI OTM** or **Reserve** for repeat or scheduled orders; **Payment Links** if you need every method in one link.
4. Ask your KAM to connect WhatsApp agentic flows to your PayU account. PayU can help structure inventory and build the checkout layer for conversational orders.

***

### Build your own AI assistant

**When this fits:** you want full control of the shopping experience on your website or app, and you have developers (or a partner) to build and maintain it. Example - Amazon Alexa, Ixigo Taara, Makemytrip Myra are some examples.&#x20;

**What you need:**

- Everything listed under **Sell on AI apps**, plus:
- A plan for how your assistant accesses catalogue, cart, loyalty, and checkout (typically via APIs or an MCP server)
- UX for conversational discovery, cart edits, and payment confirmation on your surface

**What to do:**

1. **Define the journeys** — repeat purchase, guided discovery, scheduled buy, support-led sale. Pick one pilot journey, not all at once.
2. **Expose machine-readable commerce** — your assistant needs structured product truth (price, stock, delivery, returns), not just marketing pages.
3. **Integrate PayU for settlement** — choose UPI Intent for approve-each-time flows, UPI Reserve or OTM for deferred or recurring patterns, Passkeys for cards, or Payment Links in an iframe for full method coverage.
4. **Work with your KAM** on sandbox credentials, webhooks, and go-live checklist. **PayU will help build these agents through our tech resources** so you can get started as quickly as possible — you do not need to hire an AI team first.

**Build it yourself:** For a ChatGPT-native version of your assistant, follow [Build your own ChatGPT merchant app](https://docs.payu.in/update/docs/build-your-own-chatgpt-merchant-app).

***

### Allow AI shoppers on your site

**When this fits:** your website and checkout already convert well, and you want verified AI assistants to browse and buy without rebuilding the store.

**What you need:**

- A working checkout that PayU already powers (or can power)
- A trust layer so only verified AI shoppers get full catalogue and pricing access. **PayU will help you build this layer** — protecting both merchants and customers from misuse while keeping the experience open to legitimate AI traffic.
- Clear product data (structured feeds or schema) so agents do not misread your pages

**What to do:**

1. **Reach out to your KAM** to run PayU's **agent readiness survey** for your website — a structured check of whether your product pages expose accurate price, availability, and policies in machine-readable form.
2. **Add AI shopper verification** — PayU's solutions team implements the trust layer with you; you do not need a new storefront.
3. **Keep settlement on existing rails** — agentic traffic settles the same way as your normal online orders; PayU tags agent-originated transactions for reconciliation.
4. **Contact your KAM** to enable agentic checkout on your current MID and agree on pilot scope.

***

## Security and trust — what you should know

These points matter to your customers and to compliance:

- **Payment credentials never go through the AI assistant.** Card numbers, CVV, and UPI PINs are entered on PayU's secure surface — not in chat.
- **OTP and 2FA are necessary controls** where the issuer or network requires them. PayU optimises the journey; we do not bypass security.
- **You stay in control of fulfilment, refunds, and policies.** Agentic checkout creates orders on your systems; PayU handles payment and reconciliation.
- **Settlements match your existing setup.** Agent-originated transactions appear in your PayU dashboard with the references you need for support and finance.

***

## Example journeys you can enable

Once your option and payment method are chosen, these are the kinds of experiences merchants already piloting agentic commerce are building:

- **Repeat essentials** — _"Order the same diapers in XL that I bought last month"_ → agent validates variant, creates order, UPI Intent or delegated UPI for payment.
- **Discovery-led purchase** — _"White running shoes under ₹2,000, good for flat feet"_ → agent shortlists from your catalogue, customer picks, pays via Passkey or Payment Link.
- **Scheduled buy** — _"Buy the Diwali sale items when the sale starts at midnight"_ → agent saves the basket, collects consent, executes with UPI OTM or Reserve at the right time.
- **WhatsApp reorder** — customer messages your business number with something like _"Send me 2 kg atta and 1 litre olive oil — same as last time"_ → you confirm quantity and total in chat; customer taps a UPI link or pays through an embedded Payment Link.

Start with one journey. According to <Anchor target="_blank" href="https://business.adobe.com/resources/digital-economy-index.html">Adobe Digital Insights (Q1 2026)</Anchor>, AI-referred shoppers now convert **42% better** than non-AI traffic — after AI assistants have already researched, compared, and personalised the recommendation in conversation. Measure conversion and repeat rate against your current baseline; expand when the numbers justify it.

***

## Get started

| Step | Action                                                                                                                                                                                   |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Read [Which option works when](#which-option-works-when) — pick sell on AI apps, WhatsApp Commerce, build your own assistant, or allow AI shoppers on your site (you can add more later) |
| 2    | Choose your [payment method](#choose-how-customers-pay)                                                                                                                                  |
| 3    | Explore [KwikStore on ChatGPT](https://chatgpt.com/apps/kwikstore/asdk_app_6a2bb1e159e88191b0721ceddd9e04ca) as a live reference for agentic commerce                                    |
| 4    | **Contact your PayU Key Account Manager** — discovery workshop, agent readiness survey (for your website), pilot scope, and go-live plan                                                 |
| 5    | _(Optional)_ [Build your own ChatGPT merchant app](https://docs.payu.in/update/docs/build-your-own-chatgpt-merchant-app) if you have engineering capacity                                |

**Interested in UPI Circle or early access programmes?** Register your interest with your KAM — we will notify you when your category and use case are supported. We are initiating early registrations already.

***

_PayU Agentic Commerce — discovery, checkout, and payments for the conversation economy. Built for merchants who want to sell where customers already are._
