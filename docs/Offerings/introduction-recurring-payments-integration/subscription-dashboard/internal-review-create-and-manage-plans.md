---
title: '[INTERNAL REVIEW] Create and Manage Plans'
excerpt: Create a manage plans from the PayU dashboard.
deprecated: false
hidden: true
metadata:
  robots: index
---
You can manage plans by performing the following actions from PayU dashboard.

- Create a plan
- Create subscriptions for a plan
- View plans
- Duplicate plans
- Edit plans
- Deactivate plans

## Create a Plan

To create a plan:

1. Log in to the <Anchor target="_blank" href="https://payu.in/">dashboard,</Anchor> expand **Subscriptions&#x20;**&#x63;lick **Plans&#x20;**&#x66;rom the left menu.


   <Image src="https://files.readme.io/d702957802d2066612647750ceb1113b810dbe1e786d0c0375b8ea4321b3720c-Screenshot_2026-05-24_at_11.20.49_AM.png" align="center" caption="_Access Plans_" border={true} />


2. Click **+ Create Plan&#x20;**&#x64;isplayed on the top-right corner of the page.

   The **Create Plan&#x20;**&#x70;op-up menu appears.

3. Provide the following details:
   - **Plan ID:&#x20;**&#x41; unique ID of a plan.
   - **Plan Name:&#x20;**&#x54;he name of the plan visible to customers.
   - **Description:&#x20;**&#x41; short description of the plan.
   - **Billing Type:&#x20;**&#x44;etermines the billing type. Below are the available options.
     - **Recurring:&#x20;**&#x43;hoose this optio&#x6E;**&#x20;**&#x69;f you wan&#x74;**&#x20;**&#x72;ecurring debits at set intervals.
       - **Billing Cycle:&#x20;**&#x54;he intervals at which the recurring debits should happen. You will get this option only if you choose the **Billing Type** as **Recurring**. Below are the available options:
         - Enter the interval at which the recurring debits should happen in the **every&#x20;**&#x74;ext box under the **Billing Cycle&#x20;**&#x73;ection.
         - Select the frequency you want the recurring debit to happen from the drop-down that has following options under the **Billing Cycle&#x20;**&#x73;ection.
           - **Day:&#x20;**&#x52;ecurring debit happens daily.
           - **Week:&#x20;**&#x52;ecurring debit happen weekly.
           - **Month:&#x20;**&#x52;ecurring debit happens monthly.
           - **Year:&#x20;**&#x52;ecurring debit happens yearly.
     - **One-time:&#x20;**&#x43;hoose this option if you want to make a one-time payment using a link.
   - **Billing Amount:&#x20;**&#x54;he recurring amount you want to debit from the customers account.
   - **Upfront Amount:&#x20;**&#x59;ou can add any additional amount as upfront amount. This is one-time a one-time registration amount paid by the customer.


     <Image src="https://files.readme.io/f5a3311e42e877996349c8d1b3c441e064c47672b44f91791c1cc488783cce95-Screenshot_2026-05-27_at_11.18.47_AM.png" align="center" caption="_Create Plan Fields_" border={true} />


4. Click any of the following:
   - **Save as Draft:&#x20;**&#x54;o save the plan as a draft.
   - **Activate Plan:&#x20;**&#x54;o create and activate plan.

## Create Subscriptions for a Plan

To create a subscription for a plan:

1. Log in to the <Anchor target="_blank" href="https://payu.in/">dashboard,</Anchor> expand **Subscriptions&#x20;**&#x63;lick **Plans&#x20;**&#x66;rom the left menu.

   ![](https://files.readme.io/e23c9520f99c508b3a30344721344fe2c910c4ecb17b785433fe6044a56d9796-image.png)

2. Click the required plan to create a Subscription and click **+ New Subscription.**

   ![](https://files.readme.io/150db535eaadf15ae2c3fbd3c9dc02a33e890b1371a7beeb652da9f651b74122-Screenshot_2026-05-27_at_3.12.24_PM.png)

   Plan and **Payment details**  are auto-populated. You can edit the plan details as per your requirement.

3. Enter the **Customer details**. Below are the available options:

   - **Enable Third Party Validation:&#x20;**&#x45;nable this to skip checkout and take your customers directly to the bank page with **Enach** pre-selected.
   - **Customer Name**
   - **Email:&#x20;**&#x54;he customer email address. Enable **Notify via Email&#x20;**&#x72;adio button to send the subscription link via email.
   - **Phone Number:&#x20;**&#x54;he customer phone number. Enable **Notify via Phone&#x20;**&#x72;adio button to send the subscription link to a phone number.
   - **Allow Reminder:&#x20;**&#x53;elect this checkbox to allow reminders.

4. Click **Additional details&#x20;**&#x74;o expand and add additional information to the checkout. Below are the available options:

   - **Show Additional Information:&#x20;**&#x41;dd the below options to collect the additional information.
     - **Shipping Charge**
     - **Customer Address**
     - **Add More Details:&#x20;**&#x43;lick this to add or remove the following custom fields.
       - **Payment Due Date**
       - **Add Tax Amount**
       - **Add Shipping Charges**
       - **Address Details**
       - **UDF&#x20;**(User Defined Fields)
   - **Show Custom Information:&#x20;**&#x55;se this section to display the following information in the checkout.
     - **Customer Email**
     - **Customer Phone**
     - **Customer Name**
     - **Customer Address**
   - **Add Fields:&#x20;**&#x55;se this option to add any other custom field.


   <Image src="https://files.readme.io/8bc52c6890605dbfce90a7f4974faf7c1f7bf6c4a64722faf5143bead55984a5-create-sub.gif" align="center" caption="_Subscription Fields_" border={true} />


5. Check the preview in the **Payment Request Preview&#x20;**&#x64;isplayed section and click **Create Link**.

## View Plans

To view plans:

Log in to the <Anchor target="_blank" href="https://payu.in/">dashboard,</Anchor> expand **Subscriptions&#x20;**&#x63;lick **Plans&#x20;**&#x66;rom the left menu.


<Image src="https://files.readme.io/8274162ac9b932fd0e22ff9c71f76c8f0dc0b06daefd369b9b1cce6a0ab86107-image.png" align="center" caption="_Access Plans_" border={true} />


A list of all plans with the following information in displayed in the **All Plans&#x20;**&#x73;ection:

- **Created Date**
- **Updated Date**
- **Plan**
- **Pricing**
- **Status**
- **Active Mandates**

> 📘 **Action Plans**
>
> You can perform various actions from the **All Plans&#x20;**&#x73;ection. Click the three dots menu icon against the required plan to perform actions depending on the plan status.
>
> - **Active Plans:&#x20;**&#x59;ou can perform the following actions on active plans.
>   - **Create Subscription**
>   - **Duplicate Plan**
>   - **Deactivate**
> - **Draft Plans:&#x20;**&#x59;ou can perform the following actions on draft plans.
>   - **Edit Plan**
>   - **Duplicate Plan**
>   - **Deactivate**
> - **Archived/Deactivated Plans:&#x20;**&#x59;ou can perform the following actions on archived/deactivated plans.
>   - **Duplicate Plan**

## View Plan Details

To view plan details:

1. Log in to the <Anchor target="_blank" href="https://payu.in/">dashboard,</Anchor> expand **Subscriptions&#x20;**&#x63;lick **Plans&#x20;**&#x66;rom the left menu.

   <Image src="https://files.readme.io/faf9b9f8cb4054c9f853a7a9cda47dec261dc15c979b44e6445d1a8114be4e0a-image.png" align="center" caption="_Access Plans_" border={true} framed={true} />

2. Click the required plan to view its details.

   <Image src="https://files.readme.io/8a5ecd36ab4e00206b6abc46cb8b8d14e03b1bc91251b8c76f760e8e76141a9e-plan_details.png" align="center" caption="_Plan Details_" border={true} framed={true} />


## Edit a Plan

To edit a plan:

1. Log in to the <Anchor target="_blank" href="https://payu.in/">dashboard,</Anchor> expand **Subscriptions&#x20;**&#x63;lick **Plans&#x20;**&#x66;rom the left menu.

   <Image src="https://files.readme.io/6dd00a0649d7a065da4c71dfbb07f397f40b32119b229c64f4d777816dcc426b-image.png" align="center" caption="_Access Plans_" border={true} framed={true} />

2. Click the three dot menu against a required plan and click **Edit Plan.&#x20;**&#x41;lternatively, you can edit a plan from the **Plan Details&#x20;**&#x73;ection.

   <Image src="https://files.readme.io/7b2f07679fc29e9d8c53d297921cc2b66fe3ab1cfba9496bfe6734b7a4ed019a-click_edit_plan.png" align="center" caption="_Edit a Plan_" border={true} framed={true} />


The **Edit Plan&#x20;**&#x70;op-up menu appears.

3. Edit the required details and click **Activate Plan**.

   <Image src="https://files.readme.io/f5995efb86c7ef669db14120eb5c0e2778a247d297dc217add02ab77a4cac589-click_activate_plan_edit.png" align="center" caption="_Edit Plan Fields_" border={true} framed={true} />


## Duplicate a Plan

1. Log in to the <Anchor target="_blank" href="https://payu.in/">dashboard,</Anchor> expand **Subscriptions&#x20;**&#x63;lick **Plans&#x20;**&#x66;rom the left menu.

   <Image src="https://files.readme.io/09c0706eca55ec4dcac330b21a131f18ee15efc743f2f5cdc703dd84e2ba6f9e-image.png" align="center" caption="_Access Plans_" border={true} framed={true} />

2. Click the three dot menu against a required plan and click **Duplicate Plan.&#x20;**&#x41;lternatively, you can duplicate a plan from the **Plan Details&#x20;**&#x73;ection.

   <Image src="https://files.readme.io/749c0c6d0b0674cb8642049ae13a164151d9641ca519103cdb592e06fd0dbcb2-duplicate_plan.png" align="center" caption="_Duplicate a Plan_" border={true} framed={true} />


The **Duplicate Plan&#x20;**&#x70;op-up menu appears.

3. Enter the **Plan ID&#x20;**&#x61;nd change other details as required in the **Duplicate Plan&#x20;**&#x70;op-up menu.
4. Click **Activate Plan**.

   <Image src="https://files.readme.io/224de78f92d50b7038dfb6273f2300d0346612830be5f81fb877c8b6274a26f5-duplicate_plan_activate.png" align="center" caption="_Duplicate Plan Fields_" border={true} framed={true} />


<br />
