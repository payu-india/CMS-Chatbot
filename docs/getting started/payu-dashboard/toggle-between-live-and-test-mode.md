---
title: Generate Merchant Key and Salt
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Before starting Checkout integration or integrating your website with PayU products, you need to get your API key and Salt for test and production environment from the PayU Merchant Dashboard.

Use the right pair depending on your environment:

## Merchant Key Salt

<Tabs>
  <Tab title="Test Environment">
    You can access your **Test Key and Salt** from the PayU Test Dashboard.

    1. Log in to the [PayU Test Dashboard](https://test.payu.in/).

    2. Switch to **Test Mode** from the toggle option on the menu bar.

       <Image align="center" border={true} src="https://files.readme.io/2282abf-dashboard_select_test_mode.png" width="320px" />

    3. Select **Developer** from the menu on the left-pane and select the **API Details** tab if required.

       The *Developers* page is displayed similar to the following screenshot. The values for the following fields are generated automatically (for the first time) and displayed similar to the following screenshot:

       <Image align="center" border={true} src="https://files.readme.io/ab723100609b4fa6179ab350ba7d5755807aaf52f1027a134dacc87f21a48bda-Screenshot_2024-09-09_at_6.25.24_PM.png" />

    > 📘 Note: These credentials are only valid in the **test environment**. They cannot be used in production.
  </Tab>

  <Tab title="Production Environment">
    Once your merchant account is activated, you can generate **production credentials** from the PayU Merchant Dashboard.

    1. Log in to the [PayU Merchant Dashboard](https://merchant.payu.in/).

    2. Switch to **Live Mode** from the toggle option on the menu bar.

       <Image align="center" border={true} src="https://files.readme.io/e36828514287161a9b189454dd07463fea3a0697651e04b8f22ba3fc7bffbd54-Screenshot_2024-10-01_at_5.31.20_PM.png" width="320px" />

    3. Select **Developer** from the menu on the left-pane and select the **API Details** tab if required.

       The *Developers* page is displayed similar to the following screenshot. The values for the following fields are generated automatically (for the first time) and displayed similar to the following screenshot:

       <Image align="center" border={true} src="https://files.readme.io/0ddaa94d203d7102154ece7c74b95ec50274d3fc3e4004ed64bbb8eadc0b37f3-dashboard_key_salt_live_mode.png" />

    > 📘 Note:  These credentials are sensitive.
    >
    > * Do not share them publicly.
    > * Do not hard-code them in frontend code.

    * Always store them securely on your server.
  </Tab>
</Tabs>

***

## Notes

* **Key** → Unique identifier for your merchant account.
* **Salt** → Secret value used for hashing and securing requests.
* Each environment has **separate Key–Salt pairs**. Ensure you’re using the correct set for **Test** vs **Production**.
* If you regenerate credentials, update them immediately in your application to avoid integration failures.

<br />
