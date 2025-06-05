---
title: Create a Milestone Offer
deprecated: false
hidden: true
metadata:
  robots: index
---
Milestone offer enables you to reward your customers when they reach a spending milestone on your eCommerce website or app.

> 📘 Notes
>
> * **Customer Login Requirement**: Customers must be signed into their accounts to view and monitor their progress toward milestone offers.
>
> * **Offer Compatibility**: Milestone offers are designed to work alongside other payment offers and discounts during the checkout process.
>
> * **Calculation Method**: Milestone offers are calculated based on the final payable amount—this means the total is determined after all applicable offers have been applied, accurately reflecting the actual amount customers pay.
>
> * **Post-Publication Restrictions**: After publishing a milestone offer, the core conditions in step 3 (Offer Rules) cannot be modified, including both the required number of transactions and the total spending amount.

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
3. Select the discount type as **Milestone Offer**.

The *Basic Offer Details* page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/9bab18901c8b403e85eab564ea7ea7d82a0a7b40c39d81ede7c6b6aa14f0517b-dashboard-milestone-offer-basic-details.png" />

5. Add the basic details. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer).
6. Select **Instant Discount** or **Cashback** from the **Apply Offer as** field so the offer is applied accordingly.
7. After you complete the above details and click **Next**.

   The *Payment Options* page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/aa1809a52ebd6df2165e992c2a16037d6b4e6ca160393f5519db9e25dca8421f-dashboard-milestone-offer-rules.png" />

> 📘 Note
>
> When you are creating an offer, you can choose to save the incomplete offer details in the Draft state using the **Save as Draft & Exit** button at the top-right corner and publish it later.

## Step 2: Configure payment modes

1. Configure the payment modes. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer#configure-payment-modes).

> 📘 Note:
>
> For this offer, ensure that the customer's phone number is included in the **Collect Payment** (\_payment) API request for this offer.

1. Click **Next**.

The *Offer Rules* page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/fdf77020936a86f2f3050ab3acac1265a7a9670ada69c04fc324d10fbfbcc386-dashboard-milestone-offer-rules-page.png" />

## Step 3: Include the Offer rules

1. <br />
2. <br />
3. After you complete the above details and click **Next**.

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