---
title: Introduction
deprecated: false
hidden: false
metadata:
  title: WhatsApp Integration Introduction
  robots: index
---
PayU supports multiple ways to accept payments on WhatsApp in partnership with Meta. Merchants integrate with PayU; PayU handles the Meta side—you do not need a separate commercial or technical integration with Meta for these flows.

- **P2M** (PG Deep Integration or Native WhatsApp Payments): P2M is Meta’s full in-chat checkout: When your business sends a **catalogue&#x20;**&#x6F;r **order** in WhatsApp, the customer taps **Review & Pay**, and a native payment sheet opens the following payment modes without leaving the app: UPI, Cards, Net Banking, Wallets and EMI.<br />It is the highest-capability flavour and best for e-commerce, D2C, travel, and OTT but needs  integration (often with a BSP), PG–WhatsApp OAuth, and handling both WhatsApp payment webhooks and PayU PG webhooks. To integrate P2M for WhatsApp payments, refer to [WhatsApp Payments Integration.](doc:whatsapp-native-payments)
- **UPI Intent URL:&#x20;**&#x55;PI Intent URL sends a structured **order\_details** message in WhatsApp; when the customer taps **Pay Now**, where the opens with the amount pre-filled, they authorise with UPI PIN, and the business gets confirmation in chat. It as a lightweight and no Meta template approval is required, and suited to utility bills, quick collections, and subscription renewals.&#x20;

  You can use your existing PayU PG webhook; enablement typically involves VPA / MCC / payment code from PayU rather than full P2M payment\_configuration. To integrate UPI Intent URL for WhatsApp payments, refer to [WhatsApp Payments Integration.](doc:whatsapp-native-payments)
- **Enhanced Payment Links (EPL)** is the simplest option: you send an approved WhatsApp **template** message with a **Pay Now** call-to-action, the customer taps it, and completes payment on PayU’s **Hosted Checkout** page, whereas on WhatsApp app itself for UPI payments. If you already use PayU **payment links**, link generation and **webhooks** work the same as today. To integrate EPL for WhatsApp payments, refer to [Enhanced Payment Links on WhatsApp.](doc:enhanced-payment-links-on-whatsapp)

## PayU Offerings

Meta defines three WhatsApp commerce payment flavours; EPL sits at the **lowest complexity** end (typically **1–2 weeks** to go live), with **no** PG-to-WhatsApp **OAuth** linking in Business Manager.

|                                | UPI Intent                            | PG Deep Integration                      | EPL                                                |
| :----------------------------- | :------------------------------------ | :--------------------------------------- | :------------------------------------------------- |
| **Complexity**                 | Medium                                | High                                     | Low                                                |
| **Typical engineering effort** | 4–5 weeks                             | 8–12 weeks                               | 1–2 weeks                                          |
| **Payment methods**            | UPI-primary (others extendable)       | UPI, cards, net banking, wallets         | All (UPI, cards, net banking, wallets, EMI)        |
| **Payment inside WhatsApp?**   | Partial — UPI apps open from WhatsApp | Yes — native in-chat checkout            | No — opens PG checkout in browser                  |
| **Best for**                   | Bill pay, utilities, BBPS, government | E-commerce, travel, quick commerce, food | Collections, insurance, lending, EMI, fast go-live |

***

## Comparison of WhatsApp payment options

| Dimension                                | PG Deep Integration                                                        | UPI Intent                          | EPL                    |
| :--------------------------------------- | :------------------------------------------------------------------------- | :---------------------------------- | :--------------------- |
| **What you send**                        | `order_details` interactive message                                        | `order_details` interactive message | Template + CTA URL     |
| **Meta template required**               | No                                                                         | No                                  | Yes                    |
| **PG–WhatsApp OAuth**                    | Yes                                                                        | No                                  | No                     |
| `payment_configuration`**&#x20;in Meta** | Yes                                                                        | No                                  | No                     |
| **EPL allowlist or gating list**         | No                                                                         | No                                  | Yes                    |
| **Webhook changes**                      | Yes — add **WhatsApp payment status** webhooks; reconcile with PG webhooks | None (same PG webhook)              | None (same PG webhook) |
| **In-chat order management**             | Full (`order_status`, payment lookup APIs)                                 | No                                  | No                     |
| **Customer leaves WhatsApp?**            | No                                                                         | Partial (UPI app)                   | Yes (browser checkout) |

PayU is supported across **all three** solutions, so many merchants can start with **EPL** and later add **UPI Intent** or **PG Deep Integration** without changing payment gateway.

***

<br />
