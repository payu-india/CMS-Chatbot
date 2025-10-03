---
name: Go_Live_Checklist
---
<Accordion title="Go-live Checklist" icon="fa-list">
Ensure these steps before you deploy the integration in a live environment.

<Accordion title="Collect Live Payments" icon="fa-code">
After [testing the integration](https://docs.payu.in/docs/reactnative-checkoutpro-test-integration) end-to-end, once you are confident that the integration is working as expected, you can switch to live mode to start accepting payments from your customers.

> 🚧 Watch Out!
>
> Ensure that you are using the production merchant key and salt generated in the live mode.

<ProductionKeyAndSaltProcedure />

<Accordion title="Checklist 2: Configure environment() parameter" icon="fa-code">
Set the value of the `environment()`to `0` in the payment integration code. This enables the integration to accept live payments.
</Accordion>

<Accordion title="Checklist 4:- Remove/comment meta -data code from manifest file :-" icon="fa-code">
#### For Android

You must be comment/remove the below metadata code from the manifest file to use the UPI Collect flow on Production env:-

```Text XML
<application>
<meta-data android:name="payu_debug_mode_enabled" android:value="true" /> // set the value to false for production environment
<meta-data android:name="payu_web_service_url" android:value="https://test.payu.in" /> //Comment in case of Production-->
<meta-data android:name="payu_post_url" android:value="https://test.payu.in"/> //Comment in case of Production-->
</appliction>
```
</Accordion>

<Accordion title="Checklist 5: Configure verify payment method" icon="fa-code">
Configure the Verify payment method to fetch the payment status. We strongly recommend that you use this as a back up method to handle scenarios where the payment callback is failed due to technical error.
</Accordion>

<Accordion title="Checklist 6: Configure Webhook" icon="fa-code">
We recommend that you configure Webhook to receive payment responses on your server. For more information, refer to [Webhooks](https://docs.payu.in/docs/webhooks).
</Accordion>

</Accordion>
</Accordion>