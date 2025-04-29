---
title: Banking Dashboard
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Banking** section comprises the two major functions:

- [Bank Accounts](https://devguide.payu.in/dashboard/banking/bank-accounts/)
- [Vendor Payments](https://devguide.payu.in/dashboard/banking/vendor-payments/)

#### **Bank Accounts**

PayU has partnered with the RBL Bank, but RBL solely handles this account opening process. For the bank account opening process, navigate to

**Dashboard > Banking > Bank Accounts**

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/09/dashboard_banking-1024x480.png)

You can use the **Request Document Collection** to collect the required documents from home. Use the **Contact Broker** to contact the support management for any queries. The account opening checklist has been provided in the dashboard for your reference.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-76.png)

### **Vendor Payments**

The **Vendor Payments** section provides an overview of your bills along with vendor information. The dashboard gives you the view of all bills along with the outstanding bill amount and the details of vendors.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/09/Dashboard_Vendor_Payments-1024x506.png)

For a seamless experience, you can open an account through the PayU dashboard using the **Open an Account** option. A request will be sent to the bank, and the bank officials will get in touch with you for further processing of your request.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-77.png)

#### **Add a New Vendor**

To add a new vendor:

1. Navigate to **Dashboard > Banking > Account Payable**.
2. Click **Add Vendor**.

   The _Add New Vendor_ pop-up page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/08/image-78.png)

3. Enter the vendor details like **Vendor Name, Mobile Number, email address** and the **GSTIN number** in the respective fields.
4. Click **Add Vendor** to finish.

### **Add a New Bill**

To add bills or invoices in bulk:

1. Click the **Add Bill** menu and select **Add Single Bill**.

   The _Add Single Bill_ page is displayed.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-79.png)

1. Enter the following basic details of the bill:

- Bill number
- Description
- Bill date and Due date (Select dated from Calendar)
- Gross Amount

**Note:** Add additional notes to enter more information.

2. Click **Save & Next** to proceed to the next page.
3. Enter the following vendor details:
   - **Vendor Name**
   - **Mobile Number**
   - **Email**
   - **GSTIN** no.
4. Perform any of the following steps:
   - Select the **Add Bank Account Details** option and enter the bank account details of the vendor:
     - Account Holder Name
     - Account Number
     - IFSC code.
   - Select the **Add UPI details** option and enter the UPI ID in the **UPI Id** field.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-80.png)

5. Select the **This will be saved as the Default account details for this vendor** checkbox to save the account details like the default account for the vendor.
6. Click **Save and Next** to complete.

    The vendor successfully added message is displayed on the page. The _Payment Details_ page is displayed.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-82.png)

7. Select the due date in the **Due Date** field.
8. Enter the amount payable to the vendor in the **Payable Amount** field.
9. Click **Save & Next** to proceed to the next stage.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-83.png)

10. Click **Proceed to Bill Payment** and

### **Making Bill Payments for the Vendor**

#### **Single Bill**

To make a single bill payment:

1. Click **Proceed to Bill Payment**.
2. Select **Add Bill** menu and select the **Add Single Bill** option.
3. Use the **Upload** button on the left corner of the page to upload your bill.

#### **Upload Bills in Bulk**

To add the bills or invoices in bulk:

1. Go to the **Add Bill** drop-down list and select the **Add more** option.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-84.png)

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-85.png)

1. Select to import a file from your library. You can import .CSV or .XLSX file format.
2. Click **Import** to complete the action.

**Note:** You can use the sample file for the format reference. Download the sample file using the **Sample Download file**.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-86.png)

### **Export Bills**

You can export all the bill details to CSV or XLSX format. To download the bill records, follow the below steps:

1. Click the **Download** tab to view the options.
2. Click the required format (CSV or XLSX) to generate the report.
3. A pop-up window will display the status of the generated report.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-87.png)

4. Click the **Download** report option to complete the action.

The filter option enables you to filter the bill records using the Status, Bill date range, or Bill amount range options.

5. Click the **Filter** tab to view the filter options.
6. Click to select the check box for the desired options from the status.
7. Select the date range using the calendar view.
8. Enter the **Minimum and Maximum** bill amount range in the respective columns.
9. Click **Apply** to get the results.

**Note:** You can use the **Reset** button to clear all checkbox selections.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-88.png)

You can perform the below functions using the Actions fields.

- Make a payment on your bill
- Edit the bill created
- Delete the bill

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-89.png)

**Note:** Use the Select all checkbox to select or unselect all bills on the page. Use the specific checkbox to select an individual to perform any action (Edit, Pay or Delete)_._