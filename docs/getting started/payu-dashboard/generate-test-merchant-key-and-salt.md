---
title: Access Test Merchant Key and Salt
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Access Test Merchant Key and Salt
  description: >-
    Access merchant key and salt from the PayU Dashboard for test and production environments. Generate API credentials required for hosted checkout, merchant hosted, and API integrations. Covers Access Test Merchant Key and Salt.
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
  robots: index
next:
  description: ''
---
Before starting Web Checkout integration or integrating your website with PayU products for the Test environment, you need to get your API key and Salt for your test merchant from the PayU Merchant Dashboard.

## Before you Begin

You need to register for a merchant account with PayU. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

<Callout icon="📘" theme="info">
  **Note**: The Test API key and Salt is accessible for merchants who have not completed onboarding or website was verified by PayU. While onboarding, the website verification takes 1-2 days and only the Product key and salt requires the website verification.
</Callout>

## Procedure

To generate test merchant API key and Salt:

1. Log in to PayU Dashboard using the following log on page:

[https://onboarding.payu.in/app/account/signin](https://onboarding.payu.in/app/account/signin)

2. Switch to **Test Mode** from the toggle option on the menu bar.

<Image align="center" alt="PayU Dashboard - Switch to Test Mode from the toggle option on the menu bar" border={true} width="320px" src="https://files.readme.io/2282abf-dashboard_select_test_mode.png" className="border" />

3. Select **Developer** from the menu on the left-pane and select the **API Keys** tab if required.

The _Developers_ page is displayed similar to the following screenshot. The values for the following fields are generated automatically (for the first time) and displayed similar to the following screenshot:

<Image align="center" alt="PayU Dashboard - The _Developers_ page is displayed similar to the following screenshot. The values for the following" border={true} src="https://files.readme.io/ab723100609b4fa6179ab350ba7d5755807aaf52f1027a134dacc87f21a48bda-Screenshot_2024-09-09_at_6.25.24_PM.png" className="border" />

* **key**: The API key that you must use for all payment requests.
* **Salt-32 bit**: The Salt, v1 is the 32-character string that you must use to generate a hash and further post the hash along with parameters when posting a payment request with PayU.

<Callout icon="📘" theme="info">
  **Note**: Use the **Copy Key** or **Copy Salt** button next to each field to copy them to a text file and save them in a confidential location for your perusal. This will avoid any typos with the merchant key.
</Callout>
