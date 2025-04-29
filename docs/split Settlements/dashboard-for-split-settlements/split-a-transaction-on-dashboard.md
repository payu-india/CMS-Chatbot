---
title: Split a Transaction on Dashboard
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You can split a transaction by percentage or amount. This section describes how to split a transaction on Split Settlements Dashboard.

To split a transaction on Split Settlements Dashboard:

1. Select **Transactions** from the menu.

   The *Transactions Overview* page is displayed.
2. Click the **Actions** menu against the transaction and then select **Create Split** from the menu, similar to the following screenshot:

<Image align="center" className="border" border={true} src="https://files.readme.io/8e51d9fda36b2cb6a6f401d977db0e9d5787ae0c8e500b053a0988cb0aaaad4c-Screenshot_2025-02-17_at_11.22.56_AM.png" />

   The *Select Sub-Accounts and Split Configuration* page.

<Image align="center" className="border" width="412px" border={true} src="https://files.readme.io/93066d0bdb4a632dff60f559226786ed5eb031792a6378170410663422707c69-Screenshot_2025-02-17_at_11.24.34_AM.png" />

3. Select the sub-accounts or child merchants for the split from the **Select Sub Accounts for the Split** drop-down list. Use the check box to select one or more child merchants.
4. Select any of the following split types from the **Split Options** drop-down list:
   * Split By Absolute Amounts
   * Split By Percentage
5. Enter the split percentage or amount for **Parent** (your account).
6. Enter the split percentage or amount for each child merchant. For example, the split percentage specified for a parent and two sub-accounts.

<Image align="center" className="border" border={true} src="https://files.readme.io/7eda94f91a9ecadd9cc0082ec075befe358e611749524b85b9cc568b13c84603-split_sett_split_example.png" />

> 📘 Notes:
>
> * For Split by Percentage, you must ensure that the total split percentage entered in Step 5 and Step 6 is 100.
> * For Split by Amount, you must ensure that the total of the split amount entered in Step 5 and Step 6 is equal to the transaction amount (that you are trying to split).

7. Click **Proceed**.

   The *Review & confirm the Split* page is displayed.

<Image align="center" className="border" width="412px" border={true} src="https://files.readme.io/63ca53ec133f7c26bbfe2f2ceabd8849695a1434809f44917ba1c5655e74ce39-Screenshot_2025-02-17_at_11.29.25_AM.png" />

8. Click **Confirm**.

> 📘 **Note**:
>
> If you wish to update, click **Go back to edit** and perform Step 3 to Step 6.

A confirmation message is displayed.

<Image align="center" width="412px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/01/Split_Confirmation.png" />

If the split could not be created, an error message. "Split could not be created, please try again" message is displayed.
