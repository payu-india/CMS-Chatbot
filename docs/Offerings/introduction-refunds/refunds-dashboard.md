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

* **Partial refund**: Where the refund amount is less than the payment amount. This means the merchant is refunding only part of the payment done by the customer. This happens when only part of the order is canceled.  
  Ex. Customer purchases two products from merchant or value Rs. 500 and Rs. 7000. Customer pays a total of Rs. 7,500 to the merchant via online payment. Now the customer returns product 1 of value Rs. 500. Now, the merchant only must return Rs. 500 to the customer (instead of the transaction amount of Rs. 7,500).
* **Instant refund**: If the instant refund is enabled for you, the refunds are completed within 5 minutes of the refund request.
* **Full refund**: Where the refund amount is equal to the payment amount. This means that the merchant is refunding the entire payment done by the customer for a transaction. This happens when either merchant or customer cancels the entire order.  
  Ex. Customer purchases two products from merchant or value Rs. 500 and Rs. 7000. Customer pays a total of Rs. 7,500 to the merchant via online payment. Now the customer returns both the product. Now, the merchant must return Rs. 7,500 to the customer.

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

<Image border={false} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/dashboard_transaction_details-934x1024.png" />

1. Click **Send Refund** at the top-right corner of the page.

The _Refund Payment_ pop-up page is displayed.

<Image align="center" border={false} width="350px" src="https://files.readme.io/ddd30371217dfadd3582d48286bc390db91a280857858dad75c1f083574fe860-dashboard_refund_payment.png" />

1. Enter the amount to be refunded in the **Refund Payment** field.
2. Click **Send Full Refund**.

**Note**: Refund amount will be reflected in customer’s bank account in 5-6 working days.

## Upload Bulk Refunds using Dashboard

Bulk upload allows merchants using PayU Dashboard to issue refunds in bulk using a .xls, .xlsx, or .csv file. Every file you upload containing refund information on Dashboard is known as a batch. After a batch is uploaded successfully, it is picked up for processing within 60 mins. After a batch is picked for processing the status against that batch gets updated. A batch file can be in either of these states:

* **UPLOADED**: This is the initial state of the file when it is uploaded. Once you upload a file, it stays ‘uploaded’ and gets picked up for processing within 60 mins.
* **QUEUED**: This state indicates that the file is read and refunds are queued in the system for processing.
* **PROCESSING**: This state indicates that the batch file is getting processed.
* **COMPLETED**: This is the final state of the file. It indicates that all the rows in the batch file were processed, either successfully or unsuccessfully. Merchants can download the batch output file from the dashboard to check the status of each refund.

After a batch crosses the **Uploaded** stage, the **Download Output** option gets enabled for that batch. You can then download the output file for the batch to check the refund status when required.

To initiate refunds using bulk upload:

1. Log on to PayU Merchant Dashboard and select **Transactions**.

<Image border={false} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/05/word-image.png" />

2. Select the **Batch Refunds** tab.

<Image border={false} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/05/word-image-1.png" />

```
A list of batches uploaded in the past is displayed on this page. The batches can be filtered based on the date of upload and batch status.
```

<Image border={false} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/05/word-image-2.png" />

3. Click Upload to upload a batch of refunds.

   The _Batch Upload_ pop-up page is displayed with instructions to upload the file.

<Image border={false} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/05/word-image-3.png" />

4. Use the **Download sample file** option to download the Excel file template that can be used for including the refund information:
   * Add the PayU ID/transaction ID against which the refund needs to be initiated in the first column of the Excel file.
   * Add the refund amount in the second column against each transaction ID.
   * Save the file.

> 📘 Notes:
>
> * Both these columns are mandatory and the column header should not be changed.
> * A unique file name should be uploaded each time

<Image border={false} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/05/word-image-4.png" />

5. Browse for the desired file from your system and click **Upload**.

   A message is displayed after the file is successfully uploaded.

<Image border={false} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/05/word-image-5.png" />

6. Click **Submit**.

A ‘success’ message is displayed with the number of total records uploaded for processing.

<Image border={false} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/05/word-image-6.png" />

```
After the batch is uploaded, the status is displayed as **Uploaded** under the **Batch Refunds** tab.
```

<Image border={false} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/05/word-image-7.png" />

7. Click the batch ID to open the batch details page.

   All refunds uploaded within that batch, their details along with present status are displayed on this page.

<Image border={false} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/05/word-image-8.png" />

```
A refund can be in any of these states:
```

* **IN PROGRESS**: When the refund is initiated and is being processed.
* **REQUESTED**: When the refund is sent to the bank for offline processing. In such cases, it takes 5-7 business days for the credit to reflect into the customer’s account.
* **SUCCESS**: When the refund is successfully processed
* **FAILURE**: When the refund failed while processing with the PG. The merchant can download the output file to see the failure reason.
* **REJECTED**: When the refund got rejected during initiation due to some validation failures. The merchant can download the output file to see the failure reason.

## **Track Refunds on Dashboard**

The **Refunds** tab of the _Transactions_page summarizes all the refunds for the selected date range. You can view the detailed transaction records and the option to export the transaction records for the selected period.

To view the refunds for a preferred interval:

1. Login to the Merchant Dashboard. For more information, refer to [Log in to Dashboard](doc:log-in-to-dashboard).
2. Navigate to **Track > Transactions** and then select the **Refunds** tab.

   The **Refunds** tab of the _Transactions_ page is displayed.

<Image border={false} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/11/dashboard_refunds_tab-1024x801.png" />

3. Below the Transactions Overview, click the drop-down for calendar view
4. Select the option **Today** to view the summary of transactions triggered for the day.
