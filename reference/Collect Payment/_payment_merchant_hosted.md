---
title: Collect Payment API - Merchant Hosted Checkout
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collect Payment API for Merchant Hosted Checkout or Custom Checkout
  description: >-
    Explore PayU's Merchant Hosted Checkout API Reference for seamless payment
    integration. Access comprehensive documentation, including authentication
    methods, payment modes, and real-time transaction management. Utilize the
    interactive simulator to test API endpoints and streamline your custom
    checkout process. Ideal for developers seeking robust and flexible payment
    solutions.
  keywords:
    - Merchant Hosted Checkout Collect Payment API
    - Simulator for PayU payment collection
    - Custom Checkout integration with PayU
    - Collect payments using PayU API
    - Collect Payment API for Merchant Hosted Checkout
    - _payment API for Merchant Hosted Checkout
    - _payment API simulation for Custom Checkout
    - _payment API simulation for Merchant Hosted Checkout
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: custom-checkout-merchant-hosted
      title: Merchant Hosted Checkout
---
To process payments with credit/debit card, UPI, wallet, etc. on your website using PayU, collect the payment details on your website and submit them to PayU via API. This eliminates the need for redirection to PayU’s payment page, resulting in a more secure and efficient transaction. 

> 📘 Reference:
> 
> For an example of how to submit a payment request on your website, refer to [Submitting Payment Request on your Website](doc:submitting-payment-request-on-your-website). To handle redirect URLs (surl and furl), refer to [Handling the Redirect URLs](doc:handling-the-redirect-urls).

<PaymentAPIEnvironment />

You can get the **Try It** experience for the following payment modes:

- [Net Banking](ref:_payment_merchant_hosted_netbanking)
- [Cards](ref:_payment_merchant_hosted_cards)
- [UPI](ref:_payment_merchant_hosted_upi)
- [Wallets](ref:_payment_merchant_hosted_wallets)
- [EMI](ref:_payment_merchant_hosted_emi)
- [BNPL](ref:_payment_merchant_hosted_bnpl)
- [QR](ref:_payment_merchant_hosted_qr)

> 📘 Note:
> 
> Collecting the information for the following parameters from customers is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information:
> 
> - email
> - phone
> - address1