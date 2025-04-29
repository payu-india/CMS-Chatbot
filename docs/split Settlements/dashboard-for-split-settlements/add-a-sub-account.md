---
title: Add a Sub-Account
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
Adding a sub-account, sub-merchant or child merchant involves the following major steps:

* [Step 1: Basic Details](#step-1-basic-details)
* [Step 2: Verify PAN](#step-2-pan-verification)
* [Step 3: Business Details](#step-3-business-details)
* [Step 4: Sub-Account Bank Details](#step-4:-sub-account-bank-details)
* [Step 5: Verifying Authority Details](#step-5-verifying-authority-details)
* [Step 6: Additional Documents](#step-6-additional-documents)

> 📘 Notes:
>
> * There is no mail sent or intimated to sub-merchant when you add a sub-merchant using this procedure.
> * PayU will verify the documents submitted in [Step 6: Additional Documents](#step-5-additional-documents) and activate the sub-account by two working days. If you encounter any issues, contact your PayU Account Manager or [PayU Support](https://help.payu.in).

The following describes the procedure to add a sub-account:

## Step 1: Basic details

1. Select **Split & Supplier Payments** on the menu.

   The *Manage Sub-accounts* page is displayed.

<Image align="center" src="https://files.readme.io/1c5326a2b49ee5f7a5910c5a6cf93dbc1a4b662354c88359faa4b6e4c75f5b0c-Screenshot_2025-02-17_at_10.33.30_AM.png" />

2. Click **Add Sub-Merchant** at the top-right corner and select **Single Merchant**.

   The *Add a Child Merchant* page is displayed.

<Image align="center" src="https://files.readme.io/69f73c5cdf93cbb5dbc4f25461bd492ff77625157445e784b6289d8ed0aaaff1-dashboard-add-subacct-step1.png" />

3. Enter the details as specified in the following table:

| **Field**         | **Description**                                                                                                                                    |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sub-merchant Name | Enter the business account name in this field. The name entered in the field will be printed in the various reports generated from PayU Dashboard. |
| Mobile No         | Enter your 10-digit mobile number in this field.                                                                                                   |
| Email ID          | Enter your business email ID linked to this Dashboard in this field.                                                                               |

4. Click **Proceed**.

   The page is refreshed to display the other panes to complete the sub-account details.

<Image align="center" src="https://files.readme.io/02d8340a81899274a610963e3b8925224b01e2b2f0fb6f58f6d65a12e7e251ca-dashboard-add-subacct-step2.png" />

## Step 2: PAN verification

1. Enter your business PAN card number in the **Business PAN Card Number** field. If your business is a sole proprietorship, enter your personal PAN card number.
2. Enter your date of birth or company’s date of incorporation in the **Date of Birth/Date of Incorporation** field.
3. Click **Proceed to Verify**.

   A pop-up page is displayed to choose the business entity.

<Image align="center" className="border" width="350px" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/07/split_PAN_proprietorship.png" />

4. Select your business entity type from the drop-down and click the **Confirm I am\<your business name>** button. Where \<your business name> is substituted with the name you entered in the **Business PAN Card Number** field at Step 2.

   The **Tell us a little bit about your business** pane is displayed.

<Image align="center" src="https://files.readme.io/7f849b8719d73801ff4350264123b3b8c83121787d7f9759a63efe452c7d19dd-dashboard-add-subacct-step4.png" />

## Step 3: Business details

1. Enter the details on the **Tell us a little bit about your business** pane as specified in the following table:

| Field                              | Description                                                                      |
| ---------------------------------- | -------------------------------------------------------------------------------- |
| Business Category                  | Select your business category from this drop-down list.                          |
| GSTIN                              | Enter your GSTIN if your business has GSTIN.                                     |
| Monthly expected Sales (in Rupees) | Enter the expected sales from your business per month (in rupees) in this field. |

2. Click **Proceed**.

   The **Step 4: Enter Bank Details\<your name>** pane is displayed.

<Image align="center" src="https://files.readme.io/66ce9d738e5cb188328799bd36ac2aa51e1780b9f034c5507562fc7c42cd1ed8-Screenshot_2025-02-17_at_10.42.38_AM.png" />

## Step 4: Bank details

1. Enter the sub-account bank details as described in the following table:

> **Note**: In case you do not have sub-account or child merchant bank details or if you skip the step, follow the steps as described in [Step 2: Update bank details](ref:create-child-merchant-api#step-2-update-bank-details) of [Create Child Merchant API](ref:create-child-merchant-api).

| Field               | Description                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------- |
| Bank Holder Name    | Select the name of the beneficiary from the drop-down list.                                             |
| Bank Account Number | Enter the account number of the beneficiary.                                                            |
| IFSC Code           | Enter the bank branch IFSC code or click the **Search IFSC** option to search and select the IFSC code. |

2. Click **Connect Bank Account**.

   The **Step 5: Verifying Authority Details** pane is displayed.

<Image align="center" src="https://files.readme.io/147562f900b23affab21dbbf51d2101118bb35d7b966c39e37c4af1ce9335a27-split_sett_dashboard_onboarding_verify_auth_details.png" />

## Step 5: Verifying Authority Details

1. Enter the signing authority details of your company as described in the following table:

| **Field**                     | **Description**                           |
| ----------------------------- | ----------------------------------------- |
| Signing Authority Name        | Enter the signing authority name.         |
| Signing Authority Designation | Enter the signing authority designation.  |
| Signing Authority Email ID    | Enter the signing authority email-ID.     |
| Signing Authority Phone No    | Enter the signing authority phone number. |

2. Click **Connect Bank Account**.

The **Step 6: Additional documents required** pane is displayed.

## Step 6: Additional Documents

> 📘 Notes:
>
> * Upload signed schedule C document through your parent merchant or Dashboard
> * E-Sign Schedule C through OTP, triggered by parent merchant
> * If bank account verification fails, then cancelled cheque needs to be uploaded

1. Select any of the following options from the **Bank Account Proof of** drop-down list and upload the proof document using the **Upload Document** Select a scanned copy or photo of your PAN card:
   * Passport
   * Bank Passbook
   * Canceled Cheque
   * Bank Verification Letter

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/07/split_add_subacct_documents-1024x423.png)

2. Upload the Schedule C document using the **Upload Schedule C** field.  Also, you can ask your sub-merchant to e-sign the schedule C addendum using the **Send Email to Child** button.
3. Click **Submit Documents**.

   After the sub-account bank details are submitted, the following confirmation message is displayed.

<Image align="center" className="border" width="350px" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/01/Split_Payments_Subbacct_Added-_Successfully.png" />

> 📘 Verification of Docs:
>
> PayU will verify the documents and activate the sub-account by two working days. If you encounter any issues, contact your PayU Account Manager or [PayU Support](https://help.payu.in).

   If the sub-account bank details are not entered, the following page is displayed so that you can share it with your merchant.

<Image align="center" width="350px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/01/Split_Payments_Create_SubAcct_acct_details_last_Step.png" />
