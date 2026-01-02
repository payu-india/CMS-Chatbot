---
title: Manage Offers
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - PayU India Manage Offers
    - Manage Offers
    - Offers Management for PayU Checkout
  robots: index
next:
  description: ''
---
The _Offers Engine_ section of PayU Dashboard gives an overview of the offer performances in terms of GMV, discount offers, and live feed of transactions, which are also available for downloads.

The PayU Dashboard also provides a detailed list of all the offers and acts as a management tool for the same.

The following sections describe how to manage offers:

## View an Existing Offer Performance Details

To deep dive further into an offer performance, the Dashboard showcases the performances around GMV and transaction volume, along with the list of transactions for a particular offer.  

To view the performance details of an existing offer:

1. Select **Offers & Promotions** from the main menu.

The _Offers_ Overview page is displayed and the **Offers List** pane at the bottom.

<Image align="center" border={true} src="https://files.readme.io/d9c27255e1d6a33676f450c93f7e68bdbf4975d62c9eb5c615a934261029a44d-Screenshot_2025-06-06_at_9.45.01_AM_1.png" className="border" />

2. Click the drop-down list for the calendar view.

<Image align="center" border={true} src="https://files.readme.io/1b937c168a143d9cbeecc8fda294fa345ee7e4ce17b9797897e0c522b93f6876-Screenshot_2025-06-06_at_9.46.10_AM.png" className="border" />

3. Perform any of the following to view the summary of transactions:
   * Select **Today** to view the summary of transactions triggered for the day.
   * Select **Yesterday** to view the summary of transactions triggered yesterday.
   * Select **Past 7 days** to view the summary of transactions for the past week.
   * Select **Past 30 days** to view the summary of transactions for the past 30 days.
   * Click the **Custom Range** filter to choose the desired time frame. Select a particular date range, month and year from the drop-down list or you can use the next and previous buttons given on the top of the calendar view to navigate through the months.
4. Click **Apply**.

## Complete an Offer Details in Draft

When you are creating an offer, you can save as draft using the**Save as Draft & Exit button** button at the top-right corner and later complete the details.

To complete an offer details that was saved in draft earlier:

1. Navigate to the _Offers Overview_ page.

   The _Offers Overview_ page is displayed. In the **Offers List** pane, if any offers details are saved in draft, the **Drafted Offers** tab is displayed next to the **Published Offers** tab.

<Image align="center" border={true} src="https://files.readme.io/46b435d2e9694ca360e845773e9100a9a50a733f87734c7b133724c73384d076-Screenshot_2025-06-06_at_9.47.20_AM.png" className="border" />

2. Select the **Drafted Offers** tab.
3. Click the **Edit** button (pencil) in the **Actions** column for the offer that you wish to complete the details.

<Image align="center" border={true} src="https://files.readme.io/dae949079031f8a25fb12c2de7cf44d4b7f2182165f3d84dbd7d3f8677d40e41-dashboard-offers-draft-edit-selection.png" className="border" />

4. Follow these subsections of [Create an Instant Discount or Cashback Offer](doc:create-an-offer) to complete the details.

   The offer is published and can be found in the **Published Offers** tab.

## Update an Offer

After you create an offer and publish it to customers, you can update the following offer details:

* Basic details such as offer name & description, T&C, T&C URL, and valid to date.
* BIN list in case of cards, banks list for Net Banking, or wallets list for Wallets.

To update an existing offer:

1. Select **Offers Engine** > **Manage** from the menu on the left pane.

   The _Offers List_ page is displayed.

<Image align="center" border={true} src="https://files.readme.io/42dba0d373fadd714abfb9b058ce4d52f41de6958dc83c5bbd678e51be20d567-dashboard-offers-published-edit-selection.png" className="border" />

2. Click the **Actions** (**…**) menu and select **Edit**.

   The _Create New \<Offer Type> Offer_ page is displayed.

<Image align="center" border={true} src="https://files.readme.io/3b26103582ce85f37d5cc31b5f00526c0f977918cf18e21e1ac8eaf02f11d153-Screenshot_2025-06-06_at_9.54.13_AM.png" className="border" />

3. Click the **Edit** button (pencil) on the **Basic Details** pane.

   The _Basic Details_ pop-up page is displayed.

<Image border={false} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/04/Screenshot-2023-04-08-at-1.41.55-PM-1024x946.png" />

4. Update the following basic offer details. For more information, refer to  [Create an Instant Discount or Cashback Offer](doc:create-an-offer).
   * Offer Title and Description
   * Offer Period: The date range in the Offer Period field can only be postponed but not preponed.
   * Terms & Conditions

5. Click **Save & Proceed**.

   After you update the basic details of the offer, you can check the changes done using Audit Trail.

6. Click the **Edit** button (pencil) and update the details. The following fields can be updated on the Of. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer).
   * Discount Per Transaction
   * Minimum and Maximum Transaction Amount
   * All the fields in the **User Limits** section.
   * All the fields under the **Additional Options** section except for the **Always use card identifier to set user limits as required** field.

7. Click **Save & Proceed**.

8. Click any of the payment methods to add or update the details for each of the **Payments Options** section. For more information, refer to  [Create an Instant Discount or Cashback Offer](doc:create-an-offer)..

After you update the basic details of the offer, you can check the audit trials for the changes made to an existing offer.

9. Select the **Go Back to Dashboard** option at the top-right corner to go back to the _Offers Overview_ page.

## Pause an Offer

You can pause an offer temporarily for customers and resume it back when required. If you want to deactivate the offer permanently for your customers, refer to [Deactivate an Offer](https://docs.payu.in/docs/manage-offers/#deactivate-an-offer).

To pause an existing offer:

1. Select **Offers Engine** > **Manage** from the menu on the left pane.

   The _Offers_ Overview page is displayed and the **Offers List** pane at the bottom.

2. Click the **Actions** (**…**) menu and select **Pause**.

   A confirmation message is displayed.

3. Click **Confirm** to pause the offer.

## Resume a Paused Offer

If you had paused an offer as described in [Pause an Offer](https://docs.payu.in/docs/manage-offers/#pause-an-offer), you can resume it as described in this section when required.

To resume a paused offer:

1. Select **Offers Engine** > **Manage** from the menu on the left pane.

   The _Offers_ Overview page is displayed and the **Offers List** pane at the bottom.

2. Click the **Actions** (**…**) menu and select **Resume**.

   A confirmation message is displayed.

<Image align="center" border={true} width="412px" src="https://files.readme.io/19c3289de3d7cb0716a87bb69cd8fb2a42f0e88741a8a40adb1eedc1593c3a7e-Screenshot_2025-06-06_at_9.57.53_AM.png" className="border" />

3. Click **Confirm** to pause the selected offer.

## Clone an Offer

You can clone an existing offer and update the details as required. After you clone an offer, the cloned offer is listed in the **Drafts** section.

To clone an existing offer:

1. Select **Offers Engine** > **Manage** from the menu on the left pane.

   The _Offers_ Overview page is displayed and the **Offers List** pane at the bottom.

2. Click the **Actions** (**…**) menu and select **Clone**.

   A confirmation message is displayed.

<Image align="center" border={true} width="412px" src="https://files.readme.io/262998c5f0c8b972b05c352692e3896114c63b114fb967dbc2e8da506783929e-Screenshot_2025-06-06_at_9.58.47_AM.png" className="border" />

3. Click **Clone Offer** to pause the selected offer.

   The cloned offer is listed in the **Drafts** section.

4. Update the offer details as required. For more information, refer to [Update an Offer](#update-an-offer).

## Deactivate an Offer

When you want to deactivate an offer due to some unavoidable reasons, you can deactivate an offer as described in this section. If you want to pause an offer temporarily, refer to [Pause an Offer](https://docs.payu.in/docs/manage-offers/pause-an-offer).

To deactivate an existing offer:

1. Select **Offers Engine** > **Manage** from the menu on the left pane.

   The _Offers_ Overview page is displayed and the **Offers List** pane at the bottom.

2. Click the **Actions** (**…**) menu and select **Deactivate**.

   A confirmation message is displayed.

<Image align="center" border={false} width="422px" src="https://files.readme.io/28a6790c5c0cb71c1326e48e5fc6650385675c0cea6d3598daaf9c63fdfa6fc6-Screenshot_2025-06-06_at_9.59.48_AM.png" />

3. Click **Deactivate Offer** to close or deactivate the selected offer.
