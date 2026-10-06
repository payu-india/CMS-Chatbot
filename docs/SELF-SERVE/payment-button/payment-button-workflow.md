---
title: How Payment Button Works
excerpt: >-
  Understand the complete end-to-end lifecycle of a PayU Payment Button — from  
  creating your account to receiving funds in your bank account.
deprecated: false
hidden: true
metadata:
  title: How Payment Buttons Works | PayU Developer Docs
  description: >-
    End-to-end lifecycle of a PayU Payment Button 

    account setup, button creation, adding to your website, customer payment,
    status tracking, and fund settlement.
  keywords:
    - how payu payment buttons works
    - payu payment button lifecycle
    - payment button flow payu
    - payu payment button workflow
    - payment button end to end payu
    - how does payment button work india
    - payu payment button steps
    - payment button process payu
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payment-button
      title: Payment Button
      type: basic
    - slug: add-payment-button
      title: Add a Payment Button
      type: basic
    - slug: manage-payment-buttons
      title: Manage Payment Buttons
      type: basic
    - slug: payment-button-errors-troubleshooting
      title: Errors and Troubleshooting
      type: basic
    - slug: payment-button-faqs
      title: FAQs (Frequently Asked Questions)
      type: basic
---
Understand the complete end-to-end flow of how PayU Payment Buttons works — from creating your account to receiving funds in your bank account.

***

## Workflow

The steps below give a detailed view of the lifecycle of a PayU Payment Button.

<Accordion title="Step 1: Create a PayU Merchant Account" icon="far fa-user">
  Sign up for a PayU merchant account and complete KYC verification. Once your account is approved, you can start creating payment buttons immediately from the Dashboard — no technical setup needed.

  <Callout icon="💡" theme="info">
    ### **Handy Tip**

    Already have an account? Skip to Step 2.

    - <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signup">Set Up Your Account</Anchor>
  </Callout>
</Accordion>

<Accordion title="Step 2: Create a Payment Button" icon="far fa-rectangle-terminal">
  In the PayU Dashboard, go to **Payment Tools → Payment Buttons** and click <Anchor target="_blank" href="https://docs.payu.in/docs/add-payment-button">**Create New Button**</Anchor>. Set the button text (Buy Now, Pay Now, Book Now, or Donate Now), item name, amount, colour, and size. Optionally add checkout fields to collect customer details — name, email, phone — or any custom fields specific to your business.
</Accordion>

<Accordion title="Step 3: Add the Button to Your Website" icon="far fa-code">
  Click **Generate Button**. PayU creates your button and gives you a short piece of code. Copy the code and paste it into an HTML or Code block on your website such as WordPress, Wix, Squarespace, and most website builders support this. The button appears on your page right away. No developer needed.
</Accordion>

<Accordion title="Step 4: Customer Visits Your Page and Pays" icon="far fa-credit-card">
  When a customer visits your page and clicks the button, PayU's payment page opens automatically. They choose their preferred payment method such as cards, UPI, net banking, wallets, EMI, and more to complete the payment. Once done, they are sent to your success page, or your failure page if the payment did not go through.<br />

  If you have webhooks configured, PayU sends a `payment.success` event to your server the moment the payment completes.

  <Callout icon="💡" theme="info">
    ### **Handy Tip**

    Webhooks are optional. Your Dashboard always reflects the current payment status without any webhook setup.

    - [Set Redirect Pages](https://docs.payu.in/docs/add-payment-button#how-do-i-add-a-payment-button)
    - <Anchor target="_blank" href="https://docs.payu.in/docs/manage-webhooks-using-dashboard">Webhooks for Payments</Anchor>
  </Callout>
</Accordion>

<Accordion title="Step 5: Track and Manage Your Payments" icon="far fa-chart-line">
  Every payment made through your button appears in the **Transactions** tab of your PayU Dashboard right away. You can filter by date, search by amount, view individual transaction details, and download payment records as CSV or Excel. All your buttons and their statuses are listed under **Payment Tools → Payment Buttons**.

  <Callout icon="💡" theme="info">
    ### **Handy Tip**

    Use the **Download** option on the Payment Buttons list to export all button records for reconciliation or your own reporting.

    - <Anchor target="_blank" href="https://docs.payu.in/docs/manage-payment-buttons">Manage Payment Buttons</Anchor>
  </Callout>
</Accordion>

<Accordion title="Step 6: Funds Are Settled to Your Account" icon="far fa-building-columns">
  After a successful payment, PayU settles the funds to your registered bank account as per the settlement schedule excluding applicable fees and taxes. You can track settlement reports from the PayU Dashboard.

  <Callout icon="💡" theme="info">
    ### **Handy Tip**

    If a customer requests a refund or raises a dispute with their bank, PayU has a process for each.

    - [Refunds](doc:introduction-refunds)
    - [Settlements](doc:split-settlments)
    - [Disputes and Chargebacks](doc:chargeback)
  </Callout>
</Accordion>
