---
title: Create a Personalized Coupon
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Create a Personalized Coupon Offer
  description: >-
    The document outlines the process of creating personalized coupon offers,
    which can be used to attract customers and boost sales by providing
    discounts or cashback. It details steps such as selecting discount types,
    adding offer details, setting rules, configuring payment modes, setting up
    customer communications, and reviewing the offer before publishing.
  keywords:
    - Personalized Coupon Offer
    - ' Coupon Offer'
    - ' Personalized Coupon'
    - ' Coupon on Dashboard'
  robots: index
next:
  description: ''
---
Coupon codes are an important feature of offers as they add tangibility to offers, thereby helping attract customers and improve sales by providing discounts or cashback on behalf of merchants, banks and brands.  Personalised coupons helps you mass-generate unique coupons that are specifically mapped to a unique customer, thus no pilferage, wrongful usage or mis-use of coupons. Also, they can be easily shared with your customers directly on WhatsApp.

This procedure describes how to create a Personalized coupon.

### Steps to Create an Offer

1. [Select the discount type](#step-1-select-the-discount-type)
2. [Add basic details of the offer](#step-2-add-basic-details)
3. [Include the offer rules or limitations](#step-3-include-the-offer-rules-or-limitations)
4. [Configure the payment modes which can avail the offer](#step-4-configure-the-payment-modes-which-can-avail-the-offer)
5. [Setting up customers and communications](#step-5-setting-up-customers-and-communications)
6. [Subvention details](#step-6-subvention-details)
7. [Review the offer](#step-7-review-the-offer)

***

## Step 1: Select the discount type

1. Navigate to [Offers Dashboard](doc:offers-dashboard).
2. Click **Create an Offer** at the top-right corner.

   The _Create New Offers_ page is displayed. 

![A screenshot of a computer
AI-generated content may be incorrect.](https://files.readme.io/0919005ba5c24643a0db4f15c0ea491db08dce9778b6ee5e47fde8666f25e97c-offers-dashboard-coupon-step1.png) 

1. Select **Personalised Coupons** as the offer type.  

![Personalised Coupons Offer Step1](https://files.readme.io/bafce64b610808d8b4ff9255331557956c624f391601e124e890f758de9e0392-Screenshot_2025-03-10_at_11.51.15_AM.png)   

## Step 2: Add basic details

1. Include the basic details as described in the following table:

| **Field**               | **Description**                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Offer Title             | Enter a unique title for the offer. This would be displayed as the offer title on your Checkout page.                                                                                 |
| Offer Description       | Enter the offer text that would be shown to your customer at checkout (for PayU Hosted Checkout Integration transactions).                                                            |
| Offer Period            | Enter the offer validity date and time range. Your offer will be valid and visible to the customer between this time period. You can specify the time range up to the seconds detail. |
| Terms & Conditions Text | Enter the text content that should appear under the “Terms and Conditions” on the Checkout page for customers.                                                                        |
| Apply Offer as          | You can apply the offer as** Instant Discount **or **Cashback Offer.**                                                                                                                |

2. Include the details in the **Coupon Code Guidelines** section as described in the following table and then click **Save & Process**:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "0-0": "Coupon Code Prefix",
    "0-1": "Enter a prefix for the coupon code to match with your campaign. For example, \"Welcome\".",
    "1-0": "Authenticate coupon at checkout",
    "1-1": "Select **Yes** to authenticate the coupon code entered by your customer whether it is valid one.",
    "2-0": "Authenticate coupon at checkout",
    "2-1": "Select **Yes** to show the coupon code on the checkout page after authentication.  \n**Note**: This option is enabled or visible only if **Yes** is selected in **Authenticate coupon at checkout**."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    null,
    null
  ]
}
[/block]


2. After you complete the above details and click **Next**,

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


2. After you complete the above details and click **Next**.

***

## Step 4: Configure payment modes

Select any of the following payment modes to configure offer details that is explained in the corresponding tabs. You can configure one or multiple payment options for an offer. For example, the “HDFC Diwali Offer” can contain 10% discount for HDFC debit or credit cards, HDFC UPI, and a 3-month interest-free EMI for HDFC cards.

> 📘 Reference:
> 
> For detailed information to configure payment modes, refer to [Create an Instant Discount or Cashback Offer.](https://docs.payu.in/docs/create-an-offer)

- [Cards](https://docs.payu.in/docs/create-an-offer#cards)
- [Net Banking](https://docs.payu.in/docs/create-an-offer#net-banking)
- [UPI](https://docs.payu.in/docs/create-an-offer#upi)
- [Wallets](https://docs.payu.in/docs/create-an-offer#wallets)
- [EMI](https://docs.payu.in/docs/create-an-offer#emi)
- [BNPL](https://docs.payu.in/docs/create-an-offer#bnpl)

The offer for the payment options you configured gets added to the Setup _Payment options of your offer_ page.

After you complete the above details and click **Next**.

***

## Step 5: Setting up customers and communications

### Setting up new customer base

1. Select the customer base from the **Customer Base** field.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/32326ce0ac00bf43784bf5184705f1c555e80986a21413895836426c9c640453-offers-dashboard-coupon-step5-customer-base.png",
        null,
        "A screenshot of a customer base\nAI-generated content may be incorrect."
      ],
      "align": "center",
      "sizing": "350px",
      "border": true
    }
  ]
}
[/block]


2. If you wish to configure a new customer base, click **New Customer Base** and follow these steps:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cf9dec12ce2b0b95420f20ade7d570ab6d6b68f71efcdd86fe5fafc8de3072d0-dashboard-offers-upload-new-customer-base-for-coupon.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "400px",
      "border": true
    }
  ]
}
[/block]


- Click **Download Sample File** if you are not having the sample file or CSV file template. The CSV file contains some sample customer details, which you need to update according to your requirements.  
- Update the CSV or text file to include the customer details with a unique user token. For updating the CSV file, you can use Microsoft Excel or any other Spreadsheet tool. 
- Click **Choose file** and select the CSV or text file and click **Upload**.

### Setting up communications (via WhatsApp)

This is an optional step. You can send the messages to the recipients directly and seamlessly from within the dashboard without the need to do it manually. The following communications are supported by PayU:

- [Pre-launch communication for building Intrigue](#pre-launch-communication-for-building-intrigue)
- [Post-launch communication](post-launch-communication)

> 📘 Note:
> 
> For sending WhatsApp messages, you are required to have a Meta account, using AISensy as our service provider. AISensy is a BSP that helps manage and approve WhatsApp templates with META. If you have any difficulties in setting up the AISensy account, contact your PayU Key Account Manager (KAM or [PayU Support](https://help.payu.in).) You need to log on to AISensy account to set up your WhatsApp templates. Click **logging into** and connect to the AISensy account.
> 
> [block:image]{"images":[{"image":["https://files.readme.io/8efe2dedae743d120eddcf4c639283ab545da4916126e615dfeed33f6195fd9f-dashboard-offers-coupon-setup-aisensy-acct.png","",""],"align":"center"}]}[/block]

#### Pre-launch communication for building Intrigue

They help send notifications to the end users for any upcoming offers

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2fcac7582f25ec71ee6ac756fbd249db67da89983d8bd716dbe1b84c0bb83cc6-dashboard-offers-upload-coupon-whatsapp-comm.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


#### Post-launch communication

This section is used to launch after coupon delivery. You need select template and then allow user to set up the delivery dates.

1. Click the **Enable Launch Communication** toggle button.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ef85097c3e7b68a1927d177e3b378913dd90ddfa93c07b3085deb83f9546069f-dashboard-offers-upload-coupon-whatsapp-comm-post-launch.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


2. Select the coupon from the **Select Communication Template (WhatsApp) **drop-down list.
3. Click the **Enable Re-Targeting Communication** toggle button enter the following details to enable the re-targeting communication:

| Field                                          | Description                                                                                                                                                                                   |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Set Retargeting Delay                          | Specify the number of days after the coupon is generated or the offer goes live to send retargeting communication.                                                                            |
| No. of communication to be sent (per customer) | Enter the total number of messages to be sent per customer for re-targeting. Once this limit is reached, no further messages will be sent.                                                    |
| Base interval between communication            | Set the number of days between messages. For example, if 2 messages are sent with a 4-day interval, the second message will go out 4 days after the first, only if the coupon remains unused. |
| Message template and Value of variables        | Choose the template that you want to trigger a message for.                                                                                                                                   |

4. After you complete the above details and click **Next**.

## Step 6: Subvention details

You can specify the subvention details, that is whether offer settlements will be managed by you or it will be borne by bank or corresponding brand. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d938828899f591a083b321bd056d8817b2576d74b30292f62027f5c56b887d4c-dashboard-offer-subvention-details.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


## Step 7: Review of the Offer

The _Preview of Cashback Offer_ page summarizes the details you provided in Step 2 to Step 4.

1. Review all the configurations added before you make the offer available to your customers.
2. Click the **Edit** button to return back to the corresponding page and update the configuration.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.32.06-PM-1024x573.png)

3. Click **Publish Offer** to make it available to customers.

 You can choose to generate coupons for existing customer base or upload new customer base by simply adding details to the sample file and clicking upload. Post upload, it will auto select this list.