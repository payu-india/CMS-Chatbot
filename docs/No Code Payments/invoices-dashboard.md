---
title: Payment Invoices
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Create professional invoices and email them to your customers. This helps your customers, wherever they are, can pay you faster. Use the Invoices module of PayU Dashboard to send or manage invoices.

Select **Payment Tools** > **Invoices** from the left pane of the Dashboard.

<Image align="center" className="border" border={true} src="https://files.readme.io/b9ed6135e3053eb874d8bcd7e80ec64bcd98584a29d9503e4d93000e94b43da9-Screenshot_2025-06-04_at_2.58.54_PM.png" />

> 📘 Reference:
>
> You can create invoices using APIs. For more information, refer to the following sections under API reference:
>
> * [Create Invoice API](ref:create_invoice_api)
> * [Expire Invoice API](ref:expire_invoice_api)

## Search invoices

You can search for a specific invoice using the invoice number or title in the search field.

The *Invoice* page displays the records for the past seven days by default. You can select a particular date range or month or year using the calendar view option given in the dashboard.

<Image align="center" src="https://files.readme.io/38614931076cc05791bfba99a8241cc8ee9bb5bfe7d3a5ebc49c06704cf1d674-Screenshot_2025-06-02_at_7.31.48_PM.png" />

## View by time frame

To set up the time frame:

1. Click Calendar to open the calendar view.
2. Click to select **Today, Yesterday, Past 7 days,** or **Past 30 days** to view the transactions for the mentioned period.
3. Click **Apply** to view the results.

## View by custom time frame

To customize the view based on a custom time frame:

1. Click **Custom Range** option
2. Select the desired month and year from the drop-down list given at the top of the calendar view.
3. Click to select the desired date range for the selected month.
4. Click **Apply** to view the results.

<Image align="center" className="border" border={true} src="https://files.readme.io/2663edeacdcb8096f1001d53edbfe843bf0a71900b19be818c5bc74ad23918da-Screenshot_2025-06-02_at_7.32.45_PM.png" />

You can filter the invoice records by invoice status using the **Filter** option given on the page.

1. Click to select the required invoice status from the drop-down list.
2. Click **Apply** to get the results.
3. Use the **Reset** to clear the selection if required.

<Image align="center" className="border" border={true} src="https://files.readme.io/f5a14c138742dab206b151381602bffe494ea9e60099fe919cb5a21b9fa6c664-Screenshot_2025-06-02_at_7.33.50_PM.png" />

## Share or download invoices

You can export the results using the **Download** button on the *Invoice* page. After you search and view and invoice, to download an invoice:

1. Click **Download** tab to view the options.
2. Click required format (CSV, XLSX, TXNS-CSV or TXNS-XLSX) to generate the report.

   A pop-up window will display the status of the generated report.

<Image align="center" src="https://files.readme.io/6bfdbd8a5aa0302f25076d3779d2ff01d5ee80cafc87811baab72634d1491022-Screenshot_2025-06-02_at_7.35.59_PM.png" />

3. Perform any of the following steps:
   * Click **Download Report** to complete the action.
   * Click **Share** and then enter the recipient email ID. You can share the generated report using an email ID using this button.

> **Note:** You can share the report to multiple email IDs by entering the comma-separated entries\_.\_

<Image align="center" width="412px" src="https://files.readme.io/30347f87a23905772d7560b05acf0b520004f90911c51441277f4a8b4b93261b-Screenshot_2025-06-02_at_7.36.43_PM.png" />

## Manage invoice items

The **Items** tab on the invoice page provides the list of items created along with the details such as Item ID, Item Name, Item details, Amount, and Actions.

The search field enables you to search for a particular item using the item name.

<Image align="center" src="https://files.readme.io/0ecd8c420de9ec7e8a8324d187cf710d87f87ce0f9d89dc8d4ba4d1beb4f9145-Screenshot_2025-06-02_at_7.52.31_PM.png" />

### Create a new item

To create a new item:

1. Click **New Item** on the top-right corner.

   The *Add Item* pop-up page is displayed to add the details of the item.

<Image align="center" className="border" border={true} src="https://files.readme.io/035c4754ff78e35b7b83189255b7466927c3d3a09b26460b7606ed9f98808fc8-Screenshot_2025-06-02_at_7.53.17_PM.png" />

2. Add the basic details like Item **Name, Rate, Item Description** and the **Tax details** (Optional).
3. Click **Create Item** to complete the action.
4. Use the **Cancel** to cancel the item creation if required.

   The **Actions** menu on the page enables you to edit or delete the items created.

### Update an item

To update an item:

1. Click **Edit** at the top-right corner.

The *Update Item* pop-up page is displayed.

<Image align="center" src="https://files.readme.io/353b75654a9e586d4380cb15bc660d71049bb62f1c7a0edea839094937dfadc4-Screenshot_2025-06-02_at_7.54.18_PM.png" />

2. Update the Basic Details such as **Item Name, Rate,** and **Item Description** here.
3. Click **Update Item** to complete.

### Update Tax Details for an Item

If you want to edit the Tax details for the item.

1. Click **Skip** to go to the **Tax Details** section (optional).

   The **Tax Details** tab is displayed on the *Update Item* pop-up page.

2. Update the **Inter-State Tax, Intra State Tax, Cess, HSN or SAC code** in the respective fields.

3. Click **Tax Inclusive or Tax Exclusive** as required.

4. Click **Save** to complete the action.

<Image align="center" src="https://files.readme.io/9384f328520e599c79f2b146a9868b343bc67d6c22274906d90028e3df59a23a-Screenshot_2025-06-02_at_7.55.24_PM.png" />

You can delete a particular item using the **Delete** button provided in the item view.

## Create a new customer

To create a customer in the **Invoice** section:

1. Navigate to **Dashboard** > **Collect Payments** > **Invoice**.
2. Select the **Customer**s tab.
3. Click **New Customer** at the top-right corner of the tab.

   The *Add Customer* pop-up page is displayed.

<Image align="center" src="https://files.readme.io/dee5d8ae60ef68986e18cdb8bad2a0677449be5b45431202a1a05ab12720f73a-Screenshot_2025-06-02_at_7.56.19_PM.png" />

4. Enter the following details in the respective fields.
   * Customer Name
   * Email
   * Contact Number
   * GSTIN
5. Click **Create Customer**.

   The customer gets created and the **Billing Address** tab is displayed.

<Image align="center" src="https://files.readme.io/51b00da2c05b345ca3d4166d9613782a3c379decc05f7c3843980638e3eaa895-Screenshot_2025-06-02_at_7.57.01_PM.png" />

6. Enter the following details for the billing address:
   * Address (Address line 1 and Address line 2)
   * PIN Code
   * City
   * State
   * Country
7. Click **Save & next**.

   The **Shipping Address** tab is displayed.

<Image align="center" src="https://files.readme.io/7cdf3f643fffb6cb45e6c7491133a836cbc76b686946c90167bbcf8388d21b5a-Screenshot_2025-06-02_at_7.57.55_PM.png" />

8. Perform any of the following steps:
   * Select the **Use same as Billing Address** check box.
   * Enter the following details for the shipping address:
     * Address (Address line 1 and Address line 2)
     * PIN Code
     * City
     * State
     * Country
9. Click **Save**.