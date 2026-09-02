---
title: '[INTERNAL REVIEW] Plans'
excerpt: >-
  Learn how to create, manage, activate, and update SI subscription plans using
  PayU Dashboard and APIs. Explore plan lifecycle, statuses, recurring billing
  flows, integration steps, request parameters, error handling, and best
  practices.
deprecated: false
hidden: true
metadata:
  title: SI Plan Management - Create, Update & Manage Subscription Plans | PayU Docs
  description: >-
    Learn how to create, manage, activate, and update SI subscription plans
    using PayU Dashboard and APIs. Explore plan lifecycle, statuses, recurring
    billing flows, integration steps, request parameters, error handling, and
    best practices.
  keywords:
    - PayU SI Plan
    - PayU subscription plans
    - recurring payment plans
    - subscription integration API
    - SI plan management
    - PayU recurring billing
    - plan lifecycle API
    - PayU mandate plans
    - create subscription plans
    - recurring payments API
    - PayU subscriptions
    - SI integration docs
    - subscription management API
    - PayU developer docs
    - recurring billing integration
  robots: index
---
## What is a Plan?

A **plan** is a predefined subscription template that defines the billing terms for recurring payments. It includes:

- Billing amount (how much to charge)
- Billing frequency (daily, weekly, monthly, yearly)
- Billing interval (every X days/weeks/months/years)
- Plan description and merchant reference

Plans are created and managed by merchants either through the PayU Dashboard or via APIs. Once created, a plan can be used to generate multiple subscription payment links for different customers.

<Callout icon="📘" theme="info">
  ### **Handy Tips**

  - Creating a plan is optional - you can create a subscription without creating a plan
  - You can create multiple subscriptions for a plan
</Callout>

## Plan vs Mandate

| Aspect                          | Plan                                                     | Mandate                                                        |
| ------------------------------- | -------------------------------------------------------- | -------------------------------------------------------------- |
| **What is it?**                 | Subscription billing template defining terms and pricing | Customer's authorization to debit their account automatically  |
| **Who creates it?**             | Merchant (via Dashboard or API)                          | Customer (by providing consent during payment)                 |
| **When is it created?**         | Before customer sees the subscription offer              | After customer approves the subscription terms                 |
| **What does it contain?**       | Billing amount, frequency, interval, description         | Customer consent, payment instrument token, mandate ID, status |
| **Can it exist independently?** | Yes, as a reusable template                              | No, must be linked to a customer and payment method            |
| **Purpose**                     | Define what and when to charge                           | Authorize PayU to execute recurring charges                    |

### When Should You Create Plans?

You should create plans when:

- **You offer subscription-based services**: SaaS products, OTT platforms, memberships, digital content subscriptions
- **You have recurring billing cycles**: Monthly fees, annual renewals, quarterly payments
- **You need reusable billing templates**: Same plan used for multiple customers (e.g., "Premium Monthly ₹499")
- **You want dashboard-based subscription management**: Non-technical teams managing subscriptions via PayU Dashboard
- **You generate subscription payment links**: Creating shareable links for customers to subscribe

### Use Cases for Plan-Based Subscriptions

<Cards>
  <Card title="SaaS & Digital Services" icon="fa-laptop-code">
    Create plans for different subscription tiers (Basic, Pro, Enterprise) with monthly or annual billing cycles.
  </Card>

  <Card title="OTT & Streaming Platforms" icon="fa-tv">
    Define plans for different content packages with recurring charges for continued access.
  </Card>

  <Card title="Membership & Clubs" icon="fa-users">
    Set up plans for gym memberships, club subscriptions, or loyalty programs with fixed recurring fees.
  </Card>

  <Card title="Utility & Service Providers" icon="fa-bolt">
    Create plans for recurring utility payments, insurance premiums, or maintenance fees.
  </Card>
</Cards>

## Prerequisites

- Enable Subscriptions for your PayU merchant account. Contact your PayU Key Account Manager or onboarding team before integrating SI plans.

## Benefits of Using Plans

Using plans provides merchants with a structured approach to managing subscription-based recurring payments.

<Accordion title="Plan Benefits" icon="fa-list-check">
  <ul><li><strong>Reusable subscription templates:</strong> Create once, use for multiple customers with the same billing terms, reducing setup errors and saving time.</li>
  <li><strong>Better dashboard controls:</strong> Manage all subscriptions from a centralized dashboard with clear visibility into plan status and associated subscriptions.</li>
  <li><strong>Improved reconciliation:</strong> Plan ID or merchant reference, mandate ID, and transaction IDs can be mapped together for easier reporting and tracking.</li>
  <li><strong>Safer modifications:</strong> Separate draft plan edits from active subscription changes, ensuring you don't accidentally modify live billing arrangements.</li>
  <li><strong>Simplified subscription link generation:</strong> Quickly create payment links for customers to subscribe to predefined plans without recreating billing details each time.</li></ul>
</Accordion>

## Plan Lifecycle and Statuses

Plans in PayU can have the following statuses during their lifecycle:

<Cards>
  <Card title="Draft" icon="fa-file-pen" iconColor="#0c6150">
    Plans saved in the system but not yet activated. Draft plans cannot be used to create subscriptions. Use this status to prepare plans before making them available.
  </Card>

  <Card title="Active" icon="fa-circle-check" iconColor="#0c6150">
    Plans that are activated and immediately available for creating subscription payment links. Active plans can have subscriptions associated with them.
  </Card>

  <Card title="Archived" icon="fa-box-archive" iconColor="#666">
    Plans that have been deactivated. Archived plans cannot be used for new subscriptions but can be duplicated to create new plans with similar settings.
  </Card>
</Cards>

**Status Workflow:** Draft → Active → Archived (via deactivation)

## Access Plans

You can access **Plans** under **Subscriptions&#x20;**&#x66;rom the left navigation as shown below.


<Image src="https://files.readme.io/ceab99a98c18eb24f14d434f5159d4a6ae066d810e940e9f32828515fee74cc7-plan-management.gif" alt="Access Plans" align="center" caption="_Access Plans_" border={true} />


## Plan Management Actions

From the PayU Dashboard, you can perform the following plan management actions:

- <Anchor target="_blank" href="https://docs.payu.in/docs/internal-review-create-and-manage-plans#create-a-plan">Create a plan</Anchor>
- <Anchor target="_blank" href="https://docs.payu.in/docs/internal-review-create-and-manage-plans#duplicate-a-plan">Duplicate a plan</Anchor>
- <Anchor target="_blank" href="https://docs.payu.in/docs/internal-review-create-and-manage-plans#edit-a-plan">Edit a plan</Anchor>
- <Anchor target="_blank" href="https://docs.payu.in/docs/internal-review-create-and-manage-plans#deactivate-a-plan">Deactivate a plan</Anchor>
- <Anchor target="_blank" href="https://docs.payu.in/docs/internal-review-create-and-manage-plans#create-subscriptions-for-a-plan">Create a subscription from a plan</Anchor>

For detailed step-by-step instructions, refer to <Anchor target="_blank" href="https://docs.payu.in/docs/internal-review-create-and-manage-plans">Create and Manage Plans</Anchor>.

## Frequently Asked Questions (FAQs)

Find answers to frequently asked questions about plans and subscription management.

### Understanding Plans

1. #### What is a plan?
   <Accordion title="Answer" icon="fa-comment-dots">
     A plan is a reusable subscription template that defines billing terms for recurring payments. It specifies the billing amount, frequency (daily, weekly, monthly, yearly), and interval for charging customers. Plans are created by merchants via the PayU Dashboard or APIs and can be used to generate multiple subscription payment links.
   </Accordion>

2. #### When should I create plans?
   <Accordion title="Answer" icon="fa-comment-dots">
     Create plans when you offer subscription-based services with recurring billing cycles. Plans are ideal for:

       <ul>
       <li><strong>SaaS platforms and digital services:</strong> Software subscriptions with monthly/annual billing</li>
       <li><strong>OTT and streaming platforms:</strong> Content access with recurring charges</li>
       <li><strong>Membership programs:</strong> Gym memberships, club subscriptions, loyalty programs</li>
       <li><strong>Utility and service providers:</strong> Insurance premiums, utility bills, maintenance fees</li>
       </ul>

     Plans work best when you need reusable billing templates or want non-technical teams to manage subscriptions via the Dashboard.
   </Accordion>

3. #### What is the difference between a plan and a mandate?
   <Accordion title="Answer" icon="fa-comment-dots">
     <strong>Plan:</strong> A subscription template defining what to charge and how often (created by merchant before customer sees the offer).<br /> <strong>Mandate:</strong> Customer's authorization to automatically debit their payment method (created after customer provides consent).<br /><br /> <strong>Example:</strong> You create a "Premium Monthly" plan for ₹499/month. When a customer subscribes and completes payment consent, a mandate is created that authorizes PayU to charge ₹499 from their card every month.
   </Accordion>

4. #### Can a customer have multiple plans?
   <Accordion title="Answer" icon="fa-comment-dots">
     Yes, a customer can subscribe to multiple plans. Each subscription creates a separate mandate linked to that specific plan. For example, a customer might have an "OTT Basic" plan and a "Cloud Storage" plan, each with its own mandate and billing schedule.
   </Accordion>

5. #### Is plan status the same as mandate status?
   <Accordion title="Answer" icon="fa-comment-dots">
     No. Plan status is merchant-controlled (Draft, Active, Archived) and indicates template availability. Mandate status is ecosystem-controlled (Active, Cancelled, Paused) and indicates whether automatic debits are authorized for a specific customer subscription.
   </Accordion>

6. #### How does billing cycle configuration work?
   <Accordion title="Answer" icon="fa-comment-dots">
     Billing cycle is configured using two parameters:<br /> <strong>Billing Cycle:</strong> The unit of time (DAILY, WEEKLY, MONTHLY, YEARLY)<br /> <strong>Billing Interval:</strong> How many units between charges<br /><br /> <strong>Examples:</strong>

       <ul>
       <li>Monthly subscription: billingCycle=MONTHLY, billingInterval=1</li>
       <li>Quarterly subscription: billingCycle=MONTHLY, billingInterval=3</li>
       <li>Every 3 days: billingCycle=DAILY, billingInterval=3</li>
       <li>Bi-weekly: billingCycle=WEEKLY, billingInterval=2</li>
       </ul>
   </Accordion>

### Managing Plans

1. #### What is the difference between Draft and Active plans?
   <Accordion title="Answer" icon="fa-comment-dots">
     <strong>Draft:</strong> Plans that are saved but not activated. Cannot be used to create subscriptions. Use this status to prepare plans before making them available.<br /> <strong>Active:</strong> Plans that are activated and ready to use. Can be used to create subscription payment links immediately.
   </Accordion>

2. #### Can I edit a plan?
   <Accordion title="Answer" icon="fa-comment-dots">
     Yes, you can edit plans through the PayU Dashboard. However, certain fields may have editing restrictions depending on whether the plan has active subscriptions. For details, refer to [Edit a Plan](doc:internal-review-create-and-manage-plans#edit-a-plan).
   </Accordion>

3. #### Can I delete a plan?
   <Accordion title="Answer" icon="fa-comment-dots">
     No, you cannot permanently delete a plan. However, you can deactivate it, which moves the plan to <strong>Archived</strong> status. Archived plans cannot be used for new subscriptions but can be duplicated to create new plans with similar settings.
   </Accordion>

4. #### Can I duplicate a plan?
   <Accordion title="Answer" icon="fa-comment-dots">
     Yes, you can duplicate any plan (Draft, Active, or Archived) to create a new plan with the same configuration. When duplicating, you must provide a unique Plan ID for the new plan. This is useful for creating similar plans with minor variations.
   </Accordion>

5. #### Can I pause or resume a plan?
   <Accordion title="Answer" icon="fa-comment-dots">
     No, plans do not have pause/resume functionality. Plans can only be in Draft, Active, or Archived status. To temporarily stop using a plan, deactivate it (moves to Archived). To use it again, duplicate it to create a new active plan.
   </Accordion>

6. #### Can I edit a plan that has active subscriptions?
   <Accordion title="Answer" icon="fa-comment-dots">
     Yes, you can edit plans with active subscriptions, but changes to certain fields like billing amount or billing cycle may only apply to new subscriptions created after the edit. Existing active subscriptions typically continue with their original plan terms. For specific field-level edit restrictions, refer to the plan management documentation.
   </Accordion>
