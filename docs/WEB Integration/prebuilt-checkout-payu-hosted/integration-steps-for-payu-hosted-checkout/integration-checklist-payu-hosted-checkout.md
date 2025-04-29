---
title: 3. Production Checklist
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
## 1. Update Production Key and Salt

Update your Production Key and Salt in your integration code to replace the Test Key and Salt. To generate the live merchant key and salt:

1. Log in to the PayU Dashboard and switch to Live Mode on the menu.
2. Navigate to **Developers → API Keys** tab.
3. Copy the key and salt using the copy button.
4. Replace the Test key and Test salt with the Production Key and Live salt in the payment integration code and start accepting actual payments.

## 2. Final checkout verification

Use the following checklist to ensure your PayU Hosted Checkout integration is complete:

1. Completed all the required checkout details have been collected correctly on your website and validated.

> 📘 Reference:
> 
> For more information on collecting and submitting the request parameter, refer to the following:
> 
> - [Submitting Payment Request on your Website](doc:submitting-payment-request-on-your-website)
> 
> - [Working with Response after a Customer Checkout](doc:working-with-response-after-a-customer-checkout)

2. Verified the Response from PayU. For more information on responses, refer to [API Integration](https://payu-hosted-checkout.readme.io/docs/integrate-with-payu-hosted-checkout).
3. Completed the callback response (reverse hashing) is not tampered with. For more information, refer to [Hashing Request and Response](doc:generate-hash-payu-hosted).
4. Confirmed the transaction status on the Server-side, if the callback fail. Use Webhooks for hearing callbacks. For more information, refer to \~~Verify Payment Status \~~ (under API Reference) and [Webhooks](/docs/webhooks).
5. Completed the integration on Production. The endpoint for the  Production environment is:

 <https://secure.payu.in/>