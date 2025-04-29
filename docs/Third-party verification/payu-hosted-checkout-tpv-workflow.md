---
title: PayU Hosted Checkout TPV Workflow
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
For the <Glossary>TPV</Glossary> payment mode using PayU Hosted Checkout integration, PayU takes care of the integration and you just need to enable TPV.

The customer journey involved when collecting payment using TPV:

> 📘 Note:
>
> If you don’t have TPV enabled, try requesting using Dashboard. For more information, refer to [Configure User Settings](doc:configure-user-settings#checkout-payment-modes). If you could not request through Dashboard, contact your PayU Key Account Manager or [PayU Support](https://help.payu.in/).

## General workflow

### Step 1

The customer chooses to pay via a supported payment mode on PayU checkout. 

<Image align="center" className="border" border={true} src="https://files.readme.io/45ffbb01f0018847bdc5fdefd1562365754f0cb8fcc29ea4a4a9cf951671e29f-Screenshot_2025-02-24_at_11.52.57_AM.png" />

### Step 2

Here the customer chooses the payment mode they want to proceed. For example, **UPI** and then select **Pay through UPI Number/ID**.

<Image align="center" className="border" width="475px" border={true} src="https://files.readme.io/8f020aeaf60cb6033dd5221e78c6c661c7d3b34d36a0022cc3d929f215473195-payu_hosted_tpv_step2.png" />

<Image align="center" className="border" width="475px" border={true} src="https://files.readme.io/1d1cfe1ce3a0574a9fd83d800a82593359d1324dae64e9a4d5052db97503897b-payu_hosted_tpv_step2a.png" />

### Step 3

A pop-up page is displauyed. Here, the customer needs to enter their UPI ID or registered mobile number.

<Image align="center" src="https://files.readme.io/83e8762fb57dd7ed53ee1b585c56aeb0376fd8b5a74e39a3d4baae721e7f33c2-payu_hopsted_tpv_step3.png" />

### Step 4

Customer enters the Phone number/UPI ID and clicks Verify. Payment gets completed successfully.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/02/word-image-4.png)

<br />

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/02/word-image-4.png)
