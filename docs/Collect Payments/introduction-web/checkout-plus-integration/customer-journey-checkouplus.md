---
title: Customer Journey
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
This document demonstrates the checkout plus workflow for an UPI payment.

<Callout icon="📘" theme="info">
  ### Note

  The following is a sample workflow, so the actual user experience may vary based upon the checkout page GUI (for example, the button names can be different) of your website/Mobile app but broadly, the flow of the transaction remains unchanged.
</Callout>

**Step 1**: Enter the mobile number and the email address associated with your user account and click on Buy Now.


<Image src="https://files.readme.io/dba2a2d-getobject.jpeg" align="center" />


_The payment modal is displayed on the same page_


<Image src="https://files.readme.io/3e1fe55-getobject_1.jpeg" align="center" />


**Step 2**: Since we are using UPI for this payment, select UPI and choose the UPI option that is convenient for you, such as PhonePe, Google Pay, BHIM, Paytm etc and then:

1. Enter your UPI ID.
2. Click Proceed, once the UPI id is verified.

<Callout icon="📘" theme="info">
  ### Note

  In this example we have used PhonePe as the UPI option.
</Callout>


<Image src="https://files.readme.io/a1b98cd-getobject_2.jpeg" align="center" />


**Step 3**: PayU checkout plus modal waits for the payment to be approved by you.


<Image src="https://files.readme.io/3652db8-getobject_3.jpeg" align="center" />


The payment status(Success/Failure) is displayed on the screen. If the payment is failed, you can click on Retry to restart the payment process from Step 1.

<Callout icon="🚧" theme="warn">
  ### Remember

  The page that is displayed on a successful/failed transaction depends on the URL specified in the surl/furl parameters by the merchant in the Transaction Request.
</Callout>

<br />
