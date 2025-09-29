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
Follow these steps to create a new payment link:

1. **Click "Create New Payment Link"** at the top-right corner of the page.

   * The *Create New Payment Link* pop-up page appears to add details such as the payment amount and purpose.

   <Image align="center" className="border" border={true} src="https://files.readme.io/554b3cb321e0336bb4886c7cd21aab5b800d75d238dbe647b7febe10decef1f0-dashboard_create_new_payment_link_step1.png" />

2. Enter the amount to be paid in the **Amount** field with the payment amount.

3. Enter the payment purpose description in the **Purpose** field.

4. Click the **Allow Partial Payment** toggle button if you want to allow partial payments. For example, if you want to collect an advance amount for a product or service, you can use this feature.

5. Define how many transactions are allowed using this payment link in the **Max Transactions Allowed** field.

6. Click **Add more details** to expand additional parameters.

   A pop-up page with additional fields will be displayed:\
   ![Step 2 Screenshot](https://files.readme.io/c73e2f1739d759815cf7503096e7c971927f4986c8b0dddafc6951b4a760cff2-dashboard_create_new_payment_link_step2.png)

   <br />

7. Select the following checkboxes for fields you want to include and click **Add Fields** to save.

   * Invoice Number
   * Tax
   * Shipping
   * Address Details
   * UDF
   * Merchant Reference ID

Scroll down to the \*\*Customer Details \*\*pane.

<Image align="center" className="border" border={true} src="https://files.readme.io/09b1e5b30bbcb46d0d1b457bfff8ccf422f49190014ec95d198640db0bf55eb2-dashboard_create_new_payment_link_step3.png" />

8. Enter the following information in the **Customer Details** pane to capture customer information:
   * Customer Name
   * Email
   * Phone Number
   * Notify via SMS/Email
   * Link Expiry (by default, it is 1 year)
9. Scroll down to configure additional details to capture while making payments using the link on Checkout page in the **Additional Customer Details** pane.
   * Customer Name
   * Customer Address
   * Customer Email
   * Customer Mobile

> 📘 Note:
>
> To add custom fields, click **Add New Fields+** for specific data you want to capture from customers.
>
> * Field Type
> * Mark as Mandatory (if required)
> * Field Name
>
> ![Custom Field Screenshot](https://files.readme.io/8eca3400c847299b4e879cf737dee9b719af66bf2a384e7a3054c62572b0dcac-dashboard_create_new_payment_link_custom_field.png)

After you create a payment link with these additional customer details fields, the PayU Check Out page will be similar to the following sample screenshot (**Customer Phone** and **Customer Email** are the additional customer details enabled in this sample):

<Image align="center" className="border" border={true} src="https://files.readme.io/d322acc2c2795a82b620e501380e4366576307f7a1c17ff79b89c6f0cfda5e66-dashboard_payment_link_with_additional_details.png" />

10. Click **Create and Send Payment Link** (at the top-right corner).

The link can be sent to the customer via SMS or email.