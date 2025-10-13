---
name: IOS_Go_Live
---
<Accordion title="Go-Live Checklist" icon="fa-table">
Ensure these steps before you deploy the integration in a live environment.

<Accordion title="Collect Live Payments" icon="fa-code">
  After [testing the integration](https://docs.payu.in/docs/ios-checkoutprosdk-test-integration) end-to-end, once you are confident that the integration is working as expected, you can switch to live mode to start accepting payments from your customers.

  > 🚧 Watch Out!
  >
  > Ensure that you are using the production merchant key and salt generated in the live mode.

  <ProductionKeyAndSaltProcedure />
</Accordion>

<Accordion title="Checklist 2: Configure environment" icon="fa-code">
  Set the value of the `environment`to `test/production` in the payment integration code. This enables the integration to accept live payments.
</Accordion>

<Accordion title="Checklist 3: Configure your SURL/FURL" icon="fa-code">
  PayU recommends you to design, your own SURL and FURL.

  Refer the Link to [Handle SURL and FURL](https://docs.payu.in/docs/handling-redirect-surlfurl-urls-with-ios).

  > 🚧 You are not recommended to go live with PayU SURL and FURL.
</Accordion>

<Accordion title="Checklist 4: Configure Verify Payment" icon="fa-code">
  Configure the Verify payment method to fetch the payment status. For more information, refer to [Verify Payment API](https://docs.payu.in/reference/verify_payment_api/)
</Accordion>

<Accordion title="Checklist 5: Configure Webhook" icon="fa-code">
  PayU recommends you to configure Webhooks to receive payment responses on your server. For more information, refer to [Webhooks](https://docs.payu.in/docs/webhooks).
</Accordion>
</Accordion>
