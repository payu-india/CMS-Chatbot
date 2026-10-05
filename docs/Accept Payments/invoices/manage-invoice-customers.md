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
Your customer directory is a reusable list of the people and businesses you bill an <Anchor target="_blank" href="https://docs.payu.in/docs/invoices">invoice</Anchor>. Add customers here once — with their contact details, GSTIN, and billing address — and you can quickly select them from the **Billed To** field when creating any invoice.

***

## How Do I Access My Customers?

To open the customer directory: log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor>, click **Invoices** under **Payment Tools**, then click the **Customers** tab.


<Image src="https://files.readme.io/eed8f2fd4cc2b4dd46be4d2d62fe7c5a99966f2f9383c542be8982bd22937b4c-Screenshot_2026-10-05_at_3.24.36_PM.png" align="center" caption="Access customers under invoices" border={true} />


The list shows all your saved customers with the following information:

- **Customer Id**
- **Customer Name**
- **Customer Email**
- **Mobile**
- **Actions**

Use the **Search** field at the top to find a specific customer by name or email.

***

## What Can I Do With Customers?

You can perfrom the following actions:

- Create a new customer
- Edit customer details
- Delete a customer

### Create a New Customer

<Accordion title="Steps to Create a New Customer" icon="far fa-user-plus">
  To add a customer to your directory:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and go to **Payment Tools → Invoices → Customers**.

     <Image src="https://files.readme.io/8da3a92473104698182d0649b84a9b2eb8cb2e0c4e55923ad88015efdcb6344b-image.png" align="center" caption="Access customers under invoices" border={true} />

  2. Click **New Customer** at the top-right corner.

  The **Add Customer** panel opens.

  3. Fill in the customer's basic details:

  | Field              | What to enter                                                                 |
  | ------------------ | ----------------------------------------------------------------------------- |
  | **Customer Name**  | The customer's full name or business name                                     |
  | **Email**          | Their email address used to send invoices                                     |
  | **Contact Number** | Their mobile number used to send invoices via SMS                             |
  | **GSTIN**          | Their GST Identification Number (optional, but required for B2B GST invoices) |


  <Image src="https://files.readme.io/dee5d8ae60ef68986e18cdb8bad2a0677449be5b45431202a1a05ab12720f73a-Screenshot_2025-06-02_at_7.56.19_PM.png" align="center" caption="Add basic details" border={true} />


  4. Click **Create Customer**.

  The customer is saved and the **Billing Address** tab opens automatically.

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

     <Image src="https://files.readme.io/7cdf3f643fffb6cb45e6c7491133a836cbc76b686946c90167bbcf8388d21b5a-Screenshot_2025-06-02_at_7.57.55_PM.png" align="center" caption="Enter billing address" border={true} />


  The **Shipping Address** tab opens.

  7. Enter the shipping address, or tick **Use same as Billing Address** to copy it automatically.

  8. Click **Save**.

  The customer is now available in the **Billed To** drop-down when <Anchor target="_blank" href="https://docs.payu.in/docs/create-an-invoice-1">creating any invoice</Anchor>.
</Accordion>

<Accordion title="Edit a Customer" icon="far fa-pen-to-square">
  To update a customer's details:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and go to **Payment Tools → Invoices → Customers**.

     <Image src="https://files.readme.io/e526f369ab650ab8b72d495d8d89cef913c2b4fafef8f4932a72dbe21bdf66a1-image.png" align="center" caption="Access customers under invoices" border={true} />

  2. Find the customer you want to update and click the edit icon in the **Actions** column.

     <Image src="https://files.readme.io/09d8187cef231b1f42e328991009655774d8da803c93d51e9155449cf11f27b9-Screenshot_2026-10-05_at_3.35.38_PM.png" align="center" caption="Edit customer detials" border={true} />

  3. Update the relevant fields such as basic details, billing address, or shipping address.
  4. Click **Save** to apply the changes.

  <Callout icon="📘" theme="info">
    ### **Tips:**

    Editing a customer updates the directory for future invoices. It does not change the contact details on invoices that have already been sent.
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
