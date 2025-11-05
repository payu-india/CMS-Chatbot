---
title: PayU Hosted Check-out Integration - CLW
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
With the PayU Hosted Checkout integration, the entire payment experience is controlled by PayU. The following sections describe how to use the PayU Hosted Integration to collect payments

## Customer journey

1. Customer will click on Pay on Merchant website and Application
2. Merchant will redirect the customer to PayU Checkout using \_payment API. Correct Mobile Number has to be passed by the Merchant in the API

> **Note**: Wallet URN can also be passed (Optional).

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/09/a-screenshot-of-a-computer-description-automatica.png)

3. Customer is displayed the Closed Loop wallet as the primary option (For first time customer, OTP authentication is required to display balance)
4. Basis comparison between transaction amount and balance amount, further journey will be initiated

* Sufficient Balance: This will trigger a one-click payment to debit the customer’s wallet

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/09/word-image.png)

* Insufficient Balance: This will ask customer to add money (minimum residual amount) on the fly in the wallet and then debit the transaction amount. (For cases where wallet is being used just for cashback posting, **configuration to disable load and pay** is also there)

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/09/word-image-1.png)

5. Addition of Money can be done using any of the payment instrument configured on the Merchant (Cards/NB/Wallet). Also, merchant will have the flexibility to restrict the customer for any payment instrument for only loading of the wallet (not allow CC etc)

For more information on PayU Hosted Checkout integration, refer to [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted)