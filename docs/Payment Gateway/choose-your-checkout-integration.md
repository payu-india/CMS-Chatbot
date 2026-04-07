---
title: Start Here - Choose Your Integration
deprecated: false
hidden: false
metadata:
  robots: index
next:
  description: Refer to the following pages for additional information.
  pages:
    - slug: collect-payments-introduction
      title: Payment Gateway Overview
      type: basic
    - slug: payu-payment-gateway-workflow
      title: Payment Gateway Workflow
      type: basic
---
If you're integrating payments for the first time, the first step is choosing the right integration approach based on your requirements.

***

## Available Integration Options

PayU offers multiple ways to integrate payments, depending on how much control and effort you want.

|                           | **Hosted Checkout**         | **Merchant Hosted Checkout (Custom UI)**  | **APIs or Server-to-Server**                |
| ------------------------- | --------------------------- | ----------------------------------------- | ------------------------------------------- |
| **What it is**            | PayU hosts the payment page | You build the UI, PayU processes payments | Direct API calls, no redirect               |
| **UI ownership**          | PayU                        | You                                       | You                                         |
| **PCI compliance burden** | Low — PayU handles it       | Medium                                    | High — card data passes through your server |
| **Time to integrate**     | Hours                       | Days                                      | Days to weeks                               |
| **Customization**         | Limited (logo, colors)      | Full                                      | Full                                        |
| **Best for**              | Most use cases, fast launch | Branded experiences                       | Subscriptions, mobile SDKs, headless setups |
| **Requires backend?**     | Yes (hash generation only)  | Yes                                       | Yes                                         |
| **Redirect to PayU?**     | Yes                         | No                                        | No                                          |

***

## How to Decide

**Start with Hosted Checkout if:**

* You want to accept payments quickly without building a checkout UI
* You don't want to handle raw card data
* You're building an MVP, marketplace, or e-commerce store

**Consider Web Checkout if:**

* You need full control over how the payment form looks
* You have a strong brand that must stay consistent through checkout

**Use APIs / Server-to-Server if:**

* You're building recurring billing or subscriptions
* You need to trigger payments programmatically without user interaction
* You're integrating with a mobile SDK or a headless frontend