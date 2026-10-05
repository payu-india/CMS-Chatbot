---
title: Manage Invoices
excerpt: >-
  View, filter, resend, cancel, and download your PayU Invoices from the
  Dashboard.
deprecated: false
hidden: true
metadata:
  title: Manage PayU Invoices — Dashboard Guide | Developer Docs
  description: >-
    View invoice status, resend invoices, cancel invoices, filter by date or
    status, and download records — all from the PayU Dashboard.
  keywords:
    - manage invoices payu
    - view invoice status payu
    - resend invoice payu dashboard
    - cancel invoice payu
    - filter invoices payu
    - download invoice records payu
    - payu invoice paid overdue
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
---
<Banner
  isInline={true}
  message="Integration effort: No code or website developer required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

You can view and manage all your invoices from the PayU Dashboard after they are created and sent.

***

## How Do I Access My Invoices?

To open your invoices: log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Invoices** under **Payment Tools**.


<Image src="https://files.readme.io/38614931076cc05791bfba99a8241cc8ee9bb5bfe7d3a5ebc49c06704cf1d674-Screenshot_2025-06-02_at_7.31.48_PM.png" align="center" caption="Invoices list in the PayU Dashboard" border={true} />


The list shows all your invoices for the past 7 days by default, with the following columns:

| Column             | What it shows                                            |
| ------------------ | -------------------------------------------------------- |
| **Invoice Number** | Your unique reference for the invoice                    |
| **Title**          | The invoice title you entered when creating it           |
| **Customer**       | Who the invoice was billed to                            |
| **Amount**         | The total amount on the invoice                          |
| **Due Date**       | When payment is due                                      |
| **Status**         | Current state — Draft, Sent, Paid, Overdue, or Cancelled |

***

<Callout icon="🚧" theme="warning">
  **Invoices cannot be edited after they are sent.** If an invoice has wrong details — item, amount, or due date — cancel it and create a new one with the correct information.
</Callout>

## What Can I Do With an Invoice?

<Accordion title="View Invoice Details" icon="far fa-rectangle-list">
  To see the full details of an invoice:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Invoices** under **Payment Tools**.


  <Image src="https://files.readme.io/38614931076cc05791bfba99a8241cc8ee9bb5bfe7d3a5ebc49c06704cf1d674-Screenshot_2025-06-02_at_7.31.48_PM.png" align="center" caption="Invoices list" border={true} />


  2. Click the invoice you want to view.

  The invoice detail page shows:

  - Invoice number, title, issue date, and due date
  - Customer name and contact details
  - Itemized breakdown with quantities, rates, and GST
  - Total amount, GST breakdown, and amount paid (if partial payments were made)
  - Current status and payment history
</Accordion>

<Accordion title="Resend an Invoice" icon="far fa-paper-plane">
  If your customer did not receive the invoice or needs it again:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Invoices** under **Payment Tools**.
  2. Find the invoice you want to resend and click it to open the detail page.
  3. Click **Resend** to send the invoice again to the customer's email or mobile number.

  <Callout icon="📘" theme="info">
    You can only resend invoices that are in **Sent** or **Overdue** status. Paid and Cancelled invoices cannot be resent.
  </Callout>
</Accordion>

<Accordion title="Cancel an Invoice" icon="far fa-ban">
  Cancelling an invoice marks it as void — the customer can no longer pay it.

  To cancel an invoice:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Invoices** under **Payment Tools**.
  2. Find the invoice you want to cancel and click it to open the detail page.
  3. Click **Cancel Invoice** and confirm.

  The invoice status changes to **Cancelled**.

  <Callout icon="🚧" theme="warning">
    ### **Watch Out!**

    Once an invoice is cancelled, it cannot be restored. If you need to bill the same customer again, create a new invoice.
  </Callout>
</Accordion>

***

## How Do I Search for an Invoice?

<Accordion title="Search by Invoice Number or Title" icon="far fa-magnifying-glass">
  Use the **Search** field at the top of the Invoices list to find a specific invoice by its number or title. Type any part of the invoice number or title and the list filters in real time.
</Accordion>

<Accordion title="Filter by Status" icon="far fa-filter">
  To filter invoices by their payment status:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Invoices** under **Payment Tools**.


  <Image src="https://files.readme.io/f5a14c138742dab206b151381602bffe494ea9e60099fe919cb5a21b9fa6c664-Screenshot_2025-06-02_at_7.33.50_PM.png" align="center" caption="Filter invoices by status" border={true} />


  2. Click the **Filter** drop-down and select one or more statuses:

  | Status        | What it means                          |
  | ------------- | -------------------------------------- |
  | **Draft**     | Saved but not sent to the customer yet |
  | **Sent**      | Sent to the customer, awaiting payment |
  | **Paid**      | Payment received in full               |
  | **Overdue**   | Past the due date with no payment      |
  | **Cancelled** | Manually cancelled — no longer payable |

  3. Click **Apply** to filter the list.
  4. Click **Reset** to clear the filter and see all invoices.
</Accordion>

<Accordion title="Filter by Date" icon="far fa-calendar">
  To filter invoices by when they were created:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Invoices** under **Payment Tools**.


  <Image src="https://files.readme.io/2663edeacdcb8096f1001d53edbfe843bf0a71900b19be818c5bc74ad23918da-Screenshot_2025-06-02_at_7.32.45_PM.png" align="center" caption="Date range calendar on the Invoices list" border={true} />


  2. Click the **Calendar** icon at the top of the list and select a time period:
     - Today
     - Yesterday
     - Past 7 days
     - Past 30 days
     - Custom Range

  3. For a custom range, select a start and end date from the calendar and click **Apply**.
</Accordion>

***

## How Do I Download My Invoice Records?

<Accordion title="Export Invoice Records" icon="far fa-download">
  To download invoice and transaction records:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Invoices** under **Payment Tools**.


  <Image src="https://files.readme.io/38614931076cc05791bfba99a8241cc8ee9bb5bfe7d3a5ebc49c06704cf1d674-Screenshot_2025-06-02_at_7.31.48_PM.png" align="center" caption="Invoices list" border={true} />


  2. Click the **Download** drop-down at the top of the list and select a format:

  | Format        | What it includes                                           |
  | ------------- | ---------------------------------------------------------- |
  | **CSV**       | Invoice records as a spreadsheet                           |
  | **XLSX**      | Invoice records in Excel format                            |
  | **TXNS-CSV**  | Transaction records (individual payments) as a spreadsheet |
  | **TXNS-XLSX** | Transaction records in Excel format                        |


  <Image src="https://files.readme.io/6bfdbd8a5aa0302f25076d3779d2ff01d5ee80cafc87811baab72634d1491022-Screenshot_2025-06-02_at_7.35.59_PM.png" align="center" caption="Download options for invoice records" border={true} />


  3. Click **Download Report** on the pop-up when your report is ready.

  <Callout icon="📘" theme="info">
    You can also share the report to one or more email addresses. In the pop-up, enter the email addresses separated by commas and click **Share**.
  </Callout>


  <Image src="https://files.readme.io/30347f87a23905772d7560b05acf0b520004f90911c51441277f4a8b4b93261b-Screenshot_2025-06-02_at_7.36.43_PM.png" align="center" width="412px" caption="Download and share pop-up" border={true} />

</Accordion>

***

## Next Steps

<Cards>
  <Card title="Create an Invoice" href="doc:create-an-invoice" icon="far fa-file-invoice">
    Create and send a new GST-compliant invoice to your customer.
  </Card>

  <Card title="Manage Invoice Items" href="doc:manage-invoice-items" icon="fa-box-open">
    Add, edit, and manage the products and services in your item catalog.
  </Card>

  <Card title="Invoice Troubleshooting" href="doc:invoice-troubleshooting" icon="fa-wrench">
    Fix issues with invoices not being received, payments not going through, or status not updating.
  </Card>

  <Card title="Invoice FAQs" href="doc:invoice-faqs" icon="fa-circle-question">
    Common questions about PayU Invoices.Manage Invoices
  </Card>
</Cards>
