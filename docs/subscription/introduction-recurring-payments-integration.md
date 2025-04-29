---
title: Introduction
excerpt: ''
deprecated: false
hidden: true
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
The Recurring Payments or Standing Instruction (SI) is the mode of payment agreed by the customer to pay against a package for each payment term during the subscription. The customer can instruct banks for regular funds transfers through standing instructions to automatically make payments.  
Recurring Payments is an easy and automated method to reduce the administrative burden for periodical payments. Based on the specified pay modes, the customer gives a mandate to the bank to debit a fixed amount from the customer’s account and pay to the merchant.

PayU offers Recurring Payments integration using the APIs, Zion Subscription platforms, or PayU Dashboard.

The following video describes PayU’s Recurring Payment Suite offering:

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2F5AfrrFg6CEQ%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D5AfrrFg6CEQ&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2F5AfrrFg6CEQ%2Fhqdefault.jpg&key=7788cb384c9f4d5dbbdbeffd9fe4b92f&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=5AfrrFg6CEQ",
  "title": "PayU Recurring Payment Suite - Automate Payment Collection From Your Customers",
  "favicon": "https://www.google.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/5AfrrFg6CEQ/hqdefault.jpg",
  "provider": "youtube.com",
  "href": "https://www.youtube.com/watch?v=5AfrrFg6CEQ",
  "typeOfEmbed": "youtube"
}
[/block]


To enable subscription for your customer using various payment modes, it involves the following phases for each payment mode:

> 👍 Before you begin:
> 
> Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](https://docs.payu.in/v1/docs/register-for-a-merchant-account-on-dashboard).

- Cards
  1. [Cards Recurring Payment Consent Transaction](ref:credit-card-recurring-payment-consent-transaction)
  2. [Pre-Debit Notification API](ref:pre_debit_notification_api)
  3. [Recurring Payment Transaction API](ref:recurring_payment_api)
- Net Banking
  1. [Net Banking Recurring Payment Consent Transaction](ref:netbanking-recurring-payment-consent-transaction)
  2. [Recurring Payment Transaction API](ref:recurring_payment_api)
- UPI
  1. [UPI Recurring Payment Consent Transaction](ref:upi-recurring-payment-consent-transaction)
  2. [Pre-Debit Notification API](ref:pre_debit_notification_api)
  3. [Recurring Payment Transaction API](ref:recurring_payment_api)

## Recurring platform

PayU’s recurring platform allows the merchant to offer a standing instruction feature for credit cards, selected debit cards, net banking, and UPI through various integration methods.

The PayU Standing Instructions suite of API automates repeat payments in the Subscription business. In the Subscription business, the billing amount and the billing cycle are fixed. The customer’s preferred payment instrument (credit card, debit card, net banking, or UPI) is charged regularly for a subscribed service.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-14-at-7.40.54-AM-1-2-1024x978.png)