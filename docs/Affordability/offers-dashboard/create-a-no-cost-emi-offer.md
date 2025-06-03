---
title: Create a No-Cost EMI Offer
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - No-Cost EMI Offer PayU
    - No-Cost EMI Offer Setup
    - Create No-Cost EMI Offer PayU
  robots: index
next:
  description: ''
---
Create a No-Cost EMI offer as described in this section and then you can collect payments from your customers using PayU Hosted (Non-seamless) or Merchant Hosted (Seamless) Checkout integration as described in the following sections:

* PayU Hosted
  * [Integrate with PayU Hosted Checkout - Offers](doc:payu-hosted-checkout-integration-with-offers)
* Merchant Hosted Checkout
  * [Instant Discount or Cashback using Merchant Hosted Checkout](doc:instant-discount-or-cashback-offers-integration-using-merchant-hosted-checkout)
  * [SKU-Based Offer using Merchant Hosted Checkout](doc:collect-payments-with-sku-based-offer-using-merchant-hosted-checkout-offers-integration)

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
3. Select **No Cost EMI** as the discount type.

 The *Basic Offer Details* page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/bb329721a61f129bdf8cd8376b722d5d9608b22c87f214b9b3d61cc70983f3e1-Screenshot_2025-06-03_at_5.04.39_PM.png" />

1. Add the basic details. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer).
2. After you complete the above details and click **Save & Process**.

   The *Payment Options* page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/2eb257440a7bc87f172cfb2e617bdde10d3a2792eb87bd3d442e860689565c00-Screenshot_2025-06-03_at_5.06.06_PM.png" />

> 📘 Note
>
> When you are creating an offer, you can choose to save the incomplete offer details in the Draft state using the **Save as Draft & Exit** button at the top-right corner and publish it later.

## Step 2: Configure payment modes

1. Click the **Allow Downpayment with No Cost EMI** toggle button to show the EMI options which are eligible for downpayment in the next two steps.

> 📘 Note:
>
> The **Downpayment Eligible** label in green colour is displayed next to the **Credit Card Name** column similar to the following screenshot as it is applicable only. This is not applicable for Debit Card or Cardless, so they are displayed in yellow colour.
>
>
>
> <Image align="center" className="border" border={true} src="https://files.readme.io/061a6f12abbddf3a51e7faad601caf7e84dd38bb0ada0defaed90ed5b41974e7-dashboard_emi_downpayment_enabled.png" />
>
>

1. For each of the following sub tabs, select the desired item on first column and **Tenures** column on which you wish to enable the offer. You can select all tenures of a specific bank and choose specific tenures for each bank.
   * Credit Card
   * Debit Card
   * Cardless
2. Select the **Set an exclusion/inclusion bin for the offer** check box to include/exclude the offer on a select list of BINs on the banks that were selected in Step 1 (of Configure payment modes) using the following steps in each **Exclusion Bin** and **Inclusion Bin** sub tabs:
   * Click **Download Sample File** if you are not having the sample file or CSV file template. The CSV file contains some sample BIN numbers (first 6 digits of Debit Card or Credit Cards), which you need to update according to your requirements.
   * Update the CSV or text file to include the BIN details. For updating the CSV file, you can use Microsoft Excel or any other Spreadsheet tool. 
   * Click the browse button in the **Add a list of bins that you want to include or exclude on offer** to upload the updated CSV file.

<Image align="center" className="border" border={true} src="https://files.readme.io/ffcb358c53def42d01a66edd5348191f536fd70af20a216e8e8c262b094a706d-dashboard_payment_options_emi_exclusion_list.png" />

1. Select **Yes** in the **Subvent GST** if you wish to collect GST for the subvention amount.
2. Click **Next**.

## Step 3: Include the Offer rules

1. Enter the offer rules and limitations on the *Set Offer Rules* page. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer#step-3-include-the-offer-rules).
2. After you complete the above details and click **Save & Process**.

> **Note**: You can choose either to specify the count or amount based on the **Counter** or **Budget amount** option.

3. After you complete the above details and click **Save & Proceed**.

   The *Setup Payment options of your offer* page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/03/Screenshot-2022-03-21-at-8.17.22-PM-1024x826.png)

***

## Step 4: Set up EMI options

To complete the offer details for No Cost EMI:

1. Select any of the following options from the **Select EMI Type** drop-down list:
   * Cards (Credit/Debit) EMI
   * Cardless EMI

> **Note**: Currently, only the **Cards (Credit/Debit) EMI** option is enabled and Cardless EMI will be made available by PayU soon.

The *Setup Payment options of your offer* page is updated to display the options for Cards EMI.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/03/Screenshot-2022-03-21-at-7.41.49-PM-1-1024x877.png)

2. Click **Add Payment Option**.

   The offer for the debit card payment option gets added to the Setup *Payment options of your offer* page.

3. Select **EMI** to add the cards supporting No-Cost EMI.

4. Enter the details as described in the *Setup EMI Options* page. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer).

5. Select **Yes** in the **Subvent GST** field to subvent the GST for the customers.

> **Notes**: The following must be taken care if you select the **Subvent GST** check box:
>
> * Create these types of offers if there is an agreement with the bank/brand. Reach out to KAM for any queries
> * Bank share, brand share, and merchant share should all add up to 100%
> * You will receive your reconciliation reports in this email
> * Reconciliation will be possible only after the refund window

6. Click **Save & Proceed**.

***

## Step 5: Review of the Offer

The *Preview of Cashback Offer page summarizes the details you* provided in Step 2 to Step 4.

1. Review all the configurations added before you make the offer available to your customers.
2. Click the **Edit** button to return back to the corresponding page and update the configuration.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/04/Screenshot-2023-04-18-at-8.08.24-AM-1-1024x794.png)

3. Click **Publish Offer** to make it available to customers.