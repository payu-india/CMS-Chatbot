---
title: Onboard Merchants Manually
deprecated: false
hidden: false
metadata:
  robots: index
---
Onboard merchants manually through the PayU Partner Portal. Complete the steps below to register as a partner, configure your app, log in, refer merchants, and track incentives.

## Step 1: Register a Partner Account

You need to create a partner account in the Test and Production environment to become a partner. A partner account connects you with PayU and enables access to Partner Dashboard and merchant onboarding.

To create a Partner Account:

1. Navigate to the following PayU Affiliate Partner Program URL:

   [https://partner.payu.in/](https://partner.payu.in/)

   The PayU Affiliate Partner Program page is displayed.


<Image src="https://files.readme.io/40a589301996024d72b3fa6404ade344c97b6ff98f8bc80a644c3405f6c9cd32-Screenshot_2025-08-26_at_2.40.32_PM.png" align="center" border={true} />


2. Click **Become a Partner**.
3. Enter your email address in the **Enter Email** field and click **Next**.


<Image src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/image-21-1024x512.jpg" align="center" border={true} />


The _Tell us more about yourself_ page is displayed.


<Image src="https://files.readme.io/82a984c583e59fb8a8d93aa1426accf7078fe667fae8e047d997c7baa7a2a234-Screenshot_2025-08-26_at_2.39.31_PM.png" align="center" border={true} />


4. Provide the details for the fields as described in the following table:

| **Field**          | **Description**                                                                                                                                                                                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Enter Name**     | Enter your name in this field.                                                                                                                                                                                                                                                             |
| **Phone Number**   | Enter your mobile phone number in this field. PayU will send an OTP on this number for verification.                                                                                                                                                                                       |
| **Enter Password** | Enter the password that you wish to use while logging into your merchant account with PayU. Your password must meet these requirements: at least eight characters; at least one uppercase alphabet; at least one lowercase alphabet; at least one numeral; at least one special character. |

5. Click **Next**.

   The OTP is sent to the mobile number you specified in the **Phone Number** field.

6. Enter the OTP sent to that mobile number.

7. Click **Verify Mobile**.

   Registration for the partner account in PayU is complete.

<Callout icon="📘" theme="info">
  **Note:** If you have already registered for the PayU Partner Program using the entered phone number, the following message is displayed:

  _“Mobile Number already exists with PayU. Please continue with your old password to add merchant account.”_
</Callout>

### Complete your profile on Partner Portal

After registering as a partner, complete your profile. Completing your profile is mandatory to generate your partnership agreement with PayU.

The **Profile** tab contains the following sections:

- [General Details](#general-details)
- [Business Details](#business-details)
- [PAN Details](#pan-details)
- [Bank Details](#bank-details)

If you have not completed your profile, the **Get Paid > Complete your onboarding** tile is displayed on the top after you log in. Click **Get Paid** to complete your profile.

Or click your profile photo at the top-right corner and select **My Profile** from the drop-down menu.


<Image src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Screenshot-2022-04-25-at-9.59.59-AM.png" align="center" width="250px" />


The **Profile** tab is displayed with _Fill the details below to generate your partnership agreement_ as the title.

#### General Details

The details on the **General Details** pane are automatically updated based on the details you filled in during registration. You can update these details if required.

#### Business details

1. Expand the **Business Details** pane.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Screenshot-2022-04-25-at-9.56.40-AM-1024x699.png)

2. Select your business registration type from the **Select Business Registration Type** drop-down list.
3. Enter your business name in the **Business Registration Name** field.
4. Enter your business registration address in the **Business Address** field.
5. Enter the PIN code in the **Pincode** field.
6. Enter your GSTIN in the **GSTIN** field (optional).
7. Select the domain from the **Domain** drop-down list.
8. Click **Submit**.

#### PAN details

1. Expand the **PAN Details** pane.


<Image src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Screenshot-2022-04-25-at-10.21.02-AM-1024x744.png" align="center" border={true} />


2. Enter the name in the **Name on PAN Card (PAN card of the signing authority)** field.
3. Enter your PAN number in the **Number on PAN Card** field.
4. Click **Submit** to verify.

#### Bank details

1. Expand the **Bank Details** pane.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Screenshot-2022-04-25-at-10.24.37-AM-1024x876.png)

2. Enter your business name in the **Account Holder’s Name (Same as Registered Business Name)** field.
3. Enter your account number in the **Bank Account Number** field.
4. Confirm your account number in the **Re-enter Bank Account Number** field.
5. Enter your bank IFSC code in the **IFSC Code** field. Search the IFSC code using the **Search IFSC** option, or find the IFSC code on the cheque book provided by your bank.
6. Click **Submit**.

For the full standalone guide, see [Register a Partner Account](doc:register-a-partner-account).

## Step 2: Configure URLs and Logo

Configure the following:

- URLs required to redirect to your partner platform website after merchant registration
- Company logo displayed on the left side of the merchant dashboard

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/03/merchant_dashboard_logo_placeholder-1024x476.png)

To configure the URLs and brand logo:

1. Log in at [partner.payu.in](https://partner.payu.in/) and navigate to the user menu.
2. Click your profile picture on the top-right corner and select **My App** from the drop-down menu.


<Image src="https://files.readme.io/b3e8c99125068fda5648febbd3ccbb08d8a22074d8170d447e5f264d10596dfe-Screenshot_2025-08-26_at_2.45.17_PM.png" align="center" />


<br />


<Image src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/03/Screenshot-2022-03-31-at-5.16.27-PM-1.png" align="center" width="422px" />


3. Expand the **Application Details** pane (if required).


<Image src="https://files.readme.io/08f4ed2da70075a2c0d553a2e68667d7012a97ce375da6581972462b3cb10896-partner_portal_aupdate_app_details.png" align="center" border={true} />


4. Update the following details to complete your app registration:

| **Field**           | **Description**                                    | **Example**                                      |
| ------------------- | -------------------------------------------------- | ------------------------------------------------ |
| Application name    | Enter your application name.                       | PayU Payments Pvt. Ltd.                          |
| Application website | Enter your application website.                    | [https://www.payu.in/](https://www.payu.in/)     |
| Redirect URL        | URL used to redirect back to the partner platform. | [https://www.xyz.in/](https://www.xyz.in/)       |
| Policy Page URL     | Link to your privacy policy.                       | [https://policy.xyz.in/](https://policy.xyz.in/) |

5. Click **Submit**.
6. Verify your identity with your password after submission so the details are updated.
7. Expand the **Branding Details** pane.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Screenshot-2022-04-01-at-12.00.45-PM-1024x644.png)

8. Click **Browse** in the **Add a brand logo** field and select a brand logo.

<Callout icon="📘" theme="info">
  **Note:** The brand logo should be JPG/JPEG, less than 5 MB, and 90 × 90 pixels.
</Callout>

9. Click the colour chooser in the **Pick color** field for the theme.

For the full standalone guide, see [Configure URLs and Logo](doc:configure-urls-and-logo).

## Step 3: Log in to Partner Portal

To log in to your Partner Account:

1. Navigate to the following PayU Affiliate Partner Program URL:

   [https://partner.payu.in/](https://partner.payu.in/)

   The PayU Affiliate Partner Program page is displayed.


<Image src="https://files.readme.io/40a589301996024d72b3fa6404ade344c97b6ff98f8bc80a644c3405f6c9cd32-Screenshot_2025-08-26_at_2.40.32_PM.png" align="center" border={true} />


2. Click **Log In**.

   The _Enter your email to create account or login_ page is displayed.


<Image src="https://files.readme.io/cdb7a5fe9c981c6c287f3410a3d5d10b27810eb52429aa7f1e0c0c9bac7f39fa-Screenshot_2025-08-26_at_2.53.16_PM.png" align="center" border={true} />


3. Enter your email address in the **Enter Email** field and click **Next**.

   A page requesting your password is displayed.

<Callout icon="📘" theme="info">
  **Note:** If you do not have an account or are not registered, the _Tell us more about yourself_ page is displayed. For more information, see [Step 1: Register a Partner Account](#step-1-register-a-partner-account).
</Callout>

4. Enter your password in the **Enter Password** field and click **Login**.

<Callout icon="📘" theme="info">
  **Note:** If you forgot your password or wish to log in using OTP, click **Login with OTP**. Enter the OTP sent to your registered mobile number in the **Enter OTP** field and click **Verify Mobile**.
</Callout>

The Partner Dashboard page is displayed.


<Image src="https://files.readme.io/e898a8e39d8272497e4680710b460e75091e1968eac96c8a303fd128f873d835-Screenshot_2025-08-26_at_2.54.57_PM.png" align="center" border={true} />


## Step 4: Track Incentives

You can view your incentive plan and manage incentives on the **My Incentives** tab of the Partner Portal.

<Callout icon="📘" theme="info">
  **Note:** Your net incentive is: **(Client TDR – Base Rate) × Transaction Value**, where Client TDR is the rate given to your referrals.
</Callout>

### View your incentive plan

PayU provides incentives for onboarding merchants and for payments made by customers through your merchants.

1. Log in to Partner Portal.
2. Click your profile picture at the top-right and select **Incentive Plan** from the drop-down menu.

![](https://files.readme.io/b3e8c99125068fda5648febbd3ccbb08d8a22074d8170d447e5f264d10596dfe-Screenshot_2025-08-26_at_2.45.17_PM.png)

The _Here is your incentive plan_ page is displayed.


<Image src="https://files.readme.io/d17717449085d1ce7f42f7077b8658998a5007e4685babd8ef5261ad898db41a-partner_portal_incentive_rates_list.png" align="center" border={true} />


The base rate is listed for various payment methods.

### View your incentives

Incentives refresh at the end of the day. To view incentives for a custom period, see [View incentives for a custom period](#view-incentives-for-a-custom-period).

1. Perform any of the following:
   - Select the **My Incentives** tab on top.
   - Click your profile picture on the top-right corner and select **My Incentives** from the drop-down menu.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Screenshot-2022-04-25-at-12.16.19-PM-1024x823.png)

2. Select any of the following tabs for different views of incentives:
   - **My Incentives**
   - **Merchant Incentives**


<Image src="https://files.readme.io/c34a9f797d18a802dcd03953b6b3fb2593a1eefc7b39d8f88bd392f04dcf2fa4-partner_portal_incentives_view.png" align="center" border={true} />


### View the incentive details

To view specific incentive details, including the settlement breakup:

1. Enter the merchant MID or merchant name in the search column and click **Search**.
2. Select the hamburger menu on the incentive entry and select **View Details**.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Screenshot-2022-04-25-at-12.16.19-PM-1-1024x157.png)

<Callout icon="📘" theme="info">
  **Note:** You can export the detailed settlement record to PDF using the **Download Details** option on the hamburger menu.
</Callout>

### View incentives for a custom period

The **My Incentives** tab shows incentives for the past seven days by default. You can select a date range, month, or year using the calendar view.

1. Click **Calendar** to open the calendar view.
2. Select any of the following options:
   - Today
   - Yesterday
   - Past 7 days
   - Past 30 days
3. Click **Apply** to view the results.

## Managing Users

You can invite users and provide permissions to manage or maintain your Partner Portal. You can perform the following to manage users:

### Add a User

To add a user on Partner Portal:

1. Click your profile picture on the top-right corner and select **Invite a user** from the drop-down menu.

The _My Users_ page is displayed.


<Image src="https://files.readme.io/3fb3cce6908d85f492a0a9e040c932b6083f926f0b35bc427c40b741887688f1-partner_portal_add_user.png" align="center" border={true} />


<br />


<Image src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Screenshot-2022-04-25-at-11.00.43-AM-1024x568.png" align="center" width="450px" />


2. Click **Add User** from the left pane.

   The _Add User Details_ pop-up page is displayed.


<Image src="https://files.readme.io/d99487df22adf33d23ddb38c889c7249a599ea094edb74b4a10cc7558fd123b9-Screenshot_2025-08-26_at_3.09.41_PM.png" align="center" width="320px" border={true} />


<br />


<Image src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Screenshot-2022-04-25-at-10.39.27-AM-726x1024.png" align="center" width="350px" />


3. Enter the user’s name in the **Name** field.
4. Enter the user’s email ID in the **Email ID** field.
5. Select any of the following options from the **Select the type of referral access this user will have the** field:
   - The user will be able to see all your referrals
   - The user will be able to see only their referrals
6. Select any of the following user’s permissions from the Select type of user management permissions this user will have field.
   - The user can add/manage other users
   - The user cannot add/manage other users
7. Click **Add User** to add the user.

   A confirmation message is displayed, and a link is sent to the e-mail ID that was entered in Step 4.

## Revoke a User

To revoke a user or make the user inactive on Partner Portal:

1. Click your profile picture on the top-right corner and select **Invite a user** from the drop-down menu.


<Image src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Screenshot-2022-04-25-at-10.56.12-AM.png" align="center" width="150px" />


```
The My Users page is displayed.
```

2. Click the hamburger menu next to the user you wish to revoke and select **Revoke Access**.

### Edit Permissions for a User

To edit permission for a user on Partner Portal:

1. Click your profile picture on the top-right corner and select **Invite a user** from the drop-down menu.


<Image src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Screenshot-2022-04-25-at-10.56.12-AM.png" align="center" width="150px" />


```
The _My Users_ page is displayed.
```

2. Click the hamburger menu next to the user you wish to revoke and select **Edit Permission**.

   The _Add User Details_ page is displayed.


<Image src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Screenshot-2022-04-25-at-11.10.39-AM-1024x435.png" align="center" width="550px" />


<br />


<Image src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Screenshot-2022-04-25-at-11.10.39-AM-1024x435.png" align="center" width="3px" />


3. Select any of the following user’s permissions from the **Select type of user management permissions this user will have** field.
   - The user can add/manage other users
   - The user cannot add/manage other users
4. Click **Add User**.
