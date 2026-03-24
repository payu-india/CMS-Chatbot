---
title: Subscripions or Recurring Payments
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Recurring Payments Introduction
  description: >-
    Learn how to integrate recurring payments with PayU, a leading online
    payment service provider in India. Find out how to create, manage, and
    cancel subscriptions using PayU’s hosted checkout and APIs1
  keywords:
    - Recurring Payments Integration Introduction
    - PayU Subscription Management Introduction
    - Monthly Payment Processing Integration Introduction
    - PayU Recurring Payment Platform Integration
  robots: index
next:
  description: ''
---
<Callout icon="📘" theme="info">
  <NewBadge title="What's New!" asHeading={false} />



  RuPay Debit and Credit Cards are supported for Subscriptions.
</Callout>

The Subscriptions, Recurring Payments or Standing Instruction (SI) from PayU to set up and manage recurring payments. These recurring payments:

* Can be charged as per a cycle defined
* Do not require any customer intervention

The customer can instruct banks for regular funds transfers through standing instructions to automatically make payments. Recurring Payments is an easy and automated method to reduce the administrative burden for periodical payments. Based on the specified pay modes, the customer gives a mandate to the bank to debit a fixed amount from the customer’s account and pay to the merchant.

PayU offers Recurring Payments integration using the APIs, Zion Subscription platforms, or PayU Dashboard.

The following video describes PayU’s Recurring Payment Suite offering:

<Embed url="https://www.youtube.com/watch?v=5AfrrFg6CEQ" href="https://www.youtube.com/watch?v=5AfrrFg6CEQ" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252F5AfrrFg6CEQ%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253D5AfrrFg6CEQ%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252F5AfrrFg6CEQ%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

To enable subscription for your customer using various payment modes, it involves the following phases for each payment mode:

<Callout icon="👍" theme="okay">
  **Before you begin**: Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Callout>

* Cards
  1. [Cards Recurring Payment Consent Transaction](ref:credit-card-recurring-payment-consent-transaction)
  2. [Pre-Debit Notification API](ref:pre_debit_notification_api)
  3. [Recurring Payment Transaction API](ref:recurring_payment_api)
* Net Banking
  1. [Net Banking Recurring Payment Consent Transaction](ref:netbanking-recurring-payment-consent-transaction)
  2. [Recurring Payment Transaction API](ref:recurring_payment_api)
* UPI
  1. [UPI Recurring Payment Consent Transaction](ref:upi-recurring-payment-consent-transaction)
  2. [Pre-Debit Notification API](ref:pre_debit_notification_api)
  3. [Recurring Payment Transaction API](ref:recurring_payment_api)

## Choose the Method to Implement Subscription

PayU offers the following methods to implement subscriptions for your customers:

* [Using API Integration](doc:using-api-integration-recurring-payments)
* [Using Zion Subscription Automation](doc:using-zion-subscription-automation-platform)

<Callout icon="📘" theme="info">
  **Note**: You need to enable Subscription for your PayU account after choosing the model that suits you. Contact your PayU Key Account Manager to facilitate Subscription.
</Callout>

### Using Zion Subscription Automation Platform

PayU offers the Zion Subscription automation platform to seamlessly automate recurring payments with preferred credit or debit cards over a highly customizable and scalable platform with minimum integration efforts.

This integration is possible with a few code changes, and you can start accepting recurring payments. The rest of the subscription management, like Pre Debit, recurring will be taken care by Zion Subscription automation platform.

### Using API Integration

PayU provides Seamless integration (Merchant Hosted Checkout) and Non-seamless integration (PayU Hosted Checkout) using APIs. The same set of APIs is used for the various payment modes in the case of Seamless or Non-seamless integration. The following APIs are used to enable Subscription:

* **_payment** API and integration for each payment mode are:
  * [Cards Recurring Payment Consent Transaction](ref:credit-card-recurring-payment-consent-transaction)
  * [Net Banking Recurring Payment Consent Transaction](ref:netbanking-recurring-payment-consent-transaction)
  * [UPI Recurring Payment Consent Transaction](ref:upi-recurring-payment-consent-transaction)
* [Recurring Payment Transaction API](ref:recurring_payment_api)

The PayU Recurring Payment APIs are suitable where you want complete control of the Subscription and can invest in technical bandwidth for integration.

### Using Zero Code Change

PayU provides PayUBiz Dashboard to cater to all your payment integration without the knowledge of coding or zero code change. PayUBiz Dashboard allows you to:

* [Create a Payment Link with SI](doc:create-a-payment-link-with-si)
* [Bulk Upload of Payment Links with SI Registration](doc:bulk-upload-of-payment-links-with-si-registration)
* [Bulk Upload of Payment Links for Recurring Payments + Pre-Debit Notication](doc:bulk-upload-of-payment-links-for-recurring-payments-pre-debit-notication)

The PayUBiz Dashboard is suitable for integrating without investing in any technical integration. You can set up recurring through payment links or charge subsequent debits through bulk upload.

## Recurring platform

PayU’s recurring platform allows the merchant to offer a standing instruction feature for credit cards, selected debit cards, net banking, and UPI through various integration methods.

The PayU Standing Instructions suite of API automates repeat payments in the Subscription business. In the Subscription business, the billing amount and the billing cycle are fixed. The customer’s preferred payment instrument (credit card, debit card, net banking, or UPI) is charged regularly for a subscribed service.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-14-at-7.40.54-AM-1-2-1024x978.png)
