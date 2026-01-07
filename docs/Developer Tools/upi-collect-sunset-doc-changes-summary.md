---
title: UPI Collect Sunset - Doc Changes Summary
deprecated: false
hidden: true
metadata:
  robots: index
---
This document outlines the notes to be added to various PayU documentation pages regarding UPI Intent changes for different integration types.

***

## 1. PayU Hosted Checkout

**URL**: [https://docs.payu.in/docs/prebuilt-checkout-payu-hosted](https://docs.payu.in/docs/prebuilt-checkout-payu-hosted)

**File Path**: `docs/Collect Payments/introduction-web/prebuilt-checkout-payu-hosted/index.md`

**Content to add** (after the "How it works?" section):

<Callout icon="📘" theme="info">
  **Note for Mobile Apps using WebView**: If you are using PayU Hosted Checkout within a WebView inside your Android or iOS app, you must handle deeplink URL handling in your app. For implementation details, refer to [WebView for Mobile Apps](doc:webview-for-mobile-apps).
</Callout>


***

## 2. PayU Hosted Checkout Integration

**URL**: [https://docs.payu.in/docs/prebuilt-checkout-page-integration](https://docs.payu.in/docs/prebuilt-checkout-page-integration)

**File Path**: `docs/Collect Payments/introduction-web/prebuilt-checkout-payu-hosted/prebuilt-checkout-page-integration.md`

**Content to add** (in the prerequisites or integration steps section):

<Callout icon="📘" theme="info">
  **Note for Mobile Apps using WebView**: If you are using PayU Hosted Checkout within a WebView inside your Android or iOS app, you must handle deeplink URL handling in your app. For implementation details, refer to [WebView for Mobile Apps](doc:webview-for-mobile-apps).
</Callout>


***

## 3. UPI Integration (Merchant Hosted)

**URL**: [https://docs.payu.in/docs/collect-payments-with-upi-seamless](https://docs.payu.in/docs/collect-payments-with-upi-seamless)

**File Path**: `docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/collect-payments-with-upi-seamless.md`

**Content to add** (at the top of the page, after the introduction):

<Callout icon="⚠️" theme="warning">
  **Important UPI Integration Changes**:
  
  - **Seamless Form Post Users**: Merchants using Seamless Form Post flow must migrate to `txn_s2s_flow` (UPI Intent S2S), as Intent is **not supported** in the seamless form post flow for Android and Desktop web. For migration guidance, refer to [UPI Intent S2S Integration](doc:upi-intent-server-to-server).
  
  - **For Android Apps**: Merchants must implement the Smart Intent implementation. Refer to [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow) or use [PayU Android SDKs](doc:explore-android-sdks) which have Smart Intent built-in.
  
  - **For iOS Apps**: Merchants can implement the specific deeplink and continue using the UPI Collect flow as is.
  
  - **For Web**: Merchants must use the deeplink created via [UPI Intent S2S Integration](doc:upi-intent-server-to-server) to generate a QR code of the deeplink, instead of the UPI Collect flow.
</Callout>


***

## 4. Merchant Hosted Checkout Overview

**URL**: [https://docs.payu.in/docs/custom-checkout-merchant-hosted](https://docs.payu.in/docs/custom-checkout-merchant-hosted)

**File Path**: `docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/index.md`

**Content to add** (in the UPI section or at the top):


<Callout icon="⚠️" theme="warning">
  **Important UPI Integration Changes for Merchant Hosted Checkout**:
  
  For Merchant Hosted integrations using `txn_s2s_flow = 2` or `txn_s2s_flow = 4`:
  
  - **For Android Apps**: Merchants must implement the Smart Intent implementation in the app. Refer to [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow) or use [PayU Android SDKs](doc:explore-android-sdks) which have Smart Intent built-in.
  
  - **For iOS Apps**: Merchants can implement the specific deeplink and continue using the UPI Collect flow as is.
  
  - **For Web**: Merchants must use the deeplink created via [UPI Intent S2S Integration](doc:upi-intent-server-to-server) to generate a QR code of the deeplink, instead of the UPI Collect flow.
  
  - **Seamless Form Post**: Merchants must migrate to `txn_s2s_flow` (UPI Intent S2S), as Intent is not supported in the seamless form post flow for Android and Desktop web.
</Callout>


***

## 5. UPI Intent S2S Integration

**URL**: [https://docs.payu.in/docs/upi-intent-server-to-server](https://docs.payu.in/docs/upi-intent-server-to-server)

**File Path**: `docs/Collect Payments/introduction-web/server-to-server-integration/upi-intent-server-to-server.md`

**Content to add** (after the introduction/cards section):


<Callout icon="📘" theme="info">
  **Platform-Specific Implementation Notes**:
  
  - **For Android Apps**: Merchants must implement the Smart Intent implementation. Refer to [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow) for non-SDK implementation, or use [PayU Android SDKs](doc:explore-android-sdks) which have Smart Intent built-in.
  
  - **For iOS Apps**: Merchants can implement the specific deeplink handling and continue using the UPI flow as is. Refer to [iOS UPI SDK](doc:ios-upi-sdk) for SDK-based implementation.
  
  - **For Web**: Use the deeplink returned in the API response to generate a QR code that customers can scan with their UPI app.
</Callout>

<Callout icon="👍" theme="okay">
  **Recommended**: For easier integration with built-in Smart Intent support, use PayU SDKs:
  
  - [Android Mobile SDKs](doc:explore-android-sdks)
  - [iOS Mobile SDKs](doc:explore-ios-sdks)
</Callout>


***

## 6. UPI Collection S2S Integration

**URL**: [https://docs.payu.in/docs/upi-collection-s2s](https://docs.payu.in/docs/upi-collection-s2s)

**File Path**: `docs/Collect Payments/introduction-web/server-to-server-integration/upi-collection-s2s.md`

**Content to add** (after the introduction):


<Callout icon="⚠️" theme="warning">
  **Important**: For Android and Desktop web, UPI Collect flow has limitations. Consider migrating to UPI Intent S2S for better user experience:
  
  - **For Android Apps**: Implement Smart Intent using [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow) or use [PayU Android SDKs](doc:explore-android-sdks).
  
  - **For Web**: Use [UPI Intent S2S Integration](doc:upi-intent-server-to-server) to generate a QR code of the deeplink for better conversion.
  
  - **For iOS Apps**: You can continue using the UPI Collect flow as is, or implement deeplink handling.
</Callout>
```


## 7. S2S Integration Overview

**URL**: [https://docs.payu.in/docs/server-to-server-integration](https://docs.payu.in/docs/server-to-server-integration)

**File Path**: `docs/Collect Payments/introduction-web/server-to-server-integration/index.md`

**Content to add** (in the UPI Server-to-Server Integration section):


<Callout icon="👍" theme="okay">
  **Recommended for Mobile Apps**: For Android and iOS apps, consider using PayU SDKs which have Smart Intent implementation built-in for higher success rates:
  
  - [Android Mobile SDKs](doc:explore-android-sdks)
  - [iOS Mobile SDKs](doc:explore-ios-sdks)
</Callout>


***

## 8. UPI Smart Intent - Non SDK Flow

**URL**: [https://docs.payu.in/docs/upi-smart-intent-non-sdk-flow](https://docs.payu.in/docs/upi-smart-intent-non-sdk-flow)

**File Path**: `docs/Collect Payments/explore-server-integrations/upi-smart-intent-non-sdk-flow.md`

**Content to add** (at the top of the page):


<Callout icon="👍" theme="okay">
  **Recommended**: For easier integration, merchants can use PayU SDKs for Android and iOS, which have the Smart Intent implementation built-in:
  
  - [Android UPI SDK](doc:android-upi-sdk) - Supports Collect, Intent, and In-App flows with Smart Intent
  - [Android CheckoutPro SDK](doc:android-checkoutpro-sdk) - Complete checkout solution with Smart Intent
  - [iOS UPI SDK](doc:ios-upi-sdk) - Supports Intent and Collect payments
  - [iOS CheckoutPro SDK](doc:ios-checkoutpro-sdk) - Complete checkout solution for iOS
</Callout>


***

## Summary Table

| # | Page                              | URL                                                                                                                          | File Path                                                                                                      | Note Type                               |
| - | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| 1 | PayU Hosted Checkout              | [https://docs.payu.in/docs/prebuilt-checkout-payu-hosted](https://docs.payu.in/docs/prebuilt-checkout-payu-hosted)           | `docs/Collect Payments/introduction-web/prebuilt-checkout-payu-hosted/index.md`                                | WebView handling note                   |
| 2 | PayU Hosted Checkout Integration  | [https://docs.payu.in/docs/prebuilt-checkout-page-integration](https://docs.payu.in/docs/prebuilt-checkout-page-integration) | `docs/Collect Payments/introduction-web/prebuilt-checkout-payu-hosted/prebuilt-checkout-page-integration.md`   | WebView handling note                   |
| 3 | UPI Integration (Merchant Hosted) | [https://docs.payu.in/docs/collect-payments-with-upi-seamless](https://docs.payu.in/docs/collect-payments-with-upi-seamless) | `docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/collect-payments-with-upi-seamless.md` | Smart Intent + Form Post migration note |
| 4 | Merchant Hosted Checkout Overview | [https://docs.payu.in/docs/custom-checkout-merchant-hosted](https://docs.payu.in/docs/custom-checkout-merchant-hosted)       | `docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/index.md`                              | Smart Intent + platform-specific notes  |
| 5 | UPI Intent S2S Integration        | [https://docs.payu.in/docs/upi-intent-server-to-server](https://docs.payu.in/docs/upi-intent-server-to-server)               | `docs/Collect Payments/introduction-web/server-to-server-integration/upi-intent-server-to-server.md`           | Platform-specific + SDK recommendation  |
| 6 | UPI Collection S2S Integration    | [https://docs.payu.in/docs/upi-collection-s2s](https://docs.payu.in/docs/upi-collection-s2s)                                 | `docs/Collect Payments/introduction-web/server-to-server-integration/upi-collection-s2s.md`                    | Migration recommendation note           |
| 7 | S2S Integration Overview          | [https://docs.payu.in/docs/server-to-server-integration](https://docs.payu.in/docs/server-to-server-integration)             | `docs/Collect Payments/introduction-web/server-to-server-integration/index.md`                                 | SDK recommendation                      |
| 8 | UPI Smart Intent - Non SDK Flow   | [https://docs.payu.in/docs/upi-smart-intent-non-sdk-flow](https://docs.payu.in/docs/upi-smart-intent-non-sdk-flow)           | `docs/Collect Payments/explore-server-integrations/upi-smart-intent-non-sdk-flow.md`                           | SDK recommendation                      |

***

## Integration Types Overview

| Integration Type                                    | Changes Required                                       |
| --------------------------------------------------- | ------------------------------------------------------ |
| **PayU Hosted Checkout**                            | No changes required for merchants                      |
| **PayU Hosted Checkout with WebView (Android App)** | Merchants must handle deeplink URL handling in the app |
| **Merchant Hosted (txn_s2s_flow = 2/4) - Android**  | Implement Smart Intent in the app                      |
| **Merchant Hosted (txn_s2s_flow = 2/4) - iOS**      | Implement specific deeplink, continue with UPI Collect |
| **Merchant Hosted (txn_s2s_flow = 2/4) - Web**      | Use UPI Intent S2S deeplink to generate QR code        |
| **Merchant Hosted (Seamless Form Post)**            | Migrate to txn_s2s_flow (UPI Intent S2S)               |
| **PayU SDKs (Android/iOS)**                         | Smart Intent implementation built-in                   |
