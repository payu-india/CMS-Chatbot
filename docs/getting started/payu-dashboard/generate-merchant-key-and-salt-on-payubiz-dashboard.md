---
title: Generate Merchant Key and Salt on PayUBiz Dashboard
excerpt: ''
deprecated: true
hidden: true
metadata:
  title: Generate Merchant Key and Salt on PayUBiz Dashboard
  description: >-
    Access merchant key and salt from the PayU Dashboard for test and production environments. Generate API credentials required for hosted checkout, merchant hosted, and API integrations. Covers Generate Merchant Key and Salt on PayUBiz Dashboard.
  robots: index
  keywords:
    - payu merchant key salt dashboard
    - generate api key payu dashboard
    - payu test production key salt dashboard
    - payu dashboard developer api details
    - payment gateway credentials payu dashboard
    - payu dashboard access merchant key salt
    - payu api key generation dashboard guide
    - payu dashboard test mode key salt
    - payment gateway api credentials payu india
    - payu dashboard key salt vs razorpay cashfree
next:
  description: ''
---
This section describes how to get the current Salt or generate a new Salt on PayUBiz Merchant Dashboard.

> 🚧 For only PayUBiz merchants:
>
> This procedure is only applicable for **PayUBiz** merchants.

## Get the Current Salt

You can get the new salt value from PayU Merchant Dashboard that will be used in hash calculation.\
To get the current Salt:

1. Navigate to the PayUBiz Merchant Dashboard using the following URL:

[https://txncdn.payubiz.in/login](https://txncdn.payubiz.in/login)

The PayUBiz Dashboard login page is displayed.

<Image align="center" alt="PayU Dashboard - The PayUBiz Dashboard login page is displayed." width="550px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/getobject-1.jpeg" />

1. Enter the user name and password.
2. Click **Sign in**.
3. Navigate to **My Account** > **System Settings**.

The 8-digit Salt is displayed under the **Salts** field.

<Image align="center" alt="PayU Dashboard - The 8-digit Salt is displayed under the Salts field." className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/06/test_salt_paybiz.png" />

1. Click **Copy** to copy the Salt to the clipboard.

## Regenerate Salt for Integration

If you require to change the current Salt or regenerate a new Salt, you can generate it from the PayU Dashboard.\
To regenerate salt from Dashboard:

1. Log in to PayU Merchant Dashboard as described above.
2. Navigate to **My Account** > **System Settings**.

The *System Settings* page is displayed and **Generate New Salt** button can be found below the current Salts.

<Image align="center" alt="PayU Dashboard - The System Settings page is displayed and Generate New Salt button can be found below the curr" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/06/salt_payubiz.png" />

3. Click **Generate New Salt** to generate a new Salt for your existing account.

The new Salt is generated.

4. Click **Copy** to copy the new Salt to clipboard.

**Note**: Your new salt will be generated, and the old salt will be de-activated. Ensure that you update the new Salt for all your integration with PayU.