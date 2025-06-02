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

   The *Generate Bulk Payment links* page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/37a87c3f6d179953c5b1cbfb4ef6298650079b2353815363545d35c344046d09-Screenshot_2025-06-02_at_6.45.35_PM.png" />

2. Select the file from the library and click **Upload** to complete the action.

> **Note**: Click **Download Sample File** to download a sample CSV file to know the columns allowed in bulk upload.

The following table describes the purpose of each columns and whether it is mandatory:

<Table>
  <thead>
    <tr>
      <th>
        Parameters
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Amount
        `mandatory`
      </td>

      <td>
        The columns must contain the payment amount must be greater than equal to 1.
      </td>
    </tr>

    <tr>
      <td>
        Transaction ID
        `optional`
      </td>

      <td>
        The columns must contain the merchant generated transaction number which is used to track a particular order. This value must be unique.
      </td>
    </tr>

    <tr>
      <td>
        Product Description
        `mandatory`
      </td>

      <td>
        This column must contain the payment description.
      </td>
    </tr>

    <tr>
      <td>
        Customer Name
        `optional`
      </td>

      <td>
        This column must contain the customer's name.
      </td>
    </tr>

    <tr>
      <td>
        Customer Email
        `optional`
      </td>

      <td>
        This column must contain the customer's email.
      </td>
    </tr>

    <tr>
      <td>
        Customer Mobile
        `optional`
      </td>

      <td>
        This column must contain the customer’s mobile number. This must be 10-digit number.
      </td>
    </tr>

    <tr>
      <td>
        Validation Period
        `optional`
      </td>

      <td>
        This column must contain the validation period of the email invoice. If this field is left empty, then default value will be taken as 365 days. This column value must be filled based on the Numerical value ( eg 7)column where the unit is defined.

        * *Note*\*: Maximum value for validation period can be 1000 days from the time of invoice creation.
      </td>
    </tr>

    <tr>
      <td>
        Time Unit\
        `optional`
      </td>

      <td>
        The column must time contain the unit for invoice validation period can be any of the following:

        * D- to expire the invoice after x days.
        * H-to expire the invoice after x hours.
        * M-to expire the invoice after x minutes.
      </td>
    </tr>

    <tr>
      <td>
        Send SMS\
        `optional`
      </td>

      <td>
        The column must time contain any of the following whether to send SMS to customer or not:\
        .  **1**:  SMS is sent to customer

        * **0** : SMS isnot sent to customer\
          The default value (or if the column is left blank) is 0.
      </td>
    </tr>

    <tr>
      <td>
        Is Partial Payment Allowed\
        `optional`
      </td>

      <td>
        The column must time contain:\
        .  **1**:  Allow partial payment by customer

        * **0** : Do not allow partial payment by customer\
          The default value (or if the column is left blank) is 0.
      </td>
    </tr>
  </tbody>
</Table>

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