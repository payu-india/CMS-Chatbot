---
title: Production Checklist
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: Production Checklist for EMI Integration
  description: ''
  robots: index
next:
  description: ''
---
Use the following checklist to ensure your EMI integration using Merchant Hosted Checkout is complete:

1. Completed all the required checkout details have been collected correctly on your website and validated.

> 📘 Reference:
> 
> For more information on collecting and submitting the request parameter, refer to:
> 
> - [Submitting Payment Request on your Website](doc:submitting-payment-request-on-your-website)
> 
> - [Working with Response after a Customer Checkout](doc:working-with-response-after-a-customer-checkout)

2. Verified the Response from PayU. For more information on responses, refer to [Collect Merchant API - Merchant Hosted Checkout](ref:_payment_merchant_hosted)
3. Completed the callback response (reverse hashing) is not tampered with. For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).
4. Confirmed the transaction status on the Server-side, if the callback fail. Use Webhooks for hearing callbacks. For more information, refer to[Verify Payment API](ref:verify_payment_api) and [Webhooks](doc:webhooks).
5. Completed the integration on Production. The endpoint for the  Production environment is:

```
   <https://secure.payu.in/>
```