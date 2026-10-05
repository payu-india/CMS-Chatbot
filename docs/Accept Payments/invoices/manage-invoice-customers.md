---
title: Manage Customers
excerpt: >-
  Build and manage your customer directory in PayU — add customers with their
  contact details and billing address so you can quickly bill them on any
  invoice.
deprecated: false
hidden: true
metadata:
  title: Manage Customers — PayU Invoice Customer Directory | Developer Docs
  description: >-
    Add, edit, and manage customers in PayU's Invoice section. Store customer
    name, email, GSTIN, billing and shipping address for fast invoice creation.
  keywords:
    - payu invoice customers
    - add customer payu invoice
    - payu customer directory invoice
    - gstin customer payu
    - billing address payu invoice
    - manage customers payu dashboard
    - payu invoice billed to
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
---
Your customer directory is a reusable list of the people and businesses you bill. Add customers here once — with their contact details, GSTIN, and billing address — and you can quickly select them from the **Billed To** field when creating any invoice.

***

## How Do I Access My Customers?

To open the customer directory: log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor>, click **Invoices** under **Payment Tools**, then click the **Customers** tab.

The list shows all your saved customers with their name, email, contact number, and GSTIN.

Use the **Search** field at the top to find a specific customer by name or email.

***

## What Can I Do With Customers?

<Accordion title="Create a New Customer" icon="far fa-user-plus">
  To add a customer to your directory:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and go to **Payment Tools → Invoices → Customers**.
  2. Click **New Customer** at the top-right corner.

  The **Add Customer** panel opens.


  <Image src="https://files.readme.io/dee5d8ae60ef68986e18cdb8bad2a0677449be5b45431202a1a05ab12720f73a-Screenshot_2025-06-02_at_7.56.19_PM.png" align="center" caption="Add Customer — basic details" border={true} />


  3. Fill in the customer's basic details:

  | Field              | What to enter                                                                 |
  | ------------------ | ----------------------------------------------------------------------------- |
  | **Customer Name**  | The customer's full name or business name                                     |
  | **Email**          | Their email address — used to send invoices                                   |
  | **Contact Number** | Their mobile number — used to send invoices via SMS                           |
  | **GSTIN**          | Their GST Identification Number (optional, but required for B2B GST invoices) |

  4. Click **Create Customer**.

  The customer is saved and the **Billing Address** tab opens automatically.


  <Image src="https://files.readme.io/51b00da2c05b345ca3d4166d9613782a3c379decc05f7c3843980638e3eaa895-Screenshot_2025-06-02_at_7.57.01_PM.png" align="center" caption="Billing Address tab" border={true} />


  5. Enter the customer's billing address:

  | Field              | What to enter                                |
  | ------------------ | -------------------------------------------- |
  | **Address Line 1** | Street address or building name              |
  | **Address Line 2** | Apartment, floor, or suite number (optional) |
  | **PIN Code**       | 6-digit postal code                          |
  | **City**           | City name                                    |
  | **State**          | State or union territory                     |
  | **Country**        | Country (defaults to India)                  |

  6. Click **Save & Next**.

  The **Shipping Address** tab opens.


  <Image src="https://files.readme.io/7cdf3f643fffb6cb45e6c7491133a836cbc76b686946c90167bbcf8388d21b5a-Screenshot_2025-06-02_at_7.57.55_PM.png" align="center" caption="Shipping Address tab" border={true} />


  7. Enter the shipping address, or tick **Use same as Billing Address** to copy it automatically.

  8. Click **Save**.

  The customer is now available in the **Billed To** drop-down when creating any invoice.
</Accordion>

<Accordion title="Edit a Customer" icon="far fa-pen-to-square">
  To update a customer's details:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and go to **Payment Tools → Invoices → Customers**.
  2. Find the customer you want to update and click **Edit** in the **Actions** column.
  3. Update the relevant fields — basic details, billing address, or shipping address.
  4. Click **Save** to apply the changes.

  <Callout icon="📘" theme="info">
    Editing a customer updates the directory for future invoices. It does not change the contact details on invoices that have already been created or sent.
  </Callout>
</Accordion>

<Accordion title="Delete a Customer" icon="far fa-trash">
  To remove a customer from your directory:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and go to **Payment Tools → Invoices → Customers**.
  2. Find the customer you want to delete and click **Delete** in the **Actions** column.
  3. Confirm the deletion in the prompt.

  The customer is removed from the directory and will no longer appear in the **Billed To** drop-down when creating invoices.

  <Callout icon="🚧" theme="warning">
    Deleting a customer is permanent. It does not affect invoices that have already been created or sent — those invoices keep their original customer details.
  </Callout>
</Accordion>

***

## Next Steps

<Cards>
  <Card title="Create an Invoice" href="doc:create-an-invoice" icon="far fa-file-invoice">
    Create and send an invoice to a customer from your directory.
  </Card>

  <Card title="Manage Invoice Items" href="doc:manage-invoice-items" icon="fa-box-open">
    Build your product and service catalog with rates and GST details.
  </Card>

  <Card title="Manage Invoices" href="doc:manage-invoices" icon="fa-list-check">
    View, resend, cancel, and download your invoice records.
  </Card>

  <Card title="Invoice FAQs" href="doc:invoice-faqs" icon="fa-circle-question">
    Common questions about PayU Invoices.
  </Card>
</Cards>
