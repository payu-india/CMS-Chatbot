---
title: Create a Low-Cost EMI Offer
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
Low-Cost EMI offers are for credit or debit cards to make purchases by paying a low-interest rate on the purchase amount. In this payment option, the customer has to pay interest charges on their purchase amount but at a lower rate than the regular interest rate.

For example, the purchase amount is ₹50,000. If the customer opts for the Low-Cost EMI offer, they can choose to pay for the product in installments over a period of 12 months at a lower interest rate. If the regular interest rate for a credit card is 18% per annum, but the bank is offering a special interest rate of 12% per annum. In this case, the customer will pay a total interest of ₹3,000 (i.e., ₹50,000 x 12% x 1 year) on the purchase, which adds up to a total payment of ₹53,000 over 12 months. So, instead of paying the entire amount upfront, the customer will pay ₹4,417 per month for 12 months.

While Low-Cost EMI may offer a lower interest rate than the regular interest rate, the total interest cost may still add up to a considerable amount over the payment period.

### Steps to Create a No-Cost EMI Offer

1. [Add the basic details](#step-1-add-the-basic-details)
2. [Configure payment modes](#step-2-configure-payment-modes)
3. [Include the Offer rules](#step-3-include-the-offer-rules)
4. [Configure Offer Subvention Details](#step-4-configure-offer-subvention-details)
5. [Review of the Offer](#step-5-review-of-the-offer)

## Step 1: Add the basic details

1. Navigate to [.Offers Dashboard](doc:offers-dashboard).
2. Click **Create an Offer** at the top-right corner.

   The _Create New Offer_ page is displayed.


   <Image src="https://files.readme.io/94d041dbfbfc5faa76260a76e736cdbb4030553dddcde8c5ef3efeb9ca5d0f95-Screenshot_2025-06-03_at_10.16.03_AM.png" align="center" border={true} />

3. Select **No Cost EMI** as the discount type.

 The _Basic Offer Details_ page is displayed.


<Image src="https://files.readme.io/bb329721a61f129bdf8cd8376b722d5d9608b22c87f214b9b3d61cc70983f3e1-Screenshot_2025-06-03_at_5.04.39_PM.png" align="center" border={true} />


4. Add the basic details. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer).
5. After you complete the above details and click **Save & Process**.

   The _Payment Options_ page is displayed.


<Image src="https://files.readme.io/2eb257440a7bc87f172cfb2e617bdde10d3a2792eb87bd3d442e860689565c00-Screenshot_2025-06-03_at_5.06.06_PM.png" align="center" border={true} />


<Callout icon="📘" theme="info">
  ### Note

  When you are creating an offer, you can choose to save the incomplete offer details in the Draft state using the **Save as Draft & Exit** button at the top-right corner and publish it later.
</Callout>

## Step 2: Configure payment modes

1. Click the **Allow Downpayment with No Cost EMI** toggle button to show the EMI options which are eligible for downpayment in the next two steps.

<Callout icon="📘" theme="info">
  ### Note:

  The **Downpayment Eligible** label in green colour is displayed next to the **Credit Card Name** column similar to the following screenshot as it is applicable only. This is not applicable for Debit Card or Cardless, so they are displayed in yellow colour.


  <Image src="https://files.readme.io/061a6f12abbddf3a51e7faad601caf7e84dd38bb0ada0defaed90ed5b41974e7-dashboard_emi_downpayment_enabled.png" align="center" border={true} />

</Callout>

2. For each of the following sub tabs, select the desired item on first column and **Tenures** column on which you wish to enable the offer. You can select all tenures of a specific bank and choose specific tenures for each bank.
   - Credit Card
   - Debit Card
   - Cardless
3. Select the **Set an exclusion/inclusion bin for the offer** check box to include/exclude the offer on a select list of BINs on the banks that were selected in Step 1 (of Configure payment modes) using the following steps in each **Exclusion Bin** and **Inclusion Bin** sub tabs:
   - Click **Download Sample File** if you are not having the sample file or CSV file template. The CSV file contains some sample BIN numbers (first 6 digits of Debit Card or Credit Cards), which you need to update according to your requirements.
   - Update the CSV or text file to include the BIN details. For updating the CSV file, you can use Microsoft Excel or any other Spreadsheet tool. 
   - Click the browse button in the **Add a list of bins that you want to include or exclude on offer** to upload the updated CSV file.


<Image src="https://files.readme.io/ffcb358c53def42d01a66edd5348191f536fd70af20a216e8e8c262b094a706d-dashboard_payment_options_emi_exclusion_list.png" align="center" border={true} />


4. Select **Yes** in the **Subvent GST** if you wish to collect GST for the subvention amount.
5. Click **Next**.

The _Enter details of your Offer_ page is displayed


<Image src="https://files.readme.io/8e8036030bd73b52addefb493b5ad800c10cc446b32fa2ddc194879dd8148c5a-dashboard_emi_offer_details.png" align="center" border={true} />


## Step 3: Include the Offer rules

1. Enter the offer rules and limitations on the _Set Offer Rules_ page. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer#step-3-include-the-offer-rules).
2. After you complete the above details and click **Next**.

   The _Subvention Details_ page is displayed.

## Step 4: Configure Offer Subvention Details

1. Enter the subvention details in the _Subvention Details_ page. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer#step-4-configure-offer-subvention-details).
2. After you complete the above details and click **Next**.

The _Preview Details_ page is displayed

## Step 5: Review of the Offer

The _Preview Details_ page summarizes the details you provided in Step 2 to Step 4.

1. Review all the configurations added before you make the offer available to your customers.
2. Click the **Edit** button to return back to the corresponding page and update the configuration.


<Image src="https://files.readme.io/0b82b32bea63aec925e5a31d7918397f489b0e59f19f187ba4e52790539de677-Screenshot_2025-06-03_at_6.04.05_PM.png" align="center" border={true} />


3. Click **Publish** to make it available to customers.

<br />
