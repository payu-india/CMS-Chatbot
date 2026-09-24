---
title: ' PayU Hosted Customer Journey - Banking Connect'
deprecated: false
hidden: true
metadata:
  robots: index
---
This section describes the customer journey for PayU Hosted integration on Desktop and Mobile devices.

<Callout icon="📘" theme="info">
  ### Notes:

  * **Enable Banking Connect**: To enable Banking Connect or NBBL, contact your PayU Key Account Manager (KAM) or contact <Anchor target="_blank" href="https://help.payu.in">PayU Support.</Anchor>
  * **Collect customer mobile number**: For NBBL, you must collect the customer mobile number. For more information, refer to [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted) > [Web Integration](doc:web-integration-virtual-cards).
</Callout>

## &#x20;Desktop

### QR Flow

1. Customer selects net banking on PayU Hosted Checkout (desktop)
2. PayU generates dynamic QR code via Banking Connect

3) Customer scans QR with their mobile banking app

4. Banking app decodes transaction details and initiates authentication
5. Payment completion with OTP/biometric verification on mobile
6. Real-time status update displayed on desktop merchant page

![](https://files.readme.io/d55ade8734304dfb5a0ba1261c91d63f3f38735bb8267a3830006af08fee9475-PayU_Hosted_Web_Checkout_flow.png)

<br />

### Redirect Flow

1. Customer chooses net banking payment option on desktop
2. PayU redirects to Banking Connect-managed bank pages
3. Customer login with banking credentials on desktop browser
4. Transaction completion on bank website interface
5. Automatic redirect back to merchant confirmation page
6. Transaction status displayed on desktop

## Mobile

### App Intent Flow

1. Customer selects net banking on mobile browser/app

2) PayU creates intent URL for selected bank via Banking Connect

3. Automatic deep linking to banking app (Android/iOS)

4) Native in-app authentication and payment authorization

5. Instant callback to PayU mobile interface

6) Seamless transaction confirmation

![]()

<br />

### Mobile Desktop Compatibility

* Cross-platform session management between mobile and desktop
* QR codes generated on desktop can be scanned by mobile app
* Transaction status synchronization across device
* Unified merchant dashboard for multi-device transactions
