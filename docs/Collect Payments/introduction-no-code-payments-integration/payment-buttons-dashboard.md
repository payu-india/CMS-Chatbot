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

To create a new Payment Button:

1. [Open the Create New Payment page](#step-1-open-the-create-new-payment-page)
2. [Customize the Payment Button](#step-2-customize-the-payment-button)
3. [Customize your Checkout Page](#step-3-customize-the-checkout-page)
4. [Configure Advanced Options](#step-4-customize-the-advanced-options)

## Step 1: Open the Create New Payment page

1. Select **Payment Tools** > **Payment Buttons** from the left pane of the Dashboard.

   The list of existing buttons are listed on the _Buttons_ page.


<Image src="https://files.readme.io/a494bb1de682ae83ec3d1023e1e13dfb65e02db0ef5332ca52b6e85232638c63-Screenshot_2025-06-02_at_7.09.40_PM.png" align="center" border={true} />


2. Click **Create New Button** at the top-right corner.

   The _Create New Payment Button_ page is displayed.


<Image src="https://files.readme.io/dace80a25807f722b25d1ee7054db2836a7a3d44d97cb7ca82f67664bdbfd54b-Screenshot_2025-06-02_at_7.09.15_PM.png" align="center" border={true} />


<Callout icon="👍" theme="okay">
  ###

  **Reference**: You can configure webhooks and check the status of transaction. For more information, refer to [Webhooks for Payments](doc:webhooks).
</Callout>

## Step 2: Customize the Payment button

To customize the Payment Button:

1. Select any of the following button label that must be displayed from the **Button Text** drop-down list:
   - Buy Now
   - Pay Now
   - Book Now
   - Donate Now
2. Enter the description in the **Item Name** field.
3. Enter the amount that must be collected in the **Amount** field.

> **Note**: The **Amount** field is optional and if you leave the field blank, the customers will be asked to enter the amount on the Checkout page.

4. Select the color of the button from the primary colours or use the dropper to select a custom color.
5. Select any the following button size that suits your website:
   - Small
   - Medium
   - Large

## Step 3: Customize the Checkout page

1. Navigate to the **Custom Details** tile.

   The fields on the **Custom Details** tile are displayed.


<Image src="https://files.readme.io/b3a27b5d2959197102e56442a3f0fa6054486c1db2caba39ba45c7bbab504f4f-Screenshot_2025-06-04_at_12.32.20_PM.png" align="center" width="250px" border={true} />


2. Click the toggle button to enable each field on the **Custom Details** tile and then Click the pencil button next to the field to launch the pop-up page similar to the following and then provide the details as described in the following table and click **Add Field**:

> **Note**: Use the **Add Fields** option at the bottom to add more fields on your Check Out page if required.


<Image src="https://files.readme.io/1eb6333ecf79f41c3bb978bd2c289d2af3822688df83f22b10edda2199e93a21-Screenshot_2025-06-04_at_12.33.44_PM.png" align="center" width="312px" border={true} />


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
        Select any of the following field types or controls that you wish to add on your Checkout page:

        - Text
        - Calendar
        - Drop-down the following field types or controls that you wish to add on your Checkout page:
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

After the fields are enabled, they are displayed on the PayU Checkout page when the customer clicks the payment button similar to the following sample screenshot (Customer Name and Customer Address in this sample screenshot):


<Image src="https://files.readme.io/865616d7519cf08e3ca37a1583db494fb638d457de658d32e0a157f9309388ac-Screenshot_2025-06-04_at_12.37.53_PM.png" align="center" border={true} />


## Step 4: Configure the advanced options

After the customer completes filling the details on Check Out page, they will enter the additional details as configured in this step and then redirected to after completing the checkout.

To configure the additional fields (to be displayed after payment page):

1. Scroll down to the **Custom Details** pane.

   The fields on the **Custom Details**tile are displayed.


<Image src="https://files.readme.io/414d861556b165c6f6065aa4eebc25ecbc543e74e4ba08a1d6ab5fc5d7ff4fbe-Screenshot_2025-06-02_at_7.22.41_PM.png" align="center" width="412px" border={true} />


2. Click any of the following toggle button so that must those customer details must be collected by customer during checkout:
   - Customer Name
   - Customer Address
   - Customer Email
   - Customer Name
3. Enter the page URL for the following fields:
   - **Success URL**:  URL to which the customer must be redirected if the payment is successful.
   - **Cancel URL**: URL  to which the customer must be redirected if the customer cancels or aborts the payment.
   - **Failure URL** : URL to which the customer must be redirected if the payment has failed.
4. Click **Generate Button**.

## Filter the Payment buttons

The **Filter** menu enables you to filter the payment buttons based on date range or payment button type.


<Image src="https://files.readme.io/aa8017f76337f733c85c604f5405b654e85a9d2ab165d9b60e1f34dc716fda54-Screenshot_2025-06-02_at_7.25.33_PM.png" align="center" border={true} />


#### Filter by created date range

To filter the payment buttons by date range:

1. Click **Past 1 Year** drop-down menu to view the date filter options.
2. Click to select any of the the date range:
   - Today
   - Yesterday
   - Past 7 days
   - Past 30 days
   - Past 1 year
   - Custom Range

> **Note**: For the **Custom Range** option, select the start date and end date for which the payment buttons must be displayed.

3. Click **Apply** to get the results.

#### Filter by Payment Button type

To filter the payment buttons based on its type:

1. Click **Filter** drop-down menu to view the filter options.
2. Click to select the check box for the desired options from the list.
3. Click **Apply** to get the results.

### Export the Payment Buttons history

You can download the payment button records history in CSV or XSLX format.


<Image src="https://files.readme.io/7e99a0e3631c410b75ab966f9d02613852a8565cb802ce7be22f23347bcddaab-Screenshot_2025-06-02_at_7.26.33_PM.png" align="center" border={true} />


To download the payment button records:

1. Click the **Download** menu to view the options.
2. Select the required format (CSV or XLSX) to generate the report.

A pop-up page is displayed with the status of the generated report.


<Image src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-27-at-7.41.29-PM.png" align="center" width="312px" />


3. Perform any of the following steps:
   - Click **Download Report** to complete the action.
   - Click **Share**, enter the recipient email ID, and then click **Share**.

<Callout icon="📘" theme="info">
  ###

  **Note**: You can share the report to multiple email IDs by entering the comma-separated entries.
</Callout>

<br />
