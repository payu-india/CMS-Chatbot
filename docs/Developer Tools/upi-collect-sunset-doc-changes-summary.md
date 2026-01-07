---
title: UPI Collect Sunset - Doc Changes Summary
deprecated: false
hidden: true
metadata:
  robots: index
---
Here's the detailed content to be added to each page:

### PayU Hosted Checkout
URL: https://docs.payu.in/docs/prebuilt-checkout-payu-hosted
Content to add (after the "How it works?" section):
<Callout icon="📘" theme="info">  **Note for Mobile Apps using WebView**: If you are using PayU Hosted Checkout within a WebView inside your Android or iOS app, you must handle deeplink URL handling in your app. For implementation details, refer to [WebView for Mobile Apps](doc:webview-for-mobile-apps).</Callout>

### PayU Hosted Checkout Integration
URL: https://docs.payu.in/docs/prebuilt-checkout-page-integration
Content to add (in the prerequisites or integration steps section):
<Callout icon="📘" theme="info">  **Note for Mobile Apps using WebView**: If you are using PayU Hosted Checkout within a WebView inside your Android or iOS app, you must handle deeplink URL handling in your app. For implementation details, refer to [WebView for Mobile Apps](doc:webview-for-mobile-apps).</Callout>

### UPI Integration (Merchant Hosted)
URL: https://docs.payu.in/docs/collect-payments-with-upi-seamless
Content to add (at the top of the page, after the introduction):
<Callout icon="⚠️" theme="warning">  **Important UPI Integration Changes**:    - **Seamless Form Post Users**: Merchants using Seamless Form Post flow must migrate to `txn_s2s_flow` (UPI Intent S2S), as Intent is **not supported** in the seamless form post flow for Android and Desktop web. For migration guidance, refer to [UPI Intent S2S Integration](doc:upi-intent-server-to-server).    - **For Android Apps**: Merchants must implement the Smart Intent implementation. Refer to [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow) or use [PayU Android SDKs](doc:explore-android-sdks) which have Smart Intent built-in.    - **For iOS Apps**: Merchants can implement the specific deeplink and continue using the UPI Collect flow as is.    - **For Web**: Merchants must use the deeplink created via [UPI Intent S2S Integration](doc:upi-intent-server-to-server) to generate a QR code of the deeplink, instead of the UPI Collect flow.</Callout>

### Merchant Hosted Checkout Overview
URL: https://docs.payu.in/docs/custom-checkout-merchant-hosted
Content to add (in the UPI section or at the top):
<Callout icon="⚠️" theme="warning">  **Important UPI Integration Changes for Merchant Hosted Checkout**:    For Merchant Hosted integrations using `txn_s2s_flow = 2` or `txn_s2s_flow = 4`:    - **For Android Apps**: Merchants must implement the Smart Intent implementation in the app. Refer to [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow) or use [PayU Android SDKs](doc:explore-android-sdks) which have Smart Intent built-in.    - **For iOS Apps**: Merchants can implement the specific deeplink and continue using the UPI Collect flow as is.    - **For Web**: Merchants must use the deeplink created via [UPI Intent S2S Integration](doc:upi-intent-server-to-server) to generate a QR code of the deeplink, instead of the UPI Collect flow.    - **Seamless Form Post**: Merchants must migrate to `txn_s2s_flow` (UPI Intent S2S), as Intent is not supported in the seamless form post flow for Android and Desktop web.</Callout>

### UPI Intent S2S Integration
URL: https://docs.payu.in/docs/upi-intent-server-to-server
Content to add (after the introduction/cards section):
<Callout icon="📘" theme="info">  **Platform-Specific Implementation Notes**:    - **For Android Apps**: Merchants must implement the Smart Intent implementation. Refer to [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow) for non-SDK implementation, or use [PayU Android SDKs](doc:explore-android-sdks) which have Smart Intent built-in.    - **For iOS Apps**: Merchants can implement the specific deeplink handling and continue using the UPI flow as is. Refer to [iOS UPI SDK](doc:ios-upi-sdk) for SDK-based implementation.    - **For Web**: Use the deeplink returned in the API response to generate a QR code that customers can scan with their UPI app.</Callout><Callout icon="👍" theme="okay">  **Recommended**: For easier integration with built-in Smart Intent support, use PayU SDKs:    - [Android Mobile SDKs](doc:explore-android-sdks)  - [iOS Mobile SDKs](doc:explore-ios-sdks)</Callout>

### UPI Collection S2S Integration
URL: https://docs.payu.in/docs/upi-collection-s2s
Content to add (after the introduction):
<Callout icon="⚠️" theme="warning">  **Important**: For Android and Desktop web, UPI Collect flow has limitations. Consider migrating to UPI Intent S2S for better user experience:    - **For Android Apps**: Implement Smart Intent using [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow) or use [PayU Android SDKs](doc:explore-android-sdks).    - **For Web**: Use [UPI Intent S2S Integration](doc:upi-intent-server-to-server) to generate a QR code of the deeplink for better conversion.    - **For iOS Apps**: You can continue using the UPI Collect flow as is, or implement deeplink handling.</Callout>

### S2S Integration Overview
URL: https://docs.payu.in/docs/server-to-server-integration
Content to add (in the UPI Server-to-Server Integration section):
<Callout icon="👍" theme="okay">  **Recommended for Mobile Apps**: For Android and iOS apps, consider using PayU SDKs which have Smart Intent implementation built-in for higher success rates:    - [Android Mobile SDKs](doc:explore-android-sdks)  - [iOS Mobile SDKs](doc:explore-ios-sdks)</Callout>

### UPI Smart Intent - Non SDK Flow
URL: https://docs.payu.in/docs/upi-smart-intent-non-sdk-flow
Content to add (at the top of the page):
<Callout icon="👍" theme="okay">  **Recommended**: For easier integration, merchants can use PayU SDKs for Android and iOS, which have the Smart Intent implementation built-in:    - [Android UPI SDK](doc:android-upi-sdk) - Supports Collect, Intent, and In-App flows with Smart Intent  - [Android CheckoutPro SDK](doc:android-checkoutpro-sdk) - Complete checkout solution with Smart Intent  - [iOS UPI SDK](doc:ios-upi-sdk) - Supports Intent and Collect payments  - [iOS CheckoutPro SDK](doc:ios-checkoutpro-sdk) - Complete checkout solution for iOS</Callout>


