---
title: Bulk Upload of Payment Links for Recurring Payments + Pre-Debit Notication
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
In PayUBiz Dashboard, you can upload payment links to notify customers and initiate the recurring transactions in bulk using the **Process Bulk Actions** pop-up page.

> 📘 Note: 
> 
> Ensure that you download the Excel file template as described in this procedure and specify the details for each column in the Excel file.

To upload payment links with Standing Instruction in bulk on PayUBiz Dashboard:

1. Log on to PayUBiz Dashboard.
2. Select **Bulk Upload** from the menu of the left pane.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/PayUBizDash_Home_Bulk_Upload_Selection-1024x612.png)

```
The _Process Bulk Actions pop-up_ page is displayed
```

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/PayUBizDB_Bulk_Upload-1024x694.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "552px"
    }
  ]
}
[/block]

3. Perform any of the following steps based on Net Banking or cards:
   - **Cards**: Select **Standing Instruction PreNotify+Recurring** from the **Select Action** drop-down list.
   - **Net Banking**: Select **Standing Instruction** from the **Select Action** drop-down list.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/PayUBizDB_Bulk_Recuring_menu_options-copy-1024x446.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "552px"
    }
  ]
}
[/block]

4. Click the **Download an example file** option next to the **Choose File** field if you require the Excel file template.
5. Open the Excel template to include the details to initiate recurring transactions.
6. Select the **Send Email** check box in the **Send Invoice** as field.
7. Select **Default Template** from the **Select Email Template** drop-down list.
8. Click **Browse File** in the **Choose File** field to select the Excel file containing the invoice bulk upload details.
9. Enter the bulk identifier provided by PayU to you in the **Bulk Identifier** field.
10. Click **Upload & Process**.