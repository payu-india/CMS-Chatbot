---
title: How Payment Links Works
excerpt: >-
  Understand the complete end-to-end lifecycle of a PayU Payment Link — from
  creating an account to receiving funds in your bank account.
deprecated: false
hidden: true
metadata:
  title: How Payment Links Works | PayU Developer Docs
  description: >-
    End-to-end lifecycle of a PayU Payment Link — account setup, link creation,
    sending to customers, payment, status tracking, and fund settlement.
  keywords:
    - how payu payment links works
    - payu payment link lifecycle
    - payment link flow payu
    - payu payment link workflow
    - payment link end to end payu
    - how does payment link work india
    - payu payment link steps
    - payment link process payu
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payment-links
      title: Payment Links
      type: basic
    - slug: create-a-payment-link
      title: Create a Payment Link
      type: basic
    - slug: manage-payment-links
      title: Manage Payment Links
      type: basic
    - slug: payment-links-errors-and-troubleshooting
      title: Errors and Troubleshooting
      type: basic
    - slug: payment-links-faqs
      title: FAQs (Frequently Asked Questions)
      type: basic
---
Understand the complete end-to-end flow of how PayU Payment Links works. Starting from creating your account to receiving funds in your bank account.

***

## Workflow

The steps below give a detailed view of the lifecycle of a PayU Payment Link.

<Accordion title="Step 1: Create a PayU Merchant Account" icon="far fa-user">
  <Anchor target="_blank" href="https://docs.payu.in/docs/set-up-your-account">Sign up</Anchor> for a PayU merchant account and complete KYC verification. Once your account is approved, you can start creating payment links immediately from the Dashboard.

  <Callout icon="💡" theme="info">
    ### **Already Have an Account?**

    &#x20;You can skip to the Step 2
  </Callout>
</Accordion>

<Accordion title="Step 2: Create a Payment Link" icon="far fa-link">
  <Anchor target="_blank" href="https://docs.payu.in/docs/create-a-payment-link">Create a payment</Anchor> link by entering the amount, purpose of the payment and other details. You can optionally set an expiry date, enable partial payments, collect customer details at checkout, and add custom fields for your records.

  <Callout icon="💡" theme="info">
    ### **Automate:**

    You can automate creation from your own system using <Anchor target="_blank" href="https://docs.payu.in/reference/create-payment-links">Payment Links APIs</Anchor>.
  </Callout>
</Accordion>

<Accordion title="Step 3: Send the Link to Your Customer" icon="far fa-paper-plane">
  Share the payment link with your customer over SMS, Email, or WhatsApp. If you enter the customer's phone number or email when creating the link and toggle notifications on, PayU sends the link automatically the moment you click **Create Payment Link**.

  <Callout icon="💡" theme="info">
    ### **Note:**

    You can <Anchor target="_blank" href="https://docs.payu.in/docs/manage-payment-links#what-can-i-do-with-a-payment-link-after-it-is-created">resend or share</Anchor> the link again at any time from the Dashboard as long as the link is Active.
  </Callout>
</Accordion>

<Accordion title="Step 4: Customer Opens the Link and Pays" icon="far fa-credit-card">
  Your customer clicks the link and is taken to a PayU-hosted checkout page. They choose their preferred payment method such as cards, UPI, net banking, wallets, and more to complete the payment. If partial payment is enabled, they can choose how much to pay.

  The payment link is marked as **Expired** once the payment is fully made. If you have webhooks configured, PayU sends a `payment.success` event to your server.

  <Callout icon="💡" theme="info">
    ### **Webhooks:**

    Webhooks are optional — your Dashboard always reflects the current payment status without any webhook setup.
  </Callout>
</Accordion>

<Accordion title="Step 5: Track and Manage Your Links" icon="far fa-chart-line">
  Track all payment links and their statuses from the Payment Links Dashboard. You can filter by status or date, view transaction history per link, download reports in CSV or Excel format, and duplicate or deactivate links as needed.

  <Callout icon="💡" theme="info">
    ### **Note:**

    To retrieve link data programmatically — for reconciliation or reporting — use the Fetch API.

    - [Manage Payment Links — Dashboard](doc:manage-payment-links)
    - [Fetch Payment Links API](doc:api-fetch)
  </Callout>
</Accordion>

<Accordion title="Step 6: Funds Are Settled to Your Account" icon="far fa-building-columns">
  After a successful payment, PayU settles the funds to your registered bank account as per the settlement schedule — minus applicable fees and taxes. You can track settlement reports from the PayU Dashboard.

  <Callout icon="💡" theme="info">
    ### **Note:**

    If a customer requests a refund or raises a dispute with their bank, PayU has a process for each.

    - [Refunds](doc:introduction-refunds)
    - [Settlements](doc:split-settlments)
    - [Disputes and Chargebacks](doc:chargeback)
  </Callout>
</Accordion>
