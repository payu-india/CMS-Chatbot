---
title: PayU Hosted Checkout BNPL Workflow
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  keywords:
    - PayU Hosted Checkout BNPL Integration
    - ' BNPL Non-Seamless Integration with PayU'
    - PayU Non-Seamless BNPL integration
    - Buy Now Pay Later Integration with PayU Hosted Checkout
    - ' BNPL API Integration Pay Later Services with PayU'
    - PayU Hosted BNPL Merchant Integration
    - Flexible Payment Options PayU Hosted Checkout Integration
  robots: index
next:
  description: ''
---
For the <<glossary:BNPL>> payment mode using PayU Hosted Checkout integration, PayU takes care of the integration and you just need to enable BNPL.

The customer journey involved when collecting payment using BNPL:

> 📘 Note:
> 
> If you don’t have BNPL enabled, try requesting using Dashboard. For more information, refer to [Configure User Settings](doc:configure-user-settings#checkout-payment-modes). If you could not request through Dashboard, contact your PayU Key Account Manager or [PayU Support](https://help.payu.in/).

## General workflow

### Step 1

The customer chooses to pay via a supported payment mode on PayU checkout. For example, BNPL > Simpl

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/02/word-image.png)

### Step 2

Here the customer chooses the lender they want to proceed with and enters their mobile number.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/02/word-image-1.png)

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/02/word-image-2.png)

### Step 3

This opens up the Bank OTP page. Here, the customer needs to enter the OTP sent to their registered mobile number.

### Step 4

Customer enters the OTP and clicks Submit. Payment gets completed successfully.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/02/word-image-4.png)

## BNPL using Native OTP Flow-PayU Hosted Checkout Integration

For the BNPL payment mode using PayU Hosted Checkout integration, you just require the Native OTP Integration flow enabled by contacting your PayU Key Account Manager, and PayU takes care of this flow. The customer journey involved when collecting payments with BNPL using Native OTP flow:

> 📘 Notes:
> 
> - If you don’t have BNPL enabled, try requesting using Dashboard. For more information, refer to [Checkout payment modes](/docs/configure-user-settings#disable-checkout-payment-modes). If you could not request through Dashboard, contact your PayU Key Account Manager or [PayU Support](https://help.payu.in/).
> - To enable Native OTP Integration flow, contact your PayU Key Account Manager or [PayU Support](https://help.payu.in/).

### Step 1

The customer chooses to pay through a supported payment mode on PayU checkout. For example, BNPL > Simpl.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/02/word-image.png)

### Step 2

Here, the customer chooses the lender they want to proceed with and enters their mobile number.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/bnpl_list-1024x775.png)

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/bnpl_final-1-1024x755.png)

### Step 3

This opens up the OTP Collection page on PayU Page (Non-Seamless). Here, the customer needs to enter the OTP sent to their registered mobile number.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/bnpl_otp-1024x776.png)

### Step 4

The customer enters the OTP and clicks Submit. The payment gets completed successfully.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/02/word-image-4.png)