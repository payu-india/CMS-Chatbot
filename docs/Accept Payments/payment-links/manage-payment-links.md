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

All management actions on this page happen in the PayU Dashboard. No developer or code needed.

***

## How Do I Open My Payment Links?

1. Log in to the [PayU Dashboard](https://onboarding.payu.in/).
2. In the left navigation, select **Payment Tools > Payment Links**.

The Payment Links Dashboard opens on the **Payment Link** tab.


<Image src="https://files.readme.io/cc35b704632bded3088580a070ffaf24f203c3713f7880fb0a2cdc6e5b8bc842-Screenshot_2025-06-02_at_7.05.43_PM.png" align="center" caption="Payment Links Dashboard" border={true} />


The table shows one link per row with these columns: **Created On**, **Payment Link** (the URL), **Purpose of Payment**, **Amount**, **Status**, **Actions** (Duplicate / Share / Disable), and **Details**.

***

## How Do I Filter My Links?

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
  3. For a custom range, select **Custom Range**, choose a start date and end date from the calendar, then click **Apply**.


  <Image src="https://files.readme.io/ee050997f17cdc2030467be8855624d90886bb2d8296f698dc594d24713effcb-Screenshot_2025-06-04_at_12.22.39_PM.png" align="center" caption="Calendar view — custom date range selection" border={true} />

</Accordion>

***

## How Do I Take Action on a Link?

<Accordion title="Duplicate a link" icon="far fa-copy">
  Duplicating creates a new link pre-filled with the same settings (amount, purpose, options) — useful for reusing configurations or correcting a mistake.

  1. Find the link in the table.
  2. In the **Actions** column, click the **Duplicate** icon.
  3. The Create New Payment Link panel opens with the existing link's settings pre-filled.
  4. Edit any fields you need to change (for example, the expiry date).
  5. Click **Create and Send Payment Link**.

  <Callout icon="📘" theme="info">
    Duplicating does not deactivate the original link. If you want to replace a link (e.g., wrong amount), duplicate it first with the correct details, then deactivate the original.
  </Callout>
</Accordion>

<Accordion title="Resend or share a link" icon="far fa-share">
  1. Find the link in the table.
  2. In the **Actions** column, click the **Share** icon.
  3. Choose to send via **SMS**, **Email**, or copy the URL manually.

  You can share a link as many times as needed as long as it is **Active** and has not reached its max transaction limit.
</Accordion>

<Accordion title="Deactivate a link" icon="far fa-ban">
  Deactivating prevents any further payments on the link. Customers who click it will see a message that it is no longer active.

  1. Find the link in the table.
  2. In the **Actions** column, click the **Disable** icon (🚫).
  3. Confirm the action in the pop-up.

  The link status changes to **Deactivated**.

  <Callout icon="🚧" theme="warning">
    **Deactivation is permanent from the Dashboard.** To accept payment for the same purpose again, duplicate the link first, then deactivate the original. Via API, a deactivated link can be re-activated using `active: true`.
  </Callout>
</Accordion>

<Accordion title="View link details" icon="far fa-rectangle-list">
  1. Find the link in the table.
  2. Click **Details** in the rightmost column.

  The detail view shows the full link configuration (amount, purpose, expiry, options), a complete transaction history (each payment made on this link), and any customer details collected at checkout.
</Accordion>

***

## How Do I Export My Data?

<Accordion title="Export payment link records" icon="far fa-download">
  1. Click the **Download** drop-down at the top of the table.
  2. Select a format:

  | Format                           | Contents                          |
  | -------------------------------- | --------------------------------- |
  | **csv**                          | Summary of payment links          |
  | **xlsx**                         | Summary of payment links (Excel)  |
  | **Txn - csv**                    | Transaction-level detail per link |
  | **Txns - xlsx**                  | Transaction-level detail (Excel)  |
  | **Old Payment Link Data - csv**  | Legacy link data                  |
  | **Old Payment Link Data - xlsx** | Legacy link data (Excel)          |

  3. A pop-up shows the report generation status. Click **Download** when ready.


  <Image src="https://files.readme.io/238e4d7aa7373144cd4799cc70a0bdc1c363df5e428ffa21ce9f67bdbd378ade-dashboard_payment_links_download_reports_drop-down.png" align="center" caption="Download drop-down with format options" border={true} />

</Accordion>

***

## How Do I Create Links in Bulk?

<Accordion title="Bulk upload via CSV" icon="far fa-upload">
  1. Click the **Bulk Uploads** tab in the Payment Links Dashboard.
  2. Download the CSV template.
  3. Fill in the link details for each row (amount, description, expiry, customer details, etc.).
  4. Upload the completed CSV.

  PayU processes the upload and creates all links in the batch. Errors (such as missing mandatory fields or duplicate invoice numbers) are shown per row in the upload result.

  <Callout icon="📘" theme="info">
    For fully automated bulk creation from your own systems, use the [Create Payment Link API](doc:api-create-share).
  </Callout>
</Accordion>

***

## Next Steps

<Cards>
  <Card title="Payment Link Options" href="doc:payment-link-options" icon="fa-sliders">
    Expiry, partial payments, custom fields, and notifications.
  </Card>

  <Card title="Send a Payment Link" href="doc:send-a-payment-link" icon="fa-paper-plane">
    Step-by-step guide to creating and sending a payment link.
  </Card>

  <Card title="Payment Links Troubleshooting" href="doc:payment-links-troubleshooting" icon="fa-wrench">
    Fix issues with links not working, payments not reflecting, and more.
  </Card>
</Cards>
