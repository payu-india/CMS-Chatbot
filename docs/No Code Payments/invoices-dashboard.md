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

<Image align="center" src="https://files.readme.io/702b1a9-Screenshot_2023-09-29_at_12.23.31_PM.png" />

> 📘 Reference:
>
> You can create invoices using APIs. For more information, refer to the following sections under API reference:
>
> * [Create Invoice API](ref:create_invoice_api)
> * [Expire Invoice API](ref:expire_invoice_api)

## Search invoices

You can search for a specific invoice using the invoice number or title in the search field.

The *Invoice* page displays the records for the past seven days by default. You can select a particular date range or month or year using the calendar view option given in the dashboard.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-45.png)

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

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-46.png)

You can filter the invoice records by invoice status using the **Filter** option given on the page.

1. Click to select the required invoice status from the drop-down list.
2. Click **Apply** to get the results.
3. Use the **Reset** to clear the selection if required.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-47.png)

## Share or download invoices

You can export the results using the **Download** button on the *Invoice* page. After you search and view and invoice, to download an invoice:

1. Click **Download** tab to view the options.
2. Click required format (CSV, XLSX, TXNS-CSV or TXNS-XLSX) to generate the report.

   A pop-up window will display the status of the generated report.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-48.png)

3. Perform any of the following steps:
   * Click **Download report t**o complete the action.
   * Click **Share** and then enter the recipient email ID. You can share the generated report using an email ID using this button.

> **Note:** You can share the report to multiple email IDs by entering the comma-separated entrie&#x73;*.*

<Image align="center" width="412px" src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-49.png" />

## Create an Invoice

To create a GST-enabled payable new invoice to send to customers:

1. Click **Create New Invoice**.

   The *Create New Invoice* page is displayed.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-59.png)

2. Enter the Invoice number in the **Invoice** field.
3. Click to select the **Due date** from the calendar view. The current date will be filled as the Issue date by default.
4. Enter the invoice title in the **Enter an invoice title** field.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-60.png)

6. Select the customer from the **Billed To** drop-down list to whom the invoice is created for.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-61.png)

7. Click **Add item** to include the item details for the invoice.
8. In the **Description** section, select the item name from the drop-down list.

> **Note**: You can create a new item using the **Create New Item** option from the **Enter Item Name** drop-down menu. For more information, refer to [Manage Invoice Items](#manage-invoice-items).

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-63.png)

You can apply the GSTandPartialPayments for the invoice using the **Enable GST** and **Enable Partial Payments** check boxes in the **Settings** pane of the invoice page.

9. Select the following check boxes as required on the **Setting**s pane:
   * **Enable GST**: Select this check box to enable GST.
   * **Enable Partial Payments**: Select this check box to enable partial payments for this invoice.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-64.png)

10. Click **Send Invoice** to share the invoice with the customer.

> 📘 Note:
>
> You can save, send, or cancel the invoice using the options on the top-right corner of the pag&#x65;*.*

## Manage invoice items

The **Items** tab on the invoice page provides the list of items created along with the details such as Item ID, Item Name, Item details, Amount, and Actions.

The search field enables you to search for a particular item using the item name.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-50.png)

### Create a new item

To create a new item:

1. Click **New Item** on the top-right corner.

   The *Add Item* pop-up page is displayed to add the details of the item.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-51.png)

2. Add the basic details like Item **Name, Rate, Item Description** and the **Tax details** (Optional).
3. Click **Create Item** to complete the action.
4. Use the **Cancel** to cancel the item creation if required.

   The **Actions** menu on the page enables you to edit or delete the items created.

### Update an item

To update an item:

1. Click **Edit** at the top-right corner.

The *Update Item* pop-up page is displayed.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-52.png)

2. Update the Basic Details such as **Item Name, Rate,** and **Item Description** here.
3. Click **Update Item** to complete.

### Update Tax Details for an Item

If you want to edit the Tax details for the item.

1. Click **Skip** to go to the **Tax Details** section (optional).

   The **Tax Details** tab is displayed on the *Update Item* pop-up page.

2. Update the **Inter-State Tax, Intra State Tax, Cess, HSN or SAC code** in the respective fields.

3. Click **Tax Inclusive or Tax Exclusive** as required.

4. Click **Save** to complete the action.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-53.png)

You can delete a particular item using the **Delete** button provided in the item view.

## Create a new customer

To create a customer in the **Invoice** section:

1. Navigate to **Dashboard** > **Collect Payments** \> **Invoice**.
2. Select the **Customer**s tab.
3. Click **New Customer** at the top-right corner of the tab.

   The *Add Customer* pop-up page is displayed.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-62.png)

4. Enter the following details in the respective fields.
   * Customer Name
   * Email
   * Contact Number
   * GSTIN
5. Click **Create Customer**.

   The customer gets created and the **Billing Address** tab is displayed.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/Screenshot-2021-08-19-at-8.52.54-AM-1024x640.jpg)

6. Enter the following details for the billing address:
   * Address (Address line 1 and Address line 2)
   * PIN Code
   * City
   * State
   * Country
7. Click **Save & next**.

   The **Shipping Address** tab is displayed.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/Screenshot-2021-08-19-at-9.02.43-AM-1024x884.jpg)

8. Perform any of the following steps:
   * Select the **Use same as Billing Address** check box.
   * Enter the following details for the shipping address:
     * Address (Address line 1 and Address line 2)
     * PIN Code
     * City
     * State
     * Country
9. Click **Save**.
