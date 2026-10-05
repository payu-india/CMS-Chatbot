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
<Banner
  isInline={true}
  message="Integration effort: No code or website developer required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

Your item catalog is a reusable library of the products and services you bill for. Add items here once — with their rates and tax details — and you can quickly select them when creating any invoice.

***

## How Do I Access My Item Catalog?

To open the item catalog: log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor>, click **Invoices** under **Payment Tools**, then click the **Items** tab.


<Image src="https://files.readme.io/0ecd8c420de9ec7e8a8324d187cf710d87f87ce0f9d89dc8d4ba4d1beb4f9145-Screenshot_2025-06-02_at_7.52.31_PM.png" align="center" caption="Items tab in the Invoices section" border={true} />


The list shows all your items with their **Item ID**, **Item Name**, **Description**, **Rate**, and an **Actions** menu for editing or deleting each item.

Use the **Search** field at the top to find a specific item by name.

***

## What Can I Do With Items?

<Accordion title="Create a New Item" icon="far fa-plus">
  To add a product or service to your catalog:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and go to **Payment Tools → Invoices → Items**.
  2. Click **New Item** at the top-right corner.

  The **Add Item** panel opens.


  <Image src="https://files.readme.io/035c4754ff78e35b7b83189255b7466927c3d3a09b26460b7606ed9f98808fc8-Screenshot_2025-06-02_at_7.53.17_PM.png" align="center" caption="Add Item panel" border={true} />


  3. Fill in the basic details:

  | Field                | What to enter                                                                            |
  | -------------------- | ---------------------------------------------------------------------------------------- |
  | **Item Name**        | The name of the product or service — for example, "Website Design" or "Monthly Retainer" |
  | **Rate**             | The price per unit in rupees                                                             |
  | **Item Description** | A short description of what the item is (optional but useful for the customer)           |

  4. Click **Next** (or **Skip** if you do not need to add tax details now).

  5. To add tax details, fill in the **Tax Details** section:

  | Field                             | What to enter                                                                                                 |
  | --------------------------------- | ------------------------------------------------------------------------------------------------------------- |
  | **Inter-State Tax (IGST)**        | GST rate applicable when billing a customer in a different state                                              |
  | **Intra-State Tax (CGST + SGST)** | GST rate applicable when billing a customer in the same state                                                 |
  | **Cess**                          | Additional cess percentage if applicable                                                                      |
  | **HSN / SAC Code**                | The Harmonised System of Nomenclature (goods) or Service Accounting Code (services) for this item             |
  | **Tax Inclusive / Exclusive**     | Whether the rate you entered already includes tax (inclusive) or whether tax will be added on top (exclusive) |


  <Image src="https://files.readme.io/9384f328520e599c79f2b146a9868b343bc67d6c22274906d90028e3df59a23a-Screenshot_2025-06-02_at_7.55.24_PM.png" align="center" caption="Tax details for an item" border={true} />


  6. Click **Create Item** to save.

  The item is now available in the **Enter Item Name** drop-down when creating any invoice.
</Accordion>

<Accordion title="Edit an Item" icon="far fa-pen-to-square">
  To update an item's details:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and go to **Payment Tools → Invoices → Items**.
  2. Find the item you want to update and click **Edit** in the **Actions** column.

  The **Update Item** panel opens.


  <Image src="https://files.readme.io/353b75654a9e586d4380cb15bc660d71049bb62f1c7a0edea839094937dfadc4-Screenshot_2025-06-02_at_7.54.18_PM.png" align="center" caption="Update Item panel" border={true} />


  3. Update the **Item Name**, **Rate**, or **Item Description** as needed.
  4. Click **Next** to go to the Tax Details section and update the tax settings if required.
  5. Click **Update Item** to save the changes.

  <Callout icon="📘" theme="info">
    Editing an item updates the catalog for future invoices. It does not change any invoices that have already been created or sent.
  </Callout>
</Accordion>

<Accordion title="Delete an Item" icon="far fa-trash">
  To remove an item from your catalog:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and go to **Payment Tools → Invoices → Items**.
  2. Find the item you want to delete and click **Delete** in the **Actions** column.
  3. Confirm the deletion in the prompt.

  The item is removed from the catalog and will no longer appear in the **Enter Item Name** drop-down when creating invoices.

  <Callout icon="🚧" theme="warning">
    Deleting an item is permanent. It does not affect invoices that have already been created or sent — those invoices keep their original item details.
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
