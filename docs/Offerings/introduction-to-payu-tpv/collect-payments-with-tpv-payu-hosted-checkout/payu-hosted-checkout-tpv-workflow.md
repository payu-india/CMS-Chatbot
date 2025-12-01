---
title: 'Customer Journey '
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Customer Journey - TPV with PayU Hosted Checkout
  description: >-
    This section describes the customer journey for TPV integration with PayU
    Hosted Checkout.
  robots: index
next:
  description: ''
---
For the <Glossary>TPV</Glossary> payment mode using PayU Hosted Checkout integration, PayU takes care of the integration and you just need to enable TPV.

The customer journey involved when collecting payment using TPV:

<Callout icon="📘" theme="info">
  **Note**: If you don’t have TPV enabled, try requesting using Dashboard. For more information, refer to [Configure User Settings](doc:configure-user-settings#checkout-payment-modes). If you could not request through Dashboard, contact your PayU Key Account Manager or [PayU Support](https://help.payu.in/).
</Callout>

## Step 1

The customer chooses to pay via a supported payment mode on PayU checkout.

<Image align="center" border={true} width="500px" src="https://files.readme.io/42e28a7140db89ffaeebdbc940acfc84391ba18eea58560aa833fb1c20325e09-tvp_workflow_step1.png" className="border" />

## Step 2

Here the customer chooses the payment mode they want to proceed. For example, **UPI** and then select **Pay through UPI Number/ID**.

<Image align="center" border={true} width="475px" src="https://files.readme.io/8f020aeaf60cb6033dd5221e78c6c661c7d3b34d36a0022cc3d929f215473195-payu_hosted_tpv_step2.png" className="border" />

<Image align="center" border={true} width="475px" src="https://files.readme.io/1d1cfe1ce3a0574a9fd83d800a82593359d1324dae64e9a4d5052db97503897b-payu_hosted_tpv_step2a.png" className="border" />

## Step 3

Customer enters the Phone number/UPI ID and clicks **Verify** or customer transaction through Net Banking with the account already registered, and then payment gets completed successfully.

<Image align="center" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/02/word-image-4.png" className="border" />
