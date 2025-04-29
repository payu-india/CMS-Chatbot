---
title: "Upload Recurring Transactions\_in Bulk"
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: "Upload Recurring Transactions\_in Bulk or Upload SI Transactions\_in Bulk or Upload Standing Instruction Transactions\_in Bulk"
  description: >-
    Learn how to upload recurring transactions in bulk using the PayU Dashboard.
    Follow our comprehensive guide to streamline your payment processes
    efficiently.
  keywords:
    - upload recurring transactions
    - ' bulk upload PayU'
    - ' PayU Dashboard guide'
    - ' recurring payments setup'
    - ' recurring transactions bulk'
    - ' PayU bulk upload instructions'
    - ' upload transactions CSV'
    - ' PayU recurring billing'
    - ' bulk recurring upload'
    - ' PayU payment processing'
    - upload standing instruction transactions
    - upload SI transactions
  robots: index
next:
  description: ''
---
After you register for recurring payments in bulk, you can upload the recurring transactions in bulk as described in this section.

## Prerequisites

- Download the sample file as in the below [procedure](#procedure) (Step 1 to 4) and update it to include the data to be uploaded.  
- Ensure that all mandatory fields in the file are filled with the correct details. The columns in the Excel sheet for upload are described in the following table (Expandable Text):

Description of Columns in the Excel File

| Column Name | Field Type (Mandatory/ Optional) | Character Limit | Description                                             |
| ----------- | -------------------------------- | --------------- | :------------------------------------------------------ |
| authpayuid  | Mandatory                        | 20              | The authpayuid for the recurring transaction.           |
| amount      | Mandatory                        | 15              | The amount to be debited for the recurring transaction. |
| txnid       | Mandatory                        | 50              | The transaction Id of the transaction.                  |
| email       | Optional                         | 50              | The email ID of the customer.                           |
| phone       | Optional                         | 50              | The mobile number of the customer.                      |
| udf 1       | Optional                         | 255             | The user defined field information.                     |
| udf 2       | Optional                         | 255             | The user defined field information.                     |
| udf 3       | Optional                         | 255             | The user defined field information.                     |
| udf 4       | Optional                         | 255             | The user defined field information.                     |

<br />

- Ensure that your bulk upload files are in the Excel format, as this is the only supported file type. 
- Each batch can contain up to 60,000 records (approximately), which is the maximum number of records processed in a single batch.

## Procedure

To upload recurring transactions using PayU Dashboard:

1. Login to the Merchant Dashboard. For more information, refer to [Log in to Dashboard](https://docs.payu.in/docs/log-in-to-dashboard). 
2. Navigate to **Subscriptions.** 
3. Click **Bulk Upload** at the top-right corner. 
4. Select any of the following type of file you want to upload. 

- **Recurring**: This must be used for Enach mandates  
- **Recurring + Pre-Debit**: This must be used for Cards and UPI mandates  

For example, **Recurring** is selected in the following screenshot.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d726f25bdae3121caf08b5c6cc35285c3bfd52f31d17da20589d8b4a509b7efc-dashboard-subscription-recurring-upload-selection.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


5. Click **Continue**. 

> **Note:** Download the sample file for registration or mandate using the **Download** button. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9a8f99c19f1cb452a9bf8de652208e39027cc54ff53fd47836480a3326c14fbd-dashboard-subscription-recurring-bulk-upload.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


6. Click **Choose file** and select the file containing all the mandates that need to be debited. This file should follow the format outlined in the provided sample file. For more information, refer to [Prerequisites](#prerequisites). 
7. Click **Upload**. 

After uploading the file, the system will automatically check for discrepancies. If there’s an issue, an error message will appear on the screen.  

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9870655ee9e9176030cb0cbd99f85e9dece3aabbda328c6f8be8d871d1b31bab-dashboard-subscription-recurring-bulk-upload-error.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


After your file is successfully uploaded, a message similar to the following screenshot is displayed and then you will be redirected to the _Bulk Upload_ listing screen.