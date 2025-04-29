---
title: Upload Registration Transactions in Bulk
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: >-
    Upload Subscription Registration Transactions in Bulk or Recurring Payment
    Registration Transactions in Bulk
  description: >-
    Learn how to upload registration transactions in bulk using the PayU
    Dashboard. Follow our detailed guide to streamline your recurring payment
    processes efficiently.
  keywords:
    - upload registration transactions
    - ' bulk upload PayU'
    - ' PayU Dashboard guide'
    - ' recurring payments setup'
    - ' registration transactions bulk'
    - ' PayU bulk upload instructions'
    - ' upload transactions CSV'
    - ' PayU recurring billing'
    - ' bulk registration upload'
    - ' recurring payment registration'
    - ' recurring payment registration transactions in Bulk'
  robots: index
next:
  description: ''
---
This section describes the procedure to upload the registration transactions in bulk for collecting recurring payments.

## Prerequisites

- Download the sample file as in below [procedure](#procedure) (Steps 1 to 5) and update it to include the data to be uploaded.
- Ensure that all mandatory fields in the file are filled with the correct details. The columns in the Excel sheet for upload are described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "Column Name",
    "h-1": "Field Type (Mandatory/ Optional)",
    "h-2": "Character Limit",
    "0-0": "Amount",
    "0-1": "Mandatory",
    "0-2": "No Limit",
    "1-0": "Invoice Id",
    "1-1": "Optional",
    "1-2": "16 (Should be unique)",
    "2-0": "Merchant Ref Id",
    "2-1": "Optional",
    "2-2": "50 (should be unique and to support - \"^\\[A-Za-z0-9@#().+\\_;\\\\\\\\-\\\\\\\\\\[\\\\\\\\\\]\\]\\*$\" )",
    "3-0": "Product Description",
    "3-1": "Mandatory",
    "3-2": "255",
    "4-0": "Customer Name",
    "4-1": "Optional",
    "4-2": "255",
    "5-0": "Customer Email",
    "5-1": "Optional",
    "5-2": "Basic email validations",
    "6-0": "Customer Phone Number",
    "6-1": "Optional",
    "6-2": "Basic phone number validations",
    "7-0": "Validation Period",
    "7-1": "Optional",
    "7-2": "No max limit. Should be numeric ",
    "8-0": "Time Unit",
    "8-1": "Optional",
    "8-2": "The default value is D (days). Other supported values = M (minutes), H (hours)",
    "9-0": "Sendsms",
    "9-1": "Optional",
    "9-2": "Supported value = 0, 1 or empty   \n**Note**: To send a SMS, the following is required:  \n  \n- Phone number must be specified\n- **Sendsms**column = 1\n- **Notify via SMS** check box specified in Step 7  is selected",
    "10-0": "Sendemail",
    "10-1": "Optional",
    "10-2": "Supported value = 0, 1 or empty  \n**Note**: To send an email, the following is required:  \n  \n- Email ID must be specified\n- **Sendemail** column = 1\n- **Notify via Email** check box specified in Step 7  is selected",
    "11-0": "Customer Address",
    "11-1": "Optional",
    "11-2": "255",
    "12-0": "Cutomer City",
    "12-1": "Optional",
    "12-2": "255",
    "13-0": "Customer State",
    "13-1": "Optional",
    "13-2": "255",
    "14-0": "Customer Country",
    "14-1": "Optional",
    "14-2": "255",
    "15-0": "Zip code",
    "15-1": "Optional",
    "15-2": "255",
    "16-0": "Udf 1",
    "16-1": "Optional",
    "16-2": "255",
    "17-0": "Udf 2",
    "17-1": "Optional",
    "17-2": "255",
    "18-0": "Udf 3",
    "18-1": "Optional",
    "18-2": "255",
    "19-0": "Udf 4",
    "19-1": "Optional",
    "19-2": "255",
    "20-0": "Udf 5",
    "20-1": "Optional",
    "20-2": "255",
    "21-0": "IsSiEnabled",
    "21-1": "Mandatory",
    "21-2": "Supported value = 0, 1 or empty. If the value = 1 only then SI bulk upload link will be generated and the SI-related parameters will be  mandatory",
    "22-0": "Billing amount",
    "22-1": "Mandatory (if isSienabled =1)",
    "22-2": "Minimum value = 1",
    "23-0": "Billing cycle",
    "23-1": "Mandatory (if isSienabled =1)",
    "23-2": "Value should be monthly, daily, weekly, adhoc, yearly",
    "24-0": "Billing interval",
    "24-1": "Mandatory   a. if isSienabled =1  b. if billing cycle ≠ adhoc",
    "24-2": "For adhoc cycle, it is not mandatory, for other billing cycles, it is mandatory",
    "25-0": "Start date",
    "25-1": "Mandatory (if isSienabled =1)",
    "25-2": "DD/MM/YYYY format",
    "26-0": "End date",
    "26-1": "Mandatory (if isSienabled =1)",
    "26-2": "DD/MM/YYYY format",
    "27-0": "Payment Method",
    "27-1": "Mandatory (if isSienabled =1)",
    "27-2": "`creditcard\\|debitcard\\|upi\\|enach`"
  },
  "cols": 3,
  "rows": 28,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


- Ensure that your bulk upload files are in the CSV format, as this is the only supported file type. 
- The upload file size should not exceed 5 MB to ensure smooth processing. 
- Each batch can contain up to 60,000 records (approximately), which is the maximum number of records processed in a single batch.

## Procedure

1. Login to the Merchant Dashboard. For more information, refer to [Log in to Dashboard](https://docs.payu.in/docs/log-in-to-dashboard). 
2. Navigate to **Subscriptions.** 

The _Subscriptions Overview_ page is displayed on the right-pane. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b6a07fd76749d355187ca08a22fdbba9ed1b34147b404b8584e1270e99886f6d-bulk_upload_button.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


3. Click **Bulk Upload** at the top-right corner. 

The _Bulk Upload_ pop-up page is displayed. 

![](https://files.readme.io/16f626114a4d368f0a1b88113810cadf8875f013df740549c2d14af9f94a9cab-Screenshot_2024-09-16_at_11.03.44_AM.png) 

4. Select **Registration** to upload the registration transactions. 
5. Click **Continue.** 

The **Bulk Upload Registration** screen is displayed. 

![](https://files.readme.io/ff5c2bfc330bdfa1089bcc3897269318decb0d618e678222f2fb24a8051ae68c-bulk_upload_popup-page_details.png) 

6. Enter a batch description in the **Batch Description** to identify this particular upload. 
7. Select the following check boxes if you wish to notify the customer: 

- Email 
- SMS 

8. Click **Continue**. 

> **Note:** Download the sample file for registration of mandate using the **Download** button and update to include the registration transactions. For more information, refer to [Prerequisites](#prerequistes). 

9. Click **Choose file** and select the file containing all the mandates details that need to be created.  
10. Click **Upload.** 

> **Note:** After you submit a batch file, it will be picked up for processing within 60 minutes. 

After uploading the file, the system will automatically check for discrepancies. If there’s an issue, an error message is displayed on the screen. 

![](https://files.readme.io/51ee71e5b3f7b708604844bef0215f970da88238ae368f8da1af089ead9becdf-bulk_upload_popup-page_errors.png) 

After your file is successfully uploaded, a message similar to the following screenshot is displayed and then you will be redirected to the **Bulk Upload** listing screen. 

![](https://files.readme.io/f13ff94f11a504ea8ac1b552c7aaa9674ea6bac69de20e37ab8788501492099c-bulk_upload_popup-page_sucess.png) 

A record is added with the status as “Partially Processed” to the **Registration** tab sub-tab under the **Bulk Upload** tab similar to the following screenshot. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/35cc9bc263042e23420dafde87d37f6b212ecce5fd7d6547a4c471e1c5aba69f-bulk_upload_listing.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]