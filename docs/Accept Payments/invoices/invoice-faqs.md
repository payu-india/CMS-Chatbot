---
title: Invoice FAQs
excerpt: >-
  Answers to common questions about PayU Invoices — creation, GST, sending,
  editing, payments, and managing your invoices.
deprecated: false
hidden: true
metadata:
  title: Invoice FAQs | PayU Developer Docs
  description: >-
    Answers to common PayU Invoice questions — creating invoices, GST setup,
    sending to customers, editing after sending, partial payments, and more.
  keywords:
    - payu invoice faq
    - payu gst invoice questions
    - can i edit invoice payu
    - payu invoice partial payment faq
    - payu invoice vs payment link
    - payu invoice customer not received
    - payu invoice overdue
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
    - slug: invoices-workflow
      title: How Invoices Works
      type: basic
---
## General

1. #### What is a PayU Invoice and how does it work?

<Accordion title="Answer" icon="fab fa-adn">
  A <Anchor target="_blank" href="https://docs.payu.in/docs/invoices">PayU Invoice</Anchor> is a professional, GST-compliant billing document you <Anchor target="_blank" href="https://docs.payu.in/docs/create-an-invoice-1">create</Anchor> in the PayU Dashboard and send to your customer. The customer receives it by email or SMS, opens it, and pays through PayU's secure checkout page. The invoice shows an itemized breakdown with GST, the due date, and a pay-now button.
</Accordion>

***

2. #### Do I need a developer or any code to use PayU Invoices?

<Accordion title="Answer" icon="fab fa-adn">
  No. <Anchor target="_blank" href="https://docs.payu.in/docs/invoices">PayU Invoices</Anchor> are managed entirely from the Dashboard. You <Anchor target="_blank" href="https://docs.payu.in/docs/create-an-invoice-1">create the invoice</Anchor>, add your items, and click **Send Invoice**, PayU handles the delivery and payment page.
</Accordion>

***

3. #### How is an Invoice different from a Payment Link?

<Accordion title="Answer" icon="fab fa-adn">
  Both are ways to request payment from a customer, but they serve different needs:<br />

  | What is the Difference | Invoice                                                        | Payment Link                                |
  | ---------------------- | -------------------------------------------------------------- | ------------------------------------------- |
  | **Structure**          | Formal document with line items, GST, invoice number, due date | Simple payment request with a single amount |
  | **GST**                | Built-in GST calculation with HSN/SAC codes                    | Not applicable                              |
  | **Multiple items**     | Yes. Add as many line items as needed                          | No. Single amount only                      |
  | **Best for**           | Service businesses, freelancers, B2B billing                   | One-off or quick payment requests           |

  <br />

  Both use PayU's secure payment page and support the same payment methods.
</Accordion>

***

4. #### Which payment methods can my customer use?

<Accordion title="Answer" icon="fab fa-adn">
  Customers can pay using any method enabled on your merchant account such as credit and debit cards (Visa, Mastercard, RuPay, Amex), UPI, Net Banking, Wallets, EMI, and BNPL. Contact <Anchor target="_blank" href="https://help.payu.in/raise-ticket">PayU support</Anchor> to enable or disable specific methods.
</Accordion>

***

5. #### Are PayU Invoices secure?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. PayU Invoices are PCI DSS compliant. PayU uses encryption and tokenisation to protect customer payment data. No card or bank details are ever handled by your business.
</Accordion>

***

6. #### Does PayU send my customer a confirmation after they pay the invoice?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. After your customer completes the payment, PayU sends them an automatic payment confirmation by email and SMS. The confirmation includes the transaction amount, transaction ID, and a summary of what was paid.<br />

  You will also see the invoice status update to **Paid** in your Dashboard immediately. The payment appears in the **Transactions** tab as well.
</Accordion>

***

## Creating and Configuring Invoices

1. #### Can I add multiple products or services to a single invoice?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. You can add as many line items as needed to a single invoice. Each item has its own name, rate, quantity, and tax settings. The invoice calculates the subtotal, GST, and total automatically.
</Accordion>

***

2. #### Do I need to set up my items before creating an invoice?

<Accordion title="Answer" icon="fab fa-adn">
  No. You can create a new item directly from the **Enter Item Name** field while <Anchor target="_blank" href="https://docs.payu.in/docs/create-an-invoice-1">creating an invoice</Anchor>. You can reuse the same items with rates and tax details already filled in across all future invoices.
</Accordion>

***

3. #### How do I set up GST on an invoice?

<Accordion title="Answer" icon="fab fa-adn">
  GST on an invoice requires two things:<br />

  1. **Enable GST** in the **Settings** panel when <Anchor target="_blank" href="https://docs.payu.in/docs/create-an-invoice-1">creating the invoice</Anchor>.
  2. **Add tax details to each item** in the Item Catalog — GST rate, inter-state tax (IGST) or intra-state tax (CGST + SGST), cess, and HSN/SAC code.<br />

  When both are set, the invoice calculates and shows the GST breakdown automatically.
</Accordion>

***

4. #### Can I let my customer pay in installments?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. When <Anchor target="_blank" href="https://docs.payu.in/docs/create-an-invoice-1">creating the invoice</Anchor>, switch on **Enable Partial Payments** in the **Settings** panel. Your customer can then choose how much to pay when they open the invoice. The outstanding balance is tracked in the Dashboard. The invoice updates to **Paid** only when the full amount is received.
</Accordion>

***

5. #### Can I edit an invoice after I send it?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. You can only change the due date, add notes and terms and conditions. If you need to correct anything other than these details such as the amount, line items, due date, or customer details, <Anchor target="_blank" href="https://docs.payu.in/docs/manage-invoices#deactivate-an-invoice">deactivate</Anchor> the original invoice and <Anchor target="_blank" href="https://docs.payu.in/docs/create-an-invoice-1">create a new</Anchor> one with the correct information.
</Accordion>

***

6. #### Can I save an invoice and send it later?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. When <Anchor target="_blank" href="https://docs.payu.in/docs/create-an-invoice-1">creating an invoice</Anchor>, click **Save** instead of **Send Invoice**. The invoice is saved as a **Draft** and will not be sent to the customer. You can open it from the Invoices list at any time and click **Send Invoice** when you are ready.
</Accordion>

***

7. #### Can I create an invoice for a payment I have already collected?

<Accordion title="Answer" icon="fab fa-adn">
  PayU Invoices are designed to request payment. The invoice includes a pay-now button that your customer clicks to complete the transaction. They are not intended for documenting payments that have already been collected by other means (for example, cash or bank transfer).<br />

  If a customer has already paid you, the invoice would still show as **Sent** / unpaid after you create and send it. There is no way to manually mark an invoice as paid from the Dashboard without the customer completing payment through the invoice link.
</Accordion>

***

8. #### Can I use PayU Invoices alongside my existing PayU payment gateway setup? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  Yes. PayU Invoices is a separate module in the Dashboard and works independently of your payment gateway or checkout integration. You can use both at the same time — for example, using a hosted or merchant checkout on your website while also sending invoices to specific customers for custom orders or services.

  The same merchant account and settlement bank account are used for both, so all payments appear together in your **Transactions** tab.
</Accordion>

***

## Sending and Notifications

1. #### How does my customer receive the invoice?

<Accordion title="Answer" icon="fab fa-adn">
  PayU sends the invoice to your customer by **email** and/or **SMS**, depending on the contact details you entered in the **Billed To** field. The message includes a link to view the full invoice and a pay-now button. Your customer does not need a PayU account to pay.
</Accordion>

***

2. #### Can I resend an invoice if my customer did not receive it?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. Open the invoice from the Invoices list in the Dashboard and click **Resend**. The invoice is sent again to the same email address and mobile number. Also ask your customer to check their spam or junk folder — invoice emails can sometimes be filtered.
</Accordion>

***

3. #### Can I send the same invoice to multiple customers?

<Accordion title="Answer" icon="fab fa-adn">
  No. Each invoice is created for a single customer in the **Billed To** field. To bill multiple customers for the same service, create a separate invoice for each one. If you need to bill many customers at once, consider using <Anchor target="_blank" href="doc:payment-links-overview">Payment Links</Anchor> with bulk upload instead.
</Accordion>

***

4. #### How will I know when my customer has paid?

<Accordion title="Answer" icon="fab fa-adn">
  The invoice status in your Dashboard updates to **Paid** immediately after the customer completes payment. The payment also appears in the **Transactions** tab. For instant server-side notifications, set up a webhook under **Settings → Webhooks** — PayU will send a `payment.success` event each time a payment is received.
</Accordion>

***

5. #### What webhook events does PayU send for invoices? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  PayU sends three dedicated webhook events for invoices:

  | Event                    | When it fires                                     |
  | ------------------------ | ------------------------------------------------- |
  | `INVOICE_PAID_HTTP_V2`   | Payment received — the invoice is fully paid      |
  | `INVOICE_FAILED_HTTP_V2` | A payment attempt on the invoice failed           |
  | `INVOICE_DUE_HTTP`       | Invoice is approaching or has passed its due date |

  To receive these events, set up a webhook endpoint under **Settings → Webhooks** in the PayU Dashboard and subscribe to the invoice events. Your endpoint will receive a POST request with the invoice and payment details whenever one of these events occurs.

  <Callout icon="📘" theme="info">
    If you only need to track payment status in the Dashboard and do not have a server to receive webhooks, you do not need to set this up. Your Dashboard always shows the latest invoice status.
  </Callout>
</Accordion>

***

## Payments and Reconciliation

1. #### What happens if my customer does not pay by the due date?

<Accordion title="Answer" icon="fab fa-adn">
  The invoice status changes to **Overdue** after the due date passes without payment. The customer can still open the invoice link and pay — the due date is informational. If you want to stop accepting payment on an overdue invoice, cancel it from the Dashboard.
</Accordion>

***

2. #### Can I issue a refund for an invoice payment?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. Find the transaction in the **Transactions** tab of your Dashboard and start a refund from there. The refund process is the same regardless of how the payment was collected.

  → [Refunds](doc:introduction-refunds)
</Accordion>

***

3. #### Can I download invoice records for my accounts?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. From the Invoices list, click **Download** and choose a format:

  - **CSV** or **XLSX** — Invoice records (invoice number, customer, amount, status, due date)
  - **TXNS-CSV** or **TXNS-XLSX** — Transaction records (individual payment details)

  You can also share the downloaded report to one or more email addresses directly from the export pop-up.

  → [Manage Invoices](doc:manage-invoices)
</Accordion>

***

4. #### Can I use Invoices for recurring or subscription billing?

<Accordion title="Answer" icon="fab fa-adn">
  No. PayU Invoices are for one-time billing. Each invoice represents a single payment request. You can create new invoices each billing cycle — for example, a monthly consulting invoice — but each invoice is a separate, independent payment.

  If you need to charge customers automatically on a recurring schedule, use PayU's <Anchor target="_blank" href="doc:recurring-payments">Recurring Payments</Anchor> product instead.
</Accordion>

***

5. #### How do I download or save a copy of a single invoice? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  To export all your invoice records or transaction records in bulk, use the **Download** button at the top of the Invoices list and choose CSV, XLSX, TXNS-CSV, or TXNS-XLSX.

  For a single specific invoice, open it from the Invoices list — you can then print or save it as a PDF from your browser using **Print → Save as PDF**.

  → [Manage Invoices](doc:manage-invoices)
</Accordion>

***

## APIs

1. #### Are there APIs for managing invoices programmatically? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  Yes. PayU Invoices use the same OAuth2-authenticated API as Payment Links, so you can create, fetch, update, and cancel invoices without using the Dashboard at all.

  The key endpoints are:

  | Action                      | API                                                     |
  | --------------------------- | ------------------------------------------------------- |
  | Create and share an invoice | [Create & Share Payment Link API](doc:api-create-share) |
  | Fetch invoice details       | [Fetch Payment Link API](doc:api-fetch)                 |
  | Cancel an invoice           | [Cancel Payment Link API](doc:api-cancel-status)        |
  | Get invoice transactions    | [Fetch Transactions API](doc:api-transactions)          |

  Authenticate using an OAuth2 access token with the `create_payment_links`, `read_payment_links`, and `update_payment_links` scopes. The `invoiceNumber` in the Dashboard corresponds directly to the `id` field in the API.

  → [Invoice API Reference](doc:invoice-api-reference)
</Accordion>

***

## Next Steps

<Cards>
  <Card title="Create an Invoice" href="doc:create-an-invoice" icon="far fa-file-invoice">
    Step-by-step guide to creating and sending your first invoice.
  </Card>

  <Card title="Manage Invoice Items" href="doc:manage-invoice-items" icon="fa-box-open">
    Build your product and service catalog with rates and GST details.
  </Card>

  <Card title="Manage Invoices" href="doc:manage-invoices" icon="fa-list-check">
    View, filter, resend, cancel, and download your invoice records.
  </Card>

  <Card title="Invoice Troubleshooting" href="doc:invoice-troubleshooting" icon="fa-wrench">
    Fix issues with invoices not being received or payments not going through.
  </Card>

  <Card title="Payment Links" href="doc:payment-links-overview" icon="fa-link">
    Need a simpler payment request without line items? Use Payment Links.
  </Card>
</Cards>
