---
title: 2. Test the Integration
excerpt: Use the Test mode to check if the integration is working as expected.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
After the integration is complete, you must test the integration before you go live and start collecting payment. You can start accepting actual payments from your customers once the test is successful.

> 🚧 Callout
> 
> The UPI in-app and UPI intent flow is not available in the Test mode.

> 👍 Testing checklist
> 
> Things to remember while testing an integration:
> 
> 1. To test the integration make sure that you are making a transaction call to the test endpoint. 
> 2. Use your test key and salt for the transaction requests. See [Genearate test key and salt](https://docs.payu.in/docs/generate-test-merchant-key-and-salt).
> 3. Set the value of the `environment` parameters to `1`.

You can make test payments using one of the payment methods configured at the Checkout.

> 🚧 Watch Out!
> 
> You must only use the Test merchant Key and Test Salt to carry out a test transaction.

***

<TestCardsCallout />



## Test credentials for supported payment methods

Following are the payment methods supported in PayU Test mode.

### Test VPA for UPI

You can use either of the following VPAs to test your UPI-related integration:

- [anything@payu](anything@payu)
- [9999999999@payu.in](mailto:9999999999@payu.in)

For Testing the UPI Collect flow, Please follow the below steps:- 

1. Once you enter the VPA click on the verify button and proceed to pay.
2. In NPCI page timer will start, Don't "CLICK" on click text. Please wait on the NPCI page.
3. The below link opens in the browser Paste the transaction ID at the end of the URL then click on the success/failure simulator page. After that, your app will redirect to your app with the transaction response.

<https://pgsim01.payu.in/UPI-test-transaction/confirm/>\<Txn_id>

#### For Android

You can add the below metadata under the application tag in the manifest file to test the UPI Collect flow on test env:-

> 🚧 Ensure to remove the code from the manifest file before going live.

```Text xml
<application>
<meta-data android:name="payu_debug_mode_enabled" android:value="true" /> // set the value to false for production environment
<meta-data android:name="payu_web_service_url" android:value="https://test.payu.in" /> //Comment in case of Production-->
<meta-data android:name="payu_post_url" android:value="https://test.payu.in"/> //Comment in case of Production-->
</appliction>
```

### Test UPI Intent/InApp flow

> ❗️ Callout
> 
> The UPI in-app and UPI intent flow is not available in the Test mode.