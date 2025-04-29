---
title: Payment Buttons
excerpt: >-
  The Payment Buttons features allows you to create buttons on your website or
  blogs to collect payments or donations from your customers without writing
  code or no knowledge of coding.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - Payment Buttons
    - ' Create Payment Buttons'
    - ' Payment Buttons for websites'
  robots: index
next:
  description: ''
---
After you specify the button color according to your website or blog theme, button label and amount to be collected, PayU generates the code that you can embed on your website or blog.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/button-banner-bg-1.png)

The following video explains how to use payment buttons for your business:

To create a new Payment Button:

1. [Open the Create New Payment page](#step-1-open-the-create-new-payment-page)
2. [Customize the Payment Button](#step-2-customize-the-payment-button)
3. [Customize your Checkout Page](#step-3-customize-the-checkout-page)
4. [Configure Advanced Options](#step-4-customize-the-advanced-options)

## Step 1: Open the Create New Payment page

1. Select **Payment Tools** > **Payment Buttons** from the left pane of the Dashboard.

   The list of existing buttons are listed on the *Buttons* page.

<Image align="center" src="https://files.readme.io/b082dec-Screenshot_2023-09-29_at_12.15.58_PM.png" />

2. Click **Create New Button** at the top-right corner.

   The *Create New Payment Button* page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-27-at-11.00.51-AM-1024x807.jpg)

## Step 2: Customize the Payment button

To customize the Payment Button:

1. Select any of the following button label that must be displayed:
   * Buy Now
   * Pay Now
   * Book Now
   * Donate Now
2. Enter the description in the **Item Name** field.
3. Enter the amount that must be collected in the **Amount** field.

**Note**: The **Amount** field is optional and if you leave the field blank, the customers will be asked to enter the amount on the Checkout page.

4. Select the color of the button from the primary colours or use the dropper to select a custom color.
5. Select any the following button size that suits your website:
   * Small
   * Medium
   * Large

## Step 3: Customize the Checkout page

1. Expand the **Custom Details** tile.

   The fields on the **Custom Details** tile are displayed.

<Image align="center" width="412px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-27-at-1.19.59-PM-1024x529.png" />

2. Add each fields on the **Custom Details** tile to your Check Out page as follows:
   * Select the check box against the field.
   * Click the pencil button next to the field to launch the pop-up page similar to the following and then provide the details as described in the following table and click **Add Field**:

> **Note**: Use the **Add Fields** option at the bottom to add more fields on your Check Out page if required.

<Image align="center" width="312px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-27-at-1.22.13-PM.png" />

<Table>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Field Type
      </td>

      <td>
        Select the any of Select the any of the following field types or controls that you would like add on your Check Out page:  

        * Text  
        * Calendar  
        * Drop-downthe following field types or controls that you would like add on your Check Out page:
      </td>
    </tr>

    <tr>
      <td>
        Field Name
      </td>

      <td>
        Enter the field label that must be shown on the Check Out page.
      </td>
    </tr>

    <tr>
      <td>
        Mark as mandatory
      </td>

      <td>
        Select this check box to make the field mandatory so that customer has to provide input.
      </td>
    </tr>
  </tbody>
</Table>

## Step 4: Customize the Advanced options

After the customer completes filling the details on Check Out page, they will be redirected to after payment page that you specify in this step.

To customize the advanced options (after payment page):

1. Expand the **Advanced Options** tile.

   The fields on the **Advanced Options**tile are displayed.

<Image align="center" width="412px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-27-at-2.20.46-PM-1024x502.png" />

2. Enter the page URL in the **Success URL** field to which the customer must be redirected if the payment is successful.
3. Enter the page URL in the **Cancel URL** field to which the customer must be redirected if the customer cancels or aborts the payment.
4. Enter the page URL in the **Failure URL** field to which the customer must be redirected if the payment has failed.
5. Click **Generate Button**.

### Filter the Payment buttons

The **Filter** menu enables you to filter the payment buttons based on date range or payment button type.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-27-at-7.37.18-PM-1024x684.jpg)

#### Filter by created date range

To filter the payment buttons by date range:

1. Click **Past 1 Year** drop-down menu to view the date filter options.
2. Click to select any of the the date range:
   * Today
   * Yesterday
   * Past 7 days
   * Past 30 days
   * Past 1 year
   * Custom Range

> **Note**: For the **Custom Range** option, select the start date and end date for which the payment buttons must be displayed.

3. Click **Apply** to get the results.

#### Filter by Payment Button type

To filter the payment buttons based on its type:

1. Click **Filter** drop-down menu to view the filter options.
2. Click to select the check box for the desired options from the list.
3. Click **Apply** to get the results.

### Export the Payment Buttons history

You can download the payment button records history in CSV or XSLX format.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-27-at-7.39.14-PM-1024x691.png)

To download the payment button records:

1. Click the **Download** menu to view the options.
2. Select the required format (CSV or XLSX) to generate the report.

  A pop-up page is displayed with the status of the generated report.

<Image align="center" width="312px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-27-at-7.41.29-PM.png" />

3. Perform any of the following steps:
   * Click **Download Report** to complete the action.
   * Click **Share**, enter the recipient email ID, and then click **Share**.

> 📘 Note:
>
> You can share the report to multiple email IDs by entering the comma-separated entries.
