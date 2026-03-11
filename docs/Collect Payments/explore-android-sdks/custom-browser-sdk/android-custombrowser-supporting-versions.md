---
title: Supporting Versions below Lolipop
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This section describes changes that need to be made to support the versions below the Android Lollipop version (Android version 21).

## Features

* TLS v1.1+ Support for API levels 16-19 is done via chrome custom tabs.
* Chrome must be present in the device (version 45+ available JB onwards).
* Since payment is done through Chrome Custom tabs hence no surepay/OTP assist feature will be available.

## Changes required in surl/furl

Convert the response that your surl/furl processes into URI encoded format and add it to the payload key like below. In case you want to send a response sent by the PayU server then, make sure to append it after $| similar to the following:

```java Java
Uri encoded Post Data = <URI_ENCODED_YOUR_RESPONSE>$|<URI_ENCODED_PAYU_RESPONSE>

<a id="intentId" href="intent://payload?<URI_ENCODED_POST_DATA>#Intent;scheme=<YOUR_SCHEME>;package=<YOUR_PACKAGE_NAME>;end\">
```

**Where**:

For Surl -scheme=\<YOUR_PACKAGE_NAME>.success
For Furl – scheme=\<YOUR_PACKAGE_NAME>.failure

<Callout icon="📘" theme="info">
  **Tip**: You are advised to show a hyperlink, asking users to click to launch the deep link intent in.
</Callout>

```html Markup
<htmI><head></head> 
<script type="text/javascript"> 
var myFunc= function() {
 document.getElementByld('intentld').click(); 
}
window.onload = function() { 
setTimeout(myFunc, 3000); 
}</script> 
<body> 
<a id="intentld" 
href="Intent://payload?<URI_ENCODED_POST_DATA>Mntentscheme=<YOUR_SCHEME>;package=< YOUR_PACKAGE_NAME>;end\"> Click here to go back to app </a> 
</body> 
</html> 
```

<Callout icon="📘" theme="info">
  **Tip**: For API level 19, if the TLSv1.1+ connection cannot be made due to the old Cipher, you are advised to make changes as suggested in the reference.
</Callout>

## Custom Browser changes

<Callout icon="📘" theme="info">
  **Tip**: If the GMS provider is already updated or the host application handles it, PayU suggests you configure the following configuration so that CB OTP assists and SurePay can work on API 19.
</Callout>

```java Java
customBrowserConfig.setGmsProviderUpdatedStatus(CustomBrowserConfig.TRUE); //Default - CustomBrowserConfig.FALSE
```

If you do not handle the GMS Provider change, Google Chrome tabs will make payment for Android KitKat (API 19).
