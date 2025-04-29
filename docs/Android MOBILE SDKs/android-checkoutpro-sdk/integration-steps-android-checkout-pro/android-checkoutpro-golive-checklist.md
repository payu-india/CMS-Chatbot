---
title: 3. Go-live Checklist
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
Ensure these steps before you deploy the integration in a live environment. 

## Collect Live payments

After testing the integration end-to-end, once you are confident that the integration is working as expected, you can switch to live mode to start accepting payments from your customers. 

> 🚧 Watch Out!
> 
> Ensure that you are using the production merchant key and salt generated in the live mode.

<ProductionKeyAndSaltProcedure />

### Checklist 2: Configure setIsProduction()

Set the value of the `setIsProduction()`to `true` in the payment integration code. This enables the integration to accept live payments.

### Checklist 3:- Configure your SURL/FURL

PayU recommends you to design, your own SURL and FURL.

Refer the link to [Handling SURL and FURL](https://docs.payu.in/docs/handling-redirect-urls-surlfurl-with-android-sdk) doc details.

> 🚧 We are not recommended to go live with PayU SURL and FURL.

### Checklist 4:- Remove/comment meta -data code from manifest file :-

#### For Android

You must be comment/remove the below metadata code from the manifest file to use the UPI Collect flow on Production env:-

```Text XML
<application>
<meta-data android:name="payu_debug_mode_enabled" android:value="true" /> // set the value to false for production environment
<meta-data android:name="payu_web_service_url" android:value="https://test.payu.in" /> //Comment in case of Production-->
<meta-data android:name="payu_post_url" android:value="https://test.payu.in"/> //Comment in case of Production-->
</appliction>
```

### Checklist 5: Configure verify payment method

Configure the Verify payment method to fetch the payment status. We strongly recommend that you use this as a back up method to handle scenarios where the payment callback is failed due to technical error.

### Checklist 6: Configure Webhook

We recommend that you configure Webhook to receive payment responses on your server. For more information, refer to [Webhooks](https://docs.payu.in/docs/webhooks).