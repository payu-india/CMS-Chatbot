---
title: Plan Management
deprecated: false
hidden: true
metadata:
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



<br />
