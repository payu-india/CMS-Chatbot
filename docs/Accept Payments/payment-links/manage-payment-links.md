---
title: Manage Payment Links
excerpt: >-
  View, filter, duplicate, share, deactivate, and export your Payment Links, all
  from the PayU Dashboard.
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: Manage Payment Links — Dashboard Guide | PayU Developer
  description: >-
    Filter, duplicate, share, deactivate, and export PayU Payment Links from the
    Dashboard — no developer needed. Includes bulk upload and CSV export.
  keywords:
    - manage payment links payu
    - filter payment links dashboard
    - deactivate payment link payu
    - export payment links csv
    - duplicate payment link
    - bulk upload payment links
    - payu payment links dashboard
    - share payment link again
    - payment link history export
    - payu no code payment management
  robots: index
next:
  description: Explore related information and resources.
---
{/* NEW CONTENT: Template B1 — T1 Dashboard Walkthrough (V2 format) */}

{/* EXISTING CONTENT: adapted from categorize-the-payment-links-view.md, export-the-payment-link-history.md, customize-the-calendar-view-for-payment-links.md */}

<Banner
  isInline={true}
  message="Integration effort: No code or website required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

You can manage payment links from the PayU Dashboard after they are created and live.

<Callout icon="fad fa-rectangle-new" theme="warn">
  ### New to Payment Links?

  Start with the [Payment Links Overview](doc:payment-links-overview) or follow the [step-by-step guide to create your first link](doc:send-a-payment-link). To manage links from your own system, see the [Fetch API](doc:api-fetch) and [Cancel / Update Status API](doc:api-cancel-status).
</Callout>

***

## Access Your Payment Links

To open your links: log in to [PayU Dashboard](https://onboarding.payu.in/) and click **Payment Links&#x20;**&#x75;nder **Payment Tools**.


<Image src="https://files.readme.io/bca170f5ad6ba34eb18f1e8ba1a7072d45be0b24fd0f32fd4bfdf22d015682ca-Screenshot_2026-09-21_at_9.35.56_AM.png" align="center" caption="Access Payment Links" border={true} />


***

## What Can I Do With a Payment Link After It Is Created?

You can perform the following actions after a link is created:

<Accordion title="See Payment Link Details" icon="far fa-rectangle-list">
  To see payment link details:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin?first_visit_url=https%3A%2F%2Fpayu.in%2F&last_visit_url=https%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F%2Chttps%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F">PayU dashboard</Anchor> and go to **Payment Links&#x20;**&#x75;nder **Payment Tools.**

     <Image src="https://files.readme.io/53215c3e4e7294d15669cb34cd231730787e24e86505214a8d80d48cb5b67c19-image.png" align="center" caption="Access Payment Links" border={true} />

     A list of created payment links is displayed with the following information:
     - **Created On**
     - **Purpose of Payment**
     - **Invoice ID**
     - **Amount**
     - **Payment Link**
     - **Payment Type**
     - **Payment Status**
     - **Status**
  2. Click the Payment Link you want to view the details.

     <Image src="https://files.readme.io/fada3c576d9d091f8a41e2cefe2ce555ff3878f8debea9b8ddc1e08b76191d43-Screenshot_2026-09-21_at_10.21.28_AM.png" align="center" caption="Click to view details" border={true} />


  The link details are divided in to the following sections:

  <Accordion title="Link Details" icon="fad fa-link">
    The following details are displayed in this section:

    - **Name:&#x20;**&#x4E;ame of the Payment Link you enterd during creation.
    - **Status:&#x20;**&#x53;tatus of the payment link. Refer to the Payment Link statuses for more information.
    - **Link:&#x20;**&#x54;he payment with options to copy and share via WhatsApp and Facebook.
    - **Invoice ID:&#x20;**&#x54;he auto generated invoice ID. For example, **INV331178996540608300.**
    - **Total Amount:&#x20;**&#x54;he total amount for which the link is created.
    - **Type:&#x20;**&#x54;he payment type. The value can be either **Partial&#x20;**&#x6F;r **Full**.
    - **Share:&#x20;**&#x4F;ptions to copy the link or share via WhatsApp, Facebook or to any other mobile number or email ID.

      <Image src="https://files.readme.io/18374beecc40c725bf806f3eea419f259e50c0928a43a7573e94c8a661280637-Screenshot_2026-09-21_at_10.40.08_AM.png" align="center" caption="Share the Payment Link" border={true} />

  </Accordion>

  <Accordion title="" icon="fa-info-circle">

  </Accordion>
</Accordion>

<Accordion title="Duplicate a link" icon="far fa-copy">
  Duplicating creates a brand-new link pre-filled with the same settings — amount, purpose, and options — so you don't have to fill everything in again. Use it to reuse a configuration, correct a mistake on an existing link, or run the same payment request for a different customer.

  1. Find the link in the table.
  2. In the **Actions** column, click the **Duplicate** icon.
  3. The Create New Payment Link panel opens with the existing link's settings pre-filled.
  4. Edit any fields you need to change — for example, the expiry date or customer details.
  5. Click **Create and Send Payment Link**.

  <Callout icon="📘" theme="info">
    Duplicating does not deactivate the original link. If you want to replace a link (e.g., wrong amount was set), duplicate it with the correct details first, then deactivate the original.
  </Callout>
</Accordion>

<Accordion title="Share or resend a link" icon="far fa-share">
  You can send the link to a customer at any time as long as it is still **Active**.

  1. Find the link in the table.
  2. In the **Actions** column, click the **Share** icon.
  3. Choose to send via **SMS**, **Email**, or copy the URL manually and share it over WhatsApp or any other channel.

  There is no limit on how many times you can share a link — each share just sends the same URL again.
</Accordion>

<Accordion title="Deactivate a link" icon="far fa-ban">
  Deactivating stops any further payments on the link. Customers who click it will see a message that it is no longer active.

  1. Find the link in the table.
  2. In the **Actions** column, click the **Disable** icon (🚫).
  3. Confirm the action in the pop-up.

  The link status changes to **Deactivated**.

  <Callout icon="🚧" theme="warning">
    **Deactivation is permanent from the Dashboard.** To accept payment for the same purpose again, duplicate the link first, then deactivate the original. If you need to re-activate a deactivated link programmatically, use the [Cancel / Update Status API](doc:api-cancel-status) with `active: true`.
  </Callout>
</Accordion>

<Accordion title="See all transactions made on a link" icon="far fa-clock-rotate-left">
  A single payment link can be paid multiple times (unless you set a max transaction limit). To see every payment made on it:

  1. Find the link in the table.
  2. Click **Details** in the rightmost column.
  3. Scroll to the **Transaction History** section.

  Each row shows the transaction ID, amount paid, date, and status.
</Accordion>

***

## How Do I Look Up a Specific Link?

<Callout icon="📘" theme="info">
  ### **Payment Link Status**

  Not sure what **Active**, **Paid**, **Expired**, or **Deactivated** mean? See [Payment Link Statuses](doc:send-a-payment-link).
</Callout>

<Accordion title="Filter by status" icon="far fa-filter">
  1. Click the **Filter** drop-down above the link list.
  2. Select one or more status checkboxes: **Active**, **Paid**, **Deactivated**, **Expired**.
  3. Click **Apply**.

  To clear filters, click **Reset** inside the filter panel.


  <Image src="https://files.readme.io/53b5421aae446c8b0143ce30155c6d8789f8f2081d50c084083c0930fe17f839-Screenshot_2025-06-02_at_6.54.04_PM.png" align="center" caption="Filter drop-down with status checkboxes" border={true} />

</Accordion>

<Accordion title="Filter by date range" icon="far fa-calendar">
  1. Click the **Calendar** icon at the top of the table.
  2. For a quick range, select **Today**, **Yesterday**, **Past 7 days**, or **Past 30 days** and click **Apply**.
  3. For a custom range, select **Custom Range**, pick a start and end date from the calendar, then click **Apply**.


  <Image src="https://files.readme.io/ee050997f17cdc2030467be8855624d90886bb2d8296f698dc594d24713effcb-Screenshot_2025-06-04_at_12.22.39_PM.png" align="center" caption="Calendar view — custom date range selection" border={true} />

</Accordion>

***

## Can I Download All My Payment Link Records?

<Accordion title="Export payment link records" icon="far fa-download">
  1. Click the **Download** drop-down at the top of the table.
  2. Select a format:

  | Format                           | Contents                             |
  | -------------------------------- | ------------------------------------ |
  | **csv**                          | Summary of all payment links         |
  | **xlsx**                         | Summary of all payment links (Excel) |
  | **Txn - csv**                    | Transaction-level detail per link    |
  | **Txns - xlsx**                  | Transaction-level detail (Excel)     |
  | **Old Payment Link Data - csv**  | Legacy link data                     |
  | **Old Payment Link Data - xlsx** | Legacy link data (Excel)             |

  3. A pop-up shows the report generation status. Click **Download** when ready.


  <Image src="https://files.readme.io/238e4d7aa7373144cd4799cc70a0bdc1c363df5e428ffa21ce9f67bdbd378ade-dashboard_payment_links_download_reports_drop-down.png" align="center" caption="Download drop-down with format options" border={true} />

</Accordion>

***

## Next Steps

<Cards>
  <Card title="Payment Link Options" href="doc:payment-link-options" icon="fa-sliders">
    Expiry dates, partial payments, custom fields, and notifications.
  </Card>

  <Card title="Send a Payment Link" href="doc:send-a-payment-link" icon="fa-paper-plane">
    Step-by-step guide to creating and sending a payment link.
  </Card>

  <Card title="Payment Links API" href="doc:api-fetch" icon="fa-code">
    Fetch, update, and cancel payment links programmatically.
  </Card>

  <Card title="Payment Links Troubleshooting" href="doc:payment-links-troubleshooting" icon="fa-wrench">
    Fix issues with links not working, payments not reflecting, and more.
  </Card>
</Cards>
