---
title: Collect Payment API - Merchant Hosted Checkout v2 Payment
excerpt: ''
deprecated: false
hidden: true
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
> To handle redirect URLs (surl and furl), refer to [Handling the Redirect URLs](https://docs.payu.in/v1/docs/handling-the-redirect-urls).

<PaymentAPIEnvironment />

You can get the **Try It** experience for the following payment modes:

* [Net Banking](https://docs.payu.in/v2/reference/_payment_v2_merchant_hosted_netbanking)
* [Cards](https://docs.payu.in/v2/reference/_payment-v2-merchant-hosted-cards)
* [UPI](https://docs.payu.in/v2/reference/_payment_v2_merchant_hosted_upi)
* [Wallet](https://docs.payu.in/v2/reference/collect_v2_payment_wallet)
* [EMI](https://docs.payu.in/v2/reference/collect-payments-with-emi-v2_payment)
* [BNPL](https://docs.payu.in/v2/reference/bnpl-v2_payment-merchant-hosted)

> 📘 Note:
>
> Collecting the information for the following parameters from customers is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information:
>
> * email
> * phone
> * address1