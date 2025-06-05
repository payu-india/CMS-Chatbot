---
title: Create a Pre-Discounted Offer
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - PayU India Pre-Discounted Offer
    - Pre-Discounted Offer Setup
    - Pre-Discounted Offer Creation
    - Pre-Discounted Offer for PayU Checkout Integration
  robots: index
next:
  description: ''
---
Pre-discounted offers are applied at your (merchant) end and the transaction amount passed is the discounted transaction amount. PayU is primarily used for doing certain checks and validations rather than applying the discount itself. Pre-discounted offers help you with the following:

* Better user experience on the PayU Payment page (PayU Hosted Checkout) as the offer is already applied at your side, PayU will not be showing the list of offers on the PayU Payment page.
* Reconciliation and Settlements (offer engine back calculates original transaction amount, discount amount, and the net debit amount which can be used on reconciliation & settlements).
* The **Don’t allow transaction, if offer is not applicable** flag is enabled by default.

This procedure describes how to create a Prebuilt offer on PayU Dashboard and it is similar to creating a Discount offer.

> 📘 Note:
>
> In Merchant Hosted Checkout integration, hide all other offers if Pre-Discounted offer is used.

***

### Steps to Create a No-Cost EMI Offer

1. [Add the basic details](#step-1-add-the-basic-details)
2. [Configure payment modes](#step-2-configure-payment-modes)
3. [Include the Offer rules](#step-3-include-the-offer-rules)
4. [Configure Offer Subvention Details](#step-4-configure-offer-subvention-details)
5. [Review of the Offer](#step-5-review-of-the-offer)

## Step 1: Add the basic details

1. Navigate to [.Offers Dashboard](doc:offers-dashboard).
2. Click **Create an Offer** at the top-right corner.

   The *Create New Offer* page is displayed.

   <Image align="center" className="border" border={true} src="https://files.readme.io/94d041dbfbfc5faa76260a76e736cdbb4030553dddcde8c5ef3efeb9ca5d0f95-Screenshot_2025-06-03_at_10.16.03_AM.png" />
3. Select the discount type as **Pre-Discounted Offer**.

The Choose an Offer Type to get started.

![]()

1. Select any of the following offer sub-types:
   * **Instant Discount**: The instant discount is applied and discounted amount is displayed on the PayU Payment page and other offers are not shown.
   * **Low-Cost EMI**: The low-cost EMI is applied and the EMI amount is displayed on the PayU Payment page and other offers are not shown.

 The *Basic Offer Details* page is displayed.

<Image align="center" src="https://files.readme.io/09dec7da3915af1371413ad8eb9195dbaebacd7934c5ba93e97f54d311c001eb-Screenshot_2025-06-05_at_10.16.18_AM.png" />

***

## **Step 2: Add Basic Details**

1. Include the basic details as described in the following table and then click **Save & Process**:

| **Field**                                                                                                                                | **Description**                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Title                                                                                                                                    | Enter a unique title for the offer. This would be displayed as the offer title on your Checkout page.                                                                                 |
| Description                                                                                                                              | Enter the offer text that would be shown to your customer at checkout (for PayU Hosted Checkout Integration transactions).                                                            |
| From Date, From Time, To Date, To Time                                                                                                   | Enter the offer validity date and time range. Your offer will be valid and visible to the customer between this time period. You can specify the time range up to the seconds detail. |
| Terms & Conditions                                                                                                                       | Enter the text content that should appear under the “Terms and Conditions” on the Checkout page for customers.                                                                        |
| Terms & Conditions Links                                                                                                                 | Enter the hyperlinks for independent hosted pages.                                                                                                                                    |
| **Note**: It is recommended to be used only If it is absolutely necessary to avoid redirections outside your customer purchase journey). |                                                                                                                                                                                       |

1. After you complete the above details and click **Save & Process**,

The *Set Offer Rules* page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/05/Screenshot-2022-05-26-at-11.39.03-AM-1-1024x665.png)

Scroll down the *Set Offer Rules* page for the **Additional Options** section.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Offers_Details_Additional_Options-875x1024.png)

> **Note**: When you are creating an offer, you can choose to save the incomplete offer details in the Draft state using the **Save as Draft & Exit** button at the top-right corner and publish it later.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/Pre-discounted_offer_step2-988x1024.png)

***

## **Step 3: Include the Offer Rules or Limitations**

The procedure to include the rules and limitations is similar to creating an Instant Discount or Cashback Offer. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer#step-3-include-the-offer-rules-or-limitations).

## **Step 4: Configure Payment Modes**

The procedure to configure the payment mode is similar to creating an Instant Discount or Cashback Offer. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer#step-4-configure-payment-modes).

The offer for the payment options you configured gets added to the Setup *Payment options of your offer* page.

***

## **Step 5: Review of the Offer**

The *Preview of Cashback Offer* page summarizes the details you provided in [Step 2](#step-2-add-basic-details) to [Step 4](#step-4-configure-payment-modes).

1. Review all the configuration added before you make the offer available to your customers.
2. Click the **Edit** button to return back to the corresponding page and update the configuration.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.32.06-PM-1024x573.png)

3. Click **Publish Offer** to make it available to customers.