---
title: FAQs - Zion Integration
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## General

- What is the Zion Subscription Product?

  Zion is a subscription billing platform that allows merchants to automate recurring payments from customers based on predefined billing plans. It handles subscriptions, invoices, and recurring charges.

- What are the benefits of using the Zion Subscription Automation Platform? A: The Zion Subscription Automation Platform offers several benefits, including:
  - **Automated billing**: The platform automates the billing process, reducing the need for manual intervention.
  - **Flexible billing options**: Merchants can choose from a range of billing options such as daily, weekly, monthly, and yearly billing cycles.
  - **Customizable plans**: Merchants can create customized subscription plans based on their business needs.
  - **Payment gateway integration**: The platform integrates with multiple payment gateways, making it easy for merchants to accept payments from customers.
- Is there a cost associated with using the Zion Subscription Automation Platform?

Yes, there is a cost associated with using the Zion Subscription Automation Platform. However, the cost varies depending on your business needs and the features you require. You can contact PayU’s your PayU Key Account Manager to get a quote based on your requirements.

- How do I get started with the Zion Subscription Automation Platform? 

To get started with the Zion Subscription Automation Platform, you need to sign up for an PayU account, complete your onboarding, and then contact you PayU Key Account Manager (KAM).

- What are the main components of Zion?

 The main components are Plans, Subscriptions, and Invoices. Plans define billing amounts and frequencies. Subscriptions associate a customer with one or more plans. Invoices are the recurring charges executed on the customer's payment method per the subscription.

- What is the difference between PayU Zion platform and Recurring Payments offerings?

[block:parameters]
{
  "data": {
    "h-0": "Zion Subscription Automation",
    "h-1": "Recurring Payments",
    "0-0": "- Enables merchants to automate their subscription billing process.  \n- Provides features such as subscription management, payment processing, and more.  \n- Offers flexible billing options such as daily, weekly, monthly, and yearly billing cycles.  \n- Allows merchants to create customized subscription plans based on their business needs.  \n- Provides invoicing capabilities",
    "0-1": "- Refers to regular and automatic transactions where a predetermined amount is charged to a customer’s card at specified intervals.  \n- Allows merchants to offer their customers standing instruction feature for Credit Card, selected Debit cards and Net Banking (e-NACH and e-mandate), through various integration methods.  \n- Offers simple, transparent pricing.  \n- Enables recurring payments via multiple payment modes while being 100% compliant."
  },
  "cols": 2,
  "rows": 1,
  "align": [
    "left",
    "left"
  ]
}
[/block]


- What is the effort involved with PayU Zion platform in comparison with Recurring Payments?

[block:parameters]
{
  "data": {
    "h-0": "Zion Subscription Automation",
    "h-1": "Recurring Payments",
    "0-0": "Just call the Consent transaction and everything else is taking care by PayU.  \nHence, it is called Zion Subscription Automation platform. For more information, [Zion Workflow](doc:building-billing-experience-with-zion).",
    "0-1": "For Cards/UPI, the following is the flow:  \n   1. [Payment Consent Transaction with Merchant Hosted Checkout](ref:payment-consent-transaction-merchant-hosted)  \n   2. [Pre-Debit Notification API](ref:pre_debit_notification_api)  \n   3. [Recurring Payment Transaction API](ref:recurring_payment_api)  \nFor Net Banking, the following is the flow:  \n   1. [Net Banking Consent Transaction](ref:netbanking-recurring-payment-consent-transaction)  \n   2. [Recurring Payment Transaction API](ref:recurring_payment_api)  \n**Note**: The PayUBiz Dashboard can be used to set up the recurring payment transactions. For more information, refer to [Using PayUBiz Dashboard](doc:recurring-payments-using-payubiz-dashboard)."
  },
  "cols": 2,
  "rows": 1,
  "align": [
    "left",
    "left"
  ]
}
[/block]


- How does the billing process work with Zion?

 First a "consent transaction" occurs where the customer signs up and the merchant gets one-time authentication. After consent, Standing Instructions allow recurring charges without further customer approval. The merchant defines subscriptions, and Zion automatically generates invoices per the subscription plans, notifying the merchant through webhook.

- How are subscriptions started and ended?

 The merchant initiates a subscription using the Zion APIs. Subscriptions automatically end after all invoices related to the included plans are processed. Merchants can also allow customers to actively end subscriptions via their website/portal.

- What payment methods does Zion support for subscriptions?

 Zion leverages PayU's payment infrastructure and supports major credit cards, debit cards, Net Banking, and UPI payment methods.

- How does Zion handle failed or declined subscription payments?

 Zion will automatically retry and eventually notify you if a payment fails after multiple retries. The subscription status would be updated accordingly.

- Can subscriptions be changed mid-cycle?

  You can initiate plan changes on active subscriptions, which would take effect after the current billing cycle. This allows flexibility to upgrade/downgrade plans in real-time.

## Consent Transaction

Q: What is a consent transaction in Zion?

A: A consent transaction is the initial transaction where the customer signs up for a subscription and provides permission for recurring payments. It stores the payment details in PayU's vault.

Q: Why are consent transactions required?

A: Consent transactions are mandated by RBI guidelines for recurring payments without further customer approval. They capture the initial customer authentication.

Q: What should merchants check after a consent transaction?

A: Merchants should verify the status, card_token, payment_source and mihpayid values to confirm the transaction was authorized properly for future recurring billing.

Q: How are consent transactions implemented?

A: Merchants can process consent transactions using PayU's standard payment APIs. Zion can associate the authRefId later for subscriptions. For more information, refer to [Zion Workflow](doc:building-billing-experience-with-zion).

Q: Can consent transactions also capture the first payment?

A: Yes, consent transactions can deduct the first instalment or a deposit amount. They can also be penny transactions that are refunded.

Q: What is the authRefId in consent transactions?

A: The mihpayid or authRefId is a unique ID for the payment authorization. It is associated to the customer's subscription for future recurring billing.

Q: What data is required in consent transactions?

A: Consent transactions require user details like name, email, phone etc. Seamless transactions also require card details input on the merchant site.

Q: How are card details handled in consent transactions?

A: For seamless transactions, merchants need PCI compliance to handle card data directly. Non-seamless transactions can capture cards via PayU's hosted page.

Q: Do consent transactions support one-time or recurring payments?

A: Consent transactions support setting up future recurring payments. One-time payments would use a standard transaction flow.

Q: What happens when a consent transaction fails?

A: Failed consent transactions would prevent future recurring billing from being activated. The merchant would need to prompt the user to re-enter payment details.

Q: How are cards filtered for consent transactions?

A: Merchants can use PayU's BIN API to filter unsupported card types before consent transactions. This avoids rejections later on. For more information, refer to [Get Checkout Details API](ref:get_checkout_details).

Q: Can consent transactions be done separately from subscriptions?

A: Yes, merchants can perform the consent transaction first and then associate it to a subscription after. The authRefId links them.

Q: Do users need to authenticate every consent transaction?

A: For the initial payment setup, users would need to provide full authentication via OTP, passwords, etc. Recurring is automated.

Q: How does the recurring process work after consents?

A: After successful consent, Zion handles automatic subscription charges in the background per the defined billing plans.

Q: What happens if a user wants to change payment methods later?

A: Users would likely need to provide new consent for the updated payment details before the next recurring billing cycle.

Q: Are there timeout limits for consent transactions?

A: Consent authorizations may expire after some period. Users may need periodic re-authentication if no billings occur.

Q: Can discounts or promotions be applied to consent transactions?

A: Yes, any applicable discounts or promotional offers could be applied to the initial consent transaction amount.

Q: Are there any fees or charges associated with consent transactions?

A: PayU may have standard payment gateway fees that apply to consent transactions as the initial setup payment.

Q: Is PCI compliance required for seamless consent transactions?

A: Yes, any merchant capturing card data on their own site would need to be PCI compliant to handle cards securely.

Q: What credentials are required from the user for consent transactions?

A: Users would need to provide card details and authenticate with any security measures like OTP, passwords, etc.

Q: Is the consent process different for one-time vs. recurring payments?

A: One-time payments can use a standard transaction flow. Consent transactions are specific to recurring payment authorization.

Q: What happens if a card expires between recurring payments?

A: Users would need to re-authenticate with new card details before the next scheduled recurring payment.

## Invoices

Q: What are invoices in Zion?

A: Invoices are the recurring payment charges that are automatically triggered by Zion against the customer's payment instrument based on the subscription plans.

Q: How are invoices scheduled?

A: Invoices are scheduled based on the start date and billing frequency defined in each subscription plan. Zion triggers them independently for each plan.

Q: What invoice notifications does Zion send?

A: Zion sends invoice notifications for 'Due', 'Paid', and 'Failed' to the merchant's webhook URL. This keeps the merchant updated on the invoice status. For more information, refer to [Manage Invoice APIs](ref:manage-invoice-apis-for-zion).

Q: What happens if an invoice fails initially?

A: If an invoice payment fails, Zion will automatically retry for the next 3 days before sending a 'Failed' notification to the merchant.

Q: Can merchants manually trigger invoices?

A: Yes, merchants can call the **Create Invoice API **to trigger invoices, for example in ad-hoc billing models based on usage. For more information, refer to [Create Invoice API](ref:create-invoice-api-zion).

Q: How can merchants retrieve invoice details?

A: Zion provides APIs to fetch details of a single invoice by ID, or all invoices for a subscription via the subscription ID.

Q: What is the purpose of the refId parameter?

A: The refId is a unique ID provided by the merchant for each invoice. It links the invoice to the merchant's system.

## Plans

Q: What are plans in Zion?

A: Plans are billing templates that define pricing, frequency, and other details for subscription services. They allow reuse across customers.

Q: How are plans created?

A: Merchants can create plans using the **Create Plan** API by providing details like billing amount, cycle, interval, etc. Zion generates a unique plan ID. For more information, refer to [Create Plan API](ref:create-plan-api).

Q: Can plans be used across multiple subscriptions?

A: Yes, plans are templates that can be associated to multiple customer subscriptions to standardize billing for a service.

Q: How are plans associated with subscriptions?

A: Plans can be linked to a subscription during creation via the plan ID. They can also be added to existing subscriptions.

Q: Can billing details be overridden in subscriptions?

A: No, subscriptions inherit the billing settings from associated plans. Custom billing requires creating plans with specific amounts.

Q: How can merchants change or delete plans?

A: The **Update Plan** and** Delete Plan** APIs allow modifying and removing existing plans as needed. Deleting stops usage in subscriptions. For more information, refer to [Update Existing Plan for Subscription API](ref:update-existing-plan-for-subscription-api) or [Delete a Plan](ref:delete-a-plan).

Q: What happens if a used plan is deleted?

A: Deleting a plan stops its billing in any associated subscriptions. This can disrupt subscriber services.