---
title: '[Review]Subscriptions or Recurring Payments'
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
---
## What are Recurring Payments?

Recurring payments allow businesses to automatically collect payments from customers at regular intervals without requiring manual intervention each time. Using Standing Instructions (SI), customers provide one-time consent for future transactions, enabling seamless automation of subscriptions billing, EMIs, utility payments, and more.

## Why Choose PayU Subscriptions?

**Seamless Customer Experience**

* One-time setup with automatic recurring charges
* No need to re-enter payment details for future transactions

**Flexible Integration**

* Choose from API integration, platform-based solutions, or zero-code dashboard options
* Adapt to your business technical capabilities and requirements

**Multi-Modal Support**

* Credit Cards with full automation
* Debit Cards with enhanced security
* Net Banking with direct bank integration
* UPI with universal app support

**Automated Notifications**

* Pre-debit alerts and transaction confirmations
* Real-time transaction updates across all payment modes

The following video describes PayU’s Recurring Payment Suite offering:

<Embed typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=5AfrrFg6CEQ" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252F5AfrrFg6CEQ%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253D5AfrrFg6CEQ%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252F5AfrrFg6CEQ%252Fhqdefault.jpg%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" href="https://www.youtube.com/watch?v=5AfrrFg6CEQ" providerUrl="https://www.youtube.com/" providerName="YouTube" />

## Available Payment Modes

<Image align="center" border={true} src="https://files.readme.io/21e3111ac286ec2702594a9c0764ff5cec67be250de5b2f89c844abcb73dccba-subscriptions_supported_payment_modes.png" className="border" />

The following table provides comparison on various payment mode integration:

| Payment Mode     | Consent Required | Pre-debit Notifications | Instant Setup     |
| ---------------- | ---------------- | ----------------------- | ----------------- |
| **Credit Cards** | ✅ Yes            | ✅ Available             | ✅ Yes             |
| **Debit Cards**  | ✅ Yes            | ✅ Available             | ✅ Yes             |
| **Net Banking**  | ✅ Yes            | ❌ Not available         | ⚠️ Varies by bank |
| **UPI**          | ✅ Yes            | ✅ Available             | ✅ Yes             |

## Use Cases

**Subscriptions Services**

* Streaming platforms and digital content
* Software licenses and SaaS applications
* Magazine and content subscriptions

**Utility & Essential Services**

* Monthly utility bill payments
* Insurance premium collections

**Financial Products**

* Loan EMIs and installment payments
* Membership fees for clubs and organizations

<Callout icon="👍" theme="okay">
  **Example:** Ashish subscribed to a magazine on the BeSpoke Online Magazine platform. When a special edition became available, he was able to purchase it seamlessly using his stored payment method through a Pre-Debit Transaction without providing new payment consent.
</Callout>

## &#x20;Industry-Specific Solutions

### &#x20;Media & Entertainment

**Netflix-style Streaming Platform**

* Monthly plans: ₹199, ₹499, ₹649
* Annual discounts: 2 months free
* Family sharing options
* Automatic renewal with email notifications

### &#x20;Fitness & Wellness

**Gym Chain Subscriptions**

* Monthly membership: ₹1,500
* Personal training add-ons: ₹500/session
* Locker rental: ₹200/month
* Automatic renewal with 3-day grace period

### &#x20;Education & E-learning

**Online Course Platform**

* Course subscriptions: ₹999/month access to all courses
* Certification programs: ₹299/month for 6 months
* Live session add-ons: ₹150/session
* Student discount programs

### &#x20;E-commerce & Retail

**Subscriptions Box Service**

* Monthly beauty box: ₹599
* Quarterly snack box: ₹1,200
* Customizable preferences
* Pause/resume functionality

#### &#x20;Financial Services

**Insurance Premium Collection**

* Monthly health insurance: ₹1,500
* Quarterly life insurance: ₹3,000
* Annual vehicle insurance: ₹8,000
* Automated reminder system

#### &#x20;SaaS & Software

**Business Tools Subscriptions**

* Basic plan: ₹500/month for 5 users
* Pro plan: ₹1,000/month for 20 users
* Enterprise: Custom pricing
* Usage-based billing for API calls

## &#x20;Billing Models Supported

| Billing Model                            | How It Works                                                                                                 | Best Suited For                                                        | Example                                                                    | How to use this feature?                                                                                |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Fixed Frequency, Fixed Amount            | A fixed amount is auto-debited at a regular frequency - monthly, quarterly, or yearly                        | OTT platforms, SaaS tools, gyms, insurance renewals                    | ₹499 debited every month for a streaming plan.                             | In the request, pass ‘billingCycle’ as DAILY/WEEKLY/ <br />MONTHLY/YEARLY and amount in ‘billingAmount’ |
| Fixed Frequency, Variable Amount         | Payments occur at a fixed frequency, but the amount changes based on usage or consumption                    | Usage-based, telecom/data services, flexible EMIs                      | 5th of every month, debit amount varies based on actual usage              | In the request, pass ‘billingCycle’ as DAILY/WEEKLY/<br /> MONTHLY/YEARLY and amount in ‘billingAmount’ |
| Flexible Frequency, Variable Amount      | Payments are triggered as needed - there’s no fixed frequency or amount. The merchant decides when to charge | EdTech installment plans, loans with variable EMIs, donation platforms | ₹15,000 collected in April, ₹10,000 in June, from the same active mandate. | In the request, pass ‘billingCycle’ as ADHOC and amount in ‘billingAmount’                              |
| One-Time Payment, Fixed/ Variable Amount | Payment occurs only once in the mandate life cycle                                                           | Ecommerce where amount is deducted when the product is delivered       | ₹1,600 to be deducted when your furniture is delivered                     | In the request, pass ‘billingCycle’ as ONCE and amount in ‘billingAmount’                               |

## Integration Options

Choose the approach that fits your technical capabilities:

**Zero Code Dashboard Integration**

* **Best for**: Businesses with limited technical resources
* **Method**: Dashboard or CSV-based operations
* **Features**: Payment link creation, bulk uploads, automated notifications

For more information, refer to [Subscriptions Dashboard](doc:subscription-dashboard).

**API Integration**

* **Best for**: Developers requiring full control
* **Method**: Comprehensive API suite
* **Features**: Complete subscriptions workflow management

For more information, refer to [Using API Integration](doc:using-api-integration-recurring-payments)

**Zion Subscription Automation Platform**

* **Best for**: Enterprises requiring minimum technical effort
* **Method**: Platform-based automation
* **Features**: Maximum automation with enterprise-grade capabilities

For more information, refer to [Using Zion Subscription Automation](doc:using-zion-subscription-automation-platform)

The following table provides comparison of the above integrations:

| Variant                              | When to Pick                   | Merchant Suitability    | Trade-offs                   | Supported Payment Modes             | Integration Effort |
| ------------------------------------ | ------------------------------ | ----------------------- | ---------------------------- | ----------------------------------- | ------------------ |
| Zero-code / Dashboard / Payment Link | Fastest go-live, no dev needed | Small businesses, NGOs  | Limited customization        | Cards, UPI, NetBanking              | Minimal            |
| API-first / Full Control             | Custom flows, automation       | SaaS, large enterprises | More dev effort, max control | All (Cards, UPI, NetBanking, eNACH) | High               |
| Hybrid (Dashboard + API)             | Some automation + dashboard    | Growing businesses      | Balanced, some manual steps  | As enabled in both                  | Moderate           |
| Zion Plan Management                 | Complex plans, analytics       | Marketplaces, platforms | Advanced, onboarding needed  | As supported by Zion                | Varies             |

## Getting Started

* **Account Requirements:**:
  * **Active PayU Merchant Account**: [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard)
  * **Subscriptions Feature Enabled**: Contact PayU Key Account Manager or<Anchor label=" PayU Support" target="_blank" href="https://help.payu.in"> PayU Support</Anchor> for activation
* **Technical Setup:**: Choose between [API](doc:using-api-integration-recurring-payments), [Zion Subscription Automation](doc:using-zion-subscription-automation-platform), or [Dashboard](doc:subscription-dashboard) approach
* **Technical Requirements** (varies by integration method):
  * [API key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard) (for API integration)
  * [Webhook endpoints configuration](doc:webhooks)
  * Dashboard access (for zero-code implementation)

<br />
