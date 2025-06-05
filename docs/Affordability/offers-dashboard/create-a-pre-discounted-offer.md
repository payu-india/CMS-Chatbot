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

***

## Step 1: Add the basic details

1. Navigate to [.Offers Dashboard](doc:offers-dashboard).
2. Click **Create an Offer** at the top-right corner.

   The *Create New Offer* page is displayed.

   <Image align="center" className="border" border={true} src="https://files.readme.io/94d041dbfbfc5faa76260a76e736cdbb4030553dddcde8c5ef3efeb9ca5d0f95-Screenshot_2025-06-03_at_10.16.03_AM.png" />
3. Select the discount type as **Pre-Discounted Offer**.

The Choose an Offer Type to get started.

<Image align="center" className="border" border={true} src="https://files.readme.io/02fa936e855901b9f6faf8bae897cf7ad501390a4e565567315abee82f0b5020-dashboard_prediscounted_offer_types.png" />

4. Select any of the following offer sub-types:
   * **Instant Discount**: The instant discount is applied and discounted amount is displayed on the PayU Payment page and other offers are not shown.
   * **Low-Cost EMI**: The low-cost EMI is applied and the EMI amount is displayed on the PayU Payment page and other offers are not shown.

 The *Basic Offer Details* page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/09dec7da3915af1371413ad8eb9195dbaebacd7934c5ba93e97f54d311c001eb-Screenshot_2025-06-05_at_10.16.18_AM.png" />

5. Add the basic details. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer).
6. After you complete the above details and click **Save & Process**.

   The *Payment Options* page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/20face5ca921ac455c7dd74ba8fb532e274b2ac4dd69b581d64b52b3072af1a7-dashboard-prediscounted-payment-options.png" />

> 📘 Note
>
> When you are creating an offer, you can choose to save the incomplete offer details in the Draft state using the **Save as Draft & Exit** button at the top-right corner and publish it later.

## Step 2: Configure payment modes

1. Configure the payment modes. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer#configure-payment-modes).
2. Click **Next**.

The *Offer Rules* page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/2e7610844659ed93bfa6380b4023a90f4ff3c2b5743acdbe9ed3a2eeb39c385c-dashboard-prediscounted-offer-rules.png" />

## Step 3: Include the Offer rules

1. Enter the offer rules and limitations on the *Set Offer Rules* page. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer#step-3-include-the-offer-rules).
2. After you complete the above details and click **Next**.

   The *Subvention Details* page is displayed.

## Step 4: Configure Offer Subvention Details

1. Enter the subvention details in the *Subvention Details* page. For more information, refer to refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer#step-4-configure-offer-subvention-details).
2. After you complete the above details and click **Next**.

The *Preview Details* page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/a87a0559ec1e51c8daed008b50a26c33c186b877accfc72a3a4bc72b15eb3aa5-dashboard-prediscounted-preview_page.png" />

## Step 5: Review of the Offer

The *Preview Details* page summarizes the details you provided in Step 2 to Step 4.

1. Review all the configurations added before you make the offer available to your customers.
2. Click the **Edit** button to return back to the corresponding page and update the configuration.
3. Click **Publish** to make it available to customers.