---
title: Enhanced Payment Links on WhatsApp
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU supports multiple ways to accept payments on WhatsApp in partnership with Meta. Merchants integrate with PayU; PayU handles the Meta side—you do not need a separate commercial or technical integration with Meta for these flows.

**Enhanced Payment Links (EPL)** is the simplest option: you send an approved WhatsApp **template** message with a **Pay Now** call-to-action, the customer taps it, and completes payment on PayU’s **hosted checkout** in the browser (outside WhatsApp). If you already use PayU **payment links**, link generation and **webhooks** work the same as today.

<Cards>
  <Card title="Overview" href="#overview" icon="fa-info-circle">
    What EPL is and how it fits alongside other WhatsApp payment options.
  </Card>

  <Card title="How the payment flow works" href="#how-the-payment-flow-works" icon="fa-route">
    End-to-end steps from link creation to webhook notification.
  </Card>

  <Card title="Benefits and fit" href="#benefits-for-your-business" icon="fa-briefcase">
    Why EPL is often the best starting point and typical industries.
  </Card>

  <Card title="Requirements to go live" href="#requirements-to-go-live-on-epl" icon="fa-list-check">
    WABA, template approval, allowlisting, and PayU account needs.
  </Card>

  <Card title="Compare WhatsApp payment options" href="#compare-whatsapp-payment-options" icon="fa-table">
    EPL vs UPI Intent vs PG Deep Integration at a glance.
  </Card>

  <Card title="Go-live checklist" href="#go-live-checklist" icon="fa-clipboard-check">
    Checklist before you take EPL live.
  </Card>
</Cards>

## Overview

EPL uses Meta’s **Enhanced Payment Links** pattern: PayU generates a **payment link** for the order, your system sends a WhatsApp **Cloud API** template whose CTA URL carries the PayU link (with the **PayU-specific URL suffix** Meta requires), WhatsApp shows an enhanced card with **Pay Now**, and the customer pays on PayU checkout using **UPI, cards, net banking, wallets, EMI**, and other methods your PayU setup supports.

Meta defines three WhatsApp commerce payment flavours; EPL sits at the **lowest complexity** end (typically **1–2 weeks** to go live), with **no** PG-to-WhatsApp **OAuth** linking in Business Manager.

|                                | EPL                                                | UPI Intent                            | PG Deep Integration                      |
| :----------------------------- | :------------------------------------------------- | :------------------------------------ | :--------------------------------------- |
| **Complexity**                 | Low                                                | Medium                                | High                                     |
| **Typical engineering effort** | 1–2 weeks                                          | 4–5 weeks                             | 8–12 weeks                               |
| **Payment methods**            | All (UPI, cards, net banking, wallets, EMI)        | UPI-primary (others extendable)       | UPI, cards, net banking, wallets         |
| **Payment inside WhatsApp?**   | No — opens PG checkout in browser                  | Partial — UPI apps open from WhatsApp | Yes — native in-chat checkout            |
| **Best for**                   | Collections, insurance, lending, EMI, fast go-live | Bill pay, utilities, BBPS, government | E-commerce, travel, quick commerce, food |

***

## How the payment flow works

1. Your backend calls PayU to **generate a payment link** (same as existing payment-link flows).
2. Your backend calls the **WhatsApp Cloud API** with an **approved template**; the template’s CTA includes the PayU link URL pattern Meta expects.
3. The customer sees the template card in WhatsApp and taps **Pay Now**.
4. The **browser** opens PayU **hosted checkout**; the customer pays with any supported method.
5. PayU processes the payment and sends your existing **PG webhook** (same payload and reconciliation patterns as today).

```
Merchant system
  → PayU API: create payment link
  → WhatsApp Cloud API: send approved template (CTA URL includes PayU link suffix)
  → Customer taps Pay Now → PayU hosted checkout in browser
  → Customer pays → PayU webhook to merchant (same as existing payment links)
```

***

## Benefits for your business

- **Minimal backend change** if you already use PayU payment links—reuse link APIs and webhooks.
- **No OAuth linking** of your PayU account inside WhatsApp Business Manager for EPL.
- **Full checkout breadth** on PayU hosted pages (EMI, auto-debit, etc.), not limited to in-chat UPI-only flows.
- **Fastest path to WhatsApp collections** compared with deeper native integrations.

Real-world examples cited in product materials include **PolicyBazaar** (reported **17%** conversion uplift after EPL) and **Piramal Finance** for recurring EMI collection via links.

### When EPL is a strong fit

- Insurance — premium renewals and policyholder collections.
- Lending / NBFCs — EMI and recurring collection links.
- Bulk **collections and reminders** with a pay link in each template message.
- Merchants who already run **PayU payment links** and want WhatsApp as an additional channel.
- Teams that need **go-live in roughly 1–2 weeks** (often dominated by **Meta template approval**, typically **3–7 business days**).

### When to consider another flavour instead

- You need the customer to **stay inside WhatsApp** for the full payment UX → look at **PG Deep Integration** (or **UPI Intent** if UPI-only is acceptable).
- You need **rich multi-line-item orders** and real-time **order status** purely in chat (for example food delivery) → **PG Deep Integration** is usually more appropriate.

***

## Prequisites to go live on EPL

| Requirement                          | Detail                                                                                                                      |
| :----------------------------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| **WhatsApp Business Account (WABA)** | **Enterprise** WABA, **verified** with Meta.                                                                                |
| **Approved message template**        | Template with a **CTA button**; URL must follow Meta’s **PayU-specific link suffix** rules. Submitted and approved by Meta. |
| **PayU account**                     | Standard PayU merchant account. (Razorpay and Cashfree are also supported in EPL programmes where applicable.)              |
| **EPL allowlisting**                 | WABA must be added to Meta’s **EPL gating (GK) biglist**—PayU or your **BSP** drives this.                                  |
| **OAuth to link PG in WA**           | **Not required** for EPL.                                                                                                   |
| **Webhooks**                         | Keep your **existing PayU webhook**; no new WhatsApp payment webhook is required for EPL.                                   |

> 👍 Contact PayU KAM
>
> For **WABA verification**, **template submission**, **EPL allowlisting**, and **commercial enablement**, work with your **PayU Key Account Manager (KAM)** or your **BSP** so the correct Meta and PayU steps complete in order.

***

## Comparison of WhatsApp payment options

| Dimension                                | EPL                    | UPI Intent                          | PG Deep Integration                                                        |
| :--------------------------------------- | :--------------------- | :---------------------------------- | :------------------------------------------------------------------------- |
| **What you send**                        | Template + CTA URL     | `order_details` interactive message | `order_details` interactive message                                        |
| **Meta template required**               | Yes                    | No                                  | No                                                                         |
| **PG–WhatsApp OAuth**                    | No                     | No                                  | Yes                                                                        |
| `payment_configuration`**&#x20;in Meta** | No                     | No                                  | Yes                                                                        |
| **EPL GK biglist**                       | Yes                    | No                                  | No                                                                         |
| **Webhook changes**                      | None (same PG webhook) | None (same PG webhook)              | Yes — add **WhatsApp payment status** webhooks; reconcile with PG webhooks |
| **In-chat order management**             | No                     | No                                  | Full (`order_status`, payment lookup APIs)                                 |
| **Customer leaves WhatsApp?**            | Yes (browser checkout) | Partial (UPI app)                   | No                                                                         |

PayU is supported across **all three** solutions, so many merchants can start with **EPL** and later add **UPI Intent** or **PG Deep Integration** without changing payment gateway.

***

## Go-live checklist

- [ ] **Enterprise WABA** verified.
- [ ] **Active PayU** (or supported PG) merchant account.
- [ ] **Template** submitted with PayU CTA URL pattern; **approved** by Meta (often 3–7 business days).
- [ ] WABA on **EPL GK biglist** (PayU / BSP).
- [ ] Integration to **send the template** via WhatsApp Cloud API with the payment link.
- [ ] **Payment link** generation already in use (or implemented)—no EPL-specific change to PayU link APIs.
- [ ] **Existing PayU webhook** configured—unchanged for EPL.
- [ ] **End-to-end** test in sandbox / pilot.

**Typical timeline:** about **1–2 weeks**, often driven by template approval.

***

> 📘 **PayU recommends**
>
> - Treat EPL as the **default first step** for **link-based collections** and teams new to WhatsApp payments.
> - Keep using the [API Reference](ref:introduction-api-reference) for exact PayU request fields alongside this product overview.
> - Confirm **pricing and commercials** with your **PayU Key Account Manager (KAM)**; they are not covered in this technical overview.

***

##

<br />
