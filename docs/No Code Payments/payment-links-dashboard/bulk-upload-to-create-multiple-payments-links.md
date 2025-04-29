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

   The *Generate Bulk Payment links* page is displayed.

<Image align="center" src="https://files.readme.io/4612b03-Screenshot_2023-09-29_at_12.06.47_PM.png" />

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
        Transaction ID\
        `optional`
      </td>

      <td>
        The columns must contain the merchant generated transaction number which is used to track a particular order. This value must be unique.
      </td>
    </tr>

    <tr>
      <td>
        Product Description\
        `mandatory`
      </td>

      <td>
        This column must contain the payment description.
      </td>
    </tr>

    <tr>
      <td>
        Customer Name\
        `optional`
      </td>

      <td>
        This column must contain the customer's name.
      </td>
    </tr>

    <tr>
      <td>
        Customer Email\
        `optional`
      </td>

      <td>
        This column must contain the customer's email.
      </td>
    </tr>

    <tr>
      <td>
        Customer Mobile\
        `optional`
      </td>

      <td>
        This column must contain the customer’s mobile number. This must be 10-digit number.
      </td>
    </tr>

    <tr>
      <td>
        Validation Period\
        `optional`
      </td>

      <td>
        This column must contain the validation period of the email invoice. If this field is left empty, then default value will be taken as 365 days. This column value must be filled based on the Numerical value ( eg 7)column where the unit is defined.  

        * \*Note\*\*: Maximum value for validation period can be 1000 days from the time of invoice creation.
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
6. Click **Custom Details** to expand the pane.

<Image align="center" src="https://files.readme.io/07bd0db-Screenshot_2023-09-29_at_12.10.08_PM.png" />

7. Select any of the following customer details required during checkout:
   * Customer Name
   * Customer Address
   * Customer Email
   * Customer Name
8. Click **Create and Send Payment Links**.
