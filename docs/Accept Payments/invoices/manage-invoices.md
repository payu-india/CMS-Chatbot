---
title: Manage Invoices
excerpt: >-
  View, filter, resend, cancel, and download your PayU Invoices from the
  Dashboard.
deprecated: false
hidden: true
link:
  new_tab: false
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


<Image src="https://files.readme.io/67d1d45f0ad241f6d9225c7c9b5066b38e5ece5dbb426a1a56c26d4da3dd0e94-Screenshot_2026-10-05_at_11.45.06_AM.png" align="center" caption="Access Invoices" border={true} />


The list shows all your invoices for the past 7 days by default, with the following columns:

| Column            | What it shows                                            |
| ----------------- | -------------------------------------------------------- |
| **Created On**    | The date on which the invoice was created                |
| **Invoice Links** | The invoice link that is shared with customers           |
| **Title**         | The invoice title you entered when creating it           |
| **Amount**        | The total amount on the invoice                          |
| **Status**        | Current state — Draft, Sent, Paid, Overdue, or Cancelled |
| **Actions**       | Buttons to perform various actions on an invoice         |

***

<Callout icon="🚧" theme="warning">
  ### **Important!**

  Note that you cannot edit invoices after you send the&#x6D;**.** If an invoice has wrong details, deactivate it and create a new one with the correct information.
</Callout>

## What Can I Do With an Invoice?

You can perform the following actions after a button is created:<br />

- View invoice Details
- Edit an invoice
- Resend an invoice
- Duplicate an invoive
- Deactivate an invoice
- Reactivate an invoice
-

### View Invoice Details

<Accordion title="Steps to View Invoice Details" icon="far fa-rectangle-list">
  To view the full details of an invoice:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Invoices** under **Payment Tools**.

     <Image src="https://files.readme.io/68e34abad2b271fdea9cf5e50ae9641a1f996f642786e88b0412403483f227c9-image.png" align="center" caption="Access Invoices" border={true} />


  2) Click the invoice you want to view.

  The invoice detail page displays:

  - Invoice number, title, issue date, and due date
  - Customer name and contact details
  - Itemized breakdown with quantities, rates, and GST
  - Total amount, GST breakdown, and amount paid (if partial payments were made)

    <Image src="https://files.readme.io/a58aa6ab445bf626540bc72014a28f2ca8c0fac0274ff63230f1dc4699c6d4bb-Screenshot_2026-10-05_at_11.58.43_AM.png" align="center" caption="Invoice details" border={true} />

  - Transaction details

    <Image src="https://files.readme.io/4c70ecb593e3cf08f56e2ed2d2565d348eb3d7bb4d8d466de20904976626e1b4-Screenshot_2026-10-05_at_12.00.55_PM.png" align="center" caption="Transaction details" border={true} />


</Accordion>

***

### Edit an Invoice

<Accordion title="Steps to Edit an Invoice" icon="fad fa-pen-nib">
  1. 1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Invoices** under **Payment Tools**.


        <Image src="https://files.readme.io/68e34abad2b271fdea9cf5e50ae9641a1f996f642786e88b0412403483f227c9-image.png" align="center" caption="Access Invoices" border={true} />

  2. Click the edit icon against the required invoice you want to resend.

     <Image src="https://files.readme.io/6d4dd564b8ec47078d78a226479264b617c5b0327f9f3349529ab92760c3e32e-Screenshot_2026-10-05_at_12.20.34_PM.png" align="center" caption="Edit an invoice" border={true} />

  3. You can only add or update these information of an invoice:
     - **Due Date:&#x20;**&#x43;hange the due date if required
     - Add **Notes&#x20;**&#x61;nd **TERMS AND CONDITIONS&#x20;**&#x64;isplayed at the bottom of the page. You should click **Save&#x20;**&#x64;isplayed next to the respoective sections headings to save the changes.

       <Image src="https://files.readme.io/23dfa5ee4dde79210d3f0e30e76a199aae38bc3b52700797435738f986b51d38-Screenshot_2026-10-05_at_12.27.05_PM.png" align="center" caption="Add Notes and Terms and Conditions" border={true} />

</Accordion>

### Resend an Invoice

<Accordion title="Steps to Resend an Invoice" icon="far fa-paper-plane">
  To resend an invoice:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Invoices** under **Payment Tools**.

     ![](https://files.readme.io/b921c38c7c7ac7b29a674b25d3abf60daf8bfd0db5fecaba632abfde9e0cd46e-image.png)
  2. Click the share icon against the required invoice you want to resend.

     <Image src="https://files.readme.io/be99b1f5a5970c3f58a90bd4aa96ed96bf7a25317d41494a34dd2b4f09450510-Screenshot_2026-10-05_at_12.09.32_PM.png" align="center" caption="Share an invoice" border={true} />

  3. Share the invoice using any of the following options:
     - Copy the link and share it manually
     - Share the link via WhatsApp or Facebook
     - Phone or email by entering either of the details and clicking **Send Invoice**

     <Image src="https://files.readme.io/6cf82fadbc0731416a7bed17c3e41920e99f4344ab3cec6435663677ce9d5b5f-Screenshot_2026-10-05_at_12.17.07_PM.png" align="center" caption="3 ways to resend an invoice" border={true} />


  <Callout icon="fad fa-alarm-exclamation" theme="error">
    ### **Important!**

    You can only resend invoices that are in **Sent** or **Overdue** status. Paid and Cancelled invoices cannot be resent.
  </Callout>
</Accordion>

***

### Duplicate an Invoice

<Accordion title="Steps to Duplicate an Invoice" icon="fad fa-copy">
  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Invoices** under **Payment Tools**.


  <Image src="https://files.readme.io/b921c38c7c7ac7b29a674b25d3abf60daf8bfd0db5fecaba632abfde9e0cd46e-image.png" align="center" caption="Access Invoices" border={true} />


  2. Click the invoice you want to duplicate.
  3. Click **Duplicate Invoice&#x20;**&#x64;isplayed on the top-right of the page.

     <Image src="https://files.readme.io/6fc6afe245bb5142e58217737eba749a0281579f61ffabe51ef260d99c6eaa06-Screenshot_2026-10-05_at_1.31.43_PM.png" align="center" caption="Duplicate an invoice" border={true} />

  4. Enter the details and change the settings as required.
  5. Click either of the following:
     1. **Save&#x20;**&#x74;o save the invoice
     2. **Send Invoice&#x20;**&#x74;o send the invoice using the available options
</Accordion>

***

### Deactivate an Invoice

<Accordion title="Steps to Deactivate an Invoice" icon="far fa-ban">
  Deactivating an invoice marks it as void. The customer can no longer pay it.

  To deactivater an invoice:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Invoices** under **Payment Tools**.

     <Image src="https://files.readme.io/062dfc9778dc06bf9f02a84c4dd4388a14c8596e9341a21a263f40d603416ff6-image.png" align="center" caption="Access invoices" border={true} />

  2. Click the deactivate icon against the required invoice.

     <Image src="https://files.readme.io/a564b37e68dc153f44991c77cc23d9b36090f9ff5014760e2ddd8a8a90402069-Screenshot_2026-10-05_at_1.40.33_PM.png" align="center" caption="Deactivate an invoice" border={true} />

  3. Click **Yes, Deactivate** on the **Are you sure?&#x20;**&#x63;onfirmation pop-up menu.

  The invoice status changes to **Deactivated**.
</Accordion>

***

### Reactivate an Invoice

<Accordion title="Steps to Reactivate an Invoice" icon="fad fa-repeat">
  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Invoices** under **Payment Tools**.

     <Image src="https://files.readme.io/629adf8c5db24dca0a4c78b619ec1ccbe86c4154515cfbdbca7bf7c9f2d98d7d-image.png" align="center" caption="Access Invoices" border={true} />

  2. Find the deactivated invoice you want to activate again and click the activate icon.

     <Image src="https://files.readme.io/f4be6ca2aad6a0a76e4336216b17e80708cb4b56fd201d1abf4261d901d9a1d7-Screenshot_2026-10-05_at_1.47.40_PM.png" align="center" caption="Reactivate an invoice" border={true} />

  3. Click **Yes, Activate&#x20;**&#x6F;n the **Are you sure?&#x20;**&#x63;onfirmation pop-up menu.

  The invoice status changes to **Active**.
</Accordion>

## How Do I Search for an Invoice?

You can search for an invoice with these options:

<Accordion title="Search by Invoice Number or Title" icon="far fa-magnifying-glass">
  Use the **Search** field at the top of the Invoices list to find a specific invoice by its number or title. Type any part of the invoice number or title and the list filters in real time.


  <Image src="https://files.readme.io/ed92abe072724f0d80c3cfc617383a819b971b4481142f2cd3385eb6f5dd4eb4-Screenshot_2026-10-05_at_1.59.21_PM.png" align="center" caption="Seacrh by invoice number or title" border={true} />

</Accordion>

<Accordion title="Filter by Status" icon="far fa-filter">
  To filter invoices by their payment status:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Invoices** under **Payment Tools**.

     <Image src="https://files.readme.io/40e3b71d01f845e1c95f7ddf0aa7a449270abf0371502cfcb163c23fb5d55384-image.png" align="center" caption="Access invoices" border={true} />


  2) Click the **Filter** drop-down and select one or more statuses:

  | Status          | What it means                                           |
  | --------------- | ------------------------------------------------------- |
  | **Draft**       | Saved but not sent to the customer yet                  |
  | **Actice**      | Sent to the customer and active                         |
  | **Deactivated** | Manually deactivated. This invoice is no longer payable |
  | **Expired**     | The invoice is expired                                  |

  3. Click **Apply** to filter the list.

     <Image src="https://files.readme.io/70ea76ae12ebd5bfec0e865064274a8b476c8855d17fd46b160ff79389e80193-Screenshot_2026-10-05_at_2.03.47_PM.png" align="center" caption="Filter the list of invoices" border={true} />

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
