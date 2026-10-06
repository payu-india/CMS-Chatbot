---
title: How Invoices Works
excerpt: >-
  Understand the complete end-to-end lifecycle of a PayU Invoice — from creating
  your account to receiving funds in your bank account.
deprecated: false
hidden: true
metadata:
  title: How Invoices Works | PayU Developer Docs
  description: >-
    End-to-end lifecycle of a PayU Invoice — account setup, item catalog,
    invoice creation, sending to customer, payment, and fund settlement.
  keywords:
    - how payu invoices works
    - payu invoice lifecycle
    - invoice flow payu
    - payu invoice workflow
    - invoice end to end payu
    - how does payu invoice work
    - payu invoice steps
    - payu gst invoice process
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: invoices
      title: Invoices
      type: basic
    - slug: create-an-invoice-1
      title: Create an Invoice
      type: basic
    - slug: manage-invoices
      title: Manage Invoices
      type: basic
    - slug: manage-invoices-items
      title: Manage Invoice Items
      type: basic
    - slug: manage-invoice-customers
      title: Manage Customers
      type: basic
    - slug: invoices-errors-troubleshooting
      title: Errors and Troubleshooting
      type: basic
---
Understand the complete end-to-end flow of how PayU Invoices works — from creating your account to receiving funds in your bank account.

***

## Workflow

The steps below give a detailed view of the lifecycle of a PayU Invoice.

<Accordion title="Step 1: Create a PayU Merchant Account" icon="far fa-user">
  <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signup">Sign up</Anchor> for a PayU merchant account and complete KYC verification. Once your account is approved, you can start <Anchor target="_blank" href="https://docs.payu.in/docs/create-an-invoice-1">creating invoices</Anchor> immediately from the Dashboard.

  <Callout icon="💡" theme="info">
    ### **Tips:**

    Already have an account? Skip to Step 2.

    - <Anchor target="_blank" href="https://docs.payu.in/docs/set-up-your-account">Set Up Your Account</Anchor>
  </Callout>
</Accordion>

<Accordion title="Step 2: Create an Invoice" icon="far fa-file-invoice">
  Go to **Payment Tools → Invoices** and click **Create New Invoice**. Enter the invoice number, due date, invoice title, and select the customer it is billed to. Add your line items, then configure settings: enable GST to calculate tax automatically, or enable partial payments to let the customer pay in installments.

  <Callout icon="💡" theme="info">
    ### **Tips:**

    You can save the invoice as a draft and send it later, or send it right away.

    - <Anchor target="_blank" href="https://docs.payu.in/docs/create-an-invoice-1">Create an Invoice</Anchor>
  </Callout>
</Accordion>

<Accordion title="Step 3: Send the Invoice to Your Customer" icon="far fa-paper-plane">
  Click **Send Invoice**. PayU sends the invoice to your customer by email or SMS. The invoice shows the invoice number, due date, itemized breakdown with GST, and a pay-now button linked to PayU's secure checkout page.

  <Callout icon="💡" theme="info">
    ### **Tips:**

    You can resend an invoice at any time from the Dashboard as long as it has not been paid or deactivated.

    - <Anchor target="_blank" href="https://docs.payu.in/docs/manage-invoices#resend-an-invoice">Resend an Invoice</Anchor>
  </Callout>
</Accordion>

<Accordion title="Step 4: Customer Opens the Invoice and Pays" icon="far fa-credit-card">
  Your customer clicks the pay button in the invoice email or SMS and is taken to PayU's secure checkout page. They choose their preferred payment method such as cards, UPI, net banking, wallets, and more and complete the payment. If partial payments are enabled, they can choose how much to pay now.

  The invoice status updates to **Paid** once the payment is confirmed. If you have webhooks configured, PayU sends a `payment.success` event to your server.

  <Callout icon="💡" theme="info">
    ### **Tips:**

    Webhooks are optional. Your Dashboard always reflects the latest invoice and payment status without any webhook setup.

    - <Anchor target="_blank" href="https://docs.payu.in/docs/manage-webhooks-using-dashboard">Webhooks for Payments</Anchor>
  </Callout>
</Accordion>

<Accordion title="Step 5: Funds Are Settled to Your Account" icon="far fa-building-columns">
  After a successful payment, PayU settles the funds to your registered bank account as per the settlement schedule excluding applicable fees and taxes. You can track settlement reports from the PayU Dashboard.

  <Callout icon="💡" theme="info">
    ### **Tips:**

    If a customer requests a refund or raises a dispute with their bank, PayU has a process for each.

    - [Refunds](doc:introduction-refunds)
    - [Settlements](doc:split-settlments)
    - [Disputes and Chargebacks](doc:chargeback)
  </Callout>
</Accordion>
