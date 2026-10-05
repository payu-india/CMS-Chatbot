---
title: Create an Invoice
excerpt: >-
  Create a GST-compliant invoice in the PayU Dashboard, add your line items, and
  send it to your customer — all in a few minutes. No developer needed.
deprecated: false
hidden: true
metadata:
  title: Create a PayU Invoice | Developer Docs
  description: >-
    Create a GST-compliant invoice in the PayU Dashboard. Add line items, set a
    due date, enable GST, and send to your customer via email or SMS.
  keywords:
    - create invoice payu
    - payu gst invoice
    - payu dashboard invoice
    - send invoice to customer payu
    - payu invoice line items
    - payu invoice due date
    - payu invoice partial payment
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: invoices
      title: Invoices
      type: basic
---
<Banner
  isInline={true}
  message="Integration effort: No code or website developer required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

Create a professional, GST-compliant invoice in the PayU Dashboard and send it directly to your customer. No developer needed.

***

## What All I Need?

<Cards>
  <Card title="A PayU Merchant Account" icon="far fa-table-cells-column-unlock">
    <Columns layout="fixed">
      <Column>
        <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signup">Set up your account</Anchor> if you have not already done so.
      </Column>
    </Columns>
  </Card>

  <Card title="Your Customer's Contact Details" icon="far fa-address-card">
    Name and email address or mobile number to send the invoice to.
  </Card>

  <Card title="Your Item or Service Details" icon="far fa-box-open">
    Name, rate, and tax details (GST rate, HSN/SAC code) for the products or services on the invoice.
  </Card>
</Cards>

***

## How Do I Create an Invoice?

<Accordion title="1. Open Invoices on the Dashboard" icon="far fa-grid-2">
  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor>.
  2. Expand **Payment Tools** and click **Invoices** from the left navigation bar.

     <Image src="https://files.readme.io/cdfb8317ce8e544a7adea38a03005bbe88a9493bf443d9a122052ac918b37373-Screenshot_2026-10-05_at_10.07.25_AM.png" align="center" caption="Access Invoices" border={true} />


  All your existing invoices are listed here, showing their status, due date, and amount.
</Accordion>

<Accordion title="2. Start a new invoice" icon="far fa-plus">
  Click **Create New Invoice** at the top-right corner of the page.

  The **Create New Invoice** page opens.


  <Image src="https://files.readme.io/e4fb62f4da41f7913d72ed32ad292fa6b317d6ae078e01920c67cfdbe63bf542-Screenshot_2025-06-02_at_7.43.06_PM.png" align="center" caption="Create New Invoice" border={true} />


  Fill in the these invoice details:

  | Field             | What To Enter                                                                      |
  | ----------------- | ---------------------------------------------------------------------------------- |
  | **Invoice Title** | A short description of the invoice. For example, "Consulting Services — July 2025" |
  | **Invoice #**     | A unique invoice number for your records                                           |
  | **Issue Date**    | Filled automatically with today's date                                             |
  | **Due Date**      | Click the calendar and select when payment is due                                  |
</Accordion>

<Accordion title="3. Select the customer" icon="far fa-user">
  Click the **Billed To** drop-down and select the customer this invoice is for.

  <Callout icon="📘" theme="info">
    ### **Tips:**

    If the customer is not in the list yet, you can add them as a new customer from the drop-down. Enter these details of the customer:

    <Tabs>
      <Tab title="Basic Details">
        - **Customer Name**
        - **Email**
        - **Contact Number**
        - **GSTIN**

        ![](https://files.readme.io/b1fe174ebd8879834b28682b8c1cf15509cdd53ad526b8d6fe07f83fcf8bd64b-Screenshot_2026-10-05_at_10.21.21_AM.png)


      </Tab>

      <Tab title="Billing Address (optional)">
        - **Address line 1**
        - **Address line 2**
        - **PIN Code**
        - **City**
        - **State**
        - **Country**


        <Image src="https://files.readme.io/a4e68c9994e4b7d785548e45dc1f4362d1079136a4a0bc0fa7eb7043ee359e07-Screenshot_2026-10-05_at_10.22.26_AM.png" align="center" caption="Billing Address" border={true} />

      </Tab>

      <Tab title="Shipping Address (optional)">
        **Use same as Billing Address:&#x20;**&#x53;elect this checkbox if your shiping address is as same as billing address. If not you can provide the shipping address.


        <Image src="https://files.readme.io/f8da5af5d58d23013867e996844bb8c99c21b7fdf220573341a0f2d0f952d79b-Screenshot_2026-10-05_at_10.25.02_AM.png" align="center" caption="Shipping Address" border={true} />



      </Tab>

      <Tab title="New Tab">

      </Tab>
    </Tabs>
  </Callout>
</Accordion>

<Accordion title="4. Add line items" icon="far fa-list-check">
  1. Slect items from the **Enter Item Name** drop-down or click **Create New Item** to add the first product or service to the invoice.


  <Image src="https://files.readme.io/3daf144fb955f8a78881701fc5da7331a02f3d8a3ceba2320c1e99ef698c198d-Screenshot_2025-06-02_at_7.47.23_PM.png" border={true} />


  Enter these details in the **Add Item&#x20;**&#x70;op-up menu and click **Create Item**:

  <Tabs>
    <Tab title="Basic Details">
      - **Item Name**
      - **Rate:&#x20;**&#x54;he cost of the item.
      - **Item Description**

      ![](https://files.readme.io/320cffcee8032e83ed82b9eb10d7c56d0cfdbe97d26ab41484064587a498d6cf-Screenshot_2026-10-05_at_10.37.52_AM.png)

      <br />

      &#x20;
    </Tab>

    <Tab title="Tax Details (optional)">
      These are optional. You can add them later.

      - **Inter State Tax**
      - **Intra State Tax**
      - **Cess**
      - **Tax Inclusive/Tax Exclusive**
      - **HSN/SAC Code**

        ![](https://files.readme.io/d5259d5575d3ed2467c1afd6380ce2dd20f20643a72286fc2091fc2563a7d812-Screenshot_2026-10-05_at_10.41.36_AM.png)


    </Tab>

    <Tab title="New Tab">

    </Tab>
  </Tabs>

  2. The item's rate is filled in automatically. You can adjust the quantity if needed. The total **Amount** updates automatically.

     <Image src="https://files.readme.io/2371fd7b8f51d252e05f5f9ffe3feff781f3a2e91f1383dd90117b384b9f582d-Screenshot_2026-10-05_at_10.46.29_AM.png" align="center" caption="Line Items" border={true} />

  3. Click **Add Item** again to add more items. You can add as many line items as required.
</Accordion>

<Accordion title="5. Configure settings (optional)" icon="far fa-sliders">
  On the **Settings** panel on the right side of the page, you can turn on:

  | Setting                     | What it does                                                                                                                                                                                                            |
  | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | **Enable GST**              | Calculates and adds GST to each line item automatically, based on the tax details set in the item catalog. Upon clicking, you should add the **GSTIN&#x20;**&#x69;n the **Add your GST Details&#x20;**&#x70;op-up menu. |
  | **Enable Partial Payments** | Lets your customer choose to pay a part of the invoice now and the rest later                                                                                                                                           |

  ![](https://files.readme.io/a199c3d9b2a663928af6078b565a8401adfa9dc7da3ddfdbacf3592c54d26a30-Screenshot_2026-10-05_at_10.49.40_AM.png)

  <Callout icon="📘" theme="info">
    ### **Tips:**

    GST details — rate, HSN/SAC code, inter-state or intra-state tax, and cess — are set at the item level in the Item Catalog.
  </Callout>
</Accordion>

<Accordion title="6. Send the invoice" icon="far fa-paper-plane">
  When the invoice is ready, click **Send Invoice**.

  PayU sends the invoice to your customer by email or SMS. The message includes a link to view the invoice and a pay-now button.

  <Callout icon="📘" theme="info">
    You can also **Save** the invoice as a draft to send later, or **Cancel** to discard it. These options are in the top-right corner of the page.
  </Callout>
</Accordion>

***

## What Happens After My Customer Pays?

After your customer receives the invoice and completes a payment:

1. The invoice status in your Dashboard updates to **Paid** immediately.
2. The payment appears in the **Transactions** tab in your PayU Dashboard.
3. If partial payments are enabled, the invoice shows how much has been paid and how much is still outstanding.
4. The money is settled to your bank account on the standard settlement cycle.

<Callout icon="📘" theme="info">
  ### **Want to be notified the moment a payment comes in?**

  Set up webhooks under **Settings → Webhooks** in the Dashboard. Webhooks are optional — your Dashboard always shows you the latest payment and invoice status whether or not you set them up.
</Callout>

***

## What Do I Do If Something Goes Wrong?

| Problem                                                  | Fix                                                                                                                                  |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Customer says they did not receive the invoice           | Resend it from the Dashboard — find the invoice, open it, and click **Resend**. Also ask the customer to check their spam folder.    |
| Wrong item, amount, or due date on the invoice           | Invoices cannot be edited after they are sent. Cancel the invoice and create a new one with the correct details.                     |
| Customer paid but the invoice is still showing as unpaid | Wait a few minutes and refresh. If it does not update after 30 minutes, see [Invoice Troubleshooting](doc:invoice-troubleshooting).  |
| GST not showing on the invoice                           | Enable GST in the **Settings** panel when creating the invoice, and make sure tax details are set for each item in the Item Catalog. |
| Customer cannot complete the payment                     | Ask what error they saw. See [Invoice Troubleshooting](doc:invoice-troubleshooting) for common payment issues.                       |

***

## What If My Customer Wants the Money Back?

<Cards>
  <Card title="Refunds" href="doc:introduction-refunds" icon="fad fa-arrow-rotate-left">
    Return all or part of a payment to your customer — directly from the PayU Dashboard.
  </Card>

  <Card title="Settlements" href="doc:split-settlments" icon="fad fa-building-columns">
    Find out when your money will reach your bank account and see your settlement history.
  </Card>

  <Card title="Disputes and Chargebacks" href="doc:chargeback" icon="fad fa-shield-halved">
    Handle cases where a customer has raised a complaint with their bank about a payment.
  </Card>
</Cards>

***

## Next Steps

<Cards>
  <Card title="Manage Invoice Items" href="doc:manage-invoice-items" icon="fa-box-open">
    Build your product and service catalog with rates and GST details before creating invoices.
  </Card>

  <Card title="Manage Invoices" href="doc:manage-invoices" icon="fa-list-check">
    View, filter, resend, cancel, and download your invoice records.
  </Card>

  <Card title="Invoice Troubleshooting" href="doc:invoice-troubleshooting" icon="fa-wrench">
    Fix issues with invoices not being received, payments failing, or status not updating.
  </Card>

  <Card title="Invoice FAQs" href="doc:invoice-faqs" icon="fa-circle-question">
    Common questions about PayU Invoices.
  </Card>
</Cards>
