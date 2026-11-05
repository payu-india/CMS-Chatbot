---
title: Invoices
excerpt: >-
  Create GST-compliant invoices, send them to customers, and collect payment
  through PayU — all from the Dashboard. No developer needed.
deprecated: false
hidden: true
metadata:
  title: PayU Invoices — Overview | Developer Docs
  description: >-
    Create GST-compliant invoices, send them to customers, and collect payment
    through PayU. No developer or technical setup needed.
  keywords:
    - payu invoices
    - payu gst invoice
    - create invoice payu dashboard
    - payu no-code invoice
    - send invoice to customer payu
    - payu invoice payment
    - payu invoice vs payment link
  robots: index
next:
  description: Explore related information and resources.
---
<Banner
  isInline={true}
  message="Integration effort: No code or website developer required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

## How Does Invoices Simplify My Business?

<Accordion title="Professional GST-compliant invoices in minutes">
  Create an itemised invoice with your business name, customer details, line items, and applicable GST from the Dashboard. PayU calculates CGST, SGST, IGST, and cess automatically based on the GST rate and state you set. No accounting software or spreadsheet needed.
</Accordion>

<Accordion title="Customers pay the moment they receive the invoice">
  Every invoice includes a pay-now button linked to PayU's secure checkout page. Your customer receives the invoice by email or SMS, clicks the button, and pays using UPI, card, or any other enabled payment method.
</Accordion>

<Accordion title="Set a due date">
  Add a due date to every invoice so your customer sees exactly when payment is expected. Overdue invoices are flagged automatically in your Dashboard, so you can follow up without manually tracking them.
</Accordion>

<Accordion title="Collect a deposit, settle the balance later">
  Enable partial payments on any invoice. Your customer can pay a portion upfront and return to pay the balance when they are ready. You set the minimum first payment — keeping the billing process on your terms.
</Accordion>

<Accordion title="Items catalog: add once, reuse forever">
  Build a catalog of your products and services with name, rate, unit, and GST details. When creating an invoice, select items from the catalog instead of re-entering details every time. Changes to an item in the catalog apply to all future invoices automatically.
</Accordion>

<HTMLBlock>{`
  <style>
  .inv-btn {
    position: relative;
    background-color: #00A550;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
  }
  .inv-btn:hover::after {
    content: attr(data-tooltip);
    position: absolute;
    bottom: 125%;
    left: 50%;
    transform: translateX(-50%);
    background-color: #333;
    color: white;
    padding: 5px 10px;
    border-radius: 4px;
    white-space: nowrap;
    font-size: 12px;
    z-index: 1;
  }
  </style>
  <button onclick="window.open('https://docs.payu.in/docs/create-an-invoice-1', '_blank')"
          class="inv-btn"
          data-tooltip="Click to see steps to create your first invoice.">
    Create your first invoice →
  </button>
`}</HTMLBlock>

***

## Is Invoicing Right for Me?

| I want to…                                                           |                                            Works?                                            |
| -------------------------------------------------------------------- | :------------------------------------------------------------------------------------------: |
| Send a formal itemized invoice to a client or customer               |                                               ✅                                              |
| Include GST automatically with the correct CGST, SGST, or IGST split |                                               ✅                                              |
| Set a due date and let customers pay directly from the invoice       |                                               ✅                                              |
| Collect a partial payment and let the customer pay the balance later |                                               ✅                                              |
| Track which invoices are paid, pending, or overdue                   |                                               ✅                                              |
| Send a simple payment request without line items                     |           ⚠️ Use [Payment Links](https://docs.payu.in/docs/payment-links-overview)           |
| Add a pay button to my website                                       |          ⚠️ Use [Payment Buttons](https://docs.payu.in/docs/payment-button-overview)         |
| Collect payments from many customers at once                         |         ⚠️ Use [Bulk Payment Links](https://docs.payu.in/docs/payment-links-overview)        |
| Set up recurring auto-debit or subscriptions                         |           ⚠️ Use [Recurring Payments](https://docs.payu.in/docs/recurring-payments)          |
| Full custom checkout experience                                      | ⚠️ Use [Merchant Hosted Checkout](https://docs.payu.in/docs/custom-checkout-merchant-hosted) |

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution Is Right For You?**

  Tell us what you want to achieve and how you plan to accept payments. We will recommend the best PayU solution for your needs.

  <Anchor target="_blank" href="https://docs.payu.in/docs/start-here#find-the-right-product-for-you">Find the Right Product for You</Anchor> →
</Callout>

***

## Common Use Cases

<Cards>
  <Card title="Freelance Services" icon="fa-laptop-code">
    Add your services to the items catalog once — design, copywriting, development, strategy — and pull them into any invoice in seconds. Each line item carries its own GST rate, so the final tax amount is always calculated correctly. No spreadsheet, no manual tax lookup, no re-entering the same details invoice after invoice.
  </Card>

  <Card title="Consulting Agencies" icon="fa-building">
    Bill corporate clients with the detail their finance teams require: your GSTIN, their GSTIN, invoice number, due date, and every deliverable as a separate line item. The invoice lands in their inbox with a pay-now button. When they pay, your Dashboard updates instantly — the status moves from **Sent** to **Paid** without any manual reconciliation.
  </Card>

  <Card title="SMEs and Traders" icon="fa-boxes-stacked">
    Raise invoices for goods with HSN codes assigned per line item. PayU automatically splits the tax into CGST and SGST for intra-state sales, or IGST for inter-state — based on the states your and your customer's GSTINs are registered in. Every invoice is GST-compliant and downloadable the moment it is created.
  </Card>

  <Card title="Training Institutes" icon="fa-graduation-cap">
    Send a course or batch fee invoice with a due date and partial payment enabled. Set the minimum first payment — say, 40% at enrollment — and let students settle the balance by the due date. Each payment updates the invoice status in real time, so your accounts team always knows exactly what has been collected and what is outstanding.
  </Card>

  <Card title="CAs and Tax Professionals" icon="fa-calculator">
    Issue invoices for audit, filing, or retainer services with your firm's GSTIN and the client's GSTIN on record. The client downloads the invoice as a PDF for their books. You export all invoice data as CSV at month-end for your own accounting — no double entry, no data re-keying.
  </Card>
</Cards>

***

## What All I Need to Get Started?

You don't need a developer or any coding experience to get started.<br />

You'll need:<br />

<Columns layout="fixed">
  <Column>
    **A PayU merchant account:** <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signup">Sign up here</Anchor> if you do not have one.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Your customer's contact details:** Name and email address or mobile number to send the invoice to.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Your item or service details:** Name, rate, and any applicable tax details (GST rate, HSN/SAC code).
  </Column>
</Columns>

***

## How Do I Create and Send an Invoice?

Here is how it works:

<Accordion title="1. Create the invoice" icon="far fa-file-invoice">
  Go to **Payment Tools → Invoices** and click **Create New Invoice**. Enter the invoice number, due date, invoice title, and select the customer. Add your line items, enable GST if needed, and enable partial payments if you want to let the customer pay in installments.
</Accordion>

<Accordion title="2. Send it to your customer" icon="far fa-paper-plane">
  Click **Send Invoice**. PayU sends the invoice to your customer by email or SMS. The invoice includes a pay-now button linked to PayU's secure checkout page.
</Accordion>

<Columns layout="fixed">
  <Column>
    **Need detailed steps?** See [Create an Invoice →](doc:create-an-invoice)
  </Column>
</Columns>

***

## Is My Invoice Secure?

Yes. When a customer clicks the pay-now button in the invoice, they are taken to PayU's PCI-DSS compliant hosted payment page. Your customer's card and UPI details are entered directly on PayU's infrastructure. Your system never receives or processes sensitive payment data. You do not need to configure anything for this.<br />

You control payment exposure through two settings available at invoice creation:<br />

* **Due date**: the invoice stops accepting payments after the date you set.
* **Partial payment minimum**: if partial payments are enabled, you set the minimum first payment amount, preventing under-payments.

<Cards>
  <Card title="For Developers" icon="fad fa-key">
    Invoices use the same OAuth2 API as Payment Links. The `invoiceNumber` field in the Dashboard maps to `id` in the API. Webhook events for invoices are `INVOICE_PAID_HTTP_V2`, `INVOICE_FAILED_HTTP_V2`, and `INVOICE_DUE_HTTP`.&#x20;
  </Card>
</Cards>

***

## How Does My Customer Pay?

When your customer receives the invoice:

<Accordion title="1. Receives the invoice" icon="far fa-envelope">
  Your customer gets the invoice by email or SMS. It shows the invoice number, due date, itemized breakdown, GST amount, and total.
</Accordion>

<Accordion title="2. Clicks to pay" icon="far fa-computer-mouse">
  They click the pay button in the invoice. PayU's payment page opens with the total amount pre-filled.
</Accordion>

<Accordion title="3. Chooses a payment method" icon="far fa-credit-card">
  They can pay by UPI, card, net banking, wallet, and more, whatever payment methods are turned on for your account.
</Accordion>

<Accordion title="4. Pays and receives confirmation" icon="far fa-circle-check">
  The customer completes the payment and receives a confirmation. The invoice status in your Dashboard updates to **Paid** immediately.
</Accordion>

<Callout icon="📘" theme="success">
  ### **Tips:**

  Your customer does not need a PayU account. They can pay from any browser or mobile device.
</Callout>

***

## How Do I Manage My Invoices?

Once invoices are sent:

<Columns layout="fixed">
  <Column>
    **Track all invoices such as Paid**, **Sent**, **Overdue**, or **Draft in one place** from **Payment Tools → Invoices** in your Dashboard.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Search and filter** by invoice number, title, status, or date range to find any invoice quickly.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Download records**. Export invoice data or transaction data in CSV or Excel format for your accounts.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Cancel an invoice** at any time if it was sent by mistake or is no longer needed.
  </Column>
</Columns>

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
    View, filter, track, and download your invoice records.
  </Card>

  <Card title="Invoice FAQs" href="doc:invoice-faqs" icon="fa-circle-question">
    Common questions about PayU Invoices.
  </Card>
</Cards>