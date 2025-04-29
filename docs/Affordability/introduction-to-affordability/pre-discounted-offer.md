---
title: Pre-Discounted Offer
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Pre-discounted offers are applied at your (merchant) end and the transaction amount passed is the discounted transaction amount. PayU is primarily used for doing certain checks and validations rather than applying the discount itself. Pre-discounted offers help you with the following:

- Better user experience on the PayU Payment page (PayU Hosted Checkout) as the offer is already applied at your side, PayU will not be showing the list of offers on the PayU Payment page.
- Reconciliation and Settlements (offer engine back calculates original transaction amount, discount amount, and the net debit amount which can be used on reconciliation & settlements).
- The **Don’t allow transaction, if offer is not applicable** flag is enabled by default.

This procedure describes how to create a Prebuilt offer on PayU Dashboard and it is similar to creating a Discount offer.

**Notes**:

- In Merchant Hosted Checkout integration, hide all other offers if Pre-Discounted offer is used.

After you create a Pre-Discounted Offer, you can collect payments from your customers using PayU Hosted (Non-seamless) as described in the PayU Hosted Checkout Integration with Offers.

## **Step 1: Select the Discount Type**

1. Navigate to [_Offers_ section of PayU Dashboard](https://devguide.payu.in/affordability/getting-started-with-affordability/navigate-to-offer-engine/).
2. Click **Create an Offer** at the top-right corner.

The _Create New Offer_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/Screenshot-2023-03-23-at-11.15.54-AM-1024x662.png)

1. Select the discount type as **Pre-Discounted Offer**.
2. Select any of the following offer sub-types:
   - **Instant Discount**: The instant discount is applied and discounted amount is displayed on the PayU Payment page and other offers are not shown.
   - **Low-Cost EMI**: The low-cost EMI is applied and the EMI amount is displayed on the PayU Payment page and other offers are not shown.

The _Basic Offer Details_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.11.36-PM-1024x573.png)

***

## **Step 2: Add Basic Details**

1. Include the basic details as described in the following table and then click **Save & Process**:

| **Field**                                                                                                                                | **Description**                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Title                                                                                                                                    | Enter a unique title for the offer. This would be displayed as the offer title on your Checkout page.                                                                                |
| Description                                                                                                                              | Enter the offer text that would be shown to your customer at checkout (for PayU Hosted Checkout Integration transactions).                                                            |
| From Date, From Time, To Date, To Time                                                                                                   | Enter the offer validity date and time range. Your offer will be valid and visible to the customer between this time period. You can specify the time range up to the seconds detail. |
| Terms & Conditions                                                                                                                       | Enter the text content that should appear under the “Terms and Conditions” on the Checkout page for customers.                                                                        |
| Terms & Conditions Links                                                                                                                 | Enter the hyperlinks for independent hosted pages.                                                                                                                                    |
| **Note**: It is recommended to be used only If it is absolutely necessary to avoid redirections outside your customer purchase journey). |                                                                                                                                                                                       |

1. After you complete the above details and click **Save & Process**,

The _Set Offer Rules_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/05/Screenshot-2022-05-26-at-11.39.03-AM-1-1024x665.png)

Scroll down the _Set Offer Rules_ page for the **Additional Options** section.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Offers_Details_Additional_Options-875x1024.png)

**Note**: When you are creating an offer, you can choose to save the incomplete offer details in the Draft state using the **Save as Draft & Exit** button at the top-right corner and publish it later.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/Pre-discounted_offer_step2-988x1024.png)

***

## **Step 3: Include the Offer Rules or Limitations**

The procedure to include the rules and limitations is similar to creating an Instant Discount or Cashback Offer. For more information, refer to [Create an Instant Discount or Cashback Offer](https://devguide.payu.in/offers-integration/create-an-offer/create-an-instant-discount-or-cashback-offer#step4).

## **Step 4: Configure Payment Modes**

The procedure to configure the payment mode is similar to creating an Instant Discount or Cashback Offer. For more information, refer to [Create an Instant Discount or Cashback Offer](https://devguide.payu.in/offers-integration/create-an-offer/create-an-instant-discount-or-cashback-offer#step3).

The offer for the payment options you configured gets added to the Setup _Payment options of your offer_ page.

***

## **Step 5: Review of the Offer**

The _Preview of Cashback Offer_ page summarizes the details you provided in [Step 2](https://devguide.payu.in/temp-offers-integration/create-an-offer-temp/create-a-pre-discounted-offer/#step2) to [Step 4](https://devguide.payu.in/temp-offers-integration/create-an-offer-temp/create-a-pre-discounted-offer/#step4).

1. Review all the configuration added before you make the offer available to your customers.
2. Click the **Edit** button to return back to the corresponding page and update the configuration.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.32.06-PM-1024x573.png)

1. Click **Publish Offer** to make it available to customers.