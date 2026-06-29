---
title: No Code Solutions
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
PayU no-code solutions let merchants collect payments quickly without building a custom checkout integration. Create payment links, embed payment buttons, or send invoices from the PayU Dashboard—or automate payment links through APIs for CRM, cart abandonment, and marketplace use cases.

Customers can pay through their preferred methods, including UPI, Net Banking, debit cards, wallets, and credit cards.

<Callout icon="👍" theme="okay">
  ### Before you begin:

  Register for a account with PayU before you start integration. Contact your PayU Key Account Manager to enable Payment Links, Payment Buttons, or Invoices on the PayU Dashboard. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Callout>

## Overview of no-code payment methods

PayU offers three primary no-code ways to collect payments. Choose based on how you reach customers and whether you need API automation.

| Method                                               | What it is?                                                      | How you share or deploy?                                       | Best for                                                                                                         |
| ---------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [**Payment Links**](doc:payment-links-dashboard)     | A shareable URL with amount, purpose, and optional custom fields | SMS, email, WhatsApp, social media, CRM, or any channel        | Merchants without a website, social commerce, utility bills, EMI/SIP collections, customized or partial payments |
| [**Payment Buttons**](doc:payment-buttons-dashboard) | An embeddable Pay Now / Buy Now / Donate button for your site    | Paste HTML/JavaScript snippet on your website or blog          | Blogs, landing pages, donations, fixed or customer-entered amounts                                               |
| [**Payment Invoices**](doc:invoices-dashboard)       | A branded invoice emailed to customers with an online pay option | Email invoice to customer; customer pays from the invoice link | B2B billing, professional invoicing, itemized charges                                                            |

<Accordion title="Payment Links — dashboard vs API" icon="fa-link">
  **Dashboard** ([Payment Links](doc:payment-links-dashboard))

  * Create single links with amount, purpose, partial payment, expiry, and custom form fields
  * [Bulk upload](doc:bulk-upload-to-create-multiple-payments-links) multiple links via CSV
  * Manage, categorize, export, and share links from the Dashboard

  **API** ([Integration APIs for Payment Links](doc:integration-api-for-payment-links))

  * Automate link creation from CRM, ERP, or marketplace backends
  * Send cart-abandonment or personalized payment URLs programmatically
  * [Bulk create links via API](doc:create-payment-link-via-bulk-upload-apis) using CSV upload endpoints
  * Request add-on customer details within the payment journey via custom form fields on the link
</Accordion>

<Accordion title="Payment Buttons — embed on your site" icon="fa-hand-pointer">
  Payment Buttons require no API integration. From **Payment Tools** > **Payment Buttons** on the Dashboard:

  1. Customize button label (Buy Now, Pay Now, Book Now, Donate Now), amount, colour, and size
  2. Configure checkout page details and advanced options
  3. Copy the generated embed code onto your website or blog

  Track payments via [Webhooks for Payments](doc:webhooks). For step-by-step setup, refer to [Payment Buttons](doc:payment-buttons-dashboard).
</Accordion>

<Accordion title="Payment Invoices — bill and collect" icon="fa-file-invoice">
  From **Payment Tools** > **Invoices** on the Dashboard:

  * [Create customers](doc:create-a-new-customer) and [manage invoice items](doc:manage-invoice-items)
  * [Create and send invoices](doc:create-an-invoice) with line items and due dates
  * Search, filter, download, or share invoice reports

  Customers receive the invoice by email and pay online through the linked checkout. For details, refer to [Payment Invoices](doc:invoices-dashboard).
</Accordion>

## Use cases

<Accordion title="Where no-code payments help" icon="fa-bullseye">
  * **Small businesses** — Merchants without a website or app can start accepting online payments via shareable links
  * **Social media trade** — Share payment links on WhatsApp, Facebook, Instagram, and Twitter
  * **Utility services** — Collect electricity, telephone, insurance, and gas bill payments
  * **EMI collections** — NBFCs and agents can collect SIP instalments, loan EMIs, and credit card bills
  * **Customized payments** — Offer special discounts, advances, warranty fees, or bulk-purchase pricing via links or buttons
</Accordion>

<Accordion title="Payment Links customer journey" icon="fa-route">
  1. Merchant creates a link (Dashboard or API) with amount, description, and optional custom form fields (alphanumeric, calendar, dropdown).
  2. Merchant shares the URL with the customer via SMS, email, or other channels.
  3. Customer opens the link, fills in any custom fields, and selects a payment method.
  4. Customer completes payment on the PayU-hosted checkout page.
  5. Merchant tracks status on the Dashboard, via webhooks, or Verify Payment API.

  <Embed url="https://www.youtube.com/watch?v=rh_FQUMsaT0" title="PayU Payment Links - The easiest way to collect payments from customers or clients!" favicon="https://www.google.com/favicon.ico" image="https://i.ytimg.com/vi/rh_FQUMsaT0/hqdefault.jpg" provider="youtube.com" href="https://www.youtube.com/watch?v=rh_FQUMsaT0" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252Frh_FQUMsaT0%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253Drh_FQUMsaT0%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252Frh_FQUMsaT0%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />
</Accordion>

## Integration guides

The following sections describe how to use PayU no-code payment tools:

- [Payment Links](doc:payment-links-dashboard)
  - [Create a Payment Link](doc:create-a-new-payment-link)
  - [Create Payment Links in Bulk](doc:bulk-upload-to-create-multiple-payments-links)
  - [Customize the Calendar View for Payment Links](doc:customize-the-calendar-view-for-payment-links)
  - [Categorize the Payment Links View](doc:categorize-the-payment-links-view)
  - [Export the Payment Link History](doc:export-the-payment-link-history)
  - [Integration APIs for Payment Links](doc:integration-api-for-payment-links)
  - [Create Payment Links via Bulk Upload – APIs](doc:create-payment-link-via-bulk-upload-apis)
- [Payment Buttons](doc:payment-buttons-dashboard)
- [Payment Invoices](doc:invoices-dashboard)
  - [Create an Invoice](doc:create-an-invoice)
  - [Manage Invoice Items](doc:manage-invoice-items)
  - [Create a New Customer](doc:create-a-new-customer)

## APIs used in No Code Payments integration

| API                                                                    | Purpose                                                                                                                                 |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| [Get Token API – Payment Links](ref:get-token-api-payment-links)       | Obtain an OAuth bearer token (`create_payment_links`, `read_payment_links`, `update_payment_links` scopes) for Payment Links API calls. |
| [Revoke Token API – Payment Links](ref:revoke-token-api-payment-links) | Invalidate an access token when no longer needed.                                                                                       |
| [Create Payment Link API](ref:create-payment-links)                    | Create a payment link with amount, description, customer details, and callback URL.                                                     |
| [Share Payment Link API](ref:share_payment_link_api)                   | Share a created payment link with customers via configured channels.                                                                    |
| [Get Single Payment Link API](ref:get-single-payment-link)             | Retrieve details for one payment link.]\(doc:integration-api-for-payment-links).                                                        |
| [Get All Payment Links API](ref:get-all-payment-links-api)             | List payment links with filters and pagination.                                                                                         |

<br />
