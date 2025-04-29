---
title: Referral Onboarding
excerpt: >-
  You can onboard your clients yourself on their behalf from the Partner
  Dashboard. Merchant has to accept the Service Agreement. After being
  onboarded, merchants can complete their profiles and start enjoying the
  services offered by PayU.
deprecated: false
hidden: false
metadata:
  title: Referral Onboarding using Partner Portal
  description: >-
    Learn how to onboard referrals using the PayU Partner Portal. Follow our
    comprehensive guide to register and manage referral merchants, streamline
    the referral process, and maximize your partnership benefits. Simplify your
    referral onboarding with PayU today
  keywords:
    - PayU referral onboarding using portal
    - PayU partner portal referral
    - Onboard referrals with PayU Partner Portal
    - PayU partner referral process using portal
    - Referral merchant onboarding PayU
    - ' PayU referral registration using portal'
    - Add referral merchants using Portal
    - PayU referral program onboarding using Portal
    - PayU partner referral steps using portal
    - PayU affiliate onboarding using portal
    - How to refer merchants on PayU using Portal
  robots: index
next:
  description: ''
---
You will find an option available on the Partner Dashboard as Refer a Merchant. Using this, you can either onboard a single merchant or multiple merchants with a single click. Enter your merchant’s primary details, and you are done with creating a merchant account. You can onboard a merchant or multiple merchants as described in the following sections:

* [Add a Referral Merchant](#add-a-referral-merchant)
* [Add Multiple Referral Merchants](#add-multiple-referral-merchants)

## Add a referral merchant

This section describes the procedure add a single referral merchant. 

To onboard a referral merchant:

1. Log in to your partner account.

   On the left pane, the **Add Single Merchant** and **Add Multiple Merchant** options are displayed under **Refer a Merchant**.

2. Click **Add Single Merchant** on the left pane to add a single merchant.

![Refer\_merchant](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-188.png)

```
 The _Refer a merchant_ pop-up page is displayed.
```

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-189.png)

3. Enter the following merchant’s details:

| **Field**             | **Description**                                                                     |
| --------------------- | ----------------------------------------------------------------------------------- |
| **Name**              | Enter the name of the merchant.                                                     |
| **Email Address**     | Enter the email address of the merchant.                                            |
| **Phone Number**      | Enter the merchant’s phone number.                                                  |
| **Payment Service**   | Enter the payment service from the drop-down list that the merchant will use.       |
| **Business Category** | Select the business category from the drop-down list to which the merchant belongs. |

4. Click **Next** to proceed further.

   The *Merchant Plan* page is displayed.

<Image align="center" width="350px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/10/Screenshot-2021-10-06-at-12.11.07-PM-474x1024.png" />

5. Click **Add Merchant** button to add the merchant with the **Standard** plan (free), where the transaction charges listed on the page are applicable. Before adding, check default merchant plan details.

> **Note**: Select the **Click Here** option at the bottom of the **Merchant Plan** page to see the benefits (similar to the following screenshot) if you are a registered partner. You can avail of these benefits only if you are a registered partner. For more information, contact PayU Support.

<Image align="center" width="450px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/10/Screenshot-2021-10-06-at-12.13.59-PM-1024x878.jpg" />

The referral merchant gets added to the Home page.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/10/Screenshot-2021-10-06-at-12.23.38-PM-1024x800.png)

6. Click **Complete Profile** to complete the merchant’s profile.

You will be redirected to the *Complete Your KYC* page as in PayU Dashboard. For more information, refer the to [Activate Account](doc:complete-your-kyc) section of the *PayU Dashboard User Guide*.

## Add multiple referral merchants

You can upload multiple referral merchants by entering their details in the provided template. If you want to add a merchant (single), refer to [Onboarding APIs](ref:onboarding-apis)

To add multiple referral merchants:

1. Log in to your partner account.

   On the left pane, the **Add Single Merchant** and **Add Multiple Merchant** options are displayed under **Refer a Merchant**.

![Refer\_merchant](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-188.png)

2. Click **Add Multiple Merchants** on the left pane to add multiple merchants.

   The *Add Multiple Merchants* pop-up page is displayed.

<Image align="center" className="border" width="422px" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/10/Screenshot-2021-10-06-at-10.23.59-PM-761x1024.png" />

3. Select the **Download Sample Template** option to download the spreadsheet template in which you need to fill in the details of multiple merchants.

> **Note**: If you try to upload using any other spreadsheet or template, the upload will be successful only if the columns (marked mandatory and same order) as in the template mentioned in Step 3.

4. Click **Browse** to select the spreadsheet containing the multiple merchant details.

> **Note**: The values for the following columns in the spreadsheet are mandatory. You can fill in the other details.

* Merchant Name
* Merchant Email
* Merchant Phone

5. Click **Submit**.

## **Complete your Referral Details**

You have to complete the following sections (in the following sequence) on the KYC page to complete KYC for your merchant with PayU:

## **Navigate to the KYC page for a Referral**

To open the KYC page for a referral:

1. Log in to Partner Portal.

The list of referrals are displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Screenshot-2022-04-25-at-11.53.01-AM-1024x835.png)

1. Click **Complete Profile** next on the referral entry that you wish to complete KYC details.

   A page is displayed with a message, “Your account is active. Complete your full KYC.” The **PAN Verification** section is displayed requesting your PAN details.

## **PAN Verification**

To verify your PAN on the **PAN verification** section:

1. Enter your PAN in the **Business PAN Card** field.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-25-at-7.17.19-PM-1024x705.jpg)

2. Click **Proceed to Verify**.

After the PAN is verified, the section name gets updated to “Your PAN is verified. Way yo Go!” and **Tell us a little bit about your business** section is enabled.

## **Tell us a little bit about your business**

To enter information on your business in the **Tell us a little bit about your business** section:

1. Select your business category from the **Business Category** drop-down list.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-24-at-7.22.55-PM-1-1024x697.jpg)

2. Select your business sub category from the **Business Sub Category drop-down list.**
3. Enter your GSTIN in the **GSTIN** field (optional).
4. Enter the estimated sales or revenue per month of your business in the **Expected Sales per month** field.
5. Click **Proceed**.

The section name gets updated to **Business details submitted successfully**. The **Enter Bank details of\<your name>** section is enabled, where \<your name > is substituted with your name as in PAN.

## **Enter Bank Details**

To enter your bank details on the **Enter bank details of\<your name>** section:

1. Enter your account number in the **Bank Account Number** field.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-24-at-7.23.30-PM-1024x709.jpg)

2. Enter your bank IFSC code in the **IFSC Code** field. You can find the IFSC code on the cheque book provided by your bank.
3. Click **Connect Bank Account**.

## **How do you Wish to Accept Payments**

To specify how do wish to accept payments from your customers, select any of the following on the **How do you wish to accept payments** section:

* **On my website/app**: Enter the URL for the following fields:
  1. Website
  2. Android App
  3. iOS App

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-25-at-10.07.25-PM-1024x462.jpg" />

> **Note**: You have to ensure that the list of pages are created on your website as indicated under the **Important – Your website must have the following pages**.

* **I don’t have a website/app**: You can use the following features of Dashboard to collect payments if you don’t have website or app:
  1. [Payment Links](doc:payment-links-dashboard)
  2. [Payment Invoices](doc:invoices-dashboard)
  3. [Payment Buttons](doc:payment-buttons-dashboard)

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-25-at-9.46.50-PM-1024x343.jpg" />

Click **Next** to proceed to the **Verify signing authoring details** section.

The section title gets updated to “Signing authority details captured” and the **Verify signing authority details** section is enabled.

## Verify signing authority details

To verify your business signing authority details in the **Verify signing authority details** section:

1. Verify the details in the following fields:
   * Signing Authority Name
   * Signing Authority’s PAN card number
   * Signing Authority Email ID

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-24-at-7.23.49-PM-1-1024x657.jpg)

2. Update the email ID in the **Signing Authority Email ID** field if required.
3. Click **Proceed to KYC**.

The section name gets update to “Signing authority details captured” and the **Complete the KYC** section is enabled.

## Complete the KYC

To fetch your KYC documents automatically from the cKYC/Aadhaar database or upload the documents manually, select any of the following options:

* **Fetch from cKYC**: To fetch your automatically from the cKYC database:
  1. Enter your date of birth or company’s incorporation date in the **Date of Birth/ Date of Incorporation** field.
  2. Select the **I hereby authorize PayU …** check box to authorize PayU to fetch the KYC documents from cKYC.
  3. Click **Submit**.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-26-at-8.23.06-PM-1024x441.jpg)

* Fetch from Aadhaar: To fetch your automatically from the Aadhaar database:
  1. Select the **By proceeding I accept Aadhar Terms and Conditions** check box to accept Aaadhar Terms & Conditions.
  2. Click **Submit**.

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-26-at-8.23.17-PM-1024x611.jpg" />

* Upload documents manually: To upload the KYC documents manually:
  1. Verify the details in the following fields:
     * Name
     * Address
     * Postal Code
     * City
     * State
  2. Update the **Address** and **Postal Code** fields if required.
  3. Choose **Yes** in the **Do you have a different Operating Business Address ?** field if the business address is different and enter the following details:
     * Address
     * Postal Code
  4. Click **Confirm and Proceed**.

An additional section, **Additional documents required** is displayed. For more information, refer to [Additional Documents Required.](#additional-documents-required)

## Additional documents required

To submit the documents manually:

<Image align="center" className="border" width="450px" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-26-at-8.36.42-PM_defaced-1-1024x396.jpg" />

1. Select each of the following drop-down list and select the document by clicking **Select file from your library**:
   * **PAN Card**: Select a scanned copy or photo of your PAN card.
   * **Address Proof**: Select a scanned copy or photo of a government issued ID cards such as Passport or Driving License.
   * **Government issued certificate copy** (only if requested): Select your Income Tax returns scanned document (80G).
2. Click **Submit Documents**.

A message similar to the following is displayed at the bottom right-corner of your browser.

<Image align="center" width="3px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-26-at-9.07.24-PM.png" />

<Image align="center" className="border" width="350px" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/Screenshot-2021-09-26-at-9.07.24-PM.png" />
