---
title: Payment Link Options
deprecated: false
hidden: true
metadata:
  robots: index
---
{/* NEW CONTENT: Template D — Concept page (V2 format) */}

<Banner
  isInline={true}
  message="Integration effort: No code or website required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

All options on this page are configured in the PayU Dashboard during link creation — no developer needed. To access them, click **Add more details** or scroll to the relevant section in the **Create New Payment Link** panel.

→ For the full creation walkthrough, see [Send a Payment Link](doc:send-a-payment-link).

***

## What Options Can I Configure?

| Option                 | Default   | What it does                                         |
| ---------------------- | --------- | ---------------------------------------------------- |
| Expiry Date            | 1 year    | Stops the link after a set date/time                 |
| Partial Payments       | Off       | Lets customers pay any amount less than the total    |
| Max Transactions       | Unlimited | Caps how many times the link can be used             |
| Customer Notifications | Off       | Auto-sends the link via SMS/email on creation        |
| Custom Checkout Fields | None      | Collects extra info from customers at checkout       |
| Invoice Fields         | None      | Adds invoice number, tax, and shipping to the record |
| UDF Fields             | None      | Passes custom key-value data through the transaction |
| Merchant Reference ID  | None      | Ties the link to your internal order/reference       |

<Callout icon="🚧" theme="warning">
  **Links cannot be edited after creation.** If you made a mistake, [duplicate the link](doc:manage-payment-links) with corrected settings and deactivate the original.
</Callout>

***

## How Do I Configure Each Option?

<Accordion title="Expiry Date — stop accepting payments after a deadline" icon="far fa-calendar-xmark">
  Sets a date and time after which the link stops accepting payments. Customers who click an expired link see a message that the link is no longer active.

  **Where to set it:** Customer Details section → **Link Expiry** field (date picker).

  **When to use it:** Time-limited offers, event registrations with a deadline, or advance payments due before a specific date.

  <Callout icon="📘" theme="info">
    To accept payments again after a link expires, [duplicate it](doc:manage-payment-links) and set a new expiry date. Expired links cannot be re-activated from the Dashboard. (Via API, you can extend expiry using the [Cancel / Change Status API](doc:api-cancel-status).)
  </Callout>
</Accordion>

<Accordion title="Partial Payments — let customers pay in instalments" icon="far fa-money-bill-wave">
  {/* EXISTING CONTENT: adapted from create-a-new-payment-link.md */}

  Allows customers to pay any amount less than the total in a single transaction. Useful for collecting a deposit upfront with the balance to follow.

  **Where to set it:** Main Create Link panel → toggle **Allow Partial Payment** on.

  **When to use it:** Deposit or advance collection (e.g., 30% upfront on a project), dues recovery.

  <Callout icon="🚧" theme="warning">
    You cannot specify a minimum partial amount — the customer decides how much to pay. For structured auto-debiting in instalments, use [Recurring Payments](doc:recurring-payments) instead.
  </Callout>
</Accordion>

<Accordion title="Max Transactions — cap usage on a single link" icon="far fa-hashtag">
  Caps the total number of successful payments accepted on this link. Once the limit is reached, the link automatically deactivates.

  **Where to set it:** Main Create Link panel → **Max Transactions Allowed** field. Leave blank for unlimited.

  **When to use it:** Limited-availability offers ("First 50 customers only"), single-use personalised invoices (set to 1), or capacity-limited events.
</Accordion>

<Accordion title="Customer Notifications — auto-send the link on creation" icon="far fa-bell">
  Automatically sends the payment link to the customer via SMS, email, or both at the moment the link is created.

  **Where to set it:** Customer Details section → enter email and/or phone → toggle **Notify via SMS** and/or **Notify via Email** on.

  **When to use it:** Any time you have the customer's contact details and want PayU to deliver the link immediately on creation.

  <Callout icon="📘" theme="info">
    If you don't toggle notifications on, the link is still created and available in your Dashboard to share manually. Notifications fire once — at creation time only.
  </Callout>
</Accordion>

<Accordion title="Custom Checkout Fields — collect extra info from customers" icon="far fa-input-text">
    {/* EXISTING CONTENT: adapted from create-a-new-payment-link.md */}

  Adds extra input fields to the PayU-hosted checkout page that the customer fills in before completing payment.

  **Where to set it:** Additional Customer Details section.

  **Standard fields available:** Customer Name, Customer Address, Customer Email, Customer Mobile.

  **Custom fields:** Click **Add New Fields+** and configure:

  - **Field Type** — Alphanumeric, Calendar, or Dropdown
  - **Field Name** — the label the customer sees
  - **Mark as Mandatory** — toggle on to require the field before payment

  **When to use it:** Collecting delivery address for physical goods, capturing an order or membership reference, or any structured info required for your service.


  <Image src="https://files.readme.io/8eca3400c847299b4e879cf737dee9b719af66bf2a384e7a3054c62572b0dcac-dashboard_create_new_payment_link_custom_field.png" align="center" caption="Custom field configuration" border={true} />

</Accordion>

<Accordion title="Invoice Fields — add invoice number, tax, and shipping" icon="far fa-file-invoice">
  {/* EXISTING CONTENT: adapted from create-a-new-payment-link.md */}

  Adds invoice-specific data to the link record — visible in Dashboard exports and useful for accounting or reconciliation.

  **Where to set it:** Click **Add more details** → select the checkboxes for the fields you want → click **Add Fields**.

  | Field           | What to enter                                         |
  | --------------- | ----------------------------------------------------- |
  | Invoice Number  | Your internal invoice reference (e.g., INV-2026-0042) |
  | Tax             | Tax amount in INR                                     |
  | Shipping        | Shipping charge in INR                                |
  | Address Details | Customer shipping or billing address                  |

  <Callout icon="📘" theme="info">
    Invoice fields are metadata on the link record. They appear in exports but do not change the payment amount the customer sees — which is always set by the **Amount** field.
  </Callout>
</Accordion>

<Accordion title="UDF Fields — pass custom data through the transaction" icon="far fa-tag">
  Passes up to five custom key-value pairs (`udf1` through `udf5`) with the payment transaction. These values appear in transaction reports and in the payment success/failure webhook response.

  **Where to set them:** Click **Add more details** → select **UDF** → enter values for `udf1` through `udf5`.

  **When to use them:** Storing your internal order ID, customer segment, or product code alongside the transaction for reporting and reconciliation.
</Accordion>

<Accordion title="Merchant Reference ID — tie the link to your internal records" icon="far fa-link">
  Ties the PayU payment link to your own internal reference — an order ID, booking number, or CRM record. Appears in transaction reports alongside the payment.

  **Where to set it:** Click **Add more details** → select **Merchant Reference ID** → enter your reference string.
</Accordion>

***

## Next Steps

<Cards>
  <Card title="Send a Payment Link" href="doc:send-a-payment-link" icon="fa-paper-plane">
    Step-by-step guide with all options in context.
  </Card>

  <Card title="Manage Payment Links" href="doc:manage-payment-links" icon="fa-list-check">
    Duplicate, deactivate, filter, and export your links.
  </Card>

  <Card title="Payment Links Overview" href="doc:payment-links-overview" icon="fa-circle-info">
    Use cases, supported payment methods, and API access.
  </Card>
</Cards>
