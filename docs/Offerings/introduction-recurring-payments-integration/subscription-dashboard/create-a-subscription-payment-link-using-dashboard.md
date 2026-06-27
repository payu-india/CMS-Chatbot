---
title: Create a Subscription Payment Link
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Create a Subscription Payment Link
  description: >-
    Learn how to create a subscription payment link using the PayU Dashboard.
    Follow our step-by-step guide to set up recurring payments with ease
  keywords:
    - subscription payment link
    - create subscription payment link
    - Dashboard recurring payments setup
    - subscription billing PayU payment link creation
    - ' PayU subscription instructions subscription payment setup'
    - ' recurring billing'
    - ' how to create payment link'
    - recurring payment link using Dashboard
  robots: index
next:
  description: ''
---
In PayU Dashboard, you can create payment links with Standing Instructions. You can create payment links for all payment modes that includes: 

- Cards 
- UPI  
- Enach 

## Step 1: Navigate to Subscriptions Bulk Upload Page 

To create payment links with Standing Instruction on PayU Dashboard: 

1. Log on to Pay Dashboard. 
2. Navigate to **Subscriptions**. 
3. Click the **Create Subscription Link** button at the top-right corner. 


<Image src="https://files.readme.io/545038dbe2e70d43d372c535a0119737e3906a391ac9997f8e4849df0e4bf0fb-dashboard-subscriptions-overview.png" align="center" border={true} />


The _Create Subscriptions_ pop-up page is displayed.  


<Image src="https://files.readme.io/b636dc66b0417d5efe8ba893acee8df827b497ca8529b25896101043db02ff94-dashboard-create-subscriptions-link.png" align="center" border={true} />


## Step 2: Enter the Plan Details 

1. Enter the purpose of the subscription in the **Purpose** field.  
2. Choose the billing type in the **Billing type** field:  
3. **Fixed Amount**: The fixed amount to be debited in the specified interval. You must enter at least Rs.1 to proceed.  

> **Note:** Free trial option is not available for UPI payments. If you do choose a free trial, the UPI upfront amount will be automatically set to Rs. 1, and you must enter an amount equal to or greater than Re 1 to move forward. 

4. **Maximum Amount:** The maximum amount that you can debit in the specified interval.  

## Step 3: Enter the Subscription Details 

1. Expand the **Subscription details** pane. 


<Image src="https://files.readme.io/d96b936829b1fbe8374f93454a56950923b3f193c6490d9acaf7d8229229e552-dashboard-create-subscriptions-link-step2.png" align="center" border={true} />


2. Perform any of the following steps to select the subscription date: 

- Select the start date and end date of the subscription in the **Start & End Date** field.  
- Select the **No expiration** check box. 

> **Note**: If you select the **No expiration** check box, the end date is automatically configured as 30 years from the start date. 

3. Select the billing cycle from the **Billing Cycle** drop-down list. 
4. Select the billing interval based on the cycle chosen from the **Billing Interval** drop-down list. 

<br />

<Callout icon="📘" theme="info">
  ### Notes:

  - For eNACH, mandate start date needs to be at least (T+1). For example, in case the payment link is created today then the start date can be anything starting tomorrow.
  - The seamless flow is only possible if eNACH is selected as the payment mode and all necessary beneficiary account details are added during the payment link creation process. It will not function if all Payment Modes or multiple payment modes are selected.
</Callout>

## Step 4: Entering the Customer Details 

1. Expand the **Customer details** pane.  


<Image src="https://files.readme.io/c1793fdccafad7071dec9571fc10d91f79bac92777d290009408865b2335277f-dashboard-create-subscriptions-link-step3.png" align="center" border={true} />


2. Select the applicable payment methods from the **Select Payment Method** drop-down list:

- E-Nach
- Cards
- UPI

3. Enter the following details: 

- **Customer Name**: Enter the customer name. 
- **Email**: Enter the customer email address and click the **Notify via Email** toggle to send notifications. 
- **Phone Number**: Enter the customer mobile number and click the **Notify via Phone** toggle to send notifications. 
- **Allow Reminder**: Select this check box to send reminders to the customer 

4. Enter the following details if you had selected ENACH as the payment method in Step 2 of [Step 4: Entering the Customer Details](#step-4-entering-the-customer-details)  


<Image src="https://files.readme.io/353f05dc0c6fb1cc0899f2e8604d624455d32b2c65d8ce376f165a00834d4fab-Screenshot_2024-09-16_at_10.28.47_AM.png" align="center" border={true} />


- Bank Name 
- Bank Account Number 
- IFSC 
- Account Type 

## Step 5: Enter the Additional Details 

1. Expand the **Additonal details** pane. 


<Image src="https://files.readme.io/a573ee878a78eb38b0e7f3b7a7cfb0c51d49ea82b4efd632f1d49b7dc12b85ba-dashboard-create-subscriptions-link-step4-addl-info.png" align="center" border={true} />


2. Click the **Show Additional Information** toggle button and the enter the address details.
3. Click the **Show Customer Information** toggle button and the select the following check boxes which must be shown: 

- Customer Email 
- Customer Phone 
- Customer Name 
- Customer Address 

4. Click the **Create Link** button at the top-right corner after you complete the above steps.

<br />
