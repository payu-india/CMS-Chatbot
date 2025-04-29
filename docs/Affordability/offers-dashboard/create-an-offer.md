---
title: Create an Instant Discount or Cashback Offer
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - Create Instant Discount Offer
    - Create Cashback Offer
    - PayU India checkout cashback offer
    - PayU India checkout Instant Discount Offer
    - Cashback Offer Setup
    - Instant Discount Setup
    - Discount and Cashback Offers PayU
    - Instant Discount Offer Creation
    - Cashback Offer Creation
  robots: index
next:
  description: ''
---
The procedure to create an Instant Discount or Cashback Offer on PayU Dashboard is similar.

***

### Steps to Create an Offer

1. [Select the discount type](#step-1-select-the-discount-type)
2. [Add basic details of the offer](#step-2-add-basic-details)
3. [Include the offer rules or limitations](#step-3-include-the-offer-rules-or-limitations)
4. [Configure the payment modes which can avail the offer](#step-4-configure-the-payment-modes-which-can-avail-the-offer)
5. [Review the offer](#review-the-offer)

***

After you create an Instant Discount or Cashback Offer, you can collect payments from your customers using PayU Hosted (Non-seamless) or Merchant Hosted (Seamless) Checkout integration as described in the following sections:

- PayU Hosted
  - [Integrate with PayU Hosted Checkout - Offers](doc:payu-hosted-checkout-integration-with-offers)
- Merchant Hosted Checkout
  - [Instant Discount or Cashback using Merchant Hosted Checkout](doc:instant-discount-or-cashback-offers-integration-using-merchant-hosted-checkout)
  - [SKU-Based Offer using Merchant Hosted Checkout](doc:collect-payments-with-sku-based-offer-using-merchant-hosted-checkout-offers-integration)

***

## Step 1: Select the discount type

1. Navigate to [Offers Dashboard](doc:offers-dashboard).
2. Click **Create an Offer** at the top-right corner.

   The _Create New Offer_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.10.38-PM-1024x573.png)

3. Select the discount type.

  The _Basic Offer Details_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.11.36-PM-1024x573.png)

***

## Step 2: Add basic details

1. Include the basic details as described in the following table and then click **Save & Process**:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "0-0": "Title",
    "0-1": "Enter a unique title for the offer. This would be displayed as the offer title on your Checkout page.",
    "1-0": "Description",
    "1-1": "Enter the offer text that would be shown to your customer at checkout (for PayU Hosted Checkout Integration transactions).",
    "2-0": "From Date, From Time, To Date, To Time",
    "2-1": "Enter the offer validity date and time range. Your offer will be valid and visible to the customer between this time period. You can specify the time range up to the seconds detail.",
    "3-0": "Terms & Conditions",
    "3-1": "Enter the text content that should appear under the “Terms and Conditions” on the Checkout page for customers.",
    "4-0": "Terms & Conditions Links",
    "4-1": "Enter the hyperlinks for independent hosted pages.  \n**Note**: It is recommended to be used only If it is absolutely necessary to avoid redirections outside your customer purchase journey)."
  },
  "cols": 2,
  "rows": 5,
  "align": [
    null,
    null
  ]
}
[/block]


2. After you complete the above details and click **Save & Process**,

   The _Set Offer Rules_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/05/Screenshot-2022-05-26-at-11.39.03-AM-1-1024x665.png)

3. Scroll down _Set Offer Rules_ page for the **Additional Options** section.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Offers_Details_Additional_Options-875x1024.png)

> 📘 Note:
> 
> When you are creating an offer, you can choose to save the incomplete offer details in the Draft state using the **Save as Draft & Exit** button at the top-right corner and publish it later.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.15.59-PM-1024x573.png)

***

## Step 3: Include the Offer rules or limitations

1. Enter the following details on the _Set Offer Rules_ page.

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "0-0": "Type of Cashback/Instant Discount",
    "0-1": "Specify whether the discount is in in terms of a percentage of the transaction amount or in terms of a flat discount.",
    "1-0": "Offer Percentage/Discount per transaction",
    "1-1": "Specify the discount value that has to applied in in terms of percentage or rupees in flat.",
    "2-0": "Maximum times an offer can be used",
    "2-1": "Specify how many times a customer can avail the offer.",
    "3-0": "Minimum transaction amount & Maximum transaction amount",
    "3-1": "Specify the threshold or range for a transaction to be applicable for the offer.",
    "4-0": "User Limits",
    "4-1": " ",
    "5-0": "Max time an offer can be used by a user?",
    "5-1": "Select any of the following options from the drop-down list to specify the maximum number of transactions the user can avail this offer:  \n - **Unlimited**: Users can avail the offer for unlimited transactions.  \n  \n- **Custom**: Specify the custom limit up to which the users can avail the offer.",
    "6-0": "Budget per user ",
    "6-1": " Enter the budget amount per user.",
    "7-0": "Reset User Limits",
    "7-1": "Select any of the following options from the drop-down list to reset the user limit for specified frequency:    \n  \n- **Every Day**: Reset the user limit everyday\n- **Every Week**: Reset the user limit every week\n- **Every Month**: Reset the user limit every month\n- **Custom**: Specify the custom frequency after which the user limit is reset"
  },
  "cols": 2,
  "rows": 8,
  "align": [
    null,
    null
  ]
}
[/block]


#### Additional Options

[block:parameters]
{
  "data": {
    "h-0": "Select for Offer – Counter or Budget Amount",
    "h-1": " Specify a limit on the number of times an offer can be availed or a budget for the discount volume.  \nFor example, if you select Budget amount to provide the offer to customers until you reach the budget of Rs. 3 Lakhs, specify 3,00,000.",
    "0-0": "Don’t allow transaction, if offer is not applicable",
    "0-1": "Select this check box if you do not want to allow the transaction if the offer is not applicable for the user.   \n**Note**: The option will work only if you post the offer key and the offer is live.",
    "1-0": "Do you wish to apply offers on certain products?",
    "1-1": "Select **Yes** if you wish to apply product-based or SKU-based offer. For more information, refer to [SKU-Based Offer using Merchant Hosted Checkout](doc:collect-payments-with-sku-based-offer-using-merchant-hosted-checkout-offers-integration).",
    "2-0": "In case of multiple quantity of same product?",
    "2-1": " Select **Yes** if you wish to apply the product-based or SKU-based offer to apply for multiple quantity. This field is enabled if **Yes** is selected in the Do you wish to apply offers on certain products? field."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


2. After you complete the above details and click **Save & Process**.

The _Setup Payment options of your offer_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.17.28-PM-1024x573.png)

***

## Step 4: Configure payment modes

Select any of the following payment modes to configure offer details that is explained in the corresponding tabs:

> 📘 Note:
> 
> You can configure one or multiple payment options for an offer. For example, the “HDFC Diwali Offer” can contain 10% discount for HDFC debit or credit cards, HDFC UPI, and a 3-month interest-free EMI for HDFC cards.

- [Cards](#cards)
- [Net Banking](#net-banking)
- [UPI](#upi)
- [Wallets](#wallets)
- [EMI](#emi)
- [BNPL](#bnpl)

### Cards

1. Select any of the following options on the _Setup Payment options of your offer_ page:

- Credit Card
- Debit Card

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-24-at-9.21.48-PM-1024x865.png)

2. Perform any of the following based on the method you want to select the bank and network:

[block:parameters]
{
  "data": {
    "h-0": "**Method**",
    "h-1": "**Description**",
    "0-0": "Select Bank and Networks",
    "0-1": " - Search and select the bank from the Select Banks and Select Networks drop-down list.  \n  \n- Search and select a network from the **Select Networks** drop-down list.",
    "1-0": "Specify the BIN numbers in CSV File",
    "1-1": "- Click **Download Sample File** if you are not having the sample file or CSV file template. The CSV file contains some sample BIN numbers (first 6 digits of Debit Card or Credit Cards), which you need to update according to your requirements.\n- Update the CSV or text file to include the BIN details. For updating the CSV file, you can use Microsoft Excel or any other Spreadsheet tool.\n- Click **Select .csv or .txt from your library** and select the CSV or text file."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


3. Select any of the following options in the **Set budget for credit card** field (optional):

**Note**: You can choose either specify count or amount based on the **Counter** or **Budget amount** option.

| Budget Type   | Description                                                                                                                                                                                    |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Counter       | Select this option and then specify the count in the **Counter Value** field. This offer will be enabled only for the transactions count as defined in the **Counter Value** field.            |
| Budget amount | Select this option and then specify the amount in the **Budget Amount** field. This offer will be enabled to customers until this budget amount is reached for your transactions cumulatively. |

4. Click **Add Payment Option**.

   The offer for the debit or credit card payment option gets added to the Setup _Payment options of your offer_ page.

### UPI

1. Select the **UPIs** option on the _Setup Payment options of your offer_ page.

   The _Select UPIs_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.28.25-PM-1024x556.png)

2. Select the check boxes for the UPIs you wish to enable the offer.
3. Select any of the following options in the **Set budget for credit card** field (optional):

**Note**: You can choose either enter count or amount based on the **Counter** or **Budget amount** option.

| **Budget Type** | **Description**                                                                                                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Counter         | Select this option and then specify the count in the **Counter Value** field. This offer will be enabled only for the transactions count as specified in the **Counter Value** field.          |
| Budget amount   | Select this option and then specify the amount in the **Budget Amount** field. This offer will be enabled to customers until this budget amount is reached for your transactions cumulatively. |

4. Click **Add Payment Option**.

### Wallets

1. Select the **Wallets** option on the _Setup Payment options of your offer_ page.

   The _Select Wallets_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.30.25-PM-1024x746.png)

2. Select the check boxes for the wallets you wish to enable the offer.
3. Select any of the following options in the **Set budget for credit card** field (optional):

**Note**: You can choose either enter count or amount based on the **Counter** or **Budget amount** option.

| **Budget Type** | **Description**                                                                                                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Counter         | Select this option and then specify the count in the **Counter Value** field. This offer will be enabled only for the transactions count specified in the **Counter Value** field.             |
| Budget amount   | Select this option and then specify the amount in the **Budget Amount** field. This offer will be enabled to customers until this budget amount is reached for your transactions cumulatively. |

4. Click **Add Payment Option**.

### EMI

1. Select the **EMI** option on the _Setup Payment options of your offer_ page.

   The _EMI_ Offer page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/03/Screenshot-2022-03-21-at-7.41.49-PM-1024x877.png)

2. Select Banks and Tenures on which you wish to enable the offer. You can select all tenures of a specific bank and choose specific tenures for each bank. 
3. Restrict the offer on a select list of BINs on the banks that were selected in Step 4 if required using the following steps:

- Click **Download Sample File** if you are not having the sample file or CSV file template. The CSV file contains some sample BIN numbers (first 6 digits of Debit Card or Credit Cards), which you need to update according to your requirements.  

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/01/Screenshot-2022-01-12-at-10.07.22-PM.png)

- Update the CSV or text file to include the BIN details. For updating the CSV file, you can use Microsoft Excel or any other Spreadsheet tool. 
- Click **Select .csv or .txt from your library** and select the CSV or text file. 

5. Select any of the following options in the **Set budget for EMI** field (optional):

**Note**: You can choose either enter count or amount based on the **Counter** or **Budget amount** option.

| **Budget Type** | **Description**                                                                                                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Counter         | Select this option and then specify the count in the **Counter Value** field. This offer will only be enabled for the transactions count specified in the **Counter Value** field.              |
| Budget amount   | Select this option and then specify the amount in the **Budget Amount** field. This offer will be enabled for customers until this budget amount is reached for your transactions cumulatively. |

6. Click **Add Payment Option**.

### BNPL

Select the **BNPL** option on the _Setup Payment options of your offer_ page.

The _Select BNPL Options_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/BNPL_Offer_Options-1024x651.png)

After you complete adding any one or combination of the offers involving various payment options, click **Save & Proceed**.

> 📘 **References:**
> 
> - No-Cost EMI offers can be created on Credit and Debit Card EMIs. For more information, refer to [Create a No-Cost EMI Offer](doc:create-a-no-cost-emi-offer).
> - Low-Cost EMI offers can create on Credit and Debit Card EMIs. For more information, refer to Create a Low-Cost EMI Offer.

The offer for the payment options you configured gets added to the Setup _Payment options of your offer_ page.

***

## **Step 5: Review of the Offer**

The _Preview of Cashback Offer_ page summarizes the details you provided in Step 2 to Step 4.

1. Review all the configurations added before you make the offer available to your customers.
2. Click the **Edit** button to return back to the corresponding page and update the configuration.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.32.06-PM-1024x573.png)

3. Click **Publish Offer** to make it available to customers.