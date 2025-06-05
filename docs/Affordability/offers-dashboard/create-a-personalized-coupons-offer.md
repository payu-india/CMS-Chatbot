---
title: Create a Personalized Coupons Offer
deprecated: false
hidden: false
metadata:
  robots: index
---
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
3. Select the discount type as **Personalised  Coupons**.

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

1. Click **or** button or **and** button and accordingly enter the following details to configure the milestone conditions in the **Set Milestone Conditions** section:

   * Enter the number of transactions required from the customer in the **Number of Transactions Required** field.
   * Configure the total amount to spent by a customer in the **Set Total Amount to be Spent** field
2. Select the **Flat Discount** or **Percentage** tab in the **Offer Type** section to specify the discount is in terms of a flat discount or percentage of the transaction amount.
3. Enter the following details on the *Set Offer Rules* page.

   | **Field**                                               | **Description**                                                                    |
   | ------------------------------------------------------- | ---------------------------------------------------------------------------------- |
   | Discount per transaction/Offer Percentage               | Specify the value that has to applied in in terms of discount or discount in flat. |
   | Minimum transaction amount & Maximum transaction amount | Specify the threshold or range for a transaction to be applicable for the offer.   |

   #### Offer Usage Guidelines

   <Table>
     <thead>
       <tr>
         <th>
           **Field**
         </th>

         <th>
           **Description**
         </th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>
           User Limits
         </td>

         <td>

         </td>
       </tr>

       <tr>
         <td>
           Set the frequency for your customers to use this offer
         </td>

         <td>
           Select any of the following options from the drop-down list to specify the maximum number of transactions the user can avail this offer:

           * **Set unlimited**: Users can avail the offer for unlimited transactions.

           - **Custom**: Specify the custom limit up to which the users can avail the offer.
         </td>
       </tr>

       <tr>
         <td>
           Set Budget per user
         </td>

         <td>
           Click this toggle button (if required) and then enter the budget amount per user.
         </td>
       </tr>

       <tr>
         <td>
           Reset User Limits
         </td>

         <td>
           Select any of the following options from the drop-down list to reset the user limit for specified frequency:

           * **Every Day**: Reset the user limit everyday
           * **Every Week**: Reset the user limit every week
           * **Every Month**: Reset the user limit every month
           * **Custom**: Specify the custom frequency after which the user limit is reset
         </td>
       </tr>
     </tbody>
   </Table>
4. After you complete the above details and click **Next**.

   The *Set Offer Subvention Details* page is displayed.

## Step 4: Configure Offer Subvention Details

1. Enter the subvention details in the *Subvention Details* page. For more information, refer to refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer#step-4-configure-offer-subvention-details).
2. After you complete the above details and click **Next**.

The *Preview Details* page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/10f77e255c1847f3cca70a9b3fbc38a89648d9750a6557daef7baae4aad55018-dashboard-milestone-offer-preview.png" />

## Step 5: Review of the Offer

The *Preview Details* page summarizes the details you provided in Step 2 to Step 4.

1. Review all the configurations added before you make the offer available to your customers.
2. Click the **Edit** button to return back to the corresponding page and update the configuration.
3. Click **Publish** to make it available to customers.