---
title: Access Merchant Key and Salt
deprecated: false
hidden: true
metadata:
  robots: index
  description: >-
    Access merchant key and salt from the PayU Dashboard for test and production environments. Generate API credentials required for hosted checkout, merchant hosted, and API integrations. Covers Access Merchant Key and Salt.
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
---
Before starting Checkout integration or integrating your website with PayU products, you need to get your API key and Salt for test and production environment from the PayU Merchant Dashboard.

Use the right pair depending on your environment:

## Merchant Key Salt

<Tabs>
  <Tab title="Test Environment">
    You can access your **Test Key and Salt** from the PayU Test Dashboard as soon as you create an account with PayU.

    1. Log in to the [PayU Test Dashboard](https://test.payu.in/).

    <Image align="center" alt="PayU Dashboard - Log in to the PayU Test Dashboard" src="https://files.readme.io/66f1002-payu_in_dashboard_login.png" />

    2. Switch to **Test Mode** from the toggle option on the menu bar.

       <Image align="center" alt="PayU Dashboard - Switch to Test Mode from the toggle option on the menu bar" border={true} src="https://files.readme.io/2282abf-dashboard_select_test_mode.png" width="320px" />

    3. Select **Developer** from the menu on the left-pane and select the **API Details** tab if required.

       The *Developers* page is displayed similar to the following screenshot. The values for the following fields are generated automatically (for the first time) and displayed similar to the following screenshot:

       <Image align="center" alt="PayU Dashboard - The Developers page is displayed similar to the following screenshot. The values for the following" border={true} src="https://files.readme.io/ab723100609b4fa6179ab350ba7d5755807aaf52f1027a134dacc87f21a48bda-Screenshot_2024-09-09_at_6.25.24_PM.png" />

    > 📘 Note: These credentials are only valid in the **test environment**. They cannot be used in production.
  </Tab>

  <Tab title="Production Environment">
    Once your website is verified and merchant account is activated, you can generate **Production key and Salt** from the PayU Merchant Dashboard.

    1. Log in to the [PayU Merchant Dashboard](https://merchant.payu.in/).

    2. Switch to **Live Mode** from the toggle option on the menu bar.

       <Image align="center" alt="PayU Dashboard - Switch to Live Mode from the toggle option on the menu bar" border={true} src="https://files.readme.io/e36828514287161a9b189454dd07463fea3a0697651e04b8f22ba3fc7bffbd54-Screenshot_2024-10-01_at_5.31.20_PM.png" width="320px" />

    3. Select **Developer** from the menu on the left-pane and select the **API Details** tab if required.

       The *Developers* page is displayed similar to the following screenshot. The values for the following fields are generated automatically (for the first time) and displayed similar to the following screenshot:

       <Image align="center" alt="PayU Dashboard - The Developers page is displayed similar to the following screenshot. The values for the following" border={true} src="https://files.readme.io/0ddaa94d203d7102154ece7c74b95ec50274d3fc3e4004ed64bbb8eadc0b37f3-dashboard_key_salt_live_mode.png" />

    > 📘 Note:  These credentials are sensitive.
    >
    > * Do not share them publicly.
    > * Do not hard-code them in frontend code.

    * Always store them securely on your server.
  </Tab>
</Tabs>

***

> 📘 Notes:
>
> * **Key** → Unique identifier for your merchant account.
> * **Salt-32 bit**: The Salt, v1 is the 32-character string that you must use to generate a hash and further post the hash along with parameters when posting a payment request with PayU.
> * **Salt-256 bit**: The Salt, v2 that you must use to generate a hash and further post the hash along with parameters when posting a payment request with PayU.
> * Each environment has **separate Key–Salt pairs**. Ensure you’re using the correct set for **Test** vs **Production**.
> * If you regenerate credentials, update them immediately in your application to avoid integration failures.

## Regenerate and Activate Key and Salt

To regenerate key and salt and then activate them:

1. Log in to PayU Dashboard using the following log on page:

[https://onboarding.payu.in/app/account/signin](https://onboarding.payu.in/app/account/signin)

2. Switch to **Live Mode** or **Test Mode** from the toggle option on the menu bar based on the environment for which you wish to regenerate the key and Salt.

<Image align="center" alt="PayU merchant key and salt - Switch to Live Mode or Test Mode from the toggle option on the menu bar based on the environ" className="border" border={true} width="320px" src="https://files.readme.io/e36828514287161a9b189454dd07463fea3a0697651e04b8f22ba3fc7bffbd54-Screenshot_2024-10-01_at_5.31.20_PM.png" />

3. Select **Developer** from the menu on the left-pane and select the **API Details**tab if required.

<Image align="center" alt="PayU Dashboard - Select Developer from the menu on the left-pane and select the API Detailstab if required" className="border" border={true} src="https://files.readme.io/5173f9e018d851a3d01a90a3644ad2f201245305a920e0d53a285d935a5ced95-dashboard_regenerate_salt.png" />

4. Click the **Regenerate Salt** button to generate new salt.

   A confirmation pop-up message is displayed similar to the following screenshot:

<Image align="center" alt="PayU Dashboard - A confirmation pop-up message is displayed similar to the following screenshot:" width="450px" src="https://files.readme.io/41a57c7d4a7ad13a27b56634e8eeb0d8f812f71e973fc6ca496f3fa1701c0992-dashboard_regenerate_salt_confirmation.png" />

5. Click the **Regenerate** button.

   The _Success_ message is displayed at top-right corner similar to the following screenshot:

<Image align="center" alt="PayU Dashboard - The _Success_ message is displayed at top-right corner similar to the following screenshot:" className="border" border={true} src="https://files.readme.io/d5538ab7c7b8a3c8418b58421110d9592b10e9f6bbc83a6d66de17372ab8cce9-dashboard_regenerate_salt_activate.png" />

6. Click the **Activate** button displayed for **Salt** under the **Actions** column.

> 📘 Notes:
>
> * New Salt expires in 15 days expiry if not activated.
> * If the new Salt not activated within the 15 days, you will require to regenerate another salt.
> * After the new Salt is activated, the new Salt will be updated to replace of Salt version 1.
> * PayU recommends you to activate the regenerated Salt to avoid any payment or API call failures with your customers.