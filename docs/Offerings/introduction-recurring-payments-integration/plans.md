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

A plan defines the subscription terms that the customer accepts before a Standing Instruction (SI) mandate is registered. In API-based SI integrations, the plan is managed by your system and shared with PayU during the consent transaction through `si_details`.&#x20;

A **plan** contains all subscription details except customer and payment method information. It defines:

- Billing amount (how much to charge)
- Billing type (recurring or one-time)
- Plan description and merchant reference

PayU does not require you to create a separate plan object before registering an SI mandate. Your frontend should maintain the plan configuration, show it to the customer, pass the approved values to PayU during consent, and use the returned mandate identifiers for future pre-debit notifications, recurring debits, and mandate management.

<Callout icon="📘" theme="info">
  ### **Handy Tips**

  - Creating a plan is optional - you can create a subscription without creating a plan
  - You can create multiple subscriptions for a plan
</Callout>

**How Plan Becomes a Subscription:**
When you associate a plan with a customer and their payment method, it becomes a **subscription**. The merchant defines the subscription plan, and the customer subscribes to it by providing their payment details and consent.

<Callout icon="far fa-tick" theme="success">
  ### For Example

  - You create a **Premium Monthly ₹499** plan (just a billing template)
  - Customer A subscribes → Plan + Customer A's details + Payment Method = Subscription A
  - Customer B subscribes → Same Plan + Customer B's details + Payment Method = Subscription B
</Callout>

***

## Plan vs Subscription

| Aspect                          | Plan                                               | Subscription                                                       |
| ------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------ |
| **What is it?**                 | Subscription template with billing details only    | Plan + Customer details + Payment method                           |
| **Who creates it?**             | Merchant (via Dashboard or API)                    | Customer (by subscribing to a plan with their payment details)     |
| **When is it created?**         | Before customer sees the offer                     | After customer provides payment details and consent                |
| **What does it contain?**       | Billing amount, billing type, plan description     | Plan details + Customer information + Payment method + Mandate     |
| **Can it exist independently?** | Yes, as a reusable template for multiple customers | No, must be linked to a specific customer and their payment method |
| **Purpose**                     | Define the billing terms that can be reused        | Active billing arrangement for a specific customer                 |
| **Example**                     | "Premium Monthly ₹499" plan                        | Customer A subscribed to "Premium Monthly ₹499" using their card   |

***

### When Should You Create Plans?

You should create plans when you want to:

- **Offer standardized subscription packages**: Create reusable billing templates (e.g., "Basic ₹199/month", "Premium ₹499/month", "Enterprise ₹999/month") that multiple customers can subscribe to
- **Enable self-service subscriptions**: Allow customers to choose and subscribe to pre-defined plans without manual setup for each customer
- **Simplify subscription management**: Manage billing terms centrally - update a plan once, and it applies to all new subscriptions
- **Generate payment links for subscriptions**: Create shareable links where customers select a plan, provide their details, and complete payment to create their subscription

<Callout icon="📘" theme="info">
  ### **Note**

  Plans are templates. You do not need plans if you are creating a unique, one-off billing arrangements for each customer via API.
</Callout>

***

### Use Cases for Plan-based Subscriptions

<Cards>
  <Card title="SaaS & Digital Services" icon="fa-laptop-code">
    Define tiered plans (Basic, Pro, Enterprise). Customers subscribe by selecting a plan and providing payment details.
  </Card>

  <Card title="OTT & Streaming Platforms" icon="fa-tv">
    Create content package plans. Each customer subscription links to the plan with their specific payment method.
  </Card>

  <Card title="Membership & Clubs" icon="fa-users">
    Set up membership plans. Multiple customers subscribe to the same plan with their individual payment methods.
  </Card>

  <Card title="Utility & Service Providers" icon="fa-bolt">
    Define recurring payment plans for utilities or services. Each subscription created when customer provides payment details.
  </Card>
</Cards>

***

## Prerequisites

Enable Subscriptions for your PayU merchant account. Contact your PayU Key Account Manager or onboarding team before integrating SI plans.

***

## Benefits of Using Plans

Using plans provides merchants with a structured approach to managing subscription-based recurring payments.

<Accordion title="Plan Benefits" icon="fa-list-check">
  <ul><li><strong>Reusable subscription templates:</strong> Create once, use for multiple customers with the same billing terms, reducing setup errors and saving time.</li>
  <li><strong>Better dashboard controls:</strong> Manage all subscriptions from a centralized dashboard with clear visibility into plan status and associated subscriptions.</li>
  <li><strong>Improved reconciliation:</strong> Plan ID or merchant reference, mandate ID, and transaction IDs can be mapped together for easier reporting and tracking.</li>
  <li><strong>Safer modifications:</strong> Separate draft plan edits from active subscription changes, ensuring you don't accidentally modify live billing arrangements.</li>
  <li><strong>Simplified subscription link generation:</strong> Quickly create payment links for customers to subscribe to predefined plans without recreating billing details each time.</li></ul>
</Accordion>

***

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

***

## Access Plans

You can access **Plans** under **Subscriptions&#x20;**&#x66;rom the left navigation as shown below.


<Image src="https://files.readme.io/ceab99a98c18eb24f14d434f5159d4a6ae066d810e940e9f32828515fee74cc7-plan-management.gif" alt="Access Plans" align="center" caption="_Access Plans_" border={true} />


***

## Plan Management Actions

From the PayU Dashboard, you can perform the following plan management actions:

- <Anchor target="_blank" href="https://docs.payu.in/docs/internal-review-create-and-manage-plans#create-a-plan">Create a plan</Anchor>
- <Anchor target="_blank" href="https://docs.payu.in/docs/internal-review-create-and-manage-plans#duplicate-a-plan">Duplicate a plan</Anchor>
- <Anchor target="_blank" href="https://docs.payu.in/docs/internal-review-create-and-manage-plans#edit-a-plan">Edit a plan</Anchor>
- <Anchor target="_blank" href="https://docs.payu.in/docs/internal-review-create-and-manage-plans#deactivate-a-plan">Deactivate a plan</Anchor>
- <Anchor target="_blank" href="https://docs.payu.in/docs/internal-review-create-and-manage-plans#create-subscriptions-for-a-plan">Create a subscription from a plan</Anchor>

For detailed step-by-step instructions, refer to <Anchor target="_blank" href="https://docs.payu.in/docs/internal-review-create-and-manage-plans">Create and Manage Plans</Anchor>.

***

## Frequently Asked Questions (FAQs)

Find answers to frequently asked questions about plans and subscription management.

### Understanding Plans

1. #### What is a plan?
   <Accordion title="Answer" icon="fa-comment-dots">
     A plan is a subscription template that contains all subscription billing details except customer and payment method information. It includes billing amount, billing type (recurring or one-time), and plan description. When a plan is associated with a customer and their payment method, it becomes a subscription. Plans are created by merchants via the PayU Dashboard or APIs and can be reused for multiple customer subscriptions.
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

3. #### What is the difference between a plan and a subscription?
   <Accordion title="Answer" icon="fa-comment-dots">
     <strong>Plan:</strong> A billing template containing subscription details minus customer and payment method information (created by merchant).<br /> <strong>Subscription:</strong> Plan + Customer details + Payment method (created when customer subscribes).<br /><br /> <strong>Example:</strong> You create a "Premium Monthly ₹499" plan. When Customer A subscribes by providing their card details and consent, a subscription is created linking the plan to Customer A's card. The same plan can be used when Customer B subscribes with their own payment details, creating a separate subscription.
   </Accordion>

4. #### Can a customer have multiple subscriptions?
   <Accordion title="Answer" icon="fa-comment-dots">
     Yes, a customer can subscribe to multiple plans. Each time they subscribe, a new subscription is created that links the plan to their payment method. For example, a customer might subscribe to both an "OTT Basic ₹199" plan and a "Cloud Storage ₹99" plan, creating two separate subscriptions with their own billing schedules.
   </Accordion>

5. #### Is plan status the same as subscription status?
   <Accordion title="Answer" icon="fa-comment-dots">
     No. Plan status is merchant-controlled (Draft, Active, Archived) and indicates whether the billing template is available for creating new subscriptions. Subscription status is customer-specific and indicates the state of an individual customer's subscription (Active, Paused, Cancelled, Expired).
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

<br />

***

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
