---
title: Create Payments links in Bulk
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
Merchants can take below bulk actions on multiple transactions by uploading an excel file. Navigate **Dashboard > Collect Payments > Bulk Uploads to access the bulk upload option**.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-43.png)

You can categorize the multiple links created using bulk uploading by selecting any one or multiple statuses of the links. Use the **Filter** option to select one or more statuses from the following:

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-44.png)

## Create Payment Links in Bulk

You can generate and process Payment Links in bulk by uploading a .csv, .xls, or .xlsx file as per the provided format. This saves time and eliminates the hassle of creating multiple individual links.

To create the payment links in bulk:

1. Click **Bulk Create** given on the top right corner of the page.

   The _Generate Bulk Payment links_ page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4612b03-Screenshot_2023-09-29_at_12.06.47_PM.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


2. Select the file from the library and click **Upload** to complete the action.

> **Note**: Click **Download Sample File** to download a sample CSV file to know the columns allowed in bulk upload. 

The following table describes the purpose of each columns and whether it is mandatory:

[block:parameters]
{
  "data": {
    "h-0": "Parameters",
    "h-1": "Description",
    "0-0": "Amount  \n`mandatory`",
    "0-1": "The columns must contain the payment amount must be greater than equal to 1.",
    "1-0": "Transaction ID  \n`optional`",
    "1-1": "The columns must contain the merchant generated transaction number which is used to track a particular order. This value must be unique.",
    "2-0": "Product Description  \n`mandatory`",
    "2-1": "This column must contain the payment description.",
    "3-0": "Customer Name  \n`optional`",
    "3-1": "This column must contain the customer's name.",
    "4-0": "Customer Email  \n`optional`",
    "4-1": "This column must contain the customer's email.",
    "5-0": "Customer Mobile  \n`optional`",
    "5-1": "This column must contain the customer’s mobile number. This must be 10-digit number.",
    "6-0": "Validation Period  \n`optional`",
    "6-1": "This column must contain the validation period of the email invoice. If this field is left empty, then default value will be taken as 365 days. This column value must be filled based on the Numerical value ( eg 7)column where the unit is defined.  \n**Note**: Maximum value for validation period can be 1000 days from the time of invoice creation.",
    "7-0": "Time Unit  \n`optional`",
    "7-1": "The column must time contain the unit for invoice validation period can be any of the following:  \n  \n- D- to expire the invoice after x days.\n- H-to expire the invoice after x hours.\n- M-to expire the invoice after x minutes.",
    "8-0": "Send SMS  \n`optional`",
    "8-1": "The column must time contain any of the following whether to send SMS to customer or not:  \n.  **1 **:  SMS is sent to customer  \n  \n- **0** : SMS isnot sent to customer  \n  The default value (or if the column is left blank) is 0.",
    "9-0": "Is Partial Payment Allowed  \n`optional`",
    "9-1": "The column must time contain:  \n.  **1 **:  Allow partial payment by customer  \n  \n- **0** : Do not allow partial payment by customer  \n  The default value (or if the column is left blank) is 0."
  },
  "cols": 2,
  "rows": 10,
  "align": [
    null,
    null
  ]
}
[/block]


3. Enter the batch ID in the **Batch ID** field. 
4. Enter the batch description in the **Batch Description** field.

> **Note**: The input for** Upload File ** (at Step 2) and **Batch description ** (at Step 4) fields are mandatory.

5. Select any of the following check boxes to notify:
   - SMS
   - Email
6. Click **Custom Details** to expand the pane.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/07bd0db-Screenshot_2023-09-29_at_12.10.08_PM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


7. Select any of the following customer details required during checkout:
   - Customer Name
   - Customer Address
   - Customer Email
   - Customer Name
8. Click **Create and Send Payment Links**.