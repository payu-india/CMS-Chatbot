---
title: Customer Journey - WhatsApp Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
### Payment Experience with UPI Intent URL​

In a live integration, your backend creates the **UPI Intent** via PayU and sends `POST /messages` with `type: order_details` and `payment_type: "upi"` (per your programme spec).

<Accordion title="Step 1: Choose payment path and receive the order card" icon="fa-comments">
  In the chat, the business asks how the customer wants to pay (for example **Pay with UPI** vs **Other payment option**). After the customer selects **Pay with UPI**, the business sends an **order-style message**: order reference, line item (for example **Electricity bill**), amount, short narrative, and actions such as **Review and pay** and **Pay now**.

</Accordion>

<Accordion title="Step 2: Review native order details (pending)" icon="fa-file-invoice">
  The customer opens the **Order details** view: merchant branding, **ORDER** reference, **Order pending** state, line items and pricing (including any discount), **Total**, and **Continue** to move toward payment.

</Accordion>

<Accordion title="Step 3: Choose UPI payment method" icon="fa-list">
  The **Choose payment method** sheet lists **Pay on WhatsApp** (linked bank as **Default**), options to **Add payment method** or **View account balance**, and **Pay on other UPI app** (for example **Google Pay**, **PhonePe**, **More UPI apps**). The customer selects an option and taps **Continue** (**POWERED BY UPI**).

</Accordion>

<Accordion title="Step 4: In-chat payment confirmation" icon="fa-circle-check">
  In the thread, the customer sees the **order summary** alongside a **completed payment** bubble (amount, **Sent to** the business, **Completed** with read receipts). This corresponds to a successful **UPI** authorisation after the customer confirms on their bank or TPAP flow.

</Accordion>

<Accordion title="Step 5: Receipt and order complete" icon="fa-receipt">
  The business sends a closing message: **Order complete**, paid line item, and a **receipt** (or reference) number for the customer’s records. Your systems should already have received the **PayU PG webhook** for reconciliation.

</Accordion>


<Image src="https://files.readme.io/fa4790a59dc7d1a9722c2970ee10a68d5ad6eb1b1cdb7fdb558a05ac51b43e97-payment-experience-upi-url.gif" align="left" width="350px" border={true} wrap={true} />


