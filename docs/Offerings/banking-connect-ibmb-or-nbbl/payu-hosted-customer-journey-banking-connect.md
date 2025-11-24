---
title: ' PayU Hosted Customer Journey - Banking Connect'
deprecated: false
hidden: true
metadata:
  robots: index
---
This section describes the customer journey for PayU Hosted integration on Desktop and Mobile devices.

## &#x20;Desktop

### QR Flow

1. Customer selects net banking on PayU Hosted Checkout (desktop)
2. PayU generates dynamic QR code via Banking Connect

<Image align="center" border={true} src="https://files.readme.io/c290c0a2e2e1f247046bbb2727d15edd3c392df8f0b533f8e6e10f6c635471b8-PayU_Hosted_web_QR_Step1.png" className="border" />

1. Customer scans QR with their mobile banking app

<Image align="center" border={true} src="https://files.readme.io/8370aa5e413bb879b168311f1d5f19b9d43b9efeb2be78996c2120dfd6b01b9f-PayU_Hosted_web_QR_Step2.png" className="border" />

1. Banking app decodes transaction details and initiates authentication
2. Payment completion with OTP/biometric verification on mobile
3. Real-time status update displayed on desktop merchant page

<Image align="center" border={true} src="https://files.readme.io/f4963eecea03132e3aaf4707a05bf8cda1a42202bf2ab3a6f6775aeb93451a50-PayU_Hosted_web_QR_Step3.png" className="border" />

### Redirect Flow

1. Customer chooses net banking payment option on desktop
2. PayU redirects to Banking Connect-managed bank pages
3. Customer login with banking credentials on desktop browser
4. Transaction completion on bank website interface
5. Automatic redirect back to merchant confirmation page
6. Transaction status displayed on desktop

## Mobile

### QR Flow

1. Customer accesses PayU Hosted Checkout on mobile browser
2. Banking Connect generates QR code optimized for mobile display

<Image align="center" border={false} src="https://files.readme.io/c482f64ed45db1bb90229403551a697527fa3379b205b4cf642e4dfea47da96c-PayU_Hosted_Mobile_QR_Step3.png" />

1. Customer switches to banking app to scan QR

<Image align="center" border={false} src="https://files.readme.io/01c3ca4d8fb6d0f34b0ca5b13de7b88f940b4e1a52d8b0555b28e0c2719b1307-PayU_Hosted_Mobile_QR_Step4.png" />

1. In-app transaction processing and authentication

<Image align="center" border={false} src="https://files.readme.io/3bac1e0b01559141d24552bfa35c1918b01874731323d73a42cc3c7ef9f213bf-PayU_Hosted_Mobile_QR_Step5.png" />

1. Return to mobile browser with completion status

<Image align="center" border={false} src="https://files.readme.io/24ba78402ed89163b6437a5544ac9fcfb34e5b804e2b5cbb43c0de01270dced3-PayU_Hosted_Mobile_QR_Step6.png" />

<br />

### App Intent Flow

1. Customer selects net banking on mobile browser/app
2. PayU creates intent URL for selected bank via Banking Connect
3. Automatic deep linking to banking app (Android/iOS)
4. Native in-app authentication and payment authorization
5. Instant callback to PayU mobile interface
6. Seamless transaction confirmation

### Mobile Desktop Compatibility

* Cross-platform session management between mobile and desktop
* QR codes generated on desktop can be scanned by mobile app
* Transaction status synchronization across device
* Unified merchant dashboard for multi-device transactions
