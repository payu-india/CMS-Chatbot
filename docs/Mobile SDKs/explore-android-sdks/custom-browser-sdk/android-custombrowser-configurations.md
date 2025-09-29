---
title: Configurations
excerpt: Describes various configuration parameters supported by CustomBrowserConfig.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Create an object of CustomBrowserConfig similar to the following code snippet:

```java Java
CustomBrowserConfig customBrowserConfig = new CustomBrowserConfig(merchantKey,txnId);
```

## Mandatory configuration

* `PostData `– Payment Post Data [Post data being sent to PayU PG] – setPayuPostData(String).
* `PostURL` – Payment Post URL [PG url to be precise] -setPostURL(String)

## Optional configuration

* `HTMLdata` – setHtmlData(String htmlData) (Available since version 7.2.2+)
* `htmlData` – HTML string received from PayU web service using Server to Server call.
* `ViewPortEnable` – setViewPortWideEnable(viewPortWide);
* `true` – set viewport true
* `false` – set viewport false
* `default` – false
* `ProgressDialogCustomView` – setProgressDialogCustomView (progressDialogCustomView);
* `progressDialogCustomView`- Custom View for Progress Dialog.
* `AutoApprove` – setAutoApprove(boolean isAutoApprove);
* `true` – OTP will be fetched automatically and approved as well.
* `false` – OTP will fetch automatically.
* `default` – false`
* `Surl/Furl Response Timeout` – setMerchantResponseTimeout(int merchantResponseTimeout);
* `merchantResponseTimeout` – Surl/Furl loading timeout in milliseconds
* `AutoSelectOTP` – setAutoSelectOTP(boolean `isAutoSelect`)
* `true` – OTP option will be selected automatically
* `false` – User will select from either password or OTP
* `default` – false
* `Merchant SMS permission `– For Android M only – setMerchantSMSPermission(false);
* `true` – shows the dialog for permission
* `false` – no dialog is shown to the user
* `default` – false
* `PackageNameForSpecificApp` – Package name of the Intent App that you want to invoke. When you want to invoke any specific Intent App instead of generic intent. You must add UPI SDK dependency for this. where `UPI_PACKAGE_ID` can be any of UPI apps like `com.phonepe.app(PhonePe)`, `com.google.android.apps.nbu.paisa.user(GPay)`, etc.

```Text JAVA
setPackageNameForSpecificApp(<UPI_PACKAGE_ID>)
where UPI_PACKAGE_ID can be any of UPI apps like - 
com.phonepe.app(PhonePe),
com.google.android.apps.nbu.paisa.user(GPay) etc. 
```

* `DisableIntentSeamlessFailure`: You can disable the Manual VPA Fallback option from the Generic Intent tray from the backend as well as from the front-end. To disable it from the front-end, configure CustomBrowserConfig. ENABLE to `setDisableIntentSeamlessFailure` flag. You must include UPI SDK dependency to show the generic Intent Apps. For more information on how to include UPI SDK, refer to [integration steps](https://docs.payu.in/docs/android-upisdk-integration-steps) for Android UPI SDK.

```java Java
setDisableIntentSeamlessFailure(CustomBrowserConfig.DISABLE)
```

<Callout icon="📘" theme="info">
  **Remember**: Do not clear cookies for some URLs- We clear cookies for the URLs that load on the Custom Browser. If you don’t want to clear your webpage cookies, you should provide a list of URLs on which we would not clear the cookies.
</Callout>

```Text JAVA
setDomainUrlListToUnclear(ArrayList<String>);
```

`EnableSslDialog`: There might be a chance that the bank through an SSL error, we have handled it, PayU will redirect the user to the bank page in any SSL error. You can show the user the following popup page in case of an SSL error.

To show the popup message, you need to set true for the enableSslDialog config field:

```java Java
setEnableSslDialog(Boolean);
```
