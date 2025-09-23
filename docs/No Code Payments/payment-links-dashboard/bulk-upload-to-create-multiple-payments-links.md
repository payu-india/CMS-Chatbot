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

<Image align="center" className="border" border={true} src="https://files.readme.io/0d3d2e942cca7d461d0539c6de7fe424515fef8a0701c15de103f9315c4eb7e6-Screenshot_2025-06-02_at_6.42.44_PM.png" />

You can categorize the multiple links created using bulk uploading by selecting any one or multiple statuses of the links. Use the **Filter** option to select one or more statuses from the following:

<Image align="center" className="border" border={true} src="https://files.readme.io/81f1fd463accfc80e9405f104275270f9b2f464dc4ddd8b39594749bd47498f2-Screenshot_2025-06-02_at_6.44.36_PM.png" />

## Create Payment Links in Bulk

You can generate and process Payment Links in bulk by uploading a .csv, .xls, or .xlsx file as per the provided format. This saves time and eliminates the hassle of creating multiple individual links.

To create the payment links in bulk:

1. Click **Bulk Create** given on the top right corner of the page.

   The _Generate Bulk Payment links_ page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/37a87c3f6d179953c5b1cbfb4ef6298650079b2353815363545d35c344046d09-Screenshot_2025-06-02_at_6.45.35_PM.png" />

2. Select the file from the library and click **Upload** to complete the action.

> **Note**: Click **Download Sample File** to download a sample CSV file to know the columns allowed in bulk upload.

The following table describes the purpose of each columns and whether it is mandatory:

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameters</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        Amount<br><code>mandatory</code>
      </td>
      <td>
        The columns must contain the payment amount must be greater than equal to 1.
      </td>
    </tr>
    <tr>
      <td>
        InvoiceID<br><code>mandatory</code>
      </td>
      <td>
        The column must contain the unique invoice identifier generated for each transaction.
      </td>
    </tr>
    <tr>
      <td>
        MerchantReferenceID<br><code>optional</code>
      </td>
      <td>
        The columns must contain the merchant generated transaction number which is used to track a particular order. This value must be unique.
      </td>
    </tr>
    <tr>
      <td>
        ProductDescription<br><code>mandatory</code>
      </td>
      <td>
        This column must contain the payment description.
      </td>
    </tr>
    <tr>
      <td>
        CustomerName<br><code>optional</code>
      </td>
      <td>
        This column must contain the customer's name.
      </td>
    </tr>
    <tr>
      <td>
        CustomerEmail<br><code>optional</code>
      </td>
      <td>
        This column must contain the customer's email.
      </td>
    </tr>
    <tr>
      <td>
        CustomerPhone<br><code>optional</code>
      </td>
      <td>
        This column must contain the customer’s mobile number. This must be 10-digit number.
      </td>
    </tr>
    <tr>
      <td>
        ValidationPeriod<br><code>optional</code>
      </td>
      <td>
        This column must contain the validation period of the email invoice. If this field is left empty, then default value will be taken as 365 days. This column value must be filled based on the Numerical value (eg 7) column where the unit is defined.
        <br><em>Note:</em> Maximum value for validation period can be 1000 days from the time of invoice creation.
      </td>
    </tr>
    <tr>
      <td>
        TimeUnit<br><code>optional</code>
      </td>
      <td>
        The column must time contain the unit for invoice validation period can be any of the following:<br>
        • D- to expire the invoice after x days.<br>
        • H-to expire the invoice after x hours.<br>
        • M-to expire the invoice after x minutes.
      </td>
    </tr>
    <tr>
      <td>
        SendSms<br><code>optional</code>
      </td>
      <td>
        The column must time contain any of the following whether to send SMS to customer or not:<br>
        • <b>1</b>: SMS is sent to customer<br>
        • <b>0</b>: SMS is not sent to customer<br>
        The default value (or if the column is left blank) is 0.
      </td>
    </tr>
    <tr>
      <td>
        SendEmail<br><code>optional</code>
      </td>
      <td>
        This column must contain whether an email will be sent to the customer: 1 = Yes, 0 = No. The default value may be 0.
      </td>
    </tr>
    <tr>
      <td>
        IsPartialPaymentAllowed<br><code>optional</code>
      </td>
      <td>
        The column must time contain:<br>
        • <b>1</b>: Allow partial payment by customer<br>
        • <b>0</b>: Do not allow partial payment by customer<br>
        The default value (or if the column is left blank) is 0.
      </td>
    </tr>
    <tr>
      <td>
        CustomerAddress1<br><code>optional</code>
      </td>
      <td>
        This column must contain the customer's address line 1.
      </td>
    </tr>
    <tr>
      <td>
        CustomerAddress2<br><code>optional</code>
      </td>
      <td>
        This column must contain the customer's address line 2 (additional address information).
      </td>
    </tr>
    <tr>
      <td>
        CustomerCity<br><code>optional</code>
      </td>
      <td>
        This column must contain the customer's city.
      </td>
    </tr>
    <tr>
      <td>
        CustomerState<br><code>optional</code>
      </td>
      <td>
        This column must contain the customer's state or region.
      </td>
    </tr>
    <tr>
      <td>
        CustomerCountry<br><code>optional</code>
      </td>
      <td>
        This column must contain the customer's country.
      </td>
    </tr>
    <tr>
      <td>
        CustomerZipCode<br><code>optional</code>
      </td>
      <td>
        This column must contain the customer’s postal or ZIP code.
      </td>
    </tr>
    <tr>
      <td>
        udf1 – udf5<br><code>optional</code>
      </td>
      <td>
        These columns can be used for custom user-defined fields for any additional information needed.
      </td>
    </tr>
    <tr>
      <td>
        userToken<br><code>optional</code>
      </td>
      <td>
        This column must contain the token for identifying or authenticating the user in API calls (if applicable).
      </td>
    </tr>
    <tr>
      <td>
        splitType<br><code>optional</code>
      </td>
      <td>
        This column must contain the split type used for distributing payments among sub-merchants or child MIDs.
      </td>
    </tr>
    <tr>
      <td>
        childMID1, childMID2, childMID3<br><code>optional</code>
      </td>
      <td>
        The column(s) must contain the sub-merchant IDs to which portions of the payment are to be split.
      </td>
    </tr>
    <tr>
      <td>
        aggregatorSubAmount1, aggregatorSubAmount2, aggregatorSubAmount3<br><code>optional</code>
      </td>
      <td>
        The column(s) must contain the amount to be credited to each corresponding childMID as part of the split.
      </td>
    </tr>
    <tr>
      <td>
        aggregatorCharges1, aggregatorCharges2, aggregatorCharges3<br><code>optional</code>
      </td>
      <td>
        The column(s) must contain any aggregator charges or fees deducted from each corresponding split amount.
      </td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

3. Enter the batch ID in the **Batch ID** field.
4. Enter the batch description in the **Batch Description** field.

> **Note**: The input for **Upload File** (at Step 2) and **Batch description** (at Step 4) fields are mandatory.

5. Select any of the following check boxes to notify:
   * SMS
   * Email

Scroll down to enter the **Custom Details** to expand the pane.

<Image align="center" className="border" border={true} src="https://files.readme.io/c99e9bc3b74c687f1da7d8e8876675edae8ce93e59dbf5e70ef36c1b2201dd52-Screenshot_2025-06-02_at_6.47.40_PM.png" />

7. Click any of the following toggle button so that must those customer details must be collected by customer during checkout:
   * Customer Name
   * Customer Address
   * Customer Email
   * Customer Name
8. Click **Add New Fields+** to add custom fields to be captured when your customer uses payment links apart from the details in Step 7.

   The **Create New Field** pop-up page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/bacd6c40f13106c386056fb4350a636e9722f1c33cca6d1a750d2a6153c5be4b-Screenshot_2025-06-02_at_6.51.19_PM.png" />

9. Enter the following details in the **Create New Field** pop-up page and click **Add Field**.
   * Field Type
   * Mark as mandatory
   * Field Name
10. Click **Create and Send Payment Links**.
