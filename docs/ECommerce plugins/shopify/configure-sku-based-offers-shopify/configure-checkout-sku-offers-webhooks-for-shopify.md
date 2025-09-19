---
title: Configure Checkout SKU-Based Offers Webhooks
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Configure Checkout SKU-Based Offers Webhooks for Shopify
  description: ''
  keywords:
    - Configure Checkout SKU-Based Offers Webhooks for Shopify
    - SKU-Based Offers Webhooks for Shopify
    - ' Webhooks for Shopify'
  robots: index
next:
  description: ''
---
This section describes the procedure to allow PayU payment app access to checkout details (including SKU information in the cart).

To configure webhooks for Shopify and share it with PayU support:

1. Log in to Shopify admin panel.
2. Navigate to **Settings** > **Notifications**.
3. Select **Webhooks**. 

![](https://files.readme.io/e2d75bfd02c8d8e8a33f8ae23817f5ea778e4cb5b0195da27ca2f46689a5e554-shopify_webhook_select_webhooks_from_menu.png)

<br />

1. Select **Create webhook** from the **Webhooks** page.

<Image align="center" className="border" border={true} src="https://files.readme.io/0b17ea589a9b6a77fc1d34510463754d4d99115743cbd5c480874156c54b699d-shopify_dashboard_click_create_webhook.png" />

<br />

1. Enter the following details in the *Add webhook* pop-up page and then click **Save**.
   * Select **Checkout creation** from the **Event** drop-down list.
   * Select **JSON** from the **Format** drop-down list.
   * Enter the following URL in the **URL** field:  \
     [https://partnerapilayer.payu.in/apilayer/shopify\_app/shopifyWebhook](https://partnerapilayer.payu.in/apilayer/shopify_app/shopifyWebhook)    

<Image align="center" className="border" width="450px" border={true} src="https://files.readme.io/be6160585a76882f7018aed6b8ccdb0bb1d3023f8b808d3d58eda414f374b047-shopify_dashboard_add_webhook_page.png" />

6. Repeat Step 5 with “Checkout update” event type from the **Event** drop-down list.

<Image align="center" width="450px" src="https://files.readme.io/b5a04aaef13c494ae191bb9d83631f831c957c1a912229e570e94b2d8676673e-shopify_dashboard_webhooks_event_types.png" />

6. Copy the hash key given as under the “Your webhooks will be signed with” section at the bottom.  

<Image align="center" className="border" border={true} src="https://files.readme.io/b369535a0b7730977ace369a823ac48f0d4f28fa726c6d244ada5ccd5a1d7112-shopify_dashboard_webhooks_api_key.png" />

6. Share the following details with PayU to enable of SKU-based offers. 
   * **MID**: Your MID provided by PayU
   * **Hash key** : The hash key you copied in Step 7 from Shopify dashboard after creation of checkout webhooks
