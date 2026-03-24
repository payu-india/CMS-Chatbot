---
title: Go-live Checklist
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

## Collect Live Payments

After \[testing the integration]\(doc: ios-custombrowser-test-the-integration) end-to-end, once you are confident that the integration is working as expected, you can switch to live mode to start accepting payments from your customers. 

> 🚧 Watch Out!
>
> Ensure that you are using the production merchant key and salt generated in the live mode.

<ProductionKeyAndSaltProcedure />

### Checklist 2: Configure setIsProduction()

Set the value of the `setIsProduction()`to `true` in the payment integration code. This enables the integration to accept live payments.

### Checklist 3: Configure verify payment method

Configure the Verify payment method to fetch the payment status. We strongly recommend that you use this as a back up method to handle scenarios where the payment callback is failed due to technical error.

### Checklist 4: Configure Webhook

We recommend that you configure Webhook to receive payment responses on your server. For more information, refer to [Webhooks](https://docs.payu.in/docs/webhooks).
