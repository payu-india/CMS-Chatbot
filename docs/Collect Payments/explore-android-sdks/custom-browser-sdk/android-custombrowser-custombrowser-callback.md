---
title: CustomBrowser Callback
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: android-custombrowser-configurations
      title: Configurations
---
This section describes how to create an object of PayUCustomBrowserCallback. PayUCustomBrowserCallback provides the following callback methods:

* `onPaymentFailure`(String payuResult,String merchantResponse) – Calls when payment fails.
* `onPaymentSuccess`(String payuResult,String merchantResponse) – Calls when payment succeeds.
* `onCBErrorReceived`(int errorCode, String errormsg) – Called for any error in the custom browser.

The following error messages are thrown in the callback method:

| Error code | Error Message                             | Description                                                                                                                          |
| :--------- | :---------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| 1          | VENDOR_NOT_SUPPORTED                      | The device Vendor is not supported                                                                                                   |
| 2          | DEVICE_NOT_SUPPORTED                      | The device is not supported                                                                                                          |
| 3          | APP_VERSION_MISMATCH                      | Samsung Pay version doesn't meet the requirements                                                                                    |
| 4          | COUNTRY_NOT_SUPPORTED                     | The country of device origin is not supported by Samsung Pay                                                                         |
| 5          | MERCHANT_KEY_NOT_REGISTER_FOR_SAMSUNG_PAY | Merchant is not registered for Samsung Pay with PayU                                                                                 |
| 6          | CONTEXT_NULL                              | Context is null                                                                                                                      |
| 7          | PAYMENT_ID_NOT_PRESENT                    | Check your postdata                                                                                                                  |
| 1001       | DEVICE_NOT_SUPPORTED                      | In case `enablewebflow` is set to false for Tez payment and the Tez app is not present on the device following error would be thrown |
| 1002       | MERCHANT_INFO_NOT_PRESENT                 | In case below error is received while processing payment please check your postData and hash                                         |

* `setCBProperties`(WebView webview, Bank payUCustomBrowser)—Callback where webview setting is done.
* `onBackButton`(AlertDialog.Builder alertDialogBuilder)—This callback provides alert dialog access, so customisation can be done to alert dialog.
  * `onBackApprove()`—Calls when OK is selected from the alert dialog.
  * `onBackDismiss()`—Calls when Cancel is selected from the alert dialog.
* `onPaymentTerminate()`—Called when payment is terminated.
* `isPaymentOptionAvailable`(CustomBrowserResultData resultData)—Merchant must check for Samsung Pay/PhonePe payment option availability on customer device before showing Samsung Pay/PhonePe/Google Pay/UPI as a payment option. This callback is called in response of the`checkForPaymentAvailability` method present in CustomBrowser. Merchants can use the value of `resultData` object similar to the following:
  * `resultData.getPaymentOption()`—Gives PaymentOption, that is, SamsungPay/PhonePe/Google Pay/UPI.
  * `resultData.isPaymentOptionAvailable()`—Boolean whether Payment through selected `PaymentOption` is possible.
  * `resultData.getSamsungPayVpa()`—Gives SamsungPay VPA associated with the device.
  * `resultData.getErrorMessage()`— Gives error message in case PaymentOption is not available.
    onVpaEntered(String vpa, PackageListDialogFragment `packageListDialogFragment)`(Available from version 7.3.0): Merchants must override this function and provide verifyVpaHash in case they want payment through UPI Collect flow.

```java
packageListDialogFragment.verifyVpa(verifyVpaHash);
```

<Callout icon="👉" theme="default">
  **Tip**: To generate `verifyVpaHash`, use the validateVPA command and var1 as VPA address. To calculate the hash, refer to [Hash Generation](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk).
</Callout>

The sample code block for PayUCustomBrowserCallback:

```java
PayUCustomBrowserCallback payUCustomBrowserCallback = new PayUCustomBrowserCallback() {
@Override
public void onPaymentFailure(String payuResponse,String merchantResponse) {
Intent intent = new Intent();
intent.putExtra(getString(R.string.cb_result), merchantResponse);
intent.putExtra(getString(R.string.cb_payu_response), payuResponse);
setResult(Activity.RESULT_CANCELED, intent);
finish();
}
@Override
public void onPaymentTerminate() {
}
@Override
public void onPaymentSuccess(String payuResponse,String merchantResponse) {
Intent intent = new Intent();
intent.putExtra(getString(R.string.cb_result), merchantResponse);
intent.putExtra(getString(R.string.cb_payu_response), payuResponse);
setResult(Activity.RESULT_OK, intent);
finish();
}
@Override
public void onCBErrorReceived(int code, String errormsg) {
}
@Override
public void setCBProperties(WebView webview, Bank payUCustomBrowser) {
webview.setWebChromeClient(new PayUWebChromeClient(payUCustomBrowser));
webview.setWebViewClient(new PayUWebViewClient(payUCustomBrowser,merchantKey));
webview.postUrl(url, payuConfig.getData().getBytes());
//comment above line if you are using CB is 6.1 or above
}
@Override
public void onBackApprove() {
PaymentsActivity.this.finish();
}
@Override
public void onBackDismiss() {
super.onBackDismiss();
}
@Override
public void onBackButton(AlertDialog.Builder alertDialogBuilder) {
super.onBackButton(alertDialogBuilder);
}
//Below method is available since version 7.1.3+
@Override
public void isPaymentOptionAvailable(CustomBrowserResultData resultData) {
Toast.makeText(PaymentsActivity.this, “isPaymentOptionAvailable”+resultData.getSamsungPayVpa() 
, Toast.LENGTH_SHORT).show();
}
//Below method is available since version 7.3.0+
@Override
public void onVpaEntered(String vpa, PackageListDialogFragment packageListDialogFragment) {
//Calculate validateVpahash using vpa and provide to verifyVpa method of 
PackageListDialogFragment like below.
packageListDialogFragment.verifyVpa(calculateHash(input));
}
};
```