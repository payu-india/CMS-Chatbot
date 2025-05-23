---
title: Enable PayU for Shopmatic
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
This section describes how to enable PayU PG on your Shopmatic web-store. If you encounter any issues while integration, refer to [Troubleshooting Shopmatic Integration](doc:troubleshooting-shopmatic-integration).

To enable PayU for Shopmatic:

1. Log in to your Shopmatic account.
2. Select **Setup** > **Payments** from the menu (on the left pane).

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Screenshot-2022-04-20-at-1.12.25-PM-1024x692.png" />

The *India Domestic Payment* page is displayed.

<Image align="center" className="border" border={true} width="550px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/01/Screenshot-2023-01-23-at-12.20.09-PM-1024x838.png" />

3. Click **Enable** for PayU.

   The *Integrate PayU* page is displayed.

<Image align="center" className="border" border={true} width="412px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/01/Screenshot-2023-01-23-at-12.20.48-PM.png" />

4. Click **I already have a PayUmoney account**.

> **Note**: If you already do not have a PayU account, register for a merchant account with PayU. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard)

A page similar to the following is displayed:

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/01/Screenshot-2023-01-23-at-12.22.52-PM-1024x673.png" />

5. Enter the details as described in the following table:

| **Field**     | **Description**                                                   |
| ------------- | ----------------------------------------------------------------- |
| Merchant Key  | Enter the merchant key that was provided by PayU.                 |
| Merchant ID   | Enter your production account key for the Production environment. |
| Merchant Salt | Enter your Salt for Production environment.                       |

> **Reference**: For more information on how to access the Key and Salt, refer to any of the following:

* **Production**:  [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
* **Test**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)

6. Click **Save**.

> 📘 Note:
>
> PayU recommends this step to reconcile with PayU’s database after you receive the response. Verify the transaction details using the **Verification Payment**API. For API reference, refer to <a href="https://docs.payu.in/reference/verify_payment_api" target="_blank">Verify Payment API</a>.