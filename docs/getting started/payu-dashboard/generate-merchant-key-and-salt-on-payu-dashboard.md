---
title: Access Production Key and Salt
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Access Production Key and Salt
  description: >-
    Access merchant key and salt from the PayU Dashboard for test and production environments. Generate API credentials required for hosted checkout, merchant hosted, and API integrations. Covers Access Production Key and Salt.
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
Before starting Web Checkout integration or integrating your website with PayU products, you need to generate your API key and Salt using the PayU Merchant Dashboard.

## Before you Begin

You need to activate your account with PayU to get the key and salt details on PayU Dashboard. You account gets activated only if you had submitted all the basic documents while onboarding. For more information, refer to [Activate Account](http://docs.payu.in/docs/complete-your-kyc).

> 📘 Notes:
>
> * The Production key and Salt will not be visible or accessible for merchants who have not completed onboarding or website was verified by PayU. While onboarding, the website verification takes 1-2 days.
> * The Production API key and Salt will not be visible for merchants without a website.

## Procedure to Access Key and Salt

To generate Salt from the PayU Merchant Dashboard:

1. Log in to PayU Dashboard using the following log on page:

[https://onboarding.payu.in/app/account/signin](https://onboarding.payu.in/app/account/signin)

2. Switch to **Live Mode** from the toggle option on the menu bar.

<Image align="center" alt="PayU Dashboard - Switch to Live Mode from the toggle option on the menu bar" border={true} width="320px" src="https://files.readme.io/e36828514287161a9b189454dd07463fea3a0697651e04b8f22ba3fc7bffbd54-Screenshot_2024-10-01_at_5.31.20_PM.png" className="border" />

3. Select **Developer** from the menu on the left-pane and select the **API Details**tab if required.

The _Developers_ page is displayed similar to the following screenshot. The values for the following fields are generated automatically (for the first time) and displayed similar to the following screenshot:

<Image align="center" alt="PayU Dashboard - The _Developers_ page is displayed similar to the following screenshot. The values for the following" border={true} src="https://files.readme.io/5a0b88f0cdb5d94c61b2100c99e64043ccf0dcda0e0041b6e0ec177d04a4ed26-Screenshot_2026-05-07_at_7.53.16_PM.png" className="border" />

* **key**: The API key that you must use for all payment requests.
* **Salt-32 bit**: The Salt, v1 is the 32-character string that you must use to generate a hash and further post the hash along with parameters when posting a payment request with PayU.

> 📘 Note:
>
> Use the **Copy Key** or **Copy Salt** button next to each field to copy them to a text file and save them in a confidential location for your perusal. This will avoid any typos with the merchant key.

## Regenerate and Activate Key and Salt

To regenerate key and salt and then activate them:

1. Log in to PayU Dashboard using the following log on page:

[https://onboarding.payu.in/app/account/signin](https://onboarding.payu.in/app/account/signin)

2. Switch to **Live Mode** from the toggle option on the menu bar.

<Image align="center" alt="PayU Dashboard - Switch to Live Mode from the toggle option on the menu bar" border={true} width="320px" src="https://files.readme.io/e36828514287161a9b189454dd07463fea3a0697651e04b8f22ba3fc7bffbd54-Screenshot_2024-10-01_at_5.31.20_PM.png" className="border" />

3. Select **Developer** from the menu on the left-pane and select the **API Details**tab if required.

<Image align="center" alt="PayU Dashboard - Select Developer from the menu on the left-pane and select the API Detailstab if required" border={true} src="https://files.readme.io/5173f9e018d851a3d01a90a3644ad2f201245305a920e0d53a285d935a5ced95-dashboard_regenerate_salt.png" className="border" />

4. Click the **Regenerate Salt** button to generate new salt.

   A confirmation pop-up message is displayed similar to the following screenshot:

<Image align="center" alt="PayU Dashboard - A confirmation pop-up message is displayed similar to the following screenshot:" width="450px" src="https://files.readme.io/41a57c7d4a7ad13a27b56634e8eeb0d8f812f71e973fc6ca496f3fa1701c0992-dashboard_regenerate_salt_confirmation.png" />

5. Click the **Regenerate** button.

   The _Success_ message is displayed at top-right corner similar to the following screenshot:

<Image align="center" alt="PayU Dashboard - The _Success_ message is displayed at top-right corner similar to the following screenshot:" border={true} src="https://files.readme.io/d5538ab7c7b8a3c8418b58421110d9592b10e9f6bbc83a6d66de17372ab8cce9-dashboard_regenerate_salt_activate.png" className="border" />

6. Click the **Activate** button displayed for **Salt** under the **Actions** column.

> 📘 Notes:
>
> * New Salt expires in 15 days expiry if not activated.
> * If the new Salt not activated within the 15 days, you will require to regenerate another salt.
> * After the new Salt is activated, the new Salt will be updated to replace of Salt version 1.
> * PayU recommends you to activate the regenerated Salt to avoid any payment or API call failures with your customers.
