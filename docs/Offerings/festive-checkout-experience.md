---
title: Festive Checkout Experience
deprecated: false
hidden: true
metadata:
  robots: index
---
During peak festive and holiday seasons, the checkout journey plays a pivotal role in consumer sentiment and purchase completion. **Festive Elements on PayU Hosted Checkout** is a theme enhancement on PayU Hosted Checkout (Checkout Pro) that introduces vibrant, occasion-specific visual elements to elevate customer delight and celebrate the spirit of the festivities.

This feature operates purely at the UI/UX presentation layer on top of your existing integration. Payment options, promotional offers, order summaries, bank authentications, and transaction security remain completely unaffected.

<Callout icon="🎉" theme="default">
  ### **Festive Checkout Experience**

  Festive theming creates an engaging and celebratory payment environment, reinforcing brand warmth and consumer confidence during high-velocity holiday shopping seasons.
</Callout>

<Callout icon="📞" theme="warn">
  ### **How to deactivate?**

  Festive Elements are enabled by default to all merchants and can be deactived at the Merchant ID (MID) profile level by PayU. To deactivate festive themes for your checkout,  contact your **Key Account Manager (KAM)** or write to **PayU Support**. No code updates or API revisions are required on your website or application.
</Callout>

***

## Key Merchant Benefits

<Callout icon="far fa-circle-info" theme="info">
  ### Festive Animation cannot be customized:

  If you enable the Festive Checkout Experience, the animations on the checkout page displayed cannot be customized. It is displayed similar to the screenshots under [Sample Checkout pages.](#sample-checkout-pages)
</Callout>

| Benefit                             | Description                                                                                                                                          |
| :---------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zero Integration Overhead**       | Enable festive vibes without updating backend APIs, payment payloads, or hash calculation algorithms.                                                |
| **Elevated Buyer Delight**          | Vibrant, culturally resonant visuals create a warm shopping atmosphere that enhances brand recall and buyer engagement.                              |
| **Uncompromised Payment Integrity** | Core checkout functionality, payment method prioritization, saved cards, offers, and bank redirection flows continue to function without alteration. |
| **Cross-Platform Consistency**      | Optimized design assets ensure smooth rendering across desktop web, mobile web (MWeb), and enforced payment journeys.                                |
| **High Performance**                | Lightweight SVG vectors and pre-optimized assets ensure no impact on page load times or checkout latency.                                            |

***

## Supported Checkout Experiences & Platforms

Festive Elements are engineered to adapt across multiple checkout interfaces:

<Cards columns="2">
  <Card title="Checkout Pro (Desktop Web)" href="#checkout-pro-desktop-web">
    Full-bleed ambient festive backgrounds, thematic headers, and stylized order summary sections designed for large screens.
  </Card>

  <Card title="Checkout Pro (Mobile Web / MWeb)" href="#checkout-pro-mobile-web">
    Touch-optimized festive headers, compact banners, and streamlined accent illustrations tailored for mobile viewports.
  </Card>
</Cards>

### 1. Checkout Pro (Standard Hosted Checkout)

When customers are redirected to PayU Hosted Checkout:

* **Thematic Ambient Backgrounds**: Contextual festive graphics and color palettes reflect the active festival (such as Diwali or New Year).
* **Header & Accent Elements**: Festive embellishments frame the merchant logo and payable amount.
* **Expanded Order Amount & Offers View**: A consistent festive visual language is maintained even when customers expand order details, enter promo codes, or view bank offers.

#### Sample Checkout pages

**Checkout Pro**

![](https://files.readme.io/55975e75cd45dd93fd2cf5c04761006642e47666f6868d192bf92534be30efe1-image-20261030-060839.png)

<br />

**Enforced MWeb + Web**

![](https://files.readme.io/4c953202a14c4274ae6998b2a57711aa168b1365f5ad29225ba01e55b2d8f282-image-20261029-072730.png)

<br />

### 2. Enforced Payment Flows (Web & MWeb)

For merchants who route customers directly into an enforced payment option (such as Enforced Card, Net Banking, or UPI):

* The festive styling seamlessly wraps around the enforced instrument container.
* Form fields, bank selection drop-downs, and instant discount cards inherit the festive theme while maintaining accessibility and readability standards.