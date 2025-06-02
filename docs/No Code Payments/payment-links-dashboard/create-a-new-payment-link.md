---
title: Create a Payment Link
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
To create a new payment link:

1. Click **Create New Payment Link** at the top right corner of the page.

   The *Create New Payment Link* pop-up page is displayed to add the details like amount and purpose of payment.

<Image align="center" className="border" border={true} src="https://files.readme.io/554b3cb321e0336bb4886c7cd21aab5b800d75d238dbe647b7febe10decef1f0-dashboard_create_new_payment_link_step1.png" />

2. Enter the amount to be paid in the **Amount** field.
3. Enter a description on the payment purpose in the **Purpose** field.
4. Click the **Allow Partial Payment** toggle button to allow partial payment.
5. Enter the maximum number of transactions allowed using this payment link in the **Max Transactions Allowed** field
6. Click **Add more details** to expand.

   A pop-up page with additional parameters is displayed.

<Image align="center" src="https://files.readme.io/c73e2f1739d759815cf7503096e7c971927f4986c8b0dddafc6951b4a760cff2-dashboard_create_new_payment_link_step2.png" />

7. Select the check box against the fields you wish to capture for the payment link and click **Add Fields** to save the changes. Based on the fields selected, enter the details
   * Invoice Number
   * Tax
   * Shipping
   * Address Details
   * UDF
   * Merchant Reference ID

After enter the above details, the \*\*Customer Details \*\*pane is used to capture the customer details.

<Image align="center" className="border" border={true} src="https://files.readme.io/09b1e5b30bbcb46d0d1b457bfff8ccf422f49190014ec95d198640db0bf55eb2-dashboard_create_new_payment_link_step3.png" />

6. Enter the following customer details as described in the following table:

* Customer Name
* Email
* Phone number
* Notify via SMS/Email
* Link Expiry

Scroll down for configuring details to be capturing while making payment using the payment link the **Additional Customer Details** pane.

7. Click the toggle buttons based on the details to be capture in the **Additional Customer Details** pane.
   * Customer Name
   * Customer Address
   * Customer Email
   * Customer Mobile
8. Click **Add New Fields+** to add custom fields to be captured when your customer uses payment links apart from the details in Step 7.

The **Create New Field** pop-up page is displayed.

<Image align="center" src="https://files.readme.io/8eca3400c847299b4e879cf737dee9b719af66bf2a384e7a3054c62572b0dcac-dashboard_create_new_payment_link_custom_field.png" />

9. Enter the following details in the **Create New Field** pop-up page and click **Add Field**.
   * Field Type
   * Mark as mandatory
   * Field Name
10. Click **Create and Send Payment Link** at the top-right corner to create and send the payment link (as SMS to the mobile or as an email).