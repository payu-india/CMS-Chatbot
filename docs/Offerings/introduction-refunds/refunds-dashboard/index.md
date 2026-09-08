---
title: Refunds Dashboard
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
Order cancellations are an unfortunate reality for any business. Customers may cancel an order, return part of the order, or the full order. Merchants may not have the resources to fulfill the order and must cancel it. Therefore, it is imperative for merchants collecting payment online can refund the payment to the merchant.

## Types of Refunds

Refunds can be classified into two types:

* **Partial refund**: Where the refund amount is less than the payment amount. This means the merchant is refunding only part of the payment done by the customer. This happens when only part of the order is canceled.<br />Ex. Customer purchases two products from merchant or value Rs. 500 and Rs. 7000. Customer pays a total of Rs. 7,500 to the merchant via online payment. Now the customer returns product 1 of value Rs. 500. Now, the merchant only must return Rs. 500 to the customer (instead of the transaction amount of Rs. 7,500).
* **Instant refund**: If the instant refund is enabled for you, the refunds are completed within 5 minutes of the refund request.
* **Full refund**: Where the refund amount is equal to the payment amount. This means that the merchant is refunding the entire payment done by the customer for a transaction. This happens when either merchant or customer cancels the entire order.<br />Ex. Customer purchases two products from merchant or value Rs. 500 and Rs. 7000. Customer pays a total of Rs. 7,500 to the merchant via online payment. Now the customer returns both the product. Now, the merchant must return Rs. 7,500 to the customer.

## Understanding Refunds

### How to get a Refund from various PayU India products

PayU offers refunds for payments made using PayU India products: PayU Offers, PayU Partners, Split Settlements, etc. Generally, you need to initiate a refund request using any of the following methods:

* **Cancel Refund Transaction** API: For more information, refer to [Refund Transaction API](ref:refund_transaction_api).
* **PayU Dashboard**: For more information, refer to [Refunds Dashboard](doc:refunds-dashboard#initiate-a-refund-using-dashboard).

### How long does it take to get a refund?

Refunds will take between 5-21 days for the refund amount to reflect in your customer’s bank account. In the case of Net Banking transactions, certain government banks may take some more days. You will be communicated over email with the status (successful or failed) once the request for a refund is processed.

### How does Chargeback differ from Refunds?

A chargeback is raised by the customer to the issuing bank for many reasons like a fraud transaction, unsatisfactory product or service delivery, etc. In refunds, it is initiated by you (merchants) after your customer requests for a refund or a transaction has failed for the customer.

## Initiate a Refund using Dashboard

You can issue refunds easily with PayU Dashboard.

To initiate the refund using Dashboard:

1. Login to the Merchant Dashboard.
2. Navigate to **Track > Transactions**.
3. Click the transaction ID to view the transaction details.

The transaction details are displayed for the transaction.


<Image src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/dashboard_transaction_details-934x1024.png" align="center" width="550px" />


4. Click **Send Refund** at the top-right corner of the page.

The _Refund Payment_ pop-up page is displayed.


<Image src="https://files.readme.io/ddd30371217dfadd3582d48286bc390db91a280857858dad75c1f083574fe860-dashboard_refund_payment.png" align="center" width="350px" border={true} />


5. Enter the amount to be refunded in the **Refund Payment** field.
6. Click **Send Full Refund** if the full amount is refunded or Send **Partial Refund** or partial amount is refunded.

<Callout icon="📘" theme="info">
  **Note**: Refund amount will be reflected in customer’s bank account in 5-6 working days.
</Callout>

## Upload Bulk Refunds using Dashboard

### Understanding Upload Bulk Refunds

Bulk refunds let merchants initiate multiple refund requests at after uploading a file through the PayU Dashboard. PayU processes the uploaded file row by row: each row represents one refund request and can be accepted for processing or rejected if it does not meet the file requirements. A batch output file provides the processing result for each row, helping merchants review refund outcomes.<br />Use this format to prepare the merchant-level file for a bulk refund upload. The file contains six columns: the first two columns are mandatory, followed by optional and Closed Loop Wallet-only conditional fields.

Every file you upload containing refund information on Dashboard is known as a batch. After a batch is uploaded successfully, it is picked up for processing within 60 mins. After a batch is picked for processing the status against that batch gets updated. A batch file can be in either of these states:

* **UPLOADED**: This is the initial state of the file when it is uploaded. Once you upload a file, it stays ‘uploaded’ and gets picked up for processing within 60 mins.
* **QUEUED**: This state indicates that the file is read and refunds are queued in the system for processing.
* **PROCESSING**: This state indicates that the batch file is getting processed.
* **COMPLETED**: This is the final state of the file. It indicates that all the rows in the batch file were processed, either successfully or unsuccessfully. Merchants can download the batch output file from the dashboard to check the status of each refund.

After a batch crosses the **Uploaded** stage, the **Download Output** option gets enabled for that batch. You can then download the output file for the batch to check the refund status when required.

## Supported file types

Bulk refund uploads support `.xls`, `.xlsx`, and `.csv` files.

## File requirements

- The first two columns, `transactionid` and `amount`, are mandatory.
- Do not change the first two column headers.
- Include all six columns in the file, in the order shown below. Leave fields that do not apply blank.
- Use a unique filename for each upload.

## Merchant-level fields

The following fields are defined at the merchant level:

| Field name       | Description                                                                                                                                                             | Requirement                          |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| `transactionid`  | Unique PayU Transaction ID (PayU ID) for which the refund is processed.                                                                                                 | Mandatory                            |
| `amount`         | Refund amount.                                                                                                                                                          | Mandatory                            |
| `remarks`        | Additional information or notes for reference and future tracking.                                                                                                      | Optional                             |
| `reference_id`   | Merchant's unique refund reference ID for merchant-side tracking and reconciliation.                                                                                    | Optional                             |
| `refund_type`    | Applicable only to Closed Loop Wallet merchants; other merchants may leave blank. Supported value: `wallet`.                                                            | Conditional: Closed Loop Wallet only |
| `customer_phone` | Customer's registered mobile number. Required only for Closed Loop Wallet refund processing; other merchants may leave blank. Supported value: a 10-digit phone number. | Conditional: Closed Loop Wallet only |

The first two fields, `transactionid` and `amount`, are mandatory for every merchant. The `remarks` and `reference_id` fields are optional. The `refund_type` and `customer_phone` fields are conditional: use them for Closed Loop Wallet refunds and leave them blank for other merchants. For Closed Loop Wallet refunds, set `refund_type` to `wallet` and provide the customer's registered 10-digit mobile number in `customer_phone`.

## Examples

The following examples show the six-column order. They are illustrative rows only.

### Standard refund row

For a non-Closed Loop Wallet refund, the two conditional fields are blank:

```csv
transactionid,amount,remarks,reference_id,refund_type,customer_phone
PayUTxn12345,500.00,Customer return,MER-REF-1001,,
```

### Closed Loop Wallet refund row

For a Closed Loop Wallet refund, provide `wallet` and the customer's registered 10-digit phone number:

```csv
transactionid,amount,remarks,reference_id,refund_type,customer_phone
PayUWallet67890,250.00,Wallet refund,MER-REF-1002,wallet,9876543210
```

<br />

### Procedure

To initiate refunds using bulk upload:

1. Log on to PayU Merchant Dashboard and select **Transactions**.


<Image src="https://files.readme.io/35b21b6978fc94e8ca9bbe3532fabbca3cccfaddcf88c503433cf9c479d27160-Screenshot_2025-10-28_at_3.23.33_PM.png" align="center" border={true} />


2. Select the **Batch Refunds** tab.


<Image src="https://files.readme.io/39c1803b52dd6308b958d37bcd7a512c75a5c4757314f89e450cbacb8f3d969c-Screenshot_2025-10-28_at_3.27.13_PM.png" align="center" border={true} />


A list of batches uploaded in the past is displayed on this page. The batches can be filtered based on the date of upload and batch status.

3. Click **Upload Batch Refund** to upload a batch of refunds.

   The _Batch Upload_ pop-up page is displayed with instructions to upload the file.


<Image src="https://files.readme.io/4466141eb8909a5b6940ee6da9f9e3481ec6e10101d0d234b561b95caeac28cf-Screenshot_2025-10-28_at_3.29.06_PM.png" align="center" width="350px" />


4. Use the **Download sample file** option to download the Excel file template that can be used for including the refund information:
   * Update the following columns of the Excel. For more information, refer to [Understanding Bulk Upload](#understanding-upload-bulk-refunds).
     * transactionid
     * amount
     * remarks
     * reference_id
     * refund_type
     * customer_phone
   * Save the file.

<Callout icon="📘" theme="info">
  ### **Notes:**

  - The first two columns, `transactionid` and `amount`, are mandatory.
  - Do not change the first two column headers.
  - Include all six columns in the file, in the order shown below. Leave fields that do not apply blank.
  - Use a unique filename for each upload.
</Callout>


<Image src="https://files.readme.io/be292fe196339018b61de275fd3233e7eb2865a19f238e4d2db36b643a37dad1-image_14.png" align="center" width="350px" />


5. Browse for the desired file from your system and click **Upload**.

   A message is displayed after the file is successfully uploaded.


<Image src="https://files.readme.io/ee4e6313213add86baf86026190a8fea13aed2f4d129e034cbe5b945f0d2329e-Screenshot_2025-10-28_at_3.44.05_PM.png" align="center" width="350px" border={true} />


6. Click **Submit**.

A ‘success’ message is displayed with the number of total records uploaded for processing.


<Image src="https://files.readme.io/ce7f19640f0b99797d15ad9b678c1d0108d7a767c5c0ba09b613acf67153e674-Screenshot_2025-10-28_at_3.44.41_PM.png" align="center" />


After the batch is uploaded, the status is displayed as **Uploaded** under the **Batch Refunds** tab.


<Image src="https://files.readme.io/eebf18ddeb4b753facbbad10da0ce010e39e09aff120c97ff51b47af5d67ac0d-Screenshot_2025-10-28_at_3.45.18_PM.png" align="center" border={true} />


7. Click the batch ID to open the batch details page.

   All refunds uploaded within that batch, their details along with present status are displayed on this page.

A refund can be in any of these states:

* **IN PROGRESS**: When the refund is initiated and is being processed.
* **REQUESTED**: When the refund is sent to the bank for offline processing. In such cases, it takes 5-7 business days for the credit to reflect into the customer’s account.
* **SUCCESS**: When the refund is successfully processed
* **FAILURE**: When the refund failed while processing with the PG. The merchant can download the output file to see the failure reason.
* **REJECTED**: When the refund got rejected during initiation due to some validation failures. The merchant can download the output file to see the failure reason.

## **Track Refunds on Dashboard**

The **Refunds** tab of the \_Transactions_page summarizes all the refunds for the selected date range. You can view the detailed transaction records and the option to export the transaction records for the selected period.

To view the refunds for a preferred interval:

1. Login to the Merchant Dashboard. For more information, refer to [Log in to Dashboard](doc:log-in-to-dashboard).
2. Navigate to **Track > Transactions** and then select the **Refunds** tab.

   The **Refunds** tab of the _Transactions_ page is displayed.


<Image src="https://files.readme.io/e971a50fb3dc37d9b6cebb19185806244b6baef7894f54034a21099e97a1d9c7-Screenshot_2025-10-28_at_3.47.38_PM.png" align="center" border={true} />


3. Below the Transactions Overview, click the drop-down for calendar view
4. Select the option **Today** to view the summary of transactions triggered for the day.
