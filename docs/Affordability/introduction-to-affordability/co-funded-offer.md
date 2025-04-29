---
title: Co-Funded Offer
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
Co-funded offers are created when the discount/cashback is co-funded by the merchant along with a bank/brand. In such type of offer, PayU will help with end-to-end reconciliation and settlement of bank/brand funds to the merchant.

**Note:** PayU recommends you create these types of offers if there is an agreement with the bank/brand along with PayU, offers will not be co-funded otherwise. For any questions or to enable this co-funded offer, contact your PayU Key Account Manager.

After you create an Co-funded Offer, you can collect payments from your customers using PayU Hosted (Non-seamless) or Merchant Hosted (Seamless) Checkout integration as described in the following sections:

* [PayU Hosted Checkout Integration with Offers](https://devguide.payu.in/offers-integration/collect-payments-with-offers/instant-discount-or-cashback-offer/payu-hosted-checkout-integration-with-offers/)
* [Merchant Hosted Checkout Integration with Offers](https://devguide.payu.in/offers-integration/collect-payments-with-offers/instant-discount-or-cashback-offer/merchant-hosted-checkout-integration-with-offers/)

***

## **Step 1: Select the Discount Type**

1. Navigate to [*Offers* section of PayU Dashboard](https://devguide.payu.in/affordability/getting-started-with-affordability/navigate-to-offer-engine/).
2. Click **Create an Offer** at the top-right corner.

The *Create New Offer* page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.10.38-PM-1024x573.png)

1. Select the discount type as **Co-funded offer**.

 The *Basic Offer Details* page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.11.36-PM-1024x573.png)

***

## **Step 2: Add Basic Details**

Include the basic details on the *Basic Offer Details* page. or more information, refer to [Create an Instant Discount Offer or Cashback Offer](https://devguide.payu.in/offers-integration/create-an-offer/create-an-instant-discount-or-cashback-offer#step2) > [Add Basic Details](https://devguide.payu.in/offers-integration/create-an-offer/create-an-instant-discount-or-cashback-offer#step2).

## **Step 3: Include the Offer Rules or Limitations**

Enter the details on the *Set Offer Rules* page. For more information, refer to [Create an Instant Discount Offer or Cashback Offer](https://devguide.payu.in/offers-integration/create-an-offer/create-an-instant-discount-or-cashback-offer#step2) > [Include Offer Rules or Limitations](https://devguide.payu.in/offers-integration/create-an-offer/create-an-instant-discount-or-cashback-offer#step3).

## **Step 4: Configure Payment Modes**

Select any of the following payment modes to configure offer details. For more information, refer to [Create an Instant Discount Offer or Cashback Offer](https://devguide.payu.in/offers-integration/create-an-offer/create-an-instant-discount-or-cashback-offer#step2) > [Confgure Payment Modes](https://devguide.payu.in/offers-integration/create-an-offer/create-an-instant-discount-or-cashback-offer#step4).

## **Step 5: Adding Subvention Details**

Select **I will be sharing offer settlements with banks & brands** for a co-funding offer:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/04/subvention-offer-details-1024x510.png)

The fields related to subvention are displayed similar to the following screenshot:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/04/subevention-fields-1024x787.png)

Enter the details for each field as described in the following table:

| **Field** | **Description** |
| --------- | --------------- |

\| Your share\
**mandatory** | Enter a value between 0-100 for this. This will be the ratio of merchant’s share of the offer funding |\
\| Brand share\
**optional** | Enter a value between 0-100 for this. This will be the ratio of brand share of the offer funding |\
\| Bank Share\
**optional** | Enter a value between 0-100 for this. This will be the ratio of bank share of the offer funding |\
\| Choose bank\
**optional** | Select the bank name/bank id from the dropdown |\
\| Choose brand\
**optional** | Select the brand name/bank id from the dropdown |\
\| Emails\
**optional** | Enter the email id where you would like the reconciliation reports to be sent |\
\| Refund window\
**optional** | Recon files and settlement will be processed post the refund window |

## **Step 6: Review the Offer**

The *Preview of Cashback Offer* page summarizes the details you provided in [Step 2](https://devguide.payu.in/temp-offers-integration/create-an-offer-temp/create-a-co-funded-offer/#step2) to [Step 4](https://devguide.payu.in/temp-offers-integration/create-an-offer-temp/create-a-co-funded-offer/#step4).

1. Review all the configurations added before you make the offer available to your customers.
2. Click the **Edit** button to return back to the corresponding page and update the configuration.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.32.06-PM-1024x573.png)

1. Click **Publish Offer** to make it available to customers.
