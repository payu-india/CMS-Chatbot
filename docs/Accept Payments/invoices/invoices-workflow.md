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
  Sign up for a PayU merchant account and complete KYC verification. Once your account is approved, you can start creating invoices immediately from the Dashboard — no technical setup needed.

  <Callout icon="💡" theme="info">
    **Handy Tip**

    Already have an account? Skip to Step 2.

    - [Set Up Your Account](doc:set-up-your-account)
  </Callout>
</Accordion>

<Accordion title="Step 2: Add Items to Your Catalog" icon="far fa-box-open">
  Before creating your first invoice, add the products or services you bill for to the **Items** catalog. You only need to do this once — items are reusable across all future invoices. For each item, set the name, rate, description, and any applicable tax details: GST rate, inter-state or intra-state tax, cess, and HSN/SAC code.

  <Callout icon="💡" theme="info">
    **Handy Tip**

    You can also create a new item on the fly while creating an invoice — no need to set up the catalog separately in advance.

    - [Manage Invoice Items](doc:manage-invoice-items)
  </Callout>
</Accordion>

<Accordion title="Step 3: Create an Invoice" icon="far fa-file-invoice">
  Go to **Payment Tools → Invoices** and click **Create New Invoice**. Enter the invoice number, due date, invoice title, and select the customer it is billed to. Add your line items from the catalog, then configure settings: enable GST to calculate tax automatically, or enable partial payments to let the customer pay in installments.

  <Callout icon="💡" theme="info">
    **Handy Tip**

    You can save the invoice as a draft and send it later, or send it right away.

    - [Create an Invoice — Dashboard walkthrough](doc:create-an-invoice)
  </Callout>
</Accordion>

<Accordion title="Step 4: Send the Invoice to Your Customer" icon="far fa-paper-plane">
  Click **Send Invoice**. PayU sends the invoice to your customer by email or SMS. The invoice shows the invoice number, due date, itemized breakdown with GST, and a pay-now button linked to PayU's secure checkout page.

  <Callout icon="💡" theme="info">
    **Handy Tip**

    You can resend an invoice at any time from the Dashboard as long as it has not been paid or cancelled.

    - [Manage Invoices](doc:manage-invoices)
  </Callout>
</Accordion>

<Accordion title="Step 5: Customer Opens the Invoice and Pays" icon="far fa-credit-card">
  Your customer clicks the pay button in the invoice email or SMS and is taken to PayU's secure checkout page. They choose their preferred payment method — cards, UPI, net banking, wallets, and more — and complete the payment. If partial payments are enabled, they can choose how much to pay now.

  The invoice status updates to **Paid** once the payment is confirmed. If you have webhooks configured, PayU sends a `payment.success` event to your server.

  <Callout icon="💡" theme="info">
    **Handy Tip**

    Webhooks are optional — your Dashboard always reflects the latest invoice and payment status without any webhook setup.

    - [Webhooks for Payments](doc:webhooks)
  </Callout>
</Accordion>

<Accordion title="Step 6: Funds Are Settled to Your Account" icon="far fa-building-columns">
  After a successful payment, PayU settles the funds to your registered bank account as per the settlement schedule — minus applicable fees and taxes. You can track settlement reports from the PayU Dashboard.

  <Callout icon="💡" theme="info">
    **Handy Tip**

    If a customer requests a refund or raises a dispute with their bank, PayU has a process for each.

    - [Refunds](doc:introduction-refunds)
    - [Settlements](doc:split-settlments)
    - [Disputes and Chargebacks](doc:chargeback)
  </Callout>
</Accordion>

***

## Related Information

- [Invoices Overview](doc:invoice-overview)
- [Create an Invoice](doc:create-an-invoice)
- [Manage Invoices](doc:manage-invoices)
- [Manage Invoice Items](doc:manage-invoice-items)
- [Invoice Troubleshooting](doc:invoice-troubleshooting)
- [Invoice FAQs](doc:invoice-faqs)
