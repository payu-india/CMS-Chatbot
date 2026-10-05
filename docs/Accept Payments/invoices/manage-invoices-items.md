---
title: Manage Invoice Items
excerpt: >-
  Build and manage your product and service catalog in PayU — add items with
  rates and GST details so you can quickly add them to any invoice.
deprecated: false
hidden: true
metadata:
  title: Manage Invoice Items — PayU Item Catalog | Developer Docs
  description: >-
    Add, edit, and delete products and services in your PayU item catalog. Set
    rates, GST rates, HSN/SAC codes, and tax details for use in invoices.
  keywords:
    - payu invoice items
    - payu item catalog
    - add item payu invoice
    - gst invoice item payu
    - hsn sac code payu invoice
    - edit item payu
    - delete item payu invoice
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
---
Your item catalog is a reusable library of the products and services you bill for. Add items here once with their rates and tax details and you can quickly select them when creating any invoice.

***

## How Do I Access My Item Catalog?

To open the item catalog: log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor>, click **Invoices** under **Payment Tools**, then click the **Items** tab.


<Image src="https://files.readme.io/0ecd8c420de9ec7e8a8324d187cf710d87f87ce0f9d89dc8d4ba4d1beb4f9145-Screenshot_2025-06-02_at_7.52.31_PM.png" align="center" caption="Access invoice items" border={true} />


The list shows all your items with their **Item ID**, **Item Name**, **Description**, **Rate**, and an **Actions** menu for editing or deleting each item. Use the **Search** field at the top to find a specific item by name.

***

## What Can I Do With Items?

You can perform the following actions:

- Create a new item
- Edit an item
- Delete an item

### Create a New Item

<Accordion title="Steps to Create a New Item" icon="far fa-plus">
  To add a product or service to your catalog:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and go to **Payment Tools → Invoices → Items**.

     <Image src="https://files.readme.io/94dfa65d0a446791a15b16e521d968d5ffe489bd2a57fb8ee68836ae4e0eafd8-Screenshot_2026-10-05_at_2.47.50_PM.png" align="center" caption="Access invoice items" border={true} />

  2. Click **New Item** at the top-right corner.

  The **Add Item** panel opens.

  3. Fill in the basic details:

  | Field                            | What to enter                                                                           |
  | -------------------------------- | --------------------------------------------------------------------------------------- |
  | **Item Name**                    | The name of the product or service. For example, "Website Design" or "Monthly Retainer" |
  | **Rate**                         | The price per unit in rupees                                                            |
  | **Item Description (optional )** | A short description of what the item is (optional but useful for the customer)          |


  <Image src="https://files.readme.io/035c4754ff78e35b7b83189255b7466927c3d3a09b26460b7606ed9f98808fc8-Screenshot_2025-06-02_at_7.53.17_PM.png" align="center" caption="Item basic details" border={true} />


  4. Click **Create Item**.

  5. Fill in the **Tax Details** section:

  | Field                             | What to enter                                                                                                 |
  | --------------------------------- | ------------------------------------------------------------------------------------------------------------- |
  | **Inter-State Tax (IGST)**        | GST rate applicable when billing a customer in a different state                                              |
  | **Intra-State Tax (CGST + SGST)** | GST rate applicable when billing a customer in the same state                                                 |
  | **Cess**                          | Additional cess percentage if applicable                                                                      |
  | **HSN / SAC Code**                | The Harmonised System of Nomenclature (goods) or Service Accounting Code (services) for this item             |
  | **Tax Inclusive / Exclusive**     | Whether the rate you entered already includes tax (inclusive) or whether tax will be added on top (exclusive) |


  <Image src="https://files.readme.io/340f21aba87184dad28da9f4893ebc6f3042c95b438d9b453d41d0c737febe22-Screenshot_2026-10-05_at_2.52.55_PM.png" align="center" caption="Item tax details" border={true} />


  6. Click **Save** to save the tax details.
     <Callout icon="📘" theme="info">
       ### **Tips:**

       You can choose to skip this step and add these details later.
     </Callout>

  The item is now available in the **Enter Item Name** drop-down when <Anchor target="_blank" href="https://docs.payu.in/docs/create-an-invoice-1">creating any invoice</Anchor>.
</Accordion>

***

### Edit an Item

<Accordion title="Steps to Edit an Item" icon="far fa-pen-to-square">
  To update an item's details:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and go to **Payment Tools → Invoices → Items**.

     <Image src="https://files.readme.io/a2ea6afb2fdf3c21f19368281176f8ab2ed3b9b973b7e878f6b5eea8c677e804-image.png" align="center" caption="Access invoice items" border={true} />

  2. Find the item you want to update and click the edit icon in the **Actions** column.


  <Image src="https://files.readme.io/2233d746b18292f5b3494252f563a9e2da15d4da491127c00d25467b599d23df-Screenshot_2026-10-05_at_2.56.08_PM.png" align="center" caption="Edit an item" border={true} />


  The **Update Item** panel opens.

  3. Update the **Item Name**, **Rate**, or **Item Description** as needed.


  <Image src="https://files.readme.io/353b75654a9e586d4380cb15bc660d71049bb62f1c7a0edea839094937dfadc4-Screenshot_2025-06-02_at_7.54.18_PM.png" border={true} />


  3. Click **Update Item** to go to the **Tax Details** section and update the tax settings if required.
  4. Click **Save** to save the changes.

  <Callout icon="📘" theme="info">
    ### **Tips:**

    Editing an item updates the catalog for future invoices. It does not change any invoices that have already been created or sent.
  </Callout>
</Accordion>

<Accordion title="Delete an Item" icon="far fa-trash">
  To remove an item from your catalog:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and go to **Payment Tools → Invoices → Items**.

     <Image src="https://files.readme.io/0c73be528be5f1125184abccdad445a78f934b98d19f3deab510312624efa903-image.png" align="center" caption="Access invouce items" border={true} />

  2. Find the item you want to delete and click the delete icon in the **Actions** column.

     <Image src="https://files.readme.io/a243c92fc31cc9ee8b6f6cdea692bd566b1efd96168e4f9f1aa9ae4499c637b2-Screenshot_2026-10-05_at_3.12.12_PM.png" align="center" caption="Delete an item" border={true} />

  3. Click **Yes, Delete** in the pop-up menu.

  The item is removed from the catalog and will no longer appear in the **Enter Item Name** drop-down when creating invoices.

  <Callout icon="🚧" theme="warning">
    ### Important!

    Deleting an item is permanent. It does not affect invoices that have already been created or sent.
  </Callout>
</Accordion>

***

## Next Steps

<Cards>
  <Card title="Create an Invoice" href="doc:create-an-invoice" icon="far fa-file-invoice">
    Create and send an invoice using items from your catalog.
  </Card>

  <Card title="Manage Invoices" href="doc:manage-invoices" icon="fa-list-check">
    View, resend, cancel, and download your invoice records.
  </Card>

  <Card title="Invoice Troubleshooting" href="doc:invoice-troubleshooting" icon="fa-wrench">
    Fix issues with invoices not being received or payments not going through.
  </Card>

  <Card title="Invoice FAQs" href="doc:invoice-faqs" icon="fa-circle-question">
    Common questions about PayU Invoices.
  </Card>
</Cards>
