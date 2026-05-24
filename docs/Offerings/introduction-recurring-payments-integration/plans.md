---
title: Plans
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
A plan defines the subscription terms that the customer accepts before a Standing Instruction (SI) mandate is registered. In API-based SI integrations, the plan is managed by your system and shared with PayU during the consent transaction through `si_details`.

PayU does not require you to create a separate plan object before registering an SI mandate. Your frontend should maintain the plan configuration, show it to the customer, pass the approved values to PayU during consent, and use the returned mandate identifiers for future pre-debit notifications, recurring debits, and mandate management.

You can create a plan:

- From PayU dashboard.
- Using APIs.

> 📘 **Handy Tips**
>
> - Creating a plan is optional. You can create a subscription without creating a plan.
> - You can create multiple subscriptions for a plan.

## Prerequisites

- Enable Subscriptions for your PayU merchant account. Contact your PayU Key Account Manager or onboarding team before integrating SI plans.

## Benefits of a Plan

Using a plan gives merchants a structured way to manage SI subscriptions.

<Accordion title="Plan Benefits" icon="fa-list-check">
<ul><li><strong>Clear customer consent:</strong> The customer sees the amount, frequency, start date, and end date before approving the mandate.</li>
<li><strong>Consistent billing schedule:</strong> Your system can calculate upcoming debit dates from the plan instead of relying on manual inputs for every cycle.</li>
<li><strong>Easier pre-debit management:</strong> The plan provides the amount and due date needed to trigger pre-debit notifications on time.</li>
<li><strong>Faster recurring payment operations:</strong> Merchants can trigger debits from a saved plan and mandate mapping instead of recreating payment details.</li>
<li><strong>Better dashboard controls:</strong> The frontend can show plan status, next debit date, last debit status, and allowed actions in one place.</li>
<li><strong>Improved reconciliation:</strong> Plan ID or merchant reference, mandate ID, invoice number, and transaction IDs can be mapped together for reports.</li>
<li><strong>Safer modifications and cancellations:</strong> Merchants can separate draft edits from active mandate changes and use the correct PayU APIs for supported updates.</li>
<li><strong>Reusable subscription setup:</strong> Common plan templates can reduce errors when merchants create similar subscriptions for multiple customers.</li>
<li><strong>Better customer support:</strong> Support teams can quickly see what the customer approved, when the next charge is due, and why a debit succeeded or failed.</li></ul>

</Accordion>

## Plan Status

Every plan goes through the following statuses:

<Cards>
  <Card title="Draft" icon="fa-file-pen" iconColor="#0c6150">
    Plans are saved in the system but not active. You cannot use draft plans for subscriptions until they are activated.
  </Card>

  <Card title="Active" icon="fa-circle-check" iconColor="#0c6150">
    A plan becomes active once it is created and immediately available for creating subscriptions.
  </Card>
</Cards>

## Access Plans

You can access **Plans** under **Subscriptions&#x20;**&#x66;rom the left navigation as shown below.


<Image src="https://files.readme.io/ceab99a98c18eb24f14d434f5159d4a6ae066d810e940e9f32828515fee74cc7-plan-management.gif" alt="Access Plans" align="center" caption="_Access Plans_" border={true} />


## Dashboard Actions

- Create a plan
- Duplicate a plan
- Edit a plan
- Deactivate a plan
- Create a Subscription

# Frequently Asked Questions (FAQs)

Find answers to frequently asked questions about SI plans.

### SI Plan Basics

1. #### What is an SI plan?
   <Accordion title="Answer" icon="fa-comment-dots">
   An SI Plan is the billing schedule and amount that your customer agrees to before a Standing Instruction mandate is registered. In this API-based flow, the plan is maintained in your system and passed to PayU as `si_details` during consent.<br/>
   <strong>Best Practice:</strong> Keep a unique merchant-side plan reference so support, reconciliation, and retries can be traced back to the exact plan shown to the customer
   </Accordion>
2. #### When should I create a plan?
   <Accordion title="Answer" icon="fa-comment-dots">
   Create the plan before initiating consent, after the customer has selected the subscription terms but before calling the consent transaction API.<br/>
   **Best Practice:** Move a plan from Draft to activate only when the exact amount, frequency, start date, end date, and customer details are frozen for the consent attempt.
   </Accordion>
3. #### What is the difference between a plan and a mandate?
   <Accordion title="Answer" icon="fa-comment-dots">
   A plan is your business configuration for what to charge and when. A mandate is the customer's authorized payment instruction created after successful consent through PayU and the issuer/payment ecosystem.<br/>
   <blockquote class="callout callout_info" theme="📘">
     <h3>📘 Handy Tips</h3>
     <p>Your plan can exist before consent. The mandate exists only after successful registration.</p>
   </blockquote>
   </Accordion>
4. #### Can a customer have multiple plans?
   <Accordion title="Answer" icon="fa-comment-dots">
   Yes, your system can maintain multiple plans for a customer. Each plan should have its own merchant reference and should be mapped to the correct mandate and debit schedule.<br/>
   <blockquote class="callout callout_info" theme="📘">
     <h3>📘 Handy Tips</h3>
     <p>Avoid reusing the same merchant transaction ID or invoice number across plans.</p>
   </blockquote>
   </Accordion>
5. #### Is plan status the same as mandate status?
   <Accordion title="Answer" icon="fa-comment-dots">
   No. Plan status is usually merchant-managed, such as **Draft** or **Active**. Mandate status is returned by PayU or the payment ecosystem and indicates whether debits are allowed.
   </Accordion>
6. #### How does billing cycle behavior work?
   <Accordion title="Answer" icon="fa-comment-dots">
   `billingCycle` defines the unit, such as DAILY, WEEKLY, MONTHLY, or YEARLY. `billingInterval` defines how many units must pass between debits.<br/>
   <blockquote class="callout callout_info" theme="📘">
     <h3>📘 Example</h3>
     <p><code>billingCycle=MONTHLY</code> and <code>billingInterval=1</code> means once every month. <code>billingCycle=DAILY</code> and <code>billingInterval=3</code> means once every 3 days.</p>
   </blockquote>
   </Accordion>

### Plan Management

1. #### How should I set start date and end date?
   <Accordion title="Answer" icon="fa-comment-dots">
   Use the start date as the first date from which recurring debits may begin and the end date as the last date through which the mandate can be used.<br/>
   **Best Practice:** Do not schedule pre-debit or recurring debit attempts outside the approved start and end date range.
   </Accordion>
2. #### Can the start date be the current date?
   <Accordion title="Answer" icon="fa-comment-dots">
   It depends on payment mode and issuer rules. Even if consent completes today, subsequent recurring debits may require a pre-debit notification window before the actual charge.<br/>
   **Best Practice:** Build date validation that accounts for pre-debit lead time, especially for Cards and UPI.
   </Accordion>
3. #### Can I create duplicate plans?
   <Accordion title="Answer" icon="fa-comment-dots">
   You can duplicate a draft plan as a convenience feature, but every consent attempt should use unique transaction and invoice identifiers.
   </Accordion>

### Plan Lifecycle and Statuses

1. #### What is the difference between Draft and Active plans?
   <Accordion title="Answer" icon="fa-comment-dots">
   Draft means the plan exists only in your system and has not activated. Active means the plan is activated and ready to use.
   </Accordion>
2. #### Can I edit a plan?
   <Accordion title="Answer" icon="fa-comment-dots">
   Yes, you can edit a plan.
   </Accordion>
3. Can i delete a plan?
   <Accordion title="Answer" icon="fa-comment-dots">
   No, you cannot delete a plan. However, you can deactivate a plan. Once deactivated, a plan moves to the **Archived** state. You can dupliacte it to create a new plan.
   </Accordion>
4. Can I pause and resume a plan?
   <Accordion title="Answer" icon="fa-comment-dots">
   No, you cannot pause or resume a plan.
   </Accordion>
5. #### Can I update a plan mid-cycle?
   <Accordion title="My Accordion Title" icon="fa-info-circle">
     Lorem ipsum dolor sit amet, **consectetur adipiscing elit.** Ut enim
     ad minim veniam, quis nostrud exercitation ullamco. Excepteur sint
     occaecat cupidatat non proident!
   </Accordion>

<br />