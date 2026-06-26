---
title: Introduction
deprecated: false
hidden: true
metadata:
  title: WhatsApp Integration Introduction
  robots: index
---
PayU supports multiple ways to accept payments on WhatsApp in partnership with Meta. Merchants integrate with PayU; PayU handles the Meta side—you do not need a separate commercial or technical integration with Meta for these flows.

- P2M
- **Enhanced Payment Links (EPL)** is the simplest option: you send an approved WhatsApp **template** message with a **Pay Now** call-to-action, the customer taps it, and completes payment on PayU’s **Hosted Checkout** page on the browser (outside WhatsApp) and on WhatsApp app itself for UPI payments. If you already use PayU **payment links**, link generation and **webhooks** work the same as today. For more information, refer to [Payment Links.](doc:payment-links-dashboard)

## Comparison of PayU Offerings

Meta defines three WhatsApp commerce payment flavours; EPL sits at the **lowest complexity** end (typically **1–2 weeks** to go live), with **no** PG-to-WhatsApp **OAuth** linking in Business Manager.

|                                | EPL                                                | UPI Intent                            | PG Deep Integration                      |
| :----------------------------- | :------------------------------------------------- | :------------------------------------ | :--------------------------------------- |
| **Complexity**                 | Low                                                | Medium                                | High                                     |
| **Typical engineering effort** | 1–2 weeks                                          | 4–5 weeks                             | 8–12 weeks                               |
| **Payment methods**            | All (UPI, cards, net banking, wallets, EMI)        | UPI-primary (others extendable)       | UPI, cards, net banking, wallets         |
| **Payment inside WhatsApp?**   | No — opens PG checkout in browser                  | Partial — UPI apps open from WhatsApp | Yes — native in-chat checkout            |
| **Best for**                   | Collections, insurance, lending, EMI, fast go-live | Bill pay, utilities, BBPS, government | E-commerce, travel, quick commerce, food |

***

## Comparison of WhatsApp payment options

| Dimension                                | EPL                    | UPI Intent                          | PG Deep Integration                                                        |
| :--------------------------------------- | :--------------------- | :---------------------------------- | :------------------------------------------------------------------------- |
| **What you send**                        | Template + CTA URL     | `order_details` interactive message | `order_details` interactive message                                        |
| **Meta template required**               | Yes                    | No                                  | No                                                                         |
| **PG–WhatsApp OAuth**                    | No                     | No                                  | Yes                                                                        |
| `payment_configuration`**&#x20;in Meta** | No                     | No                                  | Yes                                                                        |
| **EPL allowlist or gating list**         | Yes                    | No                                  | No                                                                         |
| **Webhook changes**                      | None (same PG webhook) | None (same PG webhook)              | Yes — add **WhatsApp payment status** webhooks; reconcile with PG webhooks |
| **In-chat order management**             | No                     | No                                  | Full (`order_status`, payment lookup APIs)                                 |
| **Customer leaves WhatsApp?**            | Yes (browser checkout) | Partial (UPI app)                   | No                                                                         |

PayU is supported across **all three** solutions, so many merchants can start with **EPL** and later add **UPI Intent** or **PG Deep Integration** without changing payment gateway.

***

<br />