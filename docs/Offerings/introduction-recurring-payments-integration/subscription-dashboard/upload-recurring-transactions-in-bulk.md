---
title: "Upload Recurring Transactions\_in Bulk"
excerpt: ''
deprecated: false
hidden: false
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

<Callout icon="fad fa-thumbs-up" theme="success">
  ### **Schedule Recurring Debits:**

  You can schedule recurring debits for future date by passing the `debit_date` field in the YYYY-MM-DD format in the bulk upload file.
</Callout>

***

## Prerequisites

* Download the sample file as in the below [procedure](#procedure) (Step 1 to 4) and update it to include the data to be uploaded.  
* Ensure that all mandatory fields in the file are filled with the correct details. The columns in the Excel sheet for upload are described in the following table (Expandable Text):

<Accordion title="Description of Columns in Excel sheet for uploading transactions in bulk" icon="fa-info-table">
  | Column Name | Field Type (Mandatory/ Optional) | Character Limit | Description                                                                                                                                           |
  | ----------- | -------------------------------- | --------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
  | authpayuid  | Mandatory                        | 20              | The authpayuid for the recurring transaction.                                                                                                         |
  | amount      | Mandatory                        | 15              | The amount to be debited for the recurring transaction.                                                                                               |
  | txnid       | Mandatory                        | 50              | The transaction Id of the transaction.                                                                                                                |
  | email       | Optional                         | 50              | The email ID of the customer.                                                                                                                         |
  | phone       | Optional                         | 50              | The mobile number of the customer.                                                                                                                    |
  | udf 1       | Optional                         | 255             | The user defined field information.                                                                                                                   |
  | udf 2       | Optional                         | 255             | The user defined field information.                                                                                                                   |
  | udf 3       | Optional                         | 255             | The user defined field information.                                                                                                                   |
  | udf 4       | Optional                         | 255             | The user defined field information.                                                                                                                   |
  | debit_date  | Optional                         | 10              | The date on which you want this transaction to be charged. Format: YYYY-MM-DD. If left blank, the transaction will be processed immediately as usual. |
</Accordion>

* Ensure that your bulk upload files are in the Excel format, as this is the only supported file type. 
* Each batch can contain up to 60,000 records (approximately), which is the maximum number of records processed in a single batch.
* You can schedule a transaction for a future T+1 date or any date up to 3 month in advance.
* You cannot schedule a transaction for a date more than 3 month from today — such rows will be rejected/marked as failed with an appropriate error.
* If you don't provide a debit date, the transaction is processed right away.

***

## Procedure

To upload recurring transactions using PayU Dashboard:

1. Login to the Merchant Dashboard. For more information, refer to [Log in to Dashboard](https://docs.payu.in/docs/log-in-to-dashboard). 
2. Navigate to **Subscriptions.** 
3. Click **Bulk Upload** at the top-right corner. 
4. Select any of the following file type you want to upload and click **Continue**. 
   - **Recurring**: This should be used for Enach mandates  
   - **Recurring + Pre-Debit**: This should be used for Cards and UPI mandates  


<Image src="https://files.readme.io/d726f25bdae3121caf08b5c6cc35285c3bfd52f31d17da20589d8b4a509b7efc-dashboard-subscription-recurring-upload-selection.png" align="center" caption="Select the file type" border={true} />


5. Click the **Download&#x20;**&#x62;utton to download the sample file for registration or mandate. 


<Image src="https://files.readme.io/9a8f99c19f1cb452a9bf8de652208e39027cc54ff53fd47836480a3326c14fbd-dashboard-subscription-recurring-bulk-upload.png" align="center" border={true} />


6. You can either:
   - Click **Choose file** and select the file containing all the mandates that need to be debited.
   - Drag and drop the file in the dedicated area.

The file should follow the format outlined in the provided sample file. Refer to the [Prerequisites](#prerequisites) section for more details. 

7. Click **Upload&#x20;**&#x74;o upload the file. 

After uploading the file, the system will automatically check for discrepancies. If there’s an issue, an error message will appear on the screen as shown below.


<Image src="https://files.readme.io/9870655ee9e9176030cb0cbd99f85e9dece3aabbda328c6f8be8d871d1b31bab-dashboard-subscription-recurring-bulk-upload-error.png" align="center" border={true} />


After your file is successfully uploaded, a message similar to the following screenshot is displayed.&#x20;

![](https://files.readme.io/c45881e015685b64795f94211d311a664f4d252d3482a98487ae4e6c49e7edb5-Screenshot_2026-10-12_at_11.43.29_AM.png)

<br />

8. Click **Ok, Got it.**

***

## Sample Response

You will receive the following data in the response

| Column name             | value                                       |
| ----------------------- | ------------------------------------------- |
| authpayuid              | 30300810212                                 |
| amount                  | 1.000000000000000000                        |
| transactionid           | sample123497                                |
| status                  | RC_DUE                                      |
| pg_response             | Info Response: Invoice Created Successfully |
| payuid                  |                                             |
| scheduled_debit_date    | 06/10/26 19:26                              |
| scheduled_predebit_date | 05/10/26 23:16                              |
| predebit_status         | Success                                     |
| recurring_status        | Scheduled                                   |
| predebit_executed_at    | 05/10/26 23:16                              |
| recurring_executed_at   |                                             |
| failure_reason          | Info Response: Invoice Created Successfully |
| currentstatus           | Scheduled                                   |
| previousstatus          |                                             |
| last_updated_at         | 05/10/26 23:16                              |
| errormessage            |                                             |
| errorcode               |                                             |
| txndate                 |                                             |
