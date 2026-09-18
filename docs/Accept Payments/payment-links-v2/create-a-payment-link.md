---
title: Create a Payment Link
excerpt: >-
  Create a payment link in the PayU Dashboard and share it with your customer in
  under 5 minutes. No code required.
deprecated: false
hidden: true
metadata:
  title: Create a Payment Link — 5-Minute Quickstart | PayU Docs
  description: >-
    Step-by-step guide to creating and sending a PayU Payment Link in 5 minutes.
    No code required — share over WhatsApp, SMS, or email from the Dashboard.
  keywords:
    - send payment link payu
    - create payment link tutorial
    - how to create payment link india
    - payu payment link step by step
    - payment link whatsapp india
    - no code payment quickstart payu
    - payu dashboard create payment link
    - payment link sms notification
    - accept payment link no website
    - payu payment link guide
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payment-links-v2
      title: Payment Links
      type: basic
---
{/* NEW CONTENT: Template F — T1 Quickstart/Tutorial (V2 format) */}

<Banner
  isInline={true}
  message="Integration effort: No code or website required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

Create a Payment Link from the PayU Dashboard and share it with your customer in under 5 minutes without the help of a developer or code.

***

## What All I Need?

<Cards>
  <Card title="A PayU Merchant Account" icon="far fa-table-cells-column-unlock">
    <Columns layout="fixed">
      <Column>
        [Set up your account](doc:set-up-your-account) if you have not already.
      </Column>
    </Columns>
  </Card>

  <Card title="Dashboard Access" icon="far fa-pager">
    Log in to the [PayU Dashboard](https://onboarding.payu.in/) to check whether you have access to the PayU dashboard before you start.
  </Card>
</Cards>

***

## How Do I Create a Payment Link?

To create and send a Payment Link:

<Accordion title="1. Open Payment Links on the Dashboard" icon="far fa-grid-2">
  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin?first_visit_url=https%3A%2F%2Fpayu.in%2F&last_visit_url=https%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F%2Chttps%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F">PayU dashboard</Anchor>.
  2. Expand **Payment Tools&#x20;**&#x61;nd clic&#x6B;**&#x20;Payment Links&#x20;**&#x64;isplayed in the left navigation.


  <Image src="https://files.readme.io/35fe8235c387b22f93c4af37425c7ce2077534a981c17a8abb22d037f98486a1-Screenshot_2026-09-18_at_11.04.00_AM.png" align="center" caption="Go to Payment Links" border={true} />

</Accordion>

<Accordion title="2. Create a new link" icon="far fa-link">
  1. Click **Create New Payment Links** displayed in the top-right corner of the **Payment Links** page.


  <Image src="https://files.readme.io/889bdf1e584b7531c1f79d1396230fbbfcb7ae0c6beaa5789d764d57c95aef8f-Screenshot_2026-09-18_at_11.06.18_AM.png" align="center" caption="Create New Payment Link panel" border={true} />


  2. Provide the these details in respective sections:
     1. **Payment Link Details**
        <Callout icon="📘" theme="info">
          ### **Required Fields**

            <RequiredStar legend />
        </Callout>
        | Information                                                   | Description                                          |
        | ------------------------------------------------------------- | ---------------------------------------------------- |
        | <RequiredStar param="merchant_id" bold={true}></RequiredStar> | A short description about the link you are creating. |
        | **Total Amount**                                              |                                                      |

  - **Amount** — enter the payment amount in INR.
  - **Purpose** — a brief description, e.g. _"Invoice #1042 — Web Design Services"_.

  Optional fields:

  - Toggle **Allow Partial Payment** on if you want the customer to pay in instalments.
  - Set **Max Transactions Allowed** to cap how many times the link can be used (leave blank for unlimited).
</Accordion>

<Accordion title="3. Add invoice or reference details (optional)" icon="far fa-file-invoice">
  Click **Add more details** to expand additional configuration fields:


  <Image src="https://files.readme.io/c73e2f1739d759815cf7503096e7c971927f4986c8b0dddafc6951b4a760cff2-dashboard_create_new_payment_link_step2.png" align="center" caption="Add more details panel" border={true} />


  | Field                 | When to use                                  |
  | --------------------- | -------------------------------------------- |
  | Invoice Number        | Tie the link to your internal invoice ID     |
  | Tax                   | Add a tax line to the payment record         |
  | Shipping              | Add a shipping charge                        |
  | Address Details       | Collect delivery address from the customer   |
  | UDF 1–5               | Custom key-value fields for your own records |
  | Merchant Reference ID | Your internal order or booking reference     |

  Click **Add Fields** to apply your selection and return to the main panel.
</Accordion>

<Accordion title="4. Set customer details and expiry" icon="far fa-user">
  Scroll to the **Customer Details** section:


  <Image src="https://files.readme.io/09b1e5b30bbcb46d0d1b457bfff8ccf422f49190014ec95d198640db0bf55eb2-dashboard_create_new_payment_link_step3.png" align="center" caption="Customer Details section" border={true} />


  - **Customer Name / Email / Phone** — pre-fills the checkout page and enables automatic delivery.
  - **Notify via SMS / Notify via Email** — toggle on to have PayU send the link automatically on creation.
  - **Link Expiry** — defaults to 1 year from today; set a shorter date for time-sensitive offers.

  <Callout icon="📘" theme="info">
    If you enter the customer's phone or email and toggle notifications on, PayU sends the link the moment you click **Create** — no manual copying or sharing needed.
  </Callout>
</Accordion>

<Accordion title="5. Add checkout fields (optional)" icon="far fa-list-check">
  Scroll to **Additional Customer Details** to specify what PayU collects from your customer at checkout:

  - Standard fields: Customer Name, Address, Email, Mobile
  - Custom fields: click **Add New Fields+** and configure:
    - **Field Type** — Alphanumeric, Calendar, or Dropdown
    - **Field Name** — the label the customer sees
    - **Mark as Mandatory** — toggle on to require the field before payment can proceed


  <Image src="https://files.readme.io/d322acc2c2795a82b620e501380e4366576307f7a1c17ff79b89c6f0cfda5e66-dashboard_payment_link_with_additional_details.png" align="center" caption="Checkout page with additional customer detail fields enabled" border={true} />

</Accordion>

<Accordion title="6. Create and send" icon="far fa-paper-plane">
  Click **Create and Send Payment Link** in the top-right corner.

  - **If notifications are on** → PayU sends the link to the customer immediately via SMS/email.
  - **If not** → the link appears in your Payment Links Dashboard. Copy the URL from the **Payment Link** column and share it over WhatsApp, email, or any channel.
</Accordion>

***

## What Happens After My Customer Pays?

1. Customer clicks the link and completes payment on the PayU-hosted checkout page.
2. PayU updates the link status to **Paid** in your Dashboard.
3. The transaction appears in **Transactions** in your Dashboard.
4. If you have webhooks configured, PayU sends a `payment.success` event to your server.

<Callout icon="📘" theme="info">
  Webhooks are optional — your Dashboard always reflects the current payment status without any webhook setup.
</Callout>

***

## What Do I Do If Something Goes Wrong?

| Problem                                         | Fix                                                                                                                                      |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Customer says the link isn't opening            | Check the link status in your Dashboard — it may be expired or deactivated.                                                              |
| Customer didn't receive the SMS or email        | Confirm phone/email were entered and the notification toggle was on before creation. Reshare from **Actions > Share** in your Dashboard. |
| Customer paid but Dashboard still shows Pending | Wait 5–10 minutes and refresh. See [Payment Links Troubleshooting](doc:payment-links-troubleshooting).                                   |
| Wrong amount or details on the link             | Deactivate it and create a new one — links cannot be edited after creation. Duplicate the link to reuse the settings.                    |

***

## Next Steps

<Cards>
  <Card title="Manage Payment Links" href="doc:manage-payment-links" icon="fa-list-check">
    Filter, duplicate, resend, deactivate, and export your links.
  </Card>

  <Card title="Payment Link Options" href="doc:payment-link-options" icon="fa-sliders">
    Expiry dates, partial payments, custom fields, and notifications.
  </Card>

  <Card title="Payment Links Overview" href="doc:payment-links-overview" icon="fa-circle-info">
    Full overview — use cases, supported payment methods, and API access.
  </Card>
</Cards>
