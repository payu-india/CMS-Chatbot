---
title: Customer Journey for FKSC
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: payu-hosted-checkout-fksc
      title: PayU Hosted Checkout Integration
    - type: basic
      slug: merchant-hosted-integration-fksc
      title: Merchant Hosted Integration
---
## Website Integration

The customer workflow while using Supercoins Pay using the PayU Checkout Integration is illustrated in the following video:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/ezgif-3-48775f472b.gif)

1. The customer is redirected to the PayU Checkout page from the merchant’s website.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/09/Screenshot-2023-09-21-at-1.02.28-PM-488x1024.png)

2. Customer selects **Supercoin Pay** as a payment option.
3. PayU redirects the customer to Flipkart’s Supercoin Pay Page and the customer will log in using their mobile OTP (for a repeat customer this step will be skipped).

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/09/Screenshot-2023-09-21-at-12.56.29-PM-1-511x1024.png)

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/09/Screenshot-2023-09-21-at-12.54.30-PM-511x1024.png)

3. Customers can split the payment amount into Supercoins and any other payment instrument by selecting/deselecting the Supercoins checkbox.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/09/Screenshot-2023-09-21-at-12.51.44-PM-518x1024.png)

4. The customer selects a payment instrument for split payment.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/09/combined_fksc-1-556x1024.png)

5. The customer initiates payment flow (3DS/OTP/Pin).

The success page is displayed after successful payment