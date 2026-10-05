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

PayU Invoices let you create and send professional billing documents to your customers including GST calculations built in, line items for each product or service, and a pay-now button included.<br />

You can use Invoices to:<br />

* Create itemized invoices with multiple products or services
* Add GST automatically including inter-state and intra-state tax, cess, and HSN/SAC codes
* Set a due date so customers know when payment is expected
* Enable partial payments so customers can pay in installments
* Send invoices directly to customers by email or SMS from the Dashboard
* Track which invoices are paid, pending, or overdue in one place
* Download invoice and transaction records as CSV or Excel

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
  <button onclick="window.open('https://docs.payu.in/docs/create-an-invoice', '_blank')"
          class="inv-btn"
          data-tooltip="Click to see steps to create your first invoice.">
    Create your first invoice →
  </button>
`}</HTMLBlock>

***

## Is Invoicing Right for Me?

An Invoice is a good choice if you:<br />

* **Bill customers for services or multiple products** and need an itemized breakdown.
* **Need GST-compliant invoices** for your business records or to share with customers.
* **Want to send formal payment requests** with your invoice number, due date, and line items.
* **Run a service business** such as consulting, freelancing, events, logistics, or any work-based billing.<br />

Consider another PayU solution if you:<br />

* Need a simple payment request without line items → <Anchor target="_blank" href="https://docs.payu.in/docs/payment-links">**Payment Links**</Anchor>
* Want a buy or donate button on your website → <Anchor target="_blank" href="https://docs.payu.in/docs/payment-button">**Payment Buttons**</Anchor>
* Want customers to pay on your website → PayU Hosted Checkout
* You need a fully custom checkout experience → <Anchor target="_blank" href="doc:merchant-hosted-checkout">**Merchant Hosted Checkout**</Anchor>

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution Is Right For You?**

  Tell us what you want to achieve and how you plan to accept payments. We will recommend the best PayU solution for your needs.

  <Anchor target="_blank" href="doc:start-here">Find the right solution</Anchor> →
</Callout>

***

## What Will I Need?

You don't need a developer or any coding experience to get started.

You'll need:

<Columns layout="fixed">
  <Column>
    **A PayU merchant account:** <Anchor target="_blank" href="doc:set-up-your-account">Sign up here</Anchor> if you do not have one.
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

<Accordion title="1. Set up your item catalog" icon="far fa-box-open">
  Before creating your first invoice, add the products or services you bill for to the **Items** catalog. You only need to do this once — items are reusable across all future invoices.

  Go to **Payment Tools → Invoices → Items** and click **New Item**.
</Accordion>

<Accordion title="2. Create the invoice" icon="far fa-file-invoice">
  Go to **Payment Tools → Invoices** and click **Create New Invoice**. Enter the invoice number, due date, invoice title, and select the customer. Add your line items, enable GST if needed, and enable partial payments if you want to let the customer pay in installments.
</Accordion>

<Accordion title="3. Send it to your customer" icon="far fa-paper-plane">
  Click **Send Invoice**. PayU sends the invoice to your customer by email or SMS. The invoice includes a pay-now button linked to PayU's secure checkout page.
</Accordion>

<Columns layout="fixed">
  <Column>
    **Need detailed steps?** See [Create an Invoice →](doc:create-an-invoice)
  </Column>
</Columns>

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
  They can pay by UPI, card, net banking, wallet, and more — whatever payment methods are turned on for your account.
</Accordion>

<Accordion title="4. Pays and receives confirmation" icon="far fa-circle-check">
  The customer completes the payment and receives a confirmation. The invoice status in your Dashboard updates to **Paid** immediately.
</Accordion>

Your customer does not need a PayU account — they can pay from any browser or mobile device.

***

## How Do I Manage My Invoices?

Once invoices are sent:

<Columns layout="fixed">
  <Column>
    **Track all invoices in one place** — Paid, Sent, Overdue, or Draft — from **Payment Tools → Invoices** in your Dashboard.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Search and filter** by invoice number, title, status, or date range to find any invoice quickly.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Download records** — export invoice data or transaction data in CSV or Excel format for your accounts.
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

  <Card title="Payment Links" href="doc:payment-links-overview" icon="fa-link">
    Need a simpler payment request without line items? Use Payment Links.
  </Card>
</Cards>
