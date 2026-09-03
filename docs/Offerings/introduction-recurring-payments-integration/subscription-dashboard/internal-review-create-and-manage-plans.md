---
title: '[INTERNAL REVIEW] Create and Manage Plans'
excerpt: Create a manage plans from the PayU dashboard.
deprecated: false
hidden: true
metadata:
  robots: index
---
You can manage plans by performing the following actions from PayU dashboard.

- [Create a plan](https://docs.payu.in/docs/internal-review-create-and-manage-plans#create-a-plan)
- [Create subscriptions for a plan](https://docs.payu.in/docs/internal-review-create-and-manage-plans#create-subscriptions-for-a-plan)
- [View plans](https://docs.payu.in/docs/internal-review-create-and-manage-plans#view-plans)
- [Duplicate plans](https://docs.payu.in/docs/internal-review-create-and-manage-plans#duplicate-a-plan)
- [Edit plans](https://docs.payu.in/docs/internal-review-create-and-manage-plans#edit-a-plan)
- [Deactivate plans](https://docs.payu.in/docs/internal-review-create-and-manage-plans#deactivate-a-plan)

***

## Create a Plan

To create a plan:

1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin">PayU dashboard,</Anchor> expand **Subscriptions and&#x20;**&#x63;lick **Plans&#x20;**&#x66;rom the left menu.


   <Image src="https://files.readme.io/d702957802d2066612647750ceb1113b810dbe1e786d0c0375b8ea4321b3720c-Screenshot_2026-05-24_at_11.20.49_AM.png" align="center" caption="_Access Plans_" border={true} />


2. Click **+ Create Plan&#x20;**&#x64;isplayed on the top-right corner of the page.

   The **Create Plan&#x20;**&#x70;op-up menu appears.

3. Provide the following details:

   | Field                                                               | Description                                                                 | Required/Optional       | Notes                                                                                                                                             |
   | ------------------------------------------------------------------- | --------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Plan ID**                                                         | A unique identifier for the plan                                            | Optional                | Maximum 32 characters. Cannot be changed after plan creation. Auto-generated if not provided.                                                     |
   | **Plan Name**                                                       | The name of the plan visible to customers                                   | Mandatory               | No character limit.                                                                                                                               |
   | **Description**                                                     | A short description of the plan                                             | Mandatory               | Maximum 100 characters.                                                                                                                           |
   | **Billing Type**                                                    | Determines whether the plan is for recurring or one-time payments           | Mandatory               | Choose **Recurring** or **One-time**                                                                                                              |
   | **Billing Cycle** _(appears only when Billing Type = Recurring)_    | The frequency at which recurring debits should happen                       | Mandatory for Recurring | Options: Day, Week, Month, Year                                                                                                                   |
   | **Billing Interval** _(appears only when Billing Type = Recurring)_ | The number of billing cycles between each debit                             | Mandatory for Recurring | Positive integer (e.g., 1 for every cycle, 3 for every 3 cycles)                                                                                  |
   | **Billing Amount**                                                  | The amount to debit from the customer's account                             | Mandatory               | Minimum ₹1. Up to 2 decimal places. **Note:** For free trial (FreeTrial=1), upfront amount is auto-populated as ₹2 for Cards/UPI or ₹0 for ENach. |
   | **Upfront Amount**                                                  | One-time registration amount paid by the customer during subscription setup | Optional                | Same format as Billing Amount. For free trials, this is auto-populated.                                                                           |

   **Billing Type Options:**

   - **Recurring:** Choose this option for recurring debits at set intervals. You must configure the Billing Cycle and Billing Interval.
     - **Billing Cycle Examples:**
       - **Day:** Recurring debit happens daily
       - **Week:** Recurring debit happens weekly
       - **Month:** Recurring debit happens monthly
       - **Year:** Recurring debit happens yearly
     - **Billing Interval:** Enter how many cycles should pass between debits (e.g., 1 for every month, 3 for every 3 months)

   - **One-time:** Choose this option to create a one-time payment link without recurring charges.


     <Image src="https://files.readme.io/f5a3311e42e877996349c8d1b3c441e064c47672b44f91791c1cc488783cce95-Screenshot_2026-05-27_at_11.18.47_AM.png" align="center" caption="_Create Plan Fields_" border={true} />


4. Click any of the following:
   - **Save as Draft:&#x20;**&#x54;o save the plan as a draft.
   - **Activate Plan:&#x20;**&#x54;o create and activate plan.

***

## Create Subscriptions for a Plan

To create a subscription for a plan:

1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin">PayU dashboard,</Anchor> expand **Subscriptions&#x20;**&#x63;lick **Plans&#x20;**&#x66;rom the left menu.

   ![](https://files.readme.io/e23c9520f99c508b3a30344721344fe2c910c4ecb17b785433fe6044a56d9796-image.png)

2. Click the required plan to create a Subscription and click **+ New Subscription.**

   ![](https://files.readme.io/150db535eaadf15ae2c3fbd3c9dc02a33e890b1371a7beeb652da9f651b74122-Screenshot_2026-05-27_at_3.12.24_PM.png)

   The subscription creation form appears with **Plan Details** and **Payment Details** sections auto-populated from the selected plan.

   **Plan Details:** Shows the plan name, billing amount, billing cycle, and upfront amount from the selected plan. You can edit these values for this specific subscription if needed.

   **Payment Details:** Configure the payment schedule and preferences:

   - **Start Date:** The date from which the subscription becomes active and recurring charges begin
   - **End Date:** The last date through which the subscription remains active
   - **Payment Methods:** Select which payment modes are available for the customer (Cards, UPI, Net Banking)

3. Enter **Customer Details** including name, email, and phone number. You can enable email/SMS notifications to send the subscription link directly to the customer.

4. _(Optional)_ Click **Additional Details** to add custom fields, shipping information, tax amounts, or other checkout customizations.

   For complete details on configuring customer information and additional fields, refer to [Create a Subscription Payment Link](doc:create-a-subscription-payment-link-using-dashboard).


   <Image src="https://files.readme.io/8bc52c6890605dbfce90a7f4974faf7c1f7bf6c4a64722faf5143bead55984a5-create-sub.gif" align="center" caption="_Subscription Fields_" border={true} />


5. Check the preview in the **Payment Request Preview** section and click **Create Link**.

***

## View Plans

To view plans:

Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin">PayU dashboard,</Anchor> expand **Subscriptions&#x20;**&#x63;lick **Plans&#x20;**&#x66;rom the left menu.


<Image src="https://files.readme.io/8274162ac9b932fd0e22ff9c71f76c8f0dc0b06daefd369b9b1cce6a0ab86107-image.png" align="center" caption="_Access Plans_" border={true} />


A list of all plans with the following information in displayed in the **All Plans&#x20;**&#x73;ection:

- **Created Date**
- **Updated Date**
- **Plan**
- **Pricing**
- **Status**
- **Active Mandates**

<Callout icon="📘" theme="info">
  ### **Action Plans**

  You can perform various actions from the **All Plans&#x20;**&#x73;ection. Click the three dots menu icon against the required plan to perform actions depending on the plan status.

  - **Active Plans:&#x20;**&#x59;ou can perform the following actions on active plans.
    - **Create Subscription**
    - **Duplicate Plan**
    - **Deactivate**
  - **Draft Plans:&#x20;**&#x59;ou can perform the following actions on draft plans.
    - **Edit Plan**
    - **Duplicate Plan**
    - **Deactivate**
  - **Archived/Deactivated Plans:&#x20;**&#x59;ou can perform the following actions on archived/deactivated plans.
    - **Duplicate Plan**
</Callout>

***

## View Plan Details

To view plan details:

1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin">PayU dashboard,</Anchor> expand **Subscriptions&#x20;**&#x63;lick **Plans&#x20;**&#x66;rom the left menu.


   <Image src="https://files.readme.io/faf9b9f8cb4054c9f853a7a9cda47dec261dc15c979b44e6445d1a8114be4e0a-image.png" align="center" caption="_Access Plans_" border={true} framed={true} />


2. Click the required plan to view its details.


   <Image src="https://files.readme.io/8a5ecd36ab4e00206b6abc46cb8b8d14e03b1bc91251b8c76f760e8e76141a9e-plan_details.png" align="center" caption="_Plan Details_" border={true} framed={true} />


   The Plan Details page displays:

   - **Plan Information:** Plan ID, name, description, billing type, billing amount, and upfront amount
   - **Pricing:** Billing cycle and interval configuration
   - **Created On:** Date when the plan was created
   - **Updated On:** Date when the plan was last modified
   - **Active Subscribers:** Number of subscriptions currently active under this plan (customers with active mandates who are being charged)
   - **Inactive Subscribers:** Number of subscriptions that were created from this plan but are no longer active (cancelled, expired, or failed mandates)

***

## Edit a Plan

To edit a plan:

1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin">PayU dashboard,</Anchor> expand **Subscriptions&#x20;**&#x63;lick **Plans&#x20;**&#x66;rom the left menu.


   <Image src="https://files.readme.io/6dd00a0649d7a065da4c71dfbb07f397f40b32119b229c64f4d777816dcc426b-image.png" align="center" caption="_Access Plans_" border={true} framed={true} />


2. Click the three dot menu against a required plan and click **Edit Plan.&#x20;**&#x41;lternatively, you can edit a plan from the **Plan Details&#x20;**&#x73;ection.


   <Image src="https://files.readme.io/7b2f07679fc29e9d8c53d297921cc2b66fe3ab1cfba9496bfe6734b7a4ed019a-click_edit_plan.png" align="center" caption="_Edit a Plan_" border={true} framed={true} />


   The **Edit Plan** pop-up menu appears.

3. Edit the required details and click **Activate Plan**.


   <Image src="https://files.readme.io/f5995efb86c7ef669db14120eb5c0e2778a247d297dc217add02ab77a4cac589-click_activate_plan_edit.png" align="center" caption="_Edit Plan Fields_" border={true} framed={true} />


   <Callout icon="⚠️" theme="warning">
     ### **Edit Restrictions**

     The following fields **cannot be edited** after plan creation:

     - **Plan ID:** The unique identifier cannot be changed once the plan is created
     - **Billing Cycle and Interval** _(for plans with active subscriptions)_: Cannot be modified if the plan has active subscribers

     All other fields including Plan Name, Description, Billing Amount, and Upfront Amount can be edited. Note that changes may only apply to new subscriptions created after the edit.
   </Callout>

***

## Duplicate a Plan

1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin">PayU dashboard,</Anchor> expand **Subscriptions&#x20;**&#x63;lick **Plans&#x20;**&#x66;rom the left menu.


   <Image src="https://files.readme.io/09c0706eca55ec4dcac330b21a131f18ee15efc743f2f5cdc703dd84e2ba6f9e-image.png" align="center" caption="_Access Plans_" border={true} framed={true} />


2. Click the three dot menu against a required plan and click **Duplicate Plan.&#x20;**&#x41;lternatively, you can duplicate a plan from the **Plan Details&#x20;**&#x73;ection.


   <Image src="https://files.readme.io/749c0c6d0b0674cb8642049ae13a164151d9641ca519103cdb592e06fd0dbcb2-duplicate_plan.png" align="center" caption="_Duplicate a Plan_" border={true} framed={true} />


The **Duplicate Plan&#x20;**&#x70;op-up menu appears.

3. Enter the **Plan ID&#x20;**&#x61;nd change other details as required in the **Duplicate Plan&#x20;**&#x70;op-up menu.
4. Click **Activate Plan**.


   <Image src="https://files.readme.io/224de78f92d50b7038dfb6273f2300d0346612830be5f81fb877c8b6274a26f5-duplicate_plan_activate.png" align="center" caption="_Duplicate Plan Fields_" border={true} framed={true} />


***

## Deactivate a Plan

To deactivate a plan:

1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin">PayU dashboard,</Anchor> expand **Subscriptions&#x20;**&#x63;lick **Plans&#x20;**&#x66;rom the left menu.


   <Image src="https://files.readme.io/b83c7ac1688e70c104dcf30e79a82c4896613466da5c13f2e6decd7a90406635-image.png" align="center" caption="_Access Plan_" border={true} framed={true} />


2. Click the three dot menu against a required plan and click **Deactivate.&#x20;**&#x41;lternatively, you can deactivate a plan from the **Plan Details&#x20;**&#x73;ection.


   <Image src="https://files.readme.io/ae2cc70b54a1153da183dd5b501498ffcf18e0cb195dd08fb37653bd515a3acf-deactivate_plan.png" align="center" caption="_Access Plans_" border={true} framed={true} />


3. Click **Deactivate Plan&#x20;**&#x69;n the **Deactivate Plan&#x20;**&#x70;op-up menu.

The plan moves to the **Archived** state. You can reuse by duplicating it.

<br />

<br />
