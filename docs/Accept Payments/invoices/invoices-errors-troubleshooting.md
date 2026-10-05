---
title: Errors and Troubleshooting
excerpt: >-
  Fix common PayU Invoice problems — invoice not received by customer, payment
  page not loading, GST not calculating, payment not reflecting, and more.
deprecated: false
hidden: true
metadata:
  title: Invoice Troubleshooting | PayU Developer Docs
  description: >-
    Fix PayU Invoice issues — invoice not received, payment failing, GST not
    calculating, invoice status not updating, and wrong invoice details.
  keywords:
    - payu invoice not received
    - payu invoice payment not working
    - payu invoice gst not calculating
    - payu invoice troubleshooting
    - invoice status not updating payu
    - payu invoice overdue
    - payu invoice error
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
---
Something not working after creating and sending your <Anchor target="_blank" href="https://docs.payu.in/docs/invoices">Invoice</Anchor>? Go through the most common issues — invoice not reaching the customer, payment page not loading, GST not appearing, and status not updating after payment.

<Callout icon="📘" theme="info">
  ### **Invoices**

  Haven't created an invoice yet? → <Anchor target="_blank" href="https://docs.payu.in/docs/create-an-invoice-1">Create an Invoice</Anchor>
</Callout>

***

## Why Did My Customer Not Receive the Invoice?

<Accordion title="Invoice Not Arriving by Email or SMS" icon="far fa-envelope-open">
  Check these in order:

  1. **Confirm the customer's contact details are correct:&#x20;**&#x4F;pen the invoice in your Dashboard and check the email address and mobile number under **Billed To**. A single typo will prevent delivery. If the details are wrong, <Anchor target="_blank" href="https://docs.payu.in/docs/manage-invoices#deactivate-an-invoice">deactivate</Anchor> the invoice, <Anchor target="_blank" href="https://docs.payu.in/docs/create-an-invoice-1">create a new</Anchor> one with the correct contact, and resend.

  2. **Ask the customer to check their spam or junk folder:&#x20;**&#x49;nvoice emails can sometimes be filtered by email providers, especially for first-time senders. Ask your customer to mark PayU as a trusted sender.

  3. **Resend the invoice:&#x20;**&#x46;rom the Dashboard, open the invoice and click <Anchor target="_blank" href="https://docs.payu.in/docs/manage-invoices#resend-an-invoice">**Resend**</Anchor> to send it again.

  4. **Check the invoice status in your Dashboard:** If the status shows **Draft**, the invoice was saved but never sent. Click **Send Invoice** to send it now.
</Accordion>

***

## Why Is the Payment Page Not Opening?

<Accordion title="Customer Clicks Pay but Nothing Loads" icon="far fa-rectangle-xmark">
  Ask your customer to try the following:

  1. **Check the internet connection:&#x20;**&#x41; poor connection can prevent PayU's payment page from loading.

  2. **Try a different browser:&#x20;**&#x53;ome older browsers or those with strict security settings may block the payment page. Ask them to try Chrome, Firefox, or Safari with extensions turned off.

  3. **Check if the invoice link has expired:&#x20;**&#x49;f the invoice is past its due date, the pay button may no longer be active. Check the invoice status in your Dashboard. If it shows **Overdue**, contact <Anchor target="_blank" href="https://help.payu.in/raise-ticket">PayU support</Anchor> to check if payment can still be accepted.

  4. **Check if the invoice was deactivated:&#x20;**&#x41; **Deactivated** invoice cannot be paid. You can <Anchor target="_blank" href="https://docs.payu.in/docs/manage-invoices#reactivate-an-invoice">reactivate</Anchor> the same invoice to accept payments.
</Accordion>

***

## Why Is the Payment Not Going Through?

<Accordion title="Customer Reaches the Payment Page but Payment Fails" icon="far fa-circle-xmark">
  Ask your customer what message they saw and which payment method they tried.

  | Message the Customer Saw       | Likely Reason                                      | What to Do                                                                                           |
  | ------------------------------ | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
  | "Transaction declined by bank" | Their bank or card issuer declined the payment     | Ask them to try a different card or contact their bank                                               |
  | "Payment method not available" | That method is not turned on for your account      | Contact <Anchor target="_blank" href="https://help.payu.in/query">PayU support</Anchor> to enable it |
  | Page stuck or keeps loading    | Poor internet connection on the customer's side    | Ask them to try on a better connection or different browser                                          |
  | "Amount exceeds limit"         | The customer's card or UPI daily limit was reached | Ask them to try a different payment method                                                           |

  **If no payment methods appear at all on the payment page:** contact <Anchor target="_blank" href="https://help.payu.in/query">PayU support</Anchor> — your account may need specific payment methods turned on.
</Accordion>

***

## Why Is GST Not Showing on the Invoice?

<Accordion title="GST Amount Is Zero or Not Appearing" icon="far fa-receipt">
  Check the following:

  1. **Make sure GST was enabled when creating the invoice.** GST is not turned on by default — you must switch on **Enable GST** in the **Settings** panel when creating the invoice. Since invoices cannot be edited after sending, if GST was not enabled, cancel the invoice and create a new one with GST turned on.

  2. **Check that tax details are set for each item in the catalog.** GST is calculated from the tax details on each item — GST rate, inter-state or intra-state rate, and cess. If these are blank for an item, no GST will appear for that line. → [Manage Invoice Items](doc:manage-invoice-items)

  3. **Check whether the rate was set as tax inclusive.** If the item's rate was set to **Tax Inclusive**, GST is already included in the rate and will not be shown as a separate addition. Change it to **Tax Exclusive** if you want GST shown separately on top of the rate.
</Accordion>

***

## Why Is the Invoice Still Showing as Unpaid After Payment?

<Accordion title="Payment Was Made but Status Has Not Updated" icon="far fa-clock">
  Follow these steps:

  1. **Wait 5–10 minutes and refresh.** The Dashboard updates in near-real-time but can occasionally take a few minutes after a payment.

  2. **Check the Transactions tab.** Payments received through invoices appear in the main **Transactions** section of your Dashboard. Search by amount or date to confirm the payment was received.

  3. **If partial payments are enabled**, the invoice may still show as **Sent** if the customer paid only a portion of the total. The invoice updates to **Paid** only when the full amount is received.

  If the status does not update after 30 minutes and the payment appears confirmed in the customer's bank account, contact <Anchor target="_blank" href="https://help.payu.in/query">PayU support</Anchor> with the invoice number and the customer's bank reference number.
</Accordion>

***

## How Do I Fix Wrong Details on a Sent Invoice?

<Accordion title="Wrong Amount, Item, Due Date, or Customer on the Invoice" icon="far fa-pen-to-square">
  Invoices cannot be changed after they are sent.

  **What to do:** Cancel the incorrect invoice from the Dashboard, then create a new invoice with the correct details and send it to your customer. Let your customer know the original invoice has been cancelled and to use the new one for payment.

  <Callout icon="📘" theme="info">
    If the customer has already paid the incorrect invoice, issue a refund for the overpaid or wrong amount and send a corrected invoice for the right amount. → [Refunds](doc:introduction-refunds)
  </Callout>
</Accordion>

***

## Still Stuck?

Contact PayU support with these details:

* [x] Invoice number (from your Dashboard)
* [x] Customer name and contact details (email or mobile)
* [x] Transaction ID (if your customer attempted a payment)
* [x] Date and time of the issue
* [x] Screenshot of any error message
* [x] The invoice status currently showing in your Dashboard

Contact PayU Support via the Dashboard **Help** section, or email `support@payu.in`.

***

## Next Steps

<Cards>
  <Card title="Create an Invoice" href="doc:create-an-invoice" icon="far fa-file-invoice">
    Create a new invoice and send it to your customer.
  </Card>

  <Card title="Manage Invoices" href="doc:manage-invoices" icon="fa-list-check">
    View, resend, cancel, and download your invoice records.
  </Card>

  <Card title="Invoice FAQs" href="doc:invoice-faqs" icon="fa-circle-question">
    Common questions about PayU Invoices.
  </Card>
</Cards>
