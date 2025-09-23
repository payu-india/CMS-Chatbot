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
    You can access your **test Key and Salt** from the PayU Test Dashboard.

    1. Log in to the [PayU Test Dashboard](https://test.payu.in/).\
       ![Login to Test Dashboard](test-dashboard-login.png)

    2. Navigate to **Dashboard → Explore Dashboard → Access Test Merchant Key and Salt**.\
       ![Access Test Key and Salt](test-key-salt.png)

    3. The page displays the **Key** and **Salt** assigned for your test account.\
       ![View Test Key and Salt](test-key-salt-details.png)

    ⚠️ These credentials are only valid in the **test environment**. They cannot be used in production.
  </Tab>

  <Tab title="Production Environment">
    Once your merchant account is activated, you can generate **production credentials** from the PayU Merchant Dashboard.

    1. Log in to the [PayU Merchant Dashboard](https://merchant.payu.in/).\
       ![Login to Production Dashboard](prod-dashboard-login.png)

    2. Navigate to **Dashboard → Explore Dashboard → Access Production Key and Salt**.\
       ![Access Production Key and Salt](prod-key-salt.png)

    3. The page displays your live **Key** and **Salt**, which must be used in the **production environment**.\
       ![View Production Key and Salt](prod-key-salt-details.png)

    ⚠️ These credentials are sensitive.

    * Do not share them publicly.
    * Do not hard-code them in frontend code.
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
